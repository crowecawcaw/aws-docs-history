

# Expression syntax for conditional processing
<a name="conditional-processing"></a>

CloudWatch pipelines processors that support conditional processing accept a `when` parameter containing an expression. When the expression evaluates to true, the processor or entry executes. Expressions use dot notation (`.`) for nested field access. For example, `user.role` accesses the `role` field inside the `user` object. For more details on processors that support conditional processing and their specific parameters, see [CloudWatch pipelines processors](pipeline-processors.md). For configuration examples, see [Common processor use cases](processor-examples.md).

**Note**  
Conditional processing applies to log pipelines only. Metrics pipelines do not support the `when` parameter.

## Processor-level and entry-level conditions
<a name="conditional-levels"></a>

There are two levels at which you can apply a `when` condition, depending on the processor.

Processor-level `when` (outer level)  
A `when` placed at the top level of the processor configuration. If the expression evaluates to false, the entire processor is skipped and no operations within it execute. All processors that support conditional processing support this level.  

**Example Processor-level condition — skip entire processor**  
The following `delete_entries` processor only runs when the environment is production or staging. If the condition is false, none of the keys are deleted.  

```
processor:
  - delete_entries:
      with_keys: ["password", "api_key", "ssn"]
      when: "environment in {'prod', 'staging'}"
```

Entry-level `when` (within each entry)  
A `when` placed inside an individual entry in the `entries` array. Each entry is evaluated independently — if the expression is false, only that specific entry is skipped while other entries in the same processor still execute. Only processors with an `entries` array support this level (such as `add_entries`, `copy_values`, `rename_keys`, `move_keys`, `extract_value`, and `substitute_string`).  

**Example Entry-level condition — skip individual entries**  
The following `add_entries` processor adds different keys depending on each entry's condition. The first entry only adds `severity` when the log level is ERROR. The second entry always adds `processed` because it has no condition.  

```
processor:
  - add_entries:
      entries:
        - key: "severity"
          value: "high"
          when: "log.level == 'ERROR'"
        - key: "processed"
          value: "true"
```

Processors that support both levels can use them together. When both are specified, the processor-level condition is evaluated first. If it is false, the entire processor is skipped and no entry-level conditions are evaluated.

**Example Both levels combined**  
The processor-level `when` ensures the entire processor only runs for production traffic. Within that, each entry has its own condition to control which key is added.  

```
processor:
  - add_entries:
      when: "environment == 'prod'"
      entries:
        - key: "alert_level"
          value: "critical"
          when: "log.level == 'ERROR'"
        - key: "alert_level"
          value: "warning"
          when: "log.level == 'WARN'"
```

For a table showing which processors support which level, see the [Conditional processing support](#conditional-support) section below.

**Fallback with `when_else`**  
Processors that support entry-level conditions also support `when_else`. An entry with `when_else` acts as a fallback — it executes only when none of the other `when` conditions in the same processor matched. The expression value provided to `when_else` identifies which set of `when` conditions to consider, but the entry itself runs based solely on whether those conditions all evaluated to false. There is no explicit negation check — the entry simply runs when no other `when` matched.

**Example Fallback entry with when\_else**  
The first entry runs when the log level is ERROR. The second entry uses `when_else` and runs only when the first entry's `when` condition did not match (that is, the log level is anything other than ERROR).  

```
processor:
  - add_entries:
      entries:
        - key: "alert_level"
          value: "critical"
          when: "log.level == 'ERROR'"
        - key: "alert_level"
          value: "info"
          when_else: "log.level == 'ERROR'"
```

## Conditional processing support
<a name="conditional-support"></a>

The following table shows which processors support conditional processing and at what level.


| Processor | Conditional support | Level | 
| --- | --- | --- | 
| add\_entries | Yes | Processor and entry | 
| copy\_values | Yes | Processor and entry | 
| delete\_entries | Yes | Processor | 
| move\_keys | Yes | Processor and entry | 
| flatten | Yes | Processor | 
| lowercase\_string | Yes | Processor | 
| uppercase\_string | Yes | Processor | 
| trim\_string | Yes | Processor | 
| substitute\_string | Yes | Processor and entry | 
| truncate | Yes | Processor | 
| extract\_value | Yes | Processor and entry | 
| convert\_entry\_type | Yes | Processor | 
| date | Yes | Processor | 
| dissect | Yes | Processor | 
| list\_to\_map | Yes | Processor | 
| rename\_keys | Yes | Processor and entry | 
| select\_entries | Yes | Processor | 
| translate | Yes | Processor | 
| grok | Yes | Processor | 
| drop\_events | Yes | Processor (required) | 
| OCSF, CSV, JSON, KeyValue, WAF, Postgres, CloudFront, VPC, Route53 | No | — | 

## Operators
<a name="expression-operators"></a>

The following table lists the supported operators.


| Category | Operators | Example | 
| --- | --- | --- | 
| Relational | <, <=, >, >= | status\_code >= 200 and status\_code < 300 | 
| Equality | ==, \!= | log.level == "ERROR" | 
| Conditional | and, or, not | log.level == "ERROR" or log.level == "FATAL" | 
| Arithmetic | \+, -, \*, / | response\_time \* 1000 > 5000 | 
| Set membership | in, not in | environment in {"prod", "staging", "preprod"} | 
| Regex matching | =\~, \!\~ | message =\~ "^ERROR.\*timeout" | 

## Functions
<a name="expression-functions"></a>

`length(value)`  
Returns the length of a string or array. Example: `length(message) > 100`

`contains(value, search)`  
Checks whether a string contains a substring or an array contains an element. Example: `contains(message, "error")`

`startsWith(field, prefix)`  
Checks whether a string starts with a specified prefix. Example: `startsWith(message, "ERROR")`

## Expression examples
<a name="expression-examples"></a>

```
log.level == "ERROR"
status_code >= 200 and status_code < 300
environment in {"prod", "staging", "preprod"}
message =~ "^ERROR.*timeout"
user.role == "admin" and user.permissions.write == true
length(message) > 100 and contains(message, "error")
(log.level == "ERROR" or log.level == "FATAL") and environment == "prod"
```

## Limitations
<a name="expression-limitations"></a>
+ Expression maximum length is 256 characters.
+ Parser processors (except Grok) do not support conditional processing. This includes JSON, CSV, KeyValue, WAF, Postgres, CloudFront, VPC, Route53, and OCSF parsers.
+ If the Grok processor is used as the parser (first processor) in a pipeline and its `when` condition evaluates to false, the entire pipeline does not execute for that log event.