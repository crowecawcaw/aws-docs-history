# Command-line arguments for the GraphQL utility

- **`--help, -h`**   –  
  Returns help text for the GraphQL utility to the console.
- **`--input-schema `(schema text)``**   –  
  A GraphQL schema, with or without directives, to use as input.
- **`--input-schema-file `(file URL)``**   –  
  The URL of a file containing a GraphQL schema to use as input.
- **`--input-schema-changes-file `(file URL)``**   –  
  The URL of a file containing changes you want made to a GraphQL schema.
  If you run the utility against a Neptune database multiple times, and also
  manually change the GraphQL source schema, maybe adding a custom query,
  your manual chnages will be lost. To avoid this, put your changes in a changes file
  and pass it in using this argument.

The changes file uses the following JSON format:

```
[
  {
    "type": "`(GraphQL type name)`",
    "field": "`(GraphQL field name)`",
    "action": "`(remove or add)`",
    "value": "`(value)`"
  }
]
```

See the[Todo example](tools-graphql-start-from-schema.md#tools-graphql-todo-example "tools-graphql-start-from-schema.md#tools-graphql-todo-example")
for more information.

- **`--input-graphdb-schema `(schema text)``**   –  
  Instead of running the utility against a Neptune database, you can express
  a graphdb schema in text form to use as input. A graphdb schema has a JSON
  format like this:

```
{
  "nodeStructures": [
    { "label":"nodelabel1",
      "properties": [
        { "name":"name1", "type":"type1" }
      ]
    },
    { "label":"nodelabel2",
      "properties": [
          { "name":"name2", "type":"type1" }
      ]
    }
  ],
  "edgeStructures": [
    {
      "label":"label1",
      "directions": [
        { "from":"nodelabel1", "to":"nodelabel2", "relationship":"ONE-ONE|ONE-MANY|MANY-MANY"  }
      ],
      "properties": [
        { "name":"name1", "type":"type1" }
      ]
    }
  ]
}
```

- **`--input-graphdb-schema-file `(file URL)``**   –  
  Instead of running the utility against a Neptune database, you can save
  a graphdb schema in in a file to use as input. See `--input-graphdb-schema`
  above for an example of the JSON format for a graphdb schema file.
- **`--input-graphdb-schema-neptune-endpoint `(endpoint URL)``**   –  
  The Neptune database enpoint from which the utility should extract the graphdb schema.
- **`--output-schema-file `(file name)``**   –  
  The output file name for the GraphQL schema. If not specified the default is
  `output.schema.graphql`, unless a pipeline name has been set using
  `--create-update-aws-pipeline-name`, in which case the default file name is
  ``(pipline name)`.schema.graphql`.
- **`--output-source-schema-file `(file name)``**   –  
  The output file name for the GraphQL schema with directives. If not specified
  the default is `output.source.schema.graphql`, unless a pipeline name
  has been set using `--create-update-aws-pipeline-name`, in which case the default
  name is ``(pipeline name)`.source.schema.graphql`.
- **`--output-schema-no-mutations`**   –  
  If this argument is present, the utility generates no mutations in the GraphQL API,
  only queries.
- **`--output-neptune-schema-file `(file name)``**   –  
  The output file name for Neptune graphdb schema that the utility discovers. If not
  specified the default is `output.graphdb.json`, unless a pipeline name has
  been set using `--create-update-aws-pipeline-name`, in which case the
  default file name is ``(pipeline name)`.graphdb.json`.
- **`--output-js-resolver-file `(file name)``**   –  
  The output file name for a copy of the resolver code. If not specified the default
  is `output.resolver.graphql.js`, unless a pipeline name has been set using
  `--create-update-aws-pipeline-name`, in which case the file name is
  ``(pipeline name)`.resolver.graphql.js`.

This file is zipped in the code package uploaded to the Lambda function that
runs the resolver.

- **`--output-resolver-query-sdk`**   –  
  This argument specifies that the utility's Lambda function should query Neptune
  using the Neptune data SDK, which has been available starting with Neptune
  [engine version 1.2.1.0.R5](engine-releases-1.2.1.0.md "engine-releases-1.2.1.0.md") (this is
  the default). However, if the utility detects an older Neptune engine version,
  it suggests using the HTTPS Lambda option instead, which you can invoke using the
  `--output-resolver-query-https` argument.
- **`--output-resolver-query-https`**   –  
  This argument specifies that the utility's Lambda function should query Neptune
  using the Neptune HTTPS API.
- **`--create-update-aws-pipeline`**   –  
  This argument triggers the creation of the AWS resources for the GraphQL API to use,
  including the AppSync GraphQL API and the Lambda that runs the resolver.
- **`--create-update-aws-pipeline-name `(pipeline name)``**   –  
  This argument sets the name for the pipeline, like the `pipeline-name` API for
  AppSync or `pipeline-name` function for the Lambda function. If a name is not
  specified, `--create-update-aws-pipeline` uses the `Neptune` database
  name.
- **`--create-update-aws-pipeline-region `(AWS region)``**   –  
  This argument sets the AWS region in which the pipeline for the GraphQL API is created.
  If not specified, the default region is either `us-east-1` or the region
  where the Neptune database is located, extracted from the database endpoint.
- **`--create-update-aws-pipeline-neptune-endpoint `(endpoint URL)``**   –  
  This argument sets the Neptune database endpoint used by the Lambda function
  to query the database. If not set, the endpoint set by
  `--input-graphdb-schema-neptune-endpoint` is used.
- **`--remove-aws-pipeline-name `(pipeline name)``**   –  
  This argument removes a pipeline created using `--create-update-aws-pipeline`.
  The resources to remove are listed in a file named
  ``(pipeline name)`.resources.json`.
- **`--output-aws-pipeline-cdk`**   –  
  This argument triggers the creation of a CDK file that can be used to create the AWS
  resources for the GraphQL API, including the AppSync GraphQL API and the
  Lambda function that runs the resolver.
- **`--output-aws-pipeline-cdk-neptume-endpoint `(endpoint URL)``**   –  
  This argument sets the Neptune database endpoint used by the Lambda function to query
  the Neptune database. If not set, the endpoint set by
  `--input-graphdb-schema-neptune-endpoint` is used.
- **`--output-aws-pipeline-cdk-name `(pipeline name)``**   –  
  This argument sets the pipeline name for the AppSync API and the Lambda pipeline-name function
  to use. If not specified, `--create-update-aws-pipeline` uses the Neptune
  database name.
- **`--output-aws-pipeline-cdk-region `(AWS region)``**   –  
  This sets the AWS region in which the pipeline for the GraphQL API is created. If not
  specified, it defaults to `us-east-1` or region where the Neptune database
  is located, extracted from the database endpoint.
- **`--output-aws-pipeline-cdk-file `(file name)``**   –  
  This sets the CDK file name. If not set the default is ``(pipeline name)`-cdk.js`.
