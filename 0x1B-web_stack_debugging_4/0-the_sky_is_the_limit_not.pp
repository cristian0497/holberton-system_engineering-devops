# script to add more worker process to nginx .conf file and restart service

exec { 'sed command':
command => 'sudo sed -i "5 s/[0-9]\+/$(ulimit -n)/" /etc/default/nginx; sudo service nginx restart',
path    => ['/usr/bin/', '/usr/sbin'],
}
exec { 'nginx restart':
command => 'sudo service nginx restart',
path    => '/usr/bin/',
}
