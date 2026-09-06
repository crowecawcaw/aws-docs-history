

# logcompare
<a name="CWL_QuerySyntax-Logcompare"></a>

Use the `logcompare` command to compare the current time window against a baseline window shifted back by a specified duration.

**Syntax**  


```
| logcompare timeshift {{duration}}
```

The command uses the following arguments:
+ `timeshift {{duration}}` – The duration to shift back for the baseline window (for example, `7d`).

**Example**  
The following query compares the past day's logs against the same period one week earlier.

```
SOURCE lg start=-1d end=now
| logcompare timeshift 7d
```