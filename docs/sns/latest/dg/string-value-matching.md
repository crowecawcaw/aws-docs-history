# String value matching

Filter messages by matching string values to message attribute values or
message body property values. String values are enclosed in double quotation marks in
the JSON policy. You can use the following string operations to match message attributes
or message body properties:

## Exact matching

Exact matching occurs when a policy property value matches one or more message
attribute values. For `String.Array` type attributes, each element in the
array is treated as a separate string for matching purposes.

Consider the following policy property:

```
"customer_interests": ["rugby", "tennis"]
```

It matches the following message attributes:

```
"customer_interests": {"Type": "String", "Value": "rugby"}
```

```
"customer_interests": {"Type": "String", "Value": "tennis"}
```

```
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\", \"tennis\"]"}
```

It also matches the following message bodies:

```
{
   "customer_interests": "rugby"
}
```

```
{
   "customer_interests": "tennis"
}
```

However, it doesn't match the following message attributes:

```
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```
"customer_interests": {"Type": "String.Array", "Value": "[\"baseball\"]"}
```

Nor does it match the following message body:

```
{
   "customer_interests": "baseball"
}
```

## Anything-but matching

When a policy property value includes the keyword `anything-but`, it
matches any message attribute or message body values that _don't_ include any of the policy property values.
`anything-but` can be combined with `"exists": false`. For
`String.Array` type attributes, it matches if none of the array
elements are listed in the policy property.

Consider the following policy property:

```
"customer_interests": [{"anything-but": ["rugby", "tennis"]}]
```

It matches any of the following message attributes:

```
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```
"customer_interests": {"Type": "String", "Value": "football"}
```

```
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\", \"baseball\"]"}
```

It also matches either of the following message bodies:

```
{
   "customer_interests": "baseball"
}
```

```
{
   "customer_interests": "football"
}
```

Moreover, it matches the following message attribute (because it contains a value
that _isn't_
`rugby` or `tennis`):

```
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\", \"baseball\"]"}
```

And it also matches the following message body (because it contains a value that
isn't `rugby` or `tennis`):

```
{
   "customer_interests": ["rugby", "baseball"]
}
```

However, it doesn't match the following message attributes:

```
"customer_interests": {"Type": "String", "Value": "rugby"}
```

```
"customer_interests": {"Type": "String.Array", "Value": "[\"rugby\"]"}
```

Nor does it match the following message body:

```
{
   "customer_interests": ["rugby"]
}
```

**Using a prefix with `anything-but`**

For string matching, you can also use a prefix with the `anything-but`
operator. For example, the following policy property denies the `order-`
prefix:

```
"event":[{"anything-but": {"prefix": "order-"}}]
```

It matches either of the following attributes:

```
"event": {"Type": "String", "Value": "data-entry"}
```

```
"event": {"Type": "String", "Value": "order_number"}
```

It also matches either of the following message bodies:

```
{
   "event": "data-entry"
}
```

```
{
   "event": "order_number"
}
```

However, it doesn't match the following message attribute:

```
"event": {"Type": "String", "Value": "order-cancelled"}
```

Nor does it match the following message body:

```
{
   "event": "order-cancelled"
}
```

**anything-but wildcard**

The following policy property denies the `*ball`
wildcard:

```
"customer_interests" : [{ "anything-but": { "wildcard": "*ball" }}]
```

It matches the following attributes:

```
{"customer_interests": ["hockey", "rugby", "soccer] }
```

However, it does not match the following message attribute:

```
{"customer_interests": ["baseball", "basketball"] }
```

**anything-but suffix**

The following policy property denies the `-ball`

suffix:

```
"customer_interests": [ { "anything-but": { "suffix": "ball" } } ]
```

It matches the following attributes:

```
{"customer_interests": ["hockey", "rugby", "soccer] }
```

However, it does not match the following message attribute:

```
 {"customer_interests": ["baseball", "basketball"] }
```

## Equals-ignore-case matching

When a policy property includes the keyword `equals-ignore-case`, it
will perform a case-insensitive match with any message attribute or body property
value.

Consider the following policy property:

```
"customer_interests": [{"equals-ignore-case": "tennis"}]
```

It matches either of the following message attributes:

```
"customer_interests": {"Type": "String", "Value": "TENNIS"}
```

```
"customer_interests": {"Type": "String", "Value": "Tennis"}
```

It also matches either of the following message bodies:

```
{
    "customer_interests": "TENNIS"
}
```

```
{
    "customer_interests": "teNnis"
{
```

## IP address matching

You can use the `cidr` operator to check whether an incoming message
originates from a specific IP address or subnet.

Consider the following policy property:

```
"source_ip":[{"cidr": "10.0.0.0/24"}]
```

It matches either of the following message attributes:

```
"source_ip": {"Type": "String", "Value": "10.0.0.0"}
```

```
"source_ip": {"Type": "String", "Value": "10.0.0.255"}
```

It also matches either of the following message bodies:

```
{
   "source_ip": "10.0.0.0"
}
```

```
{
   "source_ip": "10.0.0.255"
}
```

However, it doesn't match the following message attribute:

```
"source_ip": {"Type": "String", "Value": "10.1.1.0"}
```

Nor does it match the following message body:

```
{
   "source_ip": "10.1.1.0"
}
```

## Prefix matching

When a policy property includes the keyword `prefix`, it matches any
message attribute or body property values that begin with the specified
characters.

Consider the following policy property:

```
"customer_interests": [{"prefix": "bas"}]
```

It matches either of the following message attributes:

```
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```
"customer_interests": {"Type": "String", "Value": "basketball"}
```

It also matches either of the following message bodies:

```
{
   "customer_interests": "baseball"
}
```

```
{
   "customer_interests": "basketball"
}
```

However, it doesn't match the following message attribute:

```
"customer_interests": {"Type": "String", "Value": "rugby"}
```

Nor does it match the following message body:

```
{
   "customer_interests": "rugby"
}
```

## Suffix matching

When a policy property includes the keyword `suffix`, it matches any
message attribute or body property values that end with the specified
characters.

Consider the following policy property:

```
"customer_interests": [{"suffix": "ball"}]
```

It matches either of the following message attributes:

```
"customer_interests": {"Type": "String", "Value": "baseball"}
```

```
"customer_interests": {"Type": "String", "Value": "basketball"}
```

It also matches either of the following message bodies:

```
{
    "customer_interests": "baseball"
}
```

```
{
    "customer_interests": "basketball"
}
```

However, it doesn't match the following message attribute:

```
"customer_interests": {"Type": "String", "Value": "rugby"}
```

Nor does it match the following message body:

```
{
    "customer_interests": "rugby"
}
```

## Wildcard

You can use the wildcard character (\*) to match string values in event patterns.

The following policy uses the wildcard (\*) character:

```
"customer_interests": [ { "wildcard": "*ball" } ]
```

It matches the following attributes:

```
{"customer_interests": ["baseball", "basketball"] }
```
