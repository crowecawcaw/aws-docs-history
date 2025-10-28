# Zendesk connection options

The following are connection options for Zendesk:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your Object in Zendesk.
- `API_VERSION`(String) - (Required) Used for Read. Zendesk Rest API version you want to use. For example: v2.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object. For example: id, name, url, created_at
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format. For example: group_id = 100
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query. For example: "SELECT id,url FROM users WHERE role=\"end-user\""
- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query. Default field is `update_at` for entities supporting the incremental export API (`created_at` for `ticket-events` and `time` for `ticket-metric-events`).
- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.
- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field. Optional; this option will be handled by the connector if not provided in the job option. Default value - "2024-05-01T20:55:02.000Z
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read. Optional; this option will be handled by the connector if not provided in the job option. Default value : 1.
- `IMPORT_DELETED_RECORDS`(String) - Default: FALSE. Used for read. To get the delete records while querying.
- `ACCESS_TOKEN` - Access token to be used in the request.
- `INSTANCE_URL` - URL of the instance where the user wants to run the operations. For example : https://{subdomain}/.zendesk.com
