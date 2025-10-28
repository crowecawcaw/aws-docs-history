# Visualizing metadata table data with

Amazon Quick Suite

With Amazon Quick Suite, you can create interactive dashboards to analyze and visualize SQL query results
about your S3 managed metadata tables. Quick Suite dashboards can help you monitor statistics, track
changes, and get operational insights about your metadata tables.

A dashboard about your journal table might show you:

- What's the percentage of object uploads compared to deletions?
- Which objects were deleted by S3 Lifecycle in the past 24 hours?
- Which IP addresses did the most recent `PUT` requests come from?
  A dashboard about your inventory table might show you:

- How many objects are in different storage classes?
- What percentage of your storage data is small objects compared to large objects?
- What types of objects are in my bucket?
  After you [integrate your S3 table
  buckets](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md") with AWS analytics services, you can create datasets from your metadata tables and
  work with them in Amazon Quick Suite using SPICE or direct SQL queries from your query
  engine. Quick Suite supports Amazon Athena and Amazon Redshift as data sources.

For more information, see [Visualizing table data with
Amazon Quick Suite](s3-tables-integrating-quicksight.md "s3-tables-integrating-quicksight.md").
