

# Prerequisites to enable Detective
<a name="detective-prerequisites"></a>

Make sure that the following requirements are met before enabling Detective.

## Granting the required Detective permissions
<a name="detective-setup-add-iam-policy"></a>

Before you can enable Detective, you must make sure that your IAM principal has the required Detective permissions. The principal can be an existing user or role that you are already using, or you can create a new user or role to use for Detective.

When you sign up for Amazon Web Services (AWS), your account is automatically signed up for all AWS services, including Amazon Detective. However, to enable and use Detective, you first have to set up permissions that allow you to access the Amazon Detective console and API operations. You or your administrator can do this by using AWS Identity and Access Management (IAM) to attach the [`AmazonDetectiveFullAccess` managed policy](security-iam-awsmanpol.md#security-iam-awsmanpol-amazondetectivefullaccess) to your IAM principal, which grants access to all Detective actions. Without these IAM permissions, you might view the **Get started with Detective** page in the AWS console. As a result, the console will not display any active graphs until these permissions are added, even if the service is enabled.

## Supported AWS Command Line Interface version
<a name="aws-cli-version"></a>

To use the AWS CLI to perform Detective tasks, the minimum required version is 1.16.303.