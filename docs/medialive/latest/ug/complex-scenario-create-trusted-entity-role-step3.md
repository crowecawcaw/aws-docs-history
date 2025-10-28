# Create roles

Any person who is an administrator can perform the procedure to create a role and attach
policies to the role.

In [Identify the access
requirements](complex-scenario-create-trusted-entity-role-step1.md "complex-scenario-create-trusted-entity-role-step1.md"), someone in your
organization identified the roles that you need to create. Create those roles now using IAM.

In this step, you create a role that consists of a trust policy ("let MediaLive call the
`AssumeRole` action") and one or more policies (the [policies that you just
created](complex-scenario-create-trusted-entity-role-step2.md "complex-scenario-create-trusted-entity-role-step2.md")). In this way, MediaLive has permission to assume the role. When it assumes the role,
it acquires the permissions specified in the policies.

Follow this procedure for each role.

1. On the IAM console, in the navigation pane on the left, choose
   **Roles**, then **Create Role**. The **Create
   role** wizard appears. This wizard walks you through the steps of setting up a
   trusted entity, and adding permissions (by adding a policy).
2. On the **Select trusted entity** page, choose the **Custom trust
   policy** card. The **Custom trust policy** section appears, with a
   sample policy.
3. Erase the sample, copy the following text, and paste the text in the **Custom
   trust policy** section. The **Custom trust policy** section now
   looks like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "medialive.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

4. Choose **Next**.
5. On the **Add Permissions** page, find the policy or policies that you
   created (for example, `MedialiveForCurlingEvents`), and select the checkbox for
   each. Then choose **Next**.
6. On the review page, enter a name for the role. We recommend that you don't use the name
   `MediaLiveAccessRole` because it is reserved for the [simple option](scenarios-for-medialive-role.md#about-simple-scenario "scenarios-for-medialive-role.md#about-simple-scenario").

Instead, use a name that includes `Medialive` and describes this role's
purpose. For example, `MedialiveAccessRoleForSports`. 7. Choose **Create role**. 8. On the **Summary** page for the role, make a note of the value in
**Role ARN**. It looks like this:

`arn:aws:iam::111122223333:role/medialiveWorkflow15`

In the example, `111122223333` is your AWS account number. 9. After you have created all the roles, make a list of the role ARNs. Include the following
information in each item:

    * The role ARN.
    * A description of the workflow that the ARN applies to.
    * The users who can work with this workflow and therefore need the ability to attach this
     trust policy to the channels that they create and edit.

You will need this list when you [set up trusted entity access](requirements-medialiverole-complex-permissions.md "requirements-medialiverole-complex-permissions.md")
for users.
