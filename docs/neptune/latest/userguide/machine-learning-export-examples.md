# Examples of using the

Neptune-Export service to export training data for Neptune ML

This request exports property-graph training data for a node classification task:

```
curl \
  `(your NeptuneExportApiUri)` \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "command": "export-pg",
        "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export",
        "params": {
          "endpoint": "`(your Neptune endpoint DNS name)`",
          "profile": "neptune_ml"
        },
        "additionalParams": {
          "neptune_ml": {
            "version": "v2.0",
            "targets": [
              {
                "node": "Movie",
                "property": "genre",
                "type": "classification"
              }
            ]
          }
        }
      }'
```

This request exports RDF training data for a node classification task:

```
curl \
  `(your NeptuneExportApiUri)` \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "command": "export-rdf",
        "outputS3Path": "s3://`(your Amazon S3 bucket)`/neptune-export",
        "params": {
          "endpoint": "`(your Neptune endpoint DNS name)`",
          "profile": "neptune_ml"
        },
        "additionalParams": {
          "neptune_ml": {
            "version": "v2.0",
            "targets": [
              {
                "node": "http://aws.amazon.com/neptune/csv2rdf/class/Movie",
                "predicate": "http://aws.amazon.com/neptune/csv2rdf/datatypeProperty/genre",
                "type": "classification"
              }
            ]
          }
        }
      }'
```
