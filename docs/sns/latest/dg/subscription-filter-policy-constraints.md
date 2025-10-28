# Filter policy constraints in

Amazon SNS

When you’re setting up filter policies in Amazon SNS, there are a few important rules to
keep in mind. These rules help ensure the effective application of filter policies while
maintaining system performance and compatibility.

## Common policy

constraints

When configuring filter policies in Amazon SNS, follow these important rules to ensure
they work effectively while maintaining system performance and compatibility:

- **String matching** – For string
  matching in the filter policy, the comparison is case-sensitive.
- **Numeric matching** – For numeric
  matching, the value can range from -109 to
  109 (-1 billion to 1 billion), with five
  digits of accuracy after the decimal point.
- **Filter policy complexity** – The
  total combination of values in a filter policy must not exceed **150**. To calculate the total combination, multiply
  the number of values in each array in the filter policy.
- **Limit number of keys** – A filter
  policy can have a maximum of **five**
  keys.

###### **Additional considerations**

- The JSON of the filter policy can contain the following:
  - Strings enclosed in quotation marks
  - Numbers
  - The keywords `true`, `false`, and
    `null`, without quotation marks

- When using the Amazon SNS API, you must pass the JSON of the filter policy as a
  valid **UTF-8** string.

- The maximum size of a filter policy is **256
  KB**.
- By default, you can have up to **200** filter
  policies per topic, and **10,000** filter
  policies per AWS account.

This policy limit won't stop Amazon SQS queue subscriptions from being created
with the [`Subscribe`](../api/API_Subscribe.md "../api/API_Subscribe.md") API. However, it will fail when you
attach the filter policy in the `Subscribe` API call (or the
[`SetSubscriptionAttributes`](../api/API_SetSubscriptionAttributes.md "../api/API_SetSubscriptionAttributes.md") API call).

To increase this quota, you can use [AWS
Service Quotas](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md").

## Policy

constraints for attribute-based filtering

Attribute-based filtering is the default option. [`FilterPolicyScope`](../api/API_SetSubscriptionAttributes.md#API_SetSubscriptionAttributes_RequestParameters "../api/API_SetSubscriptionAttributes.md#API_SetSubscriptionAttributes_RequestParameters") is set to
`MessageAttributes` in the subscription.

- Amazon SNS doesn't accept a nested filter policy for attribute-based
  filtering.
- Amazon SNS compares policy properties only to message attributes that have the
  following data types:
  - `String`
  - `String.Array`

###### Important

When using attribute-based filtering in Amazon SNS, you must double-escape
certain special characters, specifically:

    + Double quotes (")
    + Backslashes ()Failure to double-escape these characters will result in the filter

policy not matching the attributes of a published message, and the
notification won't be delivered.

**Additional considerations**

- Passing objects in arrays isn't recommended because it may yield
  unexpected results due to the nesting, which isn't supported by
  attribute-based filtering. Use payload-based filtering for nested
  policies.
- `Number` is supported for numeric attribute values.
- Amazon SNS ignores message attributes with the Binary data type.

**Example policy for complexity:**

In the following policy example, the first key has **three** match operators, the second has **one** match operator, and the third has **two** match operators.

```
{
   "key_a": ["value_one", "value_two", "value_three"],
   "key_b": ["value_one"],
   "key_c": ["value_one", "value_two"]
}
```

The total combination is calculated as the product of the number of match
operators for each key in the filter policy:

```
3(match operators of key_a)
x 1(match operators of key_b)
x 2(match operators of key_c)
= 6
```

## Policy constraints

for payload-based filtering

To switch from attribute-based (default) to payload-based filtering, you must set
the [`FilterPolicyScope`](../../../AWSEC2/latest/APIReference/API_DeprovisionIpamPoolCidr.md "../../../AWSEC2/latest/APIReference/API_DeprovisionIpamPoolCidr.md") to `MessageBody` in the
subscription.

- Amazon SNS accepts a nested filter policy for payload-based filtering.
- For a nested policy, only **leaf keys** are
  counted towards the **five** key limit.

**Example policy for key limit:**

In the following policy example:

- There are two leaf keys: `key_c` and `key_e`.
- `key_c` has **four** match
  operators with a nested level of **three**, and
  `key_e` has **three** match
  operators with a nested level of **two**.

```
{
"key_a": {
    "key_b": {
        "key_c": ["value_one", "value_two", "value_three", "value_four"]
        }
    },
"key_d": {
    "key_e": ["value_one", "value_two", "value_three"]
    }
}
```

The total combination is calculated as the product of the number of match
operators and the nested level for each key in the filter policy:

```
4(match operators of key_c)
x 3(nested level of key_c)
x 3(match operators of key_e)
x 2(nested level of key_e)
= 72
```

## Wildcard pattern usage guidelines

Amazon SQS implements protections for when you register a filter policy containing wildcards
to ensure that filter policies too complex are not created,
as this would impact your application performance.

**Pattern structure**

Fields contain one or more patterns. The following example shows a
field using two patterns:

```
{
    "greeting": [
      {"anything-but": {"prefix": "Hello"}},
      {"wildcard": "H*"}
    ] // 2 patterns
  }

```

**Complexity rules**

- Total wildcard complexity across all fields must not exceed 100 points
- Maximum 3 wildcards per pattern

**Complexity calculation**

- Field complexity = `(Sum of pattern points)` × `(Number of patterns)`
- Pattern points:

Single wildcard: 1 point

Multiple wildcards: 3 points each

Anything-but: 1 point

The following is an example of the complexity calculation:

```
{
  "filename": [
    {"wildcard": "*.txt"},     // 1 point
    {"wildcard": "log*"}      // 1 point
  ]                           // Total: (1 + 1) × 2 = 4 points
}

```
