# Learn how to use gMSAs for EC2 Windows containers for Amazon ECS

Amazon ECS supports Active Directory authentication for Windows containers through a special
kind of service account called a _group Managed Service Account_
(gMSA).

Windows based network applications such as .NET applications often use Active Directory to
facilitate authentication and authorization management between users and services.
Developers commonly design their applications to integrate with Active Directory and run on
domain-joined servers for this purpose. Because Windows containers cannot be domain-joined,
you must configure a Windows container to run with gMSA.

A Windows container running with gMSA relies on its host Amazon EC2 instance to retrieve the
gMSA credentials from the Active Directory domain controller and provide them to the
container instance. For more information, see [Create gMSAs for Windows containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts "https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts").

###### Note

This feature is not supported on Windows containers on Fargate.

###### Topics

- [Considerations](#windows-gmsa-considerations "#windows-gmsa-considerations")
- [Prerequisites](#windows-gmsa-prerequisites "#windows-gmsa-prerequisites")
- [Setting up gMSA for Windows Containers on
  Amazon ECS](#windows-gmsa-setup "#windows-gmsa-setup")

## Considerations

The following should be considered when using gMSAs for Windows containers:

- When using the Amazon ECS-optimized Windows Server 2016 Full AMI for your container instances, the
  container hostname must be the same as the gMSA account name defined in the
  credential spec file. To specify a hostname for a container, use the
  `hostname` container definition parameter. For more information,
  see [Network settings](task_definition_parameters.md#container_definition_network "task_definition_parameters.md#container_definition_network").
- You chose between **domainless gMSA** and **joining each instance to a single domain**. By using domainless gMSA,
  the container instance isn't joined to the domain, other applications on the instance can't use
  the credentials to access the domain, and tasks that join different domains can run on the same
  instance.

Then, choose the data storage for the CredSpec and optionally, for the Active Directory user
credentials for domainless gMSA.

Amazon ECS uses an Active Directory credential specification file (CredSpec). This file
contains the gMSA metadata that's used to propagate the gMSA account context to the
container. You generate the CredSpec file and then store it in one of the CredSpec storage
options in the following table, specific to the Operating System of the container instances. To
use the domainless method, an optional section in the CredSpec file can specify credentials in
one of the _domainless user credentials_ storage options in the
following table, specific to the Operating System of the container instances.

| Storage location                           | Linux                       | Windows                               |
| ------------------------------------------ | --------------------------- | ------------------------------------- |
| Amazon Simple Storage Service              | CredSpec                    | CredSpec                              |
| AWS Secrets Manager                        | domainless user credentials | domainless user credentials           |
| Amazon EC2 Systems Manager Parameter Store | CredSpec                    | CredSpec, domainless user credentials |
| Local file                                 | N/A                         | CredSpec                              |

## Prerequisites

Before you use the gMSA for Windows containers feature with Amazon ECS, make
sure to complete the following:

- You set up an Active Directory domain with the resources that you want your
  containers to access. Amazon ECS supports the following setups:
  - An Directory Service Active Directory. Directory Service is an AWS managed Active Directory
    that's hosted on Amazon EC2. For more information, see [Getting Started with AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md") in the
    _AWS Directory Service Administration Guide_.
  - An on-premises Active Directory. You must ensure that the Amazon ECS Linux
    container instance can join the domain. For more information, see [AWS Direct Connect](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-network-to-amazon.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-network-to-amazon.md").

- You have an existing gMSA account in the Active Directory. For
  more information, see [Create gMSAs for Windows containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts "https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts").
- **You chose to use _domainless gMSA_
  or the Amazon ECS Windows container instance hosting the Amazon ECS task must be
  _domain joined_ to the Active Directory and be a
  member of the Active Directory security group that has access to the gMSA
  account.**

By using domainless gMSA,
the container instance isn't joined to the domain, other applications on the instance can't use
the credentials to access the domain, and tasks that join different domains can run on the same
instance.

- You added the required IAM permissions. The permissions that are required
  depend on the methods that you choose for the initial credentials and for
  storing the credential specification:
  - If you use _domainless gMSA_ for initial
    credentials, IAM permissions for AWS Secrets Manager are required on the Amazon EC2
    instance role.
  - If you store the credential specification in SSM Parameter Store,
    IAM permissions for Amazon EC2 Systems Manager Parameter Store are required on the task
    execution role.
  - If you store the credential specification in Amazon S3, IAM permissions
    for Amazon Simple Storage Service are required on the task execution role.

## Setting up gMSA for Windows Containers on

Amazon ECS

To set up gMSA for Windows Containers on Amazon ECS, you can follow
the complete tutorial that includes configuring the prerequisites [Using Amazon ECS Windows containers with domainless
gMSA using the AWS CLI](tutorial-gmsa-windows.md "tutorial-gmsa-windows.md").

The following sections cover the CredSpec configuration in detail.

###### Topics

- [Example CredSpec](#windows-gmsa-example "#windows-gmsa-example")
- [Domainless gMSA setup](#windows-gmsa-domainless "#windows-gmsa-domainless")
- [Referencing a Credential Spec File in
  a Task Definition](#windows-gmsa-credentialspec "#windows-gmsa-credentialspec")

### Example CredSpec

Amazon ECS uses a credential spec file that contains the gMSA metadata used to
propagate the gMSA account context to the Windows container. You can generate the
credential spec file and reference it in the `credentialSpec` field in
your task definition. The credential spec file does not contain any secrets.

The following is an example credential spec file:

```
{
    "CmsPlugins": [
        "ActiveDirectory"
    ],
    "DomainJoinConfig": {
        "Sid": "S-1-5-21-2554468230-2647958158-2204241789",
        "MachineAccountName": "WebApp01",
        "Guid": "8665abd4-e947-4dd0-9a51-f8254943c90b",
        "DnsTreeName": "contoso.com",
        "DnsName": "contoso.com",
        "NetBiosName": "contoso"
    },
    "ActiveDirectoryConfig": {
        "GroupManagedServiceAccounts": [
            {
                "Name": "WebApp01",
                "Scope": "contoso.com"
            }
        ]
    }
}
```

### Domainless gMSA setup

We recommend domainless gMSA instead of joining the container instances to a
single domain. By using domainless gMSA,
the container instance isn't joined to the domain, other applications on the instance can't use
the credentials to access the domain, and tasks that join different domains can run on the same
instance.

1. Before uploading the CredSpec to one of the storage options, add
   information to the CredSpec with the ARN of the secret in Secrets Manager or SSM
   Parameter Store. For more information, see [Additional credential spec configuration for non-domain-joined
   container host use case](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#additional-credential-spec-configuration-for-non-domain-joined-container-host-use-case "https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#additional-credential-spec-configuration-for-non-domain-joined-container-host-use-case") on the Microsoft Learn website.

###### Domainless gMSA credential format

The following is the JSON format for the domainless gMSA credentials
for your Active Directory. Store the credentials in Secrets Manager or SSM
Parameter Store.

```
{
    "username":"`WebApp01`",
    "password":"`Test123!`",
    "domainName":"`contoso.com`"
}
```

2. Add the following information to the CredSpec file inside the
   `ActiveDirectoryConfig`. Replace the ARN with the secret in
   Secrets Manager or SSM Parameter Store.

Note that the `PluginGUID` value must match the GUID in the
following example snippet and is required.

```

    "HostAccountConfig": {
        "PortableCcgVersion": "1",
        "PluginGUID": "{859E1386-BDB4-49E8-85C7-3070B13920E1}",
        "PluginInput": "{\"credentialArn\": \"arn:aws:secretsmanager:`aws-region`:111122223333:secret:`gmsa-plugin-input`\"}"
    }
```

You can also use a secret in SSM Parameter Store by using the ARN in
this format:
`\"arn:aws:ssm:`aws-region`:111122223333:parameter/`gmsa-plugin-input`\"`. 3. After you modify the CredSpec file, it should look like the following
example:

```
{
  "CmsPlugins": [
    "ActiveDirectory"
  ],
  "DomainJoinConfig": {
    "Sid": "S-1-5-21-4066351383-705263209-1606769140",
    "MachineAccountName": "WebApp01",
    "Guid": "ac822f13-583e-49f7-aa7b-284f9a8c97b6",
    "DnsTreeName": "contoso",
    "DnsName": "contoso",
    "NetBiosName": "contoso"
  },
  "ActiveDirectoryConfig": {
    "GroupManagedServiceAccounts": [
      {
        "Name": "WebApp01",
        "Scope": "contoso"
      },
      {
        "Name": "WebApp01",
        "Scope": "contoso"
      }
    ],
    "HostAccountConfig": {
      "PortableCcgVersion": "1",
      "PluginGUID": "{859E1386-BDB4-49E8-85C7-3070B13920E1}",
      "PluginInput": "{\"credentialArn\": \"arn:aws:secretsmanager:`aws-region`:111122223333:secret:`gmsa-plugin-input`\"}"
    }
  }
}
```

### Referencing a Credential Spec File in

a Task Definition

Amazon ECS supports the following ways to reference the file path in the
`credentialSpecs` field of the task definition. For each of these
options, you can provide `credentialspec:` or
`domainlesscredentialspec:`, depending on whether you are joining the
container instances to a single domain, or using domainless gMSA,
respectively.

#### Amazon S3 Bucket

Add the credential spec to an Amazon S3 bucket and then reference the Amazon
Resource Name (ARN) of the Amazon S3 bucket in the `credentialSpecs` field
of the task definition.

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

You must also add the following permissions as an inline policy to the Amazon ECS
task execution IAM role to give your tasks access to the Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor",
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:List*"
 ],
 "Resource": [
 "arn:aws:s3:::`{bucket_name}`",
 "arn:aws:s3:::`{bucket_name}/{object}`"
 ]
 }
 ]
}`

```

#### SSM Parameter Store parameter

Add the credential spec to an SSM Parameter Store parameter and then
reference the Amazon Resource Name (ARN) of the SSM Parameter Store parameter
in the `credentialSpecs` field of the task definition.

```
{
    "family": "",
    "executionRoleArn": "",
    "containerDefinitions": [
        {
            "name": "",
            ...
            **"credentialSpecs": [
 "credentialspecdomainless:arn:aws:ssm:`region`:`111122223333`:parameter/`parameter_name`"
 ]**,
            ...
        }
    ],
    ...
}
```

You must also add the following permissions as an inline policy to the Amazon ECS
task execution IAM role to give your tasks access to the SSM Parameter Store
parameter.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameters"
 ],
 "Resource": "arn:aws:ssm:*:`111122223333`:parameter/example*"
 }
 ]
}`

```

#### Local File

With the credential spec details in a local file, reference the file path in
the `credentialSpecs` field of the task definition. The file path
referenced must be relative to the
`C:\ProgramData\Docker\CredentialSpecs` directory and use the
backslash ('\') as the file path separator.

```
{
    "family": "",
    "executionRoleArn": "",
    "containerDefinitions": [
        {
            "name": "",
            ...
            **"credentialSpecs": [
 "credentialspec:file://`CredentialSpecDir\CredentialSpecFile.json`"
 ]**,
            ...
        }
    ],
    ...
}
```
