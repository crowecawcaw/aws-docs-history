# Traces sent to X-Ray

**User permissions**

To enable sending traces to AWS X-Ray, you must be signed in with the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadWriteAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:GetDelivery",
 "logs:GetDeliverySource",
 "logs:PutDeliveryDestination",
 "logs:GetDeliveryDestinationPolicy",
 "logs:DeleteDeliverySource",
 "logs:PutDeliveryDestinationPolicy",
 "logs:CreateDelivery",
 "logs:GetDeliveryDestination",
 "logs:PutDeliverySource",
 "logs:DeleteDeliveryDestination",
 "logs:DeleteDeliveryDestinationPolicy",
 "logs:DeleteDelivery",
 "logs:UpdateDeliveryConfiguration"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-source:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:delivery-destination:*"
 ]
 },
 {
 "Sid": "ListAccessForLogDeliveryActions",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeDeliveryDestinations",
 "logs:DescribeDeliverySources",
 "logs:DescribeDeliveries",
 "logs:DescribeConfigurationTemplates"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowUpdatesToResourcePolicyXRay",
 "Effect": "Allow",
 "Action": [
 "xray:PutResourcePolicy",
 "xray:ListResourcePolicies",
 "xray:GetTraceSegmentDestination"
 ],
 "Resource": "*"
 }
 ]
}`

```

**X-Ray resource policy**

The destination account where the traces are being sent must have a resource
policy that includes certain permissions. When X-Ray does not currently have a
resource policy, and the user setting up the tracing has
`xray:PutResourcePolicy` and `xray:ListResourcePolicies`
permissions in the account, AWS will automatically create the following policy
when you begin sending traces to X-Ray.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "xray:PutTraceSegments",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 },
 "ForAllValues:ArnLike": {
 "logs:LogGeneratingResourceArns": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/MemoryId"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:logs:us-east-1:123456789012:delivery-source:xray-test"
 }
 }
 }
 ]
}`

```

**Enable transaction search**

To enable sending traces to X-Ray, you must enable [transaction search](../monitoring/Enable-Lambda-TransactionSearch.md "../monitoring/Enable-Lambda-TransactionSearch.md").
