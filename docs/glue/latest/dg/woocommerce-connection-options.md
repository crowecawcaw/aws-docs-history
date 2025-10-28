# WooCommerce connection options

The following are connection options for WooCommerce:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in WooCommerce.
- `API_VERSION`(String) - (Required) Used for Read. WooCommerce Rest API version you want to use.
- `REALM_ID`(String) - An ID that identifies an individual WooCommerce Online company where you send requests.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `INSTANCE_URL`(String) - (Required) A valid WooCommerce instance URL with the format: https://<instance>.wpcomstaging.com
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
