

# Extensions
<a name="extensions-js"></a>

`extensions` contains a set of methods to make additional actions within your resolvers.

## Caching extensions
<a name="caching-extensions-js-list"></a>

**`extensions.evictFromApiCache(typeName: string, fieldName: string, keyValuePair: Record<string, any>) : Object`**  
Evicts an item from the AWS AppSync server-side cache. The first argument is the type name. The second argument is the field name. The third argument is an object containing key-value pair items that specify the caching key value. You must put the items in the object in the same order as the caching keys in the cached resolver's `cachingKey`. For more information about caching, see [Caching behavior](https://docs.aws.amazon.com/appsync/latest/devguide/enabling-caching.html#caching-behavior).  
**Example 1:**  
This example evicts the items that were cached for a resolver called `Query.allClasses` on which a caching key called `context.arguments.semester` was used. When the mutation is called and the resolver runs, if an entry is successfully cleared, then the response contains an `apiCacheEntriesDeleted` value in the extensions object that shows how many entries were deleted.  

```
import { util, extensions } from '@aws-appsync/utils';

export const request = (ctx) => ({ payload: null });

export function response(ctx) {
	extensions.evictFromApiCache('Query', 'allClasses', {
		'context.arguments.semester': ctx.args.semester,
	});
	return null;
}
```
This function **only** works for mutations, not queries.

## Subscription extensions
<a name="subscription-extensions-js-list"></a>

**`extensions.setSubscriptionFilter(filterJsonObject)`**  
Defines enhanced subscription filters. Each subscription notification event is evaluated against provided subscription filters and delivers notifications to clients if all filters evaluate to `true`. The argument is `filterJsonObject` (More information about this argument can be found below in the *Argument: filterJsonObject* section.). See [Enhanced subscription filtering](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-enhanced-filtering.html).  
You can use this extension function only in the response handler of a subscription resolver. Also, we recommend using `util.transform.toSubscriptionFilter` to create your filter.

**`extensions.setSubscriptionInvalidationFilter(filterJsonObject)`**  
Defines subscription invalidation filters. Subscription filters are evaluated against the invalidation payload, then invalidate a given subscription if the filters evaluate to `true`. The argument is `filterJsonObject` (More information about this argument can be found below in the *Argument: filterJsonObject* section.). See [Enhanced subscription filtering](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-enhanced-filtering.html).  
You can use this extension function only in the response handler of a subscription resolver. Also, we recommend using `util.transform.toSubscriptionFilter` to create your filter.

**`extensions.invalidateSubscriptions(invalidationJsonObject)`**  
Used to initiate a subscription invalidation from a mutation. The argument is `invalidationJsonObject` (More information about this argument can be found below in the *Argument: invalidationJsonObject* section.).  
This extension can be used only in the response mapping templates of the mutation resolvers.  
You can only use at most five unique `extensions.invalidateSubscriptions()` method calls in any single request. If you exceed this limit, you will receive a GraphQL error.

## Argument: filterJsonObject
<a name="extensions-filterJsonObject-js"></a>

The JSON object defines either subscription or invalidation filters. It's an array of filters in a `filterGroup`. Each filter is a collection of individual filters.

```
{
    "filterGroup": [
        {
           "filters" : [
                 {
                    "fieldName" : "userId",
                    "operator" : "eq",
                    "value" : 1
                }
           ]
           
        },
        {
           "filters" : [
                {
                    "fieldName" : "group",
                    "operator" : "in",
                    "value" : ["Admin", "Developer"]
                }
           ]
           
        }
    ]
}
```

Each filter has three attributes: 
+ `fieldName` – The GraphQL schema field.
+ `operator` – The operator type.
+ `value` – The values to compare to the subscription notification `fieldName` value.

The following is an example assignment of these attributes:

```
{
 "fieldName" : "severity",
 "operator" : "le",
 "value" : context.result.severity
}
```

## Argument: invalidationJsonObject
<a name="extensions-invalidationJsonObject-js"></a>

The `invalidationJsonObject` defines the following:
+ `subscriptionField` – The GraphQL schema subscription to invalidate. A single subscription, defined as a string in the `subscriptionField`, is considered for invalidation.
+ `payload` – A key-value pair list that's used as the input for invalidating subscriptions if the invalidation filter evaluates to `true` against their values.

  The following example invalidates subscribed and connected clients using the `onUserDelete` subscription when the invalidation filter defined in the subscription resolver evaluates to `true` against the `payload` value.

  ```
  export const request = (ctx) => ({ payload: null });
  
  export function response(ctx) {
  	extensions.invalidateSubscriptions({
  		subscriptionField: 'onUserDelete',
  		payload: { group: 'Developer', type: 'Full-Time' },
  	});
  	return ctx.result;
  }
  ```