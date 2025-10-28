# Optimizing query performance for

Amazon OpenSearch Service data sources

Query performance in Amazon OpenSearch Service might slow down when you’re accessing external data
sources. This can be due to factors like network latency, data transformation, or large
data volumes. To improve performance, consider indexing select amounts of data depending
on the use case:

- Speeding up direct queries on Amazon S3 (skipping index)
- Building dashboard visualizations on and Security Lake (materialized views)
- Ingesting query results using indexed views for offline review or improved
  performance on Security Lake (materialized views)
  For full documentation on accelerated queries, including example queries, see [Optimize query performance using OpenSearch indexing](https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/ "https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/") in the open source
  documentation.

###### Topics

- [Skipping indexes](#skipping-index "#skipping-index")
- [Materialized views](#materialized-view "#materialized-view")
- [Covering indexes](#covering-index "#covering-index")

## Skipping indexes

A skipping index ingests only the metadata of data stored in Amazon S3. When you query
a table with a skipping index, the query planner uses the index to rewrite the
query, efficiently identifying the location of the data without scanning all
partitions and files. This approach helps narrow down the exact location of the
stored data.

There are two ways to create a skipping index. The first way is to autogenerate
the skipping index from within data source details. The second is to use Query
Workbench to manually create the skipping index using a SQL statement.

To autogenerate a skipping index from your data source, go to **Dashboard
management** and **Accelerate data**, then select your
database and table (you might need to refresh to get the latest databases and
tables). You can then choose **Generate** to
autogenerate a skipping index, or manually select each field you want to index and
specify the acceleration (skipping index type). Lastly, choose **Create acceleration** to create a reoccurring job that populates the
new skipping index.

Skipping indexes are supported only for Amazon S3 data sources.

For more information about setting up skipping indexes using Query Workbench, see
[Skipping indexes](https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/#skipping-indexes "https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/#skipping-indexes") in the OpenSearch documentation.

## Materialized views

Materialized views use complex queries, such as aggregations, to support
OpenSearch Dashboards visualizations. They ingest a subset of your data based on the
query and store it in an OpenSearch index. You can then use this index to create
visualizations.

Materialized views are supported for Amazon S3 and Security Lake data sources.

For more information about setting up materialized views using Query Workbench,
see [Materialized views](https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/#materialized-views "https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/#materialized-views") in the OpenSearch documentation.

## Covering indexes

A covering index ingests data from a specified column in a table, and OpenSearch
creates a new index based on this data. You can use this new index for
visualizations and other OpenSearch features, such as anomaly detection or
geospatial analysis.

Covering indexes are supported only for Amazon S3 data sources.

For more information about setting up covering indexes, see [Covering indexes](https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/#covering-indexes "https://opensearch.org/docs/latest/dashboards/management/accelerate-external-data/#covering-indexes") in the OpenSearch documentation.
