# Using Sensitive Data Detection outside AWS Glue Studio

AWS Glue Studio allows you to detect sensitive data, however,
you can also use the Sensitive Data Detection functionality outside of AWS Glue Studio.

For a full list of managed sensitive data types, see
[Managed data types](sensitive-data-managed-data-types.md "sensitive-data-managed-data-types.md").

## Detecting Sensitive Data Detection using AWS Managed PII types

AWS Glue provides two APIs in a AWS Glue ETL job.
These are `detect()` and `classifyColumns()`:

```

  detect(frame: DynamicFrame,
      entityTypesToDetect: Seq[String],
      outputColumnName: String = "DetectedEntities",
      detectionSensitivity: String = "LOW"): DynamicFrame

 detect(frame: DynamicFrame,
      detectionParameters: JsonOptions,
      outputColumnName: String = "DetectedEntities",
      detectionSensitivity: String = "LOW"): DynamicFrame

  classifyColumns(frame: DynamicFrame,
      entityTypesToDetect: Seq[String],
      sampleFraction: Double = 0.1,
      thresholdFraction: Double = 0.1,
      detectionSensitivity: String = "LOW")

```

You can use the `detect()` API to identify AWS Managed PII types and custom entity types. A new column is automatically created
with the detection result. The `classifyColumns()` API returns
a map where keys are column names and values are list of detected entity types.
`SampleFraction` indicates the fraction of the data to sample when
scanning for PII entities whereas `ThresholdFraction` indicates
the fraction of the data that must be met in order for a column to be identified as
PII data.

### Row-level detection

In the example, the job is performing the following actions using the `detect()`
and `classifyColumns()` APIs:

- reading data from an Amazon S3 bucket and turns it into a dynamicFrame
- detecting instances of "Email" and "Credit Card" in the dynamicFrame
- returning a dynamicFrame with original values plus one column which encompasses
  detection result for each row
- writing the returned dynamicFrame in another Amazon S3 path

```

  import com.amazonaws.services.glue.GlueContext
  import com.amazonaws.services.glue.MappingSpec
  import com.amazonaws.services.glue.errors.CallSite
  import com.amazonaws.services.glue.util.GlueArgParser
  import com.amazonaws.services.glue.util.Job
  import com.amazonaws.services.glue.util.JsonOptions
  import org.apache.spark.SparkContext
  import scala.collection.JavaConverters._
  import com.amazonaws.services.glue.ml.EntityDetector

  object GlueApp {
    def main(sysArgs: Array[String]) {
      val spark: SparkContext = new SparkContext()
      val glueContext: GlueContext = new GlueContext(spark)
      val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
      Job.init(args("JOB_NAME"), glueContext, args.asJava)
      val frame= glueContext.getSourceWithFormat(formatOptions=JsonOptions("""{"quoteChar": "\"", "withHeader": true, "separator": ","}"""), connectionType="s3", format="csv", options=JsonOptions("""{"paths": ["s3://pathToSource"], "recurse": true}"""), transformationContext="AmazonS3_node1650160158526").getDynamicFrame()

      val frameWithDetectedPII = EntityDetector.detect(frame, Seq("EMAIL", "CREDIT_CARD"))

      glueContext.getSinkWithFormat(connectionType="s3", options=JsonOptions("""{"path": "s3://pathToOutput/", "partitionKeys": []}"""), transformationContext="someCtx", format="json").writeDynamicFrame(frameWithDetectedPII)

      Job.commit()
    }
  }

```

###

Row-level detection with fine-grained actions

In the example, the job is performing the following actions using the `detect()` APIs:

- reading data from an Amazon S3 bucket and turns it into a dynamicFrame
- detecting sensitive data types for “USA_PTIN”, “ BANK_ACCOUNT”, “USA_SSN”, “USA_PASSPORT_NUMBER” , and “PHONE_NUMBER” in
  the dynamicFrame
- returning a dynamicFrame with modified masked values plus one column which encompasses detection result for each row
- writing the returned dynamicFrame in another Amazon S3 path

In contrast with the above `detect()` API, this uses fine-grained actions for entity types to detect.
For more information, see
[Detection parameters for using detect()](#sensitive-data-detect-parameters-fine-grained-actions "#sensitive-data-detect-parameters-fine-grained-actions").

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.MappingSpec
import com.amazonaws.services.glue.errors.CallSite
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._
import com.amazonaws.services.glue.ml.EntityDetector

object GlueApp {
  def main(sysArgs: Array[String]) {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)
    val frame = glueContext.getSourceWithFormat(formatOptions=JsonOptions("""{"quoteChar": "\"", "withHeader": true, "separator": ","}"""), connectionType="s3", format="csv", options=JsonOptions("""{"paths": ["s3://pathToSource"], "recurse": true}"""), transformationContext="AmazonS3_node_source").getDynamicFrame()

    val detectionParameters = JsonOptions(
      """
        {
          "USA_DRIVING_LICENSE": [{
            "action": "PARTIAL_REDACT",
            "sourceColumns": ["Driving License"],
            "actionOptions": {
              "matchPattern": "[0-9]",
              "redactChar": "*"
            }
          }],
          "BANK_ACCOUNT": [{
            "action": "DETECT",
            "sourceColumns": ["*"]
          }],
          "USA_SSN": [{
            "action": "SHA256_HASH",
            "sourceColumns": ["SSN"]
          }],
          "IP_ADDRESS": [{
            "action": "REDACT",
            "sourceColumns": ["IP Address"],
            "actionOptions": {"redactText": "*****"}
          }],
          "PHONE_NUMBER": [{
            "action": "PARTIAL_REDACT",
            "sourceColumns": ["Phone Number"],
            "actionOptions": {
              "numLeftCharsToExclude": 1,
              "numRightCharsToExclude": 0,
              "redactChar": "*"
            }
          }]
        }
      """
    )

    val frameWithDetectedPII = EntityDetector.detect(frame, detectionParameters, "DetectedEntities", "HIGH")

    glueContext.getSinkWithFormat(connectionType="s3", options=JsonOptions("""{"path": "s3://pathToOutput/", "partitionKeys": []}"""), transformationContext="AmazonS3_node_target", format="json").writeDynamicFrame(frameWithDetectedPII)

    Job.commit()
  }
}


```

###

Column-level detection

In the example, the job is performing the following actions using the `classifyColumns()`APIs:

- reading data from an Amazon S3 bucket and turns it into a dynamicFrame
- detecting instances of "Email" and "Credit Card" in the dynamicFrame
- set parameters to sample 100% of the column, mark an entity as detected if it is in 10% of cells, and have “LOW” sensitivity
- returns a map where keys are column names and values are list of detected entity types
- writing the returned dynamicFrame in another Amazon S3 path

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.MappingSpec
import com.amazonaws.services.glue.errors.CallSite
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._
import com.amazonaws.services.glue.DynamicFrame
import com.amazonaws.services.glue.ml.EntityDetector

object GlueApp {
  def main(sysArgs: Array[String]) {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)
    val frame = glueContext.getSourceWithFormat(formatOptions=JsonOptions("""{"quoteChar": "\"", "withHeader": true, "separator": ",", "optimizePerformance": false}"""), connectionType="s3", format="csv", options=JsonOptions("""{"paths": ["s3://pathToSource"], "recurse": true}"""), transformationContext="frame").getDynamicFrame()

    import glueContext.sparkSession.implicits._

    val detectedDataFrame = EntityDetector.classifyColumns(
        frame,
        entityTypesToDetect = Seq("CREDIT_CARD", "PHONE_NUMBER"),
        sampleFraction = 1.0,
        thresholdFraction = 0.1,
        detectionSensitivity = "LOW"
    )
    val detectedDF = (detectedDataFrame).toSeq.toDF("columnName", "entityTypes")
    val DetectSensitiveData_node = DynamicFrame(detectedDF, glueContext)

    glueContext.getSinkWithFormat(connectionType="s3", options=JsonOptions("""{"path": "s3://pathToOutput", "partitionKeys": []}"""), transformationContext="someCtx", format="json").writeDynamicFrame(DetectSensitiveData_node)

    Job.commit()
  }
}


```

## Detecting Sensitive Data Detection using AWS

CustomEntityType PII types

You can define custom entities through AWS Studio. However,
to use this feature out of AWS Studio, you have to first define
the custom entity types and then add the defined custom entity types to the list
of `entityTypesToDetect`.

If you have specific sensitive data types in your data (such as 'Employee
Id'), you can create custom entities by calling the `CreateCustomEntityType()`
API. The following example defines the custom entity type 'EMPLOYEE_ID' to the
`CreateCustomEntityType()` API with the request parameters:

```

  {
      "name": "EMPLOYEE_ID",
      "regexString": "\d{4}-\d{3}",
      "contextWords": ["employee"]
  }

```

Then, modify the job to use the new custom sensitive data type by adding
the custom entity type (EMPLOYEE_ID) to the `EntityDetector()`
API:

```

  import com.amazonaws.services.glue.GlueContext
  import com.amazonaws.services.glue.MappingSpec
  import com.amazonaws.services.glue.errors.CallSite
  import com.amazonaws.services.glue.util.GlueArgParser
  import com.amazonaws.services.glue.util.Job
  import com.amazonaws.services.glue.util.JsonOptions
  import org.apache.spark.SparkContext
  import scala.collection.JavaConverters._
  import com.amazonaws.services.glue.ml.EntityDetector

  object GlueApp {
    def main(sysArgs: Array[String]) {
      val spark: SparkContext = new SparkContext()
      val glueContext: GlueContext = new GlueContext(spark)
      val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
      Job.init(args("JOB_NAME"), glueContext, args.asJava)
      val frame= glueContext.getSourceWithFormat(formatOptions=JsonOptions("""{"quoteChar": "\"", "withHeader": true, "separator": ","}"""), connectionType="s3", format="csv", options=JsonOptions("""{"paths": ["s3://pathToSource"], "recurse": true}"""), transformationContext="AmazonS3_node1650160158526").getDynamicFrame()

      val frameWithDetectedPII = EntityDetector.detect(frame, Seq("EMAIL", "CREDIT_CARD", "EMPLOYEE_ID"))

      glueContext.getSinkWithFormat(connectionType="s3", options=JsonOptions("""{"path": "s3://pathToOutput/", "partitionKeys": []}"""), transformationContext="someCtx", format="json").writeDynamicFrame(frameWithDetectedPII)

      Job.commit()
    }
  }

```

###### Note

If a custom sensitive data type is defined with the same name as an existing
managed entity type, then the custom sensitive data type will take precedent
and overwrite the managed entity type's logic.

##

Detection parameters for using `detect()`

This method is used for detecting entities in a DynamicFrame. It returns a new DataFrame with original values and an additional
column outputColumnName that has PII detection metadata. Custom masking can be done after this DynamicFrame is returned within
the AWS Glue script, or the detect() with fine-grained actions API can be used instead.

```
detect(frame: DynamicFrame,
       entityTypesToDetect: Seq[String],
       outputColumnName: String = "DetectedEntities",
       detectionSensitivity: String = "LOW"): DynamicFrame

```

Parameters:

- **frame** – (type: `DynamicFrame`) The input DynamicFrame containing the data to be processed.
- **entityTypesToDetect** – (type: `[Seq[String]`) List of entity types to detect.
  Can be either Managed Entity Types or Custom Entity Types.
- **outputColumnName** – (type: `String`, default: "DetectedEntities") The name of the column
  where detected entities will be stored. If not provided, the default column name is "DetectedEntities".
- **detectionSensitivity** – (type: `String`, options: "LOW" or "HIGH", default: "LOW")
  Specifies the sensitivity of the detection process. Valid options are "LOW" or "HIGH". If not provided, the default sensitivity
  is set to "LOW".

`outputColumnName` settings:

The name of the column where detected entities will be stored. If not provided, the default column name is "DetectedEntities".
For each row in the output column, the supplementary column includes a map of the column name to the detected entity metadata with
the following key-value pairs:

- **entityType** – The detected entity type.
- **start** – The starting position of the detected entity in the original data.
- **end** – The ending position of the detected entity in the original data.
- **actionUsed** – The action performed on the detected entity (e.g., "DETECT," "REDACT," "PARTIAL_REDACT,"
  "SHA256_HASH").

Example:

```
{
   "DetectedEntities":{
      "SSN Col":[
         {
            "entityType":"USA_SSN",
            "actionUsed":"DETECT",
            "start":4,
            "end":15
         }
      ],
      "Random Data col":[
         {
            "entityType":"BANK_ACCOUNT",
            "actionUsed":"PARTIAL_REDACT",
            "start":4,
            "end":13
         },
         {
            "entityType":"IP_ADDRESS",
            "actionUsed":"REDACT",
            "start":4,
            "end":13
         }
      ]
   }
}

```

**Detection Parameters for `detect()` with fine grained actions**

This method is used for detecting entities in a DynamicFrame using specified parameters. It returns a new DataFrame with
original values replaced with masked sensitive data and an additional column `outputColumnName` that has PII detection
metadata.

```
detect(frame: DynamicFrame,
       detectionParameters: JsonOptions,
       outputColumnName: String = "DetectedEntities",
       detectionSensitivity: String = "LOW"): DynamicFrame

```

Parameters:

- **frame** – (type: `DynamicFrame`): The input DynamicFrame containing the data to be processed.
- **detectionParameters** – (type: `JsonOptions`): JSON options specifying parameters for the detection process.
- **outputColumnName** – (type: `String`, default: "DetectedEntities"): The name of the column where
  detected entities will be stored. If not provided, the default column name is "DetectedEntities".
- **detectionSensitivity** – (type: `String`, options: "LOW" or "HIGH", default: "LOW"): Specifies the
  sensitivity of the detection process. Valid options are "LOW" or "HIGH". If not provided, the default sensitivity is set to "LOW".

`detectionParameters` settings

If no settings are included, default values will be used.

- **action** – (type: `String`, options: "DETECT", "REDACT", "PARTIAL_REDACT", "SHA256_HASH")
  Specifies the action to be performed on the entity. Required. Note that actions that perform masking (all but "DETECT") can only
  perform one action per column. This is a preventative measure for masking coalesced entities.
- **sourceColumns** – (type: `List[String]`, default: [“\*”]) List of source column names to
  perform detection on for the entity. Defaults to [“\*”] if not present. Raises
  `IllegalArgumentException` if an invalid column name is used.
- **sourceColumnsToExclude** – (type: `List[String]`) List of source column names to to perform
  detection on for the entity. Use either `sourceColumns` or `sourceColumnsToExclude`. Raises
  `IllegalArgumentException` if an invalid column name is used.
- **actionOptions** – Additional options based on the specified action:
  - For "DETECT" and "SHA256_HASH", no options are allowed.
  - For "REDACT":
    - **redactText** – (type: `String`, default: "\*\*\*\*\*") Text to replace the detected
      entity.

  - For "PARTIAL_REDACT":
    - **redactChar** – (type: `String`, default: "\*") Character to replace each
      detected character in the entity.
    - **matchPattern** – (type: `String`) Regex pattern for partial redaction. Cannot
      be combined with numLeftCharsToExclude or `numRightCharsToExclude`.
    - **numLeftCharsToExclude** – (type: `String, integer`) Number of left characters to
      exclude. Cannot be combined with matchPattern, but can be used with `numRightCharsToExclude`.
    - **numRightCharsToExclude** – (type: `String, integer`) Number of right characters to
      exclude. Cannot be combined with matchPattern, but can be used with `numRightCharsToExclude`.

`outputColumnName` settings

See outputColumnName settings

## Detection Parameters for `classifyColumns()`

This method is used for detecting entities in a DynamicFrame. It returns a map where keys are column names and values are list
of detected entity types. Custom masking can be done after this is returned within the AWS Glue script.

```
classifyColumns(frame: DynamicFrame,
                entityTypesToDetect: Seq[String],
                sampleFraction: Double = 0.1,
                thresholdFraction: Double = 0.1,
                detectionSensitivity: String = "LOW")

```

Parameters:

- **frame** – (type: `DynamicFrame`) The input DynamicFrame containing the data to be processed.
- **entityTypesToDetect** – (type: `Seq[String]`) List of entity types to detect. Can be either
  Managed Entity Types or Custom Entity Types.
- **sampleFraction** – (type: `Double`, default: 10%) The fraction of the data to sample when
  scanning for PII entities.
- **thresholdFraction** – (type: `Double`, default: 10%): The fraction of the data that must be
  met in order for a column to be identified as PII data.
- **detectionSensitivity** – (type: `String`, options: "LOW" or "HIGH", default: "LOW")
  Specifies the sensitivity of the detection process. Valid options are "LOW" or "HIGH". If not provided, the default sensitivity
  is set to "LOW".
