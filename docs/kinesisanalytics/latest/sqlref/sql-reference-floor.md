# FLOOR

```
FLOOR ( <time-unit> )
```

When called with a numeric argument, FLOOR returns the largest integer equal to or smaller
than the input argument.

When called with a date, time, or timestamp expression, FLOOR returns the largest value
equal to or smaller than the input, subject to the precision specified by <time
 unit>.

FLOOR returns null if any input argument is null.

## Examples

| Function                                         | Result                            |
| ------------------------------------------------ | --------------------------------- |
| FLOOR(2.0)                                       | 2                                 |
| FLOOR(-1.0)                                      | -1                                |
| FLOOR(5.2)                                       | 5                                 |
| FLOOR(-3.3)                                      | -4                                |
| FLOOR(-3 \<br>• 3.1)                             | -10                               |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO HOUR)   | TIMESTAMP '2004-09-30 13:00:00'   |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO MINUTE) | TIMESTAMP '2004-09-30 13:48:00'   |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO DAY)    | TIMESTAMP '2004-09-30 00:00:00.0' |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO YEAR)   | TIMESTAMP '2004-01-01 00:00:00.0' |

## Notes

###### Note

FLOOR ( <datetime expression> TO <timeunit> ) is an Amazon Kinesis Data Analytics

extension.

The STEP function is similar to FLOOR but can round values down to arbitrary
intervals, such as 30 seconds. For more information, see [STEP](sql-reference-step.md "sql-reference-step.md").
