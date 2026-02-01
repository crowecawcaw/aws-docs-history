Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# interval_forbid_composite_literals

## Values (default in bold)

false, **true**

## Description

A session configuration that modifies the value of an interval that contain both YEAR TO MONTH and DAY TO SECOND parts.

If `interval_forbid_composite_literals` is `true`, an error is returned if
an interval with both YEAR TO MONTH and DAY TO SECOND parts is encountered. For example, the following SQL contains an INTERVAL DAY TO SECOND with both
YEAR TO MONTH and DAY TO SECOND parts.

```
`SELECT INTERVAL '1 year 1 day' DAY TO SECOND;`
`ERROR: Interval Day To Second literal cannot contain year-month parts. Disable the GUC interval_forbid_composite_literals to suppress this error and silently discard the year-month part.`
```

If `interval_forbid_composite_literals` is
`false`, Amazon Redshift suppresses an error and truncates the YEAR TO MONTH part from an INTERVAL DAY TO SECOND value.
For example, the following SQL contains an INTERVAL DAY TO SECOND with both YEAR TO MONTH and DAY TO SECOND parts.

```
`SET interval_forbid_composite_literals to "false";
SELECT INTERVAL '1 year 1 day' DAY TO SECOND;`
`intervald2s
------------------------------
1 days 0 hours 0 mins 0.0 secs`
```
