import json
import os
from datetime import datetime
from pathlib import Path

class ToolAnalytics:
    """Track tool usage analytics"""
    
    def __init__(self):
        self.analytics_file = Path("tool_usage_analytics.json")
        self.load_analytics()
    
    def load_analytics(self):
        """Load existing analytics or create new"""
        if self.analytics_file.exists():
            with open(self.analytics_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "total_calls": 0,
                "tools": {
                    "polygon_api": {"calls": 0, "last_used": None},
                    "retriever": {"calls": 0, "last_used": None},
                    "tavily_search": {"calls": 0, "last_used": None},
                    "bing_search": {"calls": 0, "last_used": None}
                },
                "sessions": []
            }
    
    def log_tool_usage(self, tool_name, query):
        """Log when a tool is used"""
        timestamp = datetime.now().isoformat()
        
        # Update tool-specific stats
        if tool_name in self.data["tools"]:
            self.data["tools"][tool_name]["calls"] += 1
            self.data["tools"][tool_name]["last_used"] = timestamp
        
        # Update total calls
        self.data["total_calls"] += 1
        
        # Add to session log
        self.data["sessions"].append({
            "tool": tool_name,
            "query": query[:100],  # Truncate for privacy
            "timestamp": timestamp
        })
        
        # Keep only last 100 sessions
        if len(self.data["sessions"]) > 100:
            self.data["sessions"] = self.data["sessions"][-100:]
        
        self.save_analytics()
    
    def save_analytics(self):
        """Save analytics to file"""
        with open(self.analytics_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_stats(self):
        """Get usage statistics"""
        return {
            "total_calls": self.data["total_calls"],
            "polygon_api_calls": self.data["tools"]["polygon_api"]["calls"],
            "retriever_calls": self.data["tools"]["retriever"]["calls"],
            "tavily_calls": self.data["tools"]["tavily_search"]["calls"],
            "bing_calls": self.data["tools"]["bing_search"]["calls"],
            "last_session": self.data["sessions"][-1] if self.data["sessions"] else None
        }
    
    def print_stats(self):
        """Print usage statistics to console"""
        stats = self.get_stats()
        print("\n" + "="*50)
        print("📊 TOOL USAGE ANALYTICS")
        print("="*50)
        print(f"Total Tool Calls: {stats['total_calls']}")
        print(f"🚀 Polygon API: {stats['polygon_api_calls']} calls")
        print(f"🔍 Retriever: {stats['retriever_calls']} calls") 
        print(f"🌐 Tavily Search: {stats['tavily_calls']} calls")
        print(f"🔍 Bing Search: {stats['bing_calls']} calls")
        if stats['last_session']:
            print(f"Last Used: {stats['last_session']['tool']} at {stats['last_session']['timestamp']}")
        print("="*50 + "\n")

# Global analytics instance
analytics = ToolAnalytics() 