# Connecting Microsoft

OneDrive to Amazon Q Business (Original)

###### Note

**Original version notice:** This documentation
covers the original version of the Microsoft OneDrive connector. For
new implementations, we recommend using the new connector which offers improved
performance. The original connector remains available for customers requiring
specific features not yet supported in the new connector.

## Limitations

When using the test data source connection feature, the Microsoft OneDrive connector
has a potential issue when testing Identity Crawler. If it takes longer than five
minutes, Amazon Q skips testing Identity Crawler, and moves on to the next
test. Thus, it is possible for there to be a connection error with Identity Crawler even
after finishing connection testing.

The Microsoft OneDrive original connector has the following known limitations:

- No support for syncing OneNote files
- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Microsoft OneDrive API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
