# **display**

Use `display` to show a specific field or fields in query
results.

The `display` command shows only the fields you specify. If
your query contains multiple `display` commands, the query
results show only the field or fields that you specified in the final
`display` command.

**Example: Display one field**

The code snippet shows an example of a query that uses the parse command
to extract data from `@message` to create the extracted fields
`loggingType` and `loggingMessage`. The query
returns all log events where the values for `loggingType` are
**ERROR**. `display` shows only the values
for `loggingMessage` in the query results.

````
fields @message
| parse @message "[*] *" as loggingType, loggingMessage
| filter loggingType = "ERROR"
| display loggingMessage ``` ###### Tip Use `display` only once in a query. If you use `display` more than once in a query, the query results show the field specified in the last occurrence of `display` command being used.
````
