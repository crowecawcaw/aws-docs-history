

# String value matching

Filter messages by matching string values to message attribute values or message body property values. String values are enclosed in double quotation marks in the JSON policy. You can use the following string operations to match message attributes or message body properties:

## Exact matching
<a name="string-exact-matching"></a>

Exact matching occurs when a policy property value matches one or more message attribute values. For `String.Array` type attributes, each element in the array is treated as a separate string for matching purposes.

Consider the following policy property:

```json
"customer_interests": ["rugby", "tennis"]
```

It matches the following message attributes:

```json
"customer_interests": {"Type": "String", "Value": "rugby"}
```

```json
"customer_interests": {"Type": "String", "Value": "tennis"}
```

```json
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\", \"tennis\"]"}
```

It also matches the following message bodies:

```json
{
   "customer_interests": "rugby"
}
```

```json
{
   "customer_interests": "tennis"
}
```

However, it doesn't match the following message attributes:

```json
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```json
"customer_interests": {"Type": "String.Array", "Value": "[\"baseball\"]"}
```

Nor does it match the following message body:

```json
{
   "customer_interests": "baseball"
}
```

## Anything-but matching
<a name="string-anything-but-matching"></a>

When a policy property value includes the keyword `anything-but`, it matches any message attribute or message body values that *don't* include any of the policy property values. `anything-but` can be combined with `"exists": false`. For `String.Array` type attributes, it matches if none of the array elements are listed in the policy property.

Consider the following policy property:

```json
"customer_interests": [{"anything-but": ["rugby", "tennis"]}]
```

It matches any of the following message attributes:

```json
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```json
"customer_interests": {"Type": "String", "Value": "football"}
```

```json
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\", \"baseball\"]"}
```

It also matches either of the following message bodies:

```json
{
   "customer_interests": "baseball"
}
```

```json
{
   "customer_interests": "football"
}
```

Moreover, it matches the following message attribute (because it contains a value that *isn't* `rugby` or `tennis`):

```json
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\", \"baseball\"]"}
```

And it also matches the following message body (because it contains a value that isn't `rugby` or `tennis`):

```json
{
   "customer_interests": ["rugby", "baseball"]
}
```

However, it doesn't match the following message attributes:

```json
"customer_interests": {"Type": "String", "Value": "rugby"}
```

```json
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\"]"}
```

Nor does it match the following message body:

```json
{
   "customer_interests": ["rugby"]
}
```

**Using a prefix with `anything-but`**

For string matching, you can also use a prefix with the `anything-but` operator. For example, the following policy property denies the `order-` prefix:

```json
"event":[{"anything-but": {"prefix": "order-"}}]
```

It matches either of the following attributes:

```json
"event": {"Type": "String", "Value": "data-entry"}
```

```json
"event": {"Type": "String", "Value": "order_number"}
```

It also matches either of the following message bodies:

```json
{
   "event": "data-entry"
}
```

```json
{
   "event": "order_number"
}
```

However, it doesn't match the following message attribute:

```json
"event": {"Type": "String", "Value": "order-cancelled"}
```

Nor does it match the following message body:

```json
{
   "event": "order-cancelled"
}
```

**anything-but wildcard**

The following policy property denies the `*ball` wildcard:

```json
"customer_interests" : [{ "anything-but": { "wildcard": "*ball" }}]
```

It matches the following attributes:

```json
{"customer_interests": ["hockey", "rugby", "soccer] }
```

However, it does not match the following message attribute:

```json
{"customer_interests": ["baseball", "basketball"] }
```

**anything-but suffix** 

The following policy property denies the `-ball`

 suffix:

```json
"customer_interests": [ { "anything-but": { "suffix": "ball" } } ]
```

It matches the following attributes:

```json
{"customer_interests": ["hockey", "rugby", "soccer] }
```

However, it does not match the following message attribute:

```json
 {"customer_interests": ["baseball", "basketball"] }
```

## Equals-ignore-case matching
<a name="string-equals-ignore"></a>

When a policy property includes the keyword `equals-ignore-case`, it will perform a case-insensitive match with any message attribute or body property value.

Consider the following policy property:

```json
"customer_interests": [{"equals-ignore-case": "tennis"}]
```

It matches either of the following message attributes:

```json
"customer_interests": {"Type": "String", "Value": "TENNIS"}
```

```json
"customer_interests": {"Type": "String", "Value": "Tennis"}
```

It also matches either of the following message bodies:

```json
{
    "customer_interests": "TENNIS"
}
```

```json
{
    "customer_interests": "teNnis"
{
```

## IP address matching
<a name="string-address-matching"></a>

You can use the `cidr` operator to check whether an incoming message originates from a specific IP address or subnet. 

Consider the following policy property:

```json
"source_ip":[{"cidr": "10.0.0.0/24"}]
```

It matches either of the following message attributes:

```json
"source_ip": {"Type": "String", "Value": "10.0.0.0"}
```

```json
"source_ip": {"Type": "String", "Value": "10.0.0.255"}
```

It also matches either of the following message bodies:

```json
{
   "source_ip": "10.0.0.0"
}
```

```json
{
   "source_ip": "10.0.0.255"
}
```

However, it doesn't match the following message attribute:

```json
"source_ip": {"Type": "String", "Value": "10.1.1.0"}
```

Nor does it match the following message body:

```json
{
   "source_ip": "10.1.1.0"
}
```

## Prefix matching
<a name="string-prefix-matching"></a>

When a policy property includes the keyword `prefix`, it matches any message attribute or body property values that begin with the specified characters.

Consider the following policy property:

```json
"customer_interests": [{"prefix": "bas"}]
```

It matches either of the following message attributes:

```json
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```json
"customer_interests": {"Type": "String", "Value": "basketball"}
```

It also matches either of the following message bodies:

```json
{
   "customer_interests": "baseball"
}
```

```json
{
   "customer_interests": "basketball"
}
```

However, it doesn't match the following message attribute:

```json
"customer_interests": {"Type": "String", "Value": "rugby"}
```

Nor does it match the following message body:

```json
{
   "customer_interests": "rugby"
}
```

## Suffix matching
<a name="string-suffix-matching"></a>

When a policy property includes the keyword `suffix`, it matches any message attribute or body property values that end with the specified characters.

Consider the following policy property:

```json
"customer_interests": [{"suffix": "ball"}]
```

It matches either of the following message attributes:

```json
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```json
"customer_interests": {"Type": "String", "Value": "basketball"}
```

It also matches either of the following message bodies:

```json
{
    "customer_interests": "baseball"
}
```

```json
{
    "customer_interests": "basketball"
}
```

However, it doesn't match the following message attribute:

```json
"customer_interests": {"Type": "String", "Value": "rugby"}
```

Nor does it match the following message body:

```json
{
    "customer_interests": "rugby"
}
```

## Wildcard
<a name="string-value-wildcard"></a>

 You can use the wildcard character (\*) to match string values in event patterns. 

The following policy uses the wildcard (\*) character:

```json
"customer_interests": [ { "wildcard": "*ball" } ]
```

It matches the following attributes:

```json
{"customer_interests": ["baseball", "basketball"] }
```