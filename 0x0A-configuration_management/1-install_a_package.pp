# install Puppet-lint with script
package { 'puppet-lint':
	ensure   => '2.1.1',
	provider => 'gem',
}