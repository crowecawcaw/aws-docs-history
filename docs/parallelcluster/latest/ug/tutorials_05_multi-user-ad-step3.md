# Create the cluster

If you haven't exited the Amazon EC2 instance, do so now.

The environment is set up to create a cluster that can authenticate users against the Active Directory (AD).

Create a simple cluster configuration and provide the settings relevant to connecting to the AD. For more information, see the [DirectoryService](DirectoryService-v3.md "DirectoryService-v3.md") section.

Choose one of the following cluster configurations and copy it to a file that's named `ldaps_config.yaml`,
`ldaps_nocert_config.yaml`, or `ldap_config.yaml`.

We recommend that you choose the LDAPS configuration with certificate verification. If you choose this configuration, you must also copy the
bootstrap script to a file that's named `active-directory.head.post.sh`. And, you must store it in an Amazon S3 bucket as indicated in the
configuration file.

###### Note

###### The following components must be changed.

- `KeyName`: One of your Amazon EC2 keypairs.
- `SubnetId / SubnetIds`: One of the subnet IDs provided in the output of the CloudFormation quick create stack (automated tutorial) or python script
  (manual tutorial).
- `Region`: The Region where you created the AD infrastructure.
- `DomainAddr`: This IP address is one of the DNS addresses of your AD service.
- `PasswordSecretArn`: The Amazon Resource Name (ARN) of the secret that contains the password for the
  `DomainReadOnlyUser`.
- `BucketName`: The name of the bucket that holds the bootstrap script.
- `AdditionalPolicies` / `Policy`: The Amazon Resource Name (ARN) of the read domain certification policy
  ReadCertExample.
- `CustomActions` / `OnNodeConfigured` / `Args`: The Amazon Resource Name (ARN) of secret that holds the
  domain certification policy.
  For better security posture, we suggest to use the `HeadNode` / `Ssh` / `AllowedIps` configuration to limit the SSH access to the head node.

```
Region: `region-id`
Image:
  Os: alinux2
HeadNode:
  InstanceType: t2.micro
  Networking:
    SubnetId: `subnet-abcdef01234567890`
  Ssh:
    KeyName: `keypair`
  Iam:
    AdditionalIamPolicies:
      - Policy: arn:aws:iam::`123456789012`:policy/ReadCertExample
    S3Access:
      - BucketName: `amzn-s3-demo-bucket`
        EnableWriteAccess: false
        KeyName: bootstrap/active-directory/active-directory.head.post.sh
  CustomActions:
    OnNodeConfigured:
      Script: s3://`amzn-s3-demo-bucket`/bootstrap/active-directory/active-directory.head.post.sh
      Args:
        - arn:aws:secretsmanager:`region-id`:`123456789012`:secret:example-cert-`123abc`
        - /opt/parallelcluster/shared/directory_service/domain-certificate.crt
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: queue0
      ComputeResources:
        - Name: queue0-t2-micro
          InstanceType: t2.micro
          MinCount: 1
          MaxCount: 10
      Networking:
        SubnetIds:
          - `subnet-abcdef01234567890`
DirectoryService:
  DomainName: corp.example.com
  DomainAddr: ldaps://corp.example.com
  PasswordSecretArn: arn:aws:secretsmanager:`region-id`:`123456789012`:secret:ADSecretPassword-`1234`
  DomainReadOnlyUser: cn=ReadOnlyUser,ou=Users,ou=CORP,dc=corp,dc=example,dc=com
  LdapTlsCaCert: /opt/parallelcluster/shared/directory_service/domain-certificate.crt
  LdapTlsReqCert: hard
```

**Bootstrap script**

After you create the bootstrap file and before you upload it to your S3 bucket, run `chmod +x active-directory.head.post.sh` to
give AWS ParallelCluster run permission.

```
#!/bin/bash
set -e

CERTIFICATE_SECRET_ARN="$1"
CERTIFICATE_PATH="$2"

[[ -z $CERTIFICATE_SECRET_ARN ]] && echo "[ERROR] Missing CERTIFICATE_SECRET_ARN" && exit 1
[[ -z $CERTIFICATE_PATH ]] && echo "[ERROR] Missing CERTIFICATE_PATH" && exit 1

source /etc/parallelcluster/cfnconfig
REGION="${cfn_region:?}"

mkdir -p $(dirname $CERTIFICATE_PATH)
aws secretsmanager get-secret-value --region $REGION --secret-id $CERTIFICATE_SECRET_ARN --query SecretString --output text > $CERTIFICATE_PATH
```

###### Note

###### The following components must be changed.

- `KeyName`: One of your Amazon EC2 keypairs.
- `SubnetId / SubnetIds`: One of the subnet IDs that's in the output of the CloudFormation quick create stack (automated tutorial)
  or python script (manual tutorial).
- `Region`: The Region where you created the AD infrastructure.
- `DomainAddr`: This IP address is one of the DNS addresses of your AD service.
- `PasswordSecretArn`: The Amazon Resource Name (ARN) of the secret that contains the password for the
  `DomainReadOnlyUser`.
  For better security posture, we suggest to use the HeadNode/Ssh/AllowedIps configuration to limit the SSH access to the head node.

```
Region: `region-id`
Image:
  Os: alinux2
HeadNode:
  InstanceType: t2.micro
  Networking:
    SubnetId: `subnet-abcdef01234567890`
  Ssh:
    KeyName: `keypair`
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: queue0
      ComputeResources:
        - Name: queue0-t2-micro
          InstanceType: t2.micro
          MinCount: 1
          MaxCount: 10
      Networking:
        SubnetIds:
          - `subnet-abcdef01234567890`
DirectoryService:
  DomainName: corp.example.com
  DomainAddr: ldaps://corp.example.com
  PasswordSecretArn: arn:aws:secretsmanager:`region-id`:`123456789012`:secret:ADSecretPassword-`1234`
  DomainReadOnlyUser: cn=ReadOnlyUser,ou=Users,ou=CORP,dc=corp,dc=example,dc=com
  LdapTlsReqCert: never
```

###### Note

###### The following components must be changed.

- `KeyName`: One of your Amazon EC2 keypairs.
- `SubnetId / SubnetIds`: One of the subnet IDs provided in the output of the CloudFormation quick create stack (automated tutorial) or python script
  (manual tutorial).
- `Region`: The Region where you created the AD infrastructure.
- `DomainAddr`: This IP address is one of the DNS addresses of your AD service.
- `PasswordSecretArn`: The Amazon Resource Name (ARN) of the secret that contains the password for the
  `DomainReadOnlyUser`.
  For better security posture, we suggest to use the HeadNode/Ssh/AllowedIps configuration to limit the SSH access to the head node.

```
Region: `region-id`
Image:
  Os: alinux2
HeadNode:
  InstanceType: t2.micro
  Networking:
    SubnetId: `subnet-abcdef01234567890`
  Ssh:
    KeyName: `keypair`
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: queue0
      ComputeResources:
        - Name: queue0-t2-micro
          InstanceType: t2.micro
          MinCount: 1
          MaxCount: 10
      Networking:
        SubnetIds:
          - `subnet-abcdef01234567890`
DirectoryService:
  DomainName: dc=corp,dc=example,dc=com
  DomainAddr: ldap://`192.0.2.254`,ldap://`203.0.113.237`
  PasswordSecretArn: arn:aws:secretsmanager:`region-id`:`123456789012`:secret:ADSecretPassword-`1234`
  DomainReadOnlyUser: cn=ReadOnlyUser,ou=Users,ou=CORP,dc=corp,dc=example,dc=com
  AdditionalSssdConfigs:
    ldap_auth_disable_tls_never_use_in_production: True
```

Create your cluster with the following command.

````
`$` `pcluster create-cluster --cluster-name `"ad-cluster"` --cluster-configuration `"./ldaps_config.yaml"```{
 "cluster": {
 "clusterName": "pcluster",
 "cloudformationStackStatus": "CREATE_IN_PROGRESS",
 "cloudformationStackArn": "arn:aws:cloudformation:region-id:123456789012:stack/ad-cluster/1234567-abcd-0123-def0-abcdef0123456",
 "region": "region-id",
 "version": 3.14.1,
 "clusterStatus": "CREATE_IN_PROGRESS"
 }
}`
````
