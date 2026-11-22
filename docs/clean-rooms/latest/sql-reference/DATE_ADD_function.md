

# DATE\_ADD function

The DATE\_ADD function returns the date that is a specified number of days after a start date.

## Syntax
<a name="DATE_ADD_function-synopsis"></a>

```
DATE_ADD(start_date, num_days)
```

## Arguments
<a name="DATE_ADD_function-arguments"></a>

 *start\_date*   
A DATE column or an expression that evaluates to a date.

 *num\_days*   
The number of days to add, as an integer. A positive number adds days, and a negative number subtracts days.

## Return type
<a name="DATE_ADD_function-return-type"></a>

DATE\_ADD returns a DATE.

## Usage notes
<a name="DATE_ADD_usage_notes"></a>

In AWS Clean Rooms Spark SQL, DATE\_ADD adds days only. To add months or years, use a different function, such as [ADD\_MONTHS](ADD_MONTHS.md).

## Examples
<a name="DATE_ADD_function-examples"></a>

The `impressions` table has `event_date` values of `2024-03-01`, `2024-03-15`, and `2024-03-20`. The following example adds 7 days to each date.

```
SELECT user_id,
    DATE_ADD(event_date, 7) AS followup_date
FROM impressions;

user_id | followup_date
--------+--------------
u-100   | 2024-03-08
u-101   | 2024-03-22
u-103   | 2024-03-27
```

The `purchases` table has `purchase_date` values of `2024-03-31`, `2024-03-10`, and `2024-03-12`. The following example subtracts 30 days from each date by using a negative number.

```
SELECT user_id,
    DATE_ADD(purchase_date, -30) AS window_start
FROM purchases;

user_id | window_start
--------+-------------
u-100   | 2024-03-01
u-103   | 2024-02-09
u-101   | 2024-02-11
```