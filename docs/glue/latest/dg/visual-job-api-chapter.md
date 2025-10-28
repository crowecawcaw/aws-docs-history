# AWS Glue Visual Job API

AWS Glue provides an API that allows customers to create data integration jobs using the AWS Glue
API from a JSON object that represents a visual step workflow.
Customers can then use the visual editor in AWS Glue Studio to work with these jobs.

For more information on Visual Job API data types, see [Visual Job API](aws-glue-api-visual-job-api.md "aws-glue-api-visual-job-api.md").

######

Topics

- [API design and CRUD APIs](#visual-job-api-design "#visual-job-api-design")
- [Getting started](#getting-started-visual-job-api "#getting-started-visual-job-api")
- [Visual job limitations](#visual-job-limitations "#visual-job-limitations")

##

API design and CRUD APIs

The CreateJob and UpdateJob
[APIs](aws-glue-api-jobs-job.md "aws-glue-api-jobs-job.md")
now support an additional optional parameter, codeGenConfigurationNodes.
Providing a non-empty JSON structure for this field will result in the DAG being registered in AWS Glue Studio
for the created job
and the associated code being generated. A null value or empty string for this field on job create will be ignored.

Updates to the codeGenConfigurationNodes field will be done through the UpdateJob AWS Glue API in
a similar way as CreateJob. The entire field should be specified in UpdateJob where the DAG has been changed as desired.
A null value provided will be ignored and no update to the DAG would be performed. An empty structure or string will cause
the codeGenConfigurationNodes to be set as empty and any previous DAG removed. The GetJob API will return a DAG if
one exists.
The DeleteJob API will also delete any associated DAG.

##

Getting started

To create a job, use the
[CreateJob action](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob") . The `CreateJob` request input will have an additional field
‘codeGenConfigurationNodes’ where you can get specify the DAG object in JSON.

Things to keep in mind:

- The ‘codeGenConfigurationNodes’ field is a map of nodeId to node.
- Each node begins with a key identifying what kind of node it is.
- There can only be one key specified since a node can only be of one type.
- The input field contains the parent nodes of the current node.

The following is a JSON representation of a **CreateJob** input.

```
{
  "node-1": {
    "S3CatalogSource": {
      "Table": "csvFormattedTable",
      "PartitionPredicate": "",
      "Name": "S3 bucket",
      "AdditionalOptions": {},
      "Database": "myDatabase"
    }
  },
  "node-3": {
    "S3DirectTarget": {
      "Inputs": ["node-2"],
      "PartitionKeys": [],
      "Compression": "none",
      "Format": "json",
      "SchemaChangePolicy": { "EnableUpdateCatalog": false },
      "Path": "",
      "Name": "S3 bucket"
    }
  },
  "node-2": {
    "ApplyMapping": {
      "Inputs": ["node-1"],
      "Name": "ApplyMapping",
      "Mapping": [
        {
          "FromType": "long",
          "ToType": "long",
          "Dropped": false,
          "ToKey": "myheader1",
          "FromPath": ["myheader1"]
        },
        {
          "FromType": "long",
          "ToType": "long",
          "Dropped": false,
          "ToKey": "myheader2",
          "FromPath": ["myheader2"]
        },
        {
          "FromType": "long",
          "ToType": "long",
          "Dropped": false,
          "ToKey": "myheader3",
          "FromPath": ["myheader3"]
        }
      ]
    }
  }
}

```

**Updating and getting jobs**

Since _UpdateJob_ will also have a ‘codeGenConfigurationNodes’ field, the input format will
be the same. See
[UpdateJob](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-UpdateJob") Action.

The _GetJob_ action will return a ‘codeGenConfigurationNodes’ field in the same format as well. See
[GetJob](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-GetJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-GetJob") Action.

##

Visual job limitations

Since the ‘codeGenConfigurationNodes’ parameter has been added to existing APIs, any limitations in those APIs
will be inherited. In addition, the codeGenConfigurationNodes and some nodes will be limited in size.
See
[Job Structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job") for more information.
