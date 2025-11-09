AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Calling AWS services from an environment in AWS Cloud9

You can call AWS services from an AWS Cloud9 development environment. For example, you can do the following
actions:

- Upload and download data in Amazon Simple Storage Service (Amazon S3) buckets.
- Send broadcast notifications through Amazon Simple Notification Service (Amazon SNS) topics.
- Read and write data in Amazon DynamoDB (DynamoDB) databases.
  You can call AWS services from your environment in several ways. For example, you can use the
  AWS Command Line Interface (AWS CLI) or the AWS CloudShell to run commands from a terminal session. You can also call
  AWS services from code you run within your environment. You can do this by using AWS SDKs for
  programming languages such as JavaScript, Python,
  Ruby, PHP, Go, and C++. For
  more information, see the [AWS CLI and aws-shell Sample](sample-aws-cli.md "sample-aws-cli.md"),
  the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"), and the [AWS SDKs](https://aws.amazon.com/developer/tools/#sdk "https://aws.amazon.com/developer/tools/#sdk").

Each time the AWS CLI, the AWS CloudShell, or your code calls an AWS service, the AWS CLI, the
AWS CloudShell, or your code must provide a set of AWS access credentials along with the call.
These credentials determine whether the caller has the appropriate permissions to make the
call. If the credentials don't cover the appropriate permissions, the call fails.

There are several ways to provide credentials to your environment. The following table describes
some approaches.

| Environment type | Approach                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EC2              | Use AWS managed temporary credentials.<br>We recommend this approach for an EC2 environment. AWS managed temporary credentials manage AWS access<br>credentials in an EC2 environment on your behalf, while also following AWS security<br>best practices.<br>**If you're using an EC2 environment, you can skip the rest<br>of this topic. This is because AWS managed temporary credentials are already<br>set up for you in the environment.**<br>For more information, see [AWS Managed<br>Temporary Credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials"). |
| EC2              | Attach an IAM instance profile to the instance.<br>Only use this approach if for some reason you can't use AWS managed temporary credentials.<br>Similar to AWS managed temporary credentials, an instance profile manages AWS access credentials<br>on your behalf. However, you must create, manage, and attach the instance<br>profile to the Amazon EC2 instance yourself.<br>For instructions, see [Create and Use<br>an Instance Profile to Manage Temporary Credentials](#credentials-temporary "#credentials-temporary").                                                                                                                                     |
| EC2 or SSH       | Store your permanent AWS access credentials within the environment.<br>This approach is less secure than using temporary AWS access credentials.<br>However, it's the only supported approach for an SSH environment.<br>For instructions, see [Create<br>and Store Permanent Access Credentials in an Environment](#credentials-permanent-create "#credentials-permanent-create").                                                                                                                                                                                                                                                                                   |
| EC2 or SSH       | Insert your permanent AWS access credentials directly into your code.<br>We discourage this approach because it doesn't follow AWS security best<br>practices.<br>Because we discourage this approach, we do not cover it in this<br>topic.                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Create and use an instance profile to manage temporary

credentials

###### Note

You can't use this procedure for an AWS Cloud9 SSH development environment. Instead, skip ahead to [Create and Store Permanent Access Credentials
in an Environment](#credentials-permanent-create "#credentials-permanent-create").

We recommend that you use AWS managed temporary credentials instead of an instance profile. Follow these
instructions only if for some reason you can't use AWS managed temporary credentials. For more information,
see [AWS Managed
Temporary Credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials").

This procedure uses IAM and Amazon EC2 to create and attach an IAM instance profile to
the Amazon EC2 instance that connects to your environment. This instance profile manages temporary
credentials on your behalf. This procedure assumes you have already created an environment in
AWS Cloud9. To create an environment, see [Create an
Environment](create-environment.md "create-environment.md").

You can complete these tasks with the [IAM and Amazon EC2 consoles](#credentials-temporary-create-console "#credentials-temporary-create-console") or the
[AWS Command Line Interface (AWS CLI)](#credentials-temporary-create-cli "#credentials-temporary-create-cli").

### Create an instance profile with the

IAM console

###### Note

If you already have an IAM role that contains an instance profile, skip ahead to
[Attach an Instance Profile to
an Instance with the Amazon EC2 Console](#credentials-temporary-attach-console "#credentials-temporary-attach-console").

1. Sign in to the IAM console, at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").

For this step, we recommend you sign in using administrator-level credentials
in your AWS account. If you can't do this, check with your AWS account
administrator. 2. In the navigation bar, choose **Roles**.

###### Note

You cannot use the IAM console to create an instance profile by itself.
You must create an IAM role, which contains an instance profile. 3. Choose **Create role**. 4. On the **Select type of trusted entity** page, with
**AWS service** already chosen, for **Choose the
service that will use this role**, choose
**EC2**. 5. For **Select your use case**, choose
**EC2**. 6. Choose **Next: Permissions**. 7. On the **Attach permissions policies** page, in the list of
policies, select the box next to **AdministratorAccess**, and
then choose **Next: Review**.

###### Note

The **AdministratorAccess** policy allows unrestricted
access to all AWS actions and resources across your AWS account. Use it
only for experimentation purposes. For more information, see [IAM
Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_. 8. On the **Review** page, for **Role Name**,
enter a name for the role (for example,
`my-demo-cloud9-instance-profile`). 9. Choose **Create Role**.

Skip ahead to [Attach an Instance
Profile to an Instance with the Amazon EC2 Console](#credentials-temporary-attach-console "#credentials-temporary-attach-console").

### Create an instance profile with the

AWS CLI

###### Note

If you already have an IAM role that contains an instance profile, skip ahead to
[Attach an Instance Profile to an
Instance with the AWS CLI](#credentials-temporary-attach-cli "#credentials-temporary-attach-cli").

For this topic, we recommend you configure the AWS CLI using administrator-level
credentials in your AWS account. If you can't do this, check with your
AWS account administrator.

###### Note

If you're using [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials"), you can't use a terminal session in the AWS Cloud9 IDE
to run some or all of the commands in this section. To address AWS security best practices,
AWS managed temporary credentials don’t allow some commands to be run. Instead, you can run those commands
from a separate installation of the AWS Command Line Interface (AWS CLI).

1. Define a trust relationship in AWS for the instance profile's required IAM
   role. To do this, create and then save a file with the following contents (for
   example,
   `my-demo-cloud9-instance-profile-role-trust.json`).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ec2.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Using the terminal or command prompt, switch to the directory where you just
   saved this file.
3. Create an IAM role for the instance profile. To do this, run the IAM
   `create-role` command. When you do, specify a name for the new IAM
   role (for example, `my-demo-cloud9-instance-profile-role`), and the
   name of the file that you just saved.

```
aws iam create-role --role-name my-demo-cloud9-instance-profile-role --assume-role-policy-document file://my-demo-cloud9-instance-profile-role-trust.json
```

4. Attach AWS access permissions to the instance profile IAM role. To do this,
   run the IAM `attach-role-policy` command. Specify the name of the
   existing IAM role and the Amazon Resource Name (ARN) of the AWS managed policy
   that's named `AdministratorAccess`.

```
aws iam attach-role-policy --role-name my-demo-cloud9-instance-profile-role --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

###### Note

The **AdministratorAccess** policy allows unrestricted
access to all AWS actions and resources across your AWS account. Use it
only for experimentation purposes. For more information, see [IAM
Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_. 5. Create the instance profile. To do this, run the IAM
`create-instance-profile` command, specifying a name for the new
instance profile (for example,
`my-demo-cloud9-instance-profile`).

```
aws iam create-instance-profile --instance-profile-name my-demo-cloud9-instance-profile
```

6. Attach the IAM role to the instance profile. To do this, run the IAM
   `add-role-to-instance-profile`, specifying the names of the existing
   IAM role and instance profile.

```
aws iam add-role-to-instance-profile --role-name my-demo-cloud9-instance-profile-role --instance-profile-name my-demo-cloud9-instance-profile
```

Skip ahead to Create an Instance
Profile with the AWS CLI.

### Attach an instance profile to an

instance with the Amazon EC2 console

1. Sign in to the Amazon EC2 console, at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").

For this step, we recommend that you sign in using administrator-level
credentials in your AWS account. If you can't do this, check with your
AWS account administrator. 2. In the navigation bar, make sure that the Region selector displays the
AWS Region that matches the one for your environment. For example, if you created your
environment in the US East (Ohio) Region, choose **US East (Ohio)** in the
Region selector here. 3. Choose the **Running Instances** link or, in the navigation
pane, expand **Instances**, and then choose
**Instances**. 4. In the list of instances, choose the instance with the
**Name** that includes your environment name. For example, if your
environment name is `my-demo-environment`, choose the instance with the
**Name** that includes
**my-demo-environment**. 5. Choose **Actions**, **Security**,
**Modify IAM role**.

###### Note

Although you are attaching a role to the instance, the role contains an
instance profile. 6. On the **Modify IAM role** page, for **IAM
role**, choose the name of the role you identified or that you created
in the previous procedure, and then choose **Apply**. 7. Back in the environment, use the AWS CLI to run the `aws configure` command
or the AWS CloudShell to run the `configure` command. Don't specify any
values for **AWS Access Key ID** or **AWS Secret
Access Key** (press `Enter` after each of these prompts).
For **Default Region name**, specify the AWS Region closest to
you or the Region where your AWS resources are located. For example,
`us-east-2` for the US East (Ohio) Region. For a list of Regions, see
[AWS Regions and
Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_. Optionally,
specify a value for **Default output format** (for example,
`json`).

You can now start calling AWS services from your environment. To use the AWS CLI, the
aws-shell, or both to call AWS services, see the [AWS CLI and aws-shell Sample](sample-aws-cli.md "sample-aws-cli.md"). To call AWS services
from your code, see our other [tutorials and
samples](tutorials.md "tutorials.md").

### Attach an instance profile to an

instance with the AWS CLI

###### Note

If you're using [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials"), you can't use a terminal session in the AWS Cloud9 IDE
to run some or all of the commands in this section. To address AWS security best practices,
AWS managed temporary credentials don’t allow some commands to be run. Instead, you can run those commands
from a separate installation of the AWS Command Line Interface (AWS CLI).

1. Run the Amazon EC2 `associate-iam-instance-profile` command. Specify
   the name of the instance profile and the ID and AWS Region ID of the Amazon EC2
   instance for the environment.

```
aws ec2 associate-iam-instance-profile --iam-instance-profile Name=my-demo-cloud9-instance-profile --region us-east-2 --instance-id i-12a3b45678cdef9a0
```

In the preceding command, replace `us-east-2` with the AWS Region
ID for the instance and `i-12a3b45678cdef9a0` with the instance
ID.

To get the instance ID, you can, for example, run the Amazon EC2
`describe-instances` command, specifying the name and AWS Region
ID of the environment.

```
aws ec2 describe-instances --region us-east-2 --filters Name=tag:Name,Values=*my-environment* --query "Reservations[*].Instances[*].InstanceId" --output text
```

In the preceding command, replace `us-east-2` with the AWS Region
ID for the instance and `my-environment` with the name of the
environment. 2. Back in the environment, use the AWS CLI to run the `aws configure` command
or the aws-shell to run the `configure` command. Don't
specify any values for **AWS Access Key ID** or **AWS
Secret Access Key**. Press `Enter` after each of these
prompts. For **Default Region name**, specify the AWS Region
closest to you or the Region where your AWS resources are located. For example,
`us-east-2` for the US East (Ohio) Region. For a list of Regions, see
[AWS Regions and
Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_. Optionally,
specify a value for **Default output format** (for example,
`json`).

You can now start calling AWS services from your environment. To use the AWS CLI, the
aws-shell, or both to call AWS services, see the [AWS CLI and aws-shell Sample](sample-aws-cli.md "sample-aws-cli.md"). To call AWS services
from your code, see our other [tutorials and
samples](tutorials.md "tutorials.md").

## Create and store permanent access credentials

in an Environment

###### Note

If you're using an AWS Cloud9 EC2 development environment, we recommend that you use AWS managed temporary credentials instead of
AWS permanent access credentials. To work with AWS managed temporary credentials, see [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials").

In this section, you use AWS Identity and Access Management (IAM) to generate a set of permanent credentials.
The AWS CLI, the aws-shell, or your code can use this set of credentials when
calling AWS services. This set includes an AWS access key ID and an AWS secret access
key, which are unique to your user in your AWS account. If you already have an AWS
access key ID and an AWS secret access key, note those credentials, and then skip ahead
to [Store Permanent Access Credentials in
an Environment](#credentials-permanent-create-store "#credentials-permanent-create-store").

You can create a set of permanent credentials with the [IAM console](#credentials-permanent-create-console "#credentials-permanent-create-console") or the [AWS CLI](#credentials-permanent-create-cli "#credentials-permanent-create-cli").

### Grant programmatic access

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

### Create permanent access credentials with

the AWS CLI

###### Note

For this section, we recommend that you configure the AWS CLI using
administrator-level credentials in your AWS account. If you can't do this, check
with your AWS account administrator.

###### Note

If you're using [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials"), you can't use a terminal session in the AWS Cloud9 IDE
to run some or all of the commands in this section. To address AWS security best practices,
AWS managed temporary credentials don’t allow some commands to be run. Instead, you can run those commands
from a separate installation of the AWS Command Line Interface (AWS CLI).

Run the IAM `create-access-key` command to create a new AWS access key and
corresponding AWS secret access key for the user.

```
aws iam create-access-key --user-name MyUser
```

In the preceding command, replace `MyUser` with the name of the
user.

In a secure location, save the `AccessKeyId` and
`SecretAccessKey` values that are displayed. After you run the IAM
`create-access-key` command, this is the only time you can use the AWS CLI
to view the user's AWS secret access key. To generate a new AWS secret access key for
the user later if needed, see [Creating, Modifying, and Viewing Access Keys (API, CLI, PowerShell)](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey_CLIAPI "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_CreateAccessKey_CLIAPI") in the
_IAM User Guide_.

### Store permanent access credentials in

an Environment

In this procedure, you use the AWS Cloud9 IDE to store your permanent AWS access
credentials in your environment. This procedure assumes you already created an environment in AWS Cloud9,
opened the environment, and are displaying the AWS Cloud9 IDE in your web browser. For more
information, see [Creating an Environment](create-environment.md "create-environment.md") and
[Opening an Environment](open-environment.md "open-environment.md").

###### Note

The following procedure shows how to store your permanent access credentials by
using environment variables. If you have the AWS CLI or the aws-shell
installed in your environment, you can use the **`aws configure`** command for the AWS CLI or the **`configure`** command for the aws-shell to store your permanent access
credentials instead. For instructions, see [Quick Configuration](../../../cli/latest/userguide/cli-chap-getting-started.md#cli-quick-configuration "../../../cli/latest/userguide/cli-chap-getting-started.md#cli-quick-configuration") in the _AWS Command Line Interface User Guide_.

1. With your environment open, in the AWS Cloud9 IDE, start a new terminal session, if one is
   not already started. To start a new terminal session, on the menu bar, choose
   **Window**, **New Terminal**.
2. Run each of the following commands, one command at a time, to set local
   environment variables representing your permanent access credentials. In these
   commands, after `AWS_ACCESS_KEY_ID:`, enter your AWS access key ID.
   After `AWS_SECRET_ACCESS_KEY`, enter your AWS secret access key.
   After `AWS_DEFAULT_REGION_ID`, enter the AWS Region identifier
   associated with the AWS Region closest to you (or your preferred AWS Region).
   For a list of available identifiers, see [AWS Regions and
   Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_. For example, for
   the US East (Ohio), you use `us-east-2`.

```
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=
```

3. Note that the preceding environment variables are valid only for the current
   terminal session. To make these environment variables available across terminal
   sessions, you must add them to your shell profile file as user environment
   variables, as follows.
   1. In the **Environment** window of the IDE, choose the
      gear icon, and then choose **Show Home in Favorites**.
      Repeat this step and choose **Show Hidden Files** as
      well.
   2. Open the `~/.bashrc` file.
   3. Enter or paste the following code at the end of the file. In these
      commands, after `AWS_ACCESS_KEY_ID:`, enter your AWS access key
      ID. After `AWS_SECRET_ACCESS_KEY`, enter your AWS secret access
      key. After `AWS_DEFAULT_REGION_ID`, enter the AWS Region
      identifier associated with the AWS Region closest to you (or your
      preferred AWS Region). For a list of available identifiers, see [AWS Regions and
      Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_. For
      example, for the US East (Ohio) Region, you use `us-east-2`.

   ```
   export AWS_ACCESS_KEY_ID=
   export AWS_SECRET_ACCESS_KEY=
   export AWS_DEFAULT_REGION=
   ```

   4. Save the file.
   5. Source the `~/.bashrc` file to load these new
      environment variables.

   ```
   . ~/.bashrc
   ```

You can now start calling AWS services from your environment. To use the AWS CLI or the
aws-shell to call AWS services, see the [AWS CLI and aws-shell Sample](sample-aws-cli.md "sample-aws-cli.md"). To call AWS services
from your code, see our other [tutorials and
samples](tutorials.md "tutorials.md").
