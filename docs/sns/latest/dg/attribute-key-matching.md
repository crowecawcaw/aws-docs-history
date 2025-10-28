# Key matching

Use the `exists` operator in a filter policy to match incoming
messages based on whether a specific property is present or absent.

- `exists` works only on leaf nodes (final attributes in the
  structure).
- It does not apply to intermediate nodes within a nested JSON structure.

- Use `"exists": true` to match incoming messages that include the
  specified property. The key must have a non-null and non-empty value.

For example, the following policy property uses the `exists`
operator with a value of `true`:

```
"store": [{"exists": true}]
```

It matches any list of message attributes that contains the `store`
attribute key, such as the following:

```
"store": {"Type": "String", "Value": "fans"}
"customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}
```

It also matches either of the following message body:

```
{
    "store": "fans"
    "customer_interests": ["baseball", "basketball"]
}
```

However, it doesn't match any list of message attributes
_without_ the `store` attribute key, such as
the following:

```
"customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}
```

Nor does it match the following message body:

```
{
    "customer_interests": ["baseball", "basketball"]
}
```

- Use `"exists": false` to match incoming messages that
  _don't_ include the specified property.

###### Note

`"exists": false` only matches if at least one attribute is
present. An empty set of attributes results in the filter not
matching.

For example, the following policy property uses the `exists`
operator with a value of `false`:

```
"store": [{"exists": false}]
```

It _doesn't_ match any list of message attributes that
contains the `store` attribute key, such as the following:

```
"store": {"Type": "String", "Value": "fans"}
"customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}
```

It also doesn’t match the following message body:

```
{
    "store": "fans"
    "customer_interests": ["baseball", "basketball"]
}
```

However, it matches any list of message attributes
_without_ the `store` attribute key, such as
the following:

```
"customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}

```

It also matches the following message body:

```
{
    "customer_interests": ["baseball", "basketball"]
}
```
