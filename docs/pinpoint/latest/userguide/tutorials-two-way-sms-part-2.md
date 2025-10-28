**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Create IAM policies and

roles for use with SMS in Amazon Pinpoint

The next step in implementing the SMS registration solution in Amazon Pinpoint is to configure a policy and a
role in AWS Identity and Access Management (IAM). For this solution, you need to create a policy that provides
access to certain resources that are related to Amazon Pinpoint. You then create a role and attach the
policy to it. Later in this tutorial, you create an AWS Lambda function that uses this role
to call certain operations in the Amazon Pinpoint API.

This section shows you how to create an IAM policy. Users and roles that use this
policy are able to do the following:

- Use the Phone Number Validate feature
- View, create, and update Amazon Pinpoint endpoints
- Send messages to Amazon Pinpoint endpoints
  In this tutorial, you want to give Lambda the ability to perform these tasks. However,
  for added security, this policy uses the principal of granting _least
  privilege_. In other words, it grants only the permissions that are
  required to complete this solution, and no more. This policy is restricted in the
  following ways:

- You can only use it to call the Phone Number Validate API in a specific
  Region.
- You can only use it to view, create, or update endpoints that are associated
  with a specific Amazon Pinpoint project.
- You can only use it to send messages to endpoints that are associated with a
  specific Amazon Pinpoint project.

###### To create the policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then choose
   **Create policy**.
3. On the **JSON** tab, paste the following code.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup"
 ],
 "Resource": "arn:aws:logs:*:*:*"
 },
 {
 "Effect": "Allow",
 "Action": "mobiletargeting:SendMessages",
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:GetEndpoint",
 "mobiletargeting:UpdateEndpoint",
 "mobiletargeting:PutEvents"
 ],
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/endpoints/*"
 },
 {
 "Effect": "Allow",
 "Action": "mobiletargeting:PhoneNumberValidate",
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:phone/number/validate"
 }
 ]
}`

```

In the preceding example, do the following:

    * Replace `region` with the AWS Region that
     you use Amazon Pinpoint in, such as `us-east-1` or
     `eu-central-1`.


    ###### Tip

    For a complete list of AWS Regions where Amazon Pinpoint is available, see
     [AWS regions
     and endpoints](../../../general/latest/gr/rande.md#pinpoint_region "../../../general/latest/gr/rande.md#pinpoint_region") in the
     *AWS General Reference*.
    * Replace `accountId` with the unique ID for
     your AWS account.
    * Replace `projectId` with the unique ID of the
     project that you created in [Create an Amazon Pinpoint
     project](tutorials-two-way-sms-part-1.md#tutorials-two-way-sms-part-1-create-project "tutorials-two-way-sms-part-1.md#tutorials-two-way-sms-part-1-create-project") of this tutorial.

###### Note

The `logs` actions enable Lambda to log its output in
CloudWatch Logs. 4. Choose **Next**. 5. For **Policy name**, enter a name for the policy, such as
`RegistrationFormPolicy`. Choose **Create
policy**.

###### To create the role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the IAM console, in the navigation pane, choose
   **Roles**, and then choose **Create
   role**.
3. Under **Trusted entity type**, choose **AWS
   service**, and then for **Service or user case**
   choose **Lambda** from the drop down list.
4. Choose **Next**.
5. Under **Permissions policies**, choose or search for the
   policy that you created in the previous section, and then choose
   **Next**.
6. Under **Role details**, for **Role name**, enter a name
   for the role, such as `SMSRegistrationForm`. Choose
   **Create role**.
   **Next**: [Create
   Lambda functions](tutorials-two-way-sms-part-3.md "tutorials-two-way-sms-part-3.md")
