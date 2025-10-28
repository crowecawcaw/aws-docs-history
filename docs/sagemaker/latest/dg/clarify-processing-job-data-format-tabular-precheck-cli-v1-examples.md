# AWS CLI v1 examples

The example in the preceding section was for AWS CLI v2. The following request and response examples to and from the endpoint use AWS CLI
v1.

In the following code example, the request consists of a single record and
the response is its probability value.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-sagemaker-xgboost-model \
  --content-type text/csv \
  --accept text/csv \
  --body '1,2,3,4' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
0.6
```

In the following code example, the request consists of two records, and
the response includes their probabilities, which are separated by a
comma.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-sagemaker-xgboost-model \
  --content-type text/csv \
  --accept text/csv \
  --body $'1,2,3,4\n5,6,7,8' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the `$'content'` expression in
the `--body` tells the command to interpret `'\n'` in
the content as a line break. The response output follows.

```
0.6,0.3
```

In the following code example, the request consists of two records, the
response includes their probabilities, separated with a line break.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-csv-1 \
  --content-type text/csv \
  --accept text/csv \
  --body $'1,2,3,4\n5,6,7,8' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
0.6
0.3

```

In the following code example, the request consists of a single record,
and the response is probability values from a multiclass model containing
three classes.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-csv-1 \
  --content-type text/csv \
  --accept text/csv \
  --body '1,2,3,4' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
0.1,0.6,0.3
```

In the following code example, the request consists of two records, and
the response includes their probability values from a multiclass model
containing three classes.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-csv-1 \
  --content-type text/csv \
  --accept text/csv \
  --body $'1,2,3,4\n5,6,7,8' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
0.1,0.6,0.3
0.2,0.5,0.3

```

In the following code example, the request consists of two records, and
the response includes predicted label and probability.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-csv-2 \
  --content-type text/csv \
  --accept text/csv \
  --body $'1,2,3,4\n5,6,7,8' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
1,0.6
0,0.3

```

In the following code example, the request consists of two records and the
response includes label headers and probabilities.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-csv-3 \
  --content-type text/csv \
  --accept text/csv \
  --body $'1,2,3,4\n5,6,7,8' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
"['cat','dog','fish']","[0.1,0.6,0.3]"
"['cat','dog','fish']","[0.2,0.5,0.3]"

```

In the following code example, the request consists of a single record and
the response is its probability value.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-jsonlines \
  --content-type application/jsonlines \
  --accept application/jsonlines \
  --body '{"features":["This is a good product",5]}' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
{"score":0.6}
```

In the following code example, the request contains two records, and the
response includes predicted label and probability.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-jsonlines-2 \
  --content-type application/jsonlines \
  --accept application/jsonlines \
  --body $'{"features":[1,2,3,4]}\n{"features":[5,6,7,8]}' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
{"predicted_label":1,"probability":0.6}
{"predicted_label":0,"probability":0.3}

```

In the following code example, the request contains two records, and the
response includes label headers and probabilities.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-jsonlines-3 \
  --content-type application/jsonlines \
  --accept application/jsonlines \
  --body $'{"data":{"features":[1,2,3,4]}}\n{"data":{"features":[5,6,7,8]}}' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
{"predicted_labels":["cat","dog","fish"],"probabilities":[0.1,0.6,0.3]}
{"predicted_labels":["cat","dog","fish"],"probabilities":[0.2,0.5,0.3]}

```

In the following code example, the request is in CSV format and the
response is in JSON Lines format.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-csv-in-jsonlines-out \
  --content-type text/csv \
  --accept application/jsonlines \
  --body $'1,2,3,4\n5,6,7,8' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
{"probability":0.6}
{"probability":0.3}

```

In the following code example, the request is in JSON Lines format and the
response is in CSV format.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-jsonlines-in-csv-out \
  --content-type application/jsonlines \
  --accept text/csv \
  --body $'{"features":[1,2,3,4]}\n{"features":[5,6,7,8]}' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
0.6
0.3

```

In the following code example, the request is in CSV format and the
response is in JSON format.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name test-endpoint-csv-in-jsonlines-out \
  --content-type text/csv \
  --accept application/jsonlines \
  --body $'1,2,3,4\n5,6,7,8' \
  /dev/stderr 1>/dev/null
```

From the previous code example, the response output follows.

```
{"predictions":[{"label":1,"score":0.6},{"label":0,"score":0.3}]}
```
