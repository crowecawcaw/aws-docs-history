

# Filter processors
<a name="filter-processors"></a>

Filter processors let you selectively remove log entries from the pipeline based on conditions you define.

## drop\_events processor
<a name="drop-events-processor"></a>

Filters out unwanted log entries based on conditional expressions. Use this processor to reduce noise from third-party pipeline connectors and lower storage costs by removing log events that match specified conditions.

**Configuration**  
Configure the drop\_events processor with the following parameters:

```
processor:
  - drop_events:
      when: "log.level == 'DEBUG' or log.level == 'TRACE'"
```Parameters

`when` (required)  
Conditional expression that determines which log entries to drop. Log entries matching this expression are removed from the pipeline. Maximum length is 256 characters. See [Expression syntax for conditional processing](conditional-processing.md) for expression syntax.

`handle_expression_failure` (optional)  
Behavior when the `when` expression evaluation fails. Allowed values: `"skip"` (default) keeps the event, or `"apply"` drops the event regardless of the failure.

**Example Drop low-severity log entries**  
The following configuration drops all DEBUG and TRACE log entries, keeping only higher-severity events:  

```
processor:
  - drop_events:
      when: "log.level in {'DEBUG', 'TRACE'}"
      handle_expression_failure: "skip"
```