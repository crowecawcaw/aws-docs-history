# where

Use the `where` command as an alias for the
`filter` command.
It accepts identical syntax and behavior.

###### Syntax

```
| where `condition`
```

The command uses the following arguments:

- `condition` – A
  boolean expression identical to what the `filter`
  command accepts.

###### Example

The following query filters for log events containing "error".

```
fields @timestamp, @message
| where @message like /error/
```
