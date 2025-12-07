# Parser processors

Parser processors convert raw or semi-structured log data into structured formats.
Each pipeline can have at most one parser processor, which must be the first processor
in the pipeline.

## OCSF processor

Parses and transforms log data according to Open Cybersecurity Schema Framework
(OCSF) standards.

###### Configuration

Configure the OCSF processor with the following parameters:

```
processor:
  - ocsf:
      version: "1.5"
      mapping_version: 1.5.0
      schema:
          microsoft_office365_management_activity:
```

###### Parameters

`version` (required)

The OCSF schema version to use for transformation. Must be 1.5

`mapping_version` (required)

The OCSF mapping version for transformation. Must be 1.5.0.

`schema` (required)

Schema object specifying the data source type. The supported schemas
depend on the pipeline source type - each source type has its own set of
compatible OCSF schemas. You must use a schema that matches your
pipeline's source type.

This table lists the supported schema combinations.

| Pipeline Source Type      | Supported Schemas                          | Version | Mapping Version |
| ------------------------- | ------------------------------------------ | ------- | --------------- |
| `cloudwatch_logs`         | `cloud_trail:`                             | `1.5`   | Not required    |
| `cloudwatch_logs`         | `route53_resolver:`                        | `1.5`   | Not required    |
| `cloudwatch_logs`         | `vpc_flow:`                                | `1.5`   | Not required    |
| `cloudwatch_logs`         | `eks_audit:`                               | `1.5`   | Not required    |
| `cloudwatch_logs`         | `aws_waf:`                                 | `1.5`   | Not required    |
| `s3`                      | Any OCSF schema                            | Any     | Any             |
| `microsoft_office365`     | `microsoft_office365_management_activity:` | `1.5`   | `1.5.0`         |
| `microsoft_entra_id`      | `microsoft_entra_id:`                      | `1.5`   | `1.5.0`         |
| `microsoft_windows_event` | `microsoft_windows_event:`                 | `1.5`   | `1.5.0`         |
| `palo_alto_ngfw`          | `palo_alto_ngfw:`                          | `1.5`   | `1.5.0`         |

## CSV processor

Parses CSV formatted data into structured fields.

###### Configuration

Configure the CSV processor with the following parameters:

```
processor:
  - csv:
      column_names: ["col1", "col2", "col3"]
      delimiter: ","
      quote_character: '"'
```

###### Parameters

`column_names` (optional)

Array of column names for parsed fields. Maximum 100 columns, each
name up to 128 characters. If not provided, defaults to column_1, column_2, and so on.

`delimiter` (optional)

Character used to separate CSV fields. Must be a single character.
Defaults to comma (,).

`quote_character` (optional)

Character used to quote CSV fields containing delimiters. Must be a
single character. Defaults to double quote (").

To use the processor without specifying additional parameters, use the following command:

```
processor:
  - csv: {}
```

## Grok processor

Parses unstructured data using Grok patterns. At most 1 Grok is supported per
pipeline. For details on the Grok transformer in CloudWatch Logs see [Processors that you can use](../logs/CloudWatch-Logs-Transformation-Processors.md "../logs/CloudWatch-Logs-Transformation-Processors.md") in the _CloudWatch Logs User
Guide_.

###### Configuration

Configure the Grok processor with the following parameters:

When the data source is a dictionary, you can use this configuration:

```
processor:
  - grok:
      match:
       source_key: ["%{WORD:level} %{GREEDYDATA:msg}"]
```

When the data source is CloudWatch Logs, you can use this configuration:

```
processor:
  - grok:
      match:
       source_key: ["%{WORD:level} %{GREEDYDATA:msg}"]
```

###### Parameters

`match` (required)

Field mapping with Grok patterns. Only one field mapping
allowed.

`match.<field>` (required)

Array with single Grok pattern. Maximum 512 characters per
pattern.

## VPC processor

Parses VPC Flow Log data into structured fields.

###### Configuration

Configure the VPC processor with the following parameters:

```
processor:
  - parse_vpc: {}

```

## JSON processor

Parses JSON data into structured fields.

###### Configuration

Configure the JSON processor with the following parameters:

```
processor:
  - parse_json:
      source: "message"
      destination: "parsed_json"
```

###### Parameters

`source` (optional)

The field containing the JSON data to parse. If omitted, the entire
log message is processed

`destination` (optional)

The field where the parsed JSON will be stored. If omitted, parsed
fields are added to the root level

## Route 53 processor

Parses Route 53 resolver log data into structured fields.

###### Configuration

Configure the Route 53 processor with the following parameters:

```
processor:
  - parse_route53: {}

```

## Key-value processor

Parses key-value pair formatted data into structured fields.

###### Configuration

Configure the key-value processor with the following parameters:

```
processor:
  - key_value:
      source: "message"
      destination: "parsed_kv"
      field_delimiter: "&"
      key_value_delimiter: "="
```

###### Parameters

`source` (optional)

Field containing key-value data. Maximum 128 characters.

`destination` (optional)

Target field for parsed key-value pairs. Maximum 128
characters.

`field_delimiter` (optional)

Pattern to split key-value pairs. Maximum 10 characters.

`key_value_delimiter` (optional)

Pattern to split keys from values. Maximum 10 characters.

`overwrite_if_destination_exists` (optional)

Whether to overwrite existing destination field.

`prefix` (optional)

Prefix to add to extracted keys. Maximum 128 characters.

`non_match_value` (optional)

Value for keys without matches. Maximum 128 characters.

To use the processor without specifying additional parameters, use the following command:

```
processor:
  - key_value: {}
```
