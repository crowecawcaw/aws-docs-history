

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.NUMBER_FORMAT.html)

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