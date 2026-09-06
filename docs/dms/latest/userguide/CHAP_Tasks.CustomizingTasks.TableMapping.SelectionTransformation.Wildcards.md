

# Wildcards in table mapping
<a name="CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Wildcards"></a>

This section describes wildcards you can use when specifying the schema and table names for table mapping.


| Wildcard | Matches | 
| --- |--- |
| % | Zero or more characters | 
| \_ | A single character | 

**Wildcard pattern limitations**  
Use `%` or `_` in selection rules. Bracket-based patterns such as `[_]`, `[ab]`, and `[a-d]` may not work with all endpoint types - test them before relying on them, or create a separate selection rule for each explicit table name.

For Oracle source and target endpoints, you can use the `escapeCharacter` extra connection attribute to specify an escape character. An escape character allows you to use a specified wildcard character in expressions as if it was not wild. For example, `escapeCharacter=#` allows you to use '\#' to make a wildcard character act as an ordinary character in an expression as in the this sample code.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "542485267",
            "rule-name": "542485267",
            "object-locator": { "schema-name": "ROOT", "table-name": "TEST#_T%" },
            "rule-action": "include",
            "filters": []
        }
    ]
}
```

Here, the '\#' escape character makes the '\_' wildcard character act as a normal character. AWS DMS selects tables in the schema named `ROOT`, where each table has a name with `TEST_T` as its prefix.