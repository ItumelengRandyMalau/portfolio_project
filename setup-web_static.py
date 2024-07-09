#!/bin/bash

# Update package list and install Nginx if it is not already installed
if ! which nginx > /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Web Static Test
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link, remove if it already exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
NGINX_CONFIG="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$NGINX_CONFIG"; then
    sudo sed -i '/server_name _;/a \
    location /hbnb_static/ { \
        alias /data/web_static/current/; \
    }' "$NGINX_CONFIG"
fi

# Restart Nginx to apply the changes
sudo service nginx restart

echo "Web server setup complete!"

