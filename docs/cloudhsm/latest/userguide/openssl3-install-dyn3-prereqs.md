# Prerequisites for OpenSSL Dynamic Engine with AWS CloudHSM
 Client SDK 3

For information about platform support, see [AWS CloudHSM Client SDK 3 supported platforms](sdk3-support.md "sdk3-support.md").

Before you can use the AWS CloudHSM dynamic engine for OpenSSL with Client SDK 3, you need the
 AWS CloudHSM client. 

The client is a daemon that establishes end-to-end encrypted communication with the HSMs
 in your cluster, and the OpenSSL engine communicates locally with the client. To install and
 configure the AWS CloudHSM client, see [Install the client
 (Linux)](cmu-install-and-configure-client-linux.md "cmu-install-and-configure-client-linux.md"). Then use the following command
 to start it. 


Amazon Linux
```
`$` `sudo start cloudhsm-client`
```

Amazon Linux 2
```
`$` `sudo systemctl cloudhsm-client start`
```

CentOS 6

```
`$` `sudo systemctl start cloudhsm-client`
```


CentOS 7

```
`$` `sudo systemctl cloudhsm-client start`
```


RHEL 6

```
`$` `sudo systemctl start cloudhsm-client`
```


RHEL 7

```
`$` `sudo systemctl cloudhsm-client start`
```


Ubuntu 16.04 LTS
```
`$` `sudo systemctl cloudhsm-client start`
```
