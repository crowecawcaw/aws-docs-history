# Using IAM policy conditions for

fine-grained access control

In Route 53, you can specify conditions when granting permissions using an IAM policy
(see [Access control](auth-and-access-control.md#access-control "auth-and-access-control.md#access-control")). For example, you
can:

- Grant permissions to allow access to a single resource record set.
- Grant permissions to allow users access to all resource record sets of a
  specific DNS record type in a hosted zone, for example A and AAAA
  records.
- Grant permissions to allow users access to a resource record set where its
  name contains a specific string.
- Grant permissions to allow users to perform only a subset of the `CREATE
| UPSERT | DELETE` actions on the Route 53 console, or when using the
  [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md") API.
- Grant permissions to allow users to associate or dissociate private hosted zones from a particular VPC.
- Grant permissions to allow users to list hosted zones associated to a particular VPC.
- Grant permissions to allow users access to create a new private hosted zone and associate it to a particular VPC.
- Grant permissions to allow users to create or delete a VPC association authorization.
  You can also create permissions that combine any of the granular permissions.

## Normalizing the Route 53 condition key

values

The values you enter for the policy conditions must be formatted, or normalized,
as follows:

**For
`route53:ChangeResourceRecordSetsNormalizedRecordNames`:**

- All letters must be lowercase.
- The DNS name must be without the trailing dot.
- Characters other than a–z, 0–9, - (hyphen), \_ (underscore),
  and . (period, as a delimiter between labels) must use escape codes in the
  format \three-digit octal code. For example, `\052` is the octal
  code for character \*.

**For `route53:ChangeResourceRecordSetsActions`,
the value can be any of the following and must be uppercase:**

- CREATE
- UPSERT
- DELETE

**For
`route53:ChangeResourceRecordSetsRecordTypes`**:

- The value must be in uppercase, and can be any of the Route 53 supported DNS
  record types. For more information, see [Supported DNS record types](ResourceRecordTypes.md "ResourceRecordTypes.md").

**For
`route53:VPCs`:**

- The value must be in the format of `VPCId=<vpc-id>,VPCRegion=<region>`.
- The value of `<vpc-id>` and `<region>`must be in lowercase, such as `VPCId=vpc-123abc` and `VPCRegion=us-east-1`.
- The context keys and values are case sensitive.

###### Important

For your permissions to allow or restrict actions as you intend, you must
follow these conventions. Only `VPCId` and `VPCRegion`
elements are accepted by this condition key,
any other AWS resources, such as AWS account, are not supported.

You can use the
[Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md")
or [Policy Simulator](../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md "../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md")
in the _IAM User Guide_ to validate that your policy grants or restricts the
permissions as expected. You can also validate the permissions by applying an IAM
policy to a test user or role to carry out Route 53 operations.

## Specifying conditions: using condition

keys

AWS provides a set of predefined condition keys (AWS-wide condition keys) for
all AWS services that support IAM for access control. For example, you can use
the `aws:SourceIp` condition key to check the requester's IP address
before allowing an action to be performed. For more information and a list of the
AWS-wide keys, see [Available
Keys for Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

###### Note

Route 53 doesn't support tag-based condition keys.

The following table shows the Route 53 service-specific condition keys that apply to
Route 53.

| Route 53 Condition Key                                  | API operations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Value type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `route53:ChangeResourceRecordSetsNormalizedRecordNames` | [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Multi-valued | Represents a list of DNS record names in the request of<br>ChangeResourceRecordSets. To get the expected behavior, DNS<br>names in the IAM policy must be normalized as follows:<br>• All letters must be lowercase.<br>• The DNS name must be without the trailing dot.<br>• Characters other than a to z, 0 to 9, - (hyphen), \_<br>(underscore), and . (period, as a delimiter between<br>labels) must use escape codes in the format \three-digit<br>octal code. |
| `route53:ChangeResourceRecordSetsRecordTypes`           | [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Multi-valued | Represents a list of DNS record types in the request of<br>`ChangeResourceRecordSets`.<br>`ChangeResourceRecordSetsRecordTypes` can be any of<br>the Route 53 supported DNS record types. For more information, see<br>[Supported DNS record types](ResourceRecordTypes.md "ResourceRecordTypes.md"). All must be entered<br>in uppercase in the policy.                                                                                                             |
| `route53:ChangeResourceRecordSetsActions`               | [ChangeResourceRecordSets](../APIReference/API_ChangeResourceRecordSets.md "../APIReference/API_ChangeResourceRecordSets.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Multi-valued | Represents a list of actions in the request of<br>`ChangeResourceRecordSets`.<br>`ChangeResourceRecordSetsActions` can be any of the<br>following values (must be uppercase):<br>• CREATE<br>• UPSERT<br>• DELETE                                                                                                                                                                                                                                                    |
| `route53:VPCs`                                          | [AssociateVPCWithHostedZone](../APIReference/API_AssociateVPCWithHostedZone.md "../APIReference/API_AssociateVPCWithHostedZone.md")<br>[DisassociateVPCFromHostedZone](../APIReference/API_DisassociateVPCFromHostedZone.md "../APIReference/API_DisassociateVPCFromHostedZone.md")<br>[ListHostedZonesByVPC](../APIReference/API_ListHostedZonesByVPC.md "../APIReference/API_ListHostedZonesByVPC.md")<br>[CreateHostedZone](../APIReference/API_CreateHostedZone.md "../APIReference/API_CreateHostedZone.md")<br>[CreateVPCAssociationAuthorization](../APIReference/API_CreateVPCAssociationAuthorization.md "../APIReference/API_CreateVPCAssociationAuthorization.md")<br>[DeleteVPCAssociationAuthorization](../APIReference/API_DeleteVPCAssociationAuthorization.md "../APIReference/API_DeleteVPCAssociationAuthorization.md") | Multi-valued | Represents a list of VPCs in the request of `AssociateVPCWithHostedZone`, `DisassociateVPCFromHostedZone`,<br>`ListHostedZonesByVPC`, `CreateHostedZone`,<br>`CreateVPCAssociationAuthorization`, and `DeleteVPCAssociationAuthorization`, in the format of<br>"VPCId=<vpc-id>,VPCRegion=<region>                                                                                                                                                                    |

## Example policies: Using

conditions for fine-grained access

Each of the examples in this section sets the Effect clause to Allow and specifies
only the actions, resources, and parameters that are allowed. Access is permitted
only to what is explicitly listed in the IAM policy.

In some cases, it is possible to rewrite these policies so that they are
deny-based (that is, setting the Effect clause to Deny and inverting all of the
logic in the policy). However, we recommend that you avoid using deny-based policies
because they are difficult to write correctly, compared to allow-based policies.
This is especially true for Route 53 due to text normalization that is required.

###### Grant permissions that limit access to DNS records with specific

names

The following permissions policy grants permissions that allow
`ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for
example.com and marketing.example.com. It uses the
`route53:ChangeResourceRecordSetsNormalizedRecordNames` condition
key to limit user actions only on the records that match the specified names.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "route53:ChangeResourceRecordSets",
 "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
 "Condition": {
 "ForAllValues:StringEquals":{
 "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["example.com", "marketing.example.com"]
 }
 }
 }
 ]
}`

```

`ForAllValues:StringEquals` is an IAM condition operator that applies
to multi-valued keys. The condition in the policy above will allow the operation
only when all changes in `ChangeResourceRecordSets` have the DNS name of
example.com. For more information, see [IAM condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") and [IAM
condition with multiple keys or values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md") in the IAM User Guide.

To implement the permission that matches names with certain suffixes, you can use
the IAM wildcard (\*) in the policy with condition operator `StringLike`
or `StringNotLike`. The following policy will allow the operation when
all changes in the `ChangeResourceRecordSets` operation have DNS names
that end with “-beta.example.com”.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "route53:ChangeResourceRecordSets",
 "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
 "Condition": {
 "ForAllValues:StringLike":{
 "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["*-beta.example.com"]
 }
 }
 }
 ]
}`

```

###### Note

The IAM wildcard isn't the same as the domain name wildcard. See the
following example for how to use the wildcard with a domain name.

###### Grant permissions that limit access to DNS records that match a domain name

containing a wildcard

The following permissions policy grants permissions that allow
`ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for
example.com. It uses the
`route53:ChangeResourceRecordSetsNormalizedRecordNames` condition
key to limit user actions only to the records that match \*.example.com.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "route53:ChangeResourceRecordSets",
 "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
 "Condition": {
 "ForAllValues:StringEquals":{
 "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["\\052.example.com"]
 }
 }
 }
 ]
}`

```

`\052` is the octal code for character \* in the DNS name, and
`\` in `\052` is escaped to be `\\` to follow
JSON syntax.

###### Grant permissions that limit access to specific DNS records

The following permissions policy grants permissions that allow
`ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for
example.com. It uses the combination of three condition keys to limit user
actions to allow only creating or editing DNS records with certain DNS name and
type.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "route53:ChangeResourceRecordSets",
 "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
 "Condition": {
 "ForAllValues:StringEquals":{
 "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["example.com"],
 "route53:ChangeResourceRecordSetsRecordTypes": ["MX"],
 "route53:ChangeResourceRecordSetsActions": ["CREATE", "UPSERT"]
 }
 }
 }
 ]
}`

```

###### Grant permissions that limit access to creating and editing only the

specified types of DNS records

The following permissions policy grants permissions that allow
`ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for
example.com. It uses the
`route53:ChangeResourceRecordSetsRecordTypes` condition key to
limit user actions only on the records which match the specified types (A and
AAAA).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "route53:ChangeResourceRecordSets",
 "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
 "Condition": {
 "ForAllValues:StringEquals":{
 "route53:ChangeResourceRecordSetsRecordTypes": ["A", "AAAA"]
 }
 }
 }
 ]
}`

```

###### Grant permissions that specifies the VPC that the IAM principal can operate in

The following permissions policy grants permissions that allow
`AssociateVPCWithHostedZone` ,
`DisassociateVPCFromHostedZone`,
`ListHostedZonesByVPC`, `CreateHostedZone`,
`CreateVPCAssociationAuthorization`, and
`DeleteVPCAssociationAuthorization` actions on the VPC
specified by the vpc-id.

###### Important

The condition value must be in the format of `VPCId=<vpc-id>,VPCRegion=<region>`. If you specify a VPC ARN in the condition value, the condition key will not take effect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "route53:*"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "route53:VPCs": [
 "VPCId=<vpc-id>,VPCRegion=<region>"
 ]
 }
 }
 },
 {
 "Sid": "Statement2",
 "Effect": "Allow",
 "Action": "ec2:DescribeVpcs",
 "Resource": "*"
 }
 ]
}`

```
