

# Data format for loading from Amazon S3 into Neptune Analytics
<a name="loading-data-formats"></a>

 Neptune Analytics, just like [Neptune Database](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html), supports four formats for loading data: 
+  [RDF (ntriples)](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-rdf.html), which is a line-based format for triples. See [Using RDF data](using-rdf-data.md) for more information on how this data is handled. 
+  [csv](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html) and [opencypher](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html), which are csv-based formats with schema restrictions. A csv file must contain a header row and the column values. The remainder of the files are interpreted based on the corresponding header column. The header could contain predefined system column names and user-defined column names annotated with predefined datatypes and cardinality. 
+  [Parquet](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-Parquet-data.html), which is an open source, column-oriented data file format designed for efficient data storage and retrieval. It provides high performance compression and encoding schemes to handle complex data in bulk. The data for each column in a Parquet file is stored together. 

 It's possible to combine CSV, RDF and Parquet data in the same graph, for example by first loading CSV data and enriching it with RDF data. 