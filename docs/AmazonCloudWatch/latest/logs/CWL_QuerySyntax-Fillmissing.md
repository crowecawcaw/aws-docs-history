# fillmissing

Use the `fillmissing` command to insert rows for empty time
bins after `stats ... by bin()`. You can optionally fill fields
with a constant value.

###### Syntax

```
| fillmissing [with `value` for `field` [, `value` for `field` ...]]
```

The command uses the following arguments:

- `with `value`for
`field`` (Optional) – The
  constant value to assign to the specified field in the inserted
  rows.

###### Example

The following query fills empty 1-minute bins with 0 for the
`avg_latency` field.

```
fields @timestamp, latency
| stats avg(latency) as avg_latency by bin(1m)
| fillmissing with 0 for avg_latency
```
