# Install and configure a nginx server


package {'nginx':
  ensure  => 'present',
}

exec {'install':
  command  => 'sudo apt update ; sudo apt install nginx -y',
  provider => 'shell',
}

exec {'Greet':
  command  => "echo 'Hello World!' | sudo tee /var/www/html/index.html",
  provider => 'shell',
}

exec {'Redirect':
  command  => "sudo sed -i 's/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/MikeRock51 permanent;/'
   /etc/nginx/sites-available/default",
  provider => 'shell',
}

exec {'404 Page':
  command  => "echo \"Ceci n'est pas une page\" | sudo tee /usr/share/nginx/html/404.html"
  provider => 'shell',
}

exec {'Redirect 404':
  command  => "sudo sed -i 's/listen 80 default_server;/listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html
   {\n\t root \/usr\/share\/nginx\/html;\n\t internal;\n\t}/' /etc/nginx/sites-enabled/default",
  provider => 'shell',
}

exec {'Restart nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
