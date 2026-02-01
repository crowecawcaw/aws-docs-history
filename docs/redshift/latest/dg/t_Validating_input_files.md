Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Validating input data

To validate the data in the Amazon S3 input files or Amazon DynamoDB table before you actually
load the data, use the NOLOAD option with the [COPY](r_COPY.md "r_COPY.md") command. Use NOLOAD with the same COPY commands and options
you would use to load the data. NOLOAD checks the integrity of all of the data without
loading it into the database. The NOLOAD option displays any errors that occur if you
attempt to load the data.

For example, if you specified the incorrect Amazon S3 path for the input file, Amazon Redshift
would display the following error.

```
ERROR:  No such file or directory
DETAIL:
-----------------------------------------------
Amazon Redshift error:  The specified key does not exist
code:      2
context:   S3 key being read :
location:  step_scan.cpp:1883
process:   xenmaster [pid=22199]
-----------------------------------------------
```

To troubleshoot error messages, see the [Load error reference](r_Load_Error_Reference.md "r_Load_Error_Reference.md").

For an example using the NOLOAD option, see
[COPY command with the NOLOAD option](r_COPY_command_examples.md#r_COPY_command_examples-load-noload-option "r_COPY_command_examples.md#r_COPY_command_examples-load-noload-option").
