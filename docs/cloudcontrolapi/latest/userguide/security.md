# Security in AWS Cloud Control API

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that's built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security
_in_ the cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. Third-party auditors regularly test
  and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that
  apply to Cloud Control API, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company’s requirements, and applicable laws and
  regulations.
  Cloud Control API inherits its security architecture from AWS CloudFormation and operates within the AWS shared
  responsibility model. To meet your security and compliance objectives when using Cloud Control API, you
  must configure CloudFormation security controls. For guidance on applying the shared responsibility
  model with CloudFormation, see the [Security](../../../AWSCloudFormation/latest/UserGuide/security.md "../../../AWSCloudFormation/latest/UserGuide/security.md") section in the
  _AWS CloudFormation User Guide_. You can also learn how to use other AWS services that
  help you to monitor and secure your CloudFormation and Cloud Control API resources.

## IAM policy actions

for Cloud Control API

You must create and assign AWS Identity and Access Management (IAM) policies that give an IAM identity (such as
a user or role) permission to call the Cloud Control API API actions they need.

In the `Action` element of your IAM policy statement, you can specify
any API action that Cloud Control API offers. You must prefix the action name with the lowercase string
`cloudformation:`, as shown in the following example.

```
"Action": "cloudformation:CreateResource"
```

To see a list of Cloud Control API actions, see [Actions, resources, and condition keys for
AWS Cloud Control API](../../../service-authorization/latest/reference/list_awscloudcontrolapi.md "../../../service-authorization/latest/reference/list_awscloudcontrolapi.md") in the _Service Authorization Reference_.

###### Example policy to manage Cloud Control API resources

The following shows an example of a policy that grants create, read, update, and list
(but not delete) resource actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Effect":"Allow",
 "Action":[
 "cloudformation:CreateResource",
 "cloudformation:GetResource",
 "cloudformation:UpdateResource",
 "cloudformation:ListResources"
 ],
 "Resource":"*"
 }]
}`

```

## Cloud Control API

differences

Cloud Control API and CloudFormation have several important differences:

For IAM:

- Cloud Control API doesn't currently support resource-level permissions, which is the ability to
  use ARNs to specify individual resources in IAM policies.
- Cloud Control API doesn't currently support the use of service-specific condition keys in the
  IAM policies that control access to Cloud Control API resources.

For more information, see [Actions,
resources, and condition keys for AWS Cloud Control API](../../../service-authorization/latest/reference/list_awscloudcontrolapi.md "../../../service-authorization/latest/reference/list_awscloudcontrolapi.md") in the
_Service Authorization Reference_.

Additional differences:

- Cloud Control API doesn't currently support custom resources. For information about CloudFormation
  custom resources, see [Create custom
  provisioning logic with custom resources](../../../AWSCloudFormation/latest/UserGuide/template-custom-resources.md "../../../AWSCloudFormation/latest/UserGuide/template-custom-resources.md") in the
  _AWS CloudFormation User Guide_.
- When activity occurs in Cloud Control API and is recorded in AWS CloudTrail, the event source is
  listed as `cloudcontrolapi.amazonaws.com`. For information about CloudTrail logging
  for Cloud Control API operations, see [Logging
  AWS CloudFormation API calls with AWS CloudTrail](../../../AWSCloudFormation/latest/UserGuide/cfn-api-logging-cloudtrail.md "../../../AWSCloudFormation/latest/UserGuide/cfn-api-logging-cloudtrail.md") in the
  _AWS CloudFormation User Guide_.

## Account scope limitation

Cloud Control API provides a set of APIs for performing CRUDL (Create, Read, Update, Delete, List)
operations on AWS resources. When using the Cloud Control API, you can only perform CRUDL operations
on AWS resources within your own AWS account. You cannot perform these operations on AWS
resources that belong to other AWS accounts.
