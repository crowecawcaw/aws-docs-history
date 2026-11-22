

# Assume an IAM role to retrieve secrets with the ASCP

By default, the ASCP retrieves secrets with the Pod's IAM role, which the Pod gets through IAM Roles for Service Accounts (IRSA) or Amazon EKS Pod Identity.

If you set `assumeRoleArn` in the `SecretProviderClass`, the ASCP uses the Pod's credentials to call AWS STS `AssumeRole` and retrieves the secrets as the assumed role instead. If that role is in the account that owns the secrets, you don't need a resource policy or cross-account sharing. The containers in the Pod aren't affected and keep the Pod's own credentials.

Use `assumeRoleArn` in the following situations:
+ Your secrets are in a different account from the cluster, and you want to grant access with a role in that account instead of a resource policy on each secret and its AWS KMS key. For the resource policy approach, see [Access AWS Secrets Manager secrets from a different account](auth-and-access_examples_cross.md).
+ Your Pods need parameters from AWS Systems Manager Parameter Store in a different account.
+ `SecretProviderClass` resources that share a service account need different roles.

With Amazon EKS Pod Identity, you can instead assign a [target IAM role](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-assign-target-role.html) in the Pod Identity association. The Pod then receives the target role's credentials, and you don't change the `SecretProviderClass`.

## Required permissions
<a name="integrating_ascp_assume_role_setup"></a>

In this section, the *target role* is the role that the ASCP assumes, and the *base role* is the Pod's own role (the IRSA role or the Pod Identity role). They can be in the same account or in different accounts, and they need the following permissions:
+ The base role must have `sts:AssumeRole` permission on the target role ARN. It doesn't need Secrets Manager or Parameter Store permissions of its own.

  A Pod Identity base role must also have `sts:TagSession` permission on the target role ARN, unless you disable session tags in the Pod Identity association.
+ The target role must have `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` permissions for the secrets to mount, and `ssm:GetParameters` for Parameter Store parameters. If a secret or parameter is encrypted with a customer managed key, it also needs `kms:Decrypt` on the key. For an example policy, see [Example: Permission to read and describe individual secrets](auth-and-access_iam-policies.md#auth-and-access_examples-read-and-describe).
+ The target role's trust policy must allow the base role to assume it. For an IRSA base role, allow `sts:AssumeRole`.

  A Pod Identity base role carries [session tags](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html) by default, and AWS STS passes them on to the `AssumeRole` call, so the trust policy must also allow `sts:TagSession`. If either the trust policy or the base role's permissions policy lacks it, the mount fails. Neither policy needs `sts:TagSession` if you disable session tags in the Pod Identity association. The following trust policy lets {{PodBaseRole}} in {{Account2}} assume the target role, and its condition keys limit that to one cluster, namespace, and service account. Replace the role name, account ID, and condition values with your own:

  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam::{{Account2}}:role/{{PodBaseRole}}"
        },
        "Action": ["sts:AssumeRole", "sts:TagSession"],
        "Condition": {
          "StringEquals": {
            "aws:PrincipalTag/eks-cluster-arn": "arn:aws:eks:{{region}}:{{Account2}}:cluster/{{my-cluster}}",
            "aws:PrincipalTag/kubernetes-namespace": "{{my-namespace}}",
            "aws:PrincipalTag/kubernetes-service-account": "{{my-service-account}}"
          }
        }
      }
    ]
  }
  ```

Then set `assumeRoleArn` in the `SecretProviderClass` to the ARN of the target role. You don't need to change anything else on the cluster. The ASCP retrieves the objects as the target role, so a secret name without an ARN resolves in the target role's account. For more information, see [Example: Assume a role in another account](ascp-examples.md#assume-role-cross-account).

## How the ASCP assumes the role
<a name="integrating_ascp_assume_role_behavior"></a>

The ASCP calls `AssumeRole` on every mount, including every rotation poll of the Secrets Store CSI Driver, and the calls count against the AWS STS quota of the cluster's account. Each session lasts 15 minutes and carries no external ID. The call goes to the AWS STS endpoint in `region`, and to the one in `failoverRegion` if you set it. The role session name is `{{namespace}}@{{serviceAccountName}}`, cut at 64 characters, so CloudTrail events in the target role's account show which workload read the secret.

If AWS STS denies the call, the mount fails, and the Pod's `FailedMount` event shows the AWS STS error with the Pod's role and the target role in it. To see the event, run `kubectl describe pod/{{podId}}`.

With a Pod Identity base role, the error reads `not authorized to perform: sts:TagSession`. AWS STS returns that same message when the trust policy lacks `sts:TagSession`, when the base role's permissions policy lacks it, and when the trust policy doesn't match the caller at all because of a wrong principal or condition value. Check all three.