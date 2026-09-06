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

## Policy store aliases are not a traffic control mechanism

A policy store alias is a stable, friendly name for a policy store. It is not a mechanism for shifting, splitting, or weighting authorization traffic between policy stores. If you are familiar with features that route traffic between versions of a resource, such as Lambda aliases, note that policy store aliases don't behave the same way. By design, a policy store alias is closer to an AWS KMS key alias: it provides a durable name for a resource, not a routing layer in front of it.

For this reason, we intentionally don't provide an `UpdatePolicyStoreAlias` operation. To change the policy store that a policy store alias points to, you delete the policy store alias and create a new policy store alias that has the same name and targets a different policy store. This is not an atomic operation, and it doesn't provide the guarantees that a traffic control mechanism would.

When you change the policy store that a policy store alias resolves to, the change doesn't take effect everywhere at the same instant:

- The updated mapping must propagate from the control plane to the data plane that evaluates authorization requests. The mapping doesn't propagate instantaneously.
- Because policy store alias resolution is eventually consistent and can be cached, a transition window exists after a change. During this window, the previously associated policy store serves some requests, and the newly associated policy store serves other requests. The length of this window is indeterminate.

During this window, your application can receive authorization decisions from either policy store. Because different policy stores can contain different policies, entities, and schema, the same request can produce different decisions depending on which policy store serves it. Policy store aliases therefore can't provide an atomic cut-over between policy stores, and they aren't a substitute for a deployment or traffic-management strategy.

###### Don't use aliases as a cut-over mechanism

Don't build a higher-level infrastructure-as-code or deployment primitive that repoints a policy store alias in order to switch authorization traffic from one policy store to another. Because the change is not atomic, requests can be authorized against both policy stores at the same time for an indeterminate period. This can lead to inconsistent authorization decisions. To switch policy stores safely, see [Performing no-downtime policy store changes](#alias-no-downtime-changes "#alias-no-downtime-changes").

## Performing no-downtime policy store changes

Because policy store aliases don't provide an atomic cut-over (see [Policy store aliases are not a traffic control mechanism](#alias-not-traffic-control "#alias-not-traffic-control")), we recommend that you avoid migrating from one policy store to another by repointing a policy store alias. Instead, control the migration from within your application so that you can validate the new policy store and roll back instantly if you need to. The following approach lets you switch policy stores without downtime:

1. Create the new policy store and give it its own policy store alias, so that the current policy store and the new policy store each have a distinct, stable name. For example, keep `policy-store-alias/example-policy-store` pointing to your current policy store and create `policy-store-alias/example-policy-store-2` for the new policy store. Don't reuse or repoint a single policy store alias to perform the switch.
2. Replicate your policies, schema, and any other configuration into the new policy store, and run it in parallel with the current policy store.
3. Add a configuration value or feature flag to your application (for example, by using AppConfig) that determines which policy store alias is authoritative for authorization decisions. Don't rely on changing the alias itself to switch traffic.
4. Run the new policy store in shadow mode. Send the same `IsAuthorized` or `IsAuthorizedWithToken` request to both policy stores and compare the decisions. Record and investigate any discrepancies until the new policy store returns the decisions that you expect.
5. Use the feature flag to shift authorization decisions to the new policy store alias gradually, for example, in a phased rollout across your application hosts or user segments. Monitor authorization decisions and error rates as you proceed.
6. Use the feature flag to switch back to the original policy store alias immediately if you detect a problem. Because your application controls the switch, rollback is instant and doesn't depend on alias propagation.
7. Decommission the old policy store and its policy store alias after the new policy store is fully validated and serving all traffic.

This pattern gives your application, rather than alias propagation, control over which policy store serves each request. That control is what makes the migration safe and reversible, and it avoids the transition window that repointing a policy store alias would introduce.
