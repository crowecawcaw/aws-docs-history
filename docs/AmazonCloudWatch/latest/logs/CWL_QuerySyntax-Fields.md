# fields

Use `fields` to show specific fields in query results.

If your query contains multiple `fields` commands and doesn't
include a `display` command, the results display all of the
fields that are specified in the `fields` commands.

**Example: Display specific fields**

The following example shows a query that returns 20 log events and
displays them in descending order. The values for `@timestamp`
and `@message` are shown in the query results.

```
fields @timestamp, @message
| sort @timestamp desc
| limit 20
```

Use `fields` instead of `display` when you want to
use the different functions and operations supported by `fields`
for modifying field values and creating new fields that can be used in
queries.

You can use the `fields` command with the keyword
_as_ to create extracted fields that use fields and
functions in your log events. For example, `fields ispresent as
 isRes` creates an extracted field named `isRes`, and
the extracted field can be used in the rest of your query.
