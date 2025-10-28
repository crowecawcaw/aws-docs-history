# Connect to a MongoDB data source

The MongoDB Data source enables you to visualize data from MongoDB in Amazon Managed Grafana.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Usage

### Query editor

The query editor supports the same syntax as the MongoDB Shell, with some
limitations: \* You can only run one command/query. \* Only read commands are
supported: **find** and **aggregate** \* _Most_ Object constructors
are not supported (with the exception of **ISODate**, which is supported)

The editor expands upon the MongoDB Shell syntax in the following ways:

- **Database selection** – You can
  supply the name of the database in place of the normal
  "db":

###### Note

You can still use "db". It will refer to the
default database in your connection string.

```

sample_mflix.movies.find()

```

- **Aggregate sorting** – Normally
  sorting happens with a step within the aggregate pipeline, however
  the MongoDB Atlas free tier doesn’t allow sorting. We have expanded
  the syntax to allow it for those using the free tier.

###### Note

MongoDB doesn’t perform the sort with this syntax. The sort
happens after the results are queried from the
collection.

```

sample_mflix.movies.aggregate({}).sort({"time": 1})

```

- With a blank editor, **Ctrl +
  Space** will show a selection of all the available
  databases.
- Entering a dot after the database will show a selection of all
  the available collections for that database.
- Entering a dot after the collection will show the available query
  methods.
- Entering a dot after the query method will show additional
  functions: sort/limit.

#### Running the query

Press **Cmd + S** to run the query

### Time series

When visualizing time series data, the plugin needs to know which field
to use as the time. Simply project the field with a name alias of
"time". The field data type must be a date.

You can coerce non-date data types to date. Doing so will allow using
non-date fields as the time series time. The following example shows how to
convert the int field "year" to a date that is projected as
"time" using the MongoDB $dateFromParts pipeline operator.

```

sample_mflix.movies.aggregate([
{"$match": { "year": {"$gt" : 2000} }},
{"$group": { "_id": "$year", "count": { "$sum": 1 }}},
{"$project": { "_id": 0, "count": 1, "time": { "$dateFromParts": {"year": "$_id", "month": 2}}}}
]
).sort({"time": 1})

```

### Diagnostics

[Diagnostic Commands](https://docs.mongodb.com/manual/reference/command/nav-diagnostic/ "https://docs.mongodb.com/manual/reference/command/nav-diagnostic/")

The following diagnostic commands are currently supported:
"stats", "serverStatus",
"replSetGetStatus", "getLog",
"connPoolStats", "connectionStatus",
"buildInfo", "dbStats",
"hostInfo", "lockInfo"

Examples:

```

admin.connectionStatus()  // run the connectionStatus command
admin.connectionStatus({"authInfo.authenticatedUserRoles": 1})  // run and only return the "authInfo.authenticatedUserRoles" field
admin.connPoolStats({arg: "pool"})  // run the connPoolStats command and pass 1 argument
admin.serverStatus({args: {repl: 0, metrics:0}})  // run the serverStatus command and pass multiple args

```

### Macros

You can reference the dashboard time range in your queries.

- `$__timeFrom` — a macro that references the
  dashboard start time
- `$__timeTo` — a macro that references the
  dashboard end time

````

          $__timeTo -  ``` sample_mflix.movies.find({released: {$gt:
          "$__timeFrom"}}).sort({year: 1})

````

#### Template variables

MongoDB supports the idea of "Compound Variables", which
enable you to use one variable as multiple variables to perform complex
multi-key filters.

To create a Compound Variable, use the naming convention of breaking
the variables up by using underscores (must start with underscore):
`_var1_var2` When querying, the response must be in the
format: `val1-val2`

###### Example: I want to filter results on both movie name and

year.

1. Create a variable of type Query:
   `_movie_year`
2. Set the variable query to a query that will return an array of
   items with one movie-year property, as shown in the following
   example.

```
// Example sample_mflix.movies.aggregate([
          {"$match": {year: {"$gt": 2011}}},
          {"$project": {_id: 0, movie_year: {"$concat":
          ["$title", " - ", {"$toString":"$year"}]}}}
          ])
```

```
 // [{"movie-year": "Ted - 2016"},
          {"movie-year": "The Terminator -
          1985"}]
```

3. Now in your query, you can reference "Movie" and
   "Year" as separate template variables using the syntax
   "$\_variable".

##### Using ad-hoc filters

In addition to the standard "ad-hoc filter" type
variable of any name, a second helper variable must be created. It
should be a "constant" type with the name
`mongodb\_adhoc\_query` and a value compatible with the query editor.
The query result will be used to populate the selectable filters.
You can choose to hide this variable from view as it serves no
further purpose.

```

          sample_mflix.movies.aggregate([
          {"$group": { "_id": "$year"}},
          {"$project": { "year": "$_id","_id":
          0 }} ] )
```
