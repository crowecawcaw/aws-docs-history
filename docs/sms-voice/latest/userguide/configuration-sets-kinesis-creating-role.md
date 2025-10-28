# IAM policy for

Amazon Data Firehose

Use the following example to create a policy for sending events to a Amazon Data Firehose
stream.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "firehose:PutRecord",
 "Resource": "arn:aws:firehose:`us-east-1`:`111122223333`:deliverystream/`DeliveryStreamName`"
 }
 ]
}`

```

For more information about IAM policies, see [Policies and permissions in
IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

The following example statement uses the, optional but recommended,
`SourceAccount` and `SourceArn` conditions to check that
only the AWS End User Messaging SMS owner account has access to the configuration set. In this example,
replace `accountId` with your AWS account id,
`region` with the AWS Region name and
`ConfigSetName` with the name of the Configuration
Set.

After you create the policy, create a new IAM role, and then attach the policy
to it. When you create the role, also add the following trust policy to it:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {
 "Service": "sms-voice.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:sms-voice:`us-east-1`:`111122223333`:configuration-set/`ConfigSetName`"
 }
 }
 }
}`

```

For more information about creating IAM roles, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in
the _IAM User Guide_.
