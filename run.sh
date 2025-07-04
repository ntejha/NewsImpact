#!/bin/bash

PROJECT_DIR=$(pwd)
KAFKA_DIR="/home/tejhanagarajan/kafka_2.12-3.7.0"
VENV_PATH="$PROJECT_DIR/venv"
LOG_DIR="$PROJECT_DIR/logs"

mkdir -p "$LOG_DIR"

source "$VENV_PATH/bin/activate"

start_service() {
    echo "▶️ Starting $1..."
    eval "$2 > \"$LOG_DIR/$1.log\" 2>&1 &"
    sleep 2
    echo "✅ $1 started."
}

start_service "Zookeeper" "$KAFKA_DIR/bin/zookeeper-server-start.sh $KAFKA_DIR/config/zookeeper.properties"
start_service "Kafka Broker" "$KAFKA_DIR/bin/kafka-server-start.sh $KAFKA_DIR/config/server.properties"
start_service "Producer" "cd $PROJECT_DIR && source $VENV_PATH/bin/activate && python streaming/producer_news.py"
start_service "Consumer" "cd $PROJECT_DIR && source $VENV_PATH/bin/activate && python streaming/consumer_news.py"
start_service "Streamlit Dashboard" "cd $PROJECT_DIR && source $VENV_PATH/bin/activate && streamlit run dashboard/app.py --server.headless true --server.port 8501"
start_service "Airflow Scheduler" "cd $PROJECT_DIR && source $VENV_PATH/bin/activate && airflow scheduler"
start_service "Airflow Webserver" "cd $PROJECT_DIR && source $VENV_PATH/bin/activate && airflow webserver --port 8080"

echo "🚀 All services are now running in the background."
echo "📂 Logs are available in: $LOG_DIR"
