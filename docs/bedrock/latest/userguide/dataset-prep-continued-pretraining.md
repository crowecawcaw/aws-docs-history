# Prepare datasets for continued pre-training

To carry out continued pre-training on a text-to-text model, prepare a training and optional validation
dataset. Because Continued Pre-training involves unlabeled data, each JSON line is a sample containing only
an `input` field. Use 6 characters per token as an approximation for the number of tokens. The
format is as follows.

```
{"input": "<input text>"}
{"input": "<input text>"}
{"input": "<input text>"}
```

The following is an example item that could be in the training data.

```
{"input": "AWS stands for Amazon Web Services"}
```
