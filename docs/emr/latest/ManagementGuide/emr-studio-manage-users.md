# Assign and manage EMR Studio users

After you create an EMR Studio, you can assign users and groups to it. The method
you use to assign, update, and remove users depends on the Studio authentication
mode.

- When you use IAM authentication mode, you configure EMR Studio user assignment
  and permissions in IAM or with IAM and your identity provider.
- With IAM Identity Center authentication mode, you use the Amazon EMR management console or the AWS CLI to
  manage users.
  To learn more about authentication for Amazon EMR Studio, see [Choose an authentication mode for
  Amazon EMR Studio](emr-studio-authentication.md "emr-studio-authentication.md").

## Assign a user or group to an

EMR Studio

IAM
When you use [Set up IAM authentication mode for
Amazon EMR Studio](emr-studio-authentication.md#emr-studio-iam-authentication "emr-studio-authentication.md#emr-studio-iam-authentication"), you must allow the
`CreateStudioPresignedUrl` action in a user's IAM permissions policy
and restrict the user to a particular Studio. You can include
`CreateStudioPresignedUrl` in your [User permissions for IAM authentication
mode](how-emr-studio-works.md#emr-studio-iam-authorization "how-emr-studio-works.md#emr-studio-iam-authorization") or use a separate policy.

To restrict a user to a Studio (or set of Studios), you can use
attribute-based access control (ABAC) or specify the Amazon Resource Name (ARN) of a
Studio in the `Resource` element of the permissions policy.

###### Example Assign a user to a Studio using a Studio ARN

The following example policy gives a user access to a particular
EMR Studio by allowing the `CreateStudioPresignedUrl` action and
specifying the Studio's Amazon Resource Name (ARN) in the
`Resource` element.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateStudioPresignedUrl",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreateStudioPresignedUrl"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:123456789012:studio/studio-id"
 ]
 }
 ]
}`

```

###### Example Assign a user to a Studio with ABAC for IAM authentication

There are multiple ways to configure attribute-based access control (ABAC) for
a Studio. For example, you might attach one or more tags to an
EMR Studio, and then create an IAM policy that restricts the
`CreateStudioPresignedUrl` action to a particular Studio or
set of Studios with those tags.

You can add tags during or after Studio creation. To add tags to an
existing Studio, you can use the [AWS CLI`emr add-tags`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-tags.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-tags.html") command. The following example adds a
tag with the key-value pair `Team = Data Analytics` to an
EMR Studio.

```
aws emr add-tags --resource-id `<example-studio-id>` --tags Team="Data Analytics"
```

The following example permissions policy allows the
`CreateStudioPresignedUrl` action for EMR Studios with the tag
key-value pair `Team = DataAnalytics`. For more information about using
tags to control access, see [Controlling access to and for a
users and roles using tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md") or [Controlling access to AWS
resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateStudioPresignedUrl",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreateStudioPresignedUrl"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:studio/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/Team": "Data Analytics"
 }
 }
 }
 ]
}`

```

###### Example Assign a user to a Studio using the aws:SourceIdentity global

condition key

When you use IAM federation, you can use the global condition key
`aws:SourceIdentity` in a permissions policy to give users
Studio access when they assume your IAM role for federation.

You must first configure your identity provider (IdP) to return an identifying
string, such as an email address or username, when a user authenticates and
assumes your IAM role for federation. IAM sets the global condition key
`aws:SourceIdentity` to the identifying string returned by your
IdP.

For more information, see the [How to
relate IAM role activity to corporate identity](https://aws.amazon.com/blogs/security/how-to-relate-iam-role-activity-to-corporate-identity/ "https://aws.amazon.com/blogs/security/how-to-relate-iam-role-activity-to-corporate-identity/") blog post in the AWS
Security Blog and the [aws:SourceIdentity](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceidentity "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceidentity") entry in the global condition keys reference.

The following example policy allows the `CreateStudioPresignedUrl`
action and gives users with an `aws:SourceIdentity` that matches the
`<example-source-identity>` access to the
EMR Studio specified by
`<example-studio-arn>`.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreateStudioPresignedUrl"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:123456789012:studio/studio-name"
 ],
 "Condition": {
 "StringLike": {
 "aws:SourceIdentity": "example-source-identity"
 }
 },
 "Sid": "AllowELASTICMAPREDUCECreatestudiopresignedurl"
 }
 ]
}`

```

IAM Identity Center
When you assign a user or group to an EMR Studio, you specify a session
policy that defines fine-grained permissions, such as the ability to create a new
EMR cluster, for that user or group. Amazon EMR stores these session policy mappings.
You can update a user or group's session policy after assignment.

###### Note

The final permissions for a user or group is an intersection of the
permissions defined in your EMR Studio user role and the permissions defined
in the session policy for that user or group. If a user belongs to more than one
group assigned to the Studio, EMR Studio uses a union of permissions
for that user.

###### To assign users or groups to an EMR Studio using the Amazon EMR

console

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](whats-new-in-console.md#console-opt-in "whats-new-in-console.md#console-opt-in").
2. Choose **EMR Studio** from the left navigation.
3. Choose your Studio name from the
   **Studios** list, or select the Studio and
   choose **View details**, to open the Studio detail
   page.
4. Choose **Add Users** to see the **Users**
   and **Groups** search table.
5. Select the **Users** tab or the **Groups**
   tab, and enter a search term in the search bar to find a user or group.
6. Select one or more users or groups from the search results list. You can
   switch back and forth between the **Users** tab and the
   **Groups** tab.
7. After you select users and groups to add to the Studio, choose
   **Add**. You should see the users and groups appear in the
   **Studio users** list. It might take a few seconds
   for the list to refresh.
8. Follow the instructions in [Update permissions for a user or group assigned
   to a Studio](#emr-studio-update-user "#emr-studio-update-user") to refine the Studio
   permissions for a user or group.

**To assign a user or group to an EMR Studio using the
AWS CLI**

Insert your own values for the following
`create-studio-session-mapping` arguments. For more information about
the `create-studio-session-mapping` command, see the [_AWS CLI
Command Reference_](../../../cli/latest/reference/emr/create-studio-session-mapping.md "../../../cli/latest/reference/emr/create-studio-session-mapping.md").

- **`--studio-id`** –
  The ID of the Studio you want to assign the user or group to. For
  instructions on how to retrieve a Studio ID, see [View Studio details](emr-studio-manage-studio.md#emr-studio-get-studio-id "emr-studio-manage-studio.md#emr-studio-get-studio-id").
- `**--identity-name**`
  – The name of the user or group from the Identity Store. For more
  information, see [UserName](../../../singlesignon/latest/IdentityStoreAPIReference/API_User.md#singlesignon-Type-User-UserName "../../../singlesignon/latest/IdentityStoreAPIReference/API_User.md#singlesignon-Type-User-UserName") for users and [DisplayName](../../../singlesignon/latest/IdentityStoreAPIReference/API_Group.md#singlesignon-Type-Group-DisplayName "../../../singlesignon/latest/IdentityStoreAPIReference/API_Group.md#singlesignon-Type-Group-DisplayName") for groups in the _Identity Store API
  Reference_.
- **`--identity-type`**
  – Use either `USER` or `GROUP` to specify the
  identity type.
- **`--session-policy-arn`**
  – The Amazon Resource Name (ARN) for the session policy you want to
  associate with the user or group. For example, `**arn:aws:iam::`<aws-account-id>`:policy/`EMRStudio_Advanced_User_Policy`**`.
  For more information, see [Create permissions policies for
  EMR Studio users](emr-studio-user-permissions.md#emr-studio-permissions-policies "emr-studio-user-permissions.md#emr-studio-permissions-policies").

```
aws emr create-studio-session-mapping \
 --studio-id `<example-studio-id>` \
 --identity-name `<example-identity-name>` \
 --identity-type `<USER-or-GROUP>` \
 --session-policy-arn `<example-session-policy-arn>`
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

Use the `get-studio-session-mapping` command to verify the new
assignment. Replace `<example-identity-name>` with the
IAM Identity Center name of the user or group that you updated.

```
aws emr get-studio-session-mapping \
 --studio-id `<example-studio-id>` \
 --identity-type `<USER-or-GROUP>` \
 --identity-name `<user-or-group-name>` \
```

## Update permissions for a user or group assigned

to a Studio

IAM
To update user or group permissions when you use IAM authentication mode, use
IAM to change the IAM permissions policies attached to your IAM identities
(users, groups, or roles).

For more information, see [User permissions for IAM authentication
mode](how-emr-studio-works.md#emr-studio-iam-authorization "how-emr-studio-works.md#emr-studio-iam-authorization").

IAM Identity Center

###### \*\*To update EMR Studio permissions for a user or

group using the console\*\*

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](whats-new-in-console.md#console-opt-in "whats-new-in-console.md#console-opt-in").
2. Choose **EMR Studio** from the left navigation.
3. Choose your Studio name from the
   **Studios** list, or select the Studio and
   choose **View details**, to open the Studio detail
   page.
4. In the **Studio users** list on the Studio
   detail page, search for the user or group you want to update. You can search by
   name or identity type.
5. Select the user or group that you want to update and choose **Assign
   policy** to open the **Session policy** dialog
   box.
6. Select a policy to apply to the user or group that you chose in step 5, and
   choose **Apply policy**. The **Studio
   users** list should display the policy name in the **Session
   policy** column for the user or group that you updated.

**To update EMR Studio permissions for a user or group
using the AWS CLI**

Insert your own values for the following
`update-studio-session-mappings` arguments. For more information about
the `update-studio-session-mappings` command, see the [_AWS CLI
Command Reference_](../../../cli/latest/reference/emr/update-studio-session-mapping.md "../../../cli/latest/reference/emr/update-studio-session-mapping.md").

```
aws emr update-studio-session-mapping \
 --studio-id `<example-studio-id>` \
 --identity-name `<name-of-user-or-group-to-update>` \
 --session-policy-arn `<new-session-policy-arn-to-apply>` \
 --identity-type `<USER-or-GROUP>` \
```

Use the `get-studio-session-mapping` command to verify the new
session policy assignment. Replace
`<example-identity-name>` with the IAM Identity Center name of the
user or group that you updated.

```
aws emr get-studio-session-mapping \
 --studio-id `<example-studio-id>` \
 --identity-type `<USER-or-GROUP>` \
 --identity-name `<user-or-group-name>` \
```

## Remove a user or group from a

Studio

IAM
To remove a user or group from an EMR Studio when you use IAM
authentication mode, you must revoke the user's access to the Studio by
reconfiguring the user's IAM permissions policy.

In the following example policy, assume that you have an EMR Studio with the
tag key-value pair `Team = Quality Assurance`. According to the policy,
the user can access Studios tagged with the `Team` key whose
value is equal to either `Data Analytics` or `Quality
 Assurance`. To remove the user from the Studio tagged with
`Team = Quality Assurance`, remove `Quality Assurance` from
the list of tag values.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateStudioPresignedUrl",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:CreateStudioPresignedUrl"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:123456789012:studio/*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticmapreduce:ResourceTag/Team": [
 "Data Analytics",
 "Quality Assurance"
 ]
 }
 }
 }
 ]
}`

```

IAM Identity Center

###### \*\*To remove a user or group from an EMR Studio using

the console\*\*

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](whats-new-in-console.md#console-opt-in "whats-new-in-console.md#console-opt-in").
2. Choose **EMR Studio** from the left navigation.
3. Choose your Studio name from the
   **Studios** list, or select the Studio and
   choose **View details**, to open the Studio detail
   page.
4. In the **Studio users** list on the Studio
   detail page, find the user or group you want to remove from the Studio.
   You can search by name or identity type.
5. Select the user or group that you want to delete, choose
   **Delete** and confirm. The user or group that you deleted
   disappears from the **Studio users** list.

**To remove a user or group from an EMR Studio using the
AWS CLI**

Insert your own values for the following
`delete-studio-session-mapping` arguments. For more information about
the `delete-studio-session-mapping` command, see the [_AWS CLI
Command Reference_](../../../cli/latest/reference/emr/delete-studio-session-mapping.md "../../../cli/latest/reference/emr/delete-studio-session-mapping.md").

```
aws emr delete-studio-session-mapping \
 --studio-id `<example-studio-id>` \
 --identity-type `<USER-or-GROUP>` \
 --identity-name `<name-of-user-or-group-to-delete>` \
```
