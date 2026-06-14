# NUMBER_FORMAT

Returns a column in which a numeric value is converted into a formatted string.

###### Parameters

- `sourceColumn` – String. The name of an existing column.
- `decimalPlaces` – Integer. The value of number of digits after the
  decimal separator.
- `numericDecimalSeparator` – String. One of the following values
  indicating the decimal separator:

  - "."
  - ","

- `numericThousandSeparator` – String. One of the following
  values indicating the thousand separator:

  - null. Indicates that a thousand separator isn't enabled.
  - ","
  - " "
  - "."
  - "\\"

- `numericAbbreviatedUnit` – String. One of the following
  values indicating the abbreviation unit:

  - null. Indicates that an abbreviation unit isn't enabled.
  - “THOUSAND”
  - "MILLION"
  - "BILLION"
  - "TRILLION"

- `numericUnitAbbreviation` – String. One of the following
  values or any custom value, indicating unit abbreviation:

  - null. Indicates that unit abbreviation isn't enabled.
  - | Abbreviation unit | Options                   |
    | ----------------- | ------------------------- |
    | Thousands         | K, k, M, thousand, custom |
    | Million           | M, m, MM, million, custom |
    | Billion           | B, bn, billion, custom    |
    | Trillion          | T, tn, trillion, custom   |

###### Example

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
