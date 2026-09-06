

# Creating grants
<a name="create-grant-overview"></a>

Before creating a grant, learn about the options for customizing your grant. You can use *grant constraints* to limit the permissions in the grant. Also, learn about granting `CreateGrant` permission. Principals who get permission to create grants from a grant are limited in the grants that they can create.

**Topics**
+ [Creating a grant](#grant-create)
+ [Granting CreateGrant permission](#grant-creategrant)

## Creating a grant
<a name="grant-create"></a>

To create a grant, call the [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) operation. Specify a KMS key, a list of allowed [grant operations](grants.md#terms-grant-operations), and either a [grantee principal](grants.md#terms-grantee-principal) or a [grantee service principal](grants.md#terms-grantee-service-principal).

When you specify a **grantee principal**, you can optionally designate a [retiring principal](grants.md#terms-retiring-principal) or [retiring service principal](grants.md#terms-retiring-service-principal), and use the `Constraints` parameter to define [grant constraints](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html). When you specify a **grantee service principal**, you must include a [`SourceArn` grant constraint](#terms-source-arn-constraint). You must also specify either a `RetiringServicePrincipal` or a `RetiringPrincipal`.

When you create, retire, or revoke a grant, there might be a brief delay, usually less than five minutes, before the change is available throughout AWS KMS. For more information, see [Eventual consistency (for grants)](grants.md#terms-eventual-consistency).

For example, the following `CreateGrant` command creates a grant that allows users who are authorized to assume the `keyUserRole` role to call the [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation on the specified [symmetric KMS key](symm-asymm-choose-key-spec.md#symmetric-cmks). The grant uses the `RetiringPrincipal` parameter to designate a principal that can retire the grant. It also includes a grant constraint that allows the permission only when the [encryption context](encrypt_context.md) in the request includes `"Department": "IT"`.

```
$  aws kms create-grant \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-principal arn:aws:iam::111122223333:role/keyUserRole \
    --operations Decrypt \
    --retiring-principal arn:aws:iam::111122223333:role/adminRole \
    --constraints EncryptionContextSubset={Department=IT}
```

If your code retries the `CreateGrant` operation, or uses an [AWS SDK that automatically retries requests](https://docs.aws.amazon.com/general/latest/gr/api-retries.html), use the optional [Name](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html#KMS-CreateGrant-request-Name) parameter to prevent the creation of duplicate grants. If AWS KMS gets a `CreateGrant` request for a grant with the same properties as an existing grant, including the name, it recognizes the request as a retry, and does not create a new grant. You cannot use the `Name` value to identify the grant in any AWS KMS operations.

**Important**  
Do not include confidential or sensitive information in the grant name. It may appear in plain text in CloudTrail logs and other output.

```
$ aws kms create-grant \
    --name IT-1234abcd-keyUserRole-decrypt \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-principal arn:aws:iam::111122223333:role/keyUserRole \
    --operations Decrypt \
    --retiring-principal arn:aws:iam::111122223333:role/adminRole \
    --constraints EncryptionContextSubset={Department=IT}
```

For code examples that demonstrate how to create grants in several programming languages, see [Use `CreateGrant` with an AWS SDK or CLI](example_kms_CreateGrant_section.md).

### Using grant constraints
<a name="grant-constraints"></a>

[Grant constraints](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html) set conditions on the permissions that the grant gives to the grantee principal. Grant constraints take the place of [condition keys](policy-conditions.md) in a [key policy](key-policies.md) or [IAM policy](iam-policies.md).

**Important**  
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

AWS KMS supports two types of grant constraints: encryption context constraints and the `SourceArn` constraint.

#### Encryption context constraints
<a name="grant-constraints-ec"></a>

Encryption context constraints establish requirements for the [encryption context](encrypt_context.md) in a request for a cryptographic operation. Each encryption context grant constraint value can include up to 8 encryption context pairs. The encryption context value in each constraint cannot exceed 384 characters.
+ Encryption context constraints are valid only in a grant for a symmetric encryption KMS key. Cryptographic operations with other KMS keys don't support an encryption context. 
+ The encryption context constraint is ignored for `DescribeKey` and `RetireGrant` operations. `DescribeKey` and `RetireGrant` don't have an encryption context parameter, but you can include these operations in a grant that has an encryption context constraint.
+ You can use an encryption context constraint in a grant for the `CreateGrant` operation. The encryption context constraint requires that any grants created with the `CreateGrant` permission have an equally strict or stricter encryption context constraint.

AWS KMS supports two encryption context grant constraints.

**EncryptionContextEquals**  
Use `EncryptionContextEquals` to specify the exact encryption context for permitted requests.   
`EncryptionContextEquals` requires that the encryption context pairs in the request are an exact, case-sensitive match for the encryption context pairs in the grant constraint. The pairs can appear in any order, but the keys and values in each pair cannot vary.   
For example, if the `EncryptionContextEquals` grant constraint requires the `"Department": "IT"` encryption context pair, the grant allows requests of the specified type only when the encryption context in the request is exactly `"Department": "IT"`.

**EncryptionContextSubset**  
Use `EncryptionContextSubset` to require that requests include particular encryption context pairs.  
`EncryptionContextSubset` requires that the request include all encryption context pairs in the grant constraint (an exact, case-sensitive match), but the request can also have additional encryption context pairs. The pairs can appear in any order, but the keys and values in each pair cannot vary.   
For example, if the `EncryptionContextSubset` grant constraint requires the `Department=IT` encryption context pair, the grant allows requests of the specified type when the encryption context in the request is `"Department": "IT"`, or includes `"Department": "IT"` along with other encryption context pairs, such as `"Department": "IT","Purpose": "Test"`.

To specify an encryption context constraint in a grant for a symmetric encryption KMS key, use the `Constraints` parameter in the [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) operation. The grant that this command creates gives users who are authorized to assume the `keyUserRole` role permission to call the [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation. But that permission is effective only when the encryption context in the `Decrypt` request is a `"Department": "IT"` encryption context pair.

```
$ aws kms create-grant \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-principal arn:aws:iam::111122223333:role/keyUserRole \
    --operations Decrypt \
    --retiring-principal arn:aws:iam::111122223333:role/adminRole \
    --constraints EncryptionContextEquals={Department=IT}
```

The resulting grant looks like the following one. Notice that the permission granted to the `keyUserRole` role is effective only when the `Decrypt` request uses the same encryption context pair specified in the grant constraint. To find the grants on a KMS key, use the [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html) operation.

```
$ aws kms list-grants --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
{
    "Grants": [
        {
            "Name": "",
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "GrantId": "abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514a",
            "Operations": [
                "Decrypt"
            ],
            "GranteePrincipal": "arn:aws:iam::111122223333:role/keyUserRole",
            "Constraints": {
                "EncryptionContextEquals": {
                    "Department": "IT"
                }
            },
            "CreationDate": 1568565290.0,
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "RetiringPrincipal": "arn:aws:iam::111122223333:role/adminRole"
        }
    ]
}
```

To satisfy the `EncryptionContextEquals` grant constraint, the encryption context in the request for the `Decrypt` operation must be a `"Department": "IT"` pair. A request like the following from the grantee principal would satisfy the `EncryptionContextEquals` grant constraint.

```
$ aws kms decrypt \
    --key-id arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\
    --ciphertext-blob fileb://encrypted_msg \
    --encryption-context Department=IT
```

When the grant constraint is `EncryptionContextSubset`, the encryption context pairs in the request must include the encryption context pairs in the grant constraint, but the request can also include other encryption context pairs. The following grant constraint requires that one of encryption context pairs in the request is `"Deparment": "IT"`.

```
"Constraints": {
   "EncryptionContextSubset": {
       "Department": "IT"
   }
}
```

The following request from the grantee principal would satisfy both of the `EncryptionContextEqual` and `EncryptionContextSubset` grant constraints in this example.

```
$ aws kms decrypt \
    --key-id arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab \
    --ciphertext-blob fileb://encrypted_msg \
    --encryption-context Department=IT
```

However, a request like the following from the grantee principal would satisfy the `EncryptionContextSubset` grant constraint, but it would fail the `EncryptionContextEquals` grant constraint.

```
$ aws kms decrypt \
    --key-id arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab \
    --ciphertext-blob fileb://encrypted_msg \
    --encryption-context Department=IT,Purpose=Test
```

AWS services often use encryption context constraints in the grants that give them permission to use KMS keys in your AWS account. For example, Amazon DynamoDB uses a grant like the following one to get permission to use the [AWS managed key](concepts.md#aws-managed-key) for DynamoDB in your account. The `EncryptionContextSubset` grant constraint in this grant makes the permissions in the grant effective only when the encryption context in the request includes `"subscriberID": "111122223333"` and `"tableName": "Services"` pairs. This grant constraint means that the grant allows DynamoDB to use the specified KMS key only for a particular table in your AWS account.

To get this output, run the [ListGrants](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html) operation on the AWS managed key for DynamoDB in your account.

```
$ aws kms list-grants --key-id 0987dcba-09fe-87dc-65ba-ab0987654321

{
    "Grants": [
        {
            "Operations": [
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "ReEncryptFrom",
                "ReEncryptTo",
                "RetireGrant",
                "DescribeKey"
            ],
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "Constraints": {
                "EncryptionContextSubset": {
                    "aws:dynamodb:tableName": "Services",
                    "aws:dynamodb:subscriberId": "111122223333"
                }
            },
            "CreationDate": 1518567315.0,
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321",
            "GranteePrincipal": "dynamodb.us-west-2.amazonaws.com",
            "RetiringPrincipal": "dynamodb.us-west-2.amazonaws.com",
            "Name": "8276b9a6-6cf0-46f1-b2f0-7993a7f8c89a",
            "GrantId": "1667b97d27cf748cf05b487217dd4179526c949d14fb3903858e25193253fe59"
        }
    ]
}
```

#### SourceArn constraint
<a name="grant-constraints-source-arn"></a>

**SourceArn**  <a name="terms-source-arn-constraint"></a>
The `SourceArn` constraint restricts grant permissions to requests made on behalf of a specific AWS resource, identified by its Amazon Resource Name (ARN). The `SourceArn` grant constraint is effectively putting an [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) global condition key into the grant and is only evaluated when the request is made by an AWS service.  
The `SourceArn` constraint is always required when the grant specifies a `GranteeServicePrincipal`. It can optionally be used with `GranteePrincipal`.   
Unlike encryption context constraints, the `SourceArn` constraint is supported on grants for *all types* of KMS keys.

To specify a `SourceArn` constraint in a grant, use the `Constraints` parameter in the [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) operation. The following example creates a grant that allows an AWS service principal to call the `Encrypt` and `Decrypt` operations, but only when the request is made on behalf of the specified DynamoDB table. The `SourceArn` constraint is required when the grant specifies a `GranteeServicePrincipal`.

```
$ aws kms create-grant \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-service-principal {{service-name}}.amazonaws.com \
    --operations Encrypt Decrypt \
    --retiring-service-principal {{service-name}}.amazonaws.com \
    --constraints '{"SourceArn":"arn:aws:dynamodb:us-east-1:111122223333:table/ExampleTable"}'
```

The resulting grant looks like the following. The permissions in the grant are effective only when the request includes a source ARN that matches the `SourceArn` value in the grant constraint.

```
$ aws kms list-grants --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
{
    "Grants": [
        {
            "Name": "",
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "GrantId": "abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514a",
            "Operations": [
                "Encrypt",
                "Decrypt"
            ],
            "GranteeServicePrincipal": "{{service-name}}.amazonaws.com",
            "Constraints": {
                "SourceArn": "arn:aws:dynamodb:us-east-1:111122223333:table/ExampleTable"
            },
            "CreationDate": 1718567315.0,
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "RetiringServicePrincipal": "{{service-name}}.amazonaws.com"
        }
    ]
}
```

You can also combine multiple constraints in a single grant. However, you can specify either `EncryptionContextEquals` or `EncryptionContextSubset`, but not both. 

When `GranteeServicePrincipal` is specified, the `SourceArn` constraint is required, so the valid combinations to create grant with multiple constraints are:
+ `EncryptionContextEquals` with `SourceArn`
+ `EncryptionContextSubset` with `SourceArn`

The following example creates a grant with `GranteeServicePrincipal` and `RetiringServicePrincipal`, and includes both an `EncryptionContextSubset` constraint and a `SourceArn` constraint.

```
$ aws kms create-grant \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-service-principal {{service-name}}.amazonaws.com \
    --retiring-service-principal {{service-name}}.amazonaws.com \
    --operations Encrypt Decrypt GenerateDataKey DescribeKey \
    --constraints '{"EncryptionContextSubset":{"Department":"IT"},"SourceArn":"arn:aws:dynamodb:us-east-1:111122223333:table/ExampleTable"}'
```

The resulting grant looks like the following. Notice that the response includes `GranteeServicePrincipal` and `RetiringServicePrincipal` fields, and the `Constraints` field contains both `EncryptionContextSubset` and `SourceArn`.

```
$ aws kms list-grants --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
{
    "Grants": [
        {
            "Name": "",
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "GrantId": "abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514a",
            "Operations": [
                "Encrypt",
                "Decrypt",
                "GenerateDataKey",
                "DescribeKey"
            ],
            "GranteeServicePrincipal": "{{service-name}}.amazonaws.com",
            "Constraints": {
                "EncryptionContextSubset": {
                    "Department": "IT"
                },
                "SourceArn": "arn:aws:dynamodb:us-east-1:111122223333:table/ExampleTable"
            },
            "CreationDate": 1718567315.0,
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "RetiringServicePrincipal": "{{service-name}}.amazonaws.com"
        }
    ]
}
```

## Granting CreateGrant permission
<a name="grant-creategrant"></a>

A grant can include permission to call the `CreateGrant` operation. But when a [grantee principal](grants.md#terms-grantee-principal) gets permission to call `CreateGrant` from a grant, rather than from a policy, that permission is limited. 
+ The grantee principal can only create grants that allow some or all of the operations in the parent grant.
+ The [grant constraints](#grant-constraints) in the grants they create must be at least as strict as those in the parent grant.

These limitations don't apply to principals who get `CreateGrant` permission from a policy, although their permissions can be limited by [policy conditions](grant-authorization.md).

For example, consider a grant that allows the grantee principal to call the `GenerateDataKey`, `Decrypt`, and `CreateGrant` operations. We call a grant that allow `CreateGrant` permission a *parent grant*.

```
# The original grant in a ListGrants response.
{
    "Grants": [
        {
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "CreationDate": 1572216195.0,
            "GrantId": "abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514a",
            "Operations": [
                "GenerateDataKey",
                "Decrypt",
                "CreateGrant
            ]
            "RetiringPrincipal": "arn:aws:iam::111122223333:role/adminRole",
            "Name": "",
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "GranteePrincipal": "arn:aws:iam::111122223333:role/keyUserRole",
            "Constraints": {
                "EncryptionContextSubset": {
                    "Department": "IT"
                }
            },
        }
    ]
}
```

The grantee principal, exampleUser, can use this permission to create a grant that includes any subset of the operations specified in the original grant, such as `CreateGrant` and `Decrypt`. The *child grant* cannot include other operations, such as `ScheduleKeyDeletion` or `ReEncrypt`.

Also, the [grant constraints](https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantConstraints.html) in child grants must be as restrictive or more restrictive than those in the parent grant. For example, the child grant can add pairs to an `EncryptionContextSubset` constraint in the parent grant, but it cannot remove them. The child grant can change an `EncryptionContextSubset` constraint to an `EncryptionContextEquals` constraint, but not the reverse.

IAM best practices discourage the use of IAM users with long-term credentials. Whenever possible, use IAM roles, which provide temporary credentials. For details, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

For example, the grantee principal can use the `CreateGrant` permission that it got from the parent grant to create the following child grant. The operations in the child grant are a subset of the operations in the parent grant and the grant constraints are more restrictive.

```
# The child grant in a ListGrants response.
{
    "Grants": [
        {
            "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "CreationDate": 1572249600.0,
            "GrantId": "fedcba9999c1e2e9876abcde6e9d6c9b6a1987650000abcee009abcdef40183f",
            "Operations": [
                "CreateGrant"
                "Decrypt"
            ]
            "RetiringPrincipal": "arn:aws:iam::111122223333:user/exampleUser",
            "Name": "",
            "IssuingAccount": "arn:aws:iam::111122223333:root",
            "GranteePrincipal": "arn:aws:iam::111122223333:user/anotherUser",
            "Constraints": {
                "EncryptionContextEquals": {
                    "Department": "IT"
                }
            },
        }
    ]
}
```

The grantee principal in the child grant, `anotherUser`, can use their `CreateGrant` permission to create grants. However, the grants that `anotherUser` creates must include the operations in its parent grant or a subset, and the grant constraints must be the same or stricter. 