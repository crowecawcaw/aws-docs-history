# Replication across AWS Regions using global datastores

###### Note

Global Datastore is currently available for node-based clusters only.

By using the Global Datastore feature, you can work with fully managed, fast,
reliable, and secure Valkey or Redis OSS cluster replication across AWS Regions. Using this feature, you can create
cross-Region read replica clusters to enable low-latency reads and disaster
recovery across AWS Regions.

In the following sections, you can find a description of how to work with global
datastores.

###### Topics

- [Overview](#Redis-Global-Data-Stores-Overview "#Redis-Global-Data-Stores-Overview")
- [Prerequisites and limitations](Redis-Global-Datastores-Getting-Started.md "Redis-Global-Datastores-Getting-Started.md")
- [Using global datastores (console)](Redis-Global-Datastores-Console.md "Redis-Global-Datastores-Console.md")
- [Using global datastores (CLI)](Redis-Global-Datastores-CLI.md "Redis-Global-Datastores-CLI.md")

## Overview

Each _global datastore_ is a collection of one or more
clusters that replicate to one another.

A global datastore consists of the following:

- **Primary (active) cluster** – A primary
  cluster accepts writes that are replicated to all clusters within the global
  datastore. A primary cluster also accepts read requests.
- **Secondary (passive) cluster** – A secondary
  cluster only accepts read requests and replicates data updates from a primary
  cluster. A secondary cluster needs to be in a different AWS Region than the primary
  cluster.

When you create a global datastore in ElastiCache for Valkey or Redis OSS, it automatically replicates your data
from the primary cluster to the secondary cluster. You choose the AWS Region where the
Valkey or Redis OSS data should be replicated and then create a secondary cluster in that AWS Region.
ElastiCache then sets up and manages automatic, asynchronous replication of data between
the two clusters.

Using a global datastore for Valkey or Redis OSS provides the following advantages:

- **Geolocal performance** – By setting up
  remote replica clusters in additional AWS Regions and synchronizing your data
  between them, you can reduce latency of data access in that AWS Region. A global
  datastore can help increase the responsiveness of your application by serving
  low-latency, geolocal reads across AWS Regions.
- **Disaster recovery** – If your primary
  cluster in a global datastore experiences degradation, you can promote a secondary
  cluster as your new primary cluster. You can do so by connecting to any AWS Region
  that contains a secondary cluster.

The following diagram shows how global datastores can work.

![global datastore](images/Global-DataStore.png)
