# Nodestream

[Nodestream](https://nodestream-proj.github.io/docs/docs/intro/ "https://nodestream-proj.github.io/docs/docs/intro/") is a framework for dealing with semantically
modeling data as a graph. It is designed to be flexible and extensible, allowing you to define how data is collected and
modeled as a graph. It uses a pipeline-based approach to define how data is collected and processed, and it provides a way to
define how the graph should be updated when the schema changes. All of this is done using a simple, human-readable configuration
file in yaml format. To accomplish this, Nodestream uses a number of core concepts, including pipelines, extractors,
transformers, filters, interpreters, interpretations, and migrations.

Beginning with [Nodestream 0.12](https://nodestream-proj.github.io/docs/blog/2024/04/05/nodestream-0-12/ "https://nodestream-proj.github.io/docs/blog/2024/04/05/nodestream-0-12/"),
Amazon Neptune is supported for both [Neptune Database and Neptune Analytics](https://nodestream-proj.github.io/docs/docs/databases/neptune/ "https://nodestream-proj.github.io/docs/docs/databases/neptune/").

Please view the Nodestream documentation for details on how to configure and use Nodestream with Neptune:
[Nodestream support for Amazon Neptune](https://nodestream-proj.github.io/docs/docs/databases/neptune/ "https://nodestream-proj.github.io/docs/docs/databases/neptune/").

Nodestream with Neptune currently supports standard ETL pipelines as well as time to live (TTL) pipelines. ETL pipelines
enable bulk data ingestion into Neptune from a much broader range of data sources and formats than have previously been
possible in Neptune including:

- [Software Bill of Materials](https://nodestream-proj.github.io/docs/docs/official-plugins/sbom/ "https://nodestream-proj.github.io/docs/docs/official-plugins/sbom/")
- [Files including CSV, JSON, JSONL, Parquet, txt and yaml](https://nodestream-proj.github.io/docs/docs/reference/extractors/ "https://nodestream-proj.github.io/docs/docs/reference/extractors/")
- [Kafka](https://nodestream-proj.github.io/docs/docs/reference/extractors/#streamextractor "https://nodestream-proj.github.io/docs/docs/reference/extractors/#streamextractor")
- [Athena](https://nodestream-proj.github.io/docs/docs/reference/extractors/#athenaextractor "https://nodestream-proj.github.io/docs/docs/reference/extractors/#athenaextractor")
- [REST APIs](https://nodestream-proj.github.io/docs/docs/reference/extractors/#simpleapiextractor "https://nodestream-proj.github.io/docs/docs/reference/extractors/#simpleapiextractor")

Nodestream fully supports IAM authentication when connecting to Amazon Neptune, as long as credentials are properly configured.
See the [boto3 credentials guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials") for more information on correctly configuring credentials.

[Nodestream's TTL mechanism](https://nodestream-proj.github.io/docs/docs/tutorials-intermediate/removing-data/ "https://nodestream-proj.github.io/docs/docs/tutorials-intermediate/removing-data/")
also enables new capabilities not previously available in Neptune. By annotating ingested graph elements with timestamps,
Nodestream can create pipelines which automatically expire and remove data that has passed a configured lifespan.
