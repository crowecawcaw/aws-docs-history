# Migrate your OpenSSL Dynamic Engine from AWS CloudHSM Client SDK 3 to
 Client SDK 5

Use this topic to migrate your [OpenSSL Dynamic Engine](openssl-library.md "openssl-library.md") from AWS CloudHSM
 Client SDK 3 to Client SDK 5. For benefits on migrating, see [Benefits of AWS CloudHSM Client SDK 5](client-sdk-5-benefits.md "client-sdk-5-benefits.md").

In AWS CloudHSM, customer applications perform cryptographic operations using the AWS CloudHSM Client Software Development Kit (SDK).
 Client SDK 5 is the primary SDK that continues to have new features and platform support added to it.

###### Note

Random number generation is not currently supported in Client SDK 5 with OpenSSL Dynamic Engine.

To review migration instructions for all providers, see [Migrating from AWS CloudHSM Client SDK 3 to
 Client SDK 5](client-sdk-migration.md "client-sdk-migration.md").


## Migrate to Client SDK 5


Follow the instructions in this section to migrate from Client SDK 3 to Client SDK 5.


###### Note

Amazon Linux, Ubuntu 16.04, Ubuntu 18.04, CentOS 6, CentOS 8, and RHEL 6 are not currently supported with Client SDK 5. 
 If you are currently using one of these platforms with Client SDK 3, you will need to choose a different platform when migrating to Client SDK 5.


1. Uninstall the OpenSSL Dynamic Engine for Client SDK 3.



Amazon Linux 2

```
`$` `sudo yum remove cloudhsm-client-dyn`
```


CentOS 7

```
`$` `sudo yum remove cloudhsm-client-dyn`
```


RHEL 7

```
`$` `sudo yum remove cloudhsm-client-dyn`
```


RHEL 8

```
`$` `sudo yum remove cloudhsm-client-dyn`
```


Ubuntu 16.04 LTS

```
`$` `sudo apt remove cloudhsm-client-dyn`
```


Ubuntu 18.04 LTS

```
`$` `sudo apt remove cloudhsm-client-dyn`
```
2. Stop the Client Daemon for Client SDK 3.



Amazon Linux 2

```
`$` `sudo service cloudhsm-client stop`
```


CentOS 7

```
`$` `sudo service cloudhsm-client stop`
```


RHEL 7

```
`$` `sudo service cloudhsm-client stop`
```


RHEL 8

```
`$` `sudo service cloudhsm-client stop`
```


Ubuntu 16.04 LTS

```
`$` `sudo systemctl stop cloudhsm-client`
```


Ubuntu 18.04 LTS

```
`$` `sudo systemctl stop cloudhsm-client`
```
3. Uninstall the Client Daemon for Client SDK 3.



Amazon Linux 2

```
`$` `sudo yum remove cloudhsm-client`
```


CentOS 7

```
`$` `sudo yum remove cloudhsm-client`
```


RHEL 7

```
`$` `sudo yum remove cloudhsm-client`
```


RHEL 8

```
`$` `sudo yum remove cloudhsm-client`
```


Ubuntu 16.04 LTS

```
`$` `sudo apt remove cloudhsm-client`
```


Ubuntu 18.04 LTS

```
`$` `sudo apt remove cloudhsm-client`
```



###### Note

Custom configurations need to be enabled again.
4. Install the Client SDK OpenSSL Dynamic Engine by following the steps in [Install the OpenSSL Dynamic Engine for AWS CloudHSM
 Client SDK 5](openssl5-install.md "openssl5-install.md").
5. Client SDK 5 introduces a new configuration file format and command-line bootstrapping tool. To bootstrap your Client SDK 5 OpenSSL Dynamic Engine, follow the instructions listed in the user guide under 
 [Bootstrap the Client SDK](cluster-connect.md#connect-how-to "cluster-connect.md#connect-how-to").
6. In your development environment, test your application. Make updates to your existing code to resolve your breaking changes before your final migration.

## Related topics



* [Best practices for AWS CloudHSM](best-practices.md "best-practices.md")
