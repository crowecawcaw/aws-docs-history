# Connecting Google

Drive to Amazon Q Business (Original)

###### Note

This documentation covers the original version of the Google Drive
connector. For new implementations, we recommend using the New Google Drive
connector which offers significantly improved performance. The original connector
remains available for customers requiring specific features not yet supported in
new.

## Known limitations for the

Amazon Q BusinessGoogle Drive connector

The Amazon Q
Google Drive connector has the following known limitations:

- To make a document available to multiple users in Amazon Q Business, you
  need to explicitly add each user by their email address. Only documents with
  specific ACLs, including folder-level ACLs, will be available to your users for
  query responses within Amazon Q. The **Anyone with the
  link** feature is not supported.
- Custom field mapping is not available for Google Drive connector as the Google
  Drive UI does not support creating custom fields.
- Google Drive API does not support retrieving comments from a permanently
  deleted file. Comments are retrievable, however, for trashed files. When a file
  is trashed, the Amazon Q connector will delete comments from the
  Amazon Q index.
- Google Drive API does not return comments present in a .docx file.
