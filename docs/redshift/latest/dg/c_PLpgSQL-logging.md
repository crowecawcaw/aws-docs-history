Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Logging stored procedures

This topic describes the stored procedures and views that Amazon Redshift uses for stored procedure logging.

Details about stored procedures are logged in the following system tables and
views:

- SVL_STORED_PROC_CALL – details are logged about the stored procedure call's start
  time and end time, and whether the call is ended before completion. For more
  information, see [SVL_STORED_PROC_CALL](r_SVL_STORED_PROC_CALL.md "r_SVL_STORED_PROC_CALL.md").
- SVL_STORED_PROC_MESSAGES – messages in stored procedures emitted by the RAISE query are logged with the corresponding logging level.
  For more information, see [SVL_STORED_PROC_MESSAGES](r_SVL_STORED_PROC_MESSAGES.md "r_SVL_STORED_PROC_MESSAGES.md").
- SVL_QLOG – the query ID of the procedure call is logged for each query called from a stored procedure.
  For more information, see [SVL_QLOG](r_SVL_QLOG.md "r_SVL_QLOG.md").
- STL_UTILITYTEXT – stored procedure calls are logged after they are completed.
  For more information, see [STL_UTILITYTEXT](r_STL_UTILITYTEXT.md "r_STL_UTILITYTEXT.md").
- PG_PROC_INFO – this system catalog view shows information about stored procedures. For
  more information, see [PG_PROC_INFO](r_PG_PROC_INFO.md "r_PG_PROC_INFO.md").
