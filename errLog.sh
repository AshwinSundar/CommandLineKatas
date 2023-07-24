touch errLog.txt
echo "$(date +"%Y-%m-%d %H:%M:%S") $1" | cat - errLog.txt > temp && mv temp errLog.txt
