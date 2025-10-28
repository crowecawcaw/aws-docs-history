# Common data formats for inference

Amazon SageMaker AI algorithms accept and produce several different MIME types for the
HTTP payloads used in retrieving online and mini-batch predictions. You can use
multiple AWS services to transform or preprocess records before running
inference. At a minimum, you need to convert the data for the following:

- Inference request serialization (handled by you)
- Inference request deserialization (handled by the algorithm)
- Inference response serialization (handled by the algorithm)
- Inference response deserialization (handled by you)

###### Topics

- [Convert data for inference request
  serialization](#ir-serialization "#ir-serialization")
- [Convert data for inference response
  deserialization](#ir-deserialization "#ir-deserialization")
- [Common request formats for all
  algorithms](#common-in-formats "#common-in-formats")
- [Use batch transform with built-in
  algorithms](#cm-batch "#cm-batch")

## Convert data for inference request

serialization

Content type options for Amazon SageMaker AI algorithm inference requests include:
`text/csv`, `application/json`, and
`application/x-recordio-protobuf`. Algorithms that don't
support all of these types can support other types. XGBoost, for example,
only supports `text/csv` from this list, but also supports
`text/libsvm`.

For `text/csv`, the value for the Body argument to
`invoke_endpoint` should be a string with commas separating
the values for each feature. For example, a record for a model with four
features might look like `1.5,16.0,14,23.0`. Any transformations
performed on the training data should also be performed on the data before
obtaining inference. The order of the features matters and must remain
unchanged.

`application/json` is more flexible and provides multiple
possible formats for developers to use in their applications. At a high
level, in JavaScript, the payload might look like the following:

```
let request = {
  // Instances might contain multiple rows that predictions are sought for.
  "instances": [
    {
      // Request and algorithm specific inference parameters.
      "configuration": {},
      // Data in the specific format required by the algorithm.
      "data": {
         "<field name>": dataElement
       }
    }
  ]
}
```

You have the following options for specifying the
`dataElement`:

**Protocol buffers equivalent**

```
// Has the same format as the protocol buffers implementation described for training.
let dataElement = {
  "keys": [],
  "values": [],
  "shape": []
}
```

**Simple numeric vector**

```
// An array containing numeric values is treated as an instance containing a
// single dense vector.
let dataElement = [1.5, 16.0, 14.0, 23.0]

// It will be converted to the following representation by the SDK.
let converted = {
  "features": {
    "values": dataElement
  }
}
```

**For multiple records**

```
let request = {
  "instances": [
    // First instance.
    {
      "features": [ 1.5, 16.0, 14.0, 23.0 ]
    },
    // Second instance.
    {
      "features": [ -2.0, 100.2, 15.2, 9.2 ]
    }
  ]
}
```

## Convert data for inference response

deserialization

Amazon SageMaker AI algorithms return JSON in several layouts. At a high level, the
structure is:

```
let response = {
  "predictions": [{
    // Fields in the response object are defined on a per algorithm-basis.
  }]
}
```

The fields that are included in predictions differ across algorithms. The
following are examples of output for the k-means algorithm.

**Single-record inference**

```
let response = {
  "predictions": [{
    "closest_cluster": 5,
    "distance_to_cluster": 36.5
  }]
}
```

**Multi-record inference**

```
let response = {
  "predictions": [
    // First instance prediction.
    {
      "closest_cluster": 5,
      "distance_to_cluster": 36.5
    },
    // Second instance prediction.
    {
      "closest_cluster": 2,
      "distance_to_cluster": 90.3
    }
  ]
}
```

**Multi-record inference with protobuf input**

```
{
  "features": [],
  "label": {
    "closest_cluster": {
      "values": [ 5.0 ] // e.g. the closest centroid/cluster was 1.0
    },
    "distance_to_cluster": {
      "values": [ 36.5 ]
    }
  },
  "uid": "abc123",
  "metadata": "{ "created_at": '2017-06-03' }"
}
```

SageMaker AI algorithms also support the JSONLINES format, where the per-record
response content is same as that in JSON format. The multi-record structure
is a collection of per-record response objects separated by newline
characters. The response content for the built-in KMeans algorithm for 2
input data points is:

```
{"distance_to_cluster": 23.40593910217285, "closest_cluster": 0.0}
{"distance_to_cluster": 27.250282287597656, "closest_cluster": 0.0}
```

While running batch transform, we recommended using the
`jsonlines` response type by setting the `Accept`
field in the `CreateTransformJobRequest` to
`application/jsonlines`.

## Common request formats for all

algorithms

Most algorithms use many of the following inference request
formats.

### JSON request format

**Content type:** application/JSON

**Dense format**

```
let request =   {
    "instances":    [
        {
            "features": [1.5, 16.0, 14.0, 23.0]
        }
    ]
}


let request =   {
    "instances":    [
        {
            "data": {
                "features": {
                    "values": [ 1.5, 16.0, 14.0, 23.0]
                }
            }
        }
    ]
}
```

**Sparse format**

```
{
	"instances": [
		{"data": {"features": {
					"keys": [26, 182, 232, 243, 431],
					"shape": [2000],
					"values": [1, 1, 1, 4, 1]
				}
			}
		},
		{"data": {"features": {
					"keys": [0, 182, 232, 243, 431],
					"shape": [2000],
					"values": [13, 1, 1, 4, 1]
				}
			}
		},
	]
}
```

### JSONLINES request format

**Content type:**
application/JSONLINES

**Dense format**

A single record in dense format can be represented as either:

```
{ "features": [1.5, 16.0, 14.0, 23.0] }
```

or:

```
{ "data": { "features": { "values": [ 1.5, 16.0, 14.0, 23.0] } }
```

**Sparse Format**

A single record in sparse format is represented as:

```
{"data": {"features": { "keys": [26, 182, 232, 243, 431], "shape": [2000], "values": [1, 1, 1, 4, 1] } } }
```

Multiple records are represented as a collection of single-record
representations, separated by newline characters:

```
{"data": {"features": { "keys": [0, 1, 3], "shape": [4], "values": [1, 4, 1] } } }
{ "data": { "features": { "values": [ 1.5, 16.0, 14.0, 23.0] } }
{ "features": [1.5, 16.0, 14.0, 23.0] }
```

### CSV request format

**Content type:** text/CSV;
label_size=0

###### Note

CSV support is not available for factorization machines.

### RECORDIO request format

Content type: application/x-recordio-protobuf

## Use batch transform with built-in

algorithms

While running batch transform, we recommended using the JSONLINES response
type instead of JSON, if supported by the algorithm. To do this, set the
`Accept` field in the `CreateTransformJobRequest`
to `application/jsonlines`.

When you create a transform job, the `SplitType` must be set
based on the `ContentType` of the input data. Similarly,
depending on the `Accept` field in the
`CreateTransformJobRequest`, `AssembleWith` must
be set accordingly. Use the following table to set these fields:

| ContentType                       | Recommended SplitType    |
| --------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `application/x-recordio-protobuf` | `RecordIO`               |
| `text/csv`                        | `Line`                   |
| `application/jsonlines`           | `Line`                   |
| `application/json`                | `None`                   |
| `application/x-image`             | `None`                   |
| `image/*`                         | `None`                   |
| Accept                            | Recommended AssembleWith |
| ---                               | ---                      |
| `application/x-recordio-protobuf` | `None`                   |
| `application/json`                | `None`                   |
| `application/jsonlines`           | `Line`                   | For more information on response formats for specific algorithms, see the following: <br>• [DeepAR Inference Formats](deepar-in-formats.md "deepar-in-formats.md") <br>• [Factorization Machines Response Formats](fm-in-formats.md "fm-in-formats.md") <br>• [IP Insights Inference Data Formats](ip-insights-inference-data-formats.md "ip-insights-inference-data-formats.md") <br>• [K-Means Response Formats](km-in-formats.md "km-in-formats.md") <br>• [k-NN Request and Response Formats](kNN-inference-formats.md "kNN-inference-formats.md") <br>• [Linear learner response formats](LL-in-formats.md "LL-in-formats.md") <br>• [NTM Response Formats](ntm-in-formats.md "ntm-in-formats.md") <br>• [Data Formats for Object2Vec Inference](object2vec-inference-formats.md "object2vec-inference-formats.md") <br>• [Encoder Embeddings for Object2Vec](object2vec-encoder-embeddings.md "object2vec-encoder-embeddings.md") <br>• [PCA Response Formats](PCA-in-formats.md "PCA-in-formats.md") <br>• [RCF Response Formats](rcf-in-formats.md "rcf-in-formats.md") |
