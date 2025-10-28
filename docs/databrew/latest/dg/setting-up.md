# Setting up AWS Glue DataBrew

Before you get started with AWS Glue DataBrew, you need to set up some permissions, a user, and a role.
Start by doing the following steps:

1.  Signing up for an AWS account as needed, and creating AWS Identity and Access Management (IAM) policies to
    enable users to run DataBrew:

        * Signing up for a new AWS account and adding a user. For more information, see
         [Setting up a new AWS account](setting-up-aws.md "setting-up-aws.md").
        * [Adding an IAM policy for a console user](setting-up-iam-policy-for-databrew-console-access.md "setting-up-iam-policy-for-databrew-console-access.md"). A user with these
         permissions can access DataBrew on the AWS Management Console.
        * [Adding permissions for
         data resources for an IAM role](setting-up-iam-policy-for-data-resources-role.md "setting-up-iam-policy-for-data-resources-role.md"). An IAM role with these
         permissions can access data on behalf of the user.

    You need to be an IAM administrator to create users, roles, and policies.

2.  [Adding users or groups
    for DataBrew](setting-up-iam-users-and-groups-for-databrew.md "setting-up-iam-users-and-groups-for-databrew.md"). A user or group with the correct permissions attached can
    access DataBrew on the console.
3.  [Adding a role with permissions to access data for
    DataBrew](setting-up-iam-role-to-use-in-databrew.md "setting-up-iam-role-to-use-in-databrew.md"). A role with the correct permissions can access data on the user's behalf.
