# Getting started with AWS User Experience Customization

Administrators can set colors for different AWS accounts. Account colors make it easy to differentiate
between the accounts you're currently signed in to. Organizations can use account color to distinguish between different types of accounts, for example,
you can use green for development accounts, yellow for test accounts, and red for production accounts.

###### Note

Essential features for the AWS Management Console, such as AWS User Experience Customization, AWS CloudShell, and Amazon Q, require appropriate IAM permissions. AWS managed policies provide a convenient way to grant these permissions
to users and roles used within the AWS Management Console. The following managed policies are available for use:

- `AWSManagementConsoleBasicUserAccess`
  - For non-administrative users
  - Provides access to basic console features

- `AWSManagementConsoleAdministratorAccess`

      + For administrative users
      + Provides access to essential AWS Management Console features
      + Allows administrators to configure and customize the AWS Management Console for other identities

  For more information,
  see [AWS managed policies for the AWS Management Console](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

###### To set an account color

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. On the navigation bar, choose your account name.
3. Choose **Account**.
4. In **Account display settings**, choose a color.
5. Choose **Update**.
