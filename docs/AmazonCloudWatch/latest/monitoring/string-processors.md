# String manipulation processors

String processors modify text values within log events through operations like case
conversion, trimming, and pattern matching.

## lowercase_string processor

Converts specified fields to lowercase.

###### Configuration

Configure the lowercase_string processor with the following parameters:

```
processor:
  - lowercase_string:
      with_keys: ["status", "method"]
```

###### Parameters

`with_keys` (required)

Array of field names to convert to lowercase. Only processes string
values.

## uppercase_string processor

Converts specified fields to uppercase.

###### Configuration

Configure the uppercase_string processor with the following parameters:

```
processor:
  - uppercase_string:
      with_keys: ["status_code", "method"]
```

###### Parameters

`with_keys` (required)

Array of field names to convert to uppercase. Only processes string
values.

## trim_string processor

Removes leading and trailing whitespace from specified fields.

###### Configuration

Configure the trim_string processor with the following parameters:

```
processor:
  - trim_string:
      with_keys: ["message", "user_input"]
```

###### Parameters

`with_keys` (required)

Array of field names to trim whitespace from. Only processes string
values.

## substitute_string processor

Performs string substitution using regular expressions.

###### Configuration

Configure the substitute_string processor with the following
parameters:

```
processor:
  - substitute_string:
      entries:
        - source: "message"
          from: "ERROR"
          to: "WARN"
```

###### Parameters

`entries` (required)

Array of substitution operations to perform on each log event.

`entries[].source` (required)

The field to perform string substitution on.

`entries[].from` (required)

The regular expression pattern to match and replace.

`entries[].to` (required)

The replacement string for matched patterns.

## truncate processor

Truncates field values to specified length.

###### Configuration

Configure the truncate processor with the following parameters:

```
processor:
  - truncate:
      source_keys: ["message", "description"]
      length: 100
      start_at: 0
```

###### Parameters

`source_keys` (required)

Array of field names to truncate. Each field name maximum 128
characters.

`length` (optional)

Maximum length after truncation. Range: 1-8192.

`start_at` (optional)

Starting position for truncation. Range: 0-8192. Defaults to 0.

## extract_value processor

Extracts values using regular expressions.

###### Configuration

Configure the extract_value processor with the following parameters:

```
processor:
  - extract_value:
      entries:
        - source: "message"
          target: "extracted_data"
          from: "user=(?<user>\\w+)"
          to: "${user}"
          target_type: "string"
```

###### Parameters

`entries` (required)

Array of extraction operations. Maximum 20 entries.

`entries[].source` (required)

Field to extract from. Maximum 128 characters.

`entries[].target` (required)

Target field for extracted value. Maximum 128 characters.

`entries[].from` (required)

Regular expression pattern. Maximum 128 characters.

`entries[].to` (required)

Replacement pattern with capture groups. Maximum 128
characters.

`entries[].target_type` (optional)

Target data type ("integer", "double", "string", "boolean").

## convert_entry_type processor

Converts field values between different data types.

###### Configuration

Configure the convert_entry_type processor with the following
parameters:

```
processor:
  - convert_entry_type:
      key: "count"
      type: "integer"
```

###### Parameters

`key` (required)

Single field name to convert.

`type` (required)

Target data type. Options: "integer", "double", "string",
"boolean".

## date processor

Parses and formats date/time fields.

###### Configuration

Configure the date processor with the following parameters:

```
processor:
  - date:
      match:
        - key: "timestamp"
          patterns: ["yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'"]
      destination: "@timestamp"
      source_timezone: "UTC"
      destination_timezone: "America/New_York"
```

###### Parameters

`match` (required)

Array of date matching configurations. Maximum 10 entries.

`match[].key` (required)

Field containing the date string. Maximum 128 characters.

`match[].patterns` (required)

Array of date format patterns to try. Maximum 5 patterns, each up to
256 characters.

`destination` (optional)

Single target field for all parsed dates. Maximum 128
characters.

`source_timezone` (optional)

Source timezone for parsing.

`destination_timezone` (optional)

Target timezone for output.

`output_format` (optional)

Output date format. Maximum 64 characters.

`destination_type` (optional)

Output type - "timestampz", "long", or "string".

## dissect processor

Extracts structured data using pattern matching.

###### Configuration

Configure the dissect processor with the following parameters:

```
processor:
  - dissect:
      map:
        message: "%{timestamp} %{level}"
```

###### Parameters

`map` (required)

Field mapping with dissect patterns.

## list_to_map processor

Converts array fields to map structures.

###### Configuration

Configure the list_to_map processor with the following parameters:

```
processor:
  - list_to_map:
      source: "tags"
      key: "name"
      value_key: "value"
      target: "tag_map"
```

###### Parameters

`source` (required)

Field containing array data. Maximum 128 characters.

`key` (required)

Field name to use as map key. Maximum 128 characters.

`value_key` (optional)

Field name to use as map value. Maximum 128 characters.

`target` (optional)

Target field for map structure. Maximum 128 characters.

`flatten` (optional)

Whether to flatten the resulting map.

`flattened_element` (optional)

Which element to use when flattening ("first" or "last").

## rename_keys processor

Renames fields in log events.

###### Configuration

Configure the rename_keys processor with the following parameters:

```
processor:
  - rename_keys:
      entries:
        - from_key: "old_name"
          to_key: "new_name"
          overwrite_if_to_key_exists: true
```

###### Parameters

`entries` (required)

Array of rename operations. Maximum 5 entries.

`entries[].from_key` (required)

Current field name. Maximum 128 characters.

`entries[].to_key` (required)

New field name. Maximum 128 characters.

`entries[].overwrite_if_to_key_exists` (optional)

Whether to overwrite existing target field.

## select_entries processor

Selects only specified fields from events.

###### Configuration

Configure the select_entries processor with the following parameters:

```
processor:
  - select_entries:
      include_keys: ["timestamp", "level", "message"]
```

###### Parameters

`include_keys` (required)

Array of field names to keep. Maximum 50 keys, each up to 128
characters.

## translate processor

Translates field values using lookup tables.

###### Configuration

Configure the translate processor with the following parameters:

```
processor:
  - translate:
      mappings:
        - source: "status_code"
          targets:
            - target: "status_text"
              map:
                "200": "OK"
                "404": "Not Found"
```

###### Parameters

`mappings` (required)

Array of translation configurations. Maximum 10 mappings.

`mappings[].source` (required)

Field to translate. Maximum 128 characters.

`mappings[].targets` (required)

Array of target configurations. Maximum 10 targets.

`mappings[].targets[].target` (required)

Target field name. Maximum 128 characters.

`mappings[].targets[].map` (required)

Translation mapping. Maximum 100 entries, each value up to 512
characters.
