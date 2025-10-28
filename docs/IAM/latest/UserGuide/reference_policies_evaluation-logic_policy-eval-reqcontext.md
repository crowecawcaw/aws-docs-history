# Processing the

request context

When AWS evaluates and authorizes a request, it assembles the request information into a
_request context_. The request context contains any information that
can be used in policy evaluation.

- **Principal** – The user, role, or federated
  user principal that sent the request. Information about the principal includes the policies
  that are associated with that principal.
- **Actions** – One or more actions that the
  principal wants to perform.
- **Resources** – One or more AWS resource
  objects upon which the actions or operations are performed.
- **Resource data** – Data related to the
  resource that is being requested. This can include information such as a DynamoDB table
  name or a tag on an Amazon EC2 instance.
- **Environment data** – Information about the
  IP address, user agent, SSL enabled status, or the time of day.
  This information is compared against applicable policies to determine whether to allow or
  deny the request. You can organize this property information using the
  **Principal**, **Action**,
  **Resource**, and **Condition** (PARC) model to better
  understand how AWS policies are evaluated.

## Understanding the PARC model

The PARC model represents the request context based on the four JSON elements in the
policy language:

- [Principal](reference_policies_elements_principal.md "reference_policies_elements_principal.md") – The
  entity making the request. A principal represents a human user or programmatic
  workload that can be authenticated and then authorized to perform actions in
  AWS accounts.
- [Action](reference_policies_elements_action.md "reference_policies_elements_action.md") – The
  operation being performed. Often the action will map to an API action.
- [Resource](reference_policies_elements_resource.md "reference_policies_elements_resource.md") – The
  AWS resource on which the action is being performed.
- [Condition](reference_policies_elements_condition.md "reference_policies_elements_condition.md") –
  Additional constraints that must be met for the request to be allowed.

The following shows an example of how the PARC model might represent a request context:

```
Principal: AIDA123456789EXAMPLE
Action: s3:CreateBucket
Resource: arn:aws:s3:::amzn-s3-demo-bucket1
Context:
- aws:UserId=AIDA123456789EXAMPLE:BobsSession
- aws:PrincipalAccount=123456789012
- aws:PrincipalOrgId=o-example
- aws:PrincipalARN=arn:aws:iam::AIDA123456789EXAMPLE:role/HR
- aws:MultiFactorAuthPresent=true
- aws:CurrentTime=...
- aws:EpochTime=...
- aws:SourceIp=...
- aws:PrincipalTag/dept=123
- aws:PrincipalTag/project=blue
- aws:RequestTag/dept=123
```

## Importance of the request context

Understanding the request context and how it interacts with policy evaluation is
crucial for:

- Troubleshooting access issues
- Designing effective and secure policies
- Understanding the full scope of permissions granted by a policy
- Predicting the outcome of policy evaluations in different scenarios

By visualizing the request context using the PARC model, you can more easily
understand how AWS makes authorization decisions and design your policies more
effectively.

## How AWS uses the request context

When evaluating policies, AWS compares the information in the request context with
the information specified in all applicable policies. This includes identity-based
policies, resource-based policies, IAM permissions boundaries, Organizations SCPs,
Organizations RCPs, and session policies.

For each policy type, AWS uses the request context to check:

- Whether the policy applies to the request based on the principal.
- Whether the requested action is allowed on the specified resource.
- Whether any conditions specified in the policy are met by the request
  context.

How AWS evaluates policies depends on the types of policies that apply to the
request context. These policy types are available for use within a single AWS account.
For more information about these policy types, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md"). To learn how AWS evaluates policies for
cross-account access, see [Cross-account policy
evaluation logic](reference_policies_evaluation-logic-cross-account.md "reference_policies_evaluation-logic-cross-account.md").

- **AWS Organizations resource control policies (RCPs)**
  – AWS Organizations RCPs specify the maximum available permissions for resources
  within accounts in an organization or organizational unit (OU). RCPs apply to
  resources in member accounts and impact the effective permissions for
  principals, including the AWS account root user, regardless of whether the principals
  belong to your organization. RCPs don't apply to resources in the organization
  management account and to calls made by service-linked roles. If an RCP is
  present, permissions granted by identity-based and resource-based policies to
  resources in your member accounts are only effective if the RCP allows the
  action.
- **AWS Organizations service control policies (SCPs)**
  – AWS Organizations SCPs specify the maximum available permissions for principals
  within accounts in an organization or organizational unit (OU). SCPs apply to
  principals in member accounts, including each AWS account root user. If an SCP is present,
  permissions granted by identity-based and resource-based policies to principals
  in your member accounts are only effective if the SCP allows the action. The
  only exceptions are principals in the organization management account and
  service-linked roles.
- **Resource-based policies** –
  Resource-based policies grant permissions for principals specified in the
  policy. The permissions define what the principal can do with the resource to
  which the policy is attached.
- **Permissions boundaries** – Permissions
  boundaries are a feature that sets the maximum permissions that an
  identity-based policy can grant to an IAM entity (user or role). When you set
  a permissions boundary for an entity, the entity can perform only the actions
  that are allowed by both its identity-based policies and its permissions
  boundary. In some cases, an implicit deny in a permissions boundary can limit
  the permissions granted by a resource-based policy. For more information, see
  [How AWS
  enforcement code logic evaluates requests to allow or deny access](reference_policies_evaluation-logic_policy-eval-denyallow.md "reference_policies_evaluation-logic_policy-eval-denyallow.md").
- **Identity-based policies** –
  Identity-based policies are attached to an IAM identity (user, group of users,
  or role) and grant permissions to IAM entities (users and roles). If only
  identity-based policies apply to a request, then AWS checks all of those
  policies for at least one `Allow`.
- **Session policies** – Session policies
  are policies that you pass as parameters when you programmatically create a
  temporary session for a role or federated user session. To create a role session
  programmatically, use one of the `AssumeRole*` API operations. When
  you do this and pass session policies, the resulting session's permissions are
  the intersection of the IAM entity's identity-based policy and the session
  policies. To create a federated user session, you use the IAM user access keys
  to programmatically call the `GetFederationToken` API operation. For
  more information, see [Session policies](access_policies.md#policies_session "access_policies.md#policies_session").

Remember, an explicit deny in any of these policies overrides the allow.

###### Note

**AWS Organizations declarative policies** allow you to
centrally declare and enforce your desired configuration for a given AWS service
at scale across an organization. Since declarative policies are applied directly at
the service level, they don't directly impact policy evaluation requests and aren't
included with the request context. For more information, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the AWS Organizations User Guide.

## Example policy evaluation using the PARC

model

To illustrate how the request context interacts with policy evaluation, let's consider
an example policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:CreateBucket",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalTag/dept": "123"
 }
 }
 }
 ]
}`

```

In this example, the policy would allow the `CreateBucket` action only when
the request context includes an `aws:PrincipalTag/dept` value of "123" and the resource
matches the `amzn-s3-demo-bucket1` bucket name. The following table shows how
AWS uses the request context to evaluate this policy and make authorization
decisions.

| Policy                                               | Request context                                                                                                                                      | Evaluation result |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `"StringEquals": { "aws:PrincipalTag/dept": "123" }` | `Principal: AIDA123456789EXAMPLE Action: s3:CreateBucket Resource: arn:aws:s3:::amzn-s3-demo-bucket1 Context: <br>• aws:PrincipalTag/dept=123`       | **Match**         |
| `"StringEquals": { "aws:PrincipalTag/dept": "123" }` | ``Principal: AIDA123456789EXAMPLE Action: s3:`DeleteBucket` Resource: arn:aws:s3:::amzn-s3-demo-bucket1 Context: <br>• aws:PrincipalTag/dept=123``   | **No match**      |
| `"StringEquals": { "aws:PrincipalTag/dept": "123" }` | `` Principal: AIDA123456789EXAMPLE Action: s3:CreateBucket Resource: arn:aws:s3:::amzn-s3-demo-bucket1 Context: <br>• aws:PrincipalTag/dept=`321` `` | **No match**      |
| `"StringEquals": { "aws:PrincipalTag/dept": "123" }` | `Principal: AIDA123456789EXAMPLE Action: s3:CreateBucket Resource: arn:aws:s3:::amzn-s3-demo-bucket1 Context:` No `aws:PrincipalTag` in the request. | **No match**      |
