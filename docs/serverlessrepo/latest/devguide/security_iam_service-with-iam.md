# How the AWS Serverless Application Repository Works with

IAM

Before you use IAM to manage access to the AWS Serverless Application Repository, you should understand what
IAM features are available to use with the AWS Serverless Application Repository.

To get an overview of how IAM works, see [Understanding How IAM Works](../../../IAM/latest/UserGuide/intro-structure.md "../../../IAM/latest/UserGuide/intro-structure.md") in the _IAM User Guide_. To
get a high-level view of how the AWS Serverless Application Repository and other AWS services work with IAM,
see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [AWS Serverless Application Repository
  Identity-Based Policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [AWS Serverless Application Repository
  Application Policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization Based on
  AWS Serverless Application Repository Tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [AWS Serverless Application Repository IAM
  Roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## AWS Serverless Application Repository

Identity-Based Policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources, as well as the conditions under which actions are allowed or denied. The
AWS Serverless Application Repository supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

The following shows an example of a permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateApplication",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:CreateApplication"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreateApplicationVersion",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:CreateApplicationVersion"
 ],
 "Resource": "arn:aws:serverlessrepo:`us-east-1:``111122223333`:applications/`application-name`"
 }
 ]
}`

```

The policy has two statements:

- The first statement grants permissions for the AWS Serverless Application Repository action
  `serverlessrepo:CreateApplication` on all AWS Serverless Application Repository resources, as
  specified by the wildcard character (\*) as the `Resource` value.
- The second statement grants permission for the AWS Serverless Application Repository action
  `serverlessrepo:CreateApplicationVersion` on an AWS resource by
  using the Amazon Resource Name (ARN) for an AWS Serverless Application Repository application. The application
  is specified by the `Resource` value.

The policy doesn't specify the `Principal` element because in an
identity-based policy, you don't specify the principal who gets the permission. When you
attach policy to a user, the user is the implicit principal. When you attach a
permission policy to an IAM role, the principal identified in the role's trust policy
gets the permissions.

For a table showing all of the AWS Serverless Application Repository API operations and the AWS resources that
they apply to, see [AWS Serverless Application Repository API Permissions: Actions and
Resources Reference](serverlessrepo-api-permissions-ref.md "serverlessrepo-api-permissions-ref.md").

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in the AWS Serverless Application Repository use the following prefix before the action:
`serverlessrepo:`. For example, to grant someone permission to
run an AWS Serverless Application Repository instance with the AWS Serverless Application Repository
`SearchApplications` API operation, you include the
`serverlessrepo:SearchApplications` action in their policy.
Policy statements must include either an `Action` or
`NotAction` element. The AWS Serverless Application Repository defines its own set of
actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "serverlessrepo:*action1*",
      "serverlessrepo:*action2*"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `List`, include the following
action:

```
`"Action": "serverlessrepo:List*"`
```

To see a list of AWS Serverless Application Repository actions, see [Actions Defined by AWS Serverless Application Repository](../../../IAM/latest/UserGuide/list_awsserverlessapplicationrepository.md#awsserverlessapplicationrepository-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsserverlessapplicationrepository.md#awsserverlessapplicationrepository-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

In the AWS Serverless Application Repository, the primary AWS resource is an AWS Serverless Application Repository
_application_. AWS Serverless Application Repository applications have unique Amazon Resource
Names (ARNs) associated with them, as shown in the following table.

| AWS Resource Type | Amazon Resource Name (ARN) Format                                                    |
| ----------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application       | arn:`partition`:serverlessrepo:`region`:`account-id`:applications/`application-name` | For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md"). The following is an example policy that grants permissions for the `serverlessrepo:ListApplications` action on all AWS resources. In the current implementation, the AWS Serverless Application Repository doesn't support identifying specific AWS resources by using the AWS resource ARNs (also referred to as resource-level permissions) for some of the API actions. In these cases, you must specify a wildcard character (\*). JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Sid": "ListExistingApplications", "Effect": "Allow", "Action": [ "serverlessrepo:ListApplications" ], "Resource": "*" } ] }` `` For a table showing all of the AWS Serverless Application Repository API actions and the AWS resources that they apply to, see [AWS Serverless Application Repository API Permissions: Actions and Resources Reference](serverlessrepo-api-permissions-ref.md "serverlessrepo-api-permissions-ref.md"). ### Condition Keys The AWS Serverless Application Repository doesn't provide any service-specific condition keys, but it does support using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_. ### Examples To view examples of AWS Serverless Application Repository identity-based policies, see [AWS Serverless Application Repository Identity-Based Policy Examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). ## AWS Serverless Application Repository Application Policies Application policies determine the actions that a specified principal or principalOrg can perform on an AWS Serverless Application Repository application. You can add permissions to the policy associated with an AWS Serverless Application Repository application. Permissions policies attached to AWS Serverless Application Repository applications are referred to as _application policies_. [Application policies](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md") are extensions of [IAM resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md"). The primary resource is the AWS Serverless Application Repository application. You can use AWS Serverless Application Repository application policies to manage application deployment permissions. AWS Serverless Application Repository application policies are primarily used by publishers to grant permission to consumers to deploy their applications, and related operations such as to search for and view details of those applications. Publishers can set application permissions to the following three categories: <br>• **Private** – Applications that were created with the same account, and haven't been shared with any other account. You have permission to deploy applications that were created using your AWS account. <br>• **Privately shared** – Applications that the publisher has explicitly shared with a specific set of AWS accounts or AWS Organizations. You have permission to deploy applications that have been shared with your AWS account or AWS Organization. <br>• **Publicly shared** – Applications that the publisher has shared with everyone. You have permission to deploy any publicly shared application. You can grant permissions by using the AWS CLI, the AWS SDKs, or the AWS Management Console. ### Examples To view examples of managing AWS Serverless Application Repository application policies, see [AWS Serverless Application Repository Application Policy Examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md"). ## Authorization Based on AWS Serverless Application Repository Tags The AWS Serverless Application Repository doesn't support controlling access to resources or actions based on tags. ## AWS Serverless Application Repository IAM Roles An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific permissions. ### Using Temporary Credentials with the AWS Serverless Application Repository You can use temporary credentials to sign in with federation, to assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md"). The AWS Serverless Application Repository supports using temporary credentials. ### Service-Linked Roles The AWS Serverless Application Repository doesn't support service-linked roles. ### Service Roles The AWS Serverless Application Repository doesn't support service roles. |
