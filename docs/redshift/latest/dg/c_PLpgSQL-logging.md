

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Logging stored procedures
<a name="c_PLpgSQL-logging"></a>

This topic describes the stored procedures and views that Amazon Redshift uses for stored procedure logging.

Details about stored procedures are logged in the following system tables and views:
+ SVL\_STORED\_PROC\_CALL – details are logged about the stored procedure call's start time and end time, and whether the call is ended before completion. For more information, see [SVL\_STORED\_PROC\_CALL](r_SVL_STORED_PROC_CALL.md).
+ SVL\_STORED\_PROC\_MESSAGES – messages in stored procedures emitted by the RAISE query are logged with the corresponding logging level. For more information, see [SVL\_STORED\_PROC\_MESSAGES](r_SVL_STORED_PROC_MESSAGES.md).
+ SVL\_QLOG – the query ID of the procedure call is logged for each query called from a stored procedure. For more information, see [SVL\_QLOG](r_SVL_QLOG.md).
+ STL\_UTILITYTEXT – stored procedure calls are logged after they are completed. For more information, see [STL\_UTILITYTEXT](r_STL_UTILITYTEXT.md).
+ PG\_PROC\_INFO – this system catalog view shows information about stored procedures. For more information, see [PG\_PROC\_INFO](r_PG_PROC_INFO.md).