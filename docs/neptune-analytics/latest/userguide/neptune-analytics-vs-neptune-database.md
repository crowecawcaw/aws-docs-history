# When to use Neptune Analytics and when to use Neptune Database

Amazon Neptune makes it easy to work with graph data in the AWS Cloud.
Amazon Neptune includes both Neptune Database and Neptune Analytics.

[Neptune Database](../../../neptune/latest/userguide/intro.md "../../../neptune/latest/userguide/intro.md")
is a serverless graph database designed for optimal scalability and
availability. It provides a solution for graph database workloads that need to scale to
100,000 queries per second, Multi-AZ high availability, and multi-Region deployments.
You can use Neptune Database for social networking, fraud alerting, and
Customer 360 applications.

Neptune Analytics is an analytics database engine that can quickly analyze large amounts of
graph data in memory to get insights and find trends. Neptune Analytics is a solution for quickly
analyzing existing graph databases or graph datasets stored in a data lake. It uses
popular graph analytic algorithms and low-latency analytic queries.

You can use Neptune Analytics to analyze and query graphs in data science workflows that
build targeted content recommendations, assist with fraud investigations, and detect
network threats.

By providing a simple API for loading, querying, and analyzing graph data, Neptune Analytics
also removes the overhead of building and managing complex data-analytics pipelines.

Neptune Analytics makes it easy to apply powerful algorithms both to the data in your
Neptune Database and to graph data that's stored externally. Because Neptune Analytics can load
a large dataset very quickly into memory, it becomes possible to analyze graphs with
tens of billions of relationships and to process thousands of analytic queries per second
using popular graph analytics algorithms.
