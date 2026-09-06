

# addtotals
<a name="CWL_QuerySyntax-Addtotals"></a>

 Use `addtotals` to compute row totals and column totals for numeric fields. Row totals are computed per-chunk. Column totals (`col=true`) are computed post-merge for correctness across distributed chunks. You can use custom field selection, a custom fieldname, and `row=false` to disable row totals.

**Syntax**

```
| addtotals [fieldname={{Name}}] [row={{bool}}] [col={{bool}}] [{{field1}}, {{field2}}, ...]
```
+ `fieldname={{Name}}` — Sets the name of the row total column. The default is `Total`.
+ `row={{bool}}` — Enable or disable row totals. The default is `true`.
+ `col={{bool}}` — Enable or disable column totals, which adds a summary row at the bottom. The default is `false`.
+ `{{field1}}, {{field2}}, ...` — Optional list of specific fields to sum. If omitted, all numeric fields are summed.

**Examples**

```
# Row totals (default) - adds a Total column summing all numeric fields
fields a, b
| addtotals
```

```
# Sum only specific fields
fields price, tax, qty
| addtotals price, tax
```

```
# Custom total column name
fields val
| addtotals fieldname=RowSum
```

```
# Column totals - adds a Summary row at the bottom
fields x
| addtotals col=true x
```