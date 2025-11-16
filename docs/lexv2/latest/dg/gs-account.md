# Step 1: Set up an AWS Account and

create an administrator User

Before you use Amazon Lex V2 for the first time, complete the following
tasks:

1. [Sign Up for AWS](#gs-account-create "#gs-account-create")
2. [Create an IAM user](#gs-account-user "#gs-account-user")

## Sign Up for AWS

If you already have an AWS account, skip this task.

When you sign up for Amazon Web Services (AWS), your AWS account is
automatically signed up for all services in AWS, including
Amazon Lex V2. You are charged only for the services that you
use.

With Amazon Lex V2, you pay only for the resources that you use. If
you are a new AWS customer, you can get started with Amazon Lex V2
for free. For more information, see [AWS Free Usage
Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

If you already have an AWS account, skip to the next task.
If you don't have an AWS account, use the following procedure
to create one.

###### To create an AWS account

- To create an AWS account, see [How do I create and activate a new AWS account?](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html") in the AWS Knowledge Center.

Write down your AWS account ID because you'll need it for
the next task.

## Create an IAM user

Services in AWS, such as Amazon Lex V2, require that you provide
credentials when you access them so that the service can
determine whether you have permissions to access the resources
owned by that service.

Create an IAM user account to access your account for Amazon Lex V2. For comprehensive guidance on IAM user creation, see [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md") in the _IAM User Guide_.

- Use AWS Identity and Access Management (IAM) to create an IAM user
- Add the user to an IAM group with administrative
  permissions
- Grant administrative permissions to the IAM user
  that you created.

You can then access AWS using a special URL and the IAM user's
credentials.

The Getting Started exercises in this guide assume that you
have a user (`adminuser`) with administrator
privileges. Follow the procedure to create
`adminuser` in your account.

###### To create an administrator user and sign in to the

console

1. Create an administrator user called
   `adminuser` in your AWS account. For
   instructions, see [Creating Your First IAM user and Administrators
   Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
   _IAM User Guide_.
2. As a user, you can sign in to the AWS Management Console using a
   special URL. For more information, [How Users Sign In to Your Account](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md") in the
   _IAM User Guide_.
   For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

### Common Setup Issues

If you encounter issues during account setup, here are common solutions:

- **Permission Denied Errors** – Ensure your IAM user has the necessary Amazon Lex V2 permissions. For getting started, administrator permissions are recommended. For detailed information about Amazon Lex V2 permissions, see the Security section in this guide.
- **Console Access Issues** – Make sure you're signing in with the correct IAM user URL for your account, not the root AWS console. For more information about IAM best practices, see the Security section in this guide.
- **Region Availability** – Amazon Lex V2 is not available in all AWS regions. Check the [Amazon Lex endpoints and quotas](../../../general/latest/gr/lex.md "../../../general/latest/gr/lex.md") to confirm availability in your preferred region. For information about supported locales, see [Languages and locales supported by
  Amazon Lex V2](how-languages.md "how-languages.md").
- **Free Tier Limits** – Monitor your usage to stay within free tier limits: 10,000 text requests and 5,000 speech requests per month. For detailed pricing information, see [Amazon Lex Pricing](https://aws.amazon.com/lex/pricing/ "https://aws.amazon.com/lex/pricing/").
- **Quota Limits** – If you encounter service limits, review the current quotas and request increases if needed. For more information, see [Guidelines and best practices](quotas.md "quotas.md").

For additional troubleshooting help, see the Monitoring section in this guide for information about error logs and debugging.

## Grant programmatic access

For information about how to get your access key ID and secret access key, see [Understanding and getting your AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#access-keys-and-secret-access-keys") in the AWS General Reference.

### Developer Environment Setup

**For Developers:** If you plan to use the AWS CLI or SDKs, you'll also want to configure your development environment. Install the AWS CLI and configure it with your access keys. For detailed instructions, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). For SDK examples, see [Bot examples](examples.md "examples.md").

## Next step

[Step 2: Getting started
(console)](gs-console.md "gs-console.md")
