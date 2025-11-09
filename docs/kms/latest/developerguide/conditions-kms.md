# AWS KMS condition keys

AWS KMS provides a set of condition keys that you can use in key policies and IAM
policies. These condition keys are specific to AWS KMS. For example, you can use the
`kms:EncryptionContext:*context-key*` condition key to require a particular [encryption context](encrypt_context.md "encrypt_context.md") when controlling access to a symmetric
encryption KMS key.

**Conditions for an API operation request**

Many AWS KMS condition keys control access to a KMS key based on the value of a parameter
in the request for an AWS KMS operation. For example, you can use the [kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec") condition key in an IAM policy to
allow use of the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation only
when the value of the `KeySpec` parameter in the `CreateKey` request is
`RSA_4096`.

This type of condition works even when the parameter doesn't appear in the request, such
as when you use the parameter's default value. For example you can use the [kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec") condition key to allow users to use the
`CreateKey` operation only when the value of the `KeySpec` parameter
is `SYMMETRIC_DEFAULT`, which is the default value. This condition allows requests
that have the `KeySpec` parameter with the `SYMMETRIC_DEFAULT` value and
requests that have no `KeySpec` parameter.

**Conditions for KMS keys used in API operations**

Some AWS KMS condition keys can control access to operations based on a property of the
KMS key that is used in the operation. For example, you can use the [kms:KeyOrigin](#conditions-kms-key-origin "#conditions-kms-key-origin") condition to allow principals to
call [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") on a KMS key
only when the `Origin` of the KMS key is `AWS_KMS`. To find out if a
condition key can be used in this way, see the description of the condition key.

The operation must be a _KMS key resource operation_, that is, an operation that is authorized for a particular KMS key. To identify the KMS key resource operations, in the [Actions
and Resources Table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look for a value of `KMS key` in the `Resources` column for the operation. If you use this type of condition key with an operation
that is not authorized for a particular KMS key resource, like [ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md"), the permission is not effective
because the condition can never be satisfied. There is no KMS key resource involved in
authorizing the `ListKeys` operation and no `KeySpec` property.

The following topics describe each AWS KMS condition key and include example policy
statements that demonstrate policy syntax.

**Using set operators with condition
keys**

When a policy condition compares two set of values, such as the set of tags in a request
and the set of tags in a policy, you need tell AWS how to compare the sets. IAM defines
two set operators, `ForAnyValue` and `ForAllValues`, for this purpose.
Use set operators only with _multi-valued condition keys_,
which require them. Do not use set operators with _single-valued
condition keys_. As always, test your policy statements thoroughly before using
them in a production environment.

Condition keys are single-valued or multi-valued. To determine whether an AWS KMS condition
key is single-valued or multi-valued, see the **Value type** column in the
condition key description.

- _Single-valued_ condition keys have at most one
  value in the authorization context (the request or resource). For example, because each
  API call can originate from only one AWS account, [kms:CallerAccount](#conditions-kms-caller-account "#conditions-kms-caller-account") is a single valued
  condition key. Do not use a set operator with a single-valued condition key.
- _Multi-valued_ condition keys have multiple values in
  the authorization context (the request or resource). For example, because each KMS key
  can have multiple aliases, [kms:ResourceAliases](#conditions-kms-resource-aliases "#conditions-kms-resource-aliases") can have multiple values. Multi-valued condition keys
  require a set operator.
  Note that the difference between single-valued and multi-valued condition keys depends on
  the number of values in the authorization context; not the number of values in the policy
  condition.

###### Warning

Using a set operator with a single-valued condition key can create a policy statement
that is overly permissive (or overly restrictive). Use set operators only with multi-valued
condition keys.

If you create or update a policy that includes a `ForAllValues` set operator
with the kms:EncryptionContext:_context-key_ or `aws:RequestTag/*tag-key*` condition keys, AWS KMS returns the following error
message:

`OverlyPermissiveCondition: Using the ForAllValues set operator with a
 single-valued condition key matches requests without the specified [encryption context or
 tag] or with an unspecified [encryption context or tag]. To fix, remove
 ForAllValues.`

For detailed information about the `ForAnyValue` and `ForAllValues`
set operators, see [Using multiple keys and values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions") in the _IAM User Guide_. For information about the risk of using the
`ForAllValues` set operator with a single-valued condition, see [Security Warning – ForAllValues with single valued key](../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md#access-analyzer-reference-policy-checks-security-warning-forallvalues-with-single-valued-key "../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md#access-analyzer-reference-policy-checks-security-warning-forallvalues-with-single-valued-key") in the _IAM User Guide_.

###### Topics

- [kms:BypassPolicyLockoutSafetyCheck](#conditions-kms-bypass-policy-lockout-safety-check "#conditions-kms-bypass-policy-lockout-safety-check")
- [kms:CallerAccount](#conditions-kms-caller-account "#conditions-kms-caller-account")
- [kms:CustomerMasterKeySpec
  (deprecated)](#conditions-kms-key-spec-replaced "#conditions-kms-key-spec-replaced")
- [kms:CustomerMasterKeyUsage
  (deprecated)](#conditions-kms-key-usage-replaced "#conditions-kms-key-usage-replaced")
- [kms:DataKeyPairSpec](#conditions-kms-data-key-spec "#conditions-kms-data-key-spec")
- [kms:EncryptionAlgorithm](#conditions-kms-encryption-algorithm "#conditions-kms-encryption-algorithm")
- [kms:EncryptionContext:context-key](#conditions-kms-encryption-context "#conditions-kms-encryption-context")
- [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys")
- [kms:ExpirationModel](#conditions-kms-expiration-model "#conditions-kms-expiration-model")
- [kms:GrantConstraintType](#conditions-kms-grant-constraint-type "#conditions-kms-grant-constraint-type")
- [kms:GrantIsForAWSResource](#conditions-kms-grant-is-for-aws-resource "#conditions-kms-grant-is-for-aws-resource")
- [kms:GrantOperations](#conditions-kms-grant-operations "#conditions-kms-grant-operations")
- [kms:GranteePrincipal](#conditions-kms-grantee-principal "#conditions-kms-grantee-principal")
- [kms:KeyAgreementAlgorithm](#conditions-kms-key-agreement-algorithm "#conditions-kms-key-agreement-algorithm")
- [kms:KeyOrigin](#conditions-kms-key-origin "#conditions-kms-key-origin")
- [kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec")
- [kms:KeyUsage](#conditions-kms-key-usage "#conditions-kms-key-usage")
- [kms:MacAlgorithm](#conditions-kms-mac-algorithm "#conditions-kms-mac-algorithm")
- [kms:MessageType](#conditions-kms-message-type "#conditions-kms-message-type")
- [kms:MultiRegion](#conditions-kms-multiregion "#conditions-kms-multiregion")
- [kms:MultiRegionKeyType](#conditions-kms-multiregion-key-type "#conditions-kms-multiregion-key-type")
- [kms:PrimaryRegion](#conditions-kms-primary-region "#conditions-kms-primary-region")
- [kms:ReEncryptOnSameKey](#conditions-kms-reencrypt-on-same-key "#conditions-kms-reencrypt-on-same-key")
- [kms:RequestAlias](#conditions-kms-request-alias "#conditions-kms-request-alias")
- [kms:ResourceAliases](#conditions-kms-resource-aliases "#conditions-kms-resource-aliases")
- [kms:ReplicaRegion](#conditions-kms-replica-region "#conditions-kms-replica-region")
- [kms:RetiringPrincipal](#conditions-kms-retiring-principal "#conditions-kms-retiring-principal")
- [kms:RotationPeriodInDays](#conditions-kms-rotation-period-in-days "#conditions-kms-rotation-period-in-days")
- [kms:ScheduleKeyDeletionPendingWindowInDays](#conditions-kms-schedule-key-deletion-pending-window-in-days "#conditions-kms-schedule-key-deletion-pending-window-in-days")
- [kms:SigningAlgorithm](#conditions-kms-signing-algorithm "#conditions-kms-signing-algorithm")
- [kms:ValidTo](#conditions-kms-valid-to "#conditions-kms-valid-to")
- [kms:ViaService](#conditions-kms-via-service "#conditions-kms-via-service")
- [kms:WrappingAlgorithm](#conditions-kms-wrapping-algorithm "#conditions-kms-wrapping-algorithm")
- [kms:WrappingKeySpec](#conditions-kms-wrapping-key-spec "#conditions-kms-wrapping-key-spec")

## kms:BypassPolicyLockoutSafetyCheck

| AWS KMS condition keys               | Condition type | Value type    | API operations                | Policy type                                        |
| ------------------------------------ | -------------- | ------------- | ----------------------------- | -------------------------------------------------- |
| `kms:BypassPolicyLockoutSafetyCheck` | Boolean        | Single-valued | `CreateKey`<br>`PutKeyPolicy` | IAM policies only<br>Key policies and IAM policies |

The `kms:BypassPolicyLockoutSafetyCheck` condition key controls access to the
[CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") and [PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md") operations based on the
value of the `BypassPolicyLockoutSafetyCheck` parameter in the request.

The following example IAM policy statement prevents users from bypassing the policy
lockout safety check by denying them permission to create KMS keys when the value of the
`BypassPolicyLockoutSafetyCheck` parameter in the `CreateKey`
request is `true.`

```
{
  "Effect": "Deny",
  "Action": [
    "kms:CreateKey",
    "kms:PutKeyPolicy"
  ],
  "Resource": "*",
  "Condition": {
    "Bool": {
      **"kms:BypassPolicyLockoutSafetyCheck": true**
    }
  }
}
```

You can also use the `kms:BypassPolicyLockoutSafetyCheck` condition key in an
IAM policy or key policy to control access to the `PutKeyPolicy` operation. The
following example policy statement from a key policy prevents users from bypassing the
policy lockout safety check when changing the policy of a KMS key.

Instead of using an explicit `Deny`, this policy statement uses
`Allow` with the [Null condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null") to allow access only when the request
does not include the `BypassPolicyLockoutSafetyCheck` parameter. When the
parameter is not used, the default value is `false`. This slightly weaker policy
statement can be overridden in the rare case that a bypass is necessary.

```
{
  "Effect": "Allow",
  "Action": "kms:PutKeyPolicy",
  "Resource": "*",
  "Condition": {
    "Null": {
      **"kms:BypassPolicyLockoutSafetyCheck": true**
    }
  }
}
```

**See also**

- [kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec")
- [kms:KeyOrigin](#conditions-kms-key-origin "#conditions-kms-key-origin")
- [kms:KeyUsage](#conditions-kms-key-usage "#conditions-kms-key-usage")

## kms:CallerAccount

| AWS KMS condition keys | Condition type | Value type    | API operations                                             | Policy type                   |
| ---------------------- | -------------- | ------------- | ---------------------------------------------------------- | ----------------------------- |
| `kms:CallerAccount`    | String         | Single-valued | KMS key resource operations<br>Custom key store operations | Key policies and IAM policies |

You can use this condition key to allow or deny access to all identities (users and
roles) in an AWS account. In key policies, you use the `Principal` element to
specify the identities to which the policy statement applies. The syntax for the
`Principal` element does not provide a way to specify all identities in an
AWS account. But you can achieve this effect by combining this condition key with a
`Principal` element that specifies all AWS identities.

You can use it to control access to any _KMS key resource
operation_, that is, any AWS KMS operation that uses a particular KMS key.
To identify the KMS key resource operations, in the [Actions
and Resources Table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look for a value of `KMS key` in the `Resources` column for the operation. It is also valid for operations that manage [custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview").

For example, the following key policy statement demonstrates how to use the
`kms:CallerAccount` condition key. This policy statement is in the key policy
for the AWS managed key for Amazon EBS. It combines a `Principal` element that
specifies all AWS identities with the `kms:CallerAccount` condition key to
effectively allow access to all identities in AWS account 111122223333. It
contains an additional AWS KMS condition key (`kms:ViaService`) to further limit
the permissions by only allowing requests that come through Amazon EBS. For more information, see
[kms:ViaService](#conditions-kms-via-service "#conditions-kms-via-service").

```
{
  "Sid": "Allow access through EBS for all principals in the account that are authorized to use EBS",
  "Effect": "Allow",
  "Principal": {"AWS": "*"},
  "Condition": {
    "StringEquals": {
      **"kms:CallerAccount": "111122223333"**,
      "kms:ViaService": "ec2.us-west-2.amazonaws.com"
    }
  },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:CreateGrant",
    "kms:DescribeKey"
  ],
  "Resource": "*"
}
```

## kms:CustomerMasterKeySpec

(deprecated)

The `kms:CustomerMasterKeySpec` condition key is deprecated. Instead, use the
[kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec") condition key.

The `kms:CustomerMasterKeySpec` and `kms:KeySpec` condition keys
work the same way. Only the names differ. We recommend that you use
`kms:KeySpec`. However, to avoid breaking changes, AWS KMS supports both condition
keys.

## kms:CustomerMasterKeyUsage

(deprecated)

The `kms:CustomerMasterKeyUsage` condition key is deprecated. Instead, use
the [kms:KeyUsage](#conditions-kms-key-usage "#conditions-kms-key-usage") condition key.

The `kms:CustomerMasterKeyUsage` and `kms:KeyUsage` condition keys
work the same way. Only the names differ. We recommend that you use
`kms:KeyUsage`. However, to avoid breaking changes, AWS KMS supports both
condition keys.

## kms:DataKeyPairSpec

| AWS KMS condition keys | Condition type | Value type    | API operations                                                 | Policy type                   |
| ---------------------- | -------------- | ------------- | -------------------------------------------------------------- | ----------------------------- |
| `kms:DataKeyPairSpec`  | String         | Single-valued | `GenerateDataKeyPair`<br>`GenerateDataKeyPairWithoutPlaintext` | Key policies and IAM policies |

You can use this condition key to control access to the [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md") and [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md") operations based on the value of the
`KeyPairSpec` parameter in the request. For example, you can allow users to
generate only particular types of data key pairs.

The following example key policy statement uses the `kms:DataKeyPairSpec`
condition key to allow users to use the KMS key to generate only RSA data key
pairs.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": [
    "kms:GenerateDataKeyPair",
    "kms:GenerateDataKeyPairWithoutPlaintext"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      **"kms:DataKeyPairSpec": "RSA\*"**
    }
  }
}
```

**See also**

- [kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec")
- [kms:EncryptionAlgorithm](#conditions-kms-encryption-algorithm "#conditions-kms-encryption-algorithm")
- [kms:EncryptionContext:context-key](#conditions-kms-encryption-context "#conditions-kms-encryption-context")
- [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys")

## kms:EncryptionAlgorithm

| AWS KMS condition keys    | Condition type | Value type    | API operations                                                                                                                                                    | Policy type                   |
| ------------------------- | -------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `kms:EncryptionAlgorithm` | String         | Single-valued | `Decrypt`<br>`Encrypt`<br>`GenerateDataKey`<br>`GenerateDataKeyPair`<br>`GenerateDataKeyPairWithoutPlaintext`<br>`GenerateDataKeyWithoutPlaintext`<br>`ReEncrypt` | Key policies and IAM policies |

You can use the `kms:EncryptionAlgorithm` condition key to control access to
cryptographic operations based on the encryption algorithm that is used in the operation.
For the [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md"), [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"), and [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md") operations, it controls access
based on the value of the [EncryptionAlgorithm](../APIReference/API_Decrypt.md#KMS-Decrypt-request-EncryptionAlgorithm "../APIReference/API_Decrypt.md#KMS-Decrypt-request-EncryptionAlgorithm") parameter in the request. For operations that generate data
keys and data key pairs, it controls access based on the encryption algorithm that is used
to encrypt the data key.

This condition key has no effect on operations performed outside of AWS KMS, such as
encrypting with the public key in an asymmetric KMS key pair outside of AWS KMS.

**EncryptionAlgorithm parameter in a request**

To allow users to use only a particular encryption algorithm with a KMS key, use a
policy statement with a `Deny` effect and a `StringNotEquals`
condition operator. For example, the following example key policy statement prohibits
principals who can assume the `ExampleRole` role from using this KMS key in the
specified cryptographic operations unless the encryption algorithm in the request is
`RSAES_OAEP_SHA_256`, an asymmetric encryption algorithm used with RSA
KMS keys.

Unlike a policy statement that allows a user to use a particular encryption algorithm, a
policy statement with a double-negative like this one prevents other policies and grants for
this KMS key from allowing this role to use other encryption algorithms. The
`Deny` in this key policy statement takes precedence over any key policy or
IAM policy with an `Allow` effect, and it takes precedence over all grants for
this KMS key and its principals.

```
{
  "Sid": "Allow only one encryption algorithm with this asymmetric KMS key",
  "Effect": "Deny",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*"
  ],
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "kms:EncryptionAlgorithm": "RSAES_OAEP_SHA_256"
    }
  }
}
```

**Encryption algorithm used for the operation**

You can also use the `kms:EncryptionAlgorithm` condition key to control
access to operations based on the encryption algorithm used in the operation, even when the
algorithm isn't specified in the request. This allows you to require or forbid the
`SYMMETRIC_DEFAULT` algorithm, which might not be specified in a request
because it's the default value.

This feature lets you use the `kms:EncryptionAlgorithm` condition key to
control access to the operations that generate data keys and data key pairs. These
operations use only symmetric encryption KMS keys and the `SYMMETRIC_DEFAULT`
algorithm.

For example, this IAM policy limits its principals to symmetric encryption. It denies
access to any KMS key in the example account for cryptographic operations unless the
encryption algorithm specified in the request or used in the operation is SYMMETRIC_DEFAULT.
Including `GenerateDataKey*` adds [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md"), [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md"), [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md"), and [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md") to the permissions. The condition has no
effect on these operations because they always use a symmetric encryption algorithm.

```
{
  "Sid": "AllowOnlySymmetricAlgorithm",
  "Effect": "Deny",
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*"
  ],
  "Resource": "arn:aws:kms:us-west-2:111122223333:key/*",
  "Condition": {
    "StringNotEquals": {
      "kms:EncryptionAlgorithm": "SYMMETRIC_DEFAULT"
    }
  }
}
```

**See also**

- [kms:MacAlgorithm](#conditions-kms-mac-algorithm "#conditions-kms-mac-algorithm")
- [kms:SigningAlgorithm](#conditions-kms-signing-algorithm "#conditions-kms-signing-algorithm")

## kms:EncryptionContext:_context-key_

| AWS KMS condition keys                | Condition type | Value type    | API operations                                                                                                                                                                                      | Policy type                   |
| ------------------------------------- | -------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `kms:EncryptionContext:*context-key*` | String         | Single-valued | `CreateGrant`<br>`Encrypt`<br>`Decrypt`<br>`GenerateDataKey`<br>`GenerateDataKeyPair`<br>`GenerateDataKeyPairWithoutPlaintext`<br>`GenerateDataKeyWithoutPlaintext`<br>`ReEncrypt`<br>`RetireGrant` | Key policies and IAM policies |

You can use the `kms:EncryptionContext:*context-key*` condition key to control access to a
[symmetric encryption KMS key](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks") based on the [encryption context](encrypt_context.md "encrypt_context.md") in a request for a [cryptographic operation](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"). Use this condition key
to evaluate both the key and the value in the encryption context pair. To evaluate only the
encryption context keys or require an encryption context regardless of keys or values, use
the [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys")
condition key.

###### Note

Condition key values must conform to the character rules for key policies and IAM
policies. Some characters that are valid in an encryption context are not valid in
policies. You might not be able to use this condition key to express all valid encryption
context values. For details about key policy document rules, see [Key policy format](key-policy-overview.md#key-policy-format "key-policy-overview.md#key-policy-format"). For details about IAM
policy document rules, see [IAM name
requirements](../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names "../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names") in the _IAM User Guide_.

You cannot specify an encryption context in a cryptographic operation with an [asymmetric KMS key](symmetric-asymmetric.md "symmetric-asymmetric.md") or an [HMAC KMS key](hmac.md "hmac.md"). Asymmetric algorithms and MAC algorithms do not support an encryption context.

To use the kms:EncryptionContext:_context-key_ condition key, replace the
`context-key` placeholder with the encryption context key.
Replace the `context-value` placeholder with the encryption context
value.

```
`"kms:EncryptionContext:`context-key`": "`context-value`"`
```

For example, the following condition key specifies an encryption context in which the
key is `AppName` and the value is `ExampleApp` (`AppName =
 ExampleApp`).

```
`"kms:EncryptionContext:AppName": "ExampleApp"`
```

This is a [single-valued condition key](#set-operators "#set-operators"). The key in
the condition key specifies a particular encryption context key (_context-key_). Although you can include multiple encryption context pairs in
each API request, the encryption context pair with the specified _context-key_ can have only one value. For example, the
`kms:EncryptionContext:Department` condition key applies only to encryption
context pairs with a `Department` key, and any given encryption context pair with
the `Department` key can have only one value.

Do not use a set operator with the `kms:EncryptionContext:*context-key*` condition key. If
you create a policy statement with an `Allow` action, the
`kms:EncryptionContext:*context-key*` condition key, and the `ForAllValues` set
operator, the condition allows requests with no encryption context and requests with
encryption context pairs that are not specified in the policy condition.

###### Warning

Do not use a `ForAnyValue` or `ForAllValues` set operator with
this single-valued condition key. These set operators can create a policy condition that
does not require values you intend to require and allows values you intend to
forbid.

If you create or update a policy that includes a `ForAllValues` set
operator with the kms:EncryptionContext:_context-key_, AWS KMS returns the following error message:

`OverlyPermissiveCondition:EncryptionContext: Using the `ForAllValues`
 set operator with a single-valued condition key matches requests without the specified
 encryption context or with an unspecified encryption context. To fix, remove
 ForAllValues.`

To require a particular encryption context pair, use the
`kms:EncryptionContext:*context-key*` condition key with the `StringEquals` operator
.

The following example key policy statement allows principals who can assume the role to
use the KMS key in a `GenerateDataKey` request only when the encryption context
in the request includes the `AppName:ExampleApp` pair. Other encryption context
pairs are permitted.

The key name is not case sensitive. The case sensitivity of the value is determined by
the condition operator, such as `StringEquals`. For details, see [Case sensitivity of the
encryption context condition](#conditions-kms-encryption-context-case "#conditions-kms-encryption-context-case").

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:EncryptionContext:AppName": "ExampleApp"**
    }
  }
}
```

To require an encryption context pair and forbid all other encryption context pairs, use
both kms:EncryptionContext:_context-key_ and [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys") in the policy statement. The following
key policy statement uses the `kms:EncryptionContext:AppName` condition to
require the `AppName=ExampleApp` encryption context pair in the request. It also
uses a `kms:EncryptionContextKeys` condition key with the
`ForAllValues` set operator to allow only the `AppName` encryption
context key.

The `ForAllValues` set operator limits encryption context keys in the request
to `AppName`. If the `kms:EncryptionContextKeys` condition with the
`ForAllValues` set operator was used alone in a policy statement, this set
operator would allow requests with no encryption context. However, if the request had no
encryption context, the `kms:EncryptionContext:AppName` condition would fail. For
details about the `ForAllValues` set operator, see [Using multiple keys and values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions") in the _IAM User Guide_.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/KeyUsers"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:EncryptionContext:AppName": "ExampleApp"**
    },
    "ForAllValues:StringEquals": {
      "kms:EncryptionContextKeys": [
        "AppName"
      ]
    }
  }
}
```

You can also use this condition key to deny access to a KMS key for a particular
operation. The following example key policy statement uses a `Deny` effect to
forbid the principal from using the KMS key if the encryption context in the request
includes a `Stage=Restricted` encryption context pair. This condition allows a
request with other encryption context pairs, including encryption context pairs with the
`Stage` key and other values, such as `Stage=Test`.

```
{
  "Effect": "Deny",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:Stage": "Restricted"
    }
  }
}
```

### Using multiple encryption context

pairs

You can require or forbid multiple encryption context pairs. You can also require one
of several encryption context pairs. For details about the logic used to interpret these
conditions, see [Creating a condition with multiple keys or values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md") in the IAM User Guide.

###### Note

Earlier versions of this topic displayed policy statements that used the
`ForAnyValue` and `ForAllValues` set operators with the
kms:EncryptionContext:_context-key_ condition key. Using a set operator with a [single-valued condition key](#set-operators "#set-operators") can result in policies that
allow requests with no encryption context and unspecified encryption context pairs.

For example, a policy condition with the `Allow` effect, the
`ForAllValues` set operator, and the
`"kms:EncryptionContext:Department": "IT"` condition key does not limit the
encryption context to the "Department=IT" pair. It allows requests with no encryption
context and requests with unspecified encryption context pairs, such as
`Stage=Restricted`.

Please review your policies and eliminate the set operator from any condition with
kms:EncryptionContext:_context-key_. Attempts to create or update a policy with this format fail with an
`OverlyPermissiveCondition` exception. To resolve the error, delete the set
operator.

To require multiple encryption context pairs, list the pairs in the same condition.
The following example key policy statement requires two encryption context pairs,
`Department=IT` and `Project=Alpha`. Because the conditions have
different keys (`kms:EncryptionContext:Department` and
`kms:EncryptionContext:Project`), they are implicitly connected by an AND
operator. Other encryption context pairs are permitted, but not required.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:EncryptionContext:Department": "IT"**,
      **"kms:EncryptionContext:Project": "Alpha"**
    }
  }
}
```

To require one encryption context pair OR another pair, place each condition key in a
separate policy statement. The following example key policy requires
`Department=IT`
_or_
`Project=Alpha` pairs, or both. Other encryption context pairs are permitted,
but not required.

```
{
 "Effect": "Allow",
 "Principal": {
  "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
 },
 "Action": "kms:GenerateDataKey",
 "Resource": "*",
 "Condition": {
  "StringEquals": {
   **"kms:EncryptionContext:Department": "IT"**
  }
 }
},
{
 "Effect": "Allow",
 "Principal": {
  "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
 },
 "Action": "kms:GenerateDataKey",
 "Resource": "*",
 "Condition": {
  "StringEquals": {
   **"kms:EncryptionContext:Project": "Alpha"**
  }
 }
}
```

To require particular encryption pairs and exclude all other encryption context pairs,
use both kms:EncryptionContext:_context-key_ and [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys") in the policy statement. The following
key policy statement uses the kms:EncryptionContext:_context-key_ condition to require an encryption
context with both `Department=IT`
_and_
`Project=Alpha` pairs. It uses a `kms:EncryptionContextKeys`
condition key with the `ForAllValues` set operator to allow only the
`Department` and `Project` encryption context keys.

The `ForAllValues` set operator limits encryption context keys in the
request to `Department` and `Project`. If it were used alone in a
condition, this set operator would allow requests with no encryption context, but in this
configuration, the kms:EncryptionContext:_context-key_ in this condition would fail.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:Department": "IT",
      "kms:EncryptionContext:Project": "Alpha"
    },
    "ForAllValues:StringEquals": {
      "kms:EncryptionContextKeys": [
        "Department",
        "Project"
      ]
    }
  }
}
```

You can also forbid multiple encryption context pairs. The following example key
policy statement uses a `Deny` effect to forbid the principal from using the
KMS keys if the encryption context in the request includes a
`Stage=Restricted` or `Stage=Production`.pair.

Multiple values (`Restricted` and `Production`) for the same key
(`kms:EncryptionContext:Stage`) are implicitly connected by a OR. For
details, see [Evaluation logic for conditions with multiple keys or values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multiple-conditions-eval "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multiple-conditions-eval") in the _IAM User Guide_.

```
{
  "Effect": "Deny",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:Stage": [
         "Restricted",
         "Production"
      ]
    }
  }
}
```

### Case sensitivity of the

encryption context condition

The encryption context that is specified in a decryption operation must be an exact,
case-sensitive match for the encryption context that is specified in the encryption
operation. Only the order of pairs in an encryption context with multiple pair can
vary.

However, in policy conditions, the condition key is not case sensitive. The case
sensitivity of the condition value is determined by the [policy condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") that you use, such as `StringEquals` or
`StringEqualsIgnoreCase`.

As such, the condition key, which consists of the `kms:EncryptionContext:`
prefix and the `context-key` replacement, is not
case sensitive. A policy that uses this condition does not check the case of either
element of the condition key. The case sensitivity of the value, that is, the
`context-value` replacement, is determined by
the policy condition operator.

For example, the following policy statement allows the operation when the encryption
context includes an `Appname` key, regardless of its capitalization. The
`StringEquals` condition requires that `ExampleApp` be capitalized
as it is specified.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:EncryptionContext:Appname": "ExampleApp"**
    }
  }
}
```

To require a case-sensitive encryption context key, use the [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys") policy
condition with a case-sensitive condition operator, such as `StringEquals`. In
this policy condition, because the encryption context key is the value in this policy
condition, its case sensitivity is determined by the condition operator.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "ForAnyValue:StringEquals": {
      **"kms:EncryptionContextKeys": "AppName"**
    }
  }
}
```

To require a case-sensitive evaluation of both the encryption context key and value,
use the `kms:EncryptionContextKeys` and kms:EncryptionContext:_context-key_ policy conditions
together in the same policy statement. The case-sensitive condition operator (such as
`StringEquals`) always applies to the value of the condition. The encryption
context key (such as `AppName`) is the value of the
`kms:EncryptionContextKeys` condition. The encryption context value (such as
`ExampleApp`) is the value of the kms:EncryptionContext:_context-key_ condition.

For example, in the following example key policy statement, because the
`StringEquals` operator is case sensitive, both the encryption context key
and the encryption context value are case sensitive.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "ForAnyValue:StringEquals": {
      "kms:EncryptionContextKeys": "AppName"
    },
    "StringEquals": {
      "kms:EncryptionContext:AppName": "ExampleApp"
    }
  }
}
```

### Using variables in an

encryption context condition

The key and value in an encryption context pair must be simple literal strings. They
cannot be integers or objects, or any type that is not fully resolved. If you use a
different type, such as an integer or float, AWS KMS interprets it as a literal
string.

```
"encryptionContext": {
    "department": "10103.0"
}
```

However, the value of the `kms:EncryptionContext:*context-key*` condition key can be an
[IAM policy
variable](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md"). These policy variables are resolved at runtime based on values in the
request. For example, `aws:CurrentTime` resolves to the time of the request and
`aws:username` resolves to the friendly name of the caller.

You can use these policy variables to create a policy statement with a condition that
requires very specific information in an encryption context, such as the caller's user
name. Because it contains a variable, you can use the same policy statement for all users
who can assume the role. You don't have to write a separate policy statement for each
user.

Consider a situation where you want to all users who can assume a role to use the same
KMS key to encrypt and decrypt their data. However, you want to allow them to decrypt
only the data that they encrypted. Start by requiring that every request to AWS KMS include
an encryption context where the key is `user` and the value is the caller's
AWS user name, such as the following one.

```
"encryptionContext": {
    "user": "bob"
}
```

Then, to enforce this requirement, you can use a policy statement like the one in the
following example. This policy statement gives the `TestTeam` role permission
to encrypt and decrypt data with the KMS key. However, the permission is valid only when
the encryption context in the request includes a `"user":
 "`<username>`"` pair. To represent the user name,
the condition uses the [`aws:username`](../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse "../../../IAM/latest/UserGuide/reference_policies_variables.md#policy-vars-infotouse") policy variable.

When the request is evaluated, the caller's user name replaces the variable in the
condition. As such, the condition requires an encryption context of `"user":
 "bob"` for "bob" and `"user": "alice"` for "alice."

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/TestTeam"
  },
  "Action": [
    "kms:Decrypt",
    "kms:Encrypt"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:user": "${aws:username}"
    }
  }
}
```

You can use an IAM policy variable only in the value of the
`kms:EncryptionContext:*context-key*` condition key. You cannot use a variable in the
key.

You can also use [provider-specific context keys](../../../IAM/latest/UserGuide/id_roles_providers_oidc_user-id.md "../../../IAM/latest/UserGuide/id_roles_providers_oidc_user-id.md") in variables. These context keys uniquely
identify users who logged into AWS by using web identity federation.

Like all variables, these variables can be used only in the
`kms:EncryptionContext:*context-key*` policy condition, not in the actual encryption context.
And they can be used only in the value of the condition, not in the key.

For example, the following key policy statement is similar to the previous one.
However, the condition requires an encryption context where the key is `sub`
and the value uniquely identifies a user logged into an Amazon Cognito user pool. For details
about identifying users and roles in Amazon Cognito, see [IAM Roles](../../../cognito/latest/developerguide/iam-roles.md "../../../cognito/latest/developerguide/iam-roles.md") in the [Amazon Cognito Developer Guide](../../../cognito/latest/developerguide.md "../../../cognito/latest/developerguide.md").

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/TestTeam"
  },
  "Action": [
    "kms:Decrypt",
    "kms:Encrypt"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
       "kms:EncryptionContext:sub": **"${cognito-identity.amazonaws.com:sub}"**
    }
  }
}
```

**See also**

- [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys")
- [kms:GrantConstraintType](#conditions-kms-grant-constraint-type "#conditions-kms-grant-constraint-type")

## kms:EncryptionContextKeys

| AWS KMS condition keys      | Condition type | Value type   | API operations                                                                                                                                                                                      | Policy type                   |
| --------------------------- | -------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `kms:EncryptionContextKeys` | String (list)  | Multi-valued | `CreateGrant`<br>`Decrypt`<br>`Encrypt`<br>`GenerateDataKey`<br>`GenerateDataKeyPair`<br>`GenerateDataKeyPairWithoutPlaintext`<br>`GenerateDataKeyWithoutPlaintext`<br>`ReEncrypt`<br>`RetireGrant` | Key policies and IAM policies |

You can use the `kms:EncryptionContextKeys` condition key to control access
to a [symmetric encryption KMS key](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks") based on the [encryption context](encrypt_context.md "encrypt_context.md") in a request for a cryptographic
operation. Use this condition key to evaluate only the key in each encryption context pair.
To evaluate both the key and the value in the encryption context, use the
`kms:EncryptionContext:*context-key*` condition key.

You cannot specify an encryption context in a cryptographic operation with an [asymmetric KMS key](symmetric-asymmetric.md "symmetric-asymmetric.md") or an [HMAC KMS key](hmac.md "hmac.md"). Asymmetric algorithms and MAC algorithms do not support an encryption context.

###### Note

Condition key values, including an encryption context key, must conform to the
character and encoding rules for AWS KMS key policies. You might not be able to use this
condition key to express all valid encryption context keys. For details about key policy document rules, see [Key policy format](key-policy-overview.md#key-policy-format "key-policy-overview.md#key-policy-format"). For details about IAM
policy document rules, see [IAM name
requirements](../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names "../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names") in the _IAM User Guide_.

This is a [multi-valued condition key](#set-operators "#set-operators"). You can
specify multiple encryption context pairs in each API request.
`kms:EncryptionContextKeys` compares the encryption context keys in the request
to the set of encryption context keys in the policy. To determine how these sets are
compared, you must provide a `ForAnyValue` or `ForAllValues` set
operator in the policy condition. For details about the set operators, see [Using multiple keys and values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions") in the IAM User Guide.

- `ForAnyValue`: At least one encryption context key in the request must
  match an encryption context key in the policy condition. Other encryption context keys
  are permitted. If the request has no encryption context, the condition is not
  satisfied.
- `ForAllValues`: Every encryption context key in the request must match an
  encryption context key in the policy condition. This set operator limits the encryption
  context keys to those in the policy condition. It doesn't require any encryption context
  keys, but it forbids unspecified encryption context keys.

The following example key policy statement uses the
`kms:EncryptionContextKeys` condition key with the `ForAnyValue` set
operator. This policy statement allows use of a KMS key for the specified operations, but
only when at least one of the encryption context pairs in the request includes the
`AppName` key, regardless of its value.

For example, this key policy statement allows a `GenerateDataKey` request
with two encryption context pairs, `AppName=Helper` and
`Project=Alpha`, because the first encryption context pair satisfies the
condition. A request with only `Project=Alpha` or with no encryption context
would fail.

Because the [StringEquals](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") condition operation is case sensitive, this policy statement
requires the spelling and case of the encryption context key. But you can use a condition
operator that ignores the case of the key, such as
`StringEqualsIgnoreCase`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": [
    "kms:Encrypt",
    "kms:GenerateDataKey*"
  ],
  "Resource": "*",
  "Condition": {
    "ForAnyValue:StringEquals": {
      **"kms:EncryptionContextKeys": "AppName"**
    }
  }
}
```

You can also use the `kms:EncryptionContextKeys` condition key to require an
encryption context (any encryption context) in cryptographic operations that use the
KMS key;.

The following example key policy statement uses the
`kms:EncryptionContextKeys` condition key with the [Null condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null") to
allow access to a KMS key only when encryption context in the API request is not null.
This condition does not check the keys or values of the encryption context. It only verifies
that the encryption context exists.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": [
    "kms:Encrypt",
    "kms:GenerateDataKey*"
  ],
  "Resource": "*",
  "Condition": {
    "Null": {
      "kms:EncryptionContextKeys": false
    }
  }
}
```

**See also**

- [kms:EncryptionContext:context-key](#conditions-kms-encryption-context "#conditions-kms-encryption-context")
- [kms:GrantConstraintType](#conditions-kms-grant-constraint-type "#conditions-kms-grant-constraint-type")

## kms:ExpirationModel

| AWS KMS condition keys | Condition type | Value type    | API operations      | Policy type                   |
| ---------------------- | -------------- | ------------- | ------------------- | ----------------------------- |
| `kms:ExpirationModel`  | String         | Single-valued | `ImportKeyMaterial` | Key policies and IAM policies |

The `kms:ExpirationModel` condition key controls access to the [ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") operation based on
the value of the [ExpirationModel](../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ExpirationModel "../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ExpirationModel") parameter in the request.

`ExpirationModel` is an optional parameter that determines whether the
imported key material expires. Valid values are `KEY_MATERIAL_EXPIRES` and
`KEY_MATERIAL_DOES_NOT_EXPIRE`. `KEY_MATERIAL_EXPIRES` is the
default value.

The expiration date and time is determined by the value of the [ValidTo](../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ValidTo "../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ValidTo") parameter. The `ValidTo` parameter is required unless the
value of the `ExpirationModel` parameter is
`KEY_MATERIAL_DOES_NOT_EXPIRE`. You can also use the [kms:ValidTo](#conditions-kms-valid-to "#conditions-kms-valid-to") condition key to require a particular
expiration date as a condition for access.

The following example policy statement uses the `kms:ExpirationModel`
condition key to allow users to import key material into a KMS key only when the request
includes the `ExpirationModel` parameter and its value is
`KEY_MATERIAL_DOES_NOT_EXPIRE`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:ImportKeyMaterial",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:ExpirationModel": "KEY\_MATERIAL\_DOES\_NOT\_EXPIRE"**
    }
  }
}
```

You can also use the `kms:ExpirationModel` condition key to allow users to
import key material only when the key material expires. The following example key policy
statement uses the `kms:ExpirationModel` condition key with the
[Null condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Null") to allow users to import key material only when the request does not
have an `ExpirationModel` parameter. The default value for ExpirationModel is
`KEY_MATERIAL_EXPIRES`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:ImportKeyMaterial",
  "Resource": "*",
  "Condition": {
    **"Null"**: {
      **"kms:ExpirationModel": true**
    }
  }
}
```

**See also**

- [kms:ValidTo](#conditions-kms-valid-to "#conditions-kms-valid-to")
- [kms:WrappingAlgorithm](#conditions-kms-wrapping-algorithm "#conditions-kms-wrapping-algorithm")
- [kms:WrappingKeySpec](#conditions-kms-wrapping-key-spec "#conditions-kms-wrapping-key-spec")

## kms:GrantConstraintType

| AWS KMS condition keys    | Condition type | Value type    | API operations                 | Policy type                   |
| ------------------------- | -------------- | ------------- | ------------------------------ | ----------------------------- |
| `kms:GrantConstraintType` | String         | Single-valued | `CreateGrant`<br>`RetireGrant` | Key policies and IAM policies |

You can use this condition key to control access to the [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") operation based on the type of
[grant constraint](create-grant-overview.md#grant-constraints "create-grant-overview.md#grant-constraints") in the request.

When you create a grant, you can optionally specify a grant constraint to allow the
operations that the grant permit only when a particular [encryption context](encrypt_context.md "encrypt_context.md") is present. The grant constraint can be one of two types:
`EncryptionContextEquals` or `EncryptionContextSubset`. You can use
this condition key to check that the request contains one type or the other.

###### Important

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

The following example key policy statement uses the `kms:GrantConstraintType`
condition key to allow users to create grants only when the request includes an
`EncryptionContextEquals` grant constraint. The example shows a policy
statement in a key policy.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/RoleForExampleApp"
  },
  "Action": "kms:CreateGrant",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:GrantConstraintType": "EncryptionContextEquals"**
    }
  }
}
```

**See also**

- [kms:EncryptionContext:context-key](#conditions-kms-encryption-context "#conditions-kms-encryption-context")
- [kms:EncryptionContextKeys](#conditions-kms-encryption-context-keys "#conditions-kms-encryption-context-keys")
- [kms:GrantIsForAWSResource](#conditions-kms-grant-is-for-aws-resource "#conditions-kms-grant-is-for-aws-resource")
- [kms:GrantOperations](#conditions-kms-grant-operations "#conditions-kms-grant-operations")
- [kms:GranteePrincipal](#conditions-kms-grantee-principal "#conditions-kms-grantee-principal")
- [kms:RetiringPrincipal](#conditions-kms-retiring-principal "#conditions-kms-retiring-principal")

## kms:GrantIsForAWSResource

| AWS KMS condition keys      | Condition type | Value type    | API operations                                 | Policy type                   |
| --------------------------- | -------------- | ------------- | ---------------------------------------------- | ----------------------------- |
| `kms:GrantIsForAWSResource` | Boolean        | Single-valued | `CreateGrant`<br>`ListGrants`<br>`RevokeGrant` | Key policies and IAM policies |

Allows or denies permission for the [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md"), [ListGrants](../APIReference/API_ListGrants.md "../APIReference/API_ListGrants.md"), or
[RevokeGrant](../APIReference/API_RevokeGrant.md "../APIReference/API_RevokeGrant.md") operations only when an
[AWS service integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration")
calls the operation on the user's behalf. This policy condition doesn't allow the user to
call these grant operations directly.

The following example key policy statement uses the
`kms:GrantIsForAWSResource` condition key. It allows AWS services that are
integrated with AWS KMS, such as Amazon EBS, to create grants on this KMS key on behalf of the
specified principal.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:CreateGrant",
  "Resource": "*",
  "Condition": {
    "Bool": {
      **"kms:GrantIsForAWSResource": true**
    }
  }
}
```

**See also**

- [kms:GrantConstraintType](#conditions-kms-grant-constraint-type "#conditions-kms-grant-constraint-type")
- [kms:GrantOperations](#conditions-kms-grant-operations "#conditions-kms-grant-operations")
- [kms:GranteePrincipal](#conditions-kms-grantee-principal "#conditions-kms-grantee-principal")
- [kms:RetiringPrincipal](#conditions-kms-retiring-principal "#conditions-kms-retiring-principal")

## kms:GrantOperations

| AWS KMS condition keys | Condition type | Value type   | API operations | Policy type                   |
| ---------------------- | -------------- | ------------ | -------------- | ----------------------------- |
| `kms:GrantOperations`  | String         | Multi-valued | `CreateGrant`  | Key policies and IAM policies |

You can use this condition key to control access to the [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") operation based on the [grant operations](grants.md#terms-grant-operations "grants.md#terms-grant-operations") in the request. For example, you
can allow users to create grants that delegate permission to encrypt but not decrypt. For
more information about grants, see [Using grants](grants.md "grants.md").

This is a [multi-valued condition key](#set-operators "#set-operators").
`kms:GrantOperations` compares the set of grant operations in the
`CreateGrant` request to the set of grant operations in the policy. To
determine how these sets are compared, you must provide a `ForAnyValue` or
`ForAllValues` set operator in the policy condition. For details about the set
operators, see [Using multiple keys and values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions") in the IAM User Guide.

- `ForAnyValue`: At least one grant operation in the request must match one
  of the grant operations in the policy condition. Other grant operations are
  permitted.
- ForAllValues: Every grant operation in the request must match a grant operation in
  the policy condition. This set operator limits the grant operations to those specified
  in the policy condition. It doesn't require any grant operations, but it forbids
  unspecified grant operations.

ForAllValues also returns true when there are no grant operations in the request,
but `CreateGrant` doesn't permit it. If the `Operations` parameter
is missing or has a null value, the `CreateGrant` request fails.

The following example key policy statement uses the `kms:GrantOperations`
condition key to to create grants only when the grant operations are `Encrypt`,
`ReEncryptTo`, or both. If the grant includes any other operations, the
`CreateGrant` request fails.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:CreateGrant",
  "Resource": "*",
  "Condition": {
    "ForAllValues:StringEquals": {
      **"kms:GrantOperations"**: [
        **"Encrypt"**,
        **"ReEncryptTo"**
      ]
    }
  }
}
```

If you change the set operator in the policy condition to `ForAnyValue`, the
policy statement would require that at least one of the grant operations in the grant is
`Encrypt` or `ReEncryptTo`, but it would allow other grant
operations, such as `Decrypt` or `ReEncryptFrom`.

**See also**

- [kms:GrantConstraintType](#conditions-kms-grant-constraint-type "#conditions-kms-grant-constraint-type")
- [kms:GrantIsForAWSResource](#conditions-kms-grant-is-for-aws-resource "#conditions-kms-grant-is-for-aws-resource")
- [kms:GranteePrincipal](#conditions-kms-grantee-principal "#conditions-kms-grantee-principal")
- [kms:RetiringPrincipal](#conditions-kms-retiring-principal "#conditions-kms-retiring-principal")

## kms:GranteePrincipal

| AWS KMS condition keys | Condition type | Value type    | API operations | Policy type          |
| ---------------------- | -------------- | ------------- | -------------- | -------------------- |
| `kms:GranteePrincipal` | String         | Single-valued | `CreateGrant`  | IAM and key policies |

You can use this condition key to control access to the [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") operation based on the value
of the [GranteePrincipal](../APIReference/API_CreateGrant.md#KMS-CreateGrant-request-GranteePrincipal "../APIReference/API_CreateGrant.md#KMS-CreateGrant-request-GranteePrincipal") parameter in the request. For example, you can to create grants
to use a KMS key only when the grantee principal in the `CreateGrant` request
matches the principal specified in the condition statement.

To specify the grantee principal, use the Amazon Resource Name (ARN) of an AWS
principal. Valid principals include AWS accounts, IAM users, IAM roles, federated
users, and assumed role users. For help with the ARN syntax for a principal, see [IAM ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns")
in the _IAM User Guide_.

The following example key policy statement uses the `kms:GranteePrincipal`
condition key to to create grants for a KMS key only when the grantee principal in the
grant is the `LimitedAdminRole`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:CreateGrant",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:GranteePrincipal": "arn:aws:iam::111122223333:role/LimitedAdminRole"**
    }
  }
}
```

**See also**

- [kms:GrantConstraintType](#conditions-kms-grant-constraint-type "#conditions-kms-grant-constraint-type")
- [kms:GrantIsForAWSResource](#conditions-kms-grant-is-for-aws-resource "#conditions-kms-grant-is-for-aws-resource")
- [kms:GrantOperations](#conditions-kms-grant-operations "#conditions-kms-grant-operations")
- [kms:RetiringPrincipal](#conditions-kms-retiring-principal "#conditions-kms-retiring-principal")

## kms:KeyAgreementAlgorithm

| AWS KMS condition keys      | Condition type | Value type    | API operations       | Policy type                   |
| --------------------------- | -------------- | ------------- | -------------------- | ----------------------------- |
| `kms:KeyAgreementAlgorithm` | String         | Single-valued | `DeriveSharedSecret` | Key policies and IAM policies |

You can use the `kms:KeyAgreementAlgorithm` condition key to control access
to the [DeriveSharedSecret](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md")
operation based on the value of the `KeyAgreementAlgorithm` parameter in the
request. The only valid value for `KeyAgreementAlgorithm` is
`ECDH`.

For example, the following key policy statement uses the
`kms:KeyAgreementAlgorithm` condition key to deny all access to
DeriveSharedSecret unless the `KeyAgreementAlgorithm` is
`ECDH`.

```

{
       "Effect": "Deny",
       "Principal": {
         "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
       },
       "Action": "kms:DeriveSharedSecret",
       "Resource": "*",
       "Condition": {
            "StringNotEquals": {
               **"kms:KeyAgreementAlgorithm": "ECDH"**
         }
       }
}

```

**See also**

- [kms:KeyUsage](#conditions-kms-key-usage "#conditions-kms-key-usage")

## kms:KeyOrigin

| AWS KMS condition keys | Condition type | Value type    | API operations                             | Policy type                                   |
| ---------------------- | -------------- | ------------- | ------------------------------------------ | --------------------------------------------- |
| `kms:KeyOrigin`        | String         | Single-valued | `CreateKey`<br>KMS key resource operations | IAM policies<br>Key policies and IAM policies |

The `kms:KeyOrigin` condition key controls access to operations based on the
value of the `Origin` property of the KMS key that is created by or used in the
operation. It works as a resource condition or a request condition.

You can use this condition key to control access to the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation based on the value of
the [Origin](../APIReference/API_CreateKey.md#KMS-CreateKey-request-Origin "../APIReference/API_CreateKey.md#KMS-CreateKey-request-Origin")
parameter in the request. Valid values for `Origin` are `AWS_KMS`,
`AWS_CLOUDHSM`, and `EXTERNAL`.

For example, you can to create a KMS key only when the key material is generated in
AWS KMS (`AWS_KMS`), only when the key material is generated in an AWS CloudHSM cluster
that is associated with a [custom key store](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview")
(`AWS_CLOUDHSM`), or only when the [key material
is imported](importing-keys.md "importing-keys.md") from an external source (`EXTERNAL`).

The following example key policy statement uses the `kms:KeyOrigin` condition
key to to create a KMS key only when AWS KMS creates the key material.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
 },
 "Action": "kms:CreateKey",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:KeyOrigin": "AWS_KMS"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:GenerateDataKeyWithoutPlaintext",
 "kms:GenerateDataKeyPair",
 "kms:GenerateDataKeyPairWithoutPlaintext",
 "kms:ReEncrypt*"
 ],
 "Resource": "arn:aws:kms:us-west-2:111122223333:key/*",
 "Condition": {
 "StringEquals": {
 "kms:KeyOrigin": "AWS_CLOUDHSM"
 }
 }
 }
 ]
}`

```

You can also use the `kms:KeyOrigin` condition key to control access to
operations that use or manage a KMS key based on the `Origin` property of the
KMS key used for the operation. The operation must be a _KMS key resource operation_, that is, an operation that is authorized for a particular KMS key. To identify the KMS key resource operations, in the [Actions
and Resources Table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look for a value of `KMS key` in the `Resources` column for the operation.

For example, the following IAM policy allows principals to perform the specified
KMS key resource operations, but only with KMS keys in the account that were created in
a custom key store.

```
{
  "Effect": "Allow",
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:GenerateDataKey",
    "kms:GenerateDataKeyWithoutPlaintext",
    "kms:GenerateDataKeyPair",
    "kms:GenerateDataKeyPairWithoutPlaintext",
    "kms:ReEncrypt*"
  ],
  "Resource": "arn:aws:kms:us-west-2:111122223333:key/*",
  "Condition": {
    "StringEquals": {
      **"kms:KeyOrigin": "AWS\_CLOUDHSM"**
    }
  }
}
```

**See also**

- [kms:BypassPolicyLockoutSafetyCheck](#conditions-kms-bypass-policy-lockout-safety-check "#conditions-kms-bypass-policy-lockout-safety-check")
- [kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec")
- [kms:KeyUsage](#conditions-kms-key-usage "#conditions-kms-key-usage")

## kms:KeySpec

| AWS KMS condition keys | Condition type | Value type    | API operations                             | Policy type                                   |
| ---------------------- | -------------- | ------------- | ------------------------------------------ | --------------------------------------------- |
| `kms:KeySpec`          | String         | Single-valued | `CreateKey`<br>KMS key resource operations | IAM policies<br>Key policies and IAM policies |

The `kms:KeySpec` condition key controls access to operations based on the
value of the `KeySpec` property of the KMS key that is created by or used in
the operation.

You can use this condition key in an IAM policy to control access to the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation based on the value of
the [KeySpec](../APIReference/API_CreateKey.md#KMS-CreateKey-request-KeySpec "../APIReference/API_CreateKey.md#KMS-CreateKey-request-KeySpec") parameter in a `CreateKey` request. For example, you can use
this condition to allow users to create only symmetric encryption KMS keys or only HMAC
KMS keys.

The following example IAM policy statement uses the `kms:KeySpec` condition
key to allow the principals to create only RSA asymmetric KMS keys. The permission is
valid only when the `KeySpec` in the request begins with
`RSA_`.

```
{
  "Effect": "Allow",
  "Action": "kms:CreateKey",
  "Resource": "*",
  "Condition": {
    "StringLike": {
      **"kms:KeySpec": "RSA\_\*"**
    }
  }
}
```

You can also use the `kms:KeySpec` condition key to control access to
operations that use or manage a KMS key based on the `KeySpec` property of the
KMS key used for the operation. The operation must be a _KMS key resource operation_, that is, an operation that is authorized for a particular KMS key. To identify the KMS key resource operations, in the [Actions
and Resources Table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look for a value of `KMS key` in the `Resources` column for the operation.

For example, the following IAM policy allows principals to perform the specified
KMS key resource operations, but only with symmetric encryption KMS keys in the account.

```
{
  "Effect": "Allow",
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:DescribeKey"
  ],
  "Resource": "arn:aws:kms:us-west-2:111122223333:key/*",
  "Condition": {
    "StringEquals": {
      "kms:KeySpec": "SYMMETRIC_DEFAULT"
    }
  }
}
```

**See also**

- [kms:BypassPolicyLockoutSafetyCheck](#conditions-kms-bypass-policy-lockout-safety-check "#conditions-kms-bypass-policy-lockout-safety-check")
- [kms:CustomerMasterKeySpec
  (deprecated)](#conditions-kms-key-spec-replaced "#conditions-kms-key-spec-replaced")
- [kms:DataKeyPairSpec](#conditions-kms-data-key-spec "#conditions-kms-data-key-spec")
- [kms:KeyOrigin](#conditions-kms-key-origin "#conditions-kms-key-origin")
- [kms:KeyUsage](#conditions-kms-key-usage "#conditions-kms-key-usage")

## kms:KeyUsage

| AWS KMS condition keys | Condition type | Value type    | API operations                             | Policy type                                   |
| ---------------------- | -------------- | ------------- | ------------------------------------------ | --------------------------------------------- |
| `kms:KeyUsage`         | String         | Single-valued | `CreateKey`<br>KMS key resource operations | IAM policies<br>Key policies and IAM policies |

The `kms:KeyUsage` condition key controls access to operations based on the
value of the `KeyUsage` property of the KMS key that is created by or used in
the operation.

You can use this condition key to control access to the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation based on the value of
the [KeyUsage](../APIReference/API_CreateKey.md#KMS-CreateKey-request-KeyUsage "../APIReference/API_CreateKey.md#KMS-CreateKey-request-KeyUsage") parameter in the request. Valid values for `KeyUsage` are
`ENCRYPT_DECRYPT`, `SIGN_VERIFY`, `GENERATE_VERIFY_MAC`,
and `KEY_AGREEMENT`.

For example, you can to create a KMS key only when the `KeyUsage` is
`ENCRYPT_DECRYPT` or deny a user permission when the `KeyUsage` is
`SIGN_VERIFY`.

The following example IAM policy statement uses the `kms:KeyUsage`
condition key to to create a KMS key only when the `KeyUsage` is
`ENCRYPT_DECRYPT`.

```
{
  "Effect": "Allow",
  "Action": "kms:CreateKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:KeyUsage": "ENCRYPT\_DECRYPT"**
    }
  }
}
```

You can also use the `kms:KeyUsage` condition key to control access to
operations that use or manage a KMS key based on the `KeyUsage` property of the
KMS key in the operation. The operation must be a _KMS key resource operation_, that is, an operation that is authorized for a particular KMS key. To identify the KMS key resource operations, in the [Actions
and Resources Table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look for a value of `KMS key` in the `Resources` column for the operation.

For example, the following IAM policy allows principals to perform the specified
KMS key resource operations, but only with KMS keys in the account that are used for
signing and verification.

```
{
  "Effect": "Allow",
  "Action": [
    "kms:CreateGrant",
    "kms:DescribeKey",
    "kms:GetPublicKey",
    "kms:ScheduleKeyDeletion"
  ],
  "Resource": "arn:aws:kms:us-west-2:111122223333:key/*",
  "Condition": {
    "StringEquals": {
      **"kms:KeyUsage": "SIGN\_VERIFY"**
    }
  }
}
```

**See also**

- [kms:BypassPolicyLockoutSafetyCheck](#conditions-kms-bypass-policy-lockout-safety-check "#conditions-kms-bypass-policy-lockout-safety-check")
- [kms:CustomerMasterKeyUsage
  (deprecated)](#conditions-kms-key-usage-replaced "#conditions-kms-key-usage-replaced")
- [kms:KeyOrigin](#conditions-kms-key-origin "#conditions-kms-key-origin")
- [kms:KeySpec](#conditions-kms-key-spec "#conditions-kms-key-spec")

## kms:MacAlgorithm

| AWS KMS condition keys | Condition type | Value type    | API operations           | Policy type                   |
| ---------------------- | -------------- | ------------- | ------------------------ | ----------------------------- |
| `kms:MacAlgorithm`     | String         | Single-valued | `GenerateMac``VerifyMac` | Key policies and IAM policies |

You can use the `kms:MacAlgorithm` condition key to control access to the
[GenerateMac](../APIReference/API_GenerateMac.md "../APIReference/API_GenerateMac.md") and [VerifyMac](../APIReference/API_VerifyMac.md "../APIReference/API_VerifyMac.md") operations based on the value of
the `MacAlgorithm` parameter in the request.

The following example key policy allows users who can assume the `testers`
role to use the HMAC KMS key to generate and verify HMAC tags only when the MAC algorithm
in the request is `HMAC_SHA_384` or `HMAC_SHA_512`. This policy uses
two separate policy statements each with its own condition. If you specify more than one MAC
algorithm in a single condition statement, the condition requires both algorithms, instead
of one or the other.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/testers"
 },
 "Action": [
 "kms:GenerateMac",
 "kms:VerifyMac"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:MacAlgorithm": "HMAC_SHA_384"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/testers"
 },
 "Action": [
 "kms:GenerateMac",
 "kms:VerifyMac"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:MacAlgorithm": "HMAC_SHA_512"
 }
 }
 }
 ]
}`

```

**See also**

- [kms:EncryptionAlgorithm](#conditions-kms-encryption-algorithm "#conditions-kms-encryption-algorithm")
- [kms:SigningAlgorithm](#conditions-kms-signing-algorithm "#conditions-kms-signing-algorithm")

## kms:MessageType

| AWS KMS condition keys | Condition type | Value type    | API operations     | Policy type                   |
| ---------------------- | -------------- | ------------- | ------------------ | ----------------------------- |
| `kms:MessageType`      | String         | Single-valued | `Sign`<br>`Verify` | Key policies and IAM policies |

The `kms:MessageType` condition key controls access to the [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md") and [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md") operations based on the value of the
`MessageType` parameter in the request. Valid values for
`MessageType` are `RAW` and `DIGEST`.

For example, the following key policy statement uses the `kms:MessageType`
condition key to to use an asymmetric KMS key to sign a message, but not a message
digest.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:Sign",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:MessageType": "RAW"**
    }
  }
}
```

**See also**

- [kms:SigningAlgorithm](#conditions-kms-signing-algorithm "#conditions-kms-signing-algorithm")

## kms:MultiRegion

| AWS KMS condition keys | Condition type | Value type    | API operations                             | Policy type                   |
| ---------------------- | -------------- | ------------- | ------------------------------------------ | ----------------------------- |
| `kms:MultiRegion`      | Boolean        | Single-valued | `CreateKey`<br>KMS key resource operations | Key policies and IAM policies |

You can use this condition key to allow operations only on single-Region keys or only on
[multi-Region keys](multi-region-keys-overview.md "multi-region-keys-overview.md"). The
`kms:MultiRegion` condition key controls access to AWS KMS operations on
KMS keys and to the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
operation based on the value of the `MultiRegion` property of the KMS key.
Valid values are `true` (multi-Region), and `false` (single-Region).
All KMS keys have a `MultiRegion` property.

For example, the following IAM policy statement uses the `kms:MultiRegion`
condition key to allow principals to create only single-Region keys.

```
{
  "Effect": "Allow",
  "Action": "kms:CreateKey",
  "Resource": "*",
  "Condition": {
    "Bool": {
      **"kms:MultiRegion": false**
    }
  }
}
```

## kms:MultiRegionKeyType

| AWS KMS condition keys   | Condition type | Value type    | API operations                             | Policy type                   |
| ------------------------ | -------------- | ------------- | ------------------------------------------ | ----------------------------- |
| `kms:MultiRegionKeyType` | String         | Single-valued | `CreateKey`<br>KMS key resource operations | Key policies and IAM policies |

You can use this condition key to allow operations only on [multi-Region primary keys](multi-region-keys-overview.md#mrk-primary-key "multi-region-keys-overview.md#mrk-primary-key") or only on [multi-Region replica keys](multi-region-keys-overview.md#mrk-replica-key "multi-region-keys-overview.md#mrk-replica-key"). The
`kms:MultiRegionKeyType` condition key controls access to AWS KMS operations on
KMS keys and the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation
based on the `MultiRegionKeyType` property of the KMS key. The valid values are
`PRIMARY` and `REPLICA`. Only multi-Region keys have a
`MultiRegionKeyType` property.

Typically, you use the `kms:MultiRegionKeyType` condition key in an IAM
policy to control access to multiple KMS keys. However, because a given multi-Region key
can change to primary or replica, you might want to use this condition in a key policy to
allow an operation only when the particular multi-Region key is a primary or replica
key.

For example, the following IAM policy statement uses the
`kms:MultiRegionKeyType` condition key to allow principals to schedule and
cancel key deletion only on multi-Region replica keys in the specified AWS account.

```
{
  "Effect": "Allow",
  "Action": [
    "kms:ScheduleKeyDeletion",
    "kms:CancelKeyDeletion"
  ],
  "Resource": "arn:aws:kms:*:111122223333:key/*",
  "Condition": {
    "StringEquals": {
      "kms:MultiRegionKeyType": "REPLICA"
    }
  }
}
```

To allow or deny access to all multi-Region keys, you can use both values or a null
value with `kms:MultiRegionKeyType`. However, the [kms:MultiRegion](#conditions-kms-multiregion "#conditions-kms-multiregion") condition key is recommended
for that purpose.

## kms:PrimaryRegion

| AWS KMS condition keys | Condition type | Value type    | API operations        | Policy type                   |
| ---------------------- | -------------- | ------------- | --------------------- | ----------------------------- |
| `kms:PrimaryRegion`    | String (list)  | Single-valued | `UpdatePrimaryRegion` | Key policies and IAM policies |

You can use this condition key to limit the destination Regions in an [UpdatePrimaryRegion](../APIReference/API_UpdatePrimaryRegion.md "../APIReference/API_UpdatePrimaryRegion.md") operation.
These are AWS Regions that can host your multi-Region primary keys.

The `kms:PrimaryRegion` condition key controls access to the [UpdatePrimaryRegion](../APIReference/API_UpdatePrimaryRegion.md "../APIReference/API_UpdatePrimaryRegion.md") operation
based on the value of the `PrimaryRegion` parameter. The
`PrimaryRegion` parameter specifies the AWS Region of the [multi-Region replica key](multi-region-keys-overview.md#mrk-replica-key "multi-region-keys-overview.md#mrk-replica-key") that is being promoted to
primary. The value of the condition is one or more AWS Region names, such as
`us-east-1` or `ap-southeast-2`, or Region name patterns, such as
`eu-*`

For example, the following key policy statement uses the `kms:PrimaryRegion`
condition key to allow principals to update the primary region of a multi-Region key to one
of the four specified Regions.

```
{
  "Effect": "Allow",
  "Action": "kms:UpdatePrimaryRegion",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/Developer"
  },
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:PrimaryRegion": [
 "us-east-1",
 "us-west-2",
 "eu-west-3",
 "ap-southeast-2"
 ]**
    }
  }
}
```

## kms:ReEncryptOnSameKey

| AWS KMS condition keys   | Condition type | Value type    | API operations | Policy type                   |
| ------------------------ | -------------- | ------------- | -------------- | ----------------------------- |
| `kms:ReEncryptOnSameKey` | Boolean        | Single-valued | `ReEncrypt`    | Key policies and IAM policies |

You can use this condition key to control access to the [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md") operation based on whether the
request specifies a destination KMS key that is the same one used for the original
encryption.

For example, the following key policy statement uses the
`kms:ReEncryptOnSameKey` condition key to to reencrypt only when the
destination KMS key is the same one used for the original encryption.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:ReEncrypt*",
  "Resource": "*",
  "Condition": {
    "Bool": {
      **"kms:ReEncryptOnSameKey": true**
    }
  }
}
```

## kms:RequestAlias

| AWS KMS condition keys | Condition type | Value type    | API operations                                                                                                                                                                                                                                                                                                    | Policy type                   |
| ---------------------- | -------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `kms:RequestAlias`     | String (list)  | Single-valued | [Cryptographic<br>operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations")<br>[DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md")<br>[GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") | Key policies and IAM policies |

You can use this condition key to allow an operation only when the request uses a
particular alias to identify the KMS key. The `kms:RequestAlias` condition key
controls access to a KMS key used in a cryptographic operation, `GetPublicKey`,
or `DescribeKey` based on the [alias](kms-alias.md "kms-alias.md") that
identifies that KMS key in the request. (This policy condition has no effect on the [GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md") operation because the
operation doesn't use a KMS key or alias.)

This condition supports [attribute-based access control](abac.md "abac.md")
(ABAC) in AWS KMS, which lets you control access to KMS keys based on the tags and aliases
of a KMS key. You can use tags and aliases to allow or deny access to a KMS key without
changing policies or grants. For details, see [ABAC for AWS KMS](abac.md "abac.md").

To specify the alias in this policy condition, use an [alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name"), such as `alias/project-alpha`, or an alias name pattern,
such as `alias/*test*`. You cannot specify an [alias ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN") in the value of this condition key.

To satisfy this condition, the value of the `KeyId` parameter in the request
must be a matching alias name or alias ARN. If the request uses a different [key identifier](concepts.md#key-id "concepts.md#key-id"), it does not satisfy the condition, even if
identifies the same KMS key.

For example, the following key policy statement allows the principal to call the [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") operation on the
KMS key. However this is permitted only when the value of the `KeyId` parameter
in the request is `alias/finance-key` or an alias ARN with that alias name, such
as `arn:aws:kms:us-west-2:111122223333:alias/finance-key`.

```
{
  "Sid": "Key policy using a request alias condition",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/developer"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:RequestAlias": "alias/finance-key"**
    }
  }
}
```

You cannot use this condition key to control access to alias operations, such as [CreateAlias](../APIReference/API_CreateAlias.md "../APIReference/API_CreateAlias.md") or [DeleteAlias](../APIReference/API_DeleteAlias.md "../APIReference/API_DeleteAlias.md"). For information about
controlling access to alias operations, see [Controlling access to aliases](alias-access.md "alias-access.md").

## kms:ResourceAliases

| AWS KMS condition keys | Condition type | Value type   | API operations              | Policy type       |
| ---------------------- | -------------- | ------------ | --------------------------- | ----------------- |
| `kms:ResourceAliases`  | String (list)  | Multi-valued | KMS key resource operations | IAM policies only |

Use this condition key to control access to a KMS key based on the [aliases](kms-alias.md "kms-alias.md") that are associated with the KMS key.
The operation must be a _KMS key resource operation_, that is, an operation that is authorized for a particular KMS key. To identify the KMS key resource operations, in the [Actions
and Resources Table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look for a value of `KMS key` in the `Resources` column for the operation.

This condition supports attribute-based access control (ABAC) in AWS KMS. With ABAC, you
can control access to KMS keys based on the tags that are assigned to a KMS key and the
aliases that are associated with a KMS key. You can use tags and aliases to allow or deny
access to a KMS key without changing policies or grants. For details, see [ABAC for AWS KMS](abac.md "abac.md").

An alias must be unique in an AWS account and Region, but this condition lets you
control access to multiple KMS keys in the same Region (using the `StringLike`
comparison operator) or to multiple KMS keys in different AWS Regions of each
account.

###### Note

The kms:ResourceAliases
condition is effective only when the KMS key conforms to the [aliases per KMS key](resource-limits.md#aliases-per-key "resource-limits.md#aliases-per-key") quota. If a KMS key exceeds
this quota, principals who are authorized to use the KMS key by the
`kms:ResourceAliases` condition are denied access to the KMS key.

To specify the alias in this policy condition, use an [alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name"), such as `alias/project-alpha`, or an alias name pattern,
such as `alias/*test*`. You cannot specify an [alias ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN") in the value of this condition key. To satisfy the condition, the
KMS key used in the operation must have the specified alias. It does not matter whether or
how the KMS key is identified in the request for the operation.

This is a multivalued condition key that compares the set of aliases associated with a
KMS key to the set of aliases in the policy. To determine how these sets are compared, you
must provide a `ForAnyValue` or `ForAllValues` set operator in the
policy condition. For details about the set operators, see [Using multiple keys and values](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions") in the IAM User Guide.

- ForAnyValue: At least one alias associated with the KMS key must match an alias in
  the policy condition. Other aliases are permitted. If the KMS key has no aliases, the
  condition is not satisfied.
- ForAllValues: Every alias associated with the KMS key must match an alias in the
  policy. This set operator limits the aliases associated with the KMS key to those in
  the policy condition. It doesn't require any aliases, but it forbids unspecified
  aliases.

For example, the following IAM policy statement allows the principal to call the
[GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") operation on
any KMS key in the specified AWS account that is associated with the
`finance-key` alias. (The key policies of the affected KMS keys must also
allow the principal's account to use them for this operation.) To indicate that the
condition is satisfied when one of the many aliases that might be associated with the
KMS key is `alias/finance-key`, the condition uses the `ForAnyValue`
set operator.

Because the `kms:ResourceAliases` condition is based on the resource, not the
request, a call to `GenerateDataKey` succeeds for any KMS key associated with
the `finance-key` alias, even if the request uses a [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") or [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN") to identify the KMS key.

```
{
  "Sid": "AliasBasedIAMPolicy",
  "Effect": "Allow",
  "Action": "kms:GenerateDataKey",
  "Resource": [
    "arn:aws:kms:*:111122223333:key/*",
    "arn:aws:kms:*:444455556666:key/*"
  ],
  "Condition": {
    "ForAnyValue:StringEquals": {
      **"kms:ResourceAliases": "alias/finance-key"**
    }
  }
}
```

The following example IAM policy statement allows the principal to enable and disable
KMS keys but only when all aliases of the KMS keys include "`Test`." This
policy statement uses two conditions. The condition with the `ForAllValues` set
operator requires that all aliases associated with the KMS key include "Test". The
condition with the `ForAnyValue` set operator requires that the KMS key have at
least one alias with "Test." Without the `ForAnyValue` condition, this policy
statement would have allowed the principal to use KMS keys that had no aliases.

```
{
  "Sid": "AliasBasedIAMPolicy",
  "Effect": "Allow",
  "Action": [
    "kms:EnableKey",
    "kms:DisableKey"
  ],
  "Resource": "arn:aws:kms:*:111122223333:key/*",
  "Condition": {
    "ForAllValues:StringLike": {
      "kms:ResourceAliases": [
        "alias/*Test*"
      ]
    },
    "ForAnyValue:StringLike": {
      "kms:ResourceAliases": [
        "alias/*Test*"
      ]
    }
  }
}
```

## kms:ReplicaRegion

| AWS KMS condition keys | Condition type | Value type    | API operations | Policy type                   |
| ---------------------- | -------------- | ------------- | -------------- | ----------------------------- |
| `kms:ReplicaRegion`    | String (list)  | Single-valued | `ReplicateKey` | Key policies and IAM policies |

You can use this condition key to limit the AWS Regions in which a principal can
replicate a [multi-Region key](multi-region-keys-overview.md "multi-region-keys-overview.md"). The
`kms:ReplicaRegion` condition key controls access to the [ReplicateKey](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") operation based on the value
of the [ReplicaRegion](../APIReference/API_CreateGrant.md#KMS-CreateGrant-request-RetiringPrincipal "../APIReference/API_CreateGrant.md#KMS-CreateGrant-request-RetiringPrincipal") parameter in the request. This parameter specifies the AWS Region
for the new [replica key](multi-region-keys-overview.md#mrk-replica-key "multi-region-keys-overview.md#mrk-replica-key").

The value of the condition is one or more AWS Region names, such as
`us-east-1` or `ap-southeast-2`, or name patterns, such as
`eu-*`. For a list of the names of AWS Regions that AWS KMS supports, see
[AWS Key Management Service endpoints and quotas](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md") in the
AWS General Reference.

For example, the following key policy statement uses the `kms:ReplicaRegion`
condition key to allow principals to call the [ReplicateKey](../APIReference/API_ReplicateKey.md "../APIReference/API_ReplicateKey.md") operation only when the
value of the `ReplicaRegion` parameter is one of the specified Regions.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/Administrator"
  },
  "Action": "kms:ReplicateKey"
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:ReplicaRegion": [
 "us-east-1",
 "eu-west-3",
 "ap-southeast-2"
 ]**
    }
  }
}
```

This condition key controls access only to the [ReplicateKey](../APIReference/API_ReplicateKey.md "../APIReference/API_ReplicateKey.md") operation. To control access
to the [UpdatePrimaryRegion](../APIReference/API_UpdatePrimaryRegion.md "../APIReference/API_UpdatePrimaryRegion.md")
operation, use the [kms:PrimaryRegion](#conditions-kms-primary-region "#conditions-kms-primary-region")
condition key.

## kms:RetiringPrincipal

| AWS KMS condition keys  | Condition type | Value type    | API operations | Policy type                   |
| ----------------------- | -------------- | ------------- | -------------- | ----------------------------- |
| `kms:RetiringPrincipal` | String (list)  | Single-valued | `CreateGrant`  | Key policies and IAM policies |

You can use this condition key to control access to the [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") operation based on the value
of the [RetiringPrincipal](../APIReference/API_CreateGrant.md#KMS-CreateGrant-request-RetiringPrincipal "../APIReference/API_CreateGrant.md#KMS-CreateGrant-request-RetiringPrincipal") parameter in the request. For example, you can to create grants
to use a KMS key only when the `RetiringPrincipal` in the
`CreateGrant` request matches the `RetiringPrincipal` in the
condition statement.

To specify the retiring principal, use the Amazon Resource Name (ARN) of an AWS
principal. Valid principals include AWS accounts, IAM users, IAM roles, federated
users, and assumed role users. For help with the ARN syntax for a principal, see [IAM ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns")
in the _IAM User Guide_.

The following example key policy statement allows a user to create grants for the
KMS key. The `kms:RetiringPrincipal` condition key restricts the permission to
`CreateGrant` requests where the retiring principal in the grant is the
`LimitedAdminRole`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:CreateGrant",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:RetiringPrincipal": "arn:aws:iam::111122223333:role/LimitedAdminRole"**
    }
  }
}
```

**See also**

- [kms:GrantConstraintType](#conditions-kms-grant-constraint-type "#conditions-kms-grant-constraint-type")
- [kms:GrantIsForAWSResource](#conditions-kms-grant-is-for-aws-resource "#conditions-kms-grant-is-for-aws-resource")
- [kms:GrantOperations](#conditions-kms-grant-operations "#conditions-kms-grant-operations")
- [kms:GranteePrincipal](#conditions-kms-grantee-principal "#conditions-kms-grantee-principal")

## kms:RotationPeriodInDays

| AWS KMS condition keys     | Condition type | Value type    | API operations      | Policy type                   |
| -------------------------- | -------------- | ------------- | ------------------- | ----------------------------- |
| `kms:RotationPeriodInDays` | Numeric        | Single-valued | `EnableKeyRotation` | Key policies and IAM policies |

You can use this condition key to limit the values that principals can specify in the
`RotationPeriodInDays` parameter of a [EnableKeyRotation](../APIReference/API_EnableKeyRotation.md "../APIReference/API_EnableKeyRotation.md") request.

The `RotationPeriodInDays` specifies the number of days between each
automatic key rotation date. AWS KMS allows you to specify a rotation period between 90 and
2560 days, but you can use the `kms:RotationPeriodInDays` condition key to
further constrain the rotation period, such as enforcing a minimum rotation period within
the valid range.

For example, the following key policy statement uses the
`kms:RotationPeriodInDays` condition key to prevent principals from enabling
key rotation if the rotation period is less than or equal to 180 days.

```
{
  "Effect": "Deny",
  "Action": "kms:EnableKeyRotation",
  "Principal": "*",
  "Resource": "*",
  "Condition" : {
      "NumericLessThanEquals" : {
        "kms:RotationPeriodInDays" : "180"
      }
  }
}
```

## kms:ScheduleKeyDeletionPendingWindowInDays

| AWS KMS condition keys                       | Condition type | Value type    | API operations        | Policy type                   |
| -------------------------------------------- | -------------- | ------------- | --------------------- | ----------------------------- |
| `kms:ScheduleKeyDeletionPendingWindowInDays` | Numeric        | Single-valued | `ScheduleKeyDeletion` | Key policies and IAM policies |

You can use this condition key to limit the values that principals can specify in the
`PendingWindowInDays` parameter of a [ScheduleKeyDeletion](../APIReference/API_ScheduleKeyDeletion.md "../APIReference/API_ScheduleKeyDeletion.md")
request.

The `PendingWindowInDays` specifies the number of days that AWS KMS will wait
before deleting a key. AWS KMS allows you to specify a waiting period between 7 and 30 days,
but you can use the `kms:ScheduleKeyDeletionPendingWindowInDays` condition key to
further constrain the waiting period, such as enforcing a minimum waiting period within the
valid range.

For example, the following key policy statement uses the
`kms:ScheduleKeyDeletionPendingWindowInDays` condition key to prevent
principals from scheduling key deletion if the waiting period is less than or equal to 21
days.

```
{
  "Effect": "Deny",
  "Action": "kms:ScheduleKeyDeletion",
  "Principal": "*",
  "Resource": "*",
  "Condition" : {
      "NumericLessThanEquals" : {
        "kms:ScheduleKeyDeletionPendingWindowInDays" : "21"
      }
  }
}
```

## kms:SigningAlgorithm

| AWS KMS condition keys | Condition type | Value type    | API operations     | Policy type                   |
| ---------------------- | -------------- | ------------- | ------------------ | ----------------------------- |
| `kms:SigningAlgorithm` | String         | Single-valued | `Sign`<br>`Verify` | Key policies and IAM policies |

You can use the `kms:SigningAlgorithm` condition key to control access to the
[Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md") and [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md") operations based on the value of the
[SigningAlgorithm](../APIReference/API_Sign.md#KMS-Sign-request-SigningAlgorithm "../APIReference/API_Sign.md#KMS-Sign-request-SigningAlgorithm") parameter in the request. This condition key has no effect on
operations performed outside of AWS KMS, such as verifying signatures with the public key in
an asymmetric KMS key pair outside of AWS KMS.

The following example key policy allows users who can assume the `testers`
role to use the KMS key to sign messages only when the signing algorithm used for the
request is an RSASSA_PSS algorithm, such as `RSASSA_PSS_SHA512`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/testers"
  },
  "Action": "kms:Sign",
  "Resource": "*",
  "Condition": {
    "StringLike": {
      **"kms:SigningAlgorithm": "RSASSA\_PSS\*"**
    }
  }
}
```

**See also**

- [kms:EncryptionAlgorithm](#conditions-kms-encryption-algorithm "#conditions-kms-encryption-algorithm")
- [kms:MacAlgorithm](#conditions-kms-mac-algorithm "#conditions-kms-mac-algorithm")
- [kms:MessageType](#conditions-kms-message-type "#conditions-kms-message-type")

## kms:ValidTo

| AWS KMS condition keys | Condition type | Value type    | API operations      | Policy type                   |
| ---------------------- | -------------- | ------------- | ------------------- | ----------------------------- |
| `kms:ValidTo`          | Timestamp      | Single-valued | `ImportKeyMaterial` | Key policies and IAM policies |

The `kms:ValidTo` condition key controls access to the [ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md") operation based on
the value of the [ValidTo](../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ValidTo "../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ValidTo") parameter in the request, which determines when the imported key material
expires. The value is expressed in [Unix
time](https://en.wikipedia.org/wiki/Unix_time "https://en.wikipedia.org/wiki/Unix_time").

By default, the `ValidTo` parameter is required in an
`ImportKeyMaterial` request. However, if the value of the [ExpirationModel](../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ExpirationModel "../APIReference/API_ImportKeyMaterial.md#KMS-ImportKeyMaterial-request-ExpirationModel") parameter is `KEY_MATERIAL_DOES_NOT_EXPIRE`, the
`ValidTo` parameter is invalid. You can also use the [kms:ExpirationModel](#conditions-kms-expiration-model "#conditions-kms-expiration-model") condition key to
require the `ExpirationModel` parameter or a specific parameter value.

The following example policy statement allows a user to import key material into a
KMS key. The `kms:ValidTo` condition key limits the permission to
`ImportKeyMaterial` requests where the `ValidTo` value is less than
or equal to `1546257599.0` (December 31, 2018 11:59:59 PM).

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:ImportKeyMaterial",
  "Resource": "*",
  "Condition": {
    "NumericLessThanEquals": {
      **"kms:ValidTo": "1546257599.0"**
    }
  }
}
```

**See also**

- [kms:ExpirationModel](#conditions-kms-expiration-model "#conditions-kms-expiration-model")
- [kms:WrappingAlgorithm](#conditions-kms-wrapping-algorithm "#conditions-kms-wrapping-algorithm")
- [kms:WrappingKeySpec](#conditions-kms-wrapping-key-spec "#conditions-kms-wrapping-key-spec")

## kms:ViaService

| AWS KMS condition keys | Condition type | Value type    | API operations              | Policy type                   |
| ---------------------- | -------------- | ------------- | --------------------------- | ----------------------------- |
| `kms:ViaService`       | String         | Single-valued | KMS key resource operations | Key policies and IAM policies |

The `kms:ViaService` condition key limits use of an KMS key to requests
from specified AWS services. This condition key only applies for [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md"). You can specify one or more services in each
`kms:ViaService` condition key. The operation must be a _KMS key resource operation_, that is, an operation that is authorized for a particular KMS key. To identify the KMS key resource operations, in the [Actions
and Resources Table](kms-api-permissions-reference.md#kms-api-permissions-reference-table "kms-api-permissions-reference.md#kms-api-permissions-reference-table"), look for a value of `KMS key` in the `Resources` column for the operation.

For example, the following key policy statement uses the `kms:ViaService`
condition key to allow a [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") to be used for
the specified actions only when the request comes from Amazon EC2 or Amazon RDS in the
US West (Oregon) region on behalf of `ExampleRole`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:CreateGrant",
    "kms:ListGrants",
    "kms:DescribeKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:ViaService"**: [
        **"ec2.us-west-2.amazonaws.com"**,
        **"rds.us-west-2.amazonaws.com"**
      ]
    }
  }
}
```

You can also use a `kms:ViaService` condition key to deny permission to use a
KMS key when the request comes from particular services. For example, the following policy
statement from a key policy uses a `kms:ViaService` condition key to prevent a
customer managed key from being used for `Encrypt` operations when the request comes from
AWS Lambda on behalf of `ExampleRole`.

```
{
  "Effect": **"Deny"**,
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": [
    "kms:Encrypt"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:ViaService"**: [
          **"lambda.us-west-2.amazonaws.com"**
      ]
    }
  }
}
```

###### Important

When you use the `kms:ViaService` condition key, the service makes the
request on behalf of a principal in the AWS account. These principals must have the
following permissions:

- Permission to use the KMS key. The principal needs to grant these permissions to
  the integrated service so the service can use the customer managed key on behalf of the
  principal. For more information, see [Using AWS KMS encryption with AWS services](service-integration.md "service-integration.md").
- Permission to use the integrated service. For details about giving users access to
  an AWS service that integrates with AWS KMS, consult the documentation for the
  integrated service.

All [AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key") use a
`kms:ViaService` condition key in their key policy document. This condition
allows the KMS key to be used only for requests that come from the service that created
the KMS key. To see the key policy for an AWS managed key, use the [GetKeyPolicy](../APIReference/API_GetKeyPolicy.md "../APIReference/API_GetKeyPolicy.md") operation.

The `kms:ViaService` condition key is valid in IAM and key policy
statements. The services that you specify must be [integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration") and support the `kms:ViaService` condition
key.

### Services that support the `kms:ViaService`

condition key

The following table lists AWS services that are integrated with AWS KMS and support
the use of the `kms:ViaService` condition key in customer managed keys The services in
this table might not be available in all regions. Use the `.amazonaws.com`
suffix of the AWS KMS ViaService name in all AWS partitions.

###### Note

You might need to scroll horizontally or vertically to see all of the data in this table.

| Service name                                           | AWS KMS ViaService name                                                                                                                       |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon AI Operations                                   | `aiops.`AWS_region`.amazonaws.com`                                                                                                            |
| AWS App Runner                                         | `apprunner.`AWS_region`.amazonaws.com`                                                                                                        |
| AWS AppFabric                                          | `appfabric.`AWS_region`.amazonaws.com`                                                                                                        |
| Amazon AppFlow                                         | `appflow.`AWS_region`.amazonaws.com`                                                                                                          |
| AWS Application Migration Service                      | `mgn.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Athena                                          | `athena.`AWS_region`.amazonaws.com`                                                                                                           |
| AWS Audit Manager                                      | `auditmanager.`AWS_region`.amazonaws.com`                                                                                                     |
| Amazon Aurora                                          | `rds.`AWS_region`.amazonaws.com`                                                                                                              |
| AWS Backup                                             | `backup.`AWS_region`.amazonaws.com`                                                                                                           |
| AWS Backup Gateway                                     | `backup-gateway.`AWS_region`.amazonaws.com`                                                                                                   |
| Amazon Bedrock Model Copy                              | `bedrock.`AWS_region`.amazonaws.com`                                                                                                          |
| Amazon Chime SDK                                       | `chimevoiceconnector.`AWS_region`.amazonaws.com`                                                                                              |
| AWS Clean Rooms ML                                     | `cleanrooms-ml.`AWS_region`.amazonaws.com`                                                                                                    |
| AWS CodeArtifact                                       | `codeartifact.`AWS_region`.amazonaws.com`                                                                                                     |
| Amazon CodeGuru Reviewer                               | `codeguru-reviewer.`AWS_region`.amazonaws.com`                                                                                                |
| Amazon Comprehend                                      | `comprehend.`AWS_region`.amazonaws.com`                                                                                                       |
| Amazon Connect                                         | `connect.`AWS_region`.amazonaws.com`                                                                                                          |
| Amazon Connect Customer Profiles                       | `profile.`AWS_region`.amazonaws.com`                                                                                                          |
| Amazon Q in Connect                                    | `wisdom.`AWS_region`.amazonaws.com`                                                                                                           |
| AWS Database Migration Service (AWS DMS)               | `dms.`AWS_region`.amazonaws.com`                                                                                                              |
| AWS DeepRacer                                          | `deepracer.`AWS_region`.amazonaws.com`                                                                                                        |
| AWS Directory Service                                  | `directoryservice.`AWS_region`.amazonaws.com`                                                                                                 |
| Amazon DocumentDB                                      | `docdb-elastic.`AWS_region`.amazonaws.com`                                                                                                    |
| Amazon DynamoDB                                        | `dynamodb.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon EC2 Systems Manager (SSM)                       | `ssm.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Elastic Block Store (Amazon EBS)                | `ec2.`AWS_region`.amazonaws.com` (EBS<br>only)                                                                                                |
| Amazon Elastic Container Registry (Amazon ECR)         | `ecr.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Elastic File System (Amazon EFS)                | `elasticfilesystem.`AWS_region`.amazonaws.com`                                                                                                |
| Amazon ElastiCache                                     | Include both ViaService names in the condition key value:<br>• `elasticache.`AWS_region`.amazonaws.com`<br>• `dax.`AWS_region`.amazonaws.com` |
| AWS Elemental MediaTailor                              | `mediatailor.`AWS_region`.amazonaws.com`                                                                                                      |
| AWS Entity Resolution                                  | `entityresolution.`AWS_region`.amazonaws.com`                                                                                                 |
| Amazon EventBridge                                     | `events.`AWS_region`.amazonaws.com`                                                                                                           |
| Amazon FinSpace                                        | `finspace.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon Forecast                                        | `forecast.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon FSx                                             | `fsx.`AWS_region`.amazonaws.com`                                                                                                              |
| AWS Glue                                               | `glue.`AWS_region`.amazonaws.com`                                                                                                             |
| AWS Ground Station                                     | `groundstation.`AWS_region`.amazonaws.com`                                                                                                    |
| Amazon GuardDuty                                       | `malware-protection.`AWS_region`.amazonaws.com`                                                                                               |
| AWS HealthLake                                         | `healthlake.`AWS_region`.amazonaws.com`                                                                                                       |
| AWS IoT SiteWise                                       | `iotsitewise.`AWS_region`.amazonaws.com`                                                                                                      |
| Amazon Kendra                                          | `kendra.`AWS_region`.amazonaws.com`                                                                                                           |
| Amazon Keyspaces (for Apache Cassandra)                | `cassandra.`AWS_region`.amazonaws.com`                                                                                                        |
| Amazon Kinesis                                         | `kinesis.`AWS_region`.amazonaws.com`                                                                                                          |
| Amazon Data Firehose                                   | `firehose.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon Kinesis Video Streams                           | `kinesisvideo.`AWS_region`.amazonaws.com`                                                                                                     |
| AWS Lambda                                             | `lambda.`AWS_region`.amazonaws.com`                                                                                                           |
| Amazon Lex                                             | `lex.`AWS_region`.amazonaws.com`                                                                                                              |
| AWS License Manager                                    | `license-manager.`AWS_region`.amazonaws.com`                                                                                                  |
| Amazon Location Service                                | `geo.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Lookout for Equipment                           | `lookoutequipment.`AWS_region`.amazonaws.com`                                                                                                 |
| Amazon Lookout for Metrics                             | `lookoutmetrics.`AWS_region`.amazonaws.com`                                                                                                   |
| Amazon Lookout for Vision                              | `lookoutvision.`AWS_region`.amazonaws.com`                                                                                                    |
| Amazon Macie                                           | `macie.`AWS_region`.amazonaws.com`                                                                                                            |
| AWS Mainframe Modernization                            | `m2.`AWS_region`.amazonaws.com`                                                                                                               |
| AWS Mainframe Modernization Application Testing        | `apptest.`AWS_region`.amazonaws.com`                                                                                                          |
| Amazon Managed Blockchain                              | `managedblockchain.`AWS_region`.amazonaws.com`                                                                                                |
| Amazon Managed Streaming for Apache Kafka (Amazon MSK) | `kafka.`AWS_region`.amazonaws.com`                                                                                                            |
| Amazon Managed Workflows for Apache Airflow (MWAA)     | `airflow.`AWS_region`.amazonaws.com`                                                                                                          |
| Amazon MemoryDB                                        | `memorydb.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon Monitron                                        | `monitron.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon MQ                                              | `mq.`AWS_region`.amazonaws.com`                                                                                                               |
| Amazon Neptune                                         | `rds.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Nimble Studio                                   | `nimble.`AWS_region`.amazonaws.com`                                                                                                           |
| AWS HealthOmics                                        | `omics.`AWS_region`.amazonaws.com`                                                                                                            |
| Amazon OpenSearch Service                              | `es.`AWS_region`.amazonaws.com`,<br>`aoss.`AWS_region`.amazonaws.com`                                                                         |
| Amazon OpenSearch Custom Packages                      | `custom-packages.`AWS_region`.amazonaws.com`                                                                                                  |
| AWS Proton                                             | `proton.`AWS_region`.amazonaws.com`                                                                                                           |
| Amazon Quantum Ledger Database (Amazon QLDB)           | `qldb.`AWS_region`.amazonaws.com`                                                                                                             |
| Amazon RDS Performance Insights                        | `rds.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Redshift                                        | `redshift.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon Redshift query editor V2                        | `sqlworkbench.`AWS_region`.amazonaws.com`                                                                                                     |
| Amazon Redshift Serverless                             | `redshift-serverless.`AWS_region`.amazonaws.com`                                                                                              |
| Amazon Rekognition                                     | `rekognition.`AWS_region`.amazonaws.com`                                                                                                      |
| Amazon Relational Database Service (Amazon RDS)        | `rds.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Replicated Data Store                           | `ards.`AWS_region`.amazonaws.com`                                                                                                             |
| Amazon SageMaker AI                                    | `sagemaker.`AWS_region`.amazonaws.com`                                                                                                        |
| AWS Secrets Manager                                    | `secretsmanager.`AWS_region`.amazonaws.com`                                                                                                   |
| Amazon Security Lake                                   | `securitylake.`AWS_region`.amazonaws.com`                                                                                                     |
| Amazon Simple Email Service (Amazon SES)               | `ses.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Simple Notification Service (Amazon SNS)        | `sns.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Simple Queue Service (Amazon SQS)               | `sqs.`AWS_region`.amazonaws.com`                                                                                                              |
| Amazon Simple Storage Service (Amazon S3)              | `s3.`AWS_region`.amazonaws.com`                                                                                                               |
| Amazon S3 Tables                                       | `s3tables.`AWS_region`.amazonaws.com`                                                                                                         |
| AWS Snowball Edge                                      | `importexport.`AWS_region`.amazonaws.com`                                                                                                     |
| AWS Step Functions                                     | `states.`AWS_region`.amazonaws.com`                                                                                                           |
| AWS Storage Gateway                                    | `storagegateway.`AWS_region`.amazonaws.com`                                                                                                   |
| AWS Systems Manager Incident Manager                   | `ssm-incidents.`AWS_region`.amazonaws.com`                                                                                                    |
| AWS Systems Manager Incident Manager Contacts          | `ssm-contacts.`AWS_region`.amazonaws.com`                                                                                                     |
| Amazon Timestream                                      | `timestream.`AWS_region`.amazonaws.com`                                                                                                       |
| Amazon Translate                                       | `translate.`AWS_region`.amazonaws.com`                                                                                                        |
| AWS Verified Access                                    | `verified-access.`AWS_region`.amazonaws.com`                                                                                                  |
| Amazon WorkMail                                        | `workmail.`AWS_region`.amazonaws.com`                                                                                                         |
| Amazon WorkSpaces                                      | `workspaces.`AWS_region`.amazonaws.com`                                                                                                       |
| Amazon WorkSpaces Thin Client                          | `thinclient.`AWS_region`.amazonaws.com`                                                                                                       |
| Amazon WorkSpaces Web                                  | `workspaces-web.`AWS_region`.amazonaws.com`                                                                                                   |
| AWS X-Ray                                              | `xray.`AWS_region`.amazonaws.com`                                                                                                             |

## kms:WrappingAlgorithm

| AWS KMS condition keys  | Condition type | Value type    | API operations           | Policy type                   |
| ----------------------- | -------------- | ------------- | ------------------------ | ----------------------------- |
| `kms:WrappingAlgorithm` | String         | Single-valued | `GetParametersForImport` | Key policies and IAM policies |

This condition key controls access to the [GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md")
operation based on the value of the [WrappingAlgorithm](../APIReference/API_GetParametersForImport.md#KMS-GetParametersForImport-request-WrappingAlgorithm "../APIReference/API_GetParametersForImport.md#KMS-GetParametersForImport-request-WrappingAlgorithm") parameter in the request. You can use this condition to require
principals to use a particular algorithm to encrypt key material during the import process.
Requests for the required public key and import token fail when they specify a different
wrapping algorithm.

The following example key policy statement uses the `kms:WrappingAlgorithm`
condition key to give the example user permission to call the
`GetParametersForImport` operation, but prevents them from using the
`RSAES_OAEP_SHA_1` wrapping algorithm. When the `WrappingAlgorithm`
in the `GetParametersForImport` request is `RSAES_OAEP_SHA_1`, the
operation fails.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:GetParametersForImport",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      **"kms:WrappingAlgorithm": "RSAES\_OAEP\_SHA\_1"**
    }
  }
}
```

**See also**

- [kms:ExpirationModel](#conditions-kms-expiration-model "#conditions-kms-expiration-model")
- [kms:ValidTo](#conditions-kms-valid-to "#conditions-kms-valid-to")
- [kms:WrappingKeySpec](#conditions-kms-wrapping-key-spec "#conditions-kms-wrapping-key-spec")

## kms:WrappingKeySpec

| AWS KMS condition keys | Condition type | Value type    | API operations           | Policy type                   |
| ---------------------- | -------------- | ------------- | ------------------------ | ----------------------------- |
| `kms:WrappingKeySpec`  | String         | Single-valued | `GetParametersForImport` | Key policies and IAM policies |

This condition key controls access to the [GetParametersForImport](../APIReference/API_GetParametersForImport.md "../APIReference/API_GetParametersForImport.md")
operation based on the value of the [WrappingKeySpec](../APIReference/API_GetParametersForImport.md#KMS-GetParametersForImport-request-WrappingKeySpec "../APIReference/API_GetParametersForImport.md#KMS-GetParametersForImport-request-WrappingKeySpec") parameter in the request. You can use this condition to require
principals to use a particular type of public key during the import process. If the request
specifies a different key type, it fails.

Because the only valid value for the `WrappingKeySpec` parameter value is
`RSA_2048`, preventing users from using this value effectively prevents them
from using the `GetParametersForImport` operation.

The following example policy statement uses the `kms:WrappingAlgorithm`
condition key to require that the `WrappingKeySpec` in the request is
`RSA_4096`.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
  },
  "Action": "kms:GetParametersForImport",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      **"kms:WrappingKeySpec": "RSA\_4096"**
    }
  }
}
```

**See also**

- [kms:ExpirationModel](#conditions-kms-expiration-model "#conditions-kms-expiration-model")
- [kms:ValidTo](#conditions-kms-valid-to "#conditions-kms-valid-to")
- [kms:WrappingAlgorithm](#conditions-kms-wrapping-algorithm "#conditions-kms-wrapping-algorithm")
