

# Examples of using the Neptune-Export service to export training data for Neptune ML
<a name="machine-learning-export-examples"></a>

This request exports property-graph training data for a node classification task:

------
#### [ curl ]

```
curl \
  {{(your NeptuneExportApiUri)}} \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "command": "export-pg",
        "outputS3Path": "s3://{{(your Amazon S3 bucket)}}/neptune-export",
        "params": {
          "endpoint": "{{(your Neptune endpoint DNS name)}}",
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

------
#### [ awscurl ]

```
awscurl {{(your NeptuneExportApiUri)}} \
  --region {{us-east-1}} \
  --service execute-api \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "command": "export-pg",
        "outputS3Path": "s3://{{(your Amazon S3 bucket)}}/neptune-export",
        "params": {
          "endpoint": "{{(your Neptune endpoint DNS name)}}",
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

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------

This request exports RDF training data for a node classification task:

------
#### [ curl ]

```
curl \
  {{(your NeptuneExportApiUri)}} \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "command": "export-rdf",
        "outputS3Path": "s3://{{(your Amazon S3 bucket)}}/neptune-export",
        "params": {
          "endpoint": "{{(your Neptune endpoint DNS name)}}",
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

------
#### [ awscurl ]

```
awscurl {{(your NeptuneExportApiUri)}} \
  --region {{us-east-1}} \
  --service execute-api \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "command": "export-rdf",
        "outputS3Path": "s3://{{(your Amazon S3 bucket)}}/neptune-export",
        "params": {
          "endpoint": "{{(your Neptune endpoint DNS name)}}",
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

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------