# Parser processors

Parser processors convert raw or semi-structured log data into structured formats.
Each pipeline can have at most one primary parser processor, which must be the first
processor in the pipeline. The XML parser is an exception: it operates on fields
produced by a primary parser and you can add at most 5 instances to a single
pipeline.

###### Conditional processing not supported

Parser processors (except Grok and XML) do not support conditional processing with
the `when` parameter. This includes OCSF, CSV, JSON, KeyValue, VPC, Route53, RDS, WAF,
Postgres, and Amazon CloudFront parsers. For more information, see
[Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

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

| Pipeline Source Type                      | Supported Schemas                          | Version | Mapping Version |
| ----------------------------------------- | ------------------------------------------ | ------- | --------------- |
| `cloudwatch_logs`                         | `cloud_trail:`                             | `1.5`   | Not required    |
| `cloudwatch_logs`                         | `route53_resolver:`                        | `1.5`   | Not required    |
| `cloudwatch_logs`                         | `vpc_flow:`                                | `1.5`   | Not required    |
| `cloudwatch_logs`                         | `eks_audit:`                               | `1.5`   | Not required    |
| `cloudwatch_logs`                         | `aws_waf:`                                 | `1.5`   | Not required    |
| `cloudwatch_logs`                         | `aws_nlb:`                                 | `1.5`   | Not required    |
| `s3`                                      | Any OCSF schema                            | Any     | Any             |
| `microsoft_office365`                     | `microsoft_office365:`                     | `1.5`   | `1.5.0`         |
| `microsoft_entraid`                       | `microsoft_entraid:`                       | `1.5`   | `1.5.0`         |
| `microsoft_windows_event`                 | `microsoft_windows_event:`                 | `1.5`   | `1.5.0`         |
| `paloaltonetworks_nextgenerationfirewall` | `paloaltonetworks_nextgenerationfirewall:` | `1.5`   | `1.5.0`         |
| `okta_auth0`                              | `okta_auth0:`                              | `1.5`   | `1.5.0`         |
| `okta_sso`                                | `okta_sso:`                                | `1.5`   | `1.5.0`         |
| `crowdstrike_falcon`                      | `crowdstrike_falcon:`                      | `1.5`   | `1.5.0`         |
| `github_auditlogs`                        | `github_auditlogs:`                        | `1.5`   | `1.5.0`         |
| `sentinelone_endpointsecurity`            | `sentinelone_endpointsecurity:`            | `1.5`   | `1.5.0`         |
| `servicenow_cmdb`                         | `servicenow_cmdb:`                         | `1.5`   | `1.5.0`         |
| `wiz_cnapp`                               | `wiz_cnapp:`                               | `1.5`   | `1.5.0`         |
| `zscaler_internetaccess`                  | `zscaler_internetaccess:`                  | `1.5`   | `1.5.0`         |

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
name up to 128 characters. If not provided, defaults to column\_1, column\_2, and so on.

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

`when` (optional)

Conditional expression that determines whether this processor executes.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

###### Important

If the Grok processor is used as the parser (first processor) in a
pipeline and its `when` condition evaluates to false, the
entire pipeline does not execute for that log event. Parsers must run
for downstream processors to receive structured data.

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

## Amazon RDS processor

Parses Amazon RDS Aurora log data into structured fields. The `parse_rds`
processor is supported only when the pipeline's
`data_source_name` is `amazon_rds`. It applies the parsing
logic that matches the pipeline's `data_source_type`.

###### Configuration

Configure the Amazon RDS processor with the following parameters:

```
processor:
  - parse_rds: {}
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

## XML parser

Use the XML parser to convert a specified field that contains an XML string
to JSON format. Use the XML parser when your log events contain embedded XML
fields that you want to query as structured data. The XML parser operates on a
named field that already contains an XML string. Place this parser after a
primary parser in the pipeline. You can add at most 5 `parse_xml`
parsers to a single pipeline.

###### Configuration

Configure the XML parser with the following parameters:

```
processor:
  - parse_json:
      source: "@message"
  - parse_xml:
      source: "body"
      destination: "parsed_xml"
```

###### Parameters

`source` (Required)

Specifies the field that contains the XML string to parse. Use dot
notation to access nested fields. For example,
`event.body`. Maximum 128 characters.

`destination` (Optional)

Specifies the field where the parsed XML structure is stored. If
you omit this parameter, the parsed fields are added to the root
level. Maximum 128 characters.

`when` (Optional)

A conditional expression that determines whether this parser runs.
Maximum length is 256 characters. For more information, see
[Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

###### Example – XML parser output

Given the following JSON log event with an embedded XML field:

```
{
  "body": "<Person id=\"123\" active=\"true\"><name>John</name><age>30</age></Person>"
}
```

With the following configuration:

```
processor:
  - parse_json:
      source: "@message"
  - parse_xml:
      source: "body"
      destination: "parsed_xml"
```

The XML parser produces the following output:

```
{
  "body": "<Person id=\"123\" active=\"true\"><name>John</name><age>30</age></Person>",
  "parsed_xml": {
    "id": "123",
    "active": "true",
    "name": "John",
    "age": "30"
  }
}
```

###### Behavior notes

Nesting depth

The XML parser supports a maximum nesting depth of 25 levels.
Elements nested beyond this limit produce an error.

Error handling

Malformed XML does not fail the pipeline. The parser preserves the
original `@message` and sets
`@pipeline.processing.status = "error"` on the
event.
