# Date and time functions

Date and time functions allow you to perform a wide range of operations on date and time
data, such as extracting parts of a date, performing date calculations, formatting dates and
times, and working with the current date and time. These functions are essential for tasks
such as data analysis, reporting, and data manipulation involving temporal data.

AWS Clean Rooms SQL supports the following date and time functions:

###### Topics

- [ADD_MONTHS function](r_ADD_MONTHS.md "r_ADD_MONTHS.md")
- [CONVERT_TIMEZONE function](CONVERT_TIMEZONE.md "CONVERT_TIMEZONE.md")
- [CURRENT_DATE function](r_CURRENT_DATE_function.md "r_CURRENT_DATE_function.md")
- [DATEADD function](r_DATEADD_function.md "r_DATEADD_function.md")
- [DATEDIFF function](r_DATEDIFF_function.md "r_DATEDIFF_function.md")
- [DATE_PART function](r_DATE_PART_function.md "r_DATE_PART_function.md")
- [DATE_TRUNC function](r_DATE_TRUNC.md "r_DATE_TRUNC.md")
- [EXTRACT function](r_EXTRACT_function.md "r_EXTRACT_function.md")
- [GETDATE function](r_GETDATE.md "r_GETDATE.md")
- [SYSDATE function](r_SYSDATE.md "r_SYSDATE.md")
- [TIMEOFDAY function](r_TIMEOFDAY_function.md "r_TIMEOFDAY_function.md")
- [TO_TIMESTAMP function](r_TO_TIMESTAMP.md "r_TO_TIMESTAMP.md")
- [Date and time functions in
  transactions](#date-functions-transactions "#date-functions-transactions")
- [Date parts for date or timestamp
  functions](r_Dateparts_for_datetime_functions.md "r_Dateparts_for_datetime_functions.md")

## Date and time functions in

transactions

When you run the following functions within a transaction block (BEGIN … END), the
function returns the start date or time of the current transaction, not the start of the
current statement.

- SYSDATE
- TIMESTAMP
- CURRENT_DATE

The following functions always return the start date or time of the current statement,
even when they are within a transaction block.

- GETDATE
- TIMEOFDAY
