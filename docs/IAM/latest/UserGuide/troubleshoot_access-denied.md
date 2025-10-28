# Troubleshoot access denied error

messages

The following information can help you identify, diagnose, and resolve access denied
errors with AWS Identity and Access Management. Access denied errors appear when AWS explicitly or implicitly
denies an authorization request.

- An _explicit denial_ occurs when a policy contains a
  `Deny` statement for the specific AWS action.
- An _implicit denial_ occurs when there is no applicable
  `Deny` statement and also no applicable `Allow` statement.
  Because an IAM policy denies an IAM principal by default, the policy must
  explicitly allow the principal to perform an action. Otherwise, the policy
  implicitly denies access. For more information, see [The
  difference between explicit and implicit denies](reference_policies_evaluation-logic_AccessPolicyLanguage_Interplay.md "reference_policies_evaluation-logic_AccessPolicyLanguage_Interplay.md").
  When you make a request to a service or resource, multiple policies may apply to the
  request. Review all applicable policies in addition to the policy specified in the error
  message.

- If multiple policies of the same policy type deny a request, the access denied
  error message doesn't specify the number of policies evaluated.
- If multiple policy types deny an authorization request, AWS includes only one of
  those policy types in the error message.

###### Important

**Having trouble signing in to AWS?** Make sure that
you're on the correct [AWS sign-in
page](../../../signin/latest/userguide/console-sign-in-tutorials.md "../../../signin/latest/userguide/console-sign-in-tutorials.md") for your type of user. If you are the AWS account root user (account owner), you
can sign in to AWS using the credentials that you set up when you created the
AWS account. If you are an IAM user, your account administrator can give you AWS
sign-in credentials. If you need to request support, do not use the feedback link on
this page. The form is received by the AWS Documentation team, not Support. Instead, on
the [Contact Us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") page choose
**Still unable to log into your AWS account** and then choose one
of the available support options.

## I get "access denied" when

I make a request to an AWS service

- Check if the error message includes the type of policy responsible for denying
  access. For example, if the error mentions that access is denied due to a
  Service Control Policy (SCP), then you can focus on troubleshooting SCP issues.
  Once you identify the policy type, you can check for deny statements or missing
  allow actions in those policy types. If the error message doesn't mention the
  policy type responsible for denying access, use the rest of the guidelines in
  this section to troubleshoot further.
- Verify that you have the identity-based policy permission to call the action
  and resource that you have requested. If any conditions are set, you must also
  meet those conditions when you send the request. For information about viewing
  or modifying policies for an IAM user, group, or role, see [Manage IAM policies](access_policies_manage.md "access_policies_manage.md").
- If the AWS Management Console returns a message stating that you're not authorized to
  perform an action, then you must contact your administrator for assistance. Your
  administrator provided you with your sign-in credentials or sign-in link.

The following example error occurs when the `mateojackson`
IAM user attempts to use the console to view details about a fictional
`my-example-widget` resource but
does not have the fictional
`widgets:`GetWidget``
permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: widgets:`GetWidget` on resource: `my-example-widget`
```

In this case, Mateo must ask his administrator to update his policies to allow
access to the `my-example-widget` resource
using the `widgets:`GetWidget``
action.

- Are you trying to access a service that supports [resource-based
  policies](access_policies_identity-vs-resource.md "access_policies_identity-vs-resource.md"), such as Amazon S3, Amazon SNS, or Amazon SQS? If so, verify that the
  policy specifies you as a principal and grants you access. If you make a request
  to a service within your account, either your identity-based policies or the
  resource-based policies can grant you permission. If you make a request to a
  service in a different account, then both your identity-based policies and the
  resource-based policies must grant you permission. To view the services that
  support resource-based policies, see [AWS services that work with
  IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md").
- If your policy includes a condition with a key–value pair, review it
  carefully. Examples include the [aws:RequestTag/tag-key](reference_policies_condition-keys.md "reference_policies_condition-keys.md")
  global condition key, the AWS KMS [`kms:EncryptionContext:`encryption_context_key``](kms/latest/developerguide/policy-conditions.md#conditions-kms-encryption-context "kms/latest/developerguide/policy-conditions.md#conditions-kms-encryption-context"),
  and the `ResourceTag/`tag-key``condition
key supported by multiple services. Make sure that the key name does not match
multiple results. Because condition key names are not case sensitive, a
condition that checks for a key named`foo`matches`foo`,
`Foo`, or `FOO`. If your request includes multiple
  key–value pairs with key names that differ only by case, then your access
  might be unexpectedly denied. For more information, see [IAM JSON policy elements:
  Condition](reference_policies_elements_condition.md "reference_policies_elements_condition.md").
- If you have a [permissions
  boundary](access_policies_boundaries.md "access_policies_boundaries.md"), verify that the policy that is used for the permissions
  boundary allows your request. If your identity-based policies allow the request,
  but your permissions boundary does not, then the request is denied. A
  permissions boundary controls the maximum permissions that an IAM principal
  (user or role) can have. Resource-based policies are not limited by permissions
  boundaries. Permissions boundaries are not common. For more information about
  how AWS evaluates policies, see [Policy evaluation logic](reference_policies_evaluation-logic.md "reference_policies_evaluation-logic.md").
- If you are signing requests manually (without using the [AWS SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")), verify that you
  have correctly [signed
  the request](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md").
- If you're using an [Amazon VPC endpoint
  policy](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") and you get an access denied error that is not logged in
  AWS CloudTrail, it might be because the VPC endpoint owner account is different from
  the calling account or target role account.

## I get "access denied"

when I make a request with temporary security credentials

- First, make sure that you are not denied access for a reason that is unrelated
  to your temporary credentials. For more information, see [I get "access denied" when
  I make a request to an AWS service](#troubleshoot_general_access-denied-service "#troubleshoot_general_access-denied-service").
- Verify that the service accepts temporary security credentials, see [AWS services that work with
  IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md").
- Verify that your requests are being signed correctly and that the request is
  well-formed. For details, see your [toolkit](http://aws.amazon.com/developer/tools/ "http://aws.amazon.com/developer/tools/") documentation or
  [Use temporary credentials with AWS
  resources](id_credentials_temp_use-resources.md "id_credentials_temp_use-resources.md").
- Verify that your temporary security credentials haven't expired. For more
  information, see [Temporary security credentials in IAM](id_credentials_temp.md "id_credentials_temp.md").
- Verify that the IAM user or role has the correct permissions. Permissions
  for temporary security credentials are derived from an IAM user or role. As a
  result, the permissions are limited to those that are granted to the role whose
  temporary credentials you have assumed. For more information about how
  permissions for temporary security credentials are determined, see [Permissions for temporary security
  credentials](id_credentials_temp_control-access.md "id_credentials_temp_control-access.md").
- If you assumed a role, your role session might be limited by session policies.
  When you [request temporary security
  credentials](id_credentials_temp_request.md "id_credentials_temp_request.md") programmatically using AWS STS, you can optionally pass
  inline or managed [session policies](access_policies.md#policies_session "access_policies.md#policies_session").
  Session policies are advanced policies that you pass as a parameter when you
  programmatically create a temporary credential session for a role. You can pass
  a single JSON inline session policy document using the `Policy`
  parameter. You can use the `PolicyArns` parameter to specify up to 10
  managed session policies. The resulting session's permissions are the
  intersection of the role's identity-based policies and the session policies.
  Alternatively, if your administrator or a custom program provides you with
  temporary credentials, they might have included a session policy to limit your
  access.
- If you are an AWS STS federated user principal, your session might be limited by
  session policies. You create a federated user session by signing in to AWS as
  an IAM user and then requesting a federation token. For more information, see
  [Requesting credentials through a custom identity
  broker](id_credentials_temp_request.md#api_getfederationtoken "id_credentials_temp_request.md#api_getfederationtoken"). If you or your identity broker
  passed session policies while requesting a federation token, then your session
  is limited by those policies. The resulting session's permissions are the
  intersection of your IAM user identity-based policies and the session
  policies. For more information about session policies, see [Session policies](access_policies.md#policies_session "access_policies.md#policies_session").
- If you are accessing a resource that has a resource-based policy by using a
  role, verify that the policy grants permissions to the role. For example, the
  following policy allows `MyRole` from account
  `111122223333` to access `amzn-s3-demo-bucket`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "S3BucketPolicy",
 "Effect": "Allow",
 "Principal": {"AWS": ["arn:aws:iam::111122223333:role/MyRole"]},
 "Action": ["s3:PutObject"],
 "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket/*"]
 }]
}`

```

## Access denied error message

examples

Most access denied error messages appear in the format `User
 `user`is not authorized to perform
`action`on`resource`because
`context``. In this example,
 `user`is the [Amazon Resource Name
 (ARN)](reference_identifiers.md#identifiers-arns "reference_identifiers.md#identifiers-arns") that doesn't receive access,`action`is the
 service action that the policy denies, and`resource`is the
 ARN of the resource on which the policy acts. The`context`
field represents additional context about the policy type that explains why the policy
denied access.

When a policy explicitly denies access because the policy contains a `Deny`
statement, then AWS includes the phrase `with an explicit deny in a
 `type` policy` in the access denied error
message. When the policy implicitly denies access, then AWS includes the phrase
`because no `type`policy allows the
`action` action` in the access denied error
message.

###### Note

Some AWS services do not support this access denied error message format. The
content of access denied error messages can vary depending on the service making the
authorization request.

The following examples show the format for different types of access denied error
messages.

### Access denied due to a service

control policy – implicit denial

1. Check for a missing `Allow` statement for the action in your
   service control policies (SCPs). For the following example, the action is
   `codecommit:ListRepositories`.
2. Update your SCP by adding the `Allow` statement. For more
   information, see [Updating an SCP](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy") in the
   _AWS Organizations User Guide_.

```
User: arn:aws:iam::777788889999:user/John is not authorized to perform:
codecommit:ListRepositories because no service control policy allows the codecommit:ListRespositories action
```

### Access denied due to a service

control policy – explicit denial

1. Check for a `Deny` statement for the action in your service
   control policies (SCPs). For the following example, the action is
   `codecommit:ListRepositories`.
2. Update your SCP by removing the `Deny` statement. For more
   information, see [Update a service control policy (SCP)](../../../organizations/latest/userguide/orgs_policies_update.md#update_policy "../../../organizations/latest/userguide/orgs_policies_update.md#update_policy") in the
   _AWS Organizations User Guide_.

```
User: arn:aws:iam::777788889999:user/John is not authorized to perform:
codecommit:ListRepositories with an explicit deny in a service control policy
```

### Access denied due to a

resource control policy – explicit denial

1. Check for a `Deny` statement for the action in your resource
   control policies (RCPs). For the following example, the action is
   `secretsmanager:GetSecretValue`.
2. Update your RCP by removing the `Deny` statement. For more
   information, see [Update a resource control policy (RCP)](../../../organizations/latest/userguide/orgs_policies_update.md#update_policy-rcp "../../../organizations/latest/userguide/orgs_policies_update.md#update_policy-rcp") in the
   _AWS Organizations User Guide_.

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
secretsmanager:GetSecretValue on resource: arn:aws:secretsmanager:us-east-1:123456789012:secret:* with an explicit deny in a resource control policy
```

### Access denied due to

a VPC endpoint policy – implicit denial

1. Check for a missing `Allow` statement for the action in your
   Virtual Private Cloud (VPC) endpoint policies. For the following example,
   the action is `codecommit:ListRepositories`.
2. Update your VPC endpoint policy by adding the `Allow`
   statement. For more information, see [Update a VPC endpoint policy](../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy "../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy") in the
   _AWS PrivateLink Guide_.

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
codecommit:ListRepositories because no VPC endpoint policy allows the codecommit:ListRepositories action
```

### Access denied due to

a VPC endpoint policy – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   Virtual Private Cloud (VPC) endpoint policies. For the following example,
   the action is `codedeploy:ListDeployments`.
2. Update your VPC endpoint policy by removing the `Deny`
   statement. For more information, see [Update a VPC endpoint policy](../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy "../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy") in the
   _AWS PrivateLink Guide_.

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
codedeploy:ListDeployments on resource: arn:aws:codedeploy:us-east-1:123456789012:deploymentgroup:* with an explicit deny in a VPC endpoint policy
```

### Access denied

due to a permissions boundary – implicit denial

1. Check for a missing `Allow` statement for the action in your
   permissions boundary. For the following example, the action is
   `codedeploy:ListDeployments`.
2. Update your permissions boundary by adding the `Allow`
   statement to your IAM policy. For more information, see [Permissions boundaries for IAM
   entities](access_policies_boundaries.md "access_policies_boundaries.md") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
codedeploy:ListDeployments on resource: arn:aws:codedeploy:us-east-1:123456789012:deploymentgroup:* because no permissions boundary allows the codedeploy:ListDeployments action
```

### Access denied

due to a permissions boundary – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   permissions boundary. For the following example, the action is
   `sagemaker:ListModels`.
2. Update your permissions boundary by removing the `Deny`
   statement from your IAM policy. For more information, see [Permissions boundaries for IAM
   entities](access_policies_boundaries.md "access_policies_boundaries.md") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::777788889999:user/John is not authorized to perform:
sagemaker:ListModels with an explicit deny in a permissions boundary
```

### Access denied due

to session policies – implicit denial

1. Check for a missing `Allow` statement for the action in your
   session policies. For the following example, the action is
   `codecommit:ListRepositories`.
2. Update your session policy by adding the `Allow` statement. For
   more information, see [Session
   policies](access_policies.md#policies_session "access_policies.md#policies_session") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
codecommit:ListRepositories because no session policy allows the codecommit:ListRepositories action
```

### Access denied due

to session policies – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   session policies. For the following example, the action is
   `codedeploy:ListDeployments`.
2. Update your session policy by removing the `Deny` statement.
   For more information, see [Session
   policies](access_policies.md#policies_session "access_policies.md#policies_session") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
codedeploy:ListDeployments on resource: arn:aws:codedeploy:us-east-1:123456789012:deploymentgroup:* with an explicit deny in a sessions policy
```

### Access

denied due to resource-based policies – implicit denial

1. Check for a missing `Allow` statement for the action in your
   resource-based policy. For the following example, the action is
   `secretsmanager:GetSecretValue`.
2. Update your policy by adding the `Allow` statement. For more
   information, see [Resource-based policies](access_policies.md#policies_resource-based "access_policies.md#policies_resource-based") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
secretsmanager:GetSecretValue because no resource-based policy allows the secretsmanager:GetSecretValue action
```

### Access

denied due to resource-based policies – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   resource-based policy. For the following example, the action is
   `secretsmanager:GetSecretValue`.
2. Update your policy by removing the `Deny` statement. For more
   information, see [Resource-based policies](access_policies.md#policies_resource-based "access_policies.md#policies_resource-based") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
secretsmanager:GetSecretValue on resource: arn:aws:secretsmanager:us-east-1:123456789012:secret:* with an explicit deny in a resource-based policy
```

### Access denied

due to role trust policies – implicit denial

1. Check for a missing `Allow` statement for the action in your
   role trust policy. For the following example, the action is
   `sts:AssumeRole`.
2. Update your policy by adding the `Allow` statement. For more
   information, see [Resource-based policies](access_policies.md#policies_resource-based "access_policies.md#policies_resource-based") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:user/John is not authorized to perform:
sts:AssumeRole because no role trust policy allows the sts:AssumeRole action
```

### Access denied

due to role trust policies – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   role trust policy. For the following example, the action is
   `sts:AssumeRole`.
2. Update your policy by removing the `Deny` statement. For more
   information, see [Resource-based policies](access_policies.md#policies_resource-based "access_policies.md#policies_resource-based") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::777788889999:user/John is not authorized to perform:
sts:AssumeRole with an explicit deny in the role trust policy
```

### Access

denied due to identity-based policies – implicit denial

1. Check for a missing `Allow` statement for the action in
   identity-based policies attached to the identity. For the following example,
   the action is `codecommit:ListRepositories` attached to the role
   `HR`.
2. Update your policy by adding the `Allow` statement. For more
   information, see [Identity-based policies](access_policies.md#policies_id-based "access_policies.md#policies_id-based") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:role/HR is not authorized to perform:
codecommit:ListRepositories because no identity-based policy allows the codecommit:ListRepositories action
```

### Access is

denied due to identity-based policies – explicit denial

1. Check for an explicit `Deny` statement for the action in
   identity-based policies attached to the identity. For the following example,
   the action is `codedeploy:ListDeployments` attached to the role
   `HR`.
2. Update your policy by removing the `Deny` statement. For more
   information, see [Identity-based policies](access_policies.md#policies_id-based "access_policies.md#policies_id-based") and [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").

```
User: arn:aws:iam::123456789012:role/HR is not authorized to perform:
codedeploy:ListDeployments on resource: arn:aws:codedeploy:us-east-1:123456789012:deploymentgroup:* with an explicit deny in an identity-based policy
```

### Access is denied when a VPC

request fails due to another policy

1. Check for an explicit `Deny` statement for the action in your
   Service Control Policies (SCPs). For the following example, the action is
   `SNS:Publish`.
2. Update your SCP by removing the `Deny` statement. For more
   information, see [Updating an SCP](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy") in the
   _AWS IAM Identity Center User Guide_.

```
User: arn:aws:sts::111122223333:assumed-role/`role-name`/`role-session-name` is not authorized to perform:
SNS:Publish on resource: arn:aws:sns:us-east-1:444455556666:`role-name-2`
with an explicit deny in a VPC endpoint policy transitively through a service control policy
```
