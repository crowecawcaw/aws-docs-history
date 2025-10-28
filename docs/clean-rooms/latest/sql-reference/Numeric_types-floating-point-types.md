# Floating-point types

Use the REAL and DOUBLE PRECISION data types to store numeric values with
_variable precision_. These types are _inexact_
types, meaning that some values are stored as approximations, such that storing and
returning a specific value may result in slight discrepancies. If you require exact
storage and calculations (such as for monetary amounts), use the DECIMAL data
type.

REAL represents the single-precision floating point format, according to the IEEE
Standard 754 for Floating-Point Arithmetic. It has a precision of about 6 digits, and a
range of around 1E-37 to 1E+37. You can also specify this data type as FLOAT4.

DOUBLE PRECISION represents the double-precision floating point format, according to
the IEEE Standard 754 for Binary Floating-Point Arithmetic. It has a precision of about
15 digits, and a range of around 1E-307 to 1E+308. You can also specify this data type
as FLOAT or FLOAT8.
