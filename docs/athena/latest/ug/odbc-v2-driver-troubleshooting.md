# Troubleshoot the ODBC 2.x driver

If you encounter issues with the Amazon Athena ODBC driver, you can contact Support (in the
AWS Management Console, choose **Support**, **Support Center**).

Be sure to include the following information, and provide any additional details that will
help the support team understand your use case.

- Description – (Required) A description that
  includes detailed information about your use case and the difference between the
  expected and observed behavior. Include any information that can help support
  engineers navigate the issue easily. If the issue is intermittent, specify the
  dates, timestamps, or interval points at which the issue occurred.
- Version information – (Required) Information
  about the driver version, the operating system, and the applications that you used.
  For example, "ODBC driver version 1.2.3, Windows 10 (x64), Power BI."
- Log files – (Required) The minimum number of
  ODBC driver log files that are required to understand the issue. For information
  about logging options for the ODBC 2.x driver, see [Logging options](odbc-v2-driver-logging-options.md "odbc-v2-driver-logging-options.md").
- Connection string – (Required) Your ODBC
  connection string or a screen shot of the dialog box that shows the connection
  parameters that you used. For information about connection parameters, see [Athena ODBC 2.x connection parameters](odbc-v2-driver-connection-parameters.md "odbc-v2-driver-connection-parameters.md").
- Issue steps – (Optional) If possible,
  include steps or a standalone program that can help reproduce the issue.
- Query error information – (Optional) If you
  have errors that involve DML or DDL queries, include the following
  information:
  - A full or simplified version of the failed DML or DDL query.
  - The account ID and AWS Region used, and the query execution ID.

- SAML errors – (Optional) If you have an
  issue related to authentication with SAML assertion, include the following
  information:
  - The identity provider and authentication plugin that was used.
  - An example with the SAML token.
