

# Common processor use cases
<a name="processor-examples"></a>

Here are common scenarios and example configurations for combining processors.

**Logs pipeline examples**

**Example Standardize log formats and add metadata**  
Parse JSON logs, standardize field names, and add environment information:  

```
processor:
  - parse_json: {}
  - rename_keys:
      entries:
        - from_key: "timestamp"
          to_key: "@timestamp"
        - from_key: "log_level"
          to_key: "level"
  - add_entries:
      entries:
        - key: "environment"
          value: "production"
        - key: "application"
          value: "payment-service"
```

**Example Clean and normalize field values**  
Standardize status codes and remove sensitive data:  

```
processor:
  - uppercase_string:
      with_keys: ["status", "method"]
  - delete_entries:
      with_keys: ["credit_card", "password"]
  - substitute_string:
      entries:
        - source: "status"
          from: "SUCCESS"
          to: "OK"
```

**Example Extract and transform specific fields**  
Extract user information and format for analysis:  

```
processor:
  - extract_value:
      entries:
        - source: "user_agent"
          target: "browser"
          from: "(?<browser>Chrome|Firefox|Safari)"
          to: "${browser}"
  - lowercase_string:
      with_keys: ["browser"]
  - move_keys:
      entries:
        - from_key: "browser"
          to_key: "user_data.browser"
```

**Example Conditional processing with entry-level conditions**  
Add different metadata based on log severity using entry-level `when` conditions:  

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

**Example Drop unwanted log entries**  
Filter out debug and trace log entries from a third-party source to reduce noise and storage costs:  

```
processor:
  - drop_events:
      when: "log.level in {'DEBUG', 'TRACE'}"
      handle_expression_failure: "skip"
```

**Example Processor-level conditional with delete\_entries**  
Remove sensitive fields only when the environment is production:  

```
processor:
  - delete_entries:
      with_keys: ["password", "api_key", "ssn"]
      when: "environment in {'prod', 'staging'}"
```

## Metrics pipeline examples
<a name="metrics-processor-examples"></a>

The following examples show processor configurations for metrics pipelines. Metrics processors use OTTL path expressions to target attributes at different scopes.

**Example Add business context to metrics**  
Add team ownership and environment tags to metric datapoints:  

```
processor:
  - add_attributes:
      attributes:
        - key: resource.attributes["team"]
          value: "platform-engineering"
        - key: resource.attributes["cost_center"]
          value: "CC-1234"
```

**Example Remove high-cardinality attributes**  
Strip attributes that drive up storage costs. Does not apply to cumulative metrics or vended metrics — if any metrics in the selection criteria have unsupported temporality, the pipeline emits an `UnsupportedTemporality` warning metric that you can monitor in the `AWS/Observability Admin` namespace:  

```
processor:
  - delete_attributes:
      with_keys:
        - resource.attributes["host.id"]
        - datapoint.attributes["http.request.id"]
```

**Example Standardize naming conventions**  
Rename metrics and attributes to align with OpenTelemetry semantic conventions. Does not apply to cumulative metrics or vended metrics:  

```
processor:
  - rename_metrics:
      metrics:
        - from: "cpu_usage_percent"
          to: "system.cpu.utilization"
  - rename_attributes:
      attributes:
        - from_key: resource.attributes["hostname"]
          to_key: resource.attributes["host.name"]
```