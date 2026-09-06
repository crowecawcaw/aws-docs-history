

# Using CSV data
<a name="using-CSV-data"></a>

 Neptune Analytics, like [Neptune Database](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html), supports two csv formats for loading graph data: [csv](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html) and [opencypher](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html). Both are csv-based formats with a specified schema. A csv file must contain a header row and the column values. The remainder of the files are interpreted based on the corresponding header column. The header could contain predefined system column names and user-defined column names, annotated with predefined datatypes and cardinality. 

## Behavioral differences from Neptune csv (opencypher) format
<a name="using-CSV-data-differences"></a>

**Edge files**:
+  The `~id` (`:ID`) column in `edge` (`relationship`) files in `CSV` (`opencypher`) format is not supported. It is ignored if provided in any of the `edge` (`relationship`) files. 
+  If the `~label` (`:TYPE`) column is missing from an edge file, or if the `~label` value for a row is empty, the edge is assigned the default label `"edge"`. Unlike vertices, edges always have a label in Neptune Analytics. 

**Vertex files**:
+  Only explicitly provided labels are associated with the vertices. If the label provided is empty, the vertex is added without a label. If a row contains just the vertex id without any labels or properties then the row is ignored, and no vertex is added. For more information about vertices, see [vertices](query-openCypher-data-model.md#query-openCypher-data-model-vertices). 

**Edge or vertex files**:
+  Unlike Neptune Database, a vertex identifier can appear just in edge files. Neptune Analytics allows loading just the edge data from files in Amazon S3, and running an algorithm over the data without needing to provide any additional vertex information. The edges are created between vertices with the given identifiers, and the vertices have no labels or properties unless any are provided in the vertex files. For more information on vertices and what they are, see [vertices](query-openCypher-data-model.md#query-openCypher-data-model-vertices). 
+  Unlike Neptune Database, Neptune Analytics doesn't convert the `Date` type into `Datetime` type. 

## Supported column types
<a name="using-CSV-data-supported-types"></a>

### Date and Datetime
<a name="using-CSV-data-date-datetime"></a>

 The `Date` column type is supported. The following date formats are supported: `yyyy-MM-dd`, `yyyy-MM-dd[+|-]hhmm`. To include time along with date, use the `Datetime` column type instead. 

 The datetime values can either be provided in the [XSD format](https://www.w3.org/TR/xmlschema-2/) or one of the following formats: 
+ `yyyy-MM-dd`
+ `yyyy-MM-ddTHH:mm`
+ `yyyy-MM-ddTHH:mm:ss`
+ `yyyy-MM-ddTHH:mm:ssZ`
+ `yyyy-MM-ddTHH:mm:ss.SSSZ`
+ `yyyy-MM-ddTHH:mm:ss[+|-]hhmm`
+ `yyyy-MM-ddTHH:mm:ss.SSS[+|-]hhmm`

### Vector
<a name="using-CSV-data-vector"></a>

 A new column type `Vector` is supported for associating embeddings with vertices. Since Neptune Analytics only supports one index type at this moment, the property name for embeddings is currently fixed to `embedding`. If the element type of the embeddings is not floating point (FP32), it is cast to FP32. The embeddings in the `csv` files are optional when the vector index is enabled. This means that not every node needs to be associated with an embedding. If you want to set up a vector index for the graph, choose the `vector dimension` and then specify the number of dimensions for the vectors in the index. The changes to vector embeddings are non-atomic and unisolated (see [Vector index transaction support](vector-index.md#vector-index-transaction-support)), that is they become durable and visible to other queries immediately upon write, unlike other properties. 

**Important**  
 The `dimension` must match the dimension of the embeddings in the vertex files. 

 For more details of loading embeddings, refer to [vector-index](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vector-index.html). 

### Any type
<a name="using-CSV-data-any-type"></a>

 A column type `Any` is supported in the user columns. An `Any` type is a type "syntactic sugar" for all of the other types we support. It is extremely useful if a user column has multiple types in it. The payload of an `Any` type value is a list of json strings as follows: `"{""value"": ""10"", ""type"": ""Int""};{""value"": ""1.0"", ""type"": ""Float""}"` , which has a `value` field and a `type` field in each individual json string. The column header of an `Any` type is `propertyname:Any`. The cardinality value of an `Any` column is `set`, meaning that the column can accept multiple values. 

 Neptune Analytics supports the following types in an `Any` type: `Bool` (or `Boolean`), `Byte`, `Short`, `Int`, `Long`, `UnsignedByte`, `UnsignedShort`, `UnsignedInt`, `UnsignedLong`, `Float`, `Double`, `Date`, `dateTime`, and `String`. 

**Any type limitations**
+  `Vector` type is not supported in `Any` type. 
+  Nested `Any` type is not supported. For example, `"{""value"": "{""value"": ""10"", ""type"": ""Int""}", ""type"": ""Any""}"`. 

## Limitations and unsupported features
<a name="using-CSV-data-limitations"></a>
+  Multi-line string values are not supported. Import behavior is undefined if the dataset contains multi-line string values. 
+  Quoted string values must not have a leading space between the delimiter and quotes. For example, if a line is `abc, "def"` then that is interpreted as a line with two fields, with string values of `abc` and `"def"`. `"def"` is a non-quoted string field and quotes are stored as-is in the value, with a size of 6 characters. If the line is `abc,"def"` then it is interpreted as a line with two fields with string values `abc` and `def`. 
+  `Gzip` files are not supported. 
+  Float and double values in scientific notation are currently not supported. However, `Infinity`, `INF`, `-Infinity`, `-INF`, and `NaN` (`Not-a-number`) values are supported. 
+  The maximum length of the strings supported is limited to 1,048,062 bytes. The limit is lower for strings with unicode characters since some unicode characters are represented using multiple bytes. 
+  The `allowEmptyStrings` parameter is not supported. Empty string values ("") are not treated as null or missing value, and are stored as a property value. 