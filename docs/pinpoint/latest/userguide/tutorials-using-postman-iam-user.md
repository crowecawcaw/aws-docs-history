**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Create IAM policies and

roles for use with Amazon Pinpoint

When you use Postman to test the Amazon Pinpoint API, the first step is to create a user. In this
section, you create a policy that permits users to interact with all the Amazon Pinpoint resources.
Then, you create a user and attach the policy directly to the user .

Learn how to create an IAM policy. Users and roles that use this policy can interact
with all of the resources in the Amazon Pinpoint API. It also provides access to resources that
are associated with the Amazon Pinpoint Email API, as well as the Amazon Pinpoint SMS and Voice API.

###### To create the policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then choose
   **Create policy**.
3. In the **Policy editor** select **JSON**.
   Delete any JSON that is current in the **Policy editor** so
   that it is blank. Copy and paste the following JSON into the **Policy
   editor** and then in the **Policy editor** replace
   all instances of `123456789012` with your
   AWS account ID.

Your AWS account ID can be found in the upper right hand corner of the
console, or you can use the CLI, see [Finding your AWS account ID](../../../accounts/latest/reference/manage-acct-identifiers.md#FindAccountId "../../../accounts/latest/reference/manage-acct-identifiers.md#FindAccountId").

###### Note

To protect the data in your Amazon Pinpoint account, this policy only includes
permissions that allow you to read, create, and modify resources. It doesn't
include permissions that allow you to delete resources. You can modify this
policy by using the visual editor in the IAM console. For more
information, see [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the IAM User Guide. You can also
use the [CreatePolicyVersion](../../../IAM/latest/APIReference/API_CreatePolicyVersion.md "../../../IAM/latest/APIReference/API_CreatePolicyVersion.md") operation in the IAM API to update this
policy.

Also, this policy includes permissions that permit you to interact with
the `ses` and `sms-voice` services, in addition to the
`mobiletargeting` service. The `ses` and
`sms-voice` permissions allow you to interact with the
Amazon Pinpoint Email API and Amazon Pinpoint SMS and Voice API, respectively. The
`mobiletargeting` permissions allow you to interact with the
Amazon Pinpoint API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:Update*",
 "mobiletargeting:Get*",
 "mobiletargeting:Send*",
 "mobiletargeting:Put*",
 "mobiletargeting:Create*"
 ],
 "Resource": [
 "arn:aws:mobiletargeting:*:`123456789012`:apps/*",
 "arn:aws:mobiletargeting:*:`123456789012`:apps/*/campaigns/*",
 "arn:aws:mobiletargeting:*:`123456789012`:apps/*/segments/*"
 ]
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:TagResource",
 "mobiletargeting:PhoneNumberValidate",
 "mobiletargeting:ListTagsForResource",
 "mobiletargeting:CreateApp"
 ],
 "Resource": "arn:aws:mobiletargeting:*:`123456789012`:*"
 },
 {
 "Sid": "VisualEditor2",
 "Effect": "Allow",
 "Action": [
 "ses:TagResource",
 "ses:Send*",
 "ses:Create*",
 "ses:Get*",
 "ses:List*",
 "ses:Put*",
 "ses:Update*",
 "sms-voice:SendVoiceMessage",
 "sms-voice:List*",
 "sms-voice:Create*",
 "sms-voice:Get*",
 "sms-voice:Update*"
 ],
 "Resource": "*"
 }
 ]
}`

```

Choose **Next**. 4. For **Policy name**, enter a name for the policy, such as
`PostmanAccessPolicy`. Choose **Create
policy**. 5. (Optional) You can add tags to the policy by selecting **Add Tag**. 6. Choose **Next: Review**.

###### Warning

IAM users have long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed.

After you create the policy, you can create a user and attach the policy to it. When
you create the user, IAM provides a set of credentials that allow Postman to carry out
Amazon Pinpoint API operations.

###### To create the user

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the IAM console, in the navigation pane, choose
   **Users**, and then choose **Create
   users**.
3. Under **User details**, for **User name**,
   enter a name that identifies the user, such as
   `PostmanUser`. Then choose
   **Next**.
4. Under **Set permissions**, for **Permissions
   options**, choose **Attach policies directly**.
5. Under **Permissions policies**, choose the policy
   (`PostmanAccessPolicy`) that you created in [Create an
   IAM policy](#tutorials-using-postman-iam-user-create-policy "#tutorials-using-postman-iam-user-create-policy").
   Then choose **Next**.
6. On the **Review and create** page, optionally add tags that
   help you identify the user. For more information about using tags, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the
   _IAM User Guide_.
7. When you're ready to create the user, choose **Create
   user**.

###### Warning

This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Update access keys](../../../IAM/latest/UserGuide/id-credentials-access-keys-update.md "../../../IAM/latest/UserGuide/id-credentials-access-keys-update.md") in the _IAM User Guide_.

IAM provides a set of credentials that you can use to allow Postman to carry out
Amazon Pinpoint API operations.

###### To create the user

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the IAM console, in the navigation pane, choose
   **Users**. Select the user
   (`PostmanUser`) created in [Create an
   IAM user](#tutorials-using-postman-iam-user-create-user "#tutorials-using-postman-iam-user-create-user"), and
   then select the **Security credentials** tab.
3. In the **Access keys** section, choose **Create
   access key**.
4. On the **Access key best practices & alternatives** page,
   select **Application running outside AWS**.

Then choose **Next**. 5. (Optional) You can add a description tag to the policy. 6. Choose **Create access key**. 7. On the **Retrieve access keys** page, copy the credentials
that are shown in the **Access key** and **Secret
access key** columns.

###### Note

You must provide both the access key ID and the secret access key later in
this tutorial. This is the only time that you're able to view the secret
access key. We recommend that you copy it and save it in a safe
location. 8. After you've saved both keys, choose **Done**.
**Next**: [Set up Postman](tutorials-using-postman-configuration.md "tutorials-using-postman-configuration.md")
