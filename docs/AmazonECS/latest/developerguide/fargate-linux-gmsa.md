# Using gMSA for Linux

containers on Fargate

Amazon ECS supports Active Directory authentication for Linux containers on Fargate through a
special kind of service account called a _group Managed Service Account_
(gMSA).

Linux based network applications, such as .NET Core
applications, can use Active Directory to facilitate authentication and authorization
management between users and services. You can use this feature by designing applications
that integrate with Active Directory and run on domain-joined servers. But, because
Linux containers can't be domain-joined, you need to configure a
Linux container to run with gMSA.

## Considerations

Consider the following before you use gMSA for Linux containers on
Fargate:

- You must be running Platform Version 1.4 or later.
- You might need a Windows computer that's joined to the domain
  to complete the prerequisites. For example, you might need a
  Windows computer that's joined to the domain to create the
  gMSA in Active Directory with PowerShell. The
  RSAT Active Director PowerShell tools are only available for
  Windows. For more information, see [Installing the Active Directory administration tools](../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md "../../../directoryservice/latest/admin-guide/ms_ad_install_ad_tools.md").
- You must use **domainless gMSA**.

Amazon ECS uses an Active Directory credential specification file (CredSpec).
This file contains the gMSA metadata that's used to propagate the gMSA
account context to the container. You generate the CredSpec file, and then
store it in an Amazon S3 bucket.

- A task can only support one Active Directory.

## Prerequisites

Before you use the gMSA for Linux containers feature with Amazon ECS, make sure to
complete the following:

- You set up an Active Directory domain with the resources that you want your
  containers to access. Amazon ECS supports the following setups:
  - An Directory Service Active Directory. Directory Service is an AWS managed Active Directory
    that's hosted on Amazon EC2. For more information, see [Getting Started with AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md") in the
    _AWS Directory Service Administration Guide_.
  - An on-premises Active Directory. You must ensure that the Amazon ECS Linux
    container instance can join the domain. For more information, see [AWS Direct Connect](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-network-to-amazon.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-network-to-amazon.md").

- You have an existing gMSA account in the Active Directory and a user that
  has permission to access the gMSA service account. For more information, see
  [Make an Active
  Directory user for domainless gMSA](#fargate-linux-gmsa-initial-domainless "#fargate-linux-gmsa-initial-domainless").
- You have an Amazon S3 bucket. For more information, see [Creating a
  bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

## Setting up gMSA-capable Linux

Containers on Amazon ECS

###### Prepare the infrastructure

The following steps are considerations and setup that are performed once.

- ###### Make an Active
  Directory user for domainless gMSA

When you use domainless gMSA, the container isn't joined to the domain.
Other applications that run on the container can't use the credentials to access
the domain. Tasks that use a different domain can run on the same container. You
provide the name of a secret in AWS Secrets Manager in the CredSpec file. The secret
must contain a username, password, and the domain to log in to.

This feature is similar to the _gMSA support for
non-domain-joined container hosts_ feature.
For more information about the Windows feature, see [gMSA architecture and improvements](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#gmsa-architecture-and-improvements "https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#gmsa-architecture-and-improvements") on the Microsoft Learn
website.

    1. Configure a user in your Active Directory domain. The user in
     the Active Directory must have permission to access the gMSA service
     account that you use in the tasks.
    2. You have a VPC and subnets that can resolve the Active
     Directory domain name. Configure the VPC with DHCP options with the
     domain name that points to the Active Directory service name. For
     information about how to configure DHCP options for a VPC, see [Work with DHCP option sets](../../../vpc/latest/userguide/DHCPOptionSet.md "../../../vpc/latest/userguide/DHCPOptionSet.md")  in the *Amazon Virtual Private Cloud User Guide*.
    3. Create a secret in AWS Secrets Manager.
    4. Create the credential specification file.

###### Setting up permissions and secrets

Do the following steps one time for each application and each task definition. We
recommend that you use the best practice of granting the least privilege and narrow
the permissions used in the policy. This way, each task can only read the secrets
that it needs.

1. Make a user in your Active Directory domain. The user in
   Active Directory must have permission to access the gMSA
   service accounts that you use in the tasks.
2. After you make the Active Directory user, create a secret in AWS Secrets Manager. For
   more information, see [Create an AWS Secrets Manager
   secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").
3. Enter the user's username, password, and the domain into JSON
   key-value pairs called `username`,
   `password` and `domainName`,
   respectively.

```
{"username":"`username`","password":"`passw0rd`", "domainName":"example.com"}
```

4. You must add the following permissions as an inline policy to the task
   execution IAM role. Doing so gives the `credentials-fetcher` daemon access to the Secrets Manager secret.
   Replace the `MySecret` example with the Amazon Resource Name (ARN) of your secret in
   the `Resource` list.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "`arn:aws:secretsmanager:us-east-1:`111122223333`:secret:MySecret`"
 ]
 }
 ]
}`

```

###### Note

If you use your own KMS key to encrypt your secret, you must add the
necessary permissions to this role and add this role to the AWS KMS key
policy. 5. Add the credential spec to an Amazon S3 bucket. Then, reference the Amazon Resource Name (ARN) of
the Amazon S3 bucket in the `credentialSpecs` field of the task
definition.

```
{
    "family": "",
    "executionRoleArn": "",
    "containerDefinitions": [
        {
            "name": "",
            ...
            **"credentialSpecs": [
 "credentialspecdomainless:arn:aws:s3:::`${BucketName}/${ObjectName}`"
 ]**,
            ...
        }
    ],
    ...
}
```

To give your tasks access to the S3 bucket, add the following permissions as
an inline policy to the Amazon ECS task execution IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor",
 "Effect": "Allow",
 "Action": [
 "s3:GetObjectVersion",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`{bucket_name}`",
 "arn:aws:s3:::`{bucket_name}/{object}`"
 ]
 }
 ]
}`

```

## Credential specification file

Amazon ECS uses an Active Directory credential specification file
(_CredSpec_). This file contains the gMSA metadata that's
used to propagate the gMSA account context to the Linux container. You
generate the CredSpec and reference it in the `credentialSpecs` field in
your task definition. The CredSpec file doesn't contain any secrets.

The following is an example CredSpec file.

```
{
    "CmsPlugins": [
        "ActiveDirectory"
    ],
    "DomainJoinConfig": {
        "Sid": "S-1-5-21-2554468230-2647958158-2204241789",
        "MachineAccountName": "WebApp01",
        "Guid": "8665abd4-e947-4dd0-9a51-f8254943c90b",
        "DnsTreeName": "example.com",
        "DnsName": "example.com",
        "NetBiosName": "example"
    },
    "ActiveDirectoryConfig": {
        "GroupManagedServiceAccounts": [
            {
                "Name": "WebApp01",
                "Scope": "example.com"
            }
        ],
        "HostAccountConfig": {
            "PortableCcgVersion": "1",
            "PluginGUID": "{859E1386-BDB4-49E8-85C7-3070B13920E1}",
            "PluginInput": {
                "CredentialArn": "`arn:aws:secretsmanager:`aws-region`:111122223333:secret:MySecret`"
            }
        }
    }
}
```

###### Creating a CredSpec and uploading it to an Amazon S3

You create a CredSpec by using the CredSpec PowerShell module
on a Windows computer that's joined to the domain. Follow the steps
in [Create a credential spec](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#create-a-credential-spec "https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#create-a-credential-spec") on the Microsoft Learn
website.

After you create the credential specification file, upload it to an Amazon S3
bucket. Copy the CredSpec file to the computer or environment that you are running
AWS CLI commands in.

Run the following AWS CLI command to upload the CredSpec to Amazon S3. Replace
`amzn-s3-demo-bucket` with the name of your Amazon S3 bucket. You can store the file as an
object in any bucket and location, but you must allow access to that bucket and location
in the policy that you attach to the task execution role.

For PowerShell, use the following command:

```
`$` `Write-S3Object -BucketName "`amzn-s3-demo-bucket`" -Key "ecs-domainless-gmsa-credspec" -File "gmsa-cred-spec.json"`
```

The following AWS CLI command uses backslash continuation characters that are
used by `sh` and compatible shells.

```
`$` `aws s3 cp gmsa-cred-spec.json \
s3://`amzn-s3-demo-bucket/ecs-domainless-gmsa-credspec``
```
