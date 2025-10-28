# Understand error codes in the Amazon Q BusinessGoogle Drive connector

The following table provides information about error codes you may see for the
Google Drive connector and suggested resolutions.

| Error code | Error message                                                                    | Suggested resolution                                                                  |
| ---------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| GDL-5101   | The authentication credentials in your data source configuration are invalid.    | Verify your Google service account credentials or OAuth 2.0 tokens and try again.     |
| GDL-5102   | The authentication type in your data source configuration is missing or invalid. | Enter valid authentication type (Google Service Account or OAuth 2.0) and try again.  |
| GDL-5103   | Access denied to Google Drive API.                                               | Ensure your service account has proper domain-wide delegation and API access enabled. |
| GDL-5104   | Rate limit exceeded for Google Drive API.                                        | Wait and retry. Consider reducing sync frequency if the issue persists.               |
| GDL-5105   | Invalid folder or file ID specified in filters.                                  | Verify the folder or file IDs in your inclusion/exclusion filters are correct.        |
