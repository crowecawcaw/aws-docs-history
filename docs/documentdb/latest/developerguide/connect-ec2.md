# Connect using Amazon EC2

This section describes how to set up connectivity between an Amazon DocumentDB cluster and Amazon EC2 and access the Amazon DocumentDB cluster from the Amazon EC2 instance.

There are two options for configuring the EC2 connection:

- [Automatically connect your EC2 instance to an Amazon DocumentDB database](connect-ec2-auto.md "connect-ec2-auto.md") — Use the automatic connection feature in the EC2 console to automatically configure the connection between your EC2 instance and a new or existing Amazon DocumentDB database.
  This connection allows traffic to travel between the EC2 instance and the Amazon DocumentDB database. This option is typically used for testing and creating new security groups.
- [Manually connect your EC2 instance to your Amazon DocumentDB database](connect-ec2-manual.md "connect-ec2-manual.md") — Configure the connection between your EC2 instance to your Amazon DocumentDB database by manually configuring and assigning the security groups to reproduce the configuration that is created by the automatic connection feature.
  This option is typically used for changing more advanced settings and using exisitng security groups.

## Prerequisites

Regardless of the option, and before you create your first Amazon DocumentDB cluster, you must do the
following:

**Create an Amazon Web Services (AWS) account**

Before you can begin using Amazon DocumentDB, you must have an
Amazon Web Services (AWS) account. The AWS account is free.
You pay only for the services and resources that you use.

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

**Optionally, set up the needed AWS Identity and Access Management (IAM) permissions.**

Access to manage Amazon DocumentDB resources such as clusters,
instances, and cluster parameter groups requires
credentials that AWS can use to authenticate your
requests. For more information, see [Identity and Access Management for Amazon DocumentDB](security-iam.md "security-iam.md").

1. In the search bar of the AWS Management Console, type in IAM and select **IAM** in the drop down menu that appears.
2. Once you're in the IAM console, select **Users** from the navigation pane.
3. Select your username.
4. Click the button **Add permissions**.
5. Select **Attach existing policies directly**.
6. Type `AmazonDocDBFullAccess` in the search bar and select it once it appears in the search results.
7. Click the blue button at the bottom that says **Next: Review**.
8. Click the blue button at the bottom that says **Add permissions**.

**Create an Amazon Virtual Private Cloud (Amazon VPC)**

Depending on which AWS Region you are in, you may or may not have a default VPC already created. If you don't have a default VPC, complete step 1 of the [Getting Started with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md")
in the _Amazon VPC User Guide_. This will take less than five minutes.
