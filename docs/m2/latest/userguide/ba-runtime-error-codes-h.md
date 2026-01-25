AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Error Codes related to CL Command Programs

CL Command pgm error codes, prefixed with `BA-H`.

| Key        | Severity | Text                                                                                                                                                                                          | Additional details |
| ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-H2010` | Fatal    | FILE parameter is required in command RMVM. Provide a valid FILE parameter to the RMVM command. The FILE parameter specifies the file from which the member should be removed.                |                    |
| `BA-H2011` | Fatal    | Unexpected FILE parameter type in command RMVM. Ensure the FILE parameter is provided as a String or RecordAdaptable type. Check the command syntax and parameter types being passed to RMVM. |                    |
| `BA-H2020` | Warn     | File is not a database file. Lock operation ignored in command. Only database files can be locked. The file is a flatfile or does not exist. Verify the file name and library.                |                    |
