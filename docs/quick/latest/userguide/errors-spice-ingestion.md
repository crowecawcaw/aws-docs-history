

# SPICE ingestion error codes
<a name="errors-spice-ingestion"></a>

The following list of errors codes and descriptions can help you understand and troubleshoot issues with data ingestion into SPICE.

## Error codes for skipped rows
<a name="errors-skipped-rows-during-import"></a>

The following list of errors codes and descriptions can help you understand and troubleshoot issues with skipped rows. 

****ARITHMETIC\_EXCEPTION**** – An arithmetic exception occurred while processing a value.

****ENCODING\_EXCEPTION**** – An unknown exception occurred while converting and encoding data to SPICE.

****OPENSEARCH\_CURSOR\_NOT\_ENABLED**** – The OpenSearch domain doesn't have SQL cursors enabled (`"opendistro.sql.cursor.enabled" : "true"`). For more information, see [Authorizing connections to Amazon OpenSearch Service](opensearch.md).

****INCORRECT\_FIELD\_COUNT**** – One or more rows have too many fields. Make sure that the number of fields in each row matches the number of fields defined in the schema.

****INCORRECT\_SAGEMAKER\_OUTPUT\_FIELD\_COUNT**** – The SageMaker AI output has an unexpected number of fields.

****INDEX\_OUT\_OF\_BOUNDS**** – The system requested an index that isn't valid for the array or list being processed.

****MALFORMED\_DATE**** – A value in a field can't be transformed to a valid date. For example, if you try to convert a field that contains a value like `"sale date"` or `"month-1"`, the action generates a malformed date error. To fix this error, remove nondate values from your data source. Check that you aren't importing a file with a column header mixed into the data. If your string contains a date or time that doesn't convert, see [Using unsupported or custom dates](using-unsupported-dates.md).

****MISSING\_SAGEMAKER\_OUTPUT\_FIELD**** – A field in the SageMaker AI output is unexpectedly empty.

****NUMBER\_BITWIDTH\_TOO\_LARGE**** – A numeric value exceeds the length supported in SPICE. For example, your numeric value has more than 19 digits, which is the length of a `bigint` data type. For a long numeric sequence that isn't a mathematical value, use a `string` data type.

****NUMBER\_PARSE\_FAILURE**** – A value in a numeric field is not a number. For example, a field with a data type of `int` contains a string or a float.

****SAGEMAKER\_OUTPUT\_COLUMN\_TYPE\_MISMATCH**** – The data type defined in the SageMaker AI schema doesn't match the data type received from SageMaker AI. 

****STRING\_TRUNCATION**** – A string is being truncated by SPICE. Strings are truncated where the length of the string exceeds the SPICE quota. For more information about SPICE, see [Importing data into SPICE](spice.md). For more information about quotas, see [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html). 

****UNDEFINED**** – An unknown error occurred while ingesting data.

****UNSUPPORTED\_DATE\_VALUE**** – A date field contains a date that is in a supported format but is not in the supported range of dates, for example "12/31/1399" or "01/01/10000". For more information, see [Using unsupported or custom dates](using-unsupported-dates.md). 

## Error codes during data import
<a name="errors-during-import"></a>

For imports and data refresh jobs that fail, Quick Sight provides an error code indicating what caused the failure. The following list of errors codes and descriptions can help you understand and troubleshoot issues with data ingestion into SPICE.

****ACCOUNT\_CAPACITY\_LIMIT\_EXCEEDED**** – This data exceeds your current SPICE capacity. Purchase more SPICE capacity or clean up existing SPICE data and then retry this ingestion.

****CONNECTION\_FAILURE**** – Amazon Quick Sight can't connect to your data source. Check the data source connection settings and try again.

****CUSTOMER\_ERROR**** – There was a problem parsing the data. If this persists, contact Amazon Quick Sight technical support.

****DATA\_SET\_DELETED**** – The data source or dataset was deleted or became unavailable during ingestion.

****DATA\_SET\_SIZE\_LIMIT\_EXCEEDED**** – This dataset exceeds the maximum allowable SPICE dataset size. Use filters to reduce the dataset size and try again. For information on SPICE quotas, see [Data source quotas](data-source-limits.md).

****DATA\_SOURCE\_AUTH\_FAILED**** – Data source authentication failed. Check your credentials and use the **Edit data source** option to replace expired credentials.

****DATA\_SOURCE\_CONNECTION\_FAILED**** – Data source connection failed. Check the URL and try again. If this error persists, contact your data source administrator for assistance.

****DATA\_SOURCE\_NOT\_FOUND**** – No data source found. Check your Amazon Quick Sight data sources.

****DATA\_TOLERANCE\_EXCEPTION**** – There are too many invalid rows. Amazon Quick Sight has reached the quota of rows that it can skip and still continue ingesting. Check your data and try again.

****FAILURE\_TO\_ASSUME\_ROLE**** – Amazon Quick Sight couldn't assume the correct AWS Identity and Access Management (IAM) role. Verify the policies for `Amazon Quick Sight-service-role` in the IAM console.

****FAILURE\_TO\_PROCESS\_JSON\_FILE**** – Amazon Quick Sight couldn't parse a manifest file as valid JSON.

****IAM\_ROLE\_NOT\_AVAILABLE**** – Amazon Quick Sight doesn't have permission to access the data source. To manage Amazon Quick Sight permissions on AWS resources, go to the **Security and Permissions** page under the **Manage Amazon Quick Sight** option as an administrator.

****INGESTION\_CANCELED**** – The ingestion was canceled by the user.

****INGESTION\_SUPERSEDED**** – This ingestion has been superseded by another workflow. This happens when a new ingestion is created while another one is still in progress. Avoid manually editing the dataset multiple times in a short period, because each manual edit creates a new ingestion which will supersede and end the previous ingestion.

****INTERNAL\_SERVICE\_ERROR**** – An internal service error occurred.

****INVALID\_DATA\_SOURCE\_CONFIG**** – Invalid values appeared in connection settings. Check your connection details and try again.

****INVALID\_DATAPREP\_SYNTAX**** – Your calculated field expression contains invalid syntax. Correct the syntax and try again.

****INVALID\_DATE\_FORMAT**** – An invalid date format appeared.

****IOT\_DATA\_SET\_FILE\_EMPTY**** – No AWS IoT Analytics data was found. Check your account and try again.

****IOT\_FILE\_NOT\_FOUND**** – An indicated AWS IoT Analytics file wasn't found. Check your account and try again.

****OAUTH\_TOKEN\_FAILURE**** – Credentials to the data source have expired. Renew your credentials and retry this ingestion.

****PASSWORD\_AUTHENTICATION\_FAILURE**** – Incorrect credentials appeared for a data source. Update your data source credentials and retry this ingestion.

****PERMISSION\_DENIED**** – Access to the requested resources was denied by the data source. Request permissions from your database administrator or ensure proper permission has been granted to Amazon Quick Sight before retrying.

****QUERY\_TIMEOUT**** – A query to the data source timed out waiting for a response. Check your data source logs and try again.

****ROW\_SIZE\_LIMIT\_EXCEEDED**** – The row size quota exceeded the maximum.

****S3\_FILE\_INACCESSIBLE**** – Couldn't connect to an S3 bucket. Make sure that you grant Amazon Quick Sight and users necessary permissions before you connect to the S3 bucket.

****S3\_MANIFEST\_ERROR**** – Couldn't connect to S3 data. Make sure that your S3 manifest file is valid. Also verify access to the S3 data. Both Amazon Quick Sight and the Amazon Quick Sight user need permissions to connect to the S3 data.

****S3\_UPLOADED\_FILE\_DELETED**** – The file or files for the ingestion were deleted (between ingestions). Check your S3 bucket and try again.

****SOURCE\_API\_LIMIT\_EXCEEDED\_FAILURE**** – This ingestion exceeds the API quota for this data source. Contact your data source administrator for assistance.

****SOURCE\_RESOURCE\_LIMIT\_EXCEEDED**** – A SQL query exceeds the resource quota of the data source. Examples of resources involved can include the concurrent query quota, the connection quota, and physical server resources. Contact your data source administrator for assistance.

****SPICE\_TABLE\_NOT\_FOUND**** – An Amazon Quick Sight data source or dataset was deleted or became unavailable during ingestion. Check your dataset in Amazon Quick Sight and try again. For more information, see [Troubleshooting skipped row errors](troubleshooting-skipped-rows.md).

****SQL\_EXCEPTION**** – A general SQL error occurred. This error can be caused by query timeouts, resource constraints, unexpected data definition language (DDL) changes before or during a query, and other database errors. Check your database settings and your query, and try again.

****SQL\_INVALID\_PARAMETER\_VALUE**** – An invalid SQL parameter appeared. Check your SQL and try again.

****SQL\_NUMERIC\_OVERFLOW**** – Amazon Quick Sight encountered an out-of-range numeric exception. Check related values and calculated columns for overflows, and try again.

****SQL\_SCHEMA\_MISMATCH\_ERROR**** – The data source schema doesn't match the Amazon Quick Sight dataset. Update your Amazon Quick Sight dataset definition.

****SQL\_TABLE\_NOT\_FOUND**** – Amazon Quick Sight can't find the table in the data source. Verify the table specified in the dataset or custom SQL and try again.

****SSL\_CERTIFICATE\_VALIDATION\_FAILURE**** – Amazon Quick Sight can't validate the Secure Sockets Layer (SSL) certificate on your database server. Check the SSL status on that server with your database administrator and try again.

****UNRESOLVABLE\_HOST**** – Amazon Quick Sight can't resolve the host name of the data source. Verify the host name of the data source and try again.

****UNROUTABLE\_HOST**** – Amazon Quick Sight can't reach your data source because it's inside a private network. Ensure that your private VPC connection is configured correctly in Enterprise Edition, or allow Amazon Quick Sight IP address ranges to allow connectivity for Standard Edition. 