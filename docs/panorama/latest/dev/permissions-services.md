End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# AWS Panorama service roles and cross-service resources

AWS Panorama uses other AWS services to manage the AWS Panorama Appliance, store data, and import application resources. A service
role gives a service permission to manage resources or interact with other services. When you sign in to the AWS Panorama
console for the first time, you create the following service roles:

######

- **AWSServiceRoleForAWSPanorama** – Allows AWS Panorama to manage resources in AWS IoT, AWS Secrets Manager, and AWS Panorama.

Managed policy: [AWSPanoramaServiceLinkedRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSPanoramaServiceLinkedRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSPanoramaServiceLinkedRolePolicy")

- **AWSPanoramaApplianceServiceRole** – Allows an AWS Panorama Appliance to upload logs to CloudWatch, and to get objects from
  Amazon S3 access points created by AWS Panorama.

Managed policy: [AWSPanoramaApplianceServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSPanoramaApplianceServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSPanoramaApplianceServiceRolePolicy")
To view the permissions attached to each role, use the [IAM
console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam"). Wherever possible, the role's permissions are restricted to resources that match a naming pattern
that AWS Panorama uses. For example, `AWSServiceRoleForAWSPanorama` grants only permission for the service to
access AWS IoT resources that have `panorama` in their name.

###### Sections

- [Securing the appliance role](#permissions-services-appliance "#permissions-services-appliance")
- [Use of other services](#permissions-services-otherservices "#permissions-services-otherservices")

## Securing the appliance role

The AWS Panorama Appliance uses the `AWSPanoramaApplianceServiceRole` role to access resources in your account. The
appliance has permission to upload logs to CloudWatch Logs, read camera stream credentials from AWS Secrets Manager, and to access
application artifacts in Amazon Simple Storage Service (Amazon S3) access points that AWS Panorama creates.

###### Note

Applications don't use the appliance's permissions. To give your application permission to use AWS
services, create an [application role](permissions-application.md "permissions-application.md").

AWS Panorama uses the same service role with all appliances in your account, and does not use roles across accounts.
For an added layer of security, you can modify the appliance role's trust policy to enforce this explicitly, which
is a best practice when you use roles to grant a service permission to access resources in your account.

###### To update the appliance role trust policy

1. Open the appliance role in the IAM console: [AWSPanoramaApplianceServiceRole](https://console.aws.amazon.com/iam/home#/roles/AWSPanoramaApplianceServiceRole?section=trust "https://console.aws.amazon.com/iam/home#/roles/AWSPanoramaApplianceServiceRole?section=trust")
2. Choose **Edit trust relationship**.
3. Update the policy contents and then choose **Update trust policy**.

The following trust policy includes a condition that ensures that when AWS Panorama assumes the appliance role, it is
doing so for an appliance in your account. The `aws:SourceAccount` condition compares the account ID
specified by AWS Panorama to the one that you include in the policy.

###### Example trust policy – Specific account

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "panorama.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 `"StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }`
 }
 }
 ]
}`

```

If you want to restrict AWS Panorama further, and allow it to only assume the role with a specific device, you can
specify the device by ARN. The `aws:SourceArn` condition compares the ARN of the appliance specified by
AWS Panorama to the one that you include in the policy.

###### Example trust policy – Single appliance

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "panorama.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:panorama:`us-east-1`:`123456789012`:device/device-`lk7exmplpvcr3heqwjmesw76ky`"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

If you reset and reprovision the appliance, you must remove the source ARN condition temporarily and then add
it again with the new device ID.

For more information on these conditions, and security best practices when services use roles to access
resources in your account, see [The confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md")
in the IAM User Guide.

## Use of other services

AWS Panorama creates or accesses resources in the following services:

######

- [AWS IoT](../../../IAM/latest/UserGuide/list_awsiot.md "../../../IAM/latest/UserGuide/list_awsiot.md") – Things, policies, certificates, and
  jobs for the AWS Panorama Appliance
- [Amazon S3](../../../IAM/latest/UserGuide/list_amazons3.md "../../../IAM/latest/UserGuide/list_amazons3.md") – Access points for staging application
  models, code, and configurations.
- [Secrets Manager](../../../IAM/latest/UserGuide/list_awssecretsmanager.md "../../../IAM/latest/UserGuide/list_awssecretsmanager.md") – Short-term credentials for
  the AWS Panorama Appliance.

For information about Amazon Resource Name (ARN) format or permission scopes for each service, see the topics
in the _IAM User Guide_ that are linked to in this list.
