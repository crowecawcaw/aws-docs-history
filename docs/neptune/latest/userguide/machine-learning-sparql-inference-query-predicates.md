# Neptune ML predicates used in SPARQL inference queries

The following predicates are used with SPARQL inference:

## `neptune-ml:timeout` predicate

Specifies the timeout for connection with the remote server. Should not be confused
with the query request timeout, which is the maximum amount of time the server can take to
satisfy a request.

Note that if the query timeout occurs before the service timeout specified by the
`neptune-ml:timeout` predicate occurs, the service connection is canceled too.

## `neptune-ml:outputClass` predicate

The `neptune-ml:outputClass` predicate is only used to define the class
of the predicted object for object prediction or predicted subject for subect prediction.

## `neptune-ml:outputScore` predicate

The `neptune-ml:outputScore` predicate is a positive number that
represents the likelihood that the output of a machine learning model is correct.

## `neptune-ml:modelType` predicate

The `neptune-ml:modelType` predicate specifies the type of machine learning
model being trained:

- `OBJECT_CLASSIFICATION`
- `OBJECT_REGRESSION`
- `OBJECT_PREDICTION`
- `SUBJECT_PREDICTION`

## `neptune-ml:input` predicate

The `neptune-ml:input` predicate refers to the list of URIs used as inputs
for Neptune ML.

## `neptune-ml:output` predicate

The `neptune-ml:output` predicate refers to the list of binding sets
where Neptune ML returns results.

## `neptune-ml:predicate` predicate

The `neptune-ml:predicate` predicate is used differently depending on
the task being performed:

- For **object or subject prediction**: defines the
  type of predicate (the edge or relationship type).
- For **object classification and regression**:
  defines the literal (property) we want to predict.

## `neptune-ml:batchSize` predicate

The `neptune-ml:batchSize` specifies the input size for the remote
service call.
