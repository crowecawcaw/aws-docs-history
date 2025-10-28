# AWS Glue Scala DynamicRecord

class

###### Topics

- [Def addField](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-addField "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-addField")
- [Def dropField](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-dropField "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-dropField")
- [Def setError](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-setError "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-setError")
- [Def isError](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-isError "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-isError")
- [Def getError](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getError "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getError")
- [Def clearError](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-clearError "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-clearError")
- [Def write](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-write "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-write")
- [Def readFields](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-readFields "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-readFields")
- [Def clone](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-clone "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-clone")
- [Def schema](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-schema "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-schema")
- [Def getRoot](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getRoot "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getRoot")
- [Def toJson](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-toJson "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-toJson")
- [Def getFieldNode](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getFieldNode "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getFieldNode")
- [Def getField](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getField "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-getField")
- [Def hashCode](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-hashCode "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-hashCode")
- [Def equals](#glue-etl-scala-apis-glue-dynamicrecord-class-defs-equals "#glue-etl-scala-apis-glue-dynamicrecord-class-defs-equals")
- [DynamicRecord object](#glue-etl-scala-apis-glue-dynamicrecord-object "#glue-etl-scala-apis-glue-dynamicrecord-object")
- [RecordTraverser trait](#glue-etl-scala-apis-glue-recordtraverser-trait "#glue-etl-scala-apis-glue-recordtraverser-trait")
  **Package: com.amazonaws.services.glue**

```
class DynamicRecord extends Serializable with Writable with Cloneable
```

A `DynamicRecord` is a self-describing data structure that represents a row of
data in the dataset that is being processed. It is self-describing in the sense that you can get
the schema of the row that is represented by the `DynamicRecord` by inspecting the
record itself. A `DynamicRecord` is similar to a `Row` in Apache
Spark.

## Def addField

```
def addField( path : String,
              dynamicNode : DynamicNode
            ) : Unit
```

Adds a [DynamicNode](glue-etl-scala-apis-glue-types-dynamicnode.md "glue-etl-scala-apis-glue-types-dynamicnode.md") to the specified path.

- `path` — The path for the field to be added.
- `dynamicNode` — The [DynamicNode](glue-etl-scala-apis-glue-types-dynamicnode.md "glue-etl-scala-apis-glue-types-dynamicnode.md") to be added at the
  specified path.

## Def dropField

```
 def dropField(path: String, underRename: Boolean = false): Option[DynamicNode]
```

Drops a [DynamicNode](glue-etl-scala-apis-glue-types-dynamicnode.md "glue-etl-scala-apis-glue-types-dynamicnode.md") from the specified path and returns the dropped node if there is not an array in the specified path.

- `path` — The path to the field to drop.
- `underRename` — True if `dropField` is called as part of
  a rename transform, or false otherwise (false by default).

Returns a `scala.Option Option` ([DynamicNode](glue-etl-scala-apis-glue-types-dynamicnode.md "glue-etl-scala-apis-glue-types-dynamicnode.md")).

## Def setError

```
def setError( error : Error )
```

Sets this record as an error record, as specified by the `error` parameter.

Returns a `DynamicRecord`.

## Def isError

```
def isError
```

Checks whether this record is an error record.

## Def getError

```
def getError
```

Gets the `Error` if the record is an error record. Returns `scala.Some Some` (Error) if
this record is an error record, or otherwise `scala.None` .

## Def clearError

```
def clearError
```

Set the `Error` to `scala.None.None` .

## Def write

```
override def write( out : DataOutput ) : Unit
```

## Def readFields

```
override def readFields( in : DataInput ) : Unit
```

## Def clone

```
override def clone : DynamicRecord
```

Clones this record to a new `DynamicRecord` and returns it.

## Def schema

```
def schema
```

Gets the `Schema` by inspecting the record.

## Def getRoot

```
def getRoot : ObjectNode
```

Gets the root `ObjectNode` for the record.

## Def toJson

```
def toJson : String
```

Gets the JSON string for the record.

## Def getFieldNode

```
def getFieldNode( path : String ) : Option[DynamicNode]
```

Gets the field's value at the specified `path` as an option of
`DynamicNode`.

Returns `scala.Some Some` ([DynamicNode](glue-etl-scala-apis-glue-types-dynamicnode.md "glue-etl-scala-apis-glue-types-dynamicnode.md")) if the field exists, or otherwise `scala.None.None` .

## Def getField

```
def getField( path : String ) : Option[Any]
```

Gets the field's value at the specified `path` as an option of
`DynamicNode`.

Returns `scala.Some Some` (value).

## Def hashCode

```
override def hashCode : Int
```

## Def equals

```
override def equals( other : Any )
```

## DynamicRecord object

```
object DynamicRecord
```

### Def apply

```
def apply( row : Row,
           schema : SparkStructType )
```

Apply method to convert an Apache Spark SQL `Row` to a [DynamicRecord](glue-etl-scala-apis-glue-dynamicrecord-class.md "glue-etl-scala-apis-glue-dynamicrecord-class.md").

- `row` — A Spark SQL `Row`.
- `schema` — The `Schema` of that row.

Returns a `DynamicRecord`.

## RecordTraverser trait

```
trait RecordTraverser {
  def nullValue(): Unit
  def byteValue(value: Byte): Unit
  def binaryValue(value: Array[Byte]): Unit
  def booleanValue(value: Boolean): Unit
  def shortValue(value: Short) : Unit
  def intValue(value: Int) : Unit
  def longValue(value: Long) : Unit
  def floatValue(value: Float): Unit
  def doubleValue(value: Double): Unit
  def decimalValue(value: BigDecimal): Unit
  def stringValue(value: String): Unit
  def dateValue(value: Date): Unit
  def timestampValue(value: Timestamp): Unit
  def objectStart(length: Int): Unit
  def objectKey(key: String): Unit
  def objectEnd(): Unit
  def mapStart(length: Int): Unit
  def mapKey(key: String): Unit
  def mapEnd(): Unit
  def arrayStart(length: Int): Unit
  def arrayEnd(): Unit
}
```
