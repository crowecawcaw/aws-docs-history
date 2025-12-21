# Installing the ElastiCache cluster client for PHP

This section describes how to install, update, and remove the PHP components for the ElastiCache Cluster Client on Amazon EC2 instances.
For more information about Auto Discovery,
see [Automatically identify nodes in your cluster (Memcached)](AutoDiscovery.md "AutoDiscovery.md"). For
sample PHP code to use the client.
see [Using the ElastiCache Cluster Client for PHP](AutoDiscovery.Using.ModifyApp.md "AutoDiscovery.Using.ModifyApp.md").

###### Topics

- [Downloading the installation package](Appendix.PHPAutoDiscoverySetup.md "Appendix.PHPAutoDiscoverySetup.md")
- [For users who already have php-memcached extension installed](#Appendix.PHPAutoDiscoverySetup.InstallingExisting "#Appendix.PHPAutoDiscoverySetup.InstallingExisting")
- [Installation steps for new users](Appendix.PHPAutoDiscoverySetup.md "Appendix.PHPAutoDiscoverySetup.md")
- [Removing the PHP cluster client](Appendix.PHPAutoDiscoverySetup.md "Appendix.PHPAutoDiscoverySetup.md")

## For users who already have _php-memcached_ extension installed

###### To update the `php-memcached` installation

1. Remove the previous installation of the Memcached extension for PHP
   as described by the topic [Removing the PHP cluster client](Appendix.PHPAutoDiscoverySetup.md "Appendix.PHPAutoDiscoverySetup.md").
2. Install the new ElastiCache `php-memcached` extension as described previously in
   [Installation steps for new users](Appendix.PHPAutoDiscoverySetup.md "Appendix.PHPAutoDiscoverySetup.md").
