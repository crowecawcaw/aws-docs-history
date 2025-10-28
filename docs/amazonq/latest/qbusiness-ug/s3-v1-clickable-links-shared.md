# Clickable URLs

The Clickable URL feature allows end users to access source documents through citation
links in chat responses, regardless of whether a source URI is configured.

This feature improves the verification experience by making all documents of supported
datasource types accessible. Currently, clickable links are only supported for Amazon S3,
custom connectors, file upload and direct `BatchPutDocument` ingestion of
documents.

**Configuration Requirements:** While this feature works
automatically for new applications, existing customers may need additional
configuration:

- If you already use Amazon S3 data source for your Amazon Q Business application, you will need to perform a full sync of the
  data source for the clickable URLs feature to be available to your users.
- If you already use an Amazon Q Business web experience, you may need to
  add additional permissions to the IAM role for the web experience. See the
  troubleshooting section below for details.
  **Download Concurrency Limit:** For information about
  file size limits, see [Quotas and regions](quotas-regions.md "quotas-regions.md").

**Access Control:** The Clickable URL respects all access
control settings:

- If a user's access to a file is revoked after they've viewed it in a chat,
  once a resync is performed subsequent attempts to access the file will be denied
  with a clear error message.
- If a file is updated after a chat reference, then once a resync is performed
  clicking the link will retrieve the current version of the file.
- If a file is deleted and a resync is performed users will receive a clear
  error message indicating the file no longer exists.
