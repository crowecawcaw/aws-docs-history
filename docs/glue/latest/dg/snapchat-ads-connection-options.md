# Snapchat Ads connection options

The following are connection options for Snapchat Ads:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of Snapchat Ads entity. Example: `campaign` .
- `API_VERSION`(String) - (Required) Used for Read. Snapchat Ads Rest API version you want to use.
  The value will be v1, as Snapchat Ads currently supports only version v1.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Comma separated list of columns
  you want to select for the selected entity.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
