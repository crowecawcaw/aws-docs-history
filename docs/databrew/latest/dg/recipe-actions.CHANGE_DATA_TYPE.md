# CHANGE_DATA_TYPE

Changes the data type of an existing column.

If a column value can’t be converted to the new type, it will be replaced with NULL. This can happen when a string column is converted to an integer column. For example, string "123" will become integer 123, but string "ABC" cannot become a number, so it will be replaced with a NULL value.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `columnDataType` – New type of the column. The following data types are supported:
  - **byte:** 1-byte signed integer numbers. The range of numbers is from -128 to 127.
  - **short:** 2-byte signed integer numbers. The range of numbers is from -32768 to 32767.
  - **int:** 4-byte signed integer numbers. The range of numbers is from -2147483648 to 2147483647.
  - **long:** 8-byte signed integer numbers. The range of numbers is from -9223372036854775808 to 9223372036854775807.
  - **float:** 4-byte single-precision floating point numbers.
  - **double:** 8-byte double-precision floating point numbers.
  - **decimal:** Signed decimal numbers with up to 38 digits total and 18 digits after the decimal point.
  - **string:** Character string values.
  - **boolean:** Boolean type has one of two possible values: `true` and `false` or `yes` and `no`.
  - **timestamp:** Values comprising fields year, month, day, hour, minute, and second.
  - **date:** Values comprising fields year, month and day.

###### Example

```
{
    "RecipeAction": {
        "Operation": "CHANGE_DATA_TYPE",
        "Parameters": {
            "sourceColumn": "columnName",
            "columnDataType": "boolean"
        }
    }
 }
```
