# Transformation helpers in util.transform

`util.transform` contains helper methods that make it easier to perform
complex operations against data sources.

**`util.transform.toDynamoDBFilterExpression(filterObject:
 DynamoDBFilterObject) : string`**

Converts an input string to a filter expression for use with DynamoDB. We
recommend using `toDynamoDBFilterExpression` with [built-in module
functions](built-in-modules-js.md "built-in-modules-js.md").

**`util.transform.toElasticsearchQueryDSL(object:
 OpenSearchQueryObject) : string`**

Converts the given input into its equivalent OpenSearch Query DSL
expression, returning it as a JSON string.

**Example input:**

```
util.transform.toElasticsearchQueryDSL({
    "upvotes":{
        "ne":15,
        "range":[
            10,
            20
        ]
    },
    "title":{
        "eq":"hihihi",
        "wildcard":"h*i"
    }
  })
```

**Example output:**

```
{
    "bool":{
      "must":[
          {
            "bool":{
              "must":[
                  {
                    "bool":{
                      "must_not":{
                        "term":{
                          "upvotes":15
                        }
                      }
                    }
                  },
                  {
                    "range":{
                      "upvotes":{
                        "gte":10,
                        "lte":20
                      }
                    }
                  }
              ]
            }
          },
          {
            "bool":{
              "must":[
                  {
                    "term":{
                      "title":"hihihi"
                    }
                  },
                  {
                  "wildcard":{
                      "title":"h*i"
                    }
                  }
              ]
            }
          }
      ]
    }
}
```

###### Note

The default operator is assumed to be AND.

**`util.transform.toSubscriptionFilter(objFilter,
 ignoredFields?, rules?): SubscriptionFilter`**

Converts a `Map` input object to a
`SubscriptionFilter` expression object. The
`util.transform.toSubscriptionFilter` method is used as an
input to the `extensions.setSubscriptionFilter()` extension. For
more information, see [Extensions](extensions-js.md "extensions-js.md").

###### Note

The parameters and return statement is listed below:

_Parameters_

- `objFilter`:
  `SubscriptionFilterObject`

A `Map` input object that's converted to the
`SubscriptionFilter` expression object.

- `ignoredFields`:
  `SubscriptionFilterExcludeKeysType` (optional)

A `List` of field names in the first object that will
be ignored.

- `rules`: `SubscriptionFilterRuleObject`
  (optional)

A `Map` input object with strict rules that's
included when you're constructing the
`SubscriptionFilter` expression object. These strict
rules will be included in the `SubscriptionFilter`
expression object so that at least one of the rules will be
satisfied to pass the subscription filter.
_Response_

Returns a `SubscriptionFilter`.

**`util.transform.toSubscriptionFilter(Map,
 List)`**

Converts a `Map` input object to a
`SubscriptionFilter` expression object. The
`util.transform.toSubscriptionFilter` method is used as an
input to the `extensions.setSubscriptionFilter()` extension. For
more information, see [Extensions](extensions-js.md "extensions-js.md").

The first argument is the `Map` input object that's converted
to the `SubscriptionFilter` expression object. The second
argument is a `List` of field names that are ignored in the first
`Map` input object while constructing the
`SubscriptionFilter` expression object.

**`util.transform.toSubscriptionFilter(Map, List,
 Map)`**

Converts a `Map` input object to a
`SubscriptionFilter` expression object. The
`util.transform.toSubscriptionFilter` method is used as an
input to the `extensions.setSubscriptionFilter()` extension. For
more information, see [Extensions](extensions-js.md "extensions-js.md").

**`util.transform.toDynamoDBConditionExpression(conditionObject)`**

Creates a DynamoDB condition expression.

## Subscription filter arguments

The
following
table
explains the how the arguments of the following utilities are
defined:

- `Util.transform.toSubscriptionFilter(objFilter, ignoredFields?, rules?):
SubscriptionFilter`

Argument 1: Map
Argument 1 is a `Map` object with the following key
values:

- field names
- "and"
- "or"

For field names as keys, the conditions on these fields' entries are in the
form of `"operator" : "value"`.

The following example shows how entries can be added to the
`Map`:

```
"field_name" : {
                    "operator1" : value
               }

## We can have multiple conditions for the same field_name:

"field_name" : {
                    "operator1" : value
                    "operator2" : value
                    .
                    .
                    .
               }
```

When a field has two or more conditions on it, all of these conditions are
considered to use the OR operation.

The input `Map` can also have "and" and "or" as keys, implying
that all entries within these should be joined using AND or OR logic depending
on the key. The key values "and" and "or" expect an array of conditions.

```
"and" : [

            {
                "field_name1" : {
                    "operator1" : value
                }
             },

             {
                "field_name2" : {
                    "operator1" : value
                }
             },
             .
             .
        ].
```

Note that
you
can nest "and" and
"or".
That is, you can have nested "and"/"or" within another
"and"/"or" block. However, this doesn't work for simple fields.

```
"and" : [

            {
                "field_name1" : {
                    "operator" : value
                }
             },

             {
                "or" : [
                            {
                                "field_name2" : {
                                    "operator" : value
                                }
                            },

                            {
                                "field_name3" : {
                                    "operator" : value
                                }
                            }

                        ].
```

The following example shows an input of _argument
1_ using `util.transform.toSubscriptionFilter(Map) :
 Map`.

**Input(s)**

Argument 1: Map:

```
{
  "percentageUp": {
    "lte": 50,
    "gte": 20
  },
  "and": [
    {
      "title": {
        "ne": "Book1"
      }
    },
    {
      "downvotes": {
        "gt": 2000
      }
    }
  ],
  "or": [
    {
      "author": {
        "eq": "Admin"
      }
    },
    {
      "isPublished": {
        "eq": false
      }
    }
  ]
}
```

**Output**

The result is a `Map` object:

```
{
  "filterGroup": [
    {
      "filters": [
        {
          "fieldName": "percentageUp",
          "operator": "lte",
          "value": 50
        },
        {
          "fieldName": "title",
          "operator": "ne",
          "value": "Book1"
        },
        {
          "fieldName": "downvotes",
          "operator": "gt",
          "value": 2000
        },
        {
          "fieldName": "author",
          "operator": "eq",
          "value": "Admin"
        }
      ]
    },
    {
      "filters": [
        {
          "fieldName": "percentageUp",
          "operator": "lte",
          "value": 50
        },
        {
          "fieldName": "title",
          "operator": "ne",
          "value": "Book1"
        },
        {
          "fieldName": "downvotes",
          "operator": "gt",
          "value": 2000
        },
        {
          "fieldName": "isPublished",
          "operator": "eq",
          "value": false
        }
      ]
    },
    {
      "filters": [
        {
          "fieldName": "percentageUp",
          "operator": "gte",
          "value": 20
        },
        {
          "fieldName": "title",
          "operator": "ne",
          "value": "Book1"
        },
        {
          "fieldName": "downvotes",
          "operator": "gt",
          "value": 2000
        },
        {
          "fieldName": "author",
          "operator": "eq",
          "value": "Admin"
        }
      ]
    },
    {
      "filters": [
        {
          "fieldName": "percentageUp",
          "operator": "gte",
          "value": 20
        },
        {
          "fieldName": "title",
          "operator": "ne",
          "value": "Book1"
        },
        {
          "fieldName": "downvotes",
          "operator": "gt",
          "value": 2000
        },
        {
          "fieldName": "isPublished",
          "operator": "eq",
          "value": false
        }
      ]
    }
  ]
}
```

Argument 2: List
Argument 2 contains a `List` of field names that shouldn't be
considered in the input `Map` (argument 1) while constructing the
`SubscriptionFilter` expression object. The `List` can
also be empty.

The following example shows the inputs of argument 1 and argument 2 using
`util.transform.toSubscriptionFilter(Map, List) : Map`.

**Input(s)**

Argument 1: Map:

```
{
  "percentageUp": {
    "lte": 50,
    "gte": 20
  },
  "and": [
    {
      "title": {
        "ne": "Book1"
      }
    },
    {
      "downvotes": {
        "gt": 20
      }
    }
  ],
  "or": [
    {
      "author": {
        "eq": "Admin"
      }
    },
    {
      "isPublished": {
        "eq": false
      }
    }
  ]
}
```

Argument 2: List:

```
["percentageUp", "author"]
```

**Output**

The result is a `Map` object:

```
{
  "filterGroup": [
    {
      "filters": [
        {
          "fieldName": "title",
          "operator": "ne",
          "value": "Book1"
        },
        {
          "fieldName": "downvotes",
          "operator": "gt",
          "value": 20
        },
        {
          "fieldName": "isPublished",
          "operator": "eq",
          "value": false
        }
      ]
    }
  ]
}
```

Argument 3: Map
Argument 3 is a `Map` object that has field names as key values
(cannot have "and" or "or"). For field names as keys, the conditions on these
fields are entries in the form of `"operator" : "value"`. Unlike
argument 1, argument 3 cannot have multiple conditions in the same key. In
addition, argument 3 doesn't have an "and" or "or" clause, so there's no
nesting involved either.

Argument 3 represents a list of strict rules, which are added to the
`SubscriptionFilter` expression object so that **at least one** of these conditions is met to pass the
filter.

```
{
  "fieldname1": {
    "operator": value
  },
  "fieldname2": {
    "operator": value
  }
}
.
.
.
```

The following example shows the inputs of _argument
1_, _argument 2_, and _argument 3_ using
`util.transform.toSubscriptionFilter(Map, List, Map) :
 Map`.

**Input(s)**

Argument 1: Map:

```
{
  "percentageUp": {
    "lte": 50,
    "gte": 20
  },
  "and": [
    {
      "title": {
        "ne": "Book1"
      }
    },
    {
      "downvotes": {
        "lt": 20
      }
    }
  ],
  "or": [
    {
      "author": {
        "eq": "Admin"
      }
    },
    {
      "isPublished": {
        "eq": false
      }
    }
  ]
}
```

Argument 2: List:

```
["percentageUp", "author"]
```

Argument 3: Map:

```
{
  "upvotes": {
    "gte": 250
  },
  "author": {
    "eq": "Person1"
  }
}
```

**Output**

The result is a `Map` object:

```
{
  "filterGroup": [
    {
      "filters": [
        {
          "fieldName": "title",
          "operator": "ne",
          "value": "Book1"
        },
        {
          "fieldName": "downvotes",
          "operator": "gt",
          "value": 20
        },
        {
          "fieldName": "isPublished",
          "operator": "eq",
          "value": false
        },
        {
          "fieldName": "upvotes",
          "operator": "gte",
          "value": 250
        }
      ]
    },
    {
      "filters": [
        {
          "fieldName": "title",
          "operator": "ne",
          "value": "Book1"
        },
        {
          "fieldName": "downvotes",
          "operator": "gt",
          "value": 20
        },
        {
          "fieldName": "isPublished",
          "operator": "eq",
          "value": false
        },
        {
          "fieldName": "author",
          "operator": "eq",
          "value": "Person1"
        }
      ]
    }
  ]
}
```
