

# Limitations and notes for the Weaviate connector
<a name="weaviate-connector-limitations"></a>

The following are limitations and notes for the Weaviate connector:
+ Weaviate is supported as a source only. Writing to Weaviate is not supported.
+ The connector supports Weaviate Cloud clusters only. It connects to `https://{{SUBDOMAIN}}.weaviate.cloud/v1`. Self-hosted Weaviate deployments are not supported.
+ The `objects` entity returns the same columns for every collection. The collection-specific properties are in the `properties` column as a JSON string. To interpret them, read the property definitions in the `classes` entity.
+ Job bookmarks are not supported.