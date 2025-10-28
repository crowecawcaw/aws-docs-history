# Restrictions for using connectors and connections in

AWS Glue Studio

When you're using custom connectors or connectors from AWS Marketplace, take note of the following
restrictions:

- The testConnection API isn't supported with connections created for custom
  connectors.
- Data Catalog connection password encryption isn't supported with custom connectors.
- You can't use job bookmarks if you specify a filter predicate for a data source node
  that uses a JDBC connector.
- Creating a Marketplace connection is not supported outside of the AWS Glue Studio user interface.
