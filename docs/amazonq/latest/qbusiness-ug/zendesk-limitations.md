# Known limitations for the Zendesk

connector

The Zendesk connector has the following known limitations:

- Deleted and archived articles and their comments and attachments aren't supported in
  **Change log** mode since there are no SDK methods/REST API available
  for fetching deleted or archived articles.
- Archived articles aren't supported in **Full Crawl** mode since there
  are no SDK methods/REST API available for fetching archived articles.
- Deleted community topics, community posts, and their comments are not supported in
  **Change Log** mode since there are no SDK methods/REST API available
  for fetching deleted topics, deleted posts, and their comments.
- The Zendesk connector can't fetch community topics (added, edited, or
  deleted), and community posts and their comments (added, edited, or deleted) based on
  timestamps in **Change log** mode.
- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Zendesk API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
