# Clear the limit values of limits.conf file

exec { 'Change Limit config':
command => 'sed -i "s/holberton/# holberton/g" /etc/security/limits.conf',
path    => '/usr/bin',
}