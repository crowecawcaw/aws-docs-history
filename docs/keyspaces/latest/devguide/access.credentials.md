# Create an IAM user for programmatic access

to Amazon Keyspaces in your AWS account

To obtain credentials for programmatic access to Amazon Keyspaces with the AWS CLI, the AWS SDK, or the SigV4 plugin,
you need to first create an IAM user or role.
The process of creating a IAM user and
configuring that IAM user to have programmatic access to Amazon Keyspaces is shown in the following
steps:

1. Create the user in the AWS Management Console, the AWS CLI, Tools for Windows PowerShell, or using an AWS API operation. If
   you create the user in the AWS Management Console, then the credentials are created automatically.
2. If you create the user programmatically, then you must create an access key
   (access key ID and a secret access key) for that user in an additional step.
3. Give the user permissions to access Amazon Keyspaces.
   For information about the permissions that you need in order to create an IAM user, see
   [Permissions required to access IAM resources](../../../IAM/latest/UserGuide/access_permissions-required.md "../../../IAM/latest/UserGuide/access_permissions-required.md").

Console

###### Create an IAM user with programmatic access (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** and then choose
   **Add users**.
3. Type the user name for the new user. This is the sign-in name for AWS.

###### Note

User names can be a combination of up to 64 letters, digits, and
these characters: plus (+), equal (=), comma (,), period (.), at sign (@), underscore
(\_), and hyphen (-). Names must be unique within an account. They are not distinguished
by case. For example, you cannot create two users named _TESTUSER_
and _testuser_. 4. Select **Access key - Programmatic access** to
create an access key for the new user. You can view or download the access
key when you get to the **Final** page.

Choose **Next: Permissions**. 5. On the **Set permissions** page, choose **Attach existing policies directly** to assign
permissions to the new user.

This option displays
the list of AWS managed and customer managed policies available in your account.
You can enter `keyspaces` into the search field to
display only the policies that are related to Amazon Keyspaces.

For Amazon Keyspaces, the available managed policies are
`AmazonKeyspacesFullAccess` and
`AmazonKeyspacesReadOnlyAccess`. For more information about
each policy, see [AWS managed policies for Amazon Keyspaces](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

For testing purposes and to follow the connection tutorials, select the
`AmazonKeyspacesReadOnlyAccess` policy for the new IAM user.
**Note:** As a best practice, we recommend
that you follow the principle of least privilege and create custom policies
that limit access to specific resources and only allow the required actions.
For more information about IAM policies and to view example policies for
Amazon Keyspaces, see [Amazon Keyspaces
identity-based policies](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies"). After you have created custom permission policies, attach your policies to roles
and then let users assume the appropriate roles temporarily.

Choose **Next: Tags**. 6. On the **Add tags (optional)** page you can add tags for the user, or choose **Next: Review**. 7. On the **Review** page you can see all of the choices you made up to this
point. When you're ready to proceed, choose **Create user**. 8. To view the user's access keys (access key IDs and secret access keys), choose
**Show** next to the password and access key. To
save the access keys, choose **Download .csv** and then save the file to
a safe location.

###### Important

This is your only opportunity to view or download the secret access keys, and you
need this information before they can use the SigV4 plugin.
Save the user's new access key ID and secret access key in a safe and secure place.
You will not have access to the secret keys again after this step.

CLI

###### Create an IAM user with programmatic access (AWS CLI)

1. Create a user with the following AWS CLI code.
   - [aws iam create-user](../../../cli/latest/reference/iam/create-user.md "../../../cli/latest/reference/iam/create-user.md")

2. Give the user programmatic access. This requires access keys, that can be generated in the following ways.
   - AWS CLI: [aws iam
     create-access-key](../../../cli/latest/reference/iam/create-access-key.md "../../../cli/latest/reference/iam/create-access-key.md")
   - Tools for Windows PowerShell: [New-IAMAccessKey](../../../powershell/latest/reference/items/New-IAMAccessKey.md "../../../powershell/latest/reference/items/New-IAMAccessKey.md")
   - IAM API: [CreateAccessKey](../../../IAM/latest/APIReference/API_CreateAccessKey.md "../../../IAM/latest/APIReference/API_CreateAccessKey.md")

   ###### Important

   This is your only opportunity to view or download the secret access keys, and you
   need this information before they can use the SigV4 plugin.
   Save the user's new access key ID and secret access key in a safe and secure place.
   You will not have access to the secret keys again after this step.

3. Attach the `AmazonKeyspacesReadOnlyAccess` policy to the user that defines the user's permissions. **Note:** As a best practice, we recommend that you manage user permissions by adding the
   user to a group and attaching a policy to the group instead of attaching directly to a
   user.
   - AWS CLI: [aws iam
     attach-user-policy](../../../cli/latest/reference/iam/attach-user-policy.md "../../../cli/latest/reference/iam/attach-user-policy.md")
