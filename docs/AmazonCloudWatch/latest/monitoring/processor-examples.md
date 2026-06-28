# Common processor use cases

Here are common scenarios and example configurations for combining processors:

###### Example Standardize log formats and add metadata

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

###### Example Clean and normalize field values

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

###### Example Extract and transform specific fields

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

###### Example Conditional processing with entry-level conditions

Add different metadata based on log severity using entry-level
`when` conditions:

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

###### Example Drop unwanted log entries

Filter out debug and trace log entries from a third-party source to
reduce noise and storage costs:

```
processor:
  - drop_events:
      when: "log.level in {'DEBUG', 'TRACE'}"
      handle_expression_failure: "skip"
```

###### Example Processor-level conditional with delete\_entries

Remove sensitive fields only when the environment is production:

```
processor:
  - delete_entries:
      with_keys: ["password", "api_key", "ssn"]
      when: "environment in {'prod', 'staging'}"
```
