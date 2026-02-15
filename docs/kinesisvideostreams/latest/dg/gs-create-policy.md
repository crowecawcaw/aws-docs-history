# Create the AWS IoT policy

Follow these procedures to create an AWS IoT policy that will be attached to the
device certificate. This gives permissions to AWS IoT capabilities and allows the
assumption of the role alias using the certificate.

With AWS IoT Core policies, you can control access to the AWS IoT Core data plane. The
AWS IoT Core data plane consists of operations that you can use to do the
following:

- Connect to the AWS IoT Core message broker
- Send and receive MQTT messages
- Get or update a thing's device shadow
  For more information, see [AWS IoT Core
  policies](../../../iot/latest/developerguide/iot-policies.md "../../../iot/latest/developerguide/iot-policies.md").

###### Use AWS IoT policy editor to create an AWS IoT policy

1. Sign in to the AWS Management Console and open the AWS IoT Core console at
   [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. On the left navigation, select **Security** and then
   choose **Policies**.
3. Choose **Create policy**.
4. Enter a name for your policy.

###### Example

An example of a policy name is **KvsEdgeAccessIoTPolicy**. 5. (Optional) Add metadata to the policy by attaching tags as key-value
pairs.

For more information about using tags in IAM, see [Tagging your AWS IoT resources](../../../iot/latest/developerguide/tagging-iot.md "../../../iot/latest/developerguide/tagging-iot.md") in the _AWS IoT Core Developer Guide_. 6. Choose the **JSON** tab. 7. Paste the following JSON policy document:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect",
 "iot:Publish",
 "iot:Subscribe",
 "iot:Receive"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRoleWithWebIdentity"
 ],
 "Resource": "arn:aws:iot:us-west-2:123456789012:rolealias/`your-role-alias`"
 }
 ]
}`

```

###### Note

Replace `your-role-alias-arn` with the ARN of the role
alias that you created in [Create the AWS IoT role alias](gs-create-role-alias.md "gs-create-role-alias.md"). 8. Choose **Create** to save your work.
