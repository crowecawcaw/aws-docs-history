

# AWS Glue Scala GlueArgParser APIs
<a name="glue-etl-scala-apis-glue-util-glueargparser"></a>

**Package: com.amazonaws.services.glue.util**

## GlueArgParser object
<a name="glue-etl-scala-apis-glue-util-glueargparser-object"></a>

**GlueArgParser**

```
object GlueArgParser
```

This is strictly consistent with the Python version of `utils.getResolvedOptions` in the `AWSGlueDataplanePython` package.

### GlueArgParser def methods
<a name="glue-etl-scala-apis-glue-util-glueargparser-object-defs"></a>

```
def getResolvedOptions( args : Array[String],
                        options : Array[String]
                      ) : Map[String, String]
```

```
def initParser( userOptionsSet : mutable.Set[String] ) : ArgumentParser 
```

**Example Retrieving arguments passed to a job**  
To retrieve job arguments, you can use the `getResolvedOptions` method. Consider the following example, which retrieves a job argument named `aws_region`.  

```
val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME","aws_region").toArray)
Job.init(args("JOB_NAME"), glueContext, args.asJava)
val region = args("aws_region")
println(region)
```