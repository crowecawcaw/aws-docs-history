

# cidrlookup
<a name="CWL_QuerySyntax-Cidrlookup"></a>

Use the `cidrlookup` command to enrich events by matching an IP field against CIDR ranges in a lookup table.

**Syntax**  


```
| cidrlookup {{table}} {{ipField}} [AS {{cidrColumn}}]
    OUTPUT|OUTPUTNEW {{lookupField}} [AS {{eventField}}] [, ...]
```

The command uses the following arguments:
+ `{{table}}` – The name of the lookup table containing CIDR ranges.
+ `{{ipField}}` – The event field containing the IP address to match.
+ `AS {{cidrColumn}}` (Optional) – The column in the lookup table that contains the CIDR ranges.
+ `OUTPUT|OUTPUTNEW` – Use `OUTPUT` to overwrite existing fields, or `OUTPUTNEW` to fill only empty fields.
+ `{{lookupField}}` – One or more fields from the lookup table to add to the event.

**Example**  
The following query enriches events with region, owner, and datacenter from a network lookup table.

```
fields @timestamp, srcAddr
| cidrlookup net_table srcAddr OUTPUT region, owner, datacenter
```