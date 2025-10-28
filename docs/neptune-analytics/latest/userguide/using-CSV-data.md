# Using CSV data

Neptune Analytics, like [Neptune Database](../../../neptune/latest/userguide/bulk-load-tutorial-format.md "../../../neptune/latest/userguide/bulk-load-tutorial-format.md"),
supports two csv formats for loading graph data: [csv](../../../neptune/latest/userguide/bulk-load-tutorial-format-gremlin.md "../../../neptune/latest/userguide/bulk-load-tutorial-format-gremlin.md") and
[opencypher](../../../neptune/latest/userguide/bulk-load-tutorial-format-opencypher.md "../../../neptune/latest/userguide/bulk-load-tutorial-format-opencypher.md").
Both are csv-based formats with a specified schema. A csv file must contain a header row and the column values. The remainder
of the files are interpreted based on the corresponding header column. The header could contain predefined system column names
and user-defined column names, annotated with predefined datatypes and cardinality.

###### Differences with Neptune csv (opencypher) format

**Edge files**:

- The `~id` (`:ID`) column in `edge` (`relationship`) files
  in `CSV` (`opencypher`) format are not supported. They are ignored if provided in any of the
  `edge` (`relationship`) files.

**Vertex files**:

- Only explicitly provided labels are associated with the vertices. If the label provided is empty, the vertex would be
  added without a label. If a row contains just the vertex id without any labels or properties then the row is ignored,
  and no vertex is added. For more information about vertices, see
  [vertices](query-openCypher-data-model.md#query-openCypher-data-model-vertices "query-openCypher-data-model.md#query-openCypher-data-model-vertices").
- A new column type `Vector` is supported for associating embeddings with vertices. Since Neptune Analytics only supports
  one index type at this moment, the property name for embeddings is currently fixed to `Embeddings`. If the
  element type of the embeddings are not floating point (FP32), they will be typecasted to FP32. The embeddings in the
  `csv` files are optional when the vector index is enabled. This means that not every node needs to be
  associated with an embedding. If you want to set up a vector index for the graph, choose use `vector dimension`
  and then specify the number of dimensions for the vectors in the index. Note that the `dimension` must match
  the dimension of the embeddings in the vertex files. For more details of loading embeddings, refer to
  [vector-index](vector-index.md "vector-index.md").

**Edge or vertex files**:

- Unlike Neptune Database, a vertex identifier could appear just in edge files. Neptune Analytics allows loading just the edge data from files in
  Amazon S3, and running an algorithm over the data without needing to provide any additional vertex information. The edges are
  created between vertices with the given identifiers, and the vertices have no labels or properties unless any are provided
  in the vertex files. For more information on vertices and what they are, see
  [vertices](query-openCypher-data-model.md#query-openCypher-data-model-vertices "query-openCypher-data-model.md#query-openCypher-data-model-vertices").
- Date column type is supported. The following date formats are supported: yyyy-MM-dd, yyyy-MM-dd[+|-]hhmm. To include
  time along with date, use the `Datetime` column type instead.
- The datetime values can either be provided in the [XSD format](https://www.w3.org/TR/xmlschema-2/ "https://www.w3.org/TR/xmlschema-2/") or one
  of the following formats:
  - `yyyy-MM-dd`
  - `yyyy-MM-ddTHH:mm`
  - `yyyy-MM-ddTHH:mm:ss`
  - `yyyy-MM-ddTHH:mm:ssZ`
  - `yyyy-MM-ddTHH:mm:ss.SSSZ`
  - `yyyy-MM-ddTHH:mm:ss[+|-]hhmm`
  - `yyyy-MM-ddTHH:mm:ss.SSS[+|-]hhmm`

- Float and double values in scientific notation are currently not supported. Also, `Infinity`, `INF`,
  `-Infinity`, `-INF`, and `NaN` (`Not-a-number`) values are supported.
- `Gzip` files are not supported.
- The maximum length of the strings supported is smaller, and limited to 1,048,062 bytes. The limit would be lower for strings
  with unicode characters since some unicode characters are represented using multiple bytes.
- Multi-line string values are not supported. Imports behavior is undefined if the dataset contains multi-line string values.
- Quoted string values must not have a leading space between the delimiter and quotes. For example, if a line is
  `abc, “def”` then that is interpreted as a line with two fields, with string values of `abc`
  and `“def”`. `“def"` is a non-quoted string field and quotes are stored as-is in the value,
  with a size of 6 characters. If the line is `abc,“def”` then it is interpreted as a line with two fields
  with string values `abc` and `def`.
- A column type `Any` is supported in the user columns. An `Any` type is a type “syntactic sugar” for
  all of the other types we support. It is extremely useful if a user column has multiple types in it. The payload of an
  `Any` type value is a list of json strings as follows: `"{""value"": ""10"", ""type"": ""Int""};{""value"": 
""1.0"", ""type"": ""Float""}"` , which has a `value` field and a `type` field in each
  individual json string. The column header of an `Any` type is `propertyname:Any`. The cardinality
  value of an `Any` column is `set`, meaning that the column can accept multiple values.
  - Neptune Analytics supports the following types in an `Any` type: `Bool` (or `Boolean`),
    `Byte`, `Short`, `Int`, `Long`, `UnsignedByte`,
    `UnsignedShort`, `UnsignedInt`, `UnsignedLong`, `Float`, `Double`,
    `Date`, `dateTime`, and `String`.
  - `Vector` type is not supported in `Any` type.
  - Nested `Any` type is not supported. For example, `"{""value"": "{""value"": ""10"", ""type"": 
""Int""}", ""type"": ""Any""}"`.
