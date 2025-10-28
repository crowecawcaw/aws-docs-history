# Known limitations for the Amazon Q Jira connector

The Amazon Q Jira connector has the following known
limitations:

- Deleted Issues in Jira are not available through
  Jira APIs. The Amazon Q Jira connector
  won't be able to fetch information about deleted Jira issues
  during incremental syncs.
- Private and Empty projects aren't crawled by the Amazon Q
  Jira connector.
