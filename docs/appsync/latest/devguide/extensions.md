# Extensions

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

`$extensions` contains a set of methods to make additional actions within
your resolvers.

**`$extensions.evictFromApiCache(String, String,
 Object) : Object`**

Evicts an item from the AWS AppSync server-side cache. The first argument
is the type name. The second argument is the field name. The third argument
is an object containing key-value pair items that specify the caching key
value. You must put the items in the object in the same order as the caching
keys in the cached resolver's `cachingKey`.

###### Note

This utility works only for mutations, not queries.

**`$extensions.setSubscriptionFilter(filterJsonObject)`**

Defines enhanced subscription filters. Each subscription notification
event is evaluated against provided subscription filters and delivers
notifications to clients if all filters evaluate to `true`. The
argument is `filterJsonObject` as described in the following
section.

###### Note

You can use this extension method only in the response mapping
templates of a subscription resolver.

**`$extensions.setSubscriptionInvalidationFilter(filterJsonObject)`**

Defines subscription invalidation filters. Subscription filters are
evaluated against the invalidation payload, then invalidate a given
subscription if the filters evaluate to `true`. The argument is
`filterJsonObject` as described in the following
section.

###### Note

You can use this extension method only in the response mapping
templates of a subscription resolver.

**`$extensions.invalidateSubscriptions(invalidationJsonObject)`**

Used to initiate a subscription invalidation from a mutation. The
argument is `invalidationJsonObject` as described in the
following section.

###### Note

This extension can be used only in the response mapping templates of
the mutation resolvers.

You can only use at most five unique
`$extensions.invalidateSubscriptions()` method calls in any
single request. If you exceed this limit, you will receive a GraphQL
error.

## Argument:

filterJsonObject

The
JSON object defines either subscription or invalidation filters. It's an array of
filters in a `filterGroup`. Each filter is a collection of individual
filters.

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

- `fieldName` – The GraphQL schema field.
- `operator` – The operator type.
- `value` – The
  values
  to compare to the subscription notification
  `fieldName` value.

The
following is an example assignment of these attributes:

```
{
 "fieldName" : "severity",
 "operator" : "le",
 "value" : $context.result.severity
}
```

### Field: fieldName

The string type `fieldName` refers to a field defined in the GraphQL
schema that matches the `fieldName` in the subscription notification
payload. When a match is found, the `value` of the GraphQL schema field is
compared to the `value` of the subscription notification filter. In the
following example, the `fieldName` filter matches the `service`
field defined in a given GraphQL type. If the notification payload contains a
`service` field with a `value` equivalent to `AWS
 AppSync`, the filter evaluates to `true`:

```
{
 "fieldName" : "service",
 "operator" : "eq",
 "value" : "AWS AppSync"
}
```

### Field: value

The value can be a different type based on the operator:

- A single number or
  Boolean
  - String examples: `"test"`, `"service"`
  - Number examples: `1`, `2`,
    `45.75`
  - Boolean examples: `true`, `false`

- Pairs of numbers or strings
  - String pair example: `["test1","test2"]`,
    `["start","end"]`
  - Number pair example: `[1,4]`, `[67,89]`,
    `[12.45, 95.45]`

- Arrays of numbers or strings
  - String array example:
    `["test1","test2","test3","test4","test5"]`
  - Number array example: `[1,2,3,4,5]`,
    `[12.11,46.13,45.09,12.54,13.89]`

### Field: operator

A case-sensitive string with the following possible values:

| Operator    | Description                                                                  | Possible value types               |
| ----------- | ---------------------------------------------------------------------------- | ---------------------------------- |
| eq          | Equal                                                                        | integer, float, string, Boolean    |
| ne          | Not equal                                                                    | integer, float, string, Boolean    |
| le          | Less than or equal                                                           | integer, float, string             |
| lt          | Less than                                                                    | integer, float, string             |
| ge          | Greater than or equal                                                        | integer, float, string             |
| gt          | Greater than                                                                 | integer, float, string             |
| contains    | Checks for a subsequence or value in the set.                                | integer, float, string             |
| notContains | Checks for the absence of a subsequence or absence<br>of a value in the set. | integer, float, string             |
| beginsWith  | Checks for a prefix.                                                         | string                             |
| in          | Checks for matching elements that are in the<br>list.                        | Array of integer, float, or string |
| notIn       | Checks for matching elements that aren't in the<br>list.                     | Array of integer, float, or string |
| between     | Between two values                                                           | integer, float, string             |
| containsAny | Contains common elements                                                     | integer, float, string             |

The following table describes how each operator is used in the subscription
notification.

eq (equal)
The `eq` operator evaluates to `true` if the
subscription notification field value matches and is strictly equal to the
filter's value. In the following example, the filter evaluates to
`true` if the subscription notification has a
`service` field with the value equivalent to `AWS
 AppSync`.

**Possible value types:** integer, float,
string, Boolean

```
{
 "fieldName" : "service",
 "operator" : "eq",
 "value" : "AWS AppSync"
}
```

ne (not equal)
The `ne` operator evaluates to `true` if the
subscription notification field value is different from the filter's value.
In the following example, the filter evaluates to `true` if the
subscription notification has a `service` field with a value
different from `AWS AppSync`.

**Possible value types:** integer, float,
string, Boolean

```
{
 "fieldName" : "service",
 "operator" : "ne",
 "value" : "AWS AppSync"
}
```

le (less or equal)
The `le` operator evaluates to `true` if the
subscription notification field value is less than or equal to the filter's
value. In the following example, the filter evaluates to `true`
if the subscription notification has a `size` field with a value
less than or equal to `5`.

**Possible value types:** integer, float,
string

```
{
 "fieldName" : "size",
 "operator" : "le",
 "value" : 5
}
```

lt (less than)
The `lt` operator evaluates to `true` if the
subscription notification field value is lower than the filter's value. In
the following example, the filter evaluates to `true` if the
subscription notification has a `size` field with a value lower
than `5`.

**Possible value types:** integer, float,
string

```
{
 "fieldName" : "size",
 "operator" : "lt",
 "value" : 5
}
```

ge (greater or equal)
The `ge` operator evaluates to `true` if the
subscription notification field value is greater than or equal to the
filter's value. In the following example, the filter evaluates to
`true` if the subscription notification has a
`size`field with a value greater than or equal to
`5`.

**Possible value types:** integer, float,
string

```
{
 "fieldName" : "size",
 "operator" : "ge",
 "value" : 5
}
```

gt (greater than)
The `gt` operator evaluates to `true` if the
subscription notification field value is greater than the filter's value. In
the following example, the filter evaluates to `true` if the
subscription notification has a `size` field with a value greater
than `5`.

**Possible value types:** integer, float,
string

```
{
 "fieldName" : "size",
 "operator" : "gt",
 "value" : 5
}
```

contains
The `contains` operator checks for a substring, subsequence,
or value in a set or single item. A filter with the `contains`
operator evaluates to `true` if the subscription notification
field value contains the filter value. In the following example, the filter
evaluates to `true` if the subscription notification has a
`seats` field with the array value containing the value
`10`.

**Possible value types:** integer, float,
string

```
{
 "fieldName" : "seats",
 "operator" : "contains",
 "value" : 10
}
```

In another example, the filter evaluates to `true` if the
subscription notification has an `event` field with
`launch` as substring.

```
{
 "fieldName" : "event",
 "operator" : "contains",
 "value" : "launch"
}
```

notContains
The `notContains` operator checks for the absence of a
substring, subsequence, or value in a set or single item. The filter with
the `notContains` operator evaluates to `true` if the
subscription notification field value doesn't contain the filter value. In
the following example, the filter evaluates to `true` if the
subscription notification has a `seats` field with the array
value not containing the value `10`.

**Possible value types:** integer, float,
string

```
{
 "fieldName" : "seats",
 "operator" : "notContains",
 "value" : 10
}
```

In another example, filter evaluates to `true` if the
subscription notification has an `event` field value without
`launch` as its subsequence.

```
{
 "fieldName" : "event",
 "operator" : "notContains",
 "value" : "launch"
}
```

beginsWith
The `beginsWith` operator checks for a prefix in a string. The
filter containing the `beginsWith` operator evaluates to
`true` if the subscription notification field value begins
with the filter's value. In the following example, the filter evaluates to
`true` if the subscription notification has a
`service` field with a value that begins with
`AWS`.

**Possible value type:** string

```
{
 "fieldName" : "service",
 "operator" : "beginsWith",
 "value" : "AWS"
}
```

in
The `in` operator checks for matching elements in an array.
The filter containing the `in` operator evaluates to
`true` if the subscription notification field value exists in
an array. In the following example, the filter evaluates to
`true` if the subscription notification has a
`severity` field with one of the values present in the array:
`[1,2,3]`.

**Possible value type:** Array of integer,
float, or string

```
{
 "fieldName" : "severity",
 "operator" : "in",
 "value" : [1,2,3]
}
```

notIn
The `notIn` operator checks for missing elements in an array.
The filter containing the `notIn` operator evaluates to
`true` if the subscription notification field value doesn't
exist in the array. In the following example, the filter evaluates to
`true` if the subscription notification has a
`severity` field with one of the values not present in the
array: `[1,2,3]`.

**Possible value type:** Array of integer,
float, or string

```
{
 "fieldName" : "severity",
 "operator" : "notIn",
 "value" : [1,2,3]
}
```

between
The `between` operator checks for values between two numbers
or strings. The filter containing the `between` operator
evaluates to `true` if the subscription notification field value
is between the filter's value pair. In the following example, the filter
evaluates to `true` if the subscription notification has a
`severity` field with values
`2`,`3`,`4`.

**Possible value types:** Pair of integer,
float, or string

```
{
 "fieldName" : "severity",
 "operator" : "between",
 "value" : [1,5]
}
```

containsAny
The `containsAny` operator checks for common elements in
arrays. A filter with the `containsAny` operator evaluates to
`true` if the intersection of the subscription notification
field set value and filter set value is non empty. In the following example,
the filter evaluates to `true` if the subscription notification
has a `seats` field with an array value containing either
`10` or `15`. This means that filter would evaluate
to `true` if the subscription notification had a
`seats` field value of `[10,11]` or
`[15,20,30]`.

**Possible value types:** integer, float, or
string

```
{
 "fieldName" : "seats",
 "operator" : "containsAny",
 "value" : [10, 15]
}
```

### AND logic

You can combine multiple filters using AND logic by defining multiple entries
within the `filters` object in the `filterGroup` array. In the
following example, filters evaluate to `true` if the subscription
notification has a `userId` field with a value equivalent to
`1` AND a `group` field value of either `Admin`
or `Developer`.

```
{
    "filterGroup": [
        {
           "filters" : [
                 {
                    "fieldName" : "userId",
                    "operator" : "eq",
                    "value" : 1
                },
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

### OR logic

You can combine multiple filters using OR logic by defining multiple filter
objects within the `filterGroup` array. In the following example, filters
evaluate to `true` if the subscription notification has a
`userId` field with a value equivalent to `1` OR a
`group` field value of either `Admin` or
`Developer`.

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

### Exceptions

Note that there are several restrictions for using filters:

- In the `filters` object, there can be a maximum of five unique
  `fieldName` items per filter. This means that you can combine a
  maximum of five individual `fieldName` objects using AND
  logic.
- There can be a maximum of twenty values for the `containsAny`
  operator.
- There can be a maximum of five values for the `in` and
  `notIn` operators.
- Each string can be a maximum of 256 characters.
- Each string comparison is case sensitive.
- Nested object filtering allows up to five nested levels of filtering.
- Each `filterGroup` can have a maximum of 10 `filters`.
  This means that you can combine a maximum of 10 `filters` using OR
  logic.
  - The `in` operator is a special case of OR logic. In the
    following example, there are two `filters`:

  ```
  {
      "filterGroup": [
          {
             "filters" : [
                   {
                      "fieldName" : "userId",
                      "operator" : "eq",
                      "value" : 1
                  },
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

  The
  preceding
  filter group is evaluated as follows and counts towards the maximum
  filters limit:

  ```
  {
      "filterGroup": [
          {
             "filters" : [
                   {
                      "fieldName" : "userId",
                      "operator" : "eq",
                      "value" : 1
                  },
                  {
                      "fieldName" : "group",
                      "operator" : "eq",
                      "value" : "Admin"
                  }
             ]
          },
          {
             "filters" : [
                   {
                      "fieldName" : "userId",
                      "operator" : "eq",
                      "value" : 1
                  },
                  {
                      "fieldName" : "group",
                      "operator" : "eq",
                      "value" : "Developer"
                  }
             ]
          }
      ]
  }
  ```

## Argument:

invalidationJsonObject

The `invalidationJsonObject` defines the following:

- `subscriptionField` – The GraphQL schema subscription to
  invalidate. A single subscription, defined as a string in the
  `subscriptionField`, is considered for invalidation.
- `payload` – A key-value pair list that's used as the input
  for invalidating subscriptions if the invalidation filter evaluates to
  `true` against their values.

The following example invalidates subscribed and connected clients using the
`onUserDelete` subscription when the invalidation filter defined in
the subscription resolver evaluates to `true` against the
`payload` value.

```
$extensions.invalidateSubscriptions({
        "subscriptionField": "onUserDelete",
        "payload": {
                "group": "Developer"
                "type" : "Full-Time"
      }
    })
```
