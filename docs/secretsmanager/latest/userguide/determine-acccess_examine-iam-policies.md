# Determine who has permissions to

your AWS Secrets Manager secrets

By default, IAM identities don't have permission to access secrets. When authorizing
access to a secret, Secrets Manager evaluates the resource-based policy attached to the secret and all
identity-based policies attached to the IAM user or role sending the request. To do this,
Secrets Manager uses a process similar to the one described in [Determining whether a request is allowed or denied](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow") in the _IAM User Guide_.

When multiple policies apply to a request, Secrets Manager uses a hierarchy to control
permissions:

1. If a statement in any policy with an explicit `deny` matches the request action
   and resource:

The explicit `deny` overrides everything else and blocks the action. 2. If there is no explicit `deny`, but a statement with an explicit `allow` matches
the request action and resource:

The explicit `allow` grants the action in the request access to the resources in the
statement.

If the identity and the secret are in two different accounts, there must be an
`allow` in both the resource policy for the secret and the policy
attached to the identity, otherwise AWS denies the request. For more information,
see [Cross-account
access](auth-and-access_examples_cross.md "auth-and-access_examples_cross.md"). 3. If there is no statement with an explicit `allow` that matches the
request action and resource:

AWS denies the request by default, which is called an
_implicit_ deny.

###### To view the resource-based policy for a secret

- Do one of the following:
  - Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/"). In the secret details page
    for your secret, in the **Resource permissions** section,
    choose **Edit permissions**.
  - Use the AWS CLI to call [`get-resource-policy`](../../../cli/latest/reference/secretsmanager/get-resource-policy.md "../../../cli/latest/reference/secretsmanager/get-resource-policy.md") or AWS SDK to call [`GetResourcePolicy`](../apireference/API_GetResourcePolicy.md "../apireference/API_GetResourcePolicy.md").

###### To determine who has access through identity-based policies

- Use the IAM policy simulator. See [Testing IAM
  policies with the IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md")
