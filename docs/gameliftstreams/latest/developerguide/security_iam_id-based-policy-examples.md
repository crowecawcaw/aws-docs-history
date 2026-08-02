# Identity-based policy examples for Amazon GameLift Streams

By default, users and roles don't have permission to create or modify Amazon GameLift Streams
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon GameLift Streams, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon GameLift Streams](../../../service-authorization/latest/reference/gameliftstreams.md "../../../service-authorization/latest/reference/gameliftstreams.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon GameLift Streams console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Create and manage stream URLs](#create-and-manage-streamurls-iam "#create-and-manage-streamurls-iam")

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete Amazon GameLift Streams resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the Amazon GameLift Streams console

To access the Amazon GameLift Streams console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon GameLift Streams resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

## Allow users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Create and manage stream URLs

This example grants the least privilege required to create, monitor, and revoke stream URLs. `CreateStreamUrl`,
`GetStreamUrl`, and `RevokeStreamUrl` are authorized against a stream group, so you scope them to stream group
resource ARNs. A principal granted these permissions on a stream group can act on every stream URL in that stream group. You cannot scope
these permissions to an individual stream URL. `ListStreamUrls` is account-scoped and returns stream URLs across your stream
groups, so it takes `Resource` set to `"*"`. In addition, `CreateStreamUrl` requires
`gameliftstreams:StartStreamSession` permission for the application the stream URL points to, because activating the stream URL
starts a stream session that runs that application. Scope this permission to the application resource ARN.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageStreamUrls",
      "Effect": "Allow",
      "Action": [
        "gameliftstreams:CreateStreamUrl",
        "gameliftstreams:GetStreamUrl",
        "gameliftstreams:RevokeStreamUrl"
      ],
      "Resource": "arn:aws:gameliftstreams:*:`111122223333`:streamgroup/*"
    },
    {
      "Sid": "StartSessionsForStreamUrls",
      "Effect": "Allow",
      "Action": "gameliftstreams:StartStreamSession",
      "Resource": "arn:aws:gameliftstreams:*:`111122223333`:application/*"
    },
    {
      "Sid": "ListStreamUrlsInAccount",
      "Effect": "Allow",
      "Action": "gameliftstreams:ListStreamUrls",
      "Resource": "*"
    }
  ]
}
```

If you pass an IAM role in `RoleArn` when you create a stream URL, also grant `iam:PassRole` for that role, scoped
to Amazon GameLift Streams:

```
{
  "Sid": "PassRoleToStreamUrlSessions",
  "Effect": "Allow",
  "Action": "iam:PassRole",
  "Resource": "arn:aws:iam::`111122223333`:role/GameLiftStreams-`MyStreamRole`",
  "Condition": {
    "StringEquals": {
      "iam:PassedToService": "gameliftstreams.amazonaws.com"
    }
  }
}
```

###### Important

Because `CreateStreamUrl` freezes the stream URL's configuration (including an optional IAM role passed in
`RoleArn`) at creation time, grant this permission only to trusted principals. Anyone who can create a stream URL can hand
out unauthenticated, temporary access to a stream session.
