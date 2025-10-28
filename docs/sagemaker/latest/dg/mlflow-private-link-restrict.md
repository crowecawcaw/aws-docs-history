# Allow Access only from within your

VPC

Users outside your VPC can connect to SageMaker AI MLflow or over the internet even if you set
up an interface endpoint in your VPC.

To allow access to only connections made from within your VPC, create an AWS Identity and Access Management
(IAM) policy to that effect. Add that policy to every user, group, or role used to
access SageMaker AI MLflow. This feature is only supported when using IAM mode for
authentication, and is not supported in IAM Identity Center mode. The following examples demonstrate
how to create such policies.

###### Important

If you apply an IAM policy similar to one of the following examples, users
cannot access SageMaker AI MLflow through the specified SageMaker APIs through the SageMaker AI console. To
access SageMaker AI MLflow, users must use a presigned URL or call the SageMaker APIs
directly.

**Example 1: Allow connections only within the subnet of an
interface endpoint**

The following policy allows connections only to callers within the subnet where you
created the interface endpoint.

JSON

```
`{
 "Id": "mlflow-example-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MlflowAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker-mlflow:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceVpce": "vpce-111bbaaa"
 }
 }
 }
 ]
}`

```

**Example 2: Allow connections only through interface endpoints
using `aws:sourceVpce`**

The following policy allows connections only to those made through the interface
endpoints specified by the `aws:sourceVpce` condition key. For example, the
first interface endpoint could allow access through the SageMaker AI console. The second
interface endpoint could allow access through the SageMaker API.

JSON

```
`{
 "Id": "sagemaker-mlflow-example-2",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MlflowAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker-mlflow:*"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:sourceVpce": [
 `"vpce-111bbccc"`,
 `"vpce-111bbddd"`
 ]
 }
 }
 }
 ]
}`

```

**Example 3: Allow connections from IP addresses using
`aws:SourceIp`**

The following policy allows connections only from the specified range of IP addresses
using the `aws:SourceIp` condition key.

JSON

```
`{
 "Id": "sagemaker-mlflow-example-3",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MlflowAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker-mlflow:*"
 ],
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 `"192.0.2.0/24"`,
 `"203.0.113.0/24"`
 ]
 }
 }
 }
 ]
}`

```

**Example 4: Allow connections from IP addresses through an
interface endpoint using `aws:VpcSourceIp`**

If you are accessing SageMaker AI MLflow through an interface endpoint, you can use the
`aws:VpcSourceIp` condition key to allow connections only from the
specified range of IP addresses within the subnet where you created the interface
endpoint as shown in the following policy:

JSON

```
`{
 "Id": "sagemaker-mlflow-example-4",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MlflowAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker-mlflow:*"
 ],
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:VpcSourceIp": [
 `"192.0.2.0/24"`,
 `"203.0.113.0/24"`
 ]
 },
 "StringEquals": {
 "aws:SourceVpc": `"vpc-111bbaaa"`
 }
 }
 }
 ]
}`

```
