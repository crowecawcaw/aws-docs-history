# How Amazon Rekognition works with

IAM

Before you use IAM to manage access to Amazon Rekognition, you should understand what
IAM features are available to use with Amazon Rekognition. To get a high-level view of how
Amazon Rekognition and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon Rekognition
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon Rekognition
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Amazon Rekognition IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon Rekognition

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon Rekognition supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Rekognition use the following prefix before the action:
`rekognition:`. For example, to grant someone permission to detect
objects, scenes, or concepts in an image with the Amazon Rekognition `DetectLabels` API
operation, you include the `rekognition:DetectLabels` action in their policy.
Policy statements must include either an `Action` or `NotAction` element.
Amazon Rekognition defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "rekognition:*action1*",
      "rekognition:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "rekognition:Describe*"`
```

To see a list of Amazon Rekognition actions, see [Actions Defined by Amazon Rekognition](../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `MyCollection` collection in your
statement, use the following ARN:

```
"Resource": "arn:aws:rekognition:us-east-1:123456789012:collection/MyCollection"
```

To specify all instances that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:rekognition:us-east-1:123456789012:collection/*"
```

Some Amazon Rekognition actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

To see a list of Amazon Rekognition resource types and their ARNs, see
[Resources Defined by Amazon Rekognition](../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon Rekognition](../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions").

### Condition keys

Amazon Rekognition
does not provide any service-specific condition keys, but it does support using some
global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

## Amazon Rekognition

resource-based policies

Amazon Rekognition supports resource-based policies for Custom Labels model copy
operations. For more information, see [Amazon Rekognition resource-based policy examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").

Other services, such as Amazon S3, also support resource-based permissions
policies. For example, you can attach a policy to an S3 bucket to manage access
permissions to that bucket.

To access images stored in an Amazon S3 bucket, you must have permission to access
object in the S3 bucket. With this permission, Amazon Rekognition can download images from
the S3 bucket. The following example policy allows the user to perform the
`s3:GetObject` action on the S3 bucket named amzn-s3-demo-bucket3.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket3/*"
 ]
 }
 ]
}`

```

To use an S3 bucket with versioning enabled, add the
`s3:GetObjectVersion` action, as shown in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket3/*"
 ]
 }
 ]
}`

```

## Amazon Rekognition IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Amazon Rekognition

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Rekognition supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Amazon Rekognition doesn't support service-linked roles.

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Amazon Rekognition supports service roles.

Using a service role may create a security issue where Amazon Rekognition is used to
call another service and act on resources it shouldn't have access to. To keep your
account secure, you should limit the scope of Amazon Rekognition's access to just the resources
you are using. This can be done by attaching a trust policy to your IAM service
role. For information on how to do this, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

### Choosing an IAM role

in Amazon Rekognition

When you configure Amazon Rekognition to analyze stored videos,
you must choose a role to allow Amazon Rekognition to access Amazon SNS on your behalf. If
you have previously created a service role or service-linked role, then
Amazon Rekognition provides you with a list of roles to choose from. For more
information, see [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").

### Example: Configuring Amazon Rekognition to

accsss images in an Amazon S3 bucket

The following is an example of how you might configure Amazon Rekognition for analyzing
images in an Amazon S3 bucket. If you want to use Amazon Rekognition to analyze images in an
Amazon S3 bucket you must do the following:

1. Ensure your IAM user/role (the client) has permission to call the relevant
   Amazon Rekognition API operations (like DetectLabels, DetectFaces etc.)

Attach an identity-based policy that grants the appropriate permissions to
invoke your desired API operations. For example, to give your role permissions
to call `DetectLabels` and `DetectFaces`, you would
attach to your role a policy that looks like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rekognition:DetectLabels",
 "rekognition:DetectFaces"
 ],
 "Resource": "*"
 }
 ]
}`

```

2. The Amazon Rekognition service needs permission to access your Amazon S3 bucket. Create an
   IAM service role, which you will need to pass to Amazon Rekognition when making API calls.
   Ensure that the service role: Trusts the Amazon Rekognition service principal, has
   `s3:GetObject` permissions for your bucket.

The trust policy might look like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "rekognition.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The identity-based policy attached to the service role might look like
this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
 }
 ]
}`

```
