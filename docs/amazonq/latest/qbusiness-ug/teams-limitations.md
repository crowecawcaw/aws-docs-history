Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Known limitations for the Microsoft Teams connector

###### Note

**Original version notice:** We recommend using the new connector for improved performance and retrieval quality. The following limitations apply only to the original connector version.

When you use the test data source connection feature, the Microsoft Teams connector
has a potential issue when testing Identity Crawler. If testing takes longer than five
minutes, Amazon Q skips testing Identity Crawler and moves on to the next
test. A connection error with Identity Crawler is possible even
after finishing connection testing.

The Microsoft Teams connector has these known limitations:

- When you enable Access Control Lists (ACLs), the "Sync only new or modified content" option is not available due to Microsoft Teams API limitations. Use "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs to use this sync mode.
