

# Troubleshooting knowledge bases
<a name="troubleshooting-knowledge-bases"></a>

When you encounter issues with your Quick knowledge base, you can use this troubleshooting guide to identify and resolve common problems. Knowledge base issues typically involve document synchronization, refresh job failures, or access permissions.

## Documents don't appear in your knowledge base
<a name="documents-not-appearing"></a>

When documents you expect to see don't appear in your knowledge base, several factors might cause this issue.

**Common causes:**
+ **Sync in progress** – Documents might still be processing. Check the refresh status to confirm the refresh is complete.
+ **Unsupported file format** – Verify your documents are in a supported format. For supported formats and size limits, see [File size and content limits](knowledge-base-integrations.md#file-size-and-content-limits).
+ **File size too large** – Verify the file is within the size limits. For details, see [File size and content limits](knowledge-base-integrations.md#file-size-and-content-limits).
+ **Insufficient access permissions** – Confirm the knowledge base has proper permissions to access the document source.
+ **Document filtering** – Check if filters or exclusion rules prevent certain documents from being indexed.

**To troubleshoot:**

1. Review the refresh history for error messages related to specific documents that failed to sync.

1. Verify your document formats and file sizes meet requirements.

1. Check your access permissions and connection settings.

## Refresh job fails
<a name="refresh-job-fails"></a>

A refresh job typically fails when there's a configuration error in the knowledge base or data source connection.

**Common causes:**
+ **Permission issues** – The integration lacks sufficient permissions to access the data source.
+ **Configuration errors** – Incorrect URLs or data source connection settings.
+ **Resource limitations** – Rate limiting from the source system.

**To resolve:**

1. Check the refresh history details for specific error messages.

1. Verify all connection settings and permissions are correctly configured.

1. Take the recommended action based on the error message.

## Refresh job completes with issues
<a name="refresh-job-completes-with-issues"></a>

When a refresh job completes with issues, the job processed successfully but encountered problems with some documents.

**What this means:**
+ **Partial success** – Some documents synced successfully while others failed.
+ **Document-level errors** – Individual files might have formatting issues, corruption, or access problems.
+ **Metadata issues** – Problems with document metadata or associated information.
+ **Size or format violations** – Some files might exceed size limits or be in unsupported formats.

**To resolve:**

1. Review the detailed refresh reports to identify which documents encountered issues.

1. Address the individual document problems.

1. Run another refresh after resolving the issues.

## Refresh job succeeds but no documents appear
<a name="refresh-job-succeeds-no-documents"></a>

If a refresh job shows as successful but no documents appear in your knowledge base, check these potential causes.

**Common causes:**
+ **Empty source** – The configured data source location contains no documents.
+ **Incorrect path configuration** – The source path or connection settings don't point to the correct location.
+ **Document filters** – Inclusion or exclusion criteria might filter out all documents.
+ **Read permissions missing** – The job connected successfully but lacked permissions to read the actual documents.

**To resolve:**

1. Verify your data source configuration points to the correct location.

1. Confirm documents are present in the specified location.

1. Check that appropriate access permissions are configured.

1. Review any document filters that might exclude content.

## File format issues during refresh
<a name="file-format-issues"></a>

Quick knowledge bases support specific file formats. Files must meet format, size, and character limit requirements. For the full list of supported formats and limits, see [File size and content limits](knowledge-base-integrations.md#file-size-and-content-limits).

**To resolve format issues:**

1. Verify your files meet the format and size requirements.

1. Convert unsupported formats to supported ones.

1. Remove password protection from files.

1. Check that files aren't corrupted.

## Access denied errors
<a name="access-denied-errors"></a>

Access denied errors typically occur due to authentication or authorization issues.

**Common causes:**
+ **Invalid credentials** – Authentication tokens or passwords might have expired.
+ **Insufficient permissions** – The account used in the integration lacks read access to the data source.
+ **Network restrictions** – Firewall or security policies block access.
+ **SSL/TLS issues** – Certificate problems with secure connections.

**To resolve:**

1. **Verify authentication credentials** – Confirm that authentication credentials are current and valid. Edit the integration to re-authenticate and generate a new token.

1. **For web crawler data sources** – Verify that secure connections are properly configured and SSL certificates are properly configured and trusted.

1. **Contact your system administrator** – If you continue experiencing access issues, contact your system administrator. They might need to adjust permissions or security settings.

## ACL validation errors
<a name="acl-validation-errors"></a>

If your sync report shows items with status **SKIPPED** and error type **VALIDATION\_ERROR** with the message "File has no ACL while crawlACL is true, skipping ingestion," the app registration used by your knowledge base connector is missing the required ACL permissions.

**To resolve:**

1. Verify the app registration has the correct API permissions for ACL crawling. The required permissions vary by connector. See the permissions section in your connector's setup documentation.

1. Confirm that admin consent has been granted for all required permissions.

1. Re-run a full sync after fixing permissions.

## Sync run exceeds maximum runtime
<a name="sync-exceeds-maximum-runtime"></a>

If a sync run takes longer than 14 days, Amazon Quick ends the run with a status of **FAILED** and the message *Maximum sync time exceeded*. This typically happens when a knowledge base is configured to crawl more content than can be processed in a single run.

**To resolve:**

1. Edit your knowledge base to reduce the volume of content per sync. Apply include or exclude filters, restrict the file types or folders being crawled, or split the content across multiple knowledge bases.

1. For web crawler data sources, consider using the Web Search feature instead if your goal is to chat with large public websites such as `wikipedia.org`.

1. Run the sync again after narrowing the scope.

For more information about this limit, see [Maximum sync duration](knowledge-base-integrations.md#maximum-sync-duration).