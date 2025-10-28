# Temporary Credentials

Some AWS services don't work when you sign in using temporary credentials. For
additional information, including which AWS services work with temporary credentials,
see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User
Guide_.

You are using temporary credentials if you sign in to the AWS Management Console using any method
except a user name and password. For example, when you access AWS using your company's
single sign-on (SSO) link, that process automatically creates temporary credentials. You
also automatically create temporary credentials when you sign in to the console as a
user and then switch roles. For more information about switching roles, see [Switching to a role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") in the _IAM User
Guide_.

You can manually create temporary credentials using the AWS CLI or AWS API. You can
then use those temporary credentials to access AWS. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md").

## Amazon DataZone portal temporary

credentials

When you sign into the Amazon DataZone portal, you receive temporary credentials for
the AmazonDataZoneDomainExecutionRole. While you are using the
AmazonDataZoneDomainExecutionRole, these credentials are automatically refreshed
when used. When unused for a period of time, they expire automatically.
