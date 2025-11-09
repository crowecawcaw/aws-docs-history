# Setting up

Before you use Device Advisor for the first time, complete the following tasks:

## Create an IoT thing

First, create an IoT thing and attach a certificate to that thing. For a tutorial
on how to create things, see [Create a thing object](create-iot-resources.md#create-aws-thing "create-iot-resources.md#create-aws-thing").

## Create an IAM role to use as your device

role

###### Note

You can quickly create the device role with the Device Advisor console. To learn how
to set up your device role with the Device Advisor console, see [Getting started with the Device Advisor in the console](da-console-guide.md "da-console-guide.md").

1.  Go to the [AWS Identity and Access Management console](https://console.aws.amazon.com/iam/home?region=us-west-2#/home "https://console.aws.amazon.com/iam/home?region=us-west-2#/home") and log in to the AWS account you use for
    Device Advisor testing.
2.  In the left navigation pane, chose **Policies**.
3.  Choose **Create policy**.
4.  Under **Create policy**, do the following:
    1.  For **Service**, choose
        **IoT**.
    2.  Under **Actions**, do one of the
        following:
        - (Recommended) Select actions based on the policy attached
          to the IoT thing or certificate you created in the previous
          section.
        - Search for the following actions in the **Filter
          action** box and select them:
          - `Connect`
          - `Publish`
          - `Subscribe`
          - `Receive`
          - `RetainPublish`

    3.  Under **Resources**, restrict the client, topic,
        and topic resources. Restricting these resources is a security best
        practice. To restrict resources, do the following:
        1. Choose **Specify client resource ARN for the
           Connect action**.
        2. Choose **Add ARN**, then do either of the
           following:

        ###### Note

        The _clientId_ is the MQTT client
        ID that your device uses to interact with
        Device Advisor.

            * Specify the **Region**,
             **accountID**, and
             **clientID** in the visual ARN
             editor.
            * Manually enter the Amazon Resource Names (ARNs) of
             the IoT topics you want to run your test cases
             with.

        3. Choose **Add**.
        4. Choose **Specify topic resource ARN for the
           Receive and one more action**.
        5. Choose **Add ARN**, then do either of the
           following:

        ###### Note

        The _topic name_ is the MQTT topic
        that your device publishes messages to.

            * Specify the **Region**,
             **accountID**, and
             **Topic name** in the visual ARN
             editor.
            * Manually enter the ARNs of the IoT topics you want
             to run your test cases with.

        6. Choose **Add**.
        7. Choose **Specify topicFilter resource ARN for the
           Subscribe action**.
        8. Choose **Add ARN**, then do either of the
           following:

        ###### Note

        The _topic name_ is the MQTT topic
        that your device subscribes to.

            * Specify the **Region**,
             **accountID**, and
             **Topic name** in the visual ARN
             editor.
            * Manually enter the ARNs of the IoT topics you want
             to run your test cases with.

        9. Choose **Add**.

5.  Choose **Next: Tags**.
6.  Choose **Next: Review**.
7.  Under **Review policy**, enter a
    **Name** for your policy.
8.  Choose **Create policy**.
9.  On the left navigation pane, Choose **Roles**.
10. Choose **Create Role**.
11. Under **Select trusted entity**, choose **Custom
    trust policy**.
12. Enter the following trust policy into the **Custom
    trust policy** box. To protect against the confused deputy problem,
    add the global condition context keys
    `aws:SourceArn`
    and `aws:SourceAccount`
    to the policy.

###### Important

Your `aws:SourceArn` must comply with the
`format: arn:aws:iotdeviceadvisor:`region:account-id`:*.`
Make sure that `region` matches your AWS IoT
Region and `account-id` matches your customer account ID.
For more information, see [Cross-service confused deputy prevention](security-best-practices.md#cross-service-confused-deputy-prevention-DA "security-best-practices.md#cross-service-confused-deputy-prevention-DA").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAwsIoTCoreDeviceAdvisor",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotdeviceadvisor.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:iotdeviceadvisor:*:`111122223333`:suitedefinition/*"
 }
 }
 }
 ]
}`

```

13. Choose **Next**.
14. Choose the policy you created in Step 4.
15. (Optional) Under **Set permissions boundary**, choose
    **Use a permissions boundary to control the maximum role
    permissions**, and then select the policy you created.
16. Choose **Next**.
17. Enter a **Role name** and a **Role
    description**.
18. Choose **Create role**.

## Create a custom-managed policy for an IAM user

to use Device Advisor

1. Navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). If prompted, enter your AWS
   credentials to sign in.
2. In the left navigation pane, choose **Policies**.
3. Choose **Create Policy**, then choose the
   **JSON** tab.
4. Add the necessary permissions to use Device Advisor. The policy document can be
   found in the topic [Security best practices](security-best-practices.md#device-advisor-perms "security-best-practices.md#device-advisor-perms").
5. Choose **Review Policy**.
6. Enter a **Name** and
   **Description**.
7. Choose **Create Policy**.

## Create an IAM user to use Device Advisor

###### Note

We recommend that you create an IAM user to use when you run Device Advisor tests.
Running Device Advisor tests from an admin user can pose security risks and isn't
recommended.

1. Navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") If prompted, enter your AWS
   credentials to sign in.
2. In the left navigation pane, Choose **Users**.
3. Choose **Add User**.
4. Enter a **User name**.
5. Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

6. Choose **Next: Permissions**.
7. To provide access, add permissions to your users, groups, or roles:
   - Users and groups in AWS IAM Identity Center:

   Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.
   - Users managed in IAM through an identity provider:

   Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
   in the _IAM User Guide_.
   - IAM users:
     - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
     - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

8. Enter the name of the custom-managed policy that you created in the search
   box. Then, select the check box for **Policy name**.
9. Choose **Next: Tags**.
10. Choose **Next: Review**.
11. Choose **Create user**.
12. Choose **Close**.

Device Advisor requires access to your AWS resources (things, certificates, and
endpoints) on your behalf. Your IAM user must have the necessary permissions.
Device Advisor will also publish logs to Amazon CloudWatch if you attach the necessary permissions
policy to your IAM user.

## Configure your device

Device Advisor uses the server name indication (SNI) TLS extension to apply TLS
configurations. Devices must use this extension when they connect and pass a server
name that is identical to the Device Advisor test endpoint.

Device Advisor allows the TLS connection when a test is in the `Running`
state. It denies the TLS connection before and after each test run. For this reason,
we recommend that you use the device connect retry mechanism for a fully automated
testing experience with Device Advisor. You can run test suites that include more than one
test case, such as TLS connect, MQTT connect, and MQTT publish. If you run multiple
test cases, we recommend that your device try to connect to our test endpoint every
five seconds. You can then automate running multiple test cases in sequence.

###### Note

To ready your device software for testing, we recommend that you use an SDK
that can connect to AWS IoT Core. You should then update the SDK with the Device Advisor
test endpoint provided for your AWS account.

Device Advisor supports two types of endpoints: Account-level and Device-level endpoints.
Choose the endpoint that best fits your use case. To simultaneously run multiple
test suites for different devices, use a Device-level endpoint.

Run the following command to get the Device-level endpoint:

For MQTT customers using X.509 client certificates:

```
aws iotdeviceadvisor get-endpoint --thing-arn `your-thing-arn`
```

or

```
aws iotdeviceadvisor get-endpoint --certificate-arn `your-certificate-arn`
```

For MQTT over WebSocket customers using Signature Version 4:

```
aws iotdeviceadvisor get-endpoint --device-role-arn `your-device-role-arn` --authentication-method **SignatureVersion4**
```

To run one test suite at a time, choose an Account-level endpoint. Run the
following command to get the Account-level endpoint:

```
aws iotdeviceadvisor get-endpoint
```
