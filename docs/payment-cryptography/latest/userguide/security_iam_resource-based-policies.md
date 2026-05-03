# Resource-based policies for AWS Payment Cryptography

Resource-based policies are JSON policy documents that you attach to a resource, such as
a AWS Payment Cryptography key. In a resource-based policy, you specify who can access the key and the
actions they can perform on it. You can use resource-based policies to:

- Grant access to a single key to multiple users and roles.
- Grant access to users or roles in other AWS accounts.

###### Topics

- [Considerations](#security_iam_resource-based-policies-considerations "#security_iam_resource-based-policies-considerations")
- [Managing resource-based policies](#security_iam_resource-based-policies-manage "#security_iam_resource-based-policies-manage")
- [Resource-based policy examples](#security_iam_resource-based-policies-examples "#security_iam_resource-based-policies-examples")
  When you attach a resource-based policy to a AWS Payment Cryptography key, AWS Payment Cryptography uses the IAM
  policy evaluation logic to determine whether a given principal is authorized to perform the
  requested action. To enable cross-account access, you can specify an entire account or
  IAM entities in another account as the [principal in a
  resource-based policy](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md"). Cross-account access requires two policies:

1. _Resource-based policy (key owner's account)_ — The key
   owner uses `PutResourcePolicy` to grant access to the caller's account or
   IAM principal.
2. _Identity-based policy (caller's account)_ — The
   caller's IAM administrator must also allow the AWS Payment Cryptography action (for example,
   `payment-cryptography:EncryptData`) in the caller's IAM
   policy.
   Both policies must allow the action. If either one is missing, the cross-account request
   is denied with `AccessDeniedException`.

If a resource-based policy grants access to a principal in the same account, no
additional identity-based policy is required. For more information, see [How IAM Roles Differ from
Resource-based Policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the _IAM User Guide_.

###### Resource policy control plane operations

Resource-based policies do not apply to resource policy control plane operations such
as [`PutResourcePolicy`](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md"), [`GetResourcePolicy`](../APIReference/API_GetResourcePolicy.md "../APIReference/API_GetResourcePolicy.md"), and
[`DeleteResourcePolicy`](../APIReference/API_DeleteResourcePolicy.md "../APIReference/API_DeleteResourcePolicy.md"). This prevents potential lockout scenarios where a
resource policy could deny the ability to modify or remove the policy itself. Access to
these control plane operations is governed solely by IAM identity-based
policies.

## Considerations

Keep the following in mind when using resource-based policies with AWS Payment Cryptography.

- AWS Payment Cryptography automatically enforces no public access to keys. You cannot create a
  resource-based policy that grants access to anonymous or public principals. All
  access to AWS Payment Cryptography keys requires authenticated AWS principals, and public access
  is always blocked.
- Resource-based policies are applied per key. Each AWS Payment Cryptography key can have at
  most one resource-based policy attached to it.
- Resource-based policies do not apply to aliases. When you reference a key by
  its alias, the resource policy attached to the underlying key is evaluated.
- Resource-based policies do not apply to read-only Replica Region keys created using Multi-Region key replication
  at this time. Resource policies can only be attached to the Primary Region key.
- The `Resource` element in a resource-based policy must be
  `"*"` or exactly match the ARN of the key the policy is attached to.
  Using `"*"` is recommended because it allows the same policy document
  to be reused across multiple keys.
- Resource policy management APIs (`PutResourcePolicy`,
  `GetResourcePolicy`, and `DeleteResourcePolicy`) are
  restricted to the AWS account that owns the key. Only principals within the key
  owner's account can manage resource policies.

## Managing resource-based policies

You can manage resource-based policies for AWS Payment Cryptography keys using the AWS CLI or AWS
API. To use this command, replace the `italicized placeholder text` in the example command with your own information.

###### Attach a resource-based policy

Use the [`PutResourcePolicy`](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md") API action or the [**put-resource-policy**](../../../cli/latest/reference/payment-cryptography/put-resource-policy.md "../../../cli/latest/reference/payment-cryptography/put-resource-policy.md") CLI command to attach a
resource-based policy to a key. If a policy already exists, the command replaces
it.

The following example attaches a resource-based policy from a JSON file to a
key.

```
aws payment-cryptography put-resource-policy \
    --resource-arn arn:aws:payment-cryptography:`us-east-2`:`111122223333`:key/`kwapwa6qaifllw2h` \
    --policy file://`policy.json`
```

###### Retrieve a resource-based policy

Use the [`GetResourcePolicy`](../APIReference/API_GetResourcePolicy.md "../APIReference/API_GetResourcePolicy.md") API action or the [**get-resource-policy**](../../../cli/latest/reference/payment-cryptography/get-resource-policy.md "../../../cli/latest/reference/payment-cryptography/get-resource-policy.md") CLI command to retrieve the
resource-based policy attached to a key.

The following example retrieves the resource-based policy attached to a
key.

```
aws payment-cryptography get-resource-policy \
    --resource-arn arn:aws:payment-cryptography:`us-east-2`:`111122223333`:key/`kwapwa6qaifllw2h`
```

The response returns the policy document:

```
{
    "Policy": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::`111122223333`:role/`ExampleRole`"
                },
                "Action": [
                    "payment-cryptography:EncryptData",
                    "payment-cryptography:DecryptData"
                ],
                "Resource": "*"
            }
        ]
    }
}
```

###### Delete a resource-based policy

Use the [`DeleteResourcePolicy`](../APIReference/API_DeleteResourcePolicy.md "../APIReference/API_DeleteResourcePolicy.md") API action or the [**delete-resource-policy**](../../../cli/latest/reference/payment-cryptography/delete-resource-policy.md "../../../cli/latest/reference/payment-cryptography/delete-resource-policy.md") CLI command to remove the
resource-based policy from a key.

The following example deletes the resource-based policy attached to a
key.

```
aws payment-cryptography delete-resource-policy \
    --resource-arn arn:aws:payment-cryptography:`us-east-2`:`111122223333`:key/`kwapwa6qaifllw2h`
```

## Resource-based policy examples

### Grant cross-account access to a key

The following resource-based policy grants a role in another AWS account
permission to use a AWS Payment Cryptography key for cryptographic operations.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`111122223333`:role/`ExampleRole`"
            },
            "Action": [
                "payment-cryptography:GenerateCardValidationData",
                "payment-cryptography:VerifyCardValidationData"
            ],
            "Resource": "*"
        }
    ]
}
```

### Grant different permissions to different accounts

The following resource-based policy demonstrates how to grant different
permissions to principals in separate accounts. In this example, a 3DS Access Control
Server (ACS) in one account can generate card validation data, while a Payment
Authorization service in a different account can only validate 3DS Cryptograms.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow3DSACSToGenerate",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`111122223333`:role/`3dsAcsRole`"
            },
            "Action": [
                "payment-cryptography:GenerateCardValidationData"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowPaymentAuthToVerify",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`444455556666`:role/`PaymentAuthRole`"
            },
            "Action": [
                "payment-cryptography:VerifyAuthRequestCryptogram"
            ],
            "Resource": "*"
        }
    ]
}
```
