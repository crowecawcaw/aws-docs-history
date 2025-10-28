# Create a cluster with an AD domain

###### Warning

This introductory section describes how to set up AWS ParallelCluster with a Managed Active Directory (AD) server over the Lightweight
Directory Access Protocol (LDAP). LDAP is an insecure protocol. For production systems, we strongly recommended the use of TLS certificates
(LDAPS) as described in the [Example AWS Managed Microsoft AD over LDAP(S) cluster
configurations](examples-addir-v3.md "examples-addir-v3.md") section that follows.

Configure your cluster to integrate with a directory by specifying the relevant
information in the `DirectoryService` section of the cluster configuration file.
For more information, see the [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") configuration
section.

You can use this following example to integrate your cluster with an AWS Managed Microsoft AD over the Lightweight Directory Access Protocol
(LDAP).

###### Specific definitions that are required for an AWS Managed Microsoft AD over LDAP

configuration:

- You must set the `ldap_auth_disable_tls_never_use_in_production` parameter
  to `True` under [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [AdditionalSssdConfigs](DirectoryService-v3.md#yaml-DirectoryService-AdditionalSssdConfigs "DirectoryService-v3.md#yaml-DirectoryService-AdditionalSssdConfigs").
- You can specify either controller hostnames or IP addresses for [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md")
  / [DomainAddr](DirectoryService-v3.md#yaml-DirectoryService-DomainAddr "DirectoryService-v3.md#yaml-DirectoryService-DomainAddr").
- [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainReadOnlyUser](DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser "DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser") syntax must be as follows:

```
cn=ReadOnly,ou=Users,ou=CORP,dc=`corp`,dc=`example`,dc=`com`
```

**Get your AWS Managed Microsoft AD configuration data:**

```
`$` `aws ds describe-directories --directory-id `"d-abcdef01234567890"``
```

```
`{
 "DirectoryDescriptions": [
 {
 "DirectoryId": "d-abcdef01234567890",
 "Name": "corp.example.com",
 "DnsIpAddrs": [
 "203.0.113.225",
 "192.0.2.254"
 ],
 "VpcSettings": {
 "VpcId": "vpc-021345abcdef6789",
 "SubnetIds": [
 "subnet-1234567890abcdef0",
 "subnet-abcdef01234567890"
 ],
 "AvailabilityZones": [
 "region-idb",
 "region-idd"
 ]
 }
 }
 ]
}`
```

**Cluster configuration for an AWS Managed Microsoft AD:**

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
  DomainAddr: ldap://203.0.113.225,ldap://192.0.2.254
  PasswordSecretArn: arn:aws:secretsmanager:region-id:123456789012:secret:MicrosoftAD.Admin.Password-1234
  DomainReadOnlyUser: cn=ReadOnly,ou=Users,ou=CORP,dc=corp,dc=example,dc=com
  AdditionalSssdConfigs:
    ldap_auth_disable_tls_never_use_in_production: True
```

**To use this configuration for a Simple AD, change the
`DomainReadOnlyUser` property value in the `DirectoryService`
section:**

```
DirectoryService:
  DomainName: dc=corp,dc=example,dc=com
  DomainAddr: ldap://203.0.113.225,ldap://192.0.2.254
  PasswordSecretArn: arn:aws:secretsmanager:region-id:123456789012:secret:SimpleAD.Admin.Password-1234
  DomainReadOnlyUser: cn=ReadOnlyUser,cn=Users,dc=`corp`,dc=`example`,dc=`com`
  AdditionalSssdConfigs:
    ldap_auth_disable_tls_never_use_in_production: True
```

###### Considerations:

- We recommend that you use LDAP over TLS/SSL (or LDAPS) rather than LDAP alone. TLS/SSL
  ensures that the connection is encrypted.
- The [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainAddr](DirectoryService-v3.md#yaml-DirectoryService-DomainAddr "DirectoryService-v3.md#yaml-DirectoryService-DomainAddr") property value
  matches the entries in the `DnsIpAddrs` list from the
  `describe-directories` output.
- We recommend that your cluster use subnets that are located in the same Availability Zone that the [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainAddr](DirectoryService-v3.md#yaml-DirectoryService-DomainAddr "DirectoryService-v3.md#yaml-DirectoryService-DomainAddr") points to. If you use
  [custom Dynamic Host Configuration Protocol (DHCP)
  configuration](../../../directoryservice/latest/admin-guide/dhcp_options_set.md "../../../directoryservice/latest/admin-guide/dhcp_options_set.md") that's recommended for directory VPCs and your subnets _aren't_ located in the [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainAddr](DirectoryService-v3.md#yaml-DirectoryService-DomainAddr "DirectoryService-v3.md#yaml-DirectoryService-DomainAddr") Availability Zone, cross traffic among Availability Zones is possible. The use of custom DHCP configurations
  _isn't_ required to use the multi-user AD integration feature.
- The [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainReadOnlyUser](DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser "DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser") property value specifies a user that must be
  created in the directory. This user _isn't_ created by default. We
  recommend that you _don't_ give this user permission to modify
  directory data.
- The [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [PasswordSecretArn](DirectoryService-v3.md#yaml-DirectoryService-PasswordSecretArn "DirectoryService-v3.md#yaml-DirectoryService-PasswordSecretArn") property value points to an AWS Secrets Manager secret that contains the password of the user that you specified
  for the [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") / [DomainReadOnlyUser](DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser "DirectoryService-v3.md#yaml-DirectoryService-DomainReadOnlyUser") property. If this user’s password changes, update the secret value and update the cluster. To update
  the cluster for the new secret value, you must stop the compute fleet with the `pcluster update-compute-fleet` command. If you configured your
  cluster to use [LoginNodes](LoginNodes-v3.md "LoginNodes-v3.md"), stop the [LoginNodes](LoginNodes-v3.md "LoginNodes-v3.md") /
  [Pools](LoginNodes-v3.md#LoginNodes-v3-Pools "LoginNodes-v3.md#LoginNodes-v3-Pools") and update the cluster after setting [LoginNodes](LoginNodes-v3.md "LoginNodes-v3.md") /
  [Pools](LoginNodes-v3.md#LoginNodes-v3-Pools "LoginNodes-v3.md#LoginNodes-v3-Pools") / [Count](LoginNodes-v3.md#yaml-LoginNodes-Pools-Count "LoginNodes-v3.md#yaml-LoginNodes-Pools-Count") to 0.
  Then, run the following command from within the cluster head node.

```
 `sudo /opt/parallelcluster/scripts/directory_service/update_directory_service_password.sh`
```

For another example, see also [Integrating Active Directory](tutorials_05_multi-user-ad.md "tutorials_05_multi-user-ad.md").
