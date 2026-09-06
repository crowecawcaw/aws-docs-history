

# accum
<a name="CWL_QuerySyntax-Accum"></a>

Use the `accum` command to compute a running cumulative sum of a numeric field.

**Syntax**  


```
| accum {{field}} [AS {{out}}]
```

The command uses the following arguments:
+ `{{field}}` – The numeric field to accumulate.
+ `AS {{out}}` (Optional) – An alias for the output field.

**Example**  
The following query computes a running total of bytes.

```
fields @timestamp, bytes
| accum bytes AS totalBytes
```