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
