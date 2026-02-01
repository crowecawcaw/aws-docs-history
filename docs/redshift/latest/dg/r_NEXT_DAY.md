Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# NEXT_DAY function

NEXT_DAY returns the date of the first instance of the specified day that is later than
the given date.

If the _day_ value is the same day of the week as the given date, the
next occurrence of that day is returned.

## Syntax

```
NEXT_DAY( { *date* | *timestamp* }, *day* )
```

## Arguments

_date_ | _timestamp_

A column of data type `DATE` or `TIMESTAMP` or an
expression that implicitly evaluates to a `DATE` or
`TIMESTAMP` type.

_day_

A string containing the name of any day. Capitalization doesn't
matter.

Valid values are as follows.

| Day       | Values                   |
| --------- | ------------------------ |
| Sunday    | Su, Sun, Sunday          |
| Monday    | M, Mo, Mon, Monday       |
| Tuesday   | Tu, Tue, Tues, Tuesday   |
| Wednesday | W, We, Wed, Wednesday    |
| Thursday  | Th, Thu, Thurs, Thursday |
| Friday    | F, Fr, Fri, Friday       |
| Saturday  | Sa, Sat, Saturday        |

## Return type

DATE

## Examples

The following example returns the date of the first Tuesday after
8/20/2014.

```
`select next_day('2014-08-20','Tuesday');`

`next_day
-----------
2014-08-26`
```

The following example returns the date of the first Tuesday after
1/1/2008 at 5:54:44.

```
`select listtime, next_day(listtime, 'Tue') from listing limit 1;`

`listtime | next_day
--------------------+-----------
2008-01-01 05:54:44 | 2008-01-08`
```

The following example gets target marketing dates for the third quarter.

```
`select username, (firstname ||' '|| lastname) as name,
eventname, caldate, next_day (caldate, 'Monday') as marketing_target
from sales, date, users, event
where sales.buyerid = users.userid
and sales.eventid = event.eventid
and event.dateid = date.dateid
and date.qtr = 3
order by marketing_target, eventname, name;`

`username | name | eventname | caldate | marketing_target
----------+-------------------+----------------------+--------------+-------------------
MBO26QSG | Callum Atkinson | .38 Special | 2008-07-06 | 2008-07-07
WCR50YIU | Erasmus Alvarez | A Doll's House | 2008-07-03 | 2008-07-07
CKT70OIE | Hadassah Adkins | Ana Gabriel | 2008-07-06 | 2008-07-07
VVG07OUO | Nathan Abbott | Armando Manzanero | 2008-07-04 | 2008-07-07
GEW77SII | Scarlet Avila | August: Osage County | 2008-07-06 | 2008-07-07
ECR71CVS | Caryn Adkins | Ben Folds | 2008-07-03 | 2008-07-07
KUW82CYU | Kaden Aguilar | Bette Midler | 2008-07-01 | 2008-07-07
WZE78DJZ | Kay Avila | Bette Midler | 2008-07-01 | 2008-07-07
HXY04NVE | Dante Austin | Britney Spears | 2008-07-02 | 2008-07-07
URY81YWF | Wilma Anthony | Britney Spears | 2008-07-02 | 2008-07-07`
```
