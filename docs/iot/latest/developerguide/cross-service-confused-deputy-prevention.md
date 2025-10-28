# Cross-service confused deputy

prevention

The _confused deputy problem_ is a security issue where an entity that
doesn't have permission to perform an action can coerce a more-privileged entity to perform
the action. In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it shouldn't otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

To limit the permissions that AWS IoT gives another service to the resource, we recommend
using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies. If you use both global condition context keys, the `aws:SourceAccount`
value and the account in the `aws:SourceArn` value must use the same account ID
when used in the same policy statement.

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full Amazon Resource
Name (ARN) of the resource. For AWS IoT, your `aws:SourceArn` must comply with the
format:
`arn:`aws`:iot:`region`:`account-id`:`resource-type/resource-id``
 for resource specific permissions or
 `arn:`aws`:iot:`region`:`account-id`:`*``.
The resource-id can be the name or ID of the permitted resource, or a wildcard statement of
the permitted resource IDs. Make sure that the `region` matches
your AWS IoT Region and the `account-id` matches your customer
account ID.

The following example shows how to prevent the confused deputy problem by using the
`aws:SourceArn` and `aws:SourceAccount` global condition context
keys in the AWS IoT role trust policy. For more examples, see [Detailed examples of
confused deputy prevention](#cross-service-confused-deputy-prevention-examples "#cross-service-confused-deputy-prevention-examples").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"iot.amazonaws.com"
 },
 "Action":"sts:AssumeRole",
 "Condition":{
 "StringEquals":{
 "aws:SourceAccount":"`123456789012`"
 },
 "ArnLike":{
 "aws:SourceArn":"arn:`aws`:iot:`us-east-1`:`123456789012`:`*`"
 }
 }
 }
 ]
}`

```

###### Note

If you get access deny errors, it can be because the service integration with AWS
Security Token Service (STS) doesn't support the `aws:SourceArn` and
`aws:SourceAccount` context keys.

## Detailed examples of

confused deputy prevention

###### This section provides detailed examples of how to prevent the

confused deputy problem by using the aws:SourceArn and
aws:SourceAccount global condition context keys in the AWS IoT role trust
policy.

- [Fleet
  provisioning](#cross-service-confused-deputy-prevention-fleet-provision "#cross-service-confused-deputy-prevention-fleet-provision")
- [JITP](#cross-service-confused-deputy-prevention-JITP "#cross-service-confused-deputy-prevention-JITP")
- [Credential provider](#cross-service-confused-deputy-prevention-credential-provider "#cross-service-confused-deputy-prevention-credential-provider")

### Fleet

provisioning

You can configure [fleet provisioning](iot-provision.md "iot-provision.md")
using a provisioning template resource. When a provisioning template references a
provisioning role, that role's trust policy can include the
`aws:SourceArn` and `aws:SourceAccount` condition keys.
These keys limit the resources for which the configuration can invoke the
`sts:AssumeRole` request.

The role with the following trust policy can only be assumed by the IoT principal
(`iot.amazonaws.com`) for the provisioning template specified in the
`SourceArn`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"iot.amazonaws.com"
 },
 "Action":"sts:AssumeRole",
 "Condition":{
 "StringEquals":{
 "aws:SourceAccount":"`123456789012`"
 },
 "ArnLike":{
 "aws:SourceArn":"arn:`aws`:iot:`us-east-1`:`123456789012`:provisioningtemplate/`example_template`"
 }
 }
 }
 ]
}`

```

### JITP

In [just-in-time provisioning
(JITP)](jit-provisioning.md "jit-provisioning.md"), you can either use provisioning template as a resource separate
from the CA or define the template body and the role as part of the CA certificate
configuration. The value of `aws:SourceArn` in the AWS IoT role trust
policy depends on how you define the provisioning template.

If you define your provisioning template as a separate resource, the value
of `aws:SourceArn` can be
`"arn:aws:iot:`region`:`account-id`:provisioningtemplate/`example_template`"`.
You can use the same policy example in [Fleet
provisioning](#cross-service-confused-deputy-prevention-fleet-provision "#cross-service-confused-deputy-prevention-fleet-provision").

If you define your provisioning template within a CA certificate resource,
the value of `aws:SourceArn` can be
`"arn:aws:iot:`region`:`account-id`:cacert/`cert_id`"`
or
`"arn:aws:iot:`region`:`account-id`:cacert/`\*`"`.
You can use a wildcard when the resource identifier, such as the ID of a CA
certificate, is unknown at the time of creation.

The role with the following trust policy can only be assumed by the IoT
principal (`iot.amazonaws.com`) for the CA certificate specified
in the `SourceArn`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"iot.amazonaws.com"
 },
 "Action":"sts:AssumeRole",
 "Condition":{
 "StringEquals":{
 "aws:SourceAccount":"`123456789012`"
 },
 "ArnLike":{
 "aws:SourceArn":"arn:`aws`:iot:`us-east-1`:`123456789012`:cacert/`8ecde6884f3d87b1125ba31ac3fcb13d7016de7f57cc904fe1cb97c6ae98196e`"
 }
 }
 }
 ]
}`

```

When creating a CA certificate, you can reference a provisioning role in
the registration configuration. The trust policy of the provisioning role
can use `aws:SourceArn` to restrict what resources the role can
be assumed for. However, during the initial [RegisterCACertificate](../apireference/API_RegisterCACertificate.md "../apireference/API_RegisterCACertificate.md") call to register the CA certificate, you
would not have the ARN of the CA certificate to specify in the
`aws:SourceArn` condition.

To work around this, i.e., to specify the provisioning role trust policy
to the specific CA certificate that's registered with AWS IoT Core, you can do
the following:

- First, call [RegisterCACertificate](../apireference/API_RegisterCACertificate.md "../apireference/API_RegisterCACertificate.md") without providing the
  `RegistrationConfig` parameter.
- After the CA certificate is registered with AWS IoT Core, call [UpdateCACertificate](../apireference/API_UpdateCACertificate.md "../apireference/API_UpdateCACertificate.md") on it.

In the UpdateCACertificate call, provide a
`RegistrationConfig` that includes the provisioning
role trust policy with `aws:SourceArn` set to the ARN of
the newly registered CA certificate.

### Credential provider

For [AWS IoT Core
credential provider](authorizing-direct-aws.md "authorizing-direct-aws.md"), use the same AWS account you use to create the
role alias in `aws:SourceAccount`, and specify a statement that matches
the resource ARN of the rolealias resource type in `aws:SourceArn`. When
creating an IAM role for use with AWS IoT Core credential provider, you must include
in the `aws:SourceArn` condition the ARNs of any role aliases that might
need to assume the role, thereby authorizing the cross-service
`sts:AssumeRole` request.

The role with the following trust policy can only be assumed by the principal of
AWS IoT Core credential provider (`credentials.iot.amazonaws.com`) for the
roleAlias specified in the `SourceArn`. If a principal attempts to
retrieve credentials for a role alias other than what's specified in the
`aws:SourceArn` condition, the request will be denied, even if that
other role alias references the same IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "credentials.iot.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:`aws`:iot:`us-east-1`:`123456789012`:rolealias/`example_rolealias`"
 }
 }
 }
 ]
}`

```
