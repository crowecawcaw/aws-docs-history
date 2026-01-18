# Tuning Aurora MySQL with thread states

The following table summarizes the most common general thread states for Aurora MySQL.

| General thread state                                 | Description                                                                                                                                               |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [creating sort index](ams-states.md "ams-states.md") | This thread state indicates that a thread is<br>processing a `SELECT` statement that requires the use of an internal temporary<br>table to sort the data. |
| [sending data](ams-states.md "ams-states.md")        | This thread state indicates that a thread is reading and filtering rows for a query to<br>determine the correct result set.                               |
