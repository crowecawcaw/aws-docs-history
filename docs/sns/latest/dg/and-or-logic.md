# AND/OR logic

Use AND/OR logic in filter policies to match message attributes or message body
properties in Amazon SNS. This enables more precise and flexible message filtering.

## AND logic

You can apply AND logic using multiple property names.

Consider the following policy:

```
{
  "customer_interests": ["rugby"],
  "price_usd": [{"numeric": [">", 100]}]
}
```

It matches any message attribute or message body property with the value of
`customer_interests` set to `rugby`
_and_ the value of `price_usd` set to a number larger
than 100.

###### Note

You can't apply AND logic to values of the same attribute.

## OR logic

You can apply OR logic by assigning multiple values to a property name.

Consider the following policy:

```
{
   "customer_interests": ["rugby", "football", "baseball"]
}
```

It matches any message attribute or message body property with the value of
`customer_interests` set to `rugby`,
`football`, _or_
`baseball`.

## OR operator

You can use the `"$or"` operator to explicitly define a filter policy
to express the OR relationship between multiple attributes in the policy.

Amazon SNS only recognizes an `"$or"` relationship when the policy has met
all of the following conditions. When all of these conditions are not met,
`"$or"` is treated as a regular attribute name, the same as any other
string in the policy.

- There is an `"$or"` field attribute in the rule followed with
  an array, for example `“$or” : []`.
- There are at least 2 objects in the `"$or"` array: `"$or":
[{}, {}]`.
- None of the objects in the `"$or"` array have field names that
  are reserved keywords.

Otherwise `"$or"` is treated as a normal attribute name, the same as
other strings in the policy.

The following policy isn't parsed as an OR relationship because numeric and prefix
are reserved keywords.

```
{
   "$or": [ {"numeric" : 123}, {"prefix": "abc"} ]
}
```

**`OR` operator examples**

Standard `OR`:

```
{
  "source": [ "aws.cloudwatch" ],
  "$or": [
    { "metricName": [ "CPUUtilization" ] },
    { "namespace": [ "AWS/EC2" ] }
  ]
}
```

The filter logic for this policy is:

```
"source" && ("metricName" || "namespace")
```

It matches either of the following sets of message attributes:

```
"source": {"Type": "String", "Value": "aws.cloudwatch"},
"metricName": {"Type": "String", "Value": "CPUUtilization"}
```

or

```
"source": {"Type": "String", "Value": "aws.cloudwatch"},
"namespace": {"Type": "String", "Value": "AWS/EC2"}
```

It also matches either of the following message bodies:

```
{
    "source": "aws.cloudwatch",
    "metricName": "CPUUtilization"
}
```

or

```
{
    "source": "aws.cloudwatch",
    "namespace": "AWS/EC2"
}
```

### Policy constraints that include

`OR` relationships

Consider the following policy:

```
{
    "source": [ "aws.cloudwatch" ],
    "$or": [
      { "metricName": [ "CPUUtilization", "ReadLatency" ] },
      {
        "metricType": [ "MetricType" ] ,
        "$or" : [
          { "metricId": [ 1234, 4321 ] },
          { "spaceId": [ 1000, 2000, 3000 ] }
        ]
      }
    ]
  }
```

The logic for this policy can also be simplified as:

```
("source" AND "metricName")
OR
("source" AND "metricType" AND "metricId")
OR
("source" AND "metricType" AND "spaceId")
```

The complexity calculation for policies with OR relationships can be
simplified as the sum of the combination complexities for each OR
statement.

The total combination is calculated as follows:

```
(source * metricName) + (source * metricType * metricId) + (source * metricType * spaceId)
= (1 * 2) + (1 * 1 * 2) + (1 * 1 * 3)
= 7
```

`source` has one value, `metricName` has two values,
`metricType` has one value, `metricId` has two values
and `spaceId` has three values.

Consider the following nested filter policy:

```
{
    "$or": [
      { "metricName": [ "CPUUtilization", "ReadLatency" ] },
      { "namespace": [ "AWS/EC2", "AWS/ES" ] }
    ],
    "detail" : {
      "scope" : [ "Service" ],
      "$or": [
        { "source": [ "aws.cloudwatch" ] },
        { "type": [ "CloudWatch Alarm State Change"] }
      ]
    }
  }
```

The logic for this policy can be simplified as:

```
("metricName" AND ("detail"."scope" AND "detail"."source")
OR
("metricName" AND ("detail"."scope" AND "detail"."type")
OR
("namespace" AND ("detail"."scope" AND "detail"."source")
OR
("namespace" AND ("detail"."scope" AND "detail"."type")
```

The calculation for total combinations is the same for non-nested policies
except we need to consider the a key’s nesting level.

The total combination is calculated as follows:

```
(2 * 2 * 2) + (2 * 2 * 2) + (2 * 2 * 2) + (2 * 2 * 2) = 32
```

`metricName` has two values, `namespace` has two values,
`scope` is a two level nested key with one value,
`source` is a two level nested key with one value, and
`type` is a two level nested key with one value.
