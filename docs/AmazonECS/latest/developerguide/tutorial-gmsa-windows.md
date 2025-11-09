# Using Amazon ECS Windows containers with domainless

gMSA using the AWS CLI

The following tutorial shows how to create an Amazon ECS task that runs a Windows container
that has credentials to access Active Directory with the AWS CLI. By using domainless gMSA,
the container instance isn't joined to the domain, other applications on the instance can't use
the credentials to access the domain, and tasks that join different domains can run on the same
instance.

###### Topics

- [Prerequisites](#tutorial-gmsa-windows-prerequisites "#tutorial-gmsa-windows-prerequisites")
- [Step 1: Create and configure the
  gMSA account on Active Directory Domain Services (AD DS)](#tutorial-gmsa-windows-step1 "#tutorial-gmsa-windows-step1")
- [Step 2: Upload Credentials to Secrets Manager](#tutorial-gmsa-windows-step2 "#tutorial-gmsa-windows-step2")
- [Step 3: Modify your CredSpec JSON to include
  domainless gMSA information](#tutorial-gmsa-windows-step3 "#tutorial-gmsa-windows-step3")
- [Step 4: Upload CredSpec to Amazon S3](#tutorial-gmsa-windows-step4 "#tutorial-gmsa-windows-step4")
- [Step 5: (Optional) Create an Amazon ECS
  cluster](#tutorial-gmsa-windows-step5 "#tutorial-gmsa-windows-step5")
- [Step 6: Create an IAM role for container
  instances](#tutorial-gmsa-windows-step6 "#tutorial-gmsa-windows-step6")
- [Step 7: Create a custom task execution
  role](#tutorial-gmsa-windows-step7 "#tutorial-gmsa-windows-step7")
- [Step 8: Create a task role for
  Amazon ECS Exec](#tutorial-gmsa-windows-step8 "#tutorial-gmsa-windows-step8")
- [Step 9: Register a task definition that uses
  domainless gMSA](#tutorial-gmsa-windows-step9 "#tutorial-gmsa-windows-step9")
- [Step 10: Register a Windows container instance
  to the cluster](#tutorial-gmsa-windows-step10 "#tutorial-gmsa-windows-step10")
- [Step 11: Verify the container instance](#tutorial-gmsa-windows-step11 "#tutorial-gmsa-windows-step11")
- [Step 12: Run a Windows task](#tutorial-gmsa-windows-step12 "#tutorial-gmsa-windows-step12")
- [Step 13: Verify the container has gMSA
  credentials](#tutorial-gmsa-windows-step13 "#tutorial-gmsa-windows-step13")
- [Step 14: Clean up](#tutorial-gmsa-windows-step14 "#tutorial-gmsa-windows-step14")
- [Debugging Amazon ECS domainless gMSA for
  Windows containers](#tutorial-gmsa-windows-debugging "#tutorial-gmsa-windows-debugging")

## Prerequisites

This tutorial assumes that the following prerequisites have been completed:

- The steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") have been completed.
- Your IAM user has the required permissions specified in the [AmazonECS_FullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonECS_FullAccess") IAM policy
  example.
- The latest version of the AWS CLI is installed and configured. For more information
  about installing or upgrading your AWS CLI, see [Installing the
  AWS Command Line Interface](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

You can use dual-stack service endpoints to interact with Amazon ECS from the AWS CLI, SDKs, and the Amazon ECS API over both IPv4 and IPv6. For more information, see [Using Amazon ECS dual-stack endpoints](dual-stack-endpoint.md "dual-stack-endpoint.md").

- You set up an Active Directory domain with the resources that you want your containers
  to access. Amazon ECS supports the following setups:
  - An AWS Directory Service Active Directory. AWS Directory Service is an AWS managed Active Directory that's
    hosted on Amazon EC2. For more information, see [Getting Started
    with AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started.md") in the
    _AWS Directory Service Administration Guide_.
  - An on-premises Active Directory. You must ensure that the Amazon ECS Linux container
    instance can join the domain. For more information, see [AWS Direct Connect](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-network-to-amazon.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-network-to-amazon.md").

- You have a VPC and subnets that can resolve the Active Directory domain name.
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

- (Optional) AWS CloudShell is a tool that gives customers a command line without
  needing to create their own EC2 instance. For more information, see [What is AWS CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") in
  the _AWS CloudShell User Guide_.

## Step 1: Create and configure the

gMSA account on Active Directory Domain Services (AD DS)

Create and configure a gMSA account on the Active Directory domain.

###### Note

This step creates two separate accounts: a Group Managed Service Account (gMSA) that provides
the identity for your containers, and a regular user account that is used for domain authentication.
These accounts serve different purposes and should have different names.

1. ###### Generate a Key Distribution Service root key

###### Note

If you are using AWS Directory Service, then you can skip this step.

The KDS root key and gMSA permissions are configured with your AWS
managed Microsoft AD.

If you have not already created a gMSA Service Account in your domain,
you’ll need to first generate a Key Distribution Service (KDS) root key. The KDS is
responsible for creating, rotating, and releasing the gMSA password to
authorized hosts. When the `ccg.exe` needs to retrieve gMSA
credentials, it contact KDS to retrieve the current password.

To check if the KDS root key has already been created, run the following PowerShell
cmdlet with domain admin privileges on a domain controller using the
`ActiveDirectory` PowerShell module. For more information about the module,
see [ActiveDirectory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps "https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps") on the Microsoft Learn website.

```
`PS C:\>` `Get-KdsRootKey`
```

If the command returns a key ID, you can skip the rest of this step. Otherwise, create
the KDS root key by running the following command:

```
`PS C:\>` `Add-KdsRootKey -EffectiveImmediately`
```

Although the argument `EffectiveImmediately` to the command implies the key
is effective immediately, you need to wait 10 hours before the KDS root key is replicated
and available for use on all domain controllers. 2. ###### Create the gMSA account

To create the gMSA account and allow the `ccg.exe` to
retrieve the gMSA password, run the following PowerShell commands from a
Windows Server or client with access to the domain. Replace `ExampleAccount`
with the name that you want for your gMSA account, and replace `example-domain`
with your Active Directory domain name (for example, if your domain is `contoso.com`,
use `contoso`).

    1. ```
    `PS C:\>` `Install-WindowsFeature RSAT-AD-PowerShell`
    ```
    2. ```
    `PS C:\>` `New-ADGroup -Name "`ExampleAccount` Authorized Hosts" -SamAccountName "`ExampleAccount`Hosts" -GroupScope DomainLocal`
    ```
    3. ```
    `PS C:\>` `New-ADServiceAccount -Name "`ExampleAccount`" -DnsHostName "`example-domain`" -ServicePrincipalNames "host/`ExampleAccount`", "host/`example-domain`" -PrincipalsAllowedToRetrieveManagedPassword "`ExampleAccount`Hosts"`
    ```
    4. Create a user with a permanent password that doesn't expire. These credentials are
     stored in AWS Secrets Manager and used by each task to join the domain. This is a separate user account
     from the gMSA account created above. Replace `ExampleServiceUser` with the name
     you want for this service user account.



    ```
    `PS C:\>` `New-ADUser -Name "`ExampleServiceUser`" -AccountPassword (ConvertTo-SecureString -AsPlainText "`Test123`" -Force) -Enabled 1 -PasswordNeverExpires 1`
    ```
    5. ```
    `PS C:\>` `Add-ADGroupMember -Identity "`ExampleAccount`Hosts" -Members "`ExampleServiceUser`"`
    ```
    6. Install the PowerShell module for creating CredSpec objects in Active Directory
     and output the CredSpec JSON.



    ```
    `PS C:\>` `Install-PackageProvider -Name NuGet -Force`
    ```


    ```
    `PS C:\>` `Install-Module CredentialSpec`
    ```
    7. ```
    `PS C:\>` `New-CredentialSpec -AccountName `ExampleAccount``
    ```

3. Copy the JSON output from the previous command into a file called
   `gmsa-cred-spec.json`. This is the CredSpec file. It is used in
   Step 3, [Step 3: Modify your CredSpec JSON to include
   domainless gMSA information](#tutorial-gmsa-windows-step3 "#tutorial-gmsa-windows-step3").

## Step 2: Upload Credentials to Secrets Manager

Copy the Active Directory credentials into a secure credential storage system, so that
each task retrieves it. This is the domainless gMSA method. By using domainless gMSA,
the container instance isn't joined to the domain, other applications on the instance can't use
the credentials to access the domain, and tasks that join different domains can run on the same
instance.

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

- Run the following AWS CLI command and replace the username, password, and domain name to
  match your environment. Use the service user account name (not the gMSA account name) for the username.
  Keep the ARN of the secret to use in the next step, [Step 3: Modify your CredSpec JSON to include
  domainless gMSA information](#tutorial-gmsa-windows-step3 "#tutorial-gmsa-windows-step3")

The following command uses backslash continuation characters that are
used by `sh` and compatible shells. This command isn't compatible with
PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws secretsmanager create-secret \
--name `gmsa-plugin-input` \
--description "`Amazon ECS - gMSA Portable Identity.`" \
--secret-string "{\"username\":\"`ExampleServiceUser`\",\"password\":\"`Test123`\",\"domainName\":\"`contoso.com`\"}"`
```

## Step 3: Modify your CredSpec JSON to include

domainless gMSA information

Before uploading the CredSpec to one of the storage options, add information to the
CredSpec with the ARN of the secret in Secrets Manager from the previous step. For more information,
see [Additional credential spec configuration for non-domain-joined container host use
case](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#additional-credential-spec-configuration-for-non-domain-joined-container-host-use-case "https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts#additional-credential-spec-configuration-for-non-domain-joined-container-host-use-case") on the Microsoft Learn website.

1. Add the following information to the CredSpec file inside the
   `ActiveDirectoryConfig`. Replace the ARN with the secret in Secrets Manager from the
   previous step.

Note that the `PluginGUID` value must match the GUID in the following
example snippet and is required.

```
"HostAccountConfig": {
      "PortableCcgVersion": "1",
      "PluginGUID": "{859E1386-BDB4-49E8-85C7-3070B13920E1}",
      "PluginInput": "{\"credentialArn\": \"arn:aws:secretsmanager:`aws-region`:111122223333:secret:`gmsa-plugin-input`\"}"
    }
```

You can also use a secret in SSM Parameter Store by using the ARN in this format:
`\"arn:aws:ssm:`aws-region`:111122223333:parameter/`gmsa-plugin-input`\"`. 2. After you modify the CredSpec file, it should look like the following
example:

```
{
  "CmsPlugins": [
    "ActiveDirectory"
  ],
  "DomainJoinConfig": {
    "Sid": "S-1-5-21-4066351383-705263209-1606769140",
    "MachineAccountName": "ExampleAccount",
    "Guid": "ac822f13-583e-49f7-aa7b-284f9a8c97b6",
    "DnsTreeName": "example-domain",
    "DnsName": "example-domain",
    "NetBiosName": "example-domain"
  },
  "ActiveDirectoryConfig": {
    "GroupManagedServiceAccounts": [
      {
        "Name": "ExampleAccount",
        "Scope": "example-domain"
      },
      {
        "Name": "ExampleAccount",
        "Scope": "example-domain"
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

## Step 4: Upload CredSpec to Amazon S3

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

1. Copy the CredSpec file to the computer or environment that you are running AWS CLI
   commands in.
2. Run the following AWS CLI command to upload the CredSpec to Amazon S3. Replace
   `MyBucket` with the name of your Amazon S3 bucket. You can store the file as an
   object in any bucket and location, but you must allow access to that bucket and location
   in the policy that you attach to the task execution role.

The following command uses backslash continuation characters that are
used by `sh` and compatible shells. This command isn't compatible with
PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws s3 cp gmsa-cred-spec.json \
s3://`MyBucket/ecs-domainless-gmsa-credspec``
```

## Step 5: (Optional) Create an Amazon ECS

cluster

By default, your account has an Amazon ECS cluster named `default`. This cluster is
used by default in the AWS CLI, SDKs, and AWS CloudFormation. You can use additional clusters to group and
organize tasks and infrastructure, and assign defaults for some configuration.

You can create a cluster from the AWS Management Console, AWS CLI, SDKs, or AWS CloudFormation. The settings and
configuration in the cluster don't affect gMSA.

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

```
`$` `aws ecs create-cluster --cluster-name windows-domainless-gmsa-cluster`
```

###### Important

If you choose to create your own cluster, you must specify `--cluster
 clusterName` for each command that you intend to use with that cluster.

## Step 6: Create an IAM role for container

instances

A _container instance_ is a host computer to run containers in ECS
tasks, for example Amazon EC2 instances. Each container instance registers to an Amazon ECS cluster.
Before you launch Amazon EC2 instances and register them to a cluster, you must create an IAM
role for your container instances to use.

To create the container instance role, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md"). The default `ecsInstanceRole` has sufficient
permissions to complete this tutorial.

## Step 7: Create a custom task execution

role

Amazon ECS can use a different IAM role for the permissions needed to start each task,
instead of the container instance role. This role is the _task execution
role_. We recommend creating a task execution role with only the permissions
required for ECS to run the task, also known as _least-privilege
permissions_. For more information about the principle of least privilege, see
[SEC03-BP02
Grant least privilege access](../../../wellarchitected/latest/framework/sec_permissions_least_privileges.md "../../../wellarchitected/latest/framework/sec_permissions_least_privileges.md") in the _AWS Well-Architected
Framework_.

1. To create a task execution role, see [Creating the task execution role](task_execution_IAM_role.md#create-task-execution-role "task_execution_IAM_role.md#create-task-execution-role"). The default permissions allow the
   container instance to pull container images from Amazon Elastic Container Registry and `stdout` and
   `stderr` from your applications to be logged to Amazon CloudWatch Logs.

Because the role needs custom permissions for this tutorial, you can give the role a
different name than `ecsTaskExecutionRole`. This tutorial uses
`ecsTaskExecutionRole` in further steps. 2. Add the following permissions by creating a custom policy, either an inline policy
that only exists in for this role, or a policy that you can reuse. Replace the ARN for the
`Resource` in the first statement with the Amazon S3 bucket and location, and the
second `Resource` with the ARN of the secret in Secrets Manager.

If you encrypt the secret in Secrets Manager with a custom key, you must also allow
`kms:Decrypt` for the key.

If you use SSM Parameter Store instead of Secrets Manager, you must allow
`ssm:GetParameter` for the parameter, instead of
`secretsmanager:GetSecretValue`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::`MyBucket/ecs-domainless-gmsa-credspec/gmsa-cred-spec.json`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "arn:aws:secretsmanager:us-east-1:`111122223333`:secret:`gmsa-plugin-AbCdEf`"
 }
 ]
}`

```

## Step 8: Create a task role for

Amazon ECS Exec

This tutorial uses Amazon ECS Exec to verify functionality by running a
command inside a running task. To use ECS Exec, the service or task must turn on ECS Exec and the
task role (but not the task execution role) must have `ssmmessages` permissions. For
the required IAM policy, see [ECS Exec permissions](task-iam-roles.md#ecs-exec-required-iam-permissions "task-iam-roles.md#ecs-exec-required-iam-permissions").

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

To create a task role using the AWS CLI, follow these steps.

1. Create a file called `ecs-tasks-trust-policy.json` with the
   following contents:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ecs-tasks.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Create an IAM role. You can replace the name `ecs-exec-demo-task-role`
   but keep the name for following steps.

The following command uses backslash continuation characters that are
used by `sh` and compatible shells. This command isn't compatible with
PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws iam create-role --role-name `ecs-exec-demo-task-role` \
--assume-role-policy-document file://ecs-tasks-trust-policy.json`
```

You can delete the file `ecs-tasks-trust-policy.json`. 3. Create a file called `ecs-exec-demo-task-role-policy.json` with the
following contents:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": "*"
 }
 ]
}`

```

4. Create an IAM policy and attach it to the role from the previous step.

The following command uses backslash continuation characters that are
used by `sh` and compatible shells. This command isn't compatible with
PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws iam put-role-policy \
 --role-name `ecs-exec-demo-task-role` \
 --policy-name ecs-exec-demo-task-role-policy \
 --policy-document file://ecs-exec-demo-task-role-policy.json`
```

You can delete the file
`ecs-exec-demo-task-role-policy.json`.

## Step 9: Register a task definition that uses

domainless gMSA

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

1. Create a file called `windows-gmsa-domainless-task-def.json` with
   the following contents:

```
{
  "family": "windows-gmsa-domainless-task",
  "containerDefinitions": [
    {
      "name": "windows_sample_app",
      "image": "mcr.microsoft.com/windows/servercore/iis",
      "cpu": 1024,
      "memory": 1024,
      "essential": true,
      "credentialSpecs": [
                "credentialspecdomainless:arn:aws:s3:::ecs-domainless-gmsa-credspec/gmsa-cred-spec.json"
      ],
      "entryPoint": [
        "powershell",
        "-Command"
      ],
      "command": [
        "New-Item -Path C:\\inetpub\\wwwroot\\index.html -ItemType file -Value '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>' -Force ; C:\\ServiceMonitor.exe w3svc"
      ],
      "portMappings": [
        {
          "protocol": "tcp",
          "containerPort": 80,
          "hostPort": 8080
        }
      ]
    }
  ],
  "taskRoleArn": "arn:aws:iam::111122223333:role/ecs-exec-demo-task-role",
  "executionRoleArn": "arn:aws:iam::111122223333:role/ecsTaskExecutionRole"
}
```

2. Register the task definition by running the following command:

The following command uses backslash continuation characters that are
used by `sh` and compatible shells. This command isn't compatible with
PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws ecs register-task-definition \
--cli-input-json file://`windows-gmsa-domainless-task-def.json``
```

## Step 10: Register a Windows container instance

to the cluster

Launch an Amazon EC2 Windows instance and run the ECS container agent to register it as a
container instance in the cluster. ECS runs tasks on the container instances that are
registered to the cluster that the tasks are started in.

1. To launch an Amazon EC2 Windows instance that is configured for Amazon ECS in the AWS Management Console, see
   [Launching an Amazon ECS Windows container
   instance](launch_window-container_instance.md "launch_window-container_instance.md"). Stop at the step for _user
   data_.
2. For gMSA, the user data must set the environment variable
   `ECS_GMSA_SUPPORTED` before starting the ECS container agent.

For ECS Exec, the agent must start with the argument
`-EnableTaskIAMRole`.

To secure the instance IAM role by preventing tasks from reaching the EC2 IMDS web
service to retrieve the role credentials, add the argument `-AwsvpcBlockIMDS`.
This only applies to tasks that use the `awsvpc` network mode.

```

<powershell>
[Environment]::SetEnvironmentVariable("ECS_GMSA_SUPPORTED", $TRUE, "Machine")
Import-Module ECSTools
Initialize-ECSAgent -Cluster `windows-domainless-gmsa-cluster` -EnableTaskIAMRole -AwsvpcBlockIMDS
</powershell>

```

3. Review a summary of your instance configuration in the **Summary**
   panel, and when you're ready, choose **Launch instance**.

## Step 11: Verify the container instance

You can verify that there is a container instance in the cluster using the AWS Management Console.
However, gMSA needs additional features that are indicated as
_attributes_. These attributes aren't visible in the AWS Management Console, so this
tutorial uses the AWS CLI.

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

1. List the container instances in the cluster. Container instances have an ID that is
   different from the ID of the EC2 instance.

```
`$` `aws ecs list-container-instances`
```

Output:

```
{
    "containerInstanceArns": [
        "arn:aws:ecs:aws-region:111122223333:container-instance/default/MyContainerInstanceID"
    ]
}
```

For example, `526bd5d0ced448a788768334e79010fd` is a valid container
instance ID. 2. Use the container instance ID from the previous step to get the details for the
container instance. Replace `MyContainerInstanceID` with the ID.

The following command uses backslash continuation characters that are
used by `sh` and compatible shells. This command isn't compatible with
PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws ecs describe-container-instances \
 ----container-instances MyContainerInstanceID`
```

Note that the output is very long. 3. Verify that the `attributes` list has an object with the key called
`name` and a value `ecs.capability.gmsa-domainless`. The following
is an example of the object.

Output:

```
{
    "name": "ecs.capability.gmsa-domainless"
}
```

## Step 12: Run a Windows task

Run an Amazon ECS task. If there is only 1 container instance in the cluster, you can use
`run-task`. If there are many different container instances, it might be easier
to use `start-task` and specify the container instance ID to run the task on, than
to add placement constraints to the task definition to control what type of container instance
to run this task on.

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

1. The following command uses backslash continuation characters that are
   used by `sh` and compatible shells. This command isn't compatible with
   PowerShell. You must modify the command to use it with PowerShell.

```
aws ecs run-task --task-definition windows-gmsa-domainless-task \
    --enable-execute-command --cluster windows-domainless-gmsa-cluster
```

Note the task ID that is returned by the command. 2. Run the following command to verify that the task has started. This command waits and
doesn't return the shell prompt until the task starts. Replace `MyTaskID` with
the task ID from the previous step.

```
`$` `aws ecs wait tasks-running --task MyTaskID`
```

## Step 13: Verify the container has gMSA

credentials

Verify that the container in the task has a Kerberos token. gMSA

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

1. The following command uses backslash continuation characters that are
   used by `sh` and compatible shells. This command isn't compatible with
   PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws ecs execute-command \
--task MyTaskID \
--container windows_sample_app \
--interactive \
--command powershell.exe`
```

The output will be a PowerShell prompt. 2. Run the following command in the PowerShell terminal inside the container.

```
`PS C:\>` `klist get ExampleAccount$`
```

In the output, note the `Principal` is the one that you created
previously.

## Step 14: Clean up

When you are finished with this tutorial, you should clean up the associated resources to
avoid incurring charges for unused resources.

This step uses the AWS CLI. You can run these commands in
AWS CloudShell in the default shell, which is `bash`.

1. Stop the task. Replace `MyTaskID` with the task ID from step 12, [Step 12: Run a Windows task](#tutorial-gmsa-windows-step12 "#tutorial-gmsa-windows-step12").

```
`$` `aws ecs stop-task --task `MyTaskID``
```

2. Terminate the Amazon EC2 instance. Afterwards, the container instance in the cluster will
   be deleted automatically after one hour.

You can find and terminate the instance by using the Amazon EC2 console. Or, you can run the
following command. To run the command, find the EC2 instance ID in the output of the
`aws ecs describe-container-instances` command from step 1, [Step 11: Verify the container instance](#tutorial-gmsa-windows-step11 "#tutorial-gmsa-windows-step11").
i-10a64379 is an example of an EC2 instance ID.

```
`$` `aws ec2 terminate-instances --instance-ids `MyInstanceID``
```

3. Delete the CredSpec file in Amazon S3. Replace `MyBucket` with the name of
   your Amazon S3 bucket.

```
`$` `aws s3api delete-object --bucket `MyBucket` --key `ecs-domainless-gmsa-credspec/gmsa-cred-spec.json``
```

4. Delete the secret from Secrets Manager. If you used SSM Parameter Store instead, delete the
   parameter.

The following command uses backslash continuation characters that are
used by `sh` and compatible shells. This command isn't compatible with
PowerShell. You must modify the command to use it with PowerShell.

```
`$` `aws secretsmanager delete-secret --secret-id `gmsa-plugin-input` \
 --force-delete-without-recovery`
```

5. Deregister and delete the task definition. By deregistering the task definition, you
   mark it as inactive so it can't be used to start new tasks. Then, you can delete the task
   definition.
   1. Deregister the task definition by specifying the version. ECS automatically makes
      versions of task definitions, that are numbered starting from 1. You refer to the
      versions in the same format as the labels on container images, such as
      `:1`.

   ```
   `$` `aws ecs deregister-task-definition --task-definition `windows-gmsa-domainless-task:1``
   ```

   2. Delete the task definition.

   ```
   `$` `aws ecs delete-task-definitions --task-definition `windows-gmsa-domainless-task:1``
   ```

6. (Optional) Delete the ECS cluster, if you created a cluster.

```
`$` `aws ecs delete-cluster --cluster `windows-domainless-gmsa-cluster``
```

## Debugging Amazon ECS domainless gMSA for

Windows containers

Amazon ECS task status

ECS tries to start a task exactly once. Any task that has an issue is stopped, and
set to the status `STOPPED`. There are two common types of issues with tasks.
First, tasks that couldn't be started. Second, tasks where the application has stopped
inside one of the containers. In the AWS Management Console, look at the **Stopped
reason** field of the task for the reason why the task was stopped. In the
AWS CLI, describe the task and look at the `stoppedReason`. For steps in the
AWS Management Console and AWS CLI, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md").

Windows Events

Windows Events for gMSA in containers are logged in the
`Microsoft-Windows-Containers-CCG` log file and can be found in the Event
Viewer in the section Applications and Services in
`Logs\Microsoft\Windows\Containers-CCG\Admin`. For more debugging tips, see
[Troubleshoot gMSAs for Windows containers](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/gmsa-troubleshooting#non-domain-joined-container-hosts-use-event-logs-to-identify-configuration-issues "https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/gmsa-troubleshooting#non-domain-joined-container-hosts-use-event-logs-to-identify-configuration-issues") on the Microsoft Learn
website.

ECS agent gMSA plugin

Logging for gMSA plugin for the ECS agent on the Windows container instance is in
the following directory, `C:/ProgramData/Amazon/gmsa-plugin/`. Look in this
log to see if the domainless user credentials were downloaded from the storage location,
such as Secrets Manager, and that the credential format was read correctly.
