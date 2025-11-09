AWS Blockchain Templates was discontinued on April 30, 2019. No further updates to this
service or this supporting documentation will be made. For the best Managed Blockchain experience on AWS,
we recommend that you use [Amazon Managed Blockchain
(AMB)](https://aws.amazon.com/managed-blockchain/ "https://aws.amazon.com/managed-blockchain/"). To learn more about getting started with Amazon Managed Blockchain, see our
[workshop on Hyperledger Fabric](https://catalog.us-east-1.prod.workshops.aws/workshops/008da2cb-8454-42d0-877b-bc290bff7fcf/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/008da2cb-8454-42d0-877b-bc290bff7fcf/en-US"), or our [blog on deploying an Ethereum node](https://aws.amazon.com/blogs/database/deploy-an-ethereum-node-on-amazon-managed-blockchain/ "https://aws.amazon.com/blogs/database/deploy-an-ethereum-node-on-amazon-managed-blockchain/").
If you have questions about AMB or require further support, [contact Support](https://console.aws.amazon.com/support/home#/case/create?issueType=technical "https://console.aws.amazon.com/support/home#/case/create?issueType=technical") or your AWS account team.

# Setting Up AWS Blockchain Templates

Before you start with AWS Blockchain Templates, complete the following tasks:

- [Sign Up for AWS](#blockchain-templates-sign-up-for-aws "#blockchain-templates-sign-up-for-aws")
- [Create an IAM User](#blockchain-templates-create-iam-user "#blockchain-templates-create-iam-user")
- [Create a Key Pair](#blockchain-templates-create-a-key-pair "#blockchain-templates-create-a-key-pair")
  These are fundamental prerequisites for all blockchain configurations. In addition, the
  blockchain network that you choose may have prerequisites, which vary according to your desired
  environment and configuration choices. For more information, see the relevant section for your
  blockchain template in [AWS Blockchain Templates and Features](blockchain-template-features.md "blockchain-template-features.md").

For step-by-step instructions to set up prerequisites for a private Ethereum network using an Amazon ECS cluster, see [Getting Started with AWS Blockchain Templates](blockchain-templates-getting-started.md "blockchain-templates-getting-started.md").

## Sign Up for AWS

When you sign up for AWS, your AWS account is automatically signed up for all services. You are charged only for the services that you use.

If you have an AWS account already, skip to the next task. If you don't have an AWS
account, use the following procedure to create one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Note your AWS account number. You need it when you create an IAM user in the next
task.

## Create an IAM User

Services in AWS require that you provide credentials when you access them, so that the
service can determine whether you have permissions to access its resources. The console requires
your password. You can create access keys for your AWS account to access the command line
interface or API. However, we don't recommend that you access AWS using the credentials for
your AWS account; we recommend that you use AWS Identity and Access Management (IAM) instead. Create an IAM user,
and then add the user to an IAM group with administrative permissions or grant this user
administrative permissions. You can then access AWS using a special URL and the credentials
for the IAM user.

If you signed up for AWS but have not created an IAM user for yourself, you can create
one using the IAM console. If you already have an IAM user, you can skip this step.

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                  | By                                                                                                                                                                                                                                          | You can also                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center (Recommended)        | Use short-term credentials to access AWS.This aligns with the security best<br>practices. For information about best practices, see [Security best<br>practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the<br>_AWS IAM Identity Center User Guide_.                      | Configure programmatic access by [Configuring the AWS CLI to use<br>AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM (Not recommended)                    | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                            | Following the instructions in [Create an IAM user for emergency access](../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md "../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md") in the _IAM User Guide_. | Configure programmatic access by [Manage access keys for IAM<br>users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                            |

To sign in as this new IAM user, sign out of the AWS Management Console, then use the following URL,
where _your_aws_account_id_ is your AWS account number without the hyphens
(for example, if your AWS account number is `1234-5678-9012`, your AWS account ID
is `123456789012`):

```
https://`your_aws_account_id`.signin.aws.amazon.com/console/
```

Enter the IAM user name and password that you just created. When you're signed in, the
navigation bar displays "_your_user_name_ @
_your_aws_account_id_".

If you don't want the URL for your sign-in page to contain your AWS account ID, you can
create an account alias. From the IAM dashboard, choose **Create Account
Alias** and enter an alias, such as your company name. To sign in after you create an
account alias, use the following URL:

```
https://`your_account_alias`.signin.aws.amazon.com/console/
```

To verify the sign-in link for IAM users for your account, open the IAM console and
check under **IAM users sign-in link** on the dashboard.

For more information, see the [AWS Identity and Access
Management User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

## Create a Key Pair

AWS uses public-key cryptography to secure the login information for the instances in a blockchain network. You specify the name of the key pair when you use each AWS Blockchain Template. You can then use the key pair to
access instances directly, for example, to log in using SSH.

If you already have a key pair in the right Region, you can skip this step. If you haven't
created a key pair already, you can create one using the Amazon EC2 console. Create the key pair in
the same Region that you use to launch the Ethereum network. For more information, see [Regions and Availability
Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_.

###### To create a key pair

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, select a Region for the key pair. You can select any Region
   that's available to you, regardless of your location, but key pairs are specific to a Region.
   For example, if you plan to launch an instance in the US East (Ohio) region, you must
   create a key pair for the instance in the same Region.
3. In the navigation pane, choose **Key Pairs**, **Create Key
   Pair**.
4. For **Key pair name**, enter a name for the new key pair. Choose a name
   that is easy for you to remember, such as your IAM user name, followed by
   `-key-pair`, plus the region name. For example,
   _me_-key-pair-_useast2_. Choose
   **Create**.
5. The private key file is automatically downloaded by your browser. The base file name is
   the name that you specified as the name of your key pair, and the file name extension is
   `.pem`. Save the private key file in a safe place.

###### Important

This is the only chance for you to save the private key file. You provide the name of
your key pair when you launch the Ethereum network.

For more information, see [Amazon EC2 Key
Pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide_. For more information about
connecting to EC2 instances using the key pair, see [Connect to Your Linux Instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the
_Amazon EC2 User Guide_.
