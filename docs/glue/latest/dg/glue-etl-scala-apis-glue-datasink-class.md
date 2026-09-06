

# Abstract DataSink class
<a name="glue-etl-scala-apis-glue-datasink-class"></a>

**Topics**
+ [Def writeDynamicFrame](#glue-etl-scala-apis-glue-datasink-class-defs-writeDynamicFrame)
+ [Def pyWriteDynamicFrame](#glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDynamicFrame)
+ [Def writeDataFrame](#glue-etl-scala-apis-glue-datasink-class-defs-writeDataFrame)
+ [Def pyWriteDataFrame](#glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDataFrame)
+ [Def setCatalogInfo](#glue-etl-scala-apis-glue-datasink-class-defs-setCatalogInfo)
+ [Def supportsFormat](#glue-etl-scala-apis-glue-datasink-class-defs-supportsFormat)
+ [Def setFormat](#glue-etl-scala-apis-glue-datasink-class-defs-setFormat)
+ [Def withFormat](#glue-etl-scala-apis-glue-datasink-class-defs-withFormat)
+ [Def setAccumulableSize](#glue-etl-scala-apis-glue-datasink-class-defs-setAccumulableSize)
+ [Def getOutputErrorRecordsAccumulable](#glue-etl-scala-apis-glue-datasink-class-defs-getOutputErrorRecordsAccumulable)
+ [Def errorsAsDynamicFrame](#glue-etl-scala-apis-glue-datasink-class-defs-errorsAsDynamicFrame)
+ [DataSink object](#glue-etl-scala-apis-glue-datasink-object)

**Package: com.amazonaws.services.glue**

```
abstract class DataSink
```

The writer analog to a `DataSource`. `DataSink` encapsulates a destination and a format that a `DynamicFrame` can be written to.

## Def writeDynamicFrame
<a name="glue-etl-scala-apis-glue-datasink-class-defs-writeDynamicFrame"></a>

```
def writeDynamicFrame( frame : DynamicFrame,
                       callSite : CallSite = CallSite("Not provided", "")
                     ) : DynamicFrame
```



## Def pyWriteDynamicFrame
<a name="glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDynamicFrame"></a>

```
def pyWriteDynamicFrame( frame : DynamicFrame,
                         site : String = "Not provided",
                         info : String = "" )
```



## Def writeDataFrame
<a name="glue-etl-scala-apis-glue-datasink-class-defs-writeDataFrame"></a>

```
def writeDataFrame(frame: DataFrame,
                   glueContext: GlueContext,
                   callSite: CallSite = CallSite("Not provided", "")
                   ): DataFrame
```



## Def pyWriteDataFrame
<a name="glue-etl-scala-apis-glue-datasink-class-defs-pyWriteDataFrame"></a>

```
def pyWriteDataFrame(frame: DataFrame,
                     glueContext: GlueContext,
                     site: String = "Not provided",
                     info: String = ""
                     ): DataFrame
```



## Def setCatalogInfo
<a name="glue-etl-scala-apis-glue-datasink-class-defs-setCatalogInfo"></a>

```
def setCatalogInfo(catalogDatabase: String, 
                   catalogTableName : String, 
                   catalogId : String = "")
```



## Def supportsFormat
<a name="glue-etl-scala-apis-glue-datasink-class-defs-supportsFormat"></a>

```
def supportsFormat( format : String ) : Boolean
```



## Def setFormat
<a name="glue-etl-scala-apis-glue-datasink-class-defs-setFormat"></a>

```
def setFormat( format : String,
               options : JsonOptions
             ) : Unit
```



## Def withFormat
<a name="glue-etl-scala-apis-glue-datasink-class-defs-withFormat"></a>

```
def withFormat( format : String,
                options : JsonOptions = JsonOptions.empty
              ) : DataSink
```



## Def setAccumulableSize
<a name="glue-etl-scala-apis-glue-datasink-class-defs-setAccumulableSize"></a>

```
def setAccumulableSize( size : Int ) : Unit
```



## Def getOutputErrorRecordsAccumulable
<a name="glue-etl-scala-apis-glue-datasink-class-defs-getOutputErrorRecordsAccumulable"></a>

```
def getOutputErrorRecordsAccumulable : Accumulable[List[OutputError], OutputError]
```



## Def errorsAsDynamicFrame
<a name="glue-etl-scala-apis-glue-datasink-class-defs-errorsAsDynamicFrame"></a>

```
def errorsAsDynamicFrame : DynamicFrame
```



## DataSink object
<a name="glue-etl-scala-apis-glue-datasink-object"></a>

```
object DataSink
```

### Def recordMetrics
<a name="glue-etl-scala-apis-glue-datasink-object-defs-recordMetrics"></a>

```
def recordMetrics( frame : DynamicFrame,
                   ctxt : String
                 ) : DynamicFrame
```

