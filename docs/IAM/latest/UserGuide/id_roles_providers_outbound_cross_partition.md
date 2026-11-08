

# Federating AWS identities across AWS partitions
<a name="id_roles_providers_outbound_cross_partition"></a>

Cross-partition identity federation allows a workload to obtain short-lived access across [AWS partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html). AWS partitions are hard isolation boundaries with independent instances of AWS Identity and Access Management (IAM), so a credential issued in one partition isn't valid in another. As a result, direct role assumption with the [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) API doesn't work across partition boundaries.

Cross-partition identity federation works as a two-step exchange: your workload calls [sts:GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) to obtain a short-lived JSON Web Token (JWT) from [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) in the source partition. It then calls [sts:AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) to exchange the token for temporary credentials in the destination partition. This approach lets the workload use temporary credentials in both partitions, following the IAM best practice of [using temporary credentials for workloads](best-practices.md#bp-workloads-use-roles).

**Note**  
Cross-partition identity federation is available in the commercial AWS Regions (`aws`), the China Regions (`aws-cn`), the AWS GovCloud (US) Regions (`aws-us-gov`), and the AWS European Sovereign Cloud (`aws-eusc`).
The destination role must be in a different AWS partition from the one where the token was issued. The JWTs from `GetWebIdentityToken` cannot be used for OpenID Connect (OIDC) federation into the same partition through `AssumeRoleWithWebIdentity`. For role assumption within a partition, use the `AssumeRole` API instead.
If your workload requires cross-partition access, consult your compliance team to make sure that your implementation aligns with your regulatory or compliance obligations.

## How cross-partition identity federation works
<a name="cross-partition-how-it-works"></a>

Your workload first requests a token from AWS STS in the source partition, then sends the token to AWS STS in the destination partition. To validate the request, AWS STS in the destination partition retrieves verification keys from the source account's OIDC issuer, verifies the token, and evaluates the destination role's trust policy. If the request is allowed, AWS STS returns temporary credentials to the workload, which uses them to call services and access resources in the destination partition.

<a name="cross-partition-flow-diagram"></a>![Source STS issues a token; destination STS validates it and returns credentials the workload uses to access resources.](https://docs.aws.amazon.com/IAM/latest/UserGuide/images/outbound-cross-partition-flow.png)


The flow works as follows:

1. **Token request**: Your workload, running in an AWS Region in the source partition (for example, `us-east-1` in the `aws` partition), calls the `sts:GetWebIdentityToken` API.

1. **Token issuance**: AWS STS returns a short-lived, cryptographically signed JWT. The token contains claims that assert your workload's AWS identity, including the account ID, the principal Amazon Resource Name (ARN), the source AWS Region, and more.

1. **Token presentation**: Your workload calls `sts:AssumeRoleWithWebIdentity` on the AWS STS endpoint in an AWS Region in the destination partition (for example, `cn-north-1` in the `aws-cn` partition), passing the JWT as the web identity token and the ARN of the target role in the destination partition.

1. **Fetch verification keys and metadata**: AWS STS in the destination partition retrieves the public verification key from the JWKS endpoint of the source account's issuer URL.

1. **Validation**: AWS STS in the destination partition verifies the token's signature and evaluates the target role's trust policy.

1. **Return temporary credentials**: AWS STS in the destination partition returns temporary credentials scoped by the policies attached to the role.

1. **Cross-partition resource access**: Your workload uses the temporary credentials to access resources in the destination partition, such as an Amazon S3 bucket.

For more information, see the following topics:
+ [Setting up cross-partition identity federation](id_roles_providers_outbound_cross_partition_setup.md)
+ [Controls for cross-partition identity federation](id_roles_providers_outbound_cross_partition_controls.md)
+ [Auditing cross-partition identity federation](id_roles_providers_outbound_cross_partition_auditing.md)
+ [Available keys for AWS OIDC federation](reference_policies_iam-condition-keys.md#condition-keys-wif)