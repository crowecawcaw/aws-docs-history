# outlier

Use the `outlier` command to detect statistical outliers in
numeric fields based on the interquartile range (IQR). You can remove or
clamp outlier rows.

###### Syntax

```
| outlier [action=remove|transform] [param=`n`] [uselower=true|false] [mark=true|false] `field` [`field` ...]
```

The command uses the following arguments:

- `action` (Optional) – Either
  `remove` (drops outlier rows) or
  `transform` (clamps to boundary). Default:
  `transform`.
- `param` (Optional) – The IQR multiplier.
  Default: `2.5`.
- `uselower` (Optional) – Whether to detect
  lower-bound outliers. Default: `false`.
- `mark` (Optional) – Whether to add a boolean
  marker field. Default: `false`.
- `field` – One or more
  numeric fields to check for outliers.

###### Example

The following query removes rows where cpu or memory are outliers,
using a 3.0 IQR multiplier with lower-bound detection and
marking.

```
fields @timestamp, cpu, memory
| outlier action=remove param=3.0 uselower=true mark=true cpu memory
```
