# Create logging role and policy for

AWS IoT Wireless monitoring

The following shows how to create a logging role for your AWS IoT Wireless
resources. After you create the logging role and policy, you can configure logging
for your resources.

###### Note

If you want to also create a logging role for AWS IoT Core resources, see [Configure logging role and policy](../../../iot/latest/developerguide/configure-logging-role-and-policy.md "../../../iot/latest/developerguide/configure-logging-role-and-policy.md") in the _AWS IoT Core
developer guide_.

## Create a logging role for

AWS IoT Wireless

Before you can enable logging, you must create an IAM role and a policy that
gives AWS permission to monitor AWS IoT Wireless activity on your
behalf.

###### Create IAM role for logging

To create a logging role for AWS IoT Wireless, open the [Roles hub of the IAM
console](https://console.aws.amazon.com/iam/home#/roles "https://console.aws.amazon.com/iam/home#/roles") and choose **Create role**.

1. Under **Select type of trusted entity**, choose
   **Another AWS account**.
2. In **Account ID**, enter your AWS account ID, and
   then choose **Next: Permissions**.
3. In the search box, enter
   `AWSIoTWirelessLogging`.
4. Select the box next to the policy named
   **AWSIoTWirelessLogging**, and then choose
   **Next: Tags**.
5. Choose **Next: Review**.
6. In **Role name**, enter
   `IoTWirelessLogsRole`, and then choose
   **Create role**.

###### Edit trust relationship of the IAM role

In the confirmation message displayed after you ran the previous step,
choose the name of the role you created,
**IoTWirelessLogsRole**. Next, you'll edit the role to
add the following trust relationship.

1. In the **Summary** section of the role
   **IoTWirelessLogsRole**, choose the **Trust
   relationships** tab, and then choose **Edit trust
   relationship**.
2. In **Policy Document**, change the
   `Principal` property to look like this example.

```
"Principal": {
    "Service": "iotwireless.amazonaws.com"
},
```

After you change the `Principal` property, the complete
policy document should look like this example.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "iotwireless.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {}
 }
 ]
}`

```

3. To save your changes and exit, choose **Update Trust
   Policy**.

## Logging policy for AWS IoT Wireless

The following policy document provides the role policy and trust policy that
allows AWS IoT Wireless to submit log entries to CloudWatch on your behalf.

###### Note

This AWS managed policy document was automatically created for you when
you created the logging role,
**IoTWirelessLogsRole**.

###### Role policy

The following shows the role policy document.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/iotwireless*"
 }
 ]
}`

```

###### Trust policy to log only AWS IoT Wireless activity

The following shows the trust policy for logging only AWS IoT Wireless
activity.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "iotwireless.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
 }`

```

## Next steps

Now that you've create a logging role and policy, you can specify how you want
to configure logging for your AWS IoT Wireless resources using the
AWS IoT Wireless API operations or the AWS CLI. For more information, see [Configure resource logging for
AWS IoT Wireless resources](configure-resource-logging.md "configure-resource-logging.md").
