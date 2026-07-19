# sessionize

Use the `sessionize` command to group events into sessions by
identity fields and an inactivity gap. The command emits a session
identifier field.

###### Syntax

```
| sessionize `field`[, `field` ...] [maxspan `duration`] [AS `out`]
```

The command uses the following arguments:

- `field` – One or more
  identity fields to group by.
- `maxspan
 `duration`` (Optional) – The
  maximum inactivity gap before starting a new session. Default:
  `30m`.
- `AS `out`` (Optional) – The output field name. Default:
  `session_id`.

###### Example

The following query groups events into sessions by user and device
with a 1-hour inactivity gap.

```
fields @timestamp, userId, deviceId
| sessionize userId, deviceId maxspan 1h as my_session
```
