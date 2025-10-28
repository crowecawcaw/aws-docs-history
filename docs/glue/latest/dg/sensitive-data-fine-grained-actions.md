# Using fine-grained sensitive data detection

###### Note

Fine-grained actions is only available in AWS Glue 3.0 and 4.0. This includes the AWS Glue Studio experience.
The persistent audit log changes are also not available in 2.0.

All AWS Glue Studio 3.0 and 4.0 visual jobs will have a script created that automatically uses fine-grained actions APIs.

The Detect Sensitive Data transform provides the ability to detect, mask, or remove entities that you define, or are pre-defined by AWS Glue.
Fine-grained actions further allows you to apply a specific action per entity. Additional benefits include:

- Improved performance as actions are being applied as soon data is detected.
- The option to include or exclude specific columns.
- The ability to use partial masking. This allows you to mask detected sensitive data entities partially, rather than masking
  the entire string. Both simple params with offsets and regex are supported.

The following are code snippets of sensitive data detection APIs and fine-grained actions used in the sample jobs
referenced in the next section.

**Detect API** – fine-grained actions use the new `detectionParameters` parameter:

```
def detect(
    frame: DynamicFrame,
    detectionParameters: JsonOptions,
    outputColumnName: String = "DetectedEntities",
    detectionSensitivity: String = "LOW"
): DynamicFrame = {}

```

## Using Sensitive Data Detection APIs with

fine-grained actions

Sensitive data detection APIs using **detect** analyzes the data given, determines if the rows or
columns are Sensitive Data Entity Types, and will run actions specified by the user for each Entity type.

### Using the detect API with fine-grained actions

Use the **detect** API and specify the `outputColumnName` and `detectionParameters`.

```

    object GlueApp {
      def main(sysArgs: Array[String]) {

        val spark: SparkContext = new SparkContext()
        val glueContext: GlueContext = new GlueContext(spark)

        // @params: [JOB_NAME]
        val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
        Job.init(args("JOB_NAME"), glueContext, args.asJava)

        // Script generated for node S3 bucket. Creates DataFrame from data stored in S3.
        val S3bucket_node1 = glueContext.getSourceWithFormat(formatOptions=JsonOptions("""{"quoteChar": "\"", "withHeader": true, "separator": ",", "optimizePerformance": false}"""), connectionType="s3", format="csv", options=JsonOptions("""{"paths": ["s3://189657479688-ddevansh-pii-test-bucket/tiny_pii.csv"], "recurse": true}"""), transformationContext="S3bucket_node1").getDynamicFrame()

        // Script generated for node Detect Sensitive Data. Will run detect API for the DataFrame
        // detectionParameter contains information on which EntityType are being detected
        // and what actions are being applied to them when detected.
        val DetectSensitiveData_node2 = EntityDetector.detect(
            frame = S3bucket_node1,
            detectionParameters = JsonOptions(
             """
                {
                    "PHONE_NUMBER": [
                        {
                            "action": "PARTIAL_REDACT",
                            "actionOptions": {
                                "numLeftCharsToExclude": "3",
                                "numRightCharsToExclude": "4",
                                "redactChar": "#"
                            },
                            "sourceColumnsToExclude": [ "Passport No", "DL NO#" ]
                        }
                    ],
                    "USA_PASSPORT_NUMBER": [
                        {
                            "action": "SHA256_HASH",
                            "sourceColumns": [ "Passport No" ]
                        }
                    ],
                    "USA_DRIVING_LICENSE": [
                        {
                            "action": "REDACT",
                            "actionOptions": {
                                "redactText": "USA_DL"
                            },
                            "sourceColumns": [ "DL NO#" ]
                        }
                    ]

                }
            """
            ),
            outputColumnName = "DetectedEntities"
        )

        // Script generated for node S3 bucket. Store Results of detect to S3 location
        val S3bucket_node3 = glueContext.getSinkWithFormat(connectionType="s3", options=JsonOptions("""{"path": "s3://amzn-s3-demo-bucket/test-output/", "partitionKeys": []}"""), transformationContext="S3bucket_node3", format="json").writeDynamicFrame(DetectSensitiveData_node2)

        Job.commit()
      }


```

The above script will create a DataFrame from a location in Amazon S3 and then it will run the `detect` API.
Since the `detect` API requires the field `detectionParameters` (a map of the entity name to a list
all of the action settings to be used for that entity) is represented by AWS Glue’s `JsonOptions` object, it will also allow us to extend the functionality of the API.

For each action specified per entity, enter a list of all column names to which to apply the entity/action combination.
This allows you to customize the entities to detect for every column in your dataset and skip entities that you know are not
in a specific column. This also allows your jobs to be more performant by not performing unnecessary detection calls those entities and allows you to
perform actions unique to each column and entity combination.

Taking a closer look at the `detectionParameters`, there are three entity types in the sample job. These are
`Phone Number`, `USA_PASSPORT_NUMBER`, and `USA_DRIVING_LICENSE`. For each of these entity
types AWS Glue will run different actions which are either `PARTIAL_REDACT`, `SHA256_HASH`,
`REDACT`, and `DETECT`. Each of the Entity Types also have `sourceColumns` to apply to
and/or `sourceColumnsToExclude` if detected.

###### Note

Only one edit-in-place action (`PARTIAL_REDACT`, `SHA256_HASH`, or `REDACT`) can be
used per column but the `DETECT` action can be used with any of these actions.

The `detectionParameters` field has the below layout:

```

    ENTITY_NAME -> List[Actions]
    {
    	"ENTITY_NAME": [{
    		Action, // required
    		ColumnSpecs,
    		ActionOptionsMap
        }],
        "ENTITY_NAME2": [{
    		...
        }]
    }

```

The types of `actions` and `actionOptions` are listed below:

```
DETECT
{
    # Required
    "action": "DETECT",
    # Optional, depending on action chosen
    "actionOptions": {
        // There are no actionOptions for DETECT
    },
    # 1 of below required, both can also used
    "sourceColumns": [
        "COL_1", "COL_2", ..., "COL_N"
    ],
    "sourceColumnsToExclude": [
        "COL_5"
    ]
}

SHA256_HASH
{
    # Required
    "action": "SHA256_HASH",
    # Required or optional, depending on action chosen
    "actionOptions": {
        // There are no actionOptions for SHA256_HASH
    },

    # 1 of below required, both can also used
    "sourceColumns": [
        "COL_1", "COL_2", ..., "COL_N"
    ],
    "sourceColumnsToExclude": [
        "COL_5"
    ]
}

REDACT
{
    # Required
    "action": "REDACT",
    # Required or optional, depending on action chosen
    "actionOptions": {
        // The text that is being replaced
        "redactText": "USA_DL"
    },

    # 1 of below required, both can also used
    "sourceColumns": [
        "COL_1", "COL_2", ..., "COL_N"
    ],
    "sourceColumnsToExclude": [
        "COL_5"
    ]
}

PARTIAL_REDACT
{
    # Required
    "action": "PARTIAL_REDACT",
    # Required or optional, depending on action chosen
    "actionOptions": {
        // number of characters to not redact from the left side
        "numLeftCharsToExclude": "3",
        // number of characters to not redact from the right side
        "numRightCharsToExclude": "4",
        // the partial redact will be made with this redacted character
        "redactChar": "#",
        // regex pattern for partial redaction
        "matchPattern": "[0-9]"
    },

    # 1 of below required, both can also used
    "sourceColumns": [
        "COL_1", "COL_2", ..., "COL_N"
    ],
    "sourceColumnsToExclude": [
        "COL_5"
    ]
}

```

Once the script runs, results are output to the given Amazon S3 location. You can view your data in Amazon S3 but with the selected entity types being
sensitized based on the selected action. In the case, we would have a rows that would have that looked like this:

```
{
    "Name": "Colby Schuster",
    "Address": "39041 Antonietta Vista, South Rodgerside, Nebraska 24151",
    "Car Owned": "Fiat",
    "Email": "Kitty46@gmail.com",
    "Company": "O'Reilly Group",
    "Job Title": "Dynamic Functionality Facilitator",
    "ITIN": "991-22-2906",
    "Username": "Cassandre.Kub43",
    "SSN": "914-22-2906",
    "DOB": "2020-08-27",
    "Phone Number": "1-2#######1718",
    "Bank Account No": "69741187",
    "Credit Card Number": "6441-6289-6867-2162-2711",
    "Passport No": "94f311e93a623c72ccb6fc46cf5f5b0265ccb42c517498a0f27fd4c43b47111e",
    "DL NO#": "USA_DL"
}

```

In the above script, the `Phone Number` was partially redacted with `#`. The `Passport No` was changed
into a SHA256 hash. The `DL NO#` was detected as a USA driver license number and was redacted to “USA_DL” just like it was
stated in the `detectionParameters`.

###### Note

The classifyColumns API is not available for use with fine-grained actions due to the nature of the API.
This API performs column sampling (adjustable by the user but has default values) to perform detection more quickly.
Fine-grained actions require iterating over every value for this reason.

### Persistent Audit Log

A new feature introduced with fine-grained actions (but also available when using the normal APIs) is the presence of a
persistent audit log. Currently, running the detect API adds an additional column (defaults to `DetectedEntities`
but customizable through the `outputColumnName`) parameter with PII detection metadata. This now has an
“actionUsed” metadata key, which is one of `DETECT`, `PARTIAL_REDACT`, `SHA256_HASH`,
`REDACT`.

```
"DetectedEntities": {
    "Credit Card Number": [
        {
            "entityType": "CREDIT_CARD",
            "actionUsed": "DETECT",
            "start": 0,
            "end": 19
        }
    ],
    "Phone Number": [
        {
            "entityType": "PHONE_NUMBER",
            "actionUsed": "REDACT",
            "start": 0,
            "end": 14
        }
    ]
}

```

Even customers using APIs without fine-grained actions such as `detect(entityTypesToDetect, outputColumnName)`
will see this persistent audit log in the resulting dataframe.

Customers using APIs with fine-grained actions will see all of the actions, regardless of if they are redacted or not.
Example:

````
+---------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Credit Card Number  |  Phone Number  |                                                                                            DetectedEntities                                                                                             | +---------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 622126741306XXXX    | +12#####7890   | {"Credit Card Number":[{"entityType":"CREDIT_CARD","actionUsed":"PARTIAL_REDACT","start":0,"end":16}],"Phone Number":[{"entityType":"PHONE_NUMBER","actionUsed":"PARTIAL_REDACT","start":0,"end":12}]}} |
| 6221 2674 1306 XXXX | +12#######7890 | {"Credit Card Number":[{"entityType":"CREDIT_CARD","actionUsed":"PARTIAL_REDACT","start":0,"end":19}],"Phone Number":[{"entityType":"PHONE_NUMBER","actionUsed":"PARTIAL_REDACT","start":0,"end":14}]}} |
| 6221-2674-1306-XXXX | 22#######7890  | {"Credit Card Number":[{"entityType":"CREDIT_CARD","actionUsed":"PARTIAL_REDACT","start":0,"end":19}],"Phone Number":[{"entityType":"PHONE_NUMBER","actionUsed":"PARTIAL_REDACT","start":0,"end":14}]}} | +---------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ ``` If you do not want to see the **DetectedEntities** column, you can simply drop the additional column in a custom script.
````
