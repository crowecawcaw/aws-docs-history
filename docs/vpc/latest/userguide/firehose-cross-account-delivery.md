# IAM roles for cross account delivery

When you publish to Amazon Data Firehose, you can choose a delivery stream that's in the same
account as the resource to monitor (the source account), or in a different account
(the destination account). To enable cross account delivery of flow logs to Amazon Data Firehose,
you must create an IAM role in the source account and an IAM role in the
destination account.

###### Roles

- [Source account role](#firehose-source-account-role "#firehose-source-account-role")
- [Destination account role](#firehose-destination-account-role "#firehose-destination-account-role")

## Source account role

In the source account, create a role that grants the following permissions. In
this example, the name of the role is `mySourceRole`, but you can choose
a different name for this role. The last statement allows the role in the destination
account to assume this role. The condition statements ensure that this role is passed
only to the log delivery service, and only when monitoring the specified resource.
When you create your policy, specify the VPCs, network interfaces, or subnets that
you're monitoring with the condition key `iam:AssociatedResourceARN`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`123456789012`:role/`mySourceRole`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "delivery.logs.amazonaws.com"
 },
 "StringLike": {
 "iam:AssociatedResourceARN": [
 "arn:aws:ec2:`us-east-1`:`123456789012`:vpc/`vpc-00112233344556677`"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries",
 "logs:GetLogDelivery"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/AWSLogDeliveryFirehoseCrossAccountRole"
 }
 ]
}`

```

Ensure that this role has the following trust policy, which allows the log
delivery service to assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

From the source account, use the following procedure to create the role.

###### To create the source account role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the **Create policy** page, do the following:
   1. Choose **JSON**.
   2. Replace the contents of this window with the permissions policy
      at the start of this section.
   3. Choose **Next**.
   4. Enter a name for your policy and an optional description and
      tags, and then choose **Create policy**.

5. In the navigation pane, choose **Roles**.
6. Choose **Create role**.
7. For **Trusted entity type**, choose **Custom
   trust policy**. For **Custom trust
   policy**, replace `"Principal": {},` with the
   following, which specifies the log delivery service. Choose
   **Next**.

```
"Principal": {
   "Service": "delivery.logs.amazonaws.com"
},
```

8. On the **Add permissions** page, select the checkbox
   for the policy that you created earlier in this procedure, and then
   choose **Next**.
9. Enter a name for your role and optionally provide a description.
10. Choose **Create role**.

## Destination account role

In the destination account, create a role with a name that starts with
**AWSLogDeliveryFirehoseCrossAccountRole**. This role must
grant the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "firehose:TagDeliveryStream"
 ],
 "Resource": "*"
 }
 ]
}`

```

Ensure that this role has the following trust policy, which allows the
role that you created in the source account to assume this role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`mySourceRole`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

From the destination account, use the following procedure to create the role.

###### To create the destination account role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the **Create policy** page, do the following:
   1. Choose **JSON**.
   2. Replace the contents of this window with the permissions policy
      at the start of this section.
   3. Choose **Next**.
   4. Enter a name for your policy that starts with
      **AWSLogDeliveryFirehoseCrossAccountRole**,
      and then choose **Create policy**.

5. In the navigation pane, choose **Roles**.
6. Choose **Create role**.
7. For **Trusted entity type**, choose **Custom
   trust policy**. For **Custom trust
   policy**, replace `"Principal": {},` with the
   following, which specifies the source account role. Choose
   **Next**.

```
"Principal": {
   "AWS": "arn:aws:iam::`source-account`:role/`mySourceRole`"
},
```

8. On the **Add permissions** page, select the checkbox
   for the policy that you created earlier in this procedure, and then
   choose **Next**.
9. Enter a name for your role and optionally provide a description.
10. Choose **Create role**.
