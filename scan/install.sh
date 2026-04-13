#!/bin/bash

echo "[+] Installing dependencies..."
sudo apt update
sudo apt install -y nmap python3

echo "[+] Installing secscan command..."

SCRIPT_DIR=$(pwd)/scan

chmod +x "$SCRIPT_DIR/secscan"

cat <<EOF | sudo tee /usr/local/bin/secscan > /dev/null
#!/bin/bash
cd $SCRIPT_DIR
python3 main.py "\$@"
EOF

sudo chmod +x /usr/local/bin/secscan

echo "[+] Done!"
echo "Run with: secscan"
