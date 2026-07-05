Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# spectrum\_query\_maxerror

## Values (default in bold)

**-1**, integer

## Description

You can specify an integer to indicate the maximum number of errors to accept before canceling the query. A negative value turns off maximum error data handling. The results are logged in [SVL\_SPECTRUM\_SCAN\_ERROR](r_SVL_SPECTRUM_SCAN_ERROR.md "r_SVL_SPECTRUM_SCAN_ERROR.md").

## Example

The following example assumes ORC data that contains surplus characters and
characters that are not valid. The column definition for `my_string`
specifies a length of 3 characters. Following is the sample data for this
example:

```
my_string
---------------
abcdef
gh�
ab
```

The following commands set the maximum number of errors to 1 and perform the query.

```
set spectrum_query_maxerror to 1;
SELECT my_string FROM orc_data;
```

The query stops and the results are logged in [SVL\_SPECTRUM\_SCAN\_ERROR](r_SVL_SPECTRUM_SCAN_ERROR.md "r_SVL_SPECTRUM_SCAN_ERROR.md").
