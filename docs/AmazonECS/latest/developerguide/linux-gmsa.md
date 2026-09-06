

# Using gMSA for EC2 Linux containers on Amazon ECS
<a name="linux-gmsa"></a>

Amazon ECS supports Active Directory authentication for Linux containers on EC2 through a special kind of service account called a *group Managed Service Account* (gMSA).

Linux based network applications, such as .NET Core applications, can use Active Directory to facilitate authentication and authorization management between users and services. You can use this feature by designing applications that integrate with Active Directory and run on domain-joined servers. But, because Linux containers can't be domain-joined, you need to configure a Linux container to run with gMSA.

A Linux container that runs with gMSA relies on the `credentials-fetcher` daemon that runs on the container's host Amazon EC2 instance. That is, the daemon retrieves the gMSA credentials from the Active Directory domain controller and then transfers these credentials to the container instance. For more information about service accounts, see [Create gMSAs for Windows containers](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts) on the Microsoft Learn website.

## Considerations
<a name="linux-gmsa-considerations"></a>

Consider the following before you use gMSA for Linux containers:
+ If your containers run on EC2, you can use gMSA for Windows containers and Linux containers. For information about how to use gMSA for Linux container on Fargate, see [Using gMSA for Linux containers on Fargate](fargate-linux-gmsa.md).
+ You might need a Windows computer that's joined to the domain to complete the prerequisites. For example, you might need a Windows computer that's joined to the domain to create the gMSA in Active Directory with PowerShell. The RSAT Active Director PowerShell tools are only available for Windows. For more information, see [Installing the Active Directory administration tools](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html).
+ You chose between **domainless gMSA** and ** joining each instance to a single domain**. By using domainless gMSA, the container instance isn't joined to the domain, other applications on the instance can't use the credentials to access the domain, and tasks that join different domains can run on the same instance.

  Then, choose the data storage for the CredSpec and optionally, for the Active Directory user credentials for domainless gMSA.

  Amazon ECS uses an Active Directory credential specification file (CredSpec). This file contains the gMSA metadata that's used to propagate the gMSA account context to the container. You generate the CredSpec file and then store it in one of the CredSpec storage options in the following table, specific to the Operating System of the container instances. To use the domainless method, an optional section in the CredSpec file can specify credentials in one of the *domainless user credentials* storage options in the following table, specific to the Operating System of the container instances.    
<a name="gmsa-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/linux-gmsa.html)

## Prerequisites
<a name="linux-gmsa-prerequisites"></a>

Before you use the gMSA for Linux containers feature with Amazon ECS, make sure to complete the following:
+ You set up an Active Directory domain with the resources that you want your containers to access. Amazon ECS supports the following setups:
  + An Directory Service Active Directory. Directory Service is an AWS managed Active Directory that's hosted on Amazon EC2. For more information, see [Getting Started with AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started.html) in the *AWS Directory Service Administration Guide*.
  + An on-premises Active Directory. You must ensure that the Amazon ECS Linux container instance can join the domain. For more information, see [AWS Direct Connect](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html).
+ You have an existing gMSA account in the Active Directory. For more information, see [Using gMSA for EC2 Linux containers on Amazon ECS](#linux-gmsa).
+ You installed and are running the `credentials-fetcher` daemon on an Amazon ECS Linux container instance. You also added an initial set of credentials to the `credentials-fetcher` daemon to authenticate with the Active Directory.
**Note**  
The `credentials-fetcher` daemon is only available for Amazon Linux 2023 and Fedora 37 and later. The daemon isn't available for Amazon Linux 2. For more information, see [aws/credentials-fetcher](https://github.com/aws/credentials-fetcher) on GitHub.
+ You set up the credentials for the `credentials-fetcher` daemon to authenticate with the Active Directory. The credentials must be a member of the Active Directory security group that has access to the gMSA account. There are multiple options in [Decide if you want to join the instances to the domain, or use domainless gMSA.](#linux-gmsa-initial-creds).
+ You added the required IAM permissions. The permissions that are required depend on the methods that you choose for the initial credentials and for storing the credential specification:
  + If you use *domainless gMSA* for initial credentials, IAM permissions for AWS Secrets Manager are required on the task execution role.
  + If you store the credential specification in SSM Parameter Store, IAM permissions for Amazon EC2 Systems Manager Parameter Store are required on the task execution role.
  + If you store the credential specification in Amazon S3, IAM permissions for Amazon Simple Storage Service are required on the task execution role.

## Setting up gMSA-capable Linux Containers on Amazon ECS
<a name="linux-gmsa-setup"></a>
<a name="linux-gmsa-setup-infra"></a>
**Prepare the infrastructure**  
The following steps are considerations and setup that are performed once. After you complete these steps, you can automate creating container instances to reuse this configuration.

Decide how the initial credentials are provided and configure the EC2 user data in a reusable EC2 launch template to install the `credentials-fetcher` daemon.

1. <a name="linux-gmsa-initial-creds"></a>

**Decide if you want to join the instances to the domain, or use domainless gMSA.**
   + <a name="linux-gmsa-initial-join"></a>

**Join EC2 instances to the Active Directory domain**

     
     + <a name="linux-gmsa-initial-join-userdata"></a>

**Join the instances by user data**

       Add the steps to join the Active Directory domain to your EC2 user data in an EC2 launch template. Multiple Amazon EC2 Auto Scaling groups can use the same launch template.

       You can use these steps [Joining an Active Directory or FreeIPA domain](https://docs.fedoraproject.org/en-US/quick-docs/join-active-directory-freeipa/) in the Fedora Docs.
   + <a name="linux-gmsa-initial-domainless"></a>

**Make an Active Directory user for domainless gMSA**

     The `credentials-fetcher` daemon has a feature that's called *domainless gMSA*. This feature requires a domain, but the EC2 instance doesn't need to be joined to the domain. By using domainless gMSA, the container instance isn't joined to the domain, other applications on the instance can't use the credentials to access the domain, and tasks that join different domains can run on the same instance. Instead, you provide the name of a secret in AWS Secrets Manager in the CredSpec file. The secret must contain a username, password, and the domain to log in to.

     This feature is supported and can be used with Linux and Windows containers.

     This feature is similar to the *gMSA support for non-domain-joined container hosts* feature. For more information about the Windows feature, see [gMSA architecture and improvements](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#gmsa-architecture-and-improvements) on the Microsoft Learn website.

     1. Make a user in your Active Directory domain. The user in Active Directory must have permission to access the gMSA service accounts that you use in the tasks.

     1. Create a secret in AWS Secrets Manager, after you made the user in Active Directory. For more information, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).

     1. Enter the user's username, password, and the domain into JSON key-value pairs called `username`, `password` and `domainName`, respectively.

        ```
        {"username":"{{username}}","password":"{{passw0rd}}", "domainName":"example.com"}
        ```

     1. Add configuration to the CredSpec file for the service account. The additional `HostAccountConfig` contains the Amazon Resource Name (ARN) of the secret in Secrets Manager.

        On Windows, the `PluginGUID` must match the GUID in the following example snippet. On Linux, the `PluginGUID` is ignored. Replace `MySecret` with example with the Amazon Resource Name (ARN) of your secret.

        ```
            "ActiveDirectoryConfig": {
                "HostAccountConfig": {
                    "PortableCcgVersion": "1",
                    "PluginGUID": "{859E1386-BDB4-49E8-85C7-3070B13920E1}",
                    "PluginInput": {
                        "CredentialArn": "{{arn:aws:secretsmanager:{{aws-region}}:111122223333:secret:MySecret}}"
                    }
                }
        ```

     1. The *domainless gMSA* feature needs additional permissions in the task execution role. Follow the step [(Optional) domainless gMSA secret](#linux-gmsa-domainless-secret).

1. <a name="linux-gmsa-install"></a>

**Configure instances and install `credentials-fetcher` daemon**

   You can install the `credentials-fetcher` daemon with a user data script in your EC2 Launch Template. The following examples demonstrate two types of user data, `cloud-config` YAML or bash script. These examples are for Amazon Linux 2023 (AL2023). Replace `MyCluster` with the name of the Amazon ECS cluster that you want these instances to join.
   + <a name="linux-gmsa-install-yaml"></a>

**`cloud-config` YAML**

     ```
     Content-Type: text/cloud-config
     package_reboot_if_required: true
     packages:
       # prerequisites
       - dotnet
       - realmd
       - oddjob
       - oddjob-mkhomedir
       - sssd
       - adcli
       - krb5-workstation
       - samba-common-tools
       # https://github.com/aws/credentials-fetcher gMSA credentials management for containers
       - credentials-fetcher
     write_files:
     # configure the ECS Agent to join your cluster.
     # replace MyCluster with the name of your cluster.
     - path: /etc/ecs/ecs.config
       owner: root:root
       permissions: '0644'
       content: |
         ECS_CLUSTER={{MyCluster}}
         ECS_GMSA_SUPPORTED=true
     runcmd:
     # start the credentials-fetcher daemon and if it succeeded, make it start after every reboot
     - "systemctl start credentials-fetcher"
     - "systemctl is-active credentials-fetcher && systemctl enable credentials-fetcher"
     ```
   + <a name="linux-gmsa-install-userdata"></a>

**bash script**

     If you're more comfortable with bash scripts and have multiple variables to write to `/etc/ecs/ecs.config`, use the following `heredoc` format. This format writes everything between the lines beginning with **cat** and `EOF` to the configuration file.

     ```
     #!/usr/bin/env bash
     set -euxo pipefail
     
     # prerequisites
     timeout 30 dnf install -y dotnet realmd oddjob oddjob-mkhomedir sssd adcli krb5-workstation samba-common-tools
     # install https://github.com/aws/credentials-fetcher gMSA credentials management for containers
     timeout 30 dnf install -y credentials-fetcher
     
     # start credentials-fetcher
     systemctl start credentials-fetcher
     systemctl is-active credentials-fetcher && systemctl enable credentials-fetcher
     
     cat <<'EOF' >> /etc/ecs/ecs.config
     ECS_CLUSTER={{MyCluster}}
     ECS_GMSA_SUPPORTED=true
     EOF
     ```

   There are optional configuration variables for the `credentials-fetcher` daemon that you can set in `/etc/ecs/ecs.config`. We recommend that you set the variables in the user data in the YAML block or `heredoc` similar to the previous examples. Doing so prevents issues with partial configuration that can happen with editing a file multiple times. For more information about the ECS agent configuration, see [Amazon ECS Container Agent](https://github.com/aws/amazon-ecs-agent/blob/master/README.md#environment-variables) on GitHub.
   + Optionally, you can use the variable `CREDENTIALS_FETCHER_HOST` if you change the `credentials-fetcher` daemon configuration to move the socket to another location.

**Setting up permissions and secrets**  
Do the following steps once for each application and each task definition. We recommend that you use the best practice of granting the least privilege and narrow the permissions used in the policy. This way, each task can only read the secrets that it needs.

1. <a name="linux-gmsa-domainless-secret"></a>

**(Optional) domainless gMSA secret**

   If you use the domainless method where the instance isn't joined to the domain, follow this step.

   You must add the following permissions as an inline policy to the task execution IAM role. Doing so gives the `credentials-fetcher` daemon access to the Secrets Manager secret. Replace the `MySecret` example with the Amazon Resource Name (ARN) of your secret in the `Resource` list.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "secretsmanager:GetSecretValue"
               ],
               "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret-AbCdEf"
           }
       ]
   }
   ```

------
**Note**  
If you use your own KMS key to encrypt your secret, you must add the necessary permissions to this role and add this role to the AWS KMS key policy.

1. 

**Decide if you're using SSM Parameter Store or S3 to store the CredSpec**

   Amazon ECS supports the following ways to reference the file path in the `credentialSpecs` field of the task definition.

   If you join the instances to a single domain, use the prefix `credentialspec:` at the start of the ARN in the string. If you use domainless gMSA, then use `credentialspecdomainless:`.

   For more information about the CredSpec, see [Credential specification file](#linux-gmsa-credentialspec).
   + <a name="linux-gmsa-credspec-s3"></a>

**Amazon S3 Bucket**

     Add the credential spec to an Amazon S3 bucket. Then, reference the Amazon Resource Name (ARN) of the Amazon S3 bucket in the `credentialSpecs` field of the task definition.

     ```
     {
         "family": "",
         "executionRoleArn": "",
         "containerDefinitions": [
             {
                 "name": "",
                 ...
                 "credentialSpecs": [
                     "credentialspecdomainless:arn:aws:s3:::{{${BucketName}/${ObjectName}}}"
                 ],
                 ...
             }
         ],
         ...
     }
     ```

     To give your tasks access to the S3 bucket, add the following permissions as an inline policy to the Amazon ECS task execution IAM role.

------
#### [ JSON ]

****  

     ```
     {
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
                     "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                     "arn:aws:s3:::{{amzn-s3-demo-bucket/{object}}}"
                 ]
             }
         ]
     }
     ```

------
   + <a name="linux-gmsa-credspec-ssm"></a>

**SSM Parameter Store parameter**

     Add the credential spec to an SSM Parameter Store parameter. Then, reference the Amazon Resource Name (ARN) of the SSM Parameter Store parameter in the `credentialSpecs` field of the task definition.

     ```
     {
         "family": "",
         "executionRoleArn": "",
         "containerDefinitions": [
             {
                 "name": "",
                 ...
                 "credentialSpecs": [
                     "credentialspecdomainless:arn:aws:ssm:{{aws-region}}:{{111122223333}}:parameter/{{parameter_name}}"
                 ],
                 ...
             }
         ],
         ...
     }
     ```

     To give your tasks access to the SSM Parameter Store parameter, add the following permissions as an inline policy to the Amazon ECS task execution IAM role.

------
#### [ JSON ]

****  

     ```
     {
         "Version":"2012-10-17",		 	 	 
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": [
                     "ssm:GetParameters"
                 ],
                 "Resource": "arn:aws:ssm:us-east-1:123456789012:parameter/my-parameter"
             }
         ]
     }
     ```

------

## Credential specification file
<a name="linux-gmsa-credentialspec"></a>

Amazon ECS uses an Active Directory credential specification file (*CredSpec*). This file contains the gMSA metadata that's used to propagate the gMSA account context to the Linux container. You generate the CredSpec and reference it in the `credentialSpecs` field in your task definition. The CredSpec file doesn't contain any secrets.

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
                "CredentialArn": "{{arn:aws:secretsmanager:{{aws-region}}:111122223333:secret:MySecret}}"
            }
        }
    }
}
```
<a name="linux-gmsa-credentialspec-create"></a>
**Creating a CredSpec**  
You create a CredSpec by using the CredSpec PowerShell module on a Windows computer that's joined to the domain. Follow the steps in [Create a credential spec](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#create-a-credential-spec) on the Microsoft Learn website.