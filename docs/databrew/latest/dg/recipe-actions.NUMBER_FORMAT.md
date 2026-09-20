

# NUMBER\_FORMAT
<a name="recipe-actions.NUMBER_FORMAT"></a>

Returns a column in which a numeric value is converted into a formatted string.

**Parameters**
+ `sourceColumn` – String. The name of an existing column.
+ `decimalPlaces` – Integer. The value of number of digits after the decimal separator.
+ `numericDecimalSeparator` – String. One of the following values indicating the decimal separator:
  + "."
  + ","
+ `numericThousandSeparator` – String. One of the following values indicating the thousand separator:
  + null. Indicates that a thousand separator isn't enabled.
  + ","
  + " "
  + "."
  + "\\\\"
+ `numericAbbreviatedUnit` – String. One of the following values indicating the abbreviation unit:
  + null. Indicates that an abbreviation unit isn't enabled.
  + “THOUSAND”
  + "MILLION"
  + "BILLION"
  + "TRILLION"
+ `numericUnitAbbreviation` – String. One of the following values or any custom value, indicating unit abbreviation:
  + null. Indicates that unit abbreviation isn't enabled.
  + 


<table>
<thead>
  <tr><th>Abbreviation unit</th><th>Options</th></tr>
</thead>
<tbody>
  <tr><td>Thousands</td><td>K, k, M, thousand, custom</td></tr>
  <tr><td>Million</td><td>M, m, MM, million, custom</td></tr>
  <tr><td>Billion</td><td>B, bn, billion, custom</td></tr>
  <tr><td>Trillion</td><td>T, tn, trillion, custom</td></tr>
</tbody>
</table>


**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "NUMBER_FORMAT",
        "Parameters": {
            "sourceColumn": "income",
            "decimalPlaces": "2",
            "numericDecimalSeparator": ".",
            "numericThousandSeparator": ",",
            "numericAbbreviatedUnit": "THOUSAND",
            "numericUnitAbbreviation": "K"
        }
    }
}
```