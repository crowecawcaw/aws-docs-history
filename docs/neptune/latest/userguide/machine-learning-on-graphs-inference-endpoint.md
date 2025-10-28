# Creating an inference endpoint to query

An inference endpoint lets you query one specific model that the model-training
process constructed. The endpoint attaches to the best-performing model of a given
type that the training process was able to generate. The endpoint is then able to
accept Gremlin queries from Neptune and return that model's predictions for inputs
in the queries. After you have created an inference endpoint, it stays active until
you delete it.

## Managing inference endpoints for Neptune ML

After you have completed model training on data that you exported from Neptune,
you can create an inference endpoint using a `curl` (or `awscurl`)
command like the following:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/endpoints
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "mlModelTrainingJobId": "`(the model-training job-id of a completed job)`"
      }'
```

You can also create an inference endpoint from a model created by a completed model
transform job, in much the same way:

```
curl \
  -X POST https://`(your Neptune endpoint)`/ml/endpoints
  -H 'Content-Type: application/json' \
  -d '{
        "id" : "`(a unique ID for the new endpoint)`",
        "mlModelTransformJobId": "`(the model-transform job-id of a completed job)`"
      }'
```

The details of how to use these commands are explained in [The endpoints command](machine-learning-api-endpoints.md "machine-learning-api-endpoints.md"),
along with information about how to get the status of an endpoint, how to delete an endpoint,
and how to list all inference endpoints.
