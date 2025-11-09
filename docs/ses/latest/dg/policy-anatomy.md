# Amazon SES policy anatomy

Policies adhere to a specific structure, contain elements, and must meet certain
requirements.

## Policy structure

Each authorization policy is a JSON document that is attached to an identity. Each
policy includes the following sections:

- Policy-wide information at the top of the document.
- One or more individual statements, each of which describes a set of
  permissions.

The following example policy grants AWS account ID _123456789012_ permissions specified in the
_Action_ section for the verified domain
_example.com_.

JSON

```
`{
 "Id":"ExampleAuthorizationPolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeAccount",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:123456789012:identity/example.com",
 "Principal":{
 "AWS":[
 "123456789012"
 ]
 },
 "Action":[
 "ses:GetEmailIdentity",
 "ses:UpdateEmailIdentityPolicy",
 "ses:ListRecommendations",
 "ses:CreateEmailIdentityPolicy",
 "ses:DeleteEmailIdentity"
 ]
 }
 ]
}`

```

You can find more authorization policy examples at [Identity policy
examples](identity-authorization-policy-examples.md "identity-authorization-policy-examples.md").

## Policy elements

This section describes the elements contained in identity authorization policies.
First we describe policy-wide elements, and then we describe elements that apply only to
the statement in which they are included. We follow with a discussion of how to add
conditions to your statements.

For specific information about the syntax of the elements, see [Grammar of the IAM Policy
Language](../../../IAM/latest/UserGuide/policies-grammar.md "../../../IAM/latest/UserGuide/policies-grammar.md") in the _IAM User Guide_.

### Policy-wide

information

There are two policy-wide elements: `Id` and `Version`. The
following table provides information about these elements.

| Name      | Description                                   | Required | Valid values                                                                                              |
| --------- | --------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `Id`      | Uniquely identifies the policy.               | No       | Any string                                                                                                |
| `Version` | Specifies the policy access language version. | No       | Any string. As a best practice, we recommend that you include<br>this field with a value of "2012-10-17". |

### Statements specific to

the policy

Identity authorization policies require at least one statement. Each statement can
include the elements described in the following table.

| Name        | Description                                                                                                                                                                                                                                                                                                     | Required | Valid values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Sid`       | Uniquely identifies the statement.                                                                                                                                                                                                                                                                              | No       | Any string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `Effect`    | Specifies the result that you want the policy statement to<br>return at evaluation time.                                                                                                                                                                                                                        | Yes      | "Allow" or "Deny".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `Resource`  | Specifies the identity to which the policy applies.<br>(For [sending authorization](sending-authorization-identity-owner-tasks-policy.md "sending-authorization-identity-owner-tasks-policy.md"), this is the email address or<br>domain that the identity owner is authorizing the delegate<br>sender to use.) | Yes      | The Amazon Resource Name (ARN) of the identity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `Principal` | Specifies the AWS account, user, or AWS<br>service that receives the permission in the statement.                                                                                                                                                                                                               | Yes      | A valid AWS account ID, user ARN, or AWS<br>service. AWS account IDs and user ARNs are<br>specified using `"AWS"` (for example, `"AWS":<br>["123456789012"]` or `"AWS":<br>["arn:aws:iam::123456789012:root"]`).<br>AWS service names are specified using `"Service"`<br>(for example, `"Service":<br>["cognito-idp.amazonaws.com"]`).<br>For examples of the format of user ARNs, see the<br>[AWS General Reference](../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-iam.html "../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-iam.html").                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `Action`    | Specifies the action that the statement applies to.                                                                                                                                                                                                                                                             | Yes      | "ses:BatchGetMetricData", "ses:CancelExportJob",<br>"ses:CreateDeliverabilityTestReport",<br>"ses:CreateEmailIdentityPolicy", "ses:CreateExportJob",<br>"ses:DeleteEmailIdentity", "ses:DeleteEmailIdentityPolicy",<br>"ses:GetDomainStatisticsReport",<br>"ses:GetEmailIdentity","ses:GetEmailIdentityPolicies",<br>"ses:GetExportJob", "ses:ListExportJobs",<br>"ses:ListRecommendations",<br>"ses:PutEmailIdentityConfigurationSetAttributes",<br>"ses:PutEmailIdentityDkimAttributes",<br>"ses:PutEmailIdentityDkimSigningAttributes",<br>"ses:PutEmailIdentityFeedbackAttributes",<br>"ses:PutEmailIdentityMailFromAttributes", "ses:TagResource",<br>"ses:UntagResource", "ses:UpdateEmailIdentityPolicy"<br>([Sending authorization](sending-authorization-identity-owner-tasks-policy.md "sending-authorization-identity-owner-tasks-policy.md") actions: "ses:SendEmail",<br>"ses:SendRawEmail", "ses:SendTemplatedEmail",<br>"ses:SendBulkTemplatedEmail")<br>You can specify one or more of these operations. |
| `Condition` | Specifies any restrictions or details about the<br>permission.                                                                                                                                                                                                                                                  | No       | See the information about conditions following this<br>table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Conditions

A _condition_ is any restriction about the permission in the
statement. The part of the statement that specifies the conditions can be the most
detailed of all the parts. A _key_ is the specific characteristic
that's the basis for access restriction, such as the date and time of the
request.

You use both conditions and keys together to express the restriction. For example,
if you want to restrict the delegate sender from making requests to Amazon SES on your
behalf after July 30, 2019, you use the condition called `DateLessThan`.
You use the key called `aws:CurrentTime` and set it to the value
`2019-07-30T00:00:00Z`.

SES implements only the following AWS-wide policy keys:

- `aws:CurrentTime`
- `aws:EpochTime`
- `aws:SecureTransport`
- `aws:SourceIp`
- `aws:SourceVpc`
- `aws:SourceVpce`
- `aws:UserAgent`
- `aws:VpcSourceIp`

For more information about these keys, see the [IAM User Guide](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Condition "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Condition").

## Policy requirements

Policies must meet all of the following requirements:

- Each policy has to include at least one statement.
- Each policy has to include at least one valid principal.
- Each policy has to specify one resource, and that resource has to be the ARN
  of the identity that the policy is attached to.
- Identity owners can associate up to 20 policies with each unique
  identity.
- Policies can't exceed 4 kilobytes (KB) in size.
- Policy names can't exceed 64 characters. Additionally, they can only include
  alphanumeric characters, dashes, and underscores.
