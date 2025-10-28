# Known limitations for the

Box connector

The Amazon Q Box connector has the following known
limitations:

- Crawling data from external folders is not supported.
- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Box API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
