

# Temporary Credentials
<a name="temporarycredentials"></a>

Some AWS services don't work when you sign in using temporary credentials. For additional information, including which AWS services work with temporary credentials, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

You are using temporary credentials if you sign in to the AWS Management Console using any method except a user name and password. For example, when you access AWS using your company's single sign-on (SSO) link, that process automatically creates temporary credentials. You also automatically create temporary credentials when you sign in to the console as a user and then switch roles. For more information about switching roles, see [Switching to a role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) in the *IAM User Guide*.

You can manually create temporary credentials using the AWS CLI or AWS API. You can then use those temporary credentials to access AWS. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com//IAM/latest/UserGuide/id_credentials_temp.html).

## Amazon DataZone portal temporary credentials
<a name="portal-temporarycredentials"></a>

When you sign into the Amazon DataZone portal, you receive temporary credentials for the AmazonDataZoneDomainExecutionRole. While you are using the AmazonDataZoneDomainExecutionRole, these credentials are automatically refreshed when used. When unused for a period of time, they expire automatically. 