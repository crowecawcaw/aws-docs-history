

# Obtaining IAM permissions for AWS CloudShell
<a name="cloudshell-permissions"></a>

Using the access management resources provided by AWS Identity and Access Management, administrators can grant permissions to IAM users so they can access AWS CloudShell and use the environment's features.

The quickest way for an administrator to grant access to users is through an AWS managed policy. An [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) is a standalone policy that's created and administered by AWS. The following AWS managed policy for CloudShell can be attached to IAM identities:
+ `AWSCloudShellFullAccess`: Grants permission to use AWS CloudShell with full access to all features.

 If you want to limit the scope of actions that an IAM user can perform with AWS CloudShell, you can create a custom policy that uses the `AWSCloudShellFullAccess` managed policy as a template. For more information about limiting the actions that are available to users in CloudShell, see [Managing AWS CloudShell access and usage with IAM policies](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html) in the *AWS CloudShell User Guide*.

**Note**  
Your IAM identity also requires a policy that grants permission to make calls to Security Incident Response.