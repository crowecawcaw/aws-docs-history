# Connecting Microsoft OneDrive to Amazon Q Business (New)

###### Note

**Enhanced Version:** With the new connector, you can
refresh your index significantly faster than before, control the sync scope using a
date filter, automatically discover and index content for all users within your
Microsoft tenant, and enable Q&A capabilities for audio and video files stored
in OneDrive.

## Limitations

The Microsoft OneDrive new connector has the following known limitations:

- No support for syncing OneNote files
- Custom field mappings are not supported
- VPC configuration is not supported
- Document enrichment is not supported
- OneDrive API throttling limits are determined by your organization's
  Microsoft 365 license count and are applied at the application level within
  a tenant (see [this Microsoft documentation](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online#application-throttling "https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online#application-throttling")). These limits affect how many
  documents can be synced in a day, with further restrictions when Access
  Control Lists (ACLs) are involved. For example, in organizations with fewer
  than 1000 licenses, the connector can sync up to 1.2 million documents per
  day without ACLs. However, when syncing with ACLs, this limit is reduced to
  approximately 200,000 documents per day since ACLs require 5 additional
  resource units. If the sync job exceeds these limits, the OneDrive connector
  automatically pauses and resumes the following day to sync the remaining
  documents.
