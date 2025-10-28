# Add permissions to the token exchange service

(TES) role

Grant the token exchange service (TES) role to the device that assumes permissions
to look at the secrets. This is necessary for the AWS Secrets Manager AWS IoT Greengrass
component to work correctly.

###### Add permissions to the TES role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** in the left navigation and search for
   the TES role that you created earlier in the process.
3. In the **Add permissions** dropdown, select
   **Attach policies**.
4. Choose **Create policy**.
5. Scroll down and select **Edit**.
6. In the policy editor, choose **JSON** and edit the
   policy.

Replace the policy with the following:

###### Note

Replace `arn:aws:kinesisvideo:*:*:stream/streamName1/*` and
`arn:aws:kinesisvideo:*:*:stream/streamName2/*` with the
ARNs for the streams that you created in a previous step.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:ListStreams"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:DescribeStream",
 "kinesisvideo:PutMedia",
 "kinesisvideo:TagStream",
 "kinesisvideo:GetDataEndpoint"
 ],
 "Resource": [
 "`arn:aws:kinesisvideo:*:*:stream/streamName1/*`",
 "`arn:aws:kinesisvideo:*:*:stream/streamName2/*`"
 ]
 }
 ]
}`

```

7. On the **Add tags** page, choose **Next:
   Review**.
8. Name your policy, then choose **Create policy**.

An example of a policy name is **KvsEdgeAccessPolicy**. 9. Close the tab and return to the tab where you were attaching a policy to
the TES role.

Choose the refresh button, then search for the newly created
policy.

Select the check box and choose **Attach
policies**.

On the next screen, you see a note that says **Policy was
successfully attached to role.** 10. Create and attach another policy, this time for your secrets.

Replace the policy with the following:

###### Note

Replace `arn:aws:secretsmanager:*:*:secret:*` with the ARNs
containing the MediaURI secrets that you created in [Create the Amazon Kinesis Video Streams and
AWS Secrets Manager resources for your IP camera RTSP URLs](gs-create-resources.md "gs-create-resources.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": [
 "`arn:aws:secretsmanager:*:*:secret:*`",
 "`arn:aws:secretsmanager:*:*:secret:*`"
 ]
 }
 ]
}`

```

11. Create and attach another policy, this time for Amazon CloudWatch
    metrics. Replace the policy with the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
