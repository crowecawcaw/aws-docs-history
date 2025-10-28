# PCA Response Formats

All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in
[Common Data Formats - Inference](cdf-inference.md "cdf-inference.md"). This topic contains a list of the available output
formats for the SageMaker AI PCA algorithm.

## JSON Response Format

Accept—application/json

```
{
    "projections": [
        {
            "projection": [1.0, 2.0, 3.0, 4.0, 5.0]
        },
        {
            "projection": [6.0, 7.0, 8.0, 9.0, 0.0]
        },
        ....
    ]
}
```

## JSONLINES Response Format

Accept—application/jsonlines

```
{ "projection": [1.0, 2.0, 3.0, 4.0, 5.0] }
{ "projection": [6.0, 7.0, 8.0, 9.0, 0.0] }
```

## RECORDIO Response Format

Accept—application/x-recordio-protobuf

```
[
    Record = {
        features = {},
        label = {
            'projection': {
                keys: [],
                values: [1.0, 2.0, 3.0, 4.0, 5.0]
            }
        }
    },
    Record = {
        features = {},
        label = {
            'projection': {
                keys: [],
                values: [1.0, 2.0, 3.0, 4.0, 5.0]
            }
        }
    }
]
```
