# Using the additionalParams

object to tune the export of model-training information

The `additionalParams` object contains fields that you can use
to specify machine-learning class labels and features for training purposes and
guide the creation of a training data configuration file.

The export process cannot automatically infer which node and edge properties
should be the machine learning class labels to serve as examples for training
purposes. It also cannot automatically infer the best feature encoding for numeric,
categorical and text properties, so you need to supply hints using fields in the
`additionalParams` object to specify these things, or to override the
default encoding.

For property-graph data, the top-level structure of `additionalParams`
in an export request might look like this:

```
{
  "command": "export-pg",
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "profile": "neptune_ml"
  },
  "additionalParams": {
      "neptune_ml": {
        "version": "v2.0",
        "targets": [ `(an array of node and edge class label targets)` ],
        "features": [ `(an array of node feature hints)` ]
    }
  }
}
```

For RDF data, its top-level structure might look like this:

```
{
  "command": "export-rdf",
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "profile": "neptune_ml"
  },
  "additionalParams": {
      "neptune_ml": {
        "version": "v2.0",
        "targets": [ `(an array of node and edge class label targets)` ]
    }
  }
}
```

You can also supply multiple export configurations, using the `jobs` field:

```
{
  "command": "export-pg",
  "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export",
  "params": {
    "endpoint": "`(your Neptune endpoint DNS name)`",
    "profile": "neptune_ml"
  },
  "additionalParams" : {
    "neptune_ml" : {
      "version": "v2.0",
      "jobs": [
        {
          "name" : "`(training data configuration name)`",
          "targets": [ `(an array of node and edge class label targets)` ],
          "features": [ `(an array of node feature hints)` ]
        },
        {
          "name" : "`(another training data configuration name)`",
          "targets": [ `(an array of node and edge class label targets)` ],
          "features": [ `(an array of node feature hints)` ]
        }
      ]
    }
  }
}
```
