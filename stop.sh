#!/bin/bash

echo "🛑 Stopping all background services..."

# Kill processes by command match
PIDS=$(ps aux | grep -E 'zookeeper|kafka-server|producer_news.py|consumer_news.py|streamlit|airflow webserver|airflow scheduler' | grep -v grep | awk '{print $2}')

if [ -z "$PIDS" ]; then
    echo "✅ No matching services found running."
else
    echo "🔍 Found processes:"
    ps -fp $PIDS
    echo "❌ Killing..."
    kill -9 $PIDS
    echo "✅ All services stopped."
fi

