# Practice with puppet to change the ssh client config

file_line { 'sudo pwd authentication' :
  path    =>  '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
  }
file_line { 'sudo identity file' :
  path    =>  '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
  replace => true,
  }