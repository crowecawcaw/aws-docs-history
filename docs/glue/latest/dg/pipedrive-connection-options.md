

# Pipedrive connection option reference

The following are connection options for Pipedrive:
+  `ENTITY_NAME`(String) - (Required) Used for Read/Write. The name of your Object in Pipedrive. 
+  `API_VERSION`(String) - (Required) Used for Read. The Pipedrive REST API version to use. Allowed values: 
  + `v1` - Uses Pipedrive API v1 for all entities.
  + `v2` - Uses Pipedrive API v2 for entities that have a v2 endpoint (Activities, Deals, Organizations, Persons, Pipelines, Products, and Stages) and falls back to v1 for entities that do not.
+  `INSTANCE_URL`(String) - (Required) URL of the instance where the user wants to run the operations. Example: https://example.pipedrive.com. 
+  `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object. Field selection applies to v1 entities only; entities served over Pipedrive API v2 always return the full set of fields. 
+  `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format. 
+  `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query. 
+  `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query. 
+  `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field. 
+  `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field. 
+  `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read. 