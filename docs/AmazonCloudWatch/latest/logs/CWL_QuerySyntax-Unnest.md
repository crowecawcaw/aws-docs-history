# unnest

Use `unnest` to flatten a list taken as input to produce
multiple records with a single record for each element in the list. Based on
the number of items a field contains, this command discards the current
record and generates new records. Each record includes the
`unnested_field`, which represents an item. All other fields
come from the original record.

The input for `unnest` is `LIST`, which comes from
the `jsonParse` function. For more information, see [Structure types](CWL_QuerySyntax-operations-functions.md#CWL_QuerySyntax-structure-types "CWL_QuerySyntax-operations-functions.md#CWL_QuerySyntax-structure-types"). Any other types, such as `MAP`,
`String` and `numbers`, are treated as a list with
one item in `unnest`.

###### Command structure

The following example describes the format of this command.

```
unnest field into unnested_field
```

###### Example query

The following example parses a JSON object string and expands a list
of field events.

```
fields jsonParse(@message) as json_message
| unnest json_message.events into event
| display event.name
```

The log event for this example query could be a JSON string as
follows:

```
{
   "events": [
        {
            "name": "exception"
        },
        {
            "name": "user action"
        }
   ]
}
```

In this case, the sample query produces two records in the query result,
one with `event.name` as `exception` and another with
`event.name` as **user action**

###### Example query

The following example flattens a list and then filters out items.

```
fields jsonParse(@message) as js
| unnest js.accounts into account
| filter account.type = "internal"
```

###### Example query

The following example flattens a list for aggregation.

```
fields jsonParse(trimmedData) as accounts
| unnest accounts into account
| stats sum(account.droppedSpans) as n by account.accountId
| sort n desc
| limit 10
```
