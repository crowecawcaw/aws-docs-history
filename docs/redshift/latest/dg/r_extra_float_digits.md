Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# extra_float_digits

## Values (default in bold)

**0**, -15 to 2

## Description

Sets the number of digits displayed for floating-point values, including float4 and
float8. The value is added to the standard number of digits (FLT_DIG or DBL_DIG as
appropriate). The value can be set as high as 2, to include partially significant
digits. This is especially useful for outputting float data that must be restored
exactly. Or it can be set negative to suppress unwanted digits.

## Example

The following example sets `extra_float_digits` to `-2`.
First, show the current parameter setting.

```
`show all;`
      `name | setting
--------------------------+----------------
analyze_threshold_percent | 10
datestyle | ISO, MDY
extra_float_digits | 2
query_group | default
search_path | $user, public
statement_timeout | 0
timezone | UTC
wlm_query_slot_count | 1`
```

Then, set the new value to `-2`.

```
set extra_float_digits to -2;
```

Finally show the updated parameter setting.

```
`show all;`
      `name | setting
--------------------------+----------------
analyze_threshold_percent | 10
datestyle | ISO, MDY
extra_float_digits | -2
query_group | default
search_path | $user, public
statement_timeout | 0
timezone | UTC
wlm_query_slot_count | 1`
```
