# Example AWS Managed Microsoft AD over LDAP(S) cluster

configurations

AWS ParallelCluster supports multiple user access by integrating with an AWS Directory Service over the Lightweight Directory Access
Protocol (LDAP), or LDAP over TLS/SSL (LDAPS).

The following examples show how to create cluster configurations to integrate with an
AWS Managed Microsoft AD over LDAP(S).

You can use this example to integrate your cluster with an AWS Managed Microsoft AD over LDAPS,
with certificate verification.

###### Specific definitions for an AWS Managed Microsoft AD over LDAPS with certificates

configuration:

- [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [LdapTlsReqCert](DirectoryService-v3.md#yaml-DirectoryService-LdapTlsReqCert "DirectoryService-v3.md#yaml-DirectoryService-LdapTlsReqCert")
  must be set to `hard` (default) for LDAPS with certificate
  verification.
- [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [LdapTlsCaCert](DirectoryService-v3.md#yaml-DirectoryService-LdapTlsCaCert "DirectoryService-v3.md#yaml-DirectoryService-LdapTlsCaCert") must
  specify the path to your certificate of authority (CA) certificate.

The CA certificate is a certificate bundle that contains the certificates of the
entire CA chain that issued certificates for the AD domain controllers.

Your CA certificate and certificates must be installed on the cluster
nodes.

- Controllers hostnames must be specified for [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainAddr](DirectoryService-v3.md#yaml-DirectoryService-DomainAddr "DirectoryService-v3.md#yaml-DirectoryService-DomainAddr"), not IP
  addresses.
- [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainReadOnlyUser](DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser "DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser") syntax must be as follows:

```
cn=ReadOnly,ou=Users,ou=CORP,dc=`corp`,dc=`example`,dc=`com`
```

**Example cluster configuration file for using AD over
LDAPS:**

```
Region: region-id
Image:
  Os: alinux2
HeadNode:
  InstanceType: t2.micro
  Networking:
    SubnetId: subnet-1234567890abcdef0
  Ssh:
    KeyName: pcluster
  Iam:
    AdditionalIamPolicies:
      - Policy: arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
  CustomActions:
    OnNodeConfigured:
      Script: s3://&example-s3-bucket;/scripts/pcluster-dub-msad-ldaps.post.sh
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: queue1
      ComputeResources:
        - Name: t2micro
          InstanceType: t2.micro
          MinCount: 1
          MaxCount: 10
      Networking:
        SubnetIds:
          - subnet-abcdef01234567890
      Iam:
        AdditionalIamPolicies:
          - Policy: arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
      CustomActions:
        OnNodeConfigured:
          Script: s3://&example-s3-bucket;/scripts/pcluster-dub-msad-ldaps.post.sh
DirectoryService:
  DomainName: dc=corp,dc=example,dc=com
  DomainAddr: ldaps://win-abcdef01234567890.corp.example.com,ldaps://win-abcdef01234567890.corp.example.com
  PasswordSecretArn: arn:aws:secretsmanager:region-id:123456789012:secret:MicrosoftAD.Admin.Password-1234
  DomainReadOnlyUser: cn=ReadOnly,ou=Users,ou=CORP,dc=corp,dc=example,dc=com
  LdapTlsCaCert: /etc/openldap/cacerts/corp.example.com.bundleca.cer
  LdapTlsReqCert: hard
```

**Add certificates and configure domain controllers in post
install script:**

```
*#!/bin/bash*
set -e

AD_CERTIFICATE_S3_URI="s3://`amzn-s3-demo-bucket`/bundle/corp.example.com.bundleca.cer"
AD_CERTIFICATE_LOCAL="/etc/openldap/cacerts/corp.example.com.bundleca.cer"

AD_HOSTNAME_1="win-abcdef01234567890.corp.example.com"
AD_IP_1="192.0.2.254"

AD_HOSTNAME_2="win-abcdef01234567890.corp.example.com"
AD_IP_2="203.0.113.225"

# Download CA certificate
mkdir -p $(dirname "${AD_CERTIFICATE_LOCAL}")
aws s3 cp "${AD_CERTIFICATE_S3_URI}" "${AD_CERTIFICATE_LOCAL}"
chmod 644 "${AD_CERTIFICATE_LOCAL}"

# Configure domain controllers reachability
echo "${AD_IP_1} ${AD_HOSTNAME_1}" >> /etc/hosts
echo "${AD_IP_2} ${AD_HOSTNAME_2}" >> /etc/hosts
```

**You can retrieve the domain controllers hostnames from instances
joined to the domain as shown in the following examples.**

**From Windows instance**

```
`$` `nslookup `192.0.2.254``
```

```
`Server: corp.example.com
Address: 192.0.2.254

Name: win-abcdef01234567890.corp.example.com
Address: 192.0.2.254`
```

**From Linux instance**

```
`$` `nslookup `192.0.2.254``
```

```
`192.0.2.254.in-addr.arpa name = corp.example.com
192.0.2.254.in-addr.arpa name = win-abcdef01234567890.corp.example.com`
```

You can use this example to integrate your cluster with an AWS Managed Microsoft AD over LDAPS,
without certificate verification.

**Specific definitions for an AWS Managed Microsoft AD over LDAPS without
certificate verification configuration:**

- [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [LdapTlsReqCert](DirectoryService-v3.md#yaml-DirectoryService-LdapTlsReqCert "DirectoryService-v3.md#yaml-DirectoryService-LdapTlsReqCert")
  must be set to `never`.
- Either controller hostnames or IP addresses can be specified for [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainAddr](DirectoryService-v3.md#yaml-DirectoryService-DomainAddr "DirectoryService-v3.md#yaml-DirectoryService-DomainAddr").
- [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainReadOnlyUser](DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser "DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser") syntax must be as follows:

```
cn=ReadOnly,ou=Users,ou=CORP,dc=`corp`,dc=`example`,dc=`com`
```

**Example cluster configuration file for using AWS Managed Microsoft AD over
LDAPS without certificate verification:**

```
Region: region-id
Image:
  Os: alinux2
HeadNode:
  InstanceType: t2.micro
  Networking:
    SubnetId: subnet-1234567890abcdef0
  Ssh:
    KeyName: pcluster
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: queue1
      ComputeResources:
        - Name: t2micro
          InstanceType: t2.micro
          MinCount: 1
          MaxCount: 10
      Networking:
        SubnetIds:
          - subnet-abcdef01234567890
DirectoryService:
  DomainName: dc=corp,dc=example,dc=com
  DomainAddr: ldaps://203.0.113.225,ldaps://192.0.2.254
  PasswordSecretArn: arn:aws:secretsmanager:region-id:123456789012:secret:MicrosoftAD.Admin.Password-1234
  DomainReadOnlyUser: cn=ReadOnly,ou=Users,ou=CORP,dc=corp,dc=example,dc=com
  LdapTlsReqCert: never
```
