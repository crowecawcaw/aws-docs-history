# Transformation processors

Transformation processors modify the structure of log events by adding, copying,
moving, or removing fields.

## add_entries processor

Adds static key-value pairs to log events. At most 1 `add_entries`
processor can be added to a pipeline.

###### Configuration

Configure the add_entries processor with the following parameters:

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

## copy_values processor

Copies values from one field to another. At most 1 `copy_values`
processor can be added to a pipeline.

###### Configuration

Configure the copy_values processor with the following parameters:

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

## delete_entries processor

Removes specified fields from log events.

###### Configuration

Configure the delete_entries processor with the following parameters:

```
processor:
  - delete_entries:
      with_keys: ["temp_field", "debug_info"]
```

###### Parameters

`with_keys` (required)

Array of field names to remove from each log event. Supports nested
field deletion using dot notation.

## move_keys processor

Moves fields from one location to another.

###### Configuration

Configure the move_keys processor with the following parameters:

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
