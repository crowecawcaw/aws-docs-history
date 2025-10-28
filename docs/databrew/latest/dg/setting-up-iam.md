# Setting up AWS Identity and Access Management (IAM) permissions

Before you get started, you need to set up a few things in IAM. You need to be an
administrator or have help from one. However, if you have an account with administrator
access, you can do these tasks yourself. You can find simple instructions for each task in
this section.

Following is an overview of what you need to do:

- As part of this process, you add a user. You don't have to add a new user,
  you can use an existing one. You attach DataBrew permissions so that the user can
  open the DataBrew console.
- Create an IAM role. A role allows certain actions and gives permissions when it
  is used, within limits. For example, it only works for users in your AWS account.
  You can add more limitations later.
- Create the IAM policy or policies that you need. A policy is a list of things
  that a user is allowed to
  do. To create a policy, you open another console page and paste in the text
  from a file you download.

###### Note

What we provide here is basic setup information. We recommend that you take time to
customize your permissions so they meet your security and compliance needs. If you need
help, contact your administrator or AWS Support.

###### To add the required permissions

1.  Create IAM policies to enable users to run DataBrew by doing the following:

        * [Add a custom IAM
         policy for a console user](setting-up-iam-policy-for-databrew-console-access.md "setting-up-iam-policy-for-databrew-console-access.md"). If you don't need a custom policy, you can choose
         the AWS-managed policy instead. Just add it to the user in step 2. A user with these
         permissions can access the DataBrew service console.
        * [Add permissions
         for data resources](setting-up-iam-policy-for-data-resources-role.md "setting-up-iam-policy-for-data-resources-role.md"). An IAM role with these permissions can access
         data on behalf of the user.

    You need to be an administrator to create users, roles, and policies.

2.  [Add users or groups for
    DataBrew](setting-up-iam-users-and-groups-for-databrew.md "setting-up-iam-users-and-groups-for-databrew.md"). A user or group with the correct permissions attached can access the DataBrew
    console.
3.  [Add a role with permissions to access data
    for DataBrew](setting-up-iam-role-to-use-in-databrew.md "setting-up-iam-role-to-use-in-databrew.md"). A role with the correct permissions can access data on the user's behalf.
