# Math functions

Math functions are pre-defined mathematical operations used within SQL queries to
perform calculations on numerical data. They provide ways to manipulate and transform
data without needing to extract it from the database and process it separately.

| Math functions | **Function**                                                            | **Signature**                                | **Description**                                               |
| -------------- | ----------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `POWER`        | POWER (int                                                              | double, int                                  | double)                                                       | Returns the value of first argument raised to the power of the second argument. |
| `ROUND`        | <br>• ROUND (int                                                        | double, decimal_places_int) <br>• ROUND (int | double)                                                       | Rounds to the nearest integer.                                                  |
| `FLOOR`        | FLOOR (int                                                              | double)                                      | Returns the largest integer not greater than the value given. | Examples of all functions:                                                      |
| **Function**   | **Example**                                                             |                                              | ---                                                           | ---                                                                             |
| POWER          | <br>• `POWER (3, 77)` <br>• `POWER (2.3, 3.9)` <br>• `POWER (1.0, 4.2)` |                                              | ROUND                                                         | `ROUND (32.12435, 3)`                                                           |
|                | FLOOR                                                                   | `FLOOR (21.2)`                               |
