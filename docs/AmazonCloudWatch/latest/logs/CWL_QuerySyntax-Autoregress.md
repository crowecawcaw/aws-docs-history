# autoregress

Use the `autoregress` command to create lagged (previous-row)
copies of a field's values. This is the lag/lead equivalent for
CloudWatch Logs Insights.

###### Syntax

```
| autoregress `field` [AS `alias`] [p=`start`[-`end`]]
```

The command uses the following arguments:

- `field` – The field to
  create lag values for.
- `AS `alias`` (Optional) – An alias for the output field.
- `p=`N`` (Optional) – Single lag depth (default 1). Use
 `p=`N`-`M``
  for a range of lags.

###### Example

The following query creates four lag fields
(`bytes_p1` through `bytes_p4`).

```
fields @timestamp, bytes
| autoregress bytes p=1-4
```
