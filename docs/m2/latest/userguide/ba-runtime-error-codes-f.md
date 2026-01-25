AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age Runtime Error codes related to Files

Files error codes, prefixed with `BA-F`. These errors are related to files operations including ESDS and GDG (Generation Data Groups).

## GDG (Generation Data Groups)

| Key        | Severity | Text                                                                                                                | Additional details |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BA-F2000` | Error    | Failed to process GDG deletion event. Verify the GDG file path is valid and the event queue is properly configured. |                    |
| `BA-F2001` | Warn     | Cannot extract filename from path. Verify the GDG file path format is correct.                                      |                    |
