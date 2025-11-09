AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Additional setup options for

AWS Cloud9

This topic assumes you already completed the setup steps in [Team
Setup](setup.md "setup.md") or [Enterprise Setup](setup-enterprise.md "setup-enterprise.md").

In [Team Setup](setup.md "setup.md") or [Enterprise
Setup](setup-enterprise.md "setup-enterprise.md"), you created groups and added AWS Cloud9 access permissions directly to those groups.
This is to ensure that users in those groups can access AWS Cloud9. In this topic, you add more
access permissions to restrict the kinds of environments that users in those groups can create.
This can help control costs related to AWS Cloud9 in AWS accounts and organizations.

To add these access permissions, you create your own set of policies that define the AWS
access permissions you want to enforce. We call each of these a _customer managed
policy_. Then, you attach those customer managed policies to the groups that the
users belong to. In some scenarios, you must also detach existing AWS managed policies that
are already attached to those groups. To set this up, follow the procedures in this
topic.

###### Note

The following procedures cover attaching and detaching policies for AWS Cloud9 users only.
These procedures assume you already have a separate AWS Cloud9 users group and AWS Cloud9 administrators
group. They also assume that you have only a limited number of users in the AWS Cloud9
administrators group. This AWS security best practice can help you better control, track,
and troubleshoot issues with AWS resource access.

## Step 1: Create a customer managed policy

You can create a customer managed policy using the [AWS Management Console](#setup-teams-create-policy-console "#setup-teams-create-policy-console") or the [AWS Command Line Interface (AWS CLI)](#setup-teams-create-policy-cli "#setup-teams-create-policy-cli").

###### Note

This step covers creating a customer managed policy for IAM groups only. To create a
custom permission set for groups in AWS IAM Identity Center, skip this step and follow the instructions in
[Create Permission Set](../../../singlesignon/latest/userguide/permissionsets.md#howtocreatepermissionset "../../../singlesignon/latest/userguide/permissionsets.md#howtocreatepermissionset") in the _AWS IAM Identity Center User Guide_. In this
topic, follow the instructions to create a custom permission set. For related custom
permissions policies, see [Customer managed
policy examples for teams using AWS Cloud9](setup-teams-policy-examples.md "setup-teams-policy-examples.md") later in this topic.

### Step 1.1:

Create a customer managed policy using the console

1. Sign in to the AWS Management Console, if you aren't already signed in.

We recommend you sign in using credentials for an administrator user in your
AWS account. If you can't do this, check with your AWS account administrator. 2. Open the IAM console. To do this, in the console's navigation bar, choose
**Services**. Then choose **IAM**. 3. In the service's navigation pane, choose **Policies**. 4. Choose **Create policy**. 5. In the **JSON** tab, paste one of our suggested [customer managed policy examples](setup-teams-policy-examples.md "setup-teams-policy-examples.md").

###### Note

You can also create your own customer managed policies. For more information, see
the [IAM JSON
Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_ and the
AWS service's [documentation](https://aws.amazon.com/documentation/ "https://aws.amazon.com/documentation/"). 6. Choose **Review policy**. 7. On the **Review policy** page, type a **Name** and
an optional **Description** for the policy, and then choose
**Create policy**.

Repeat this step for each additional customer managed policy that you want to create.
Then, skip ahead to [Add customer managed
policies to a group using the console](#setup-teams-add-policy-console "#setup-teams-add-policy-console").

### Step 1.2:

Create a customer managed policy using the AWS CLI

1. On the computer where you run the AWS CLI, create a file to describe the policy (for
   example, `policy.json`).

If you create the file with a different file name, substitute it throughout this
procedure. 2. Paste one of our suggested [customer
managed policy examples](setup-teams-policy-examples.md "setup-teams-policy-examples.md") into the `policy.json` file.

###### Note

You can also create your own customer managed policies. For more information, see
the [IAM JSON
Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_ and the AWS
services' [documentation](https://aws.amazon.com/documentation/ "https://aws.amazon.com/documentation/"). 3. From the terminal or command prompt, switch to the directory that contains the
`policy.json` file. 4. Run the IAM `create-policy` command, specifying a name for the policy and
the `policy.json` file.

```
aws iam create-policy --policy-document file://policy.json --policy-name MyPolicy
```

In the preceding command, replace `MyPolicy` with a name for the
policy.

Skip ahead to [Add customer managed Policies
to a Group Using the AWS CLI](#setup-teams-add-policy-cli "#setup-teams-add-policy-cli").

## Step 2: Add customer managed policies to a

group

You can add customer managed policies to a group by using the [AWS Management Console](#setup-teams-add-policy-console "#setup-teams-add-policy-console") or the [AWS Command Line Interface (AWS CLI)](#setup-teams-add-policy-cli "#setup-teams-add-policy-cli"). For more
information, see
[Customer managed policy examples for
teams using AWS Cloud9](setup-teams-policy-examples.md "setup-teams-policy-examples.md").

###### Note

This step covers adding customer managed policies to IAM groups only. To add custom
permission sets to groups in AWS IAM Identity Center, skip this step and follow the
instructions in [Assign
User Access](../../../singlesignon/latest/userguide/useraccess.md#assignusers "../../../singlesignon/latest/userguide/useraccess.md#assignusers") in the _AWS IAM Identity Center User Guide_
instead.

### Step 2.1:

Add customer managed policies to a group using the console

1. With the IAM console open from the previous procedure, in the service's navigation
   pane, choose **Groups**.
2. Choose the group's name.
3. On the **Permissions** tab, for **Managed
   Policies**, choose **Attach Policy**.
4. In the list of policy names, choose the box next to each customer managed policy
   that you want to attach to the group. If you don't see a specific policy name in the
   list, enter the policy name in the **Filter** box to display it.
5. Choose **Attach Policy**.

### Step 2.2:

Add customer managed policies to a group using the AWS CLI

###### Note

If you're using [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials"), you can't use a terminal session in the AWS Cloud9 IDE
to run some or all of the commands in this section. To address AWS security best practices,
AWS managed temporary credentials don’t allow some commands to be run. Instead, you can run those commands
from a separate installation of the AWS Command Line Interface (AWS CLI).

Run the IAM `attach-group-policy` command, specifying the group's name and
the Amazon Resource Name (ARN) of the policy.

```
aws iam attach-group-policy --group-name MyGroup --policy-arn arn:aws:iam::123456789012:policy/MyPolicy
```

In the preceding command, replace `MyGroup` with the name of the group.
Replace `123456789012` with the AWS account ID. And replace
`MyPolicy` with the name of the customer managed policy.

## Next steps

| **Task**                                                                                                                    | **See this topic**                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new<br>environment. | [Creating an environment](create-environment.md "create-environment.md")                                                   |
| Learn how to use the AWS Cloud9 IDE.                                                                                        | [Getting started: basic<br>tutorials](tutorials-basic.md "tutorials-basic.md") and [Working with the IDE](ide.md "ide.md") |
| Invite others to use your new environment along with you in real time and with text<br>chat support.                        | [Working with Shared Environments](share-environment.md "share-environment.md")                                            |
