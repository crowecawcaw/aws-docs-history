After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Fill and filter operations in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

The data produced after summarizing bars could have missing bars where no data was collected or contain data that is not desired to be used in the next stage.
The objective of this stage is to prepare a dataset with evenly spaced intervals and filter out any data outside desired time window. Fill and Filter
are available in the `aws.finspace.timeseries.spark.prepare` module.

## Fill and filter functions

```
 aws.finspace.timeseries.spark.prepare.time_bar_fill_and_filter(data, timebar_column_name, business_calendar, time-bar_spec, start_date,
   end_date, fill_value=None, start_time=None, end_time=None)
```

The data produced after summarizing bars could have missing bars where no data was collected or contain data that is not desired to be used in the next stage.
The objective of this stage is to prepare a dataset with evenly spaced intervals and filter out any data outside desired time window.
Fill and Filter are available in the `aws.finspace.timeseries.spark.prepare` module.

The Fill and filter function will fill with nulls in all rows that need to exist,
and filter all rows that are outside the business calendar date/time range in a given calendar.

**Parameters**

- `data` (DataFrame) – input dataframe
- `timebar_column_name` (str) – name of the timebar column to fill against
- `business_calendar` (AbstractCalendar) – business calendar
- `timebar_spec` (TimeBarSpec) – time bar input spec associated with the bars that were created. it provides the bar frequency
- `start_date` (date) – start of date
- `end_date` (date) – end date
- `fill_value` (Optional[float]) – value to fill
- `start_time` (Optional[time]) – start time of the day
- `end_time` (Optional[time]) – end time of the day

**Return type**
`DataFrame`

**Returns**
`DataFrame`

## Calendars module

Use the calendar module for defining a calendar schedule to be used in fill and filter.

### Abstract calendar

```
class aws.finspace.finance.calendars.AbstractCalendar
Bases: object
```

Defines abstract class for calendars.

```
DISRUPTIONS = 'DISRUPTIONS'
EARLY_CLOSINGS = 'EARLY_CLOSING'
EARLY_CLOSING_TIME = datetime.time(13, 30)
END_OF_TRADING = 'END_OF_TRADING'
HOLIDAYS = 'HOLIDAYS'
START_OF_TRADING = 'START_OF_TRADING'
TZINFO ='TZINFO'
```

### Create schedule

```
create_schedule_from_to(from_date, to_date, time_bar_spec_window_duration, from_time=None, to_time=None, tzinfo=<UTC>)
Abstract method, provide override
```

Creates a list of dates associated with a particular type of calendar.

**Parameters**

- `from_date`(date) – from date
- `to_date` (date) – to date
- `time_bar_spec_window_duration` (str) –
- `from_time` (Optional[time]) – from time
- `to_time` (Optional[time]) – to time

**Return type**
`array`

**Returns** raw_calendar_data()

Return type `Dict[str,Any]`

Returns raw calendar data

### NYSE calendar

```
class aws.finspace.finance.calendars.NYSECalendar20192020
Bases: aws.finspace.finance.calendars.USEndOfDayCalendarActAct_NoWeekends
```

Returns a holiday calendar with no weekends, and according to the NYSE exchange trading holidays and half-days for
[2019](https://www.tradinghours.com/exchanges/nyse/market-holidays/2019 "https://www.tradinghours.com/exchanges/nyse/market-holidays/2019") and [2020](https://www.tradinghours.com/exchanges/nyse/market-holidays/2020 "https://www.tradinghours.com/exchanges/nyse/market-holidays/2020").

```
create_schedule_from_to(from_date, to_date, time_bar_spec_window_duration, from_time=None, to_time=None)
```

**Parameters**

- `from_date` (date) – from date
- `to_date` (date) – to date
- `time_bar_spec_window_duration` (str)
- `from_time` (Optional[time]) – from time
- `to_time` (Optional[time]) – to time
- `tzinfo` – time to localize to

**Return type**
`array`

**Returns** raw_calendar_data()

Return type `Dict[str,Any]`

Returns raw calendar data

### End of day calendar actual

```
class aws.finspace.finance.calendars.USEndOfDayCalendarActAct_NoWeekends
Bases: aws.finspace.finance.calendars.AbstractCalendar
```

Return 30/360 calendar, without weekends, without exchange hours.

```
create_schedule_from_to(from_date, to_date, time_bar_spec_window_duration, from_time=None, to_time=None)
```

**Parameters**

- `from_date` (date) – from date
- `to_date` (date) – to date
- `time_bar_spec_window_duration` (str)
- `from_time` (Optional[time]) – from time
- `to_time` (Optional[time]) – to time
- `tzinfo` – time to localize to

**Return type**
`array`

**Returns** raw_calendar_data()

Return type `Dict[str,Any]`

Returns raw calendar data
