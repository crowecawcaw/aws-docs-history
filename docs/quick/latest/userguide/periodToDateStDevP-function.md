

# periodToDateStDevP
<a name="periodToDateStDevP-function"></a>

The `periodToDateStDevP` function calculates the population standard deviation of the set of numbers in the specified measure, for a given time granularity (for instance, a quarter) up to a point in time, based on a sample in that period.

## Syntax
<a name="periodToDateStDevP-function-syntax"></a>

```
periodToDateStDevP(
	measure, 
	dateTime, 
	period, 
	endDate (optional))
```

## Arguments
<a name="periodToDateStDevP-function-arguments"></a>

 *measure*   
The argument must be a field. Null values are omitted from the results. Literal values don't work.

 *dateTime*   
The Date dimension over which you're computing PeriodToDate aggregations.

 *period*   
The time period across which you're computing the computation. Granularity of `YEAR` means `YearToDate` computation, `Quarter` means `QuarterToDate`, and so on. Valid granularities include `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, and `SECONDS`.

 *endDate*   
(Optional) The date dimension that you're ending computing periodToDate aggregations. It defaults to `now()` if omitted.

## Example
<a name="periodToDateStDevP-function-example"></a>

The following example calculates the week-to-date minimum fare amount per payment type, for the week of 06-30-21. For simplicity in the example, we filtered out only a single payment. 06-30-21 is Wednesday. Quick begins the week on Sundays. In our example, that is 06-27-21.

```
periodToDateStDevP(fare_amount, pickUpDatetime, WEEK, parseDate("06-30-2021", "MM-dd-yyyy"))
```

![This is an image of the results from the example calculation.](http://docs.aws.amazon.com/quick/latest/userguide/images/PTDStDevPResults.png)
