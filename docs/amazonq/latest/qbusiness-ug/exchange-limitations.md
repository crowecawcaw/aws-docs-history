

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Microsoft Exchange connector
<a name="exchange-limitations"></a>

**Note**  
**Legacy version notice:** We recommend using the latest connector for improved performance and retrieval quality. The following limitations apply only to the legacy connector version.

The original Microsoft Exchange connector has these known limitations:
+ When you enable Access Control Lists (ACLs), the "Sync only new or modified content" option is not available due to Microsoft Exchange API limitations. Use "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs to use this sync mode.