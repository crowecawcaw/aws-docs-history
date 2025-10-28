# Policies and Permissions in

MediaPackage

This page provides an overview of resource policies in MediaPackage and describes the
basic elements of a policy. Each listed element links to more details about that element
and examples of how to use it.

For a complete list of MediaPackage actions, resources, and conditions, see [Actions, resources,
and condition keys for AWS Elemental MediaPackage](../../../service-authorization/latest/reference/list_awselementalmediapackage.md "../../../service-authorization/latest/reference/list_awselementalmediapackage.md") in the _AWS General Reference_.

In its most basic sense, a policy contains the following elements:

- **Resources** - Channels and origin endpoints are the MediaPackage resources
  for which you can allow or deny permissions. In a policy, you use the Amazon
  Resource Name (ARN) to identify the resource. For more information, see [MediaPackage resources](actions-resources-conditions-overview.md#resources-arn-format "actions-resources-conditions-overview.md#resources-arn-format").

###### Important

Wildcards are not allowed in the resource ARN in [resource-based policies](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based"). The policy must contain the explicit ARN
for each resource that it applies to.

- **Actions** - For each
  resource, MediaPackage supports a set of operations. You identify resource
  operations that you will allow (or deny) by using action keywords. For more information, see [IAM
  JSON Policy Elements: Action](../../../IAM/latest/UserGuide/reference_policies_elements_action.md "../../../IAM/latest/UserGuide/reference_policies_elements_action.md").
- **Effect** - This determines what the effect will be when the user requests
  the specific action. This can be either _allow_ or
  _deny_.

If you do not explicitly grant access to (allow) a resource, access is
implicitly denied. You can also explicitly deny access to a resource. You
might do this to make sure that a user can't access the resource, even if a
different policy grants access. For more information, see [IAM
JSON Policy Elements: Effect](../../../IAM/latest/UserGuide/reference_policies_elements_effect.md "../../../IAM/latest/UserGuide/reference_policies_elements_effect.md").

- **Principal** - The account or user who is allowed access to
  the actions and resources in the statement. In a resource policy, the
  principal is the user, account, service, or other entity that is the
  recipient of this permission. For more information, see [Principals](policy-principal.md "policy-principal.md") and
  [AWS
  JSON Policy Elements: Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md").
- **Condition** - These are the conditions
  for when a policy is in effect. You can use AWS‐wide keys and
  MediaPackage‐specific keys to specify conditions in an MediaPackage access policy. For more information, see [IAM
  JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md").
  To illustrate, consider the following `Allow` policy. With this policy in effect, Jane Doe has
  `mediapackagev2:GetObject` and `mediapackagev2:GetHeadObject`
  permissions on all objects from the specified origin endpoint under the condition that the request are made over HTTPS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowJaneDoe",
 "Effect": "Allow",
 "Principal": { "AWS": "arn:aws:iam::`111122223333`:user/JaneDoe" },
 "Action": ["mediapackagev2:GetObject","mediapackagev2:GetHeadObject"],
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:`111122223333`:channelGroup/`ChannelGroupName`/channel/`ChannelName`/originEndpoint/`OriginEndpointName`",
 "Condition": {
 "Bool": { "aws:SecureTransport": "true" }
 }
 }
 ]
}`

```

Resource policies are specific to the resources to which they are applied. You must apply
the policy explicitly to each resource that requires it.

For example, applying a policy to a particular origin endpoint that allows anonymous
`GetObject` doesn't automatically apply `GetObject` to other
endpoints even if the ARN matches. For instance, if you apply a policy to origin
endpoint `abcdef01234567890`, it only applies to that endpoint and not to
another endpoint with a similar ARN, like `021345abcdef6789`.

For more, see the topics below. For complete policy language information, see [Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") and
[IAM JSON Policy
Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

###### Topics

- [Principals](policy-principal.md "policy-principal.md")
- [Actions, resources, and condition keys in MediaPackage](actions-resources-conditions-overview.md "actions-resources-conditions-overview.md")
