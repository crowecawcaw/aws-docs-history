# Factorization Machines Response Formats

Amazon SageMaker AI provides several response formats for getting inference from the Factorization Machines model,
such as JSON, JSONLINES, and RECORDIO, with specific structures for binary classification and regression tasks.

## JSON Response Format

Binary classification

```
let response =   {
    "predictions":    [
        {
            "score": 0.4,
            "predicted_label": 0
        }
    ]
}
```

Regression

```
let response =   {
    "predictions":    [
        {
            "score": 0.4
        }
    ]
}
```

## JSONLINES Response Format

Binary classification

```
{"score": 0.4, "predicted_label": 0}
```

Regression

```
{"score": 0.4}
```

## RECORDIO Response Format

Binary classification

```
[
    Record = {
        features = {},
        label = {
            'score’: {
                keys: [],
                values: [0.4]  # float32
            },
            'predicted_label': {
                keys: [],
                values: [0.0]  # float32
            }
        }
    }
]
```

Regression

```
[
    Record = {
        features = {},
        label = {
            'score’: {
                keys: [],
                values: [0.4]  # float32
            }
        }
    }
]

```
