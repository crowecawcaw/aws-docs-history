# Char To Timestamp(Sys)

The Char to Timestamp function is one of the most frequently-used system functions, because
it lets you create a timestamp out of any correctly formatted input string. Using this function,
you can specify which parts of the timestamp string you wish to use in subsequent processing,
and create a TIMESTAMP value containing only those. To do so, you specify a template that
identifies the parts of the timestamp you want. For example, to use only year and month, you
would specify 'yyyy-MM'.

The input date-time string can contain any parts of a full timestamp ('yyyy-MM-dd
hh:mm:ss'). If all these elements are present in your input string, and 'yyyy-MM-dd hh:mm:ss' is
the template you supply, then the input-string elements are interpreted in that order as year,
month, day, hour, minute, and seconds, such as in '2009-09-16 03:15:24'. The yyyy cannot be
uppercase; the hh can be uppercase to mean using a 24-hour clock.

For the full range of valid specifiers, see [Class SimpleDateFormat](http://docs.oracle.com/javase/7/docs/api/index.html?java/text/SimpleDateFormat.html "http://docs.oracle.com/javase/7/docs/api/index.html?java/text/SimpleDateFormat.html") on the Oracle website.

CHAR_TO_TIMESTAMP uses the template you specify as a parameter in the function call. The
template causes the TIMESTAMP result to use only the parts of the input-date-time value that you
specified in the template. Those fields in the resulting TIMESTAMP contain the corresponding
data taken from your input-date-time string. Fields not specified in your template will use
default values (see below). The format of the template used by CHAR_TO_TIMESTAMP is defined by
the [Class SimpleDateFormat](http://docs.oracle.com/javase/7/docs/api/index.html?java/text/SimpleDateFormat.html "http://docs.oracle.com/javase/7/docs/api/index.html?java/text/SimpleDateFormat.html") on the Oracle website. For more information, see [Date and Time Patterns](sql-reference-parse-timestamp-format.md "sql-reference-parse-timestamp-format.md").

The function-call syntax is as follows:

```
CHAR_TO_TIMESTAMP('<format_string>','<input_date_time_string>')
```

Where <format\_ string> is the template you specify for the parts of
<date_time_string> you want, and <input_date_time_string> is the original string
that is being converted to a TIMESTAMP result.

Note that each string must be enclosed in single quotes and each element of the
<input_date_time_string> must be in the range for its corresponding element in the
template, otherwise no result is returned.

For example, the input-string-element whose position corresponds with MM must be an integer
from 1 to 12, because anything else does not represent a valid month. Similarly, the
input-string-element whose position corresponds with dd must be an integer from 1 to 31, because
anything else does not represent a valid day. (However, if MM is 2, dd cannot be 30 or 31,
because February never has such days.)

For hours, minutes, or seconds, the default starting value is zero, so when those specifiers
are omitted from the template, zeroes are substituted. For months or days, the default starting
value substituted for the omitted parts is 01.

For example, using '2009-09-16 03:15:24' as your input string, you can obtain a TIMESTAMP
containing only the date, with zeros for the other fields such as hours, minutes, or
seconds.

```
 CHAR_TO_TIMESTAMP('yyyy-MM-dd','2009-09-16 03:15:24').

```

The result would is TIMESTAMP 2009-09-16 00:00:00.

If the call had kept hours and minutes in the template while omitting months, days, and
seconds, as illustrated in the following call.

```
--- --- CHAR_TO_TIMESTAMP('yyyy-hh-mm','2009-09-16 03:15:24')

```

Then, the resulting TIMESTAMP would be 2009-01-01 03:15:00.

[Template Strings to
Create Specific Output Timestamps](sql-reference-template-strings-create-output-timestamps.md "sql-reference-template-strings-create-output-timestamps.md") shows further illustrative
examples of templates and input strings used to create the indicated output TIMESTAMPs.

###### Note

Input string MUST use the form 'yyyy-MM-dd hh:mm:ss' or a subset or reordering thereof. As
a result, using an input string like 'Wednesday, 16 September 2009 03:15:24' will NOT work,
meaning that no output will result.

## About Delimiters and Values

Delimiters in the template must match those in the input string and values in the input
string must be acceptable for the template specifiers to which they correspond.

As a general convention, a colon is used to separate hours from minutes, and minutes from
seconds. Similarly, the general convention is to use a dash or slash to separate years from
months and months from days.

For example, the following template has values that line up correctly with the input
string.

```
values (CHAR_TO_TIMESTAMP('MM/dd/yy hh:mm:ss','09/16/11 03:15:24') );
'EXPR$0'
'2011-09-16 03:15:24'
1 row selected

```

If values in the input string are not acceptable for the template specifiers to which they
correspond, the result fails, as in the following example.

```
values (CHAR_TO_TIMESTAMP('MM/dd/yy hh:mm:ss','2009/09/16 03:15:24') );
'EXPR$0'
No rows selected

```

This example returns no rows because 2009 is not an acceptable value for months, which is
the first specifier (MM) in the template.

Omissions in the supplied string can cause the template value 'yyyy' to produce logical
but unintended or unexpected results. The following examples each return an erroneous year,
but one that derives directly from the first element in the supplied string.

```
 VALUES(CHAR_TO_TIMESTAMP('yyyy','09-16 03:15'));
'EXPR$0'
'0009-01-01 00:00:00'
1 row selected
VALUES(CHAR_TO_TIMESTAMP('yyyy','16 03:15'));
'EXPR$0'
'0016-01-01 00:00:00'
1 row selected


```

## Examples Using Templates to Create TIMESTAMPS

The order of the template must match the input string. That means that you cannot specify
"hh" after "yyyy" and expect the method to find the hour automatically. For example, the
following template specifies years first, then hours, then minutes, and returns an erroneous
result.

```
 values (CHAR_TO_TIMESTAMP('yyyy-hh-mm','2009-09-16 03:15:24'));
'EXPR$0'
'2009-01-01 09:16:00'
1 row selected

```

Since the specifiers for months and days are not present in the template, their values in
the input string were ignored, with 01 substituted for both values in the output TIMESTAMP.
The template specified hours and minutes as the second and third input values, so 09 became
the hours and 16 became the minutes. No specifier was present for seconds, so 00 was
used.

The years specifier can be alone or after a delimiter matching the input string shows the
end of the years specifier, with one of the hours:minutes:seconds specifiers.

```
values (CHAR_TO_TIMESTAMP('yyyy','2009-09-16 03:15:24') );
'EXPR$0'
'2009-01-01 00:00:00'
1 row selected

```

In contrast, the template below fails because it has a space-as-delimiter before the "hh"
rather than the dash delimiter used in the input string's date specification.

```
  values (CHAR_TO_TIMESTAMP('yyyy hh','2009-09-16 03:15:24') );
  'EXPR$0'
  No rows selected

```

The four templates below work because they use the same delimiter to separate the years
specifier from the next specifier as is used in the input string's date specification (dash in
the first case, space in the second, slash in the third, and dash in the fourth).

```
values (CHAR_TO_TIMESTAMP('yyyy-hh','2009-09-16 03:15:24') );
'EXPR$0'
'2009-01-01 09:00:00'
1 row selected
values (CHAR_TO_TIMESTAMP('yyyy hh','2009 09 16 03:15:24') );
'EXPR$0'
'2009-01-01 09:00:00'
1 row selected
values (CHAR_TO_TIMESTAMP('yyyy/hh','2009/09/16 03:15:24') );
'EXPR$0'
'2009-01-01 09:00:00'
1 row selected
values (CHAR_TO_TIMESTAMP('yyyy-mm','2009-09-16 03:15:24') );
'EXPR$0'
'2009-01-01 00:09:00'
1 row selected

```

However, if the template specifies months (MM), it cannot then specify hours, minutes, or
seconds unless days are also specified.
