

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Known limitations for the Amazon Q Jira connector
<a name="jira-limitations"></a>

The Amazon Q Jira connector has the following known limitations:
+ Deleted Issues in Jira are not available through Jira APIs. The Amazon Q Jira connector won't be able to fetch information about deleted Jira issues during incremental syncs.
+ Private and Empty projects aren't crawled by the Amazon Q Jira connector.