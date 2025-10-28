# Data types

The data for each column of your dataset are converted to one of the following data types:

- **byte** – 1-byte signed integer numbers. The
  range of numbers is from -128 to 127.
- **short** – 2-byte signed integer numbers. The
  range of numbers is from -32768 to 32767.
- **integer** – 4-byte signed integer numbers. The
  range of numbers is from -2147483648 to 2147483647.
- **long** – 8-byte signed integer numbers. The
  range of numbers is from -9223372036854775808 to 9223372036854775807.
- **float** – 4-byte single-precision floating point numbers.
- **double** – 8-byte double-precision floating point numbers.
- **decimal** – Signed decimal numbers with up to 38 digits
  total and 18 digits after the decimal point.
- **string** – Character string values.
- **boolean** – Boolean type has one of two possible
  values: `true` and `false` or `yes` and `no`.
- **timestamp** – Values comprising fields
  year, month, day, hour, minute, and second.
- **date** – Values comprising fields year, month and day.

## Advanced data types

_Advanced data types_ are data types that
DataBrew detects within a string column in a project, and therefore are not part
of a dataset. For information about advanced data types, see
[Advanced data types](projects.md#projects.adv-data-types.title "projects.md#projects.adv-data-types.title").
