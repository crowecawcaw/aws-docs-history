

# Setting up
<a name="device-advisor-setting-up"></a>

Before you use Device Advisor for the first time, complete the following tasks:

## Create an IoT thing
<a name="da-create-thing-certificate"></a>

First, create an IoT thing and attach a certificate to that thing. For a tutorial on how to create things, see [Create a thing object](https://docs.aws.amazon.com/iot/latest/developerguide/create-iot-resources.html#create-aws-thing).

## Create an IAM role to use as your device role
<a name="da-iam-role"></a>

**Note**  
You can quickly create the device role with the Device Advisor console. To learn how to set up your device role with the Device Advisor console, see [ Getting started with the Device Advisor in the console](https://docs.aws.amazon.com/iot/latest/developerguide/da-console-guide.html).

1. Go to the [AWS Identity and Access Management console](https://console.aws.amazon.com/iam/home?region=us-west-2#/home) and log in to the AWS account you use for Device Advisor testing.

1. In the left navigation pane, chose **Policies**.

1. Choose **Create policy**.

1. Under **Create policy**, do the following:

   1. For **Service**, choose **IoT**.

   1. Under **Actions**, do one of the following:
      + (Recommended) Select actions based on the policy attached to the IoT thing or certificate you created in the previous section.
      + Search for the following actions in the **Filter action** box and select them:
        + `Connect`
        + `Publish`
        + `Subscribe`
        + `Receive`
        + `RetainPublish`

   1. Under **Resources**, restrict the client, topic, and topic resources. Restricting these resources is a security best practice. To restrict resources, do the following:

      1. Choose **Specify client resource ARN for the Connect action**.

      1. Choose **Add ARN**, then do either of the following:
**Note**  
The *clientId* is the MQTT client ID that your device uses to interact with Device Advisor.
         + Specify the **Region**, **accountID**, and **clientID** in the visual ARN editor.
         + Manually enter the Amazon Resource Names (ARNs) of the IoT topics you want to run your test cases with.

      1. Choose **Add**.

      1. Choose **Specify topic resource ARN for the Receive and one more action**.

      1. Choose **Add ARN**, then do either of the following:
**Note**  
The *topic name* is the MQTT topic that your device publishes messages to.
         + Specify the **Region**, **accountID**, and **Topic name** in the visual ARN editor.
         + Manually enter the ARNs of the IoT topics you want to run your test cases with.

      1. Choose **Add**.

      1. Choose **Specify topicFilter resource ARN for the Subscribe action**.

      1. Choose **Add ARN**, then do either of the following:
**Note**  
The *topic name* is the MQTT topic that your device subscribes to.
         + Specify the **Region**, **accountID**, and **Topic name** in the visual ARN editor.
         + Manually enter the ARNs of the IoT topics you want to run your test cases with.

      1. Choose **Add**.

1. Choose **Next: Tags**.

1. Choose **Next: Review**.

1. Under **Review policy**, enter a **Name** for your policy.

1. Choose **Create policy**.

1. On the left navigation pane, Choose **Roles**.

1. Choose **Create Role**.

1. Under **Select trusted entity**, choose **Custom trust policy**.

1. Enter the following trust policy into the **Custom trust policy** box. To protect against the confused deputy problem, add the global condition context keys `[aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn)` and `[aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount)` to the policy.
**Important**  
Your `aws:SourceArn` must comply with the `format: arn:aws:iotdeviceadvisor:{{region:account-id}}:*.` Make sure that `{{region}}` matches your AWS IoT Region and `{{account-id}}` matches your customer account ID. For more information, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/iot/latest/developerguide/security-best-practices.html#cross-service-confused-deputy-prevention-DA).  
****  

   ```
   {
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
                       "aws:SourceAccount": "123456789012"
               },
                   "ArnLike": {
                       "aws:SourceArn": "arn:aws:iotdeviceadvisor:*:123456789012:suitedefinition/*"
               }
           }
           }
       ]
   }
   ```

1. Choose **Next**.

1. Choose the policy you created in Step 4.

1. (Optional) Under **Set permissions boundary**, choose **Use a permissions boundary to control the maximum role permissions**, and then select the policy you created.

1. Choose **Next**.

1. Enter a **Role name** and a **Role description**.

1. Choose **Create role**.

## Create a custom-managed policy for an IAM user to use Device Advisor
<a name="da-managed-policy"></a>

1. Navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). If prompted, enter your AWS credentials to sign in.

1. In the left navigation pane, choose **Policies**.

1. Choose **Create Policy**, then choose the **JSON** tab. 

1. Add the necessary permissions to use Device Advisor. The policy document can be found in the topic [Security best practices](https://docs.aws.amazon.com/iot/latest/developerguide/security-best-practices.html#device-advisor-perms). 

1. Choose **Review Policy**.

1. Enter a **Name** and **Description**.

1. Choose **Create Policy**.

## Create an IAM user to use Device Advisor
<a name="da-iam-user"></a>

**Note**  
We recommend that you create an IAM user to use when you run Device Advisor tests. Running Device Advisor tests from an admin user can pose security risks and isn't recommended.

1. Navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/) If prompted, enter your AWS credentials to sign in.

1. In the left navigation pane, Choose **Users**.

1. Choose **Add User**.

1. Enter a **User name**.

1. Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

   To grant users programmatic access, choose one of the following options.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-setting-up.html)

1. Choose **Next: Permissions**.

1. To provide access, add permissions to your users, groups, or roles:
   + Users and groups in AWS IAM Identity Center:

     Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
   + Users managed in IAM through an identity provider:

     Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
   + IAM users:
     + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
     + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

1. Enter the name of the custom-managed policy that you created in the search box. Then, select the check box for **Policy name**.

1. Choose **Next: Tags**.

1. Choose **Next: Review**.

1. Choose **Create user**.

1. Choose **Close**.

Device Advisor requires access to your AWS resources (things, certificates, and endpoints) on your behalf. Your IAM user must have the necessary permissions. Device Advisor will also publish logs to Amazon CloudWatch if you attach the necessary permissions policy to your IAM user.

## Configure your device
<a name="da-configure-device"></a>

Device Advisor uses the server name indication (SNI) TLS extension to apply TLS configurations. Devices must use this extension when they connect and pass a server name that is identical to the Device Advisor test endpoint.

Device Advisor allows the TLS connection when a test is in the `Running` state. It denies the TLS connection before and after each test run. For this reason, we recommend that you use the device connect retry mechanism for a fully automated testing experience with Device Advisor. You can run test suites that include more than one test case, such as TLS connect, MQTT connect, and MQTT publish. If you run multiple test cases, we recommend that your device try to connect to our test endpoint every five seconds. You can then automate running multiple test cases in sequence.

**Note**  
To ready your device software for testing, we recommend that you use an SDK that can connect to AWS IoT Core. You should then update the SDK with the Device Advisor test endpoint provided for your AWS account.

Device Advisor supports two types of endpoints: Account-level and Device-level endpoints. Choose the endpoint that best fits your use case. To simultaneously run multiple test suites for different devices, use a Device-level endpoint. 

Run the following command to get the Device-level endpoint:

For MQTT customers using X.509 client certificates:

```
aws iotdeviceadvisor get-endpoint --thing-arn {{your-thing-arn}}
```

or

```
aws iotdeviceadvisor get-endpoint --certificate-arn {{your-certificate-arn}}
```

For MQTT over WebSocket customers using Signature Version 4:

```
aws iotdeviceadvisor get-endpoint --device-role-arn {{your-device-role-arn}} --authentication-method SignatureVersion4
```

To run one test suite at a time, choose an Account-level endpoint. Run the following command to get the Account-level endpoint:

```
aws iotdeviceadvisor get-endpoint
```