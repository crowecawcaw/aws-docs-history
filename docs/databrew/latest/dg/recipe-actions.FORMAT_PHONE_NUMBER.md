

# FORMAT\_PHONE\_NUMBER
<a name="recipe-actions.FORMAT_PHONE_NUMBER"></a>

Returns a column in which a phone number string is converted into a formatted value.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `phoneNumberFormat` – The format to convert the phone number to. If no format is specified, the default is `E.164`, an internationally-recognized standard phone number format. Valid values include the following: 
  + `E164` (omit the period after `E`)
+ `defaultRegion` – A valid region code consisting of two or three uppercase letters that specifies the region for the phone number when no country code is present in the number itself. At most, one of `defaultRegion` or `defaultRegionColumn` can be provided.
+ `defaultRegionColumn` – The name of a column of the [advanced data type](projects.adv-data-types.md#projects.adv-data-types.title) `Country`. The region code from the specified column is used to determine the country code for the phone number when no country code is present in the number itself. At most, one of `defaultRegion` or `defaultRegionColumn` can be provided.

**Notes**
+ Inputs that can't be formatted to a valid phone number remain unmodified. 
+ If no default region is provided, and a phone number doesn't start with a plus symbol (\+) and country calling code, the phone number isn't formatted.

**Example**  
  
**Example: Fixed default region**  

```
{
    "Action": {
        "Operation": "FORMAT_PHONE_NUMBER",
        "Parameters": {
            "sourceColumn": "Phone Number",
            "defaultRegion": "US"
        }
    }
}
```
**Example: Default region column option**  

```
{
    "Action": {
        "Operation": "FORMAT_PHONE_NUMBER",
        "Parameters": {
            "sourceColumn": "Phone Number",
            "defaultRegionColumn": "Country Code"
        }
    }
}
```