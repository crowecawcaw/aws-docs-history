# Enable access logs for your Network Load Balancer

When you enable access logging for your load balancer, you must specify the name
of the S3 bucket where the load balancer will store the logs. The bucket must have
a bucket policy that grants ELB permission to write to the bucket.

###### Important

Access logs are created only if the load balancer has a TLS listener, and the logs
contain information about TLS requests only.

## Bucket requirements

You can use an existing bucket, or create a bucket specifically for access logs.
The bucket must meet the following requirements.

###### Requirements

- The bucket must be located in the same Region as the load balancer. The
  bucket and the load balancer can be owned by different accounts.
- The prefix that you specify must not include `AWSLogs`. We add
  the portion of the file name starting with `AWSLogs` after the
  bucket name and prefix that you specify.
- The bucket must have a bucket policy that grants permission to write the
  access logs to your bucket. Bucket policies are a collection of JSON
  statements written in the access policy language to define access
  permissions for your bucket.

###### Example bucket policy

The following is an example policy. For the `Resource` elements, replace
`amzn-s3-demo-destination-bucket` with the name of the S3 bucket for
your access logs. Be sure to omit the `Prefix/` if you are not using a
bucket prefix. For `aws:SourceAccount`, specify the ID of the AWS account with the
load balancer. For `aws:SourceArn`, replace `region` and
`012345678912` with the Region and account ID of the load balancer,
respectively.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "AWSLogDeliveryWrite",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`012345678912`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`012345678912`:*"
 ]
 }
 }
 },
 {
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/`Prefix/`AWSLogs/`account-ID`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": [
 "`012345678912`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`012345678912`:*"
 ]
 }
 }
 }
 ]
}`

```

###### Encryption

You can enable server-side encryption for your Amazon S3 access log bucket in
one of the following ways:

- Amazon S3-Managed Keys (SSE-S3)
- AWS KMS keys stored in AWS Key Management Service (SSE-KMS) †

† With Network Load Balancer access logs, you can't use AWS managed keys, you must use customer
managed keys.

For more information, see [Specifying
Amazon S3 encryption (SSE-S3)](../../../AmazonS3/latest/userguide/specifying-s3-encryption.md "../../../AmazonS3/latest/userguide/specifying-s3-encryption.md") and [Specifying server-side
encryption with AWS KMS (SSE-KMS)](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md") in the
_Amazon S3 User Guide_.

The key policy must allow the service to encrypt and decrypt the logs. The
following is an example policy.

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
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Configure access logs

Use the following procedure to configure access logs to capture request information
and deliver log files to your S3 bucket.

Console

###### To enable access logs

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the name of your load balancer to open its details page.
4. On the **Attributes** tab, choose
   **Edit**.
5. For **Monitoring**, turn on **Access
   logs**.
6. For **S3 URI**, enter the S3 URI for your log files. The URI
   that you specify depends on whether you're using a prefix.
   - URI with a prefix: s3://`amzn-s3-demo-logging-bucket`/`logging-prefix`
   - URI without a prefix: s3://`amzn-s3-demo-logging-bucket`

7. Choose **Save changes**.

AWS CLI

###### To enable access logs

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command
with the related attributes.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes \
        Key=access_logs.s3.enabled,Value=true \
        Key=access_logs.s3.bucket,Value=`amzn-s3-demo-logging-bucket` \
        Key=access_logs.s3.prefix,Value=`logging-prefix`
```

CloudFormation

###### To enable access logs

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the related attributes.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "access_logs.s3.enabled"
          Value: "true"
        - Key: "access_logs.s3.bucket"
          Value: "`amzn-s3-demo-logging-bucket`"
        - Key: "access_logs.s3.prefix"
          Value: "`logging-prefix`"
```
