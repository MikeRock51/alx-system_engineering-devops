# Sets up an SSH configuration file

exec {
  'echo "PasswordAuthentication no\n IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
  path    => '/bin/'
}
