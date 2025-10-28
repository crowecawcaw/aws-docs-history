# MappingSpec

**Package: com.amazonaws.services.glue**

## MappingSpec case

class

```
case class MappingSpec( sourcePath: SchemaPath,
                        sourceType: DataType,
                        targetPath: SchemaPath,
                        targetType: DataTyp
                       ) extends Product4[String, String, String, String] {
  override def _1: String = sourcePath.toString
  override def _2: String = ExtendedTypeName.fromDataType(sourceType)
  override def _3: String = targetPath.toString
  override def _4: String = ExtendedTypeName.fromDataType(targetType)
}
```

- `sourcePath` — The `SchemaPath` of the source
  field.
- `sourceType` — The `DataType` of the source
  field.
- `targetPath` — The `SchemaPath` of the target
  field.
- `targetType` — The `DataType` of the target
  field.

A `MappingSpec` specifies a mapping from a source path and a source data type
to a target path and a target data type. The value at the source path in the source frame
appears in the target frame at the target path. The source data type is cast to the target
data type.

It extends from `Product4` so that you can handle any `Product4` in
your `applyMapping` interface.

## MappingSpec object

```
object MappingSpec
```

The `MappingSpec` object has the following members:

## Val orderingByTarget

```
val orderingByTarget: Ordering[MappingSpec]
```

## Def apply

```
def apply( sourcePath : String,
           sourceType : DataType,
           targetPath : String,
           targetType : DataType
         ) : MappingSpec
```

Creates a `MappingSpec`.

- `sourcePath` — A string representation of the source path.
- `sourceType` — The source `DataType`.
- `targetPath` — A string representation of the target path.
- `targetType` — The target `DataType`.

Returns a `MappingSpec`.

## Def apply

```
def apply( sourcePath : String,
           sourceTypeString : String,
           targetPath : String,
           targetTypeString : String
         ) : MappingSpec
```

Creates a `MappingSpec`.

- `sourcePath` — A string representation of the source path.
- `sourceType` — A string representation of the source data
  type.
- `targetPath` — A string representation of the target path.
- `targetType` — A string representation of the target data
  type.

Returns a MappingSpec.

## Def apply

```
def apply( product : Product4[String, String, String, String] ) : MappingSpec
```

Creates a `MappingSpec`.

- `product` — The `Product4` of the source path, source
  data type, target path, and target data type.

Returns a `MappingSpec`.
