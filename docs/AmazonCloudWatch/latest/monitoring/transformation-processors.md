# Transformation processors

Transformation processors modify the structure of log events by adding, copying,
moving, or removing fields.

## add\_entries processor

Adds static key-value pairs to log events. At most 1 `add_entries`
processor can be added to a pipeline.

###### Configuration

Configure the add\_entries processor with the following parameters:

```
processor:
  - add_entries:
      entries:
        - key: "environment"
          value: "production"
          overwrite_if_key_exists: false
```

###### Parameters

`entries` (required)

Array of key-value pairs to add to each log event.

`entries[].key` (required)

The field name to add to the log event. Supports nested fields using
dot notation.

`entries[].value` (required)

The static value to assign to the key.

`entries[].overwrite_if_key_exists` (optional)

Boolean flag that determines behavior when the key already exists.
Defaults to false.

`when` (optional)

Processor-level conditional expression. When specified, the
entire processor is skipped if the expression evaluates to false.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

`entries[].when` (optional)

Entry-level conditional expression. When specified, only this
entry is skipped if the expression evaluates to false.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

`entries[].when_else` (optional)

Fallback entry that executes only when none of the other
`when` conditions in the same processor matched.
The expression value identifies which `when`
conditions to consider. Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

## copy\_values processor

Copies values from one field to another. At most 1 `copy_values`
processor can be added to a pipeline.

###### Configuration

Configure the copy\_values processor with the following parameters:

```
processor:
  - copy_values:
      entries:
        - from_key: "user_id"
          to_key: "backup_user"
          overwrite_if_to_key_exists: false
```

###### Parameters

`entries` (required)

Array of copy operations to perform on each log event.

`entries[].from_key` (required)

The field name to copy the value from. Uses dot notation for nested
fields.

`entries[].to_key` (required)

The field name to copy the value to. Will create nested structures if
using dot notation.

`entries[].overwrite_if_to_key_exists` (optional)

Boolean flag controlling behavior when target field already exists.
Defaults to false.

`when` (optional)

Processor-level conditional expression. When specified, the
entire processor is skipped if the expression evaluates to false.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

`entries[].when` (optional)

Entry-level conditional expression. When specified, only this
entry is skipped if the expression evaluates to false.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

`entries[].when_else` (optional)

Fallback entry that executes only when none of the other
`when` conditions in the same processor matched.
The expression value identifies which `when`
conditions to consider. Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

## delete\_entries processor

Removes specified fields from log events.

###### Configuration

Configure the delete\_entries processor with the following parameters:

```
processor:
  - delete_entries:
      with_keys: ["temp_field", "debug_info"]
```

###### Parameters

`with_keys` (required)

Array of field names to remove from each log event. Supports nested
field deletion using dot notation.

`when` (optional)

Conditional expression that determines whether this processor executes.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

## move\_keys processor

Moves fields from one location to another.

###### Configuration

Configure the move\_keys processor with the following parameters:

```
processor:
  - move_keys:
      entries:
        - from_key: "old_field"
          to_key: "new_field"
          overwrite_if_to_key_exists: true
```

###### Parameters

`entries` (required)

Array of move operations. Maximum 5 entries.

`entries[].from_key` (required)

Source field name. Maximum 128 characters.

`entries[].to_key` (required)

Target field name. Maximum 128 characters.

`entries[].overwrite_if_to_key_exists` (optional)

Whether to overwrite existing target field.

`when` (optional)

Processor-level conditional expression. When specified, the
entire processor is skipped if the expression evaluates to false.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

`entries[].when` (optional)

Entry-level conditional expression. When specified, only this
entry is skipped if the expression evaluates to false.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

`entries[].when_else` (optional)

Fallback entry that executes only when none of the other
`when` conditions in the same processor matched.
The expression value identifies which `when`
conditions to consider. Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

## flatten processor

Flattens nested object structures.

###### Configuration

Configure the flatten processor with the following parameters:

```
processor:
  - flatten:
      source: "metadata"
      target: "flattened"
      remove_processed_fields: true
      exclude_keys: ["sensitive_data"]
```

###### Parameters

`source` (required)

Field containing nested object to flatten.

`target` (required)

Target field prefix for flattened keys.

`remove_processed_fields` (optional)

Whether to remove the original nested field after flattening.

`exclude_keys` (optional)

Array of keys to exclude from flattening. Maximum 20 keys, each up to
128 characters.

`when` (optional)

Conditional expression that determines whether this processor executes.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

## lookup processor

Enriches log events with data from a CloudWatch Logs lookup table. The processor matches
fields in your log events against fields in the lookup table and appends specified
fields to your log events. Use this processor for data enrichment scenarios such as
mapping user IDs to user details, product codes to product information, or error
codes to error descriptions. At most 1 `lookup` processor can be added to
a pipeline.

###### Note

If a lookup table is used in a pipeline, you must provide an execution role
with `logs:GetLookupTable` permissions on the table. For more
information, see [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md "pipeline-iam-reference.md").

###### Configuration

Configure the lookup processor with the following parameters:

```
processor:
  - lookup:
      lookup_table: "arn:aws:logs:us-east-1:123456789012:lookup-table:my_lookup_table"
      match_keys:
        - log_key: "src_ip"
          lookup_key: "ip_address"
      entries:
        - source: "hostname"
          target: "src_hostname"
          overwrite_if_exists: true
```

###### Parameters

`lookup_table` (required)

The ARN of the CloudWatch Logs lookup table to use for enrichment. Maximum
length is 2048 characters.

`match_keys` (required)

Array of key pairs that define how to match log event fields to lookup
table fields. Minimum 1, maximum 5 match keys. When multiple match keys
are specified, a lookup table row must match all keys to produce a result
(AND logic).

`match_keys[].log_key` (required)

The field name in the log event to match against. Maximum 128
characters.

`match_keys[].lookup_key` (required)

The column name in the lookup table to match against. Maximum 128
characters.

`entries` (required)

Array of fields to add to the log event from the matching lookup table
row. Minimum 1, maximum 10 entries.

`entries[].source` (required)

The column name in the lookup table to retrieve the value from.
Maximum 128 characters.

`entries[].target` (optional)

The field name to add to the log event. If not specified, the
`source` column name is used as the field name. Maximum 128
characters.

`entries[].overwrite_if_exists` (optional)

Boolean flag that determines behavior when the target field already
exists in the log event. Defaults to false.

`when` (optional)

Conditional expression that determines whether this processor executes.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

###### Example

Consider a lookup table named `network_assets` with the following
rows:

network\_assets lookup table| ip\_address | hostname | owner | location |
| --- | --- | --- | --- |
| 10.0.1.12 | web-server-01 | team-alpha | us-east-1 |
| 10.0.2.45 | db-server-03 | team-beta | us-west-2 |
| 10.0.3.78 | cache-node-07 | team-alpha | eu-west-1 |

Given the following log event:

```
{
  "timestamp": "2026-05-04T12:00:00Z",
  "src_ip": "10.0.2.45",
  "action": "connection_opened",
  "bytes": 2048
}
```

And the following processor configuration:

```
processor:
  - lookup:
      lookup_table: "arn:aws:logs:us-east-1:123456789012:lookup-table:network_assets"
      match_keys:
        - log_key: "src_ip"
          lookup_key: "ip_address"
      entries:
        - source: "hostname"
          target: "src_hostname"
        - source: "owner"
        - source: "location"
          target: "src_region"
          overwrite_if_exists: false
```

The processor produces the following enriched log event:

```
{
  "timestamp": "2026-05-04T12:00:00Z",
  "src_ip": "10.0.2.45",
  "action": "connection_opened",
  "bytes": 2048,
  "src_hostname": "db-server-03",
  "owner": "team-beta",
  "src_region": "us-west-2"
}
```

###### IAM permissions

When a pipeline uses the lookup processor, the pipeline's execution role must
include `logs:GetLookupTable` permission for the referenced table. The
following example policy statement grants this permission:

```
{
  "Effect": "Allow",
  "Action": "logs:GetLookupTable",
  "Resource": "arn:aws:logs:<region>:<account-id>:lookup-table:<table-name>"
}
```

## geoip processor

The geoip processor enriches log events with geographic location data based on
IP addresses. The processor uses MaxMind databases to resolve IP addresses to
geographic information such as city, country, continent, coordinates, and autonomous
system number (ASN) details. Use this processor for network traffic analysis, user
location enrichment, and security investigation scenarios.

###### Configuration

Configure the geoip processor with the following parameters:

```
processor:
  - geoip:
      entries:
        - source: "client_ip"
          target: "client_geo"
          include_fields:
            - "city_name"
            - "country_name"
            - "country_iso_code"
            - "continent_name"
            - "latitude"
            - "longitude"
          when: '.client_ip != "127.0.0.1"'
```

###### Parameters

`entries` (required)

Array of entry objects that define which IP fields to enrich with
geographic data. Minimum 1, maximum 10 entries.

`entries[].source` (required)

The field name in the log event that contains the IP address to look
up. Must reference a valid IPv4 or IPv6 address. Maximum 128
characters.

`entries[].target` (required)

The field name where the processor writes geographic enrichment
data in the log event. Maximum 128 characters.

`entries[].include_fields` (required)

Array of geographic fields to include in the enrichment result.
Minimum 1, maximum 12 fields. The following fields are available:

- `continent_code` – Two-letter continent
  code (for example, "NA").
- `continent_name` – Name of the
  continent (for example, "North America").
- `country_name` – Name of the country
  (for example, "United States").
- `country_iso_code` – ISO 3166-1
  alpha-2 country code (for example, "US").
- `city_name` – Name of the city
  (for example, "Seattle").
- `postal_code` – Postal code associated
  with the IP address location.
- `time_zone` – IANA time zone name
  (for example, "America/Los\_Angeles").
- `latitude` – Latitude coordinate of the
  IP address location.
- `longitude` – Longitude coordinate of
  the IP address location.
- `network` – CIDR notation of the network
  associated with the IP address.
- `asn` – Autonomous system number
  associated with the IP address.
- `asn_organization` – Organization name
  associated with the autonomous system number.

`entries[].when` (optional)

Conditional expression that determines whether this entry executes.
Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

`when` (optional)

Top-level conditional expression that determines whether this processor
executes. Maximum length is 256 characters.
See [Expression syntax for conditional processing](conditional-processing.md "conditional-processing.md").

###### Example

The following example shows a sample log event with IP address fields:

```
{
  "timestamp": "2026-05-04T12:00:00Z",
  "src_ip": "203.0.113.50",
  "dst_ip": "198.51.100.25",
  "action": "ALLOW",
  "bytes": 4096
}
```

The following processor configuration maps both source and destination IP fields
to geographic enrichment targets:

```
processor:
  - geoip:
      entries:
        - source: "src_ip"
          target: "src_geo"
          include_fields:
            - "city_name"
            - "country_name"
            - "country_iso_code"
            - "latitude"
            - "longitude"
            - "asn"
            - "asn_organization"
        - source: "dst_ip"
          target: "dst_geo"
          include_fields:
            - "country_name"
            - "country_iso_code"
```

The processor produces the following enriched log event:

```
{
  "timestamp": "2026-05-04T12:00:00Z",
  "src_ip": "203.0.113.50",
  "dst_ip": "198.51.100.25",
  "action": "ALLOW",
  "bytes": 4096,
  "src_geo": {
    "city_name": "Seattle",
    "country_name": "United States",
    "country_iso_code": "US",
    "latitude": 47.6062,
    "longitude": -122.3321,
    "asn": 16509,
    "asn_organization": "Amazon.com, Inc."
  },
  "dst_geo": {
    "country_name": "Germany",
    "country_iso_code": "DE"
  }
}
```
