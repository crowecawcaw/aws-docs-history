# Abstract DataSink class

###### Topics

- [Def writeDynamicFrame](#glue-etl-scala-apis-glue-datasink-class-defs-writeDynamicFrame "#glue-etl-scala-apis-glue-datasink-class-defs-writeDynamicFrame")
- [Def pyWriteDynamicFrame](#glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDynamicFrame "#glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDynamicFrame")
- [Def
  writeDataFrame](#glue-etl-scala-apis-glue-datasink-class-defs-writeDataFrame "#glue-etl-scala-apis-glue-datasink-class-defs-writeDataFrame")
- [Def
  pyWriteDataFrame](#glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDataFrame "#glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDataFrame")
- [Def
  setCatalogInfo](#glue-etl-scala-apis-glue-datasink-class-defs-setCatalogInfo "#glue-etl-scala-apis-glue-datasink-class-defs-setCatalogInfo")
- [Def supportsFormat](#glue-etl-scala-apis-glue-datasink-class-defs-supportsFormat "#glue-etl-scala-apis-glue-datasink-class-defs-supportsFormat")
- [Def setFormat](#glue-etl-scala-apis-glue-datasink-class-defs-setFormat "#glue-etl-scala-apis-glue-datasink-class-defs-setFormat")
- [Def withFormat](#glue-etl-scala-apis-glue-datasink-class-defs-withFormat "#glue-etl-scala-apis-glue-datasink-class-defs-withFormat")
- [Def setAccumulableSize](#glue-etl-scala-apis-glue-datasink-class-defs-setAccumulableSize "#glue-etl-scala-apis-glue-datasink-class-defs-setAccumulableSize")
- [Def getOutputErrorRecordsAccumulable](#glue-etl-scala-apis-glue-datasink-class-defs-getOutputErrorRecordsAccumulable "#glue-etl-scala-apis-glue-datasink-class-defs-getOutputErrorRecordsAccumulable")
- [Def errorsAsDynamicFrame](#glue-etl-scala-apis-glue-datasink-class-defs-errorsAsDynamicFrame "#glue-etl-scala-apis-glue-datasink-class-defs-errorsAsDynamicFrame")
- [DataSink object](#glue-etl-scala-apis-glue-datasink-object "#glue-etl-scala-apis-glue-datasink-object")
  **Package: com.amazonaws.services.glue**

```
abstract class DataSink
```

The writer analog to a `DataSource`. `DataSink` encapsulates a
destination and a format that a `DynamicFrame` can be written to.

## Def writeDynamicFrame

```
def writeDynamicFrame( frame : DynamicFrame,
                       callSite : CallSite = CallSite("Not provided", "")
                     ) : DynamicFrame
```

## Def pyWriteDynamicFrame

```
def pyWriteDynamicFrame( frame : DynamicFrame,
                         site : String = "Not provided",
                         info : String = "" )
```

## Def

writeDataFrame

```
def writeDataFrame(frame: DataFrame,
                   glueContext: GlueContext,
                   callSite: CallSite = CallSite("Not provided", "")
                   ): DataFrame
```

## Def

pyWriteDataFrame

```
def pyWriteDataFrame(frame: DataFrame,
                     glueContext: GlueContext,
                     site: String = "Not provided",
                     info: String = ""
                     ): DataFrame
```

## Def

setCatalogInfo

```
def setCatalogInfo(catalogDatabase: String,
                   catalogTableName : String,
                   catalogId : String = "")
```

## Def supportsFormat

```
def supportsFormat( format : String ) : Boolean
```

## Def setFormat

```
def setFormat( format : String,
               options : JsonOptions
             ) : Unit
```

## Def withFormat

```
def withFormat( format : String,
                options : JsonOptions = JsonOptions.empty
              ) : DataSink
```

## Def setAccumulableSize

```
def setAccumulableSize( size : Int ) : Unit
```

## Def getOutputErrorRecordsAccumulable

```
def getOutputErrorRecordsAccumulable : Accumulable[List[OutputError], OutputError]
```

## Def errorsAsDynamicFrame

```
def errorsAsDynamicFrame : DynamicFrame
```

## DataSink object

```
object DataSink
```

### Def recordMetrics

```
def recordMetrics( frame : DynamicFrame,
                   ctxt : String
                 ) : DynamicFrame
```
