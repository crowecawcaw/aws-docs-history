# Google Search Console connection options

The following are connection options for Google Search Console:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Google Search Console.
- `API_VERSION`(String) - (Required) Used for Read. Google Search Console Rest API version you want to use.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: "start_end_date between <30 days ago from current date> AND <yesterday: that is, 1 day ago from the current date>". Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: "start_end_date between <30 days ago from current date> AND <yesterday: that is, 1 day ago from the current date>" Used for Read. Full Spark SQL query.
- `INSTANCE_URL`(String) - Used for Read. A valid Google Search Console instance URL.
