# Resource quotas

AWS KMS establishes resource quotas to ensure that it can provide fast and resilient service
to all of our customers. Some resource quotas apply only to resources that you create, but not
to resources that AWS services create for you. Resources that you use, but that aren't in your
AWS account, such as [AWS owned keys](concepts.md#aws-owned-key "concepts.md#aws-owned-key"), do not count against
these quotas.

If you have exceeded a resource limit, requests to create an additional resource of that
type generate an `LimitExceededException` error message.

All AWS KMS resource quotas are adjustable, except for the [on-demand rotation resource quota](#on-demand-rotation-resource-quota "#on-demand-rotation-resource-quota"). To request a quota increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-increase.md "../../../servicequotas/latest/userguide/request-increase.md") in the _Service Quotas User Guide_. To request a quota decrease, to change a quota that is not listed in Service Quotas, or to change a quota in an AWS Region where Service Quotas for AWS KMS is not available,
please visit [AWS Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") and
create a case.

The following table lists and describes the AWS KMS resource quotas in each AWS account and
Region.

| Quota name                                                                                    | Default value | Applies to               | Adjustable |
| --------------------------------------------------------------------------------------------- | ------------- | ------------------------ | ---------- |
| [AWS KMS keys](#kms-keys-limit "#kms-keys-limit")                                             | 100,000       | Customer managed keys    | Yes        |
| [Aliases per KMS key](#aliases-per-key "#aliases-per-key")                                    | 10            | Customer created aliases | Yes        |
| [Grants per KMS key](#grants-per-key "#grants-per-key")                                       | 50,000        | Customer managed keys    | Yes        |
| [Custom key store resource quota](#cks-resource-quota "#cks-resource-quota")                  | 10            | AWS account and Region   | Yes        |
| [On-demand rotation](#on-demand-rotation-resource-quota "#on-demand-rotation-resource-quota") | 50            | Customer managed keys    | No         |

In addition to resource quotas, AWS KMS uses request quotas to ensure the responsiveness of the
service. For details, see [Request quotas](requests-per-second.md "requests-per-second.md").

## AWS KMS keys: 100,000

You can have up to 100,000 [customer managed keys](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") in each
Region of your AWS account. This quota applies to all customer managed keys in all AWS Regions
regardless of their [key spec](create-keys.md#key-spec "create-keys.md#key-spec") or [key
state](key-state.md "key-state.md"). Each KMS key is considered to be one resource. [AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key") and [AWS owned keys](concepts.md#aws-owned-key "concepts.md#aws-owned-key") do not count against this quota.

## Aliases per KMS key: 50

You can associate up to 50 [aliases](kms-alias.md "kms-alias.md") with each [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key"). Aliases that AWS associates with
[AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key") do not count against this quota.
You might encounter this quota when you [create](alias-create.md "alias-create.md") or [update](alias-update.md "alias-update.md") an alias.

###### Note

The [kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases "conditions-kms.md#conditions-kms-resource-aliases") condition
is effective only when the KMS key conforms to this quota. If a KMS key exceeds this quota,
principals who are authorized to use the KMS key by the `kms:ResourceAliases`
condition are denied access to the KMS key. For details, see [Access denied due to alias quota](troubleshooting-tags-aliases.md#access-denied-alias-quota "troubleshooting-tags-aliases.md#access-denied-alias-quota").

The Aliases per KMS key quota replaces the Aliases per Region quota that limited the total number of aliases in each Region of an AWS account. AWS KMS has eliminated the Aliases per Region quota.

## Grants per KMS key: 50,000

Each [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") can have up to 50,000
[grants](grants.md "grants.md"), including the grants created by [AWS services that are integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration").
This quota does not apply to [AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key") or
[AWS owned keys](concepts.md#aws-owned-key "concepts.md#aws-owned-key").

One effect of this quota is that you cannot perform more than 50,000 grant-authorized
operations that use the same KMS key at the same time. After you reach the quota, you can create
new grants on the KMS key only when an active grant is retired or revoked.

For example, when you attach an Amazon Elastic Block Store (Amazon EBS) volume to an Amazon Elastic Compute Cloud (Amazon EC2) instance,
the volume is decrypted so you can read it. To get permission to decrypt the data, Amazon EBS
creates a grant for each volume. Therefore, if all of your Amazon EBS volumes use the same KMS key,
you cannot attach more than 50,000 volumes at one time.

## Custom key stores resource quota: 10

You can create up to 10 [custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview")
in each AWS account and Region. If you try to create more, the [CreateCustomKeyStore](../APIReference/API_CreateCustomKeyStore.md "../APIReference/API_CreateCustomKeyStore.md") operation
fails.

This quota applies to the total number of custom key stores in each account and region,
including all [AWS CloudHSM key stores](keystore-cloudhsm.md "keystore-cloudhsm.md") and [external key stores](keystore-external.md "keystore-external.md"), regardless of their connection
state.

## On-demand rotation: 10

You can perform [on-demand key rotation](rotating-keys-on-demand.md "rotating-keys-on-demand.md") a
maximum of 10 times per KMS key. If you try to perform more on-demand rotations, the
[RotateKeyOnDemand](../APIReference/API_RotateKeyOnDemand.md "../APIReference/API_RotateKeyOnDemand.md") operation
fails.

This quota is not adjustable. You cannot increase it by using Service Quotas or by creating a
case in AWS Support. To prevent reaching the on-demand rotation quota, we recommend using
[automatic key rotation](rotating-keys-enable.md "rotating-keys-enable.md") whenever possible.
