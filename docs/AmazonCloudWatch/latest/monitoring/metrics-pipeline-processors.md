# Metrics pipeline processors

Metrics pipeline processors transform OTel metric datapoints during ingestion. A metrics
pipeline can have up to 20 processors, applied sequentially in the order they are
defined.

Processors use OTTL path expressions to target attributes at different scopes:

| Path                                      | Scope                    | Example                                       |
| ----------------------------------------- | ------------------------ | --------------------------------------------- |
| `resource.attributes["key"]`              | Resource-level           | `resource.attributes["service.name"]`         |
| `instrumentation_scope.attributes["key"]` | Scope attribute          | `instrumentation_scope.attributes["library"]` |
| `datapoint.attributes["key"]`             | Datapoint-level          | `datapoint.attributes["status_code"]`         |
| `attributes["key"]`                       | Short form for datapoint | `attributes["environment"]`                   |

## add\_attributes processor

Adds or overwrites attributes on metric datapoints. Works with all temporality
types.

**OTTL equivalent:**
`set(attributes["key"], "value")`

###### Configuration

Configure the add\_attributes processor with the following parameters:

```
processor:
  - add_attributes:
      attributes:
        - key: resource.attributes["team"]
          value: "payments"
        - key: attributes["environment"]
          value: "production"
        - key: instrumentation_scope.attributes["version"]
          value: "1.0"
          overwrite_if_key_exists: true
```

###### Parameters

`attributes` (required)

Array of attribute objects to add.

`attributes[].key` (required)

OTTL attribute path specifying where to add the attribute.

`attributes[].value` (required)

String value to assign.

`attributes[].overwrite_if_key_exists` (optional)

Boolean. When `true`, overwrites existing values. Defaults
to `false`. When set to `true`, this operation is
considered destructive and does not apply to cumulative metrics or
vended metrics.

## delete\_attributes processor

Removes specific attributes from metric datapoints. **Does not
apply to cumulative metrics or vended metrics.**

**OTTL equivalent:**
`delete_key(attributes, "key")`

###### Configuration

Configure the delete\_attributes processor with the following parameters:

```
processor:
  - delete_attributes:
      with_keys:
        - resource.attributes["obsolete"]
        - attributes["temp"]
        - datapoint.attributes["debug"]
```

###### Parameters

`with_keys` (required)

Array of OTTL attribute paths to remove.

## rename\_attributes processor

Renames attribute keys on metric datapoints. **Does not apply to
cumulative metrics or vended metrics.**

**OTTL equivalent:**
`set() + delete_key()`

###### Configuration

Configure the rename\_attributes processor with the following parameters:

```
processor:
  - rename_attributes:
      attributes:
        - from_key: resource.attributes["old_key"]
          to_key: resource.attributes["new_key"]
          overwrite_if_to_key_exists: true
```

###### Parameters

`attributes` (required)

Array of rename operations.

`attributes[].from_key` (required)

Source OTTL attribute path.

`attributes[].to_key` (required)

Target OTTL attribute path.

`attributes[].overwrite_if_to_key_exists` (optional)

Boolean. When `true`, overwrites if target key exists. Defaults
to `false`.

## rename\_metrics processor

Renames metric names. **Does not apply to cumulative metrics or
vended metrics.**

**OTTL equivalent:**
`set(name, "new.metric.name") where name == "old.metric.name"`

###### Configuration

Configure the rename\_metrics processor with the following parameters:

```
processor:
  - rename_metrics:
      metrics:
        - from: "old.metric.name"
          to: "new.metric.name"
```

###### Parameters

`metrics` (required)

Array of rename operations.

`metrics[].from` (required)

Current metric name.

`metrics[].to` (required)

New metric name.

## substitute\_attribute\_values processor

Maps attribute values by using a lookup table. **Does not apply to
cumulative metrics or vended metrics.**

**OTTL equivalent:**
`replace_match()`

###### Configuration

Configure the substitute\_attribute\_values processor with the following
parameters:

```
processor:
  - substitute_attribute_values:
      attributes:
        - key: resource.attributes["region"]
          from: "us-east-1a"
          to: "us-east-1"
```

###### Parameters

`attributes` (required)

Array of substitution operations.

`attributes[].key` (required)

OTTL attribute path to match against.

`attributes[].from` (required)

Value to match.

`attributes[].to` (required)

Replacement value.

## Full example

The following example uses all five processors in a single pipeline:

```
pipeline:
  source:
    cloudwatch_metrics:
      format: otlp
      selection_criteria:
        - match_all:
            - 'resource.attributes["service.name"] == "my-service"'
            - 'metric.name == "CPUUtilization"'
  processor:
    - add_attributes:
        attributes:
          - key: resource.attributes["env"]
            value: "prod"
            overwrite_if_key_exists: true
    - delete_attributes:
        with_keys:
          - resource.attributes["internal.trace"]
    - rename_attributes:
        attributes:
          - from_key: resource.attributes["old_key"]
            to_key: resource.attributes["new_key"]
    - rename_metrics:
        metrics:
          - from: "CPUUtilization"
            to: "system.cpu.utilization"
    - substitute_attribute_values:
        attributes:
          - key: resource.attributes["environment"]
            from: "dev"
            to: "development"
  sink:
    - cloudwatch_metrics: {}
```

## Processor compatibility and restrictions

Maximum processors

A metrics pipeline can have at most 20 processors.

Destructive processors and temporality

Destructive processors (`delete_attributes`,
`rename_attributes`, `rename_metrics`,
`substitute_attribute_values`, and
`add_attributes` with
`overwrite_if_key_exists: true`) do not apply to cumulative
metrics or vended metrics. These metrics are passed through unchanged.

Vended metrics protection

Destructive processors cannot modify metrics where
`instrumentation_scope.name` starts with
`cloudwatch.aws/`. These metrics are passed through
unchanged.
