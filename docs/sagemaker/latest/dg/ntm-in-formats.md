# NTM Response Formats

All Amazon SageMaker AI built-in algorithms adhere to the common input inference format described in
[Common Data Formats - Inference](cdf-inference.md "cdf-inference.md"). This topic contains a list of the available output
formats for the SageMaker AI NTM algorithm.

## JSON Response Format

```
{
    "predictions":    [
        {"topic_weights": [0.02, 0.1, 0,...]},
        {"topic_weights": [0.25, 0.067, 0,...]}
    ]
}
```

## JSONLINES Response Format

```
{"topic_weights": [0.02, 0.1, 0,...]}
{"topic_weights": [0.25, 0.067, 0,...]}
```

## RECORDIO Response Format

```
[
    Record = {
        features = {},
        label = {
            'topic_weights': {
                keys: [],
                values: [0.25, 0.067, 0, ...]  # float32
            }
        }
    },
    Record = {
        features = {},
        label = {
            'topic_weights': {
                keys: [],
                values: [0.25, 0.067, 0, ...]  # float32
            }
        }
    }
]
```
