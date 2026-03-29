# Using Amazon Verified Permissions policy store aliases in API operations

Any Amazon Verified Permissions operation that accepts a `policyStoreId` parameter, such as
[IsAuthorized](../apireference/API_IsAuthorized.md "../apireference/API_IsAuthorized.md"),
[IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md"), and
[GetPolicyStore](../apireference/API_GetPolicyStore.md "../apireference/API_GetPolicyStore.md"), can accept a policy store alias name in place of the policy store ID.

###### Important

When you use a policy store alias as the value of a `policyStoreId` parameter, you must include the `policy-store-alias/` prefix. For example, use `policy-store-alias/example-policy-store`, not `example-policy-store`.

## Using Policy store aliases in Operations

The following `IsAuthorized` command uses a policy store alias with the name
`example-policy-store` to identify a policy store.

AWS CLI

```
`$` `aws verifiedpermissions is-authorized \
 --policy-store-id policy-store-alias/example-policy-store \
 --principal entityType=User,entityId=alice \
 --action actionType=Action,actionId=view \
 --resource entityType=Photo,entityId=photo123`
```

###### Note

You cannot use a policy store alias in place of the `policyStoreId` field for the
[DeletePolicyStore](../apireference/API_DeletePolicyStore.md "../apireference/API_DeletePolicyStore.md") operation.

## Using Policy store aliases Across AWS Regions

One of the most powerful uses of aliases is in applications that run in multiple
AWS Regions. For example, you might have a global application that uses different policy stores in each Region.

- In us-east-1, you want to use `PSEXAMPLEabcdefg111111`.
- In eu-west-1, you want to use `PSEXAMPLEabcdefg222222`.

You could create a different version of your application in each Region or use a
dictionary or switch statement to select the right policy store for each Region. But it's much
easier to create a policy store alias with the same policy store alias name in each Region. Remember that the policy store alias
name is case-sensitive.

AWS CLI

```
`$` `aws --region us-east-1 verifiedpermissions create-policy-store-alias \
 --alias-name policy-store-alias/my-app \
 --policy-store-id PSEXAMPLEabcdefg111111`

`$` `aws --region eu-west-1 verifiedpermissions create-policy-store-alias \
 --alias-name policy-store-alias/my-app \
 --policy-store-id PSEXAMPLEabcdefg222222`
```

Then, use the policy store alias in your code. When your code runs in each Region, the policy store alias will refer
to its associated policy store in that Region.

AWS CLI

```
`$` `aws verifiedpermissions is-authorized \
 --policy-store-id policy-store-alias/my-app \
 --principal entityType=User,entityId=alice \
 --action actionType=Action,actionId=view \
 --resource entityType=Photo,entityId=photo123`
```

However, there is a risk that the policy store alias might be deleted. In that case, the application's attempts to
use the policy store alias name will fail, and you might need to recreate or update the policy store alias. To mitigate this risk, be cautious about giving principals permission to manage the
policy store aliases that you use in your application.
