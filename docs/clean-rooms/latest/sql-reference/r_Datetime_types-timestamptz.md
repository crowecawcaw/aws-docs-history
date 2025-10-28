# TIMESTAMPTZ

Use the TIMESTAMPTZ data type to input complete timestamp values that include the
date, the time of day, and a time zone. When an input value includes a time zone, AWS Clean Rooms
uses the time zone to convert the value to UTC and stores the UTC value.

To view a list of supported time zone names, run the following command.

```
select my_timezone_names();
```

To view a list of supported time zone abbreviations, run the following command.

```
select my_timezone_abbrevs();
```

You can also find current information about time zones in the [IANA Time Zone Database](https://www.iana.org/time-zones "https://www.iana.org/time-zones").

The following table has examples of time zone formats.

| Format                    | Example                           |
| ------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dd mon hh:mi:ss yyyy tz   | 17 Dec 07:37:16 1997 PST          |
| mm/dd/yyyy hh:mi:ss.ss tz | 12/17/1997 07:37:16.00 PST        |
| mm/dd/yyyy hh:mi:ss.ss tz | 12/17/1997 07:37:16.00 US/Pacific |
| yyyy-mm-dd hh:mi:ss+/-tz  | 1997-12-17 07:37:16-08            |
| dd.mm.yyyy hh:mi:ss tz    | 17.12.1997 07:37:16.00 PST        | TIMESTAMPTZ columns store values with up to a maximum of six digits of precision for fractional seconds. If you insert a date into a TIMESTAMPTZ column, or a date with a partial timestamp, the value is implicitly converted into a full timestamp value. This full timestamp value has default values (00) for missing hours, minutes, and seconds. TIMESTAMPTZ values are UTC in user tables. |
