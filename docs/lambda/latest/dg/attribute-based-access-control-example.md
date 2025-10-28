# Secure your functions by tag

The following steps demonstrate one way to set up permissions for functions using ABAC. In this example scenario, you'll create four IAM permissions policies. Then, you'll attach these policies to a new IAM role. Finally, you'll create an IAM user and give that user permission to assume the new role.

###### Topics

- [Prerequisites](#abac-prerequisites "#abac-prerequisites")
- [Step 1: Require tags on new functions](#require-tag-on-create "#require-tag-on-create")
- [Step 2: Allow actions based on tags attached to a Lambda function and IAM principal](#restrict-actions-function-tags "#restrict-actions-function-tags")
- [Step 3: Grant list permissions](#abac-list-permissions "#abac-list-permissions")
- [Step 4: Grant IAM permissions](#abac-iam-permissions "#abac-iam-permissions")
- [Step 5: Create the IAM role](#abac-create-role "#abac-create-role")
- [Step 6: Create the IAM user](#abac-create-user "#abac-create-user")
- [Step 7: Test the permissions](#abac-test "#abac-test")
- [Step 8: Clean up your resources](#abac-clean-up "#abac-clean-up")

## Prerequisites

Make sure that you have a [Lambda execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md"). You'll use this role when you grant IAM permissions and when you create a Lambda function.

## Step 1: Require tags on new functions

When using ABAC with Lambda, it's a best practice to require that all functions have tags. This helps ensure that your ABAC permissions policies work as expected.

[Create an IAM policy](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") similar to the following example. This policy uses the [aws:RequestTag/tag-key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag"), [aws:ResourceTag/tag-key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag"), and [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys") condition keys to require that new functions and the IAM principal creating the functions both have the `project` tag. The `ForAllValues` modifier ensures that `project` is the only allowed tag. If you don't include the `ForAllValues` modifier, users can add other tags to the function as long as they also pass `project`.

###### Example – Require tags on new functions

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "lambda:CreateFunction",
 "lambda:TagResource"
 ],
 "Resource": "arn:aws:lambda:*:*:function:*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/`project`": "${aws:PrincipalTag/`project`}",
 "aws:ResourceTag/`project`": "${aws:PrincipalTag/`project`}"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "`project`"
 }
 }
 }
 }`

```

## Step 2: Allow actions based on tags attached to a Lambda function and IAM principal

Create a second IAM policy using the [aws:ResourceTag/tag-key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") condition key to require the principal's tag to match the tag that's attached to the function. The following example policy allows principals with the `project` tag to invoke functions with the `project` tag. If a function has any other tags, the action is denied.

###### Example – Require matching tags on function and IAM principal

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction",
 "lambda:GetFunction"
 ],
 "Resource": "arn:aws:lambda:*:*:function:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`project`": "${aws:PrincipalTag/`project`}"
 }
 }
 }
 ]
 }`

```

## Step 3: Grant list permissions

Create a policy that allows the principal to list Lambda functions and IAM roles. This allows the principal to see all Lambda functions and IAM roles on the console and when calling the API actions.

###### Example – Grant Lambda and IAM list permissions

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllResourcesLambdaNoTags",
 "Effect": "Allow",
 "Action": [
 "lambda:GetAccountSettings",
 "lambda:ListFunctions",
 "iam:ListRoles"
 ],
 "Resource": "*"
 }
 ]
 }`

```

## Step 4: Grant IAM permissions

Create a policy that allows **iam:PassRole**. This permission is required when you assign an execution role to a function. In the following example policy, replace the example ARN with the ARN of your Lambda execution role.

###### Note

Do not use the `ResourceTag` condition key in a policy with the `iam:PassRole` action. You cannot use the tag on an IAM role to control access to who can pass that role. For more information about permissions required to pass a role to a service, see [Granting a user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md").

###### Example – Grant permission to pass the execution role

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "`arn:aws:iam::`111122223333`:role/lambda-ex`"
 }
 ]
 }`

```

## Step 5: Create the IAM role

It's a best practice to [use roles to delegate permissions](../../../IAM/latest/UserGuide/best-practices.md#delegate-using-roles "../../../IAM/latest/UserGuide/best-practices.md#delegate-using-roles"). [Create an IAM role](../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console "../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console") called `abac-project-role`:

- On **Step 1: Select trusted entity**: Choose **AWS account** and then choose **This account**.
- On **Step 2: Add permissions**: Attach the four IAM policies that you created in the previous steps.
- On **Step 3: Name, review, and create**: Choose **Add tag**. For **Key**, enter `project`. Don't enter a **Value**.

## Step 6: Create the IAM user

[Create an IAM user](../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console "../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console") called `abac-test-user`. In the **Set permissions** section, choose **Attach existing policies directly** and then choose **Create policy**. Enter the following policy definition. Replace `111122223333` with your [AWS account ID](../../../general/latest/gr/acct-identifiers.md#FindingYourAccountIdentifiers "../../../general/latest/gr/acct-identifiers.md#FindingYourAccountIdentifiers"). This policy allows `abac-test-user` to assume `abac-project-role`.

###### Example – Allow IAM user to assume ABAC role

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`abac-project-role`"
 }
 }`

```

## Step 7: Test the permissions

1. Sign in to the AWS console as `abac-test-user`. For more information, see [Sign in as an IAM user](../../../IAM/latest/UserGuide/console.md#user-sign-in-page "../../../IAM/latest/UserGuide/console.md#user-sign-in-page").
2. Switch to the `abac-project-role` role. For more information, see [Switching to a role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md").
3. [Create a Lambda function](configuration-tags.md#using-tags-with-the-console "configuration-tags.md#using-tags-with-the-console"):
   - Under **Permissions**, choose **Change default execution role**, and then for **Execution role**, choose **Use an existing role**. Choose the same execution role that you used in [Step 4: Grant IAM permissions](#abac-iam-permissions "#abac-iam-permissions").
   - Under **Advanced settings**, choose **Enable tags** and then choose **Add new tag**. For **Key**, enter `project`. Don't enter a **Value**.

4. [Test the function](testing-functions.md "testing-functions.md").
5. Create a second Lambda function and add a different tag, such as `environment`. This operation should fail because the ABAC policy that you created in [Step 1: Require tags on new functions](#require-tag-on-create "#require-tag-on-create") only allows the principal to create functions with the `project` tag.
6. Create a third function without tags. This operation should fail because the ABAC policy that you created in [Step 1: Require tags on new functions](#require-tag-on-create "#require-tag-on-create") doesn't allow the principal to create functions without tags.

This authorization strategy allows you to control access without creating new policies for each new user. To grant access to new users, simply give them permission to assume the role that corresponds to their assigned project.

## Step 8: Clean up your resources

###### To delete the IAM role

1. Open the [Roles page](https://console.aws.amazon.com/iam/home#/roles "https://console.aws.amazon.com/iam/home#/roles") of the IAM console.
2. Select the role that you created in [step 5](#abac-create-role "#abac-create-role").
3. Choose **Delete**.
4. To confirm deletion, enter the role name in the text input field.
5. Choose **Delete**.

###### To delete the IAM user

1. Open the [Users page](https://console.aws.amazon.com/iam/home#/users "https://console.aws.amazon.com/iam/home#/users") of the IAM console.
2. Select the IAM user that you created in [step 6](#abac-create-user "#abac-create-user").
3. Choose **Delete**.
4. To confirm deletion, enter the user name in the text input field.
5. Choose **Delete user**.

###### To delete the Lambda function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function that you created.
3. Choose **Actions**, **Delete**.
4. Type `confirm` in the text input field and choose **Delete**.
