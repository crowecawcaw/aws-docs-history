

# Adding users or groups with DataBrew permissions
<a name="setting-up-iam-users-and-groups-for-databrew"></a>

You assign policies to roles, and roles to users and groups to manage permissions. For more information, see [IAM Identities (users, groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*.

Before you begin, you need to have at least one user to assign permissions to.

Use the following procedure to set up DataBrew permissions for users who need to work in the DataBrew console, or run DataBrew commands in the CLI.

**To set up DataBrew permissions**

1. Create an access key for you user to use the AWS CLI for DataBrew, and other development tools.

1. Enable **AWS Management Console access** to allow the user to use the AWS console.

1. Create a role for DataBrew users or groups.

1. Choose the policy you are using. Do one of the following:
   + If you created `AwsGlueDataBrewCustomUserPolicy`, select it from the list.
   + To use the AWS-managed policy, select `AwsGlueDataBrewFullAccessPolicy` from the list.

1. Assign that policy to the role.

1. Set the Trust relationships for the role so that a user or group can assume the relevant role.
   + If you are not using groups, trust the user with the role.
   + If you are using groups, trust the group with the role and add the user to the group.