# Getting started with a Domain dataset group (SDK for JavaScript v3)

This tutorial shows you how to use the AWS SDK for JavaScript v3 to create a Domain dataset group for the VIDEO_ON_DEMAND domain. In
this tutorial, you create a recommender for the _Top picks for you_ use case.

To view the code used in this tutorial on GitHub, see [Amazon Personalize code examples for SDK for JavaScript v3](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/personalize "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/personalize") in the _AWS SDK Code Examples_ repository.

When you finish the getting started exercise, to avoid incurring unnecessary charges,
delete the resources that you created. For more information, see
[Requirements for deleting Amazon Personalize resources](deleting-resources.md "deleting-resources.md").

###### Topics

- [Prerequisites](#gs-js-sdk-domain-prerequisites "#gs-js-sdk-domain-prerequisites")
- [Tutorial](#domain-gs-js-domain-tutorial "#domain-gs-js-domain-tutorial")

## Prerequisites

The following are prerequisite steps for completing this tutorial:

- Complete the [Getting started prerequisites](gs-prerequisites.md "gs-prerequisites.md") to set up the required
  permissions and create the training data. If you also completed the [Getting started with a Domain dataset group
  (console)](getting-started-console-domain.md "getting-started-console-domain.md"), you can reuse the same source data. If you are using your own source
  data, make sure that your data is formatted like in the prerequisites.
- Set up the SDK for JavaScript and AWS credentials as specified in the
  [Setting up the SDK for JavaScript](../../../sdk-for-javascript/v3/developer-guide/setting-up.md "../../../sdk-for-javascript/v3/developer-guide/setting-up.md") procedure in the _AWS SDK for JavaScript Developer Guide_.

## Tutorial

In the following steps, you install the required dependencies. Then you create a dataset group, import data, create a
recommender for the _Top picks for you_ use case, and get recommendations.

If you use Node.js, you can run each code sample
by saving the sample as a JavaScript file and then running `node <fileName.js>`.

After you complete the prerequisites, install the following Amazon Personalize dependencies:

- @aws-sdk/client-personalize
- @aws-sdk/client-personalize-runtime
- @aws-sdk/client-personalize-events (optional for this tutorial, but required if you want to
  [record events](recording-events.md "recording-events.md") after you create your recommender)
  The following is an example of a `package.json` file you can use. To install the dependencies with Node.js, navigate
  to where you saved the `package.json` file and run `npm install`.

```
{
  "name": "personalize-js-project",
  "version": "1.0.0",
  "description": "personalize operations",
  "type": "module",
  "author": "Author Name <email@address.com>",
  "license": "ISC",
  "dependencies": {
    "@aws-sdk/client-personalize": "^3.350.0",
    "@aws-sdk/client-personalize-events": "^3.350.0",
    "@aws-sdk/client-personalize-runtime": "^3.350.0",
    "fs": "^0.0.1-security"
  },
  "compilerOptions": {
    "resolveJsonModule": true,
    "esModuleInterop": true
  }
}
```

After you install the dependencies, create your Amazon Personalize clients. In this tutorial, the code samples assume you create
the clients in a file named `personalizeClients.js` stored in a directory named `libs`.

The following is an example of a `personalizeClient.js` file.

```
import { PersonalizeClient } from "@aws-sdk/client-personalize";
import { PersonalizeRuntimeClient } from "@aws-sdk/client-personalize-runtime";
import { PersonalizeEventsClient } from "@aws-sdk/client-personalize-events";
// Set your AWS region.
const REGION = "`region`"; //e.g. "us-east-1"

const personalizeClient = new PersonalizeClient({ region: REGION});
const personalizeEventsClient = new PersonalizeEventsClient({ region: REGION});
const personalizeRuntimeClient = new PersonalizeRuntimeClient({ region: REGION});

export { personalizeClient, personalizeEventsClient, personalizeRuntimeClient };
```

After you create your Amazon Personalize clients, import the historical data you created when you completed the [Getting started prerequisites](gs-prerequisites.md "gs-prerequisites.md"). To import historical data into Amazon Personalize, do the following:

1. Save the following Avro schema as a JSON file in your working directory. This schema matches the columns in
   the CSV file that you created when you completed the [Creating the training data (Domain dataset group)](gs-prerequisites.md#gs-data-prep-domain "gs-prerequisites.md#gs-data-prep-domain").

```
{
  "type": "record",
  "name": "Interactions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
      {
          "name": "USER_ID",
          "type": "string"
      },
      {
          "name": "ITEM_ID",
          "type": "string"
      },
      {
          "name": "EVENT_TYPE",
          "type": "string"
      },
      {
          "name": "TIMESTAMP",
          "type": "long"
      }
  ],
  "version": "1.0"
}
```

2. Create a domain schema in Amazon Personalize with the following `createDomainSchema.js` code. Replace `SCHEMA_PATH` with the
   path to the schema.json file you just created. Update the `createSchemaParam` to specify a name for the schema, and for `domain` specify
   `VIDEO_ON_DEMAND`.

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
  mySchema = "TEST"; // for unit tests.
}

// Set the domain schema parameters.
export const createDomainSchemaParam = {
  name: "NAME" /* required */,
  schema: mySchema /* required */,
  domain:
    "DOMAIN" /* required for a domain dataset group, specify ECOMMERCE or VIDEO_ON_DEMAND */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateSchemaCommand(createDomainSchemaParam),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

3. Create a domain dataset group in Amazon Personalize with the following `createDomainDatasetGroup.js` code. Update the `domainDatasetGroupParams` to specify a name for the dataset group,
   and for `domain` specify `VIDEO_ON_DEMAND`.

```
// Get service clients module and commands using ES6 syntax.
import { CreateDatasetGroupCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";

// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

// Set the domain dataset group parameters.
export const domainDatasetGroupParams = {
  name: "NAME" /* required */,
  domain:
    "DOMAIN" /* required for a domain dsg, specify ECOMMERCE or VIDEO_ON_DEMAND */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateDatasetGroupCommand(domainDatasetGroupParams),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

4. Create an Item interactions dataset in Amazon Personalize with the following `createDataset.js` code. Update the `createDatasetParam` to specify the Amazon Resource Name (ARN)
   of the dataset group and schema you just created, give the dataset a name, and for `datasetType`, specify `Interactions`.

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

5. Import your data with the following `createDatasetImportJob.js` code. Update the `datasetImportJobParam` to specify the following:
   - Specify a name for the job and specify your Interactions
     dataset's ARN.
   - For `dataLocation`, specify the Amazon S3 bucket path (`s3://`https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com`/`folder
     name`/ratings.csv`) where you stored the training data.
   - For `roleArn` specify the Amazon Resource Name for your Amazon Personalize service role. You
     created this role as part of the [Getting started prerequisites](gs-prerequisites.md "gs-prerequisites.md").

```
// Get service clients module and commands using ES6 syntax.
import { CreateDatasetImportJobCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";

// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

// Set the dataset import job parameters.
export const datasetImportJobParam = {
  datasetArn: "DATASET_ARN" /* required */,
  dataSource: {
    /* required */
    dataLocation: "S3_PATH",
  },
  jobName: "NAME" /* required */,
  roleArn: "ROLE_ARN" /* required */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateDatasetImportJobCommand(datasetImportJobParam),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

After your dataset import job completes, you are ready create a recommender.
To create a recommender, use the following `createRecommender.js` code.
Update the `createRecommenderParam` with the following:
Specify a name for the recommender, specify your dataset group's ARN, and for `recipeArn` specify
`arn:aws:personalize:::recipe/aws-vod-top-picks`.

```
// Get service clients module and commands using ES6 syntax.
import { CreateRecommenderCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";

// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

// Set the recommender's parameters.
export const createRecommenderParam = {
  name: "NAME" /* required */,
  recipeArn: "RECIPE_ARN" /* required */,
  datasetGroupArn: "DATASET_GROUP_ARN" /* required */,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateRecommenderCommand(createRecommenderParam),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

After you create a recommender, you use it to get recommendations. Use the following
`getRecommendations.js` code to get recommendations for a user. Update the `getRecommendationsParam`
to specify the ARN of the recommender you created in the previous step, and specify a user ID (for example,
`123`).

```
// Get service clients module and commands using ES6 syntax.
import { GetRecommendationsCommand } from "@aws-sdk/client-personalize-runtime";
import { personalizeRuntimeClient } from "./libs/personalizeClients.js";
// Or, create the client here.
// const personalizeRuntimeClient = new PersonalizeRuntimeClient({ region: "REGION"});

// Set the recommendation request parameters.
export const getRecommendationsParam = {
  recommenderArn: "RECOMMENDER_ARN" /* required */,
  userId: "USER_ID" /* required */,
  numResults: 15 /* optional */,
};

export const run = async () => {
  try {
    const response = await personalizeRuntimeClient.send(
      new GetRecommendationsCommand(getRecommendationsParam),
    );
    console.log("Success!", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```
