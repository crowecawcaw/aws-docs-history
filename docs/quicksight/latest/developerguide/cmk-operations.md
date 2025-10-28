# Key management operations

Use Quick Sight key management APIs to list and update customer managed keys (CMKs) that are registered to a Quick Sight account. For more information about key management in Quick Sight, see [Key management](../user/key-management.md "../user/key-management.md") in the Quick Sight User Guide.

**Permissons**

Before you begin, create or update an IAM role that contains a user permission to access and use all CMKs that are registered to your Quick Sight account. At minimum, the IAM policy must contain the `kms:CreateGrant`, `quicksight:UpdateKeyRegistration`, and `quicksight:DescribeKeyRegistration` permissions. To see a list of IAM policy examples that can be used to grant different degrees of access to the CMKs in a account, see [IAM identity-based policies for Amazon Quick Sight: using the admin key management console](../user/iam-policy-examples.md#security_iam_id-based-policy-examples-admin-key-management-console "../user/iam-policy-examples.md#security_iam_id-based-policy-examples-admin-key-management-console").

## CMK API Examples

The example below lists all customer managed keys that are registered to a Quick Sight account.

```
aws quicksight describe-key-registration \
--aws-account-id `AWSACCOUNTID` \
--region `REGION`
```

The example below updates a CMK registration and designates a default key.

```
aws quicksight update-key-registration \
--aws-account-id `AWSACCOUNTID` \
--key-registration '[{"KeyArn": "`KEYARN`", "DefaultKey": true}]'
--region `REGION`
```

The example below updates the registration of two CMKs in a Quick Sight account and designates one of the two updated keys as the new default key.

```
aws quicksight update-key-registration \
--aws-account-id `AWSACCOUNTID` \
--key-registration '[{"KeyArn": "`KEYARN`", "DefaultKey": true}, {"KeyArn": "`KEYARN`", "DefaultKey": false}]'
--region `REGION`
```

The example below clears all CMK registrations from a Quick Sight account. Instead, Quick Sight uses AWS owned keys to encrypt your resources.

```
aws quicksight update-key-registration \
--aws-account-id `AWSACCOUNTID` \
--key-registration '[]'
--region `REGION`
```
