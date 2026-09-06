

# The DynamicFrame object
<a name="glue-etl-scala-apis-glue-dynamicframe-object"></a>

**Package: com.amazonaws.services.glue**

```
object DynamicFrame
```

## Def apply
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-apply"></a>

```
def apply( df : DataFrame,
           glueContext : GlueContext
         ) : DynamicFrame
```



## Def emptyDynamicFrame
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-emptyDynamicFrame"></a>

```
def emptyDynamicFrame( glueContext : GlueContext ) : DynamicFrame 
```



## Def fromPythonRDD
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-fromPythonRDD"></a>

```
def fromPythonRDD( rdd : JavaRDD[Array[Byte]],
                   glueContext : GlueContext
                 ) : DynamicFrame
```



## Def ignoreErrors
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-ignoreErrors"></a>

```
def ignoreErrors( fn : DynamicRecord => DynamicRecord ) : DynamicRecord 
```



## Def inlineErrors
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-inlineErrors"></a>

```
def inlineErrors( msg : String,
                  callSite : CallSite
                ) : (DynamicRecord => DynamicRecord)
```



## Def newFrameWithErrors
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-newFrameWithErrors"></a>

```
def newFrameWithErrors( prevFrame : DynamicFrame,
                        rdd : RDD[DynamicRecord],
                        name : String = "",
                        transformationContext : String = "",
                        callSite : CallSite,
                        stageThreshold : Long,
                        totalThreshold : Long
                      ) : DynamicFrame
```

