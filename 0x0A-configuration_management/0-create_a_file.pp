# Script to create a new file with puppet
file { '/tmp/holberton':
ensure => file,
path   => '/tmp/holberton',
owner  => 'www-data',
group  => 'www-data',
mode   => '0744',
contet => 'I love Puppet',
}