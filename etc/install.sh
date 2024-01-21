set -x

cd /etc/systemd/system 
sudo rm llminstance.service
sudo ln -s ~/llminstance/etc/llminstance.service llminstance.service

sudo systemctl enable llminstance.service

