# Advanced data types

_Advanced data types_ are data types that DataBrew
detects within a string column in a project by means of pattern matching. When you
click on a string column, the column is flagged as the corresponding advanced data
type if 50% or more of the values in the column meet the criteria for that data type.

The data types DataBrew can detect are:

- Date/timestamp
- SSN
- Phone number
- Email
- Credit card
- Gender
- IP address
- URL
- Zipcode
- Country
- Currency
- State
- City

You can use the following transforms to work with advanced data types:

- [GET_ADVANCED_DATATYPE](recipe-actions.md "recipe-actions.md"): Given a string
  column, identifies the advanced data type of the column, if any.
- [EXTRACT_ADVANCED_DATATYPE_DETAILS](recipe-actions.md "recipe-actions.md"): Extracts
  details for an advanced data type.
- [ADVANCED_DATATYPE_FILTER](recipe-actions.md "recipe-actions.md"): Filters a current
  source column based on advanced data type detection.
- [ADVANCED_DATATYPE_FLAG](recipe-actions.md "recipe-actions.md"): Creates a new flag
  column based on the values for the current source column.
