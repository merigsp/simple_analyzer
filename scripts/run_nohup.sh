mkdir -p ../logs

nohup python3 ../simple_analyzer/main.py > ../logs/output.log 2>&1 &

echo $! > ../logs/main.pid

echo "Program is running in the background. PID: $(cat ../logs/main.pid)"
