

# filldown
<a name="CWL_QuerySyntax-Filldown"></a>

Use the `filldown` command to carry the last non-null value forward to fill gaps. You can specify field names or use wildcards. If you do not specify fields, all fields are filled.

**Syntax**  


```
| filldown [{{field1}} [{{field2}} ...]]
```

The command uses the following arguments:
+ `{{field}}` (Optional) – One or more field names or wildcard patterns. If omitted, all fields are filled.

**Example**  
The following query carries forward non-null values in the `host` field and all fields matching `cpu*`.

```
fields @timestamp, host, cpu_user, cpu_system
| filldown host cpu*
```