# Creating a schema and a dataset

After you [create a dataset group](data-prep-ds-group.md "data-prep-ds-group.md"), you are ready to create
an Amazon Personalize schema and a dataset for each type of data you are importing. A _schema_ tells Amazon Personalize about the structure of your data and
allows Amazon Personalize to parse the data. When you create a schema in Amazon Personalize, you use the JSON file you created in [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

A _dataset_ is a container for training data in Amazon Personalize. Different dataset types have different requirements.
You create a dataset for each type of data you are importing. For information about the different types of datasets and how to prepare your data,
see [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md").

You can create schemas and datasets with the Amazon Personalize console, AWS Command Line Interface (AWS CLI),
or AWS SDKs. You can't create next best action resources, including Actions and Action Interactions datasets, in a domain dataset group.

###### Important

After you create a schema, you can't make changes to the schema. However, if you add new columns, you can replace a dataset's schema with a new one.
For more information, see [Replacing a dataset's schema to add new columns](updating-dataset-schema.md "updating-dataset-schema.md").

###### Topics

- [Creating a dataset and a schema
  (console)](#data-prep-creating-ds-console "#data-prep-creating-ds-console")
- [Creating a dataset and a schema (AWS CLI)](#data-prep-creating-ds-cli "#data-prep-creating-ds-cli")
- [Creating a dataset and a schema (AWS SDKs)](#data-prep-creating-ds-sdk "#data-prep-creating-ds-sdk")

## Creating a dataset and a schema

(console)

If this is your first dataset in your dataset group, your first dataset type will be an Item interactions dataset. To create your Item interactions dataset in the console,
specify the dataset name and then specify a JSON schema in [Avro format](https://docs.oracle.com/database/nosql-12.1.3.0/GettingStartedGuide/avroschemas.html "https://docs.oracle.com/database/nosql-12.1.3.0/GettingStartedGuide/avroschemas.html").
If it is not your first dataset in this dataset group, choose the dataset type and then specify a name and a schema.

For information on Amazon Personalize datasets requirements,
see [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md"). If you just completed [Creating an Amazon Personalize dataset group](data-prep-ds-group.md "data-prep-ds-group.md") and you are already creating
your dataset, skip to step 4 in this procedure.

###### To create a dataset and a schema

1. If you haven't already, follow the instructions in [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md") to create a schema JSON file that outlines your data.
2. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
3. On the **Dataset groups** page, choose the dataset group you created
   in [Creating an Amazon Personalize dataset group](data-prep-ds-group.md "data-prep-ds-group.md").
4. In **Step 1. Create datasets and import data** choose **Create dataset** and
   choose the type of dataset to create.
5. Choose **Import data directly into Amazon Personalize datasets** and choose **Next**.
6. In **Dataset details**, for **Dataset name**,
   specify a name for your dataset.
7. For **Dataset schema**,
   choose either **Create a new schema** or **Use an existing schema**.
8. If you are using an existing schema, choose the existing schema to use. If you are creating a new schema, give the schema a name and paste
   in the schema JSON that matches your data. You created this file in [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").
9. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
   [Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md").
10. Choose **Next** and follow the instructions in [Importing training data into Amazon Personalize datasets](import-data.md "import-data.md") to import your
    data.

## Creating a dataset and a schema (AWS CLI)

To create a dataset and a schema using the AWS CLI, you use the
the `create-schema` command (which uses the [CreateSchema](API_CreateSchema.md "API_CreateSchema.md") API operation) and
then `create-dataset` (which uses the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") API operation).

###### To create a schema and dataset

1. If you haven't already, follow the instructions in [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md") to create a schema JSON file that outlines your data.
2. Create a schema in Amazon Personalize by running the following command. After you create a schema, you can't make changes to the schema. Replace `schemaName` with the name of the schema, and replace
   `file://SchemaName.json` with the location of your JSON file. The example shows the file as belonging to the current folder.
   If you are creating a schema for a dataset in a Domain dataset group, add the `domain` parameter and set it to `ECOMMERCE` or `VIDEO_ON_DEMAND`.
   For more information about the API, see [CreateSchema](API_CreateSchema.md "API_CreateSchema.md").

```
aws personalize create-schema \
  --name `SchemaName` \
  --schema `file://SchemaName.json`
```

The schema Amazon Resource Name (ARN) is displayed, as shown in the following
example:

```
{
  "schemaArn": "arn:aws:personalize:us-west-2:acct-id:schema/SchemaName"
}
```

3. Create an empty dataset by running the following command. Provide the dataset group
   Amazon Resource Name (ARN) from [Creating a dataset group (AWS CLI)](data-prep-ds-group.md#data-prep-creating-ds-group-cli "data-prep-ds-group.md#data-prep-creating-ds-group-cli") and schema ARN from the previous step.
   Dataset type values can be `Interactions`, `Users`, `Items`, `Actions`,
   or `Action_Interactions`. For more information about the API, see [CreateDataset](API_CreateDataset.md "API_CreateDataset.md").

```
aws personalize create-dataset \
  --name `Dataset Name` \
  --dataset-group-arn `Dataset Group ARN` \
  --dataset-type `Dataset Type` \
  --schema-arn `Schema Arn`

```

The dataset ARN is displayed, as shown in the following example.

```
{
  "datasetArn": "arn:aws:personalize:us-west-2:acct-id:dataset/DatasetName/INTERACTIONS"
}
```

4. Record the dataset ARN for later use. After you create a dataset, you are ready to import your training data. See
   [Importing training data into Amazon Personalize datasets](import-data.md "import-data.md").

## Creating a dataset and a schema (AWS SDKs)

To create a dataset and a schema using the AWS SDKs, you first define a schema in
[Avro format](https://docs.oracle.com/database/nosql-12.1.3.0/GettingStartedGuide/avroschemas.html "https://docs.oracle.com/database/nosql-12.1.3.0/GettingStartedGuide/avroschemas.html")
and add it to Amazon Personalize using
the [CreateSchema](API_CreateSchema.md "API_CreateSchema.md") operation. After you create a schema, you can't make changes to the schema. Then create a dataset using the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") operation.

###### To create a schema and a dataset

1. If you haven't already, follow the instructions in [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md") to create a schema JSON file that outlines your data.
2. Create a schema in Amazon Personalize with the following code. Specify the name for your schema and the file path for your schema JSON file. If you are creating a schema for a dataset in a Domain dataset group, add the `domain` parameter and set it to `ECOMMERCE` or `VIDEO_ON_DEMAND`.
   For more information about the API, see [CreateSchema](API_CreateSchema.md "API_CreateSchema.md").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

with open('`schemaFile.json`') as f:
    createSchemaResponse = personalize.create_schema(
        name = '`schema name`',
        schema = f.read()
    )

schema_arn = createSchemaResponse['schemaArn']

print('Schema ARN:' + schema_arn )
```

SDK for Java 2.x

```
public static String createSchema(PersonalizeClient personalizeClient, String schemaName, String filePath) {

    String schema = null;

    try {
        schema = new String(Files.readAllBytes(Paths.get(filePath)));
    } catch (IOException e) {
        System.out.println(e.getMessage());
    }

    try {
        CreateSchemaRequest createSchemaRequest = CreateSchemaRequest.builder()
                .name(schemaName)
                .schema(schema)
                .build();

        String schemaArn = personalizeClient.createSchema(createSchemaRequest).schemaArn();
        System.out.println("Schema arn: " + schemaArn);

        return schemaArn;

    } catch(PersonalizeException e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
    return "";
}
```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { CreateSchemaCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";

// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

import fs from "node:fs";

const schemaFilePath = "SCHEMA_PATH";
let mySchema = "";

try {
  mySchema = fs.readFileSync(schemaFilePath).toString();
} catch (err) {
  mySchema = "TEST"; // For unit tests.
}
// Set the schema parameters.
export const createSchemaParam = {
  name: "NAME" /* required */,
  schema: mySchema /* required */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateSchemaCommand(createSchemaParam),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

Amazon Personalize returns the ARN of the new schema. Record it because you'll need it in the next
step. 3. Create a dataset using the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") operation. The following code shows how to create a dataset. Specify the Amazon Resource Name (ARN) of your dataset group,
the schema ARN from the previous step, and specify the dataset type. Dataset type values can be `Interactions`, `Users`, `Items`, `Actions`,
or `Action_Interactions`. For information about the different types of datasets, see [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

response = personalize.create_dataset(
    name = '`dataset_name`',
    schemaArn = '`schema_arn`',
    datasetGroupArn = '`dataset_group_arn`',
    datasetType = '`dataset_type`'
)

print ('Dataset Arn: ' + response['datasetArn'])
```

SDK for Java 2.x

```
public static String createDataset(PersonalizeClient personalizeClient,
                                    String datasetName,
                                    String datasetGroupArn,
                                    String datasetType,
                                    String schemaArn) {
    try {
        CreateDatasetRequest request = CreateDatasetRequest.builder()
                .name(datasetName)
                .datasetGroupArn(datasetGroupArn)
                .datasetType(datasetType)
                .schemaArn(schemaArn).build();

        String datasetArn = personalizeClient.createDataset(request).datasetArn();
        System.out.println("Dataset " + datasetName + " created. Dataset ARN: " + datasetArn);

        return datasetArn;

    } catch(PersonalizeException e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
    return "";
}
```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { CreateDatasetCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";

// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

// Set the dataset's parameters.
export const createDatasetParam = {
  datasetGroupArn: "DATASET_GROUP_ARN" /* required */,
  datasetType: "DATASET_TYPE" /* required */,
  name: "NAME" /* required */,
  schemaArn: "SCHEMA_ARN" /* required */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateDatasetCommand(createDatasetParam),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

After you create a dataset, you are ready to import your training data. See
[Importing training data into Amazon Personalize datasets](import-data.md "import-data.md").
