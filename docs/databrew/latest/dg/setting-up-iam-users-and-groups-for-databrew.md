# Adding users or groups with

DataBrew permissions

You assign policies to roles, and roles to users and groups to manage permissions. For
more information, see [IAM Identities (users, groups, and
roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

Before you begin, you need to have at least one user to assign permissions to.

Use the following procedure to set up DataBrew permissions for users who need to work in the DataBrew console, or run DataBrew commands in the CLI.

###### To set up DataBrew permissions

1. Create an access key for you user to use the
   AWS CLI for DataBrew, and other development tools.
2. Enable **AWS Management Console access** to allow the user to
   use the AWS console.
3. Create a role for DataBrew users or groups.
4. Choose the policy you are using. Do one of the following:
   - If you created `AwsGlueDataBrewCustomUserPolicy`, select it from the list.
   - To use the AWS-managed policy, select `AwsGlueDataBrewFullAccessPolicy` from the list.

5. Assign that policy to the role.
6. Set the Trust relationships for the role so that a user or group can assume the relevant role.
   - If you are not using groups, trust the user with the role.
   - If you are using groups, trust the group with the role and add the user to the group.
