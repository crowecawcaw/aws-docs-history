# Classifier training output

After Amazon Comprehend completes the custom classifier model training, it creates output files in the Amazon S3 output
location that you specified in the [CreateDocumentClassifier](../APIReference/API_CreateDocumentClassifier.md "../APIReference/API_CreateDocumentClassifier.md") API request or the equivalent console
request.

Amazon Comprehend creates a confusion matrix when you train a plain-text model or a native document model.
It can create additional output files when you train a native document model.

###### Topics

- [Confusion matrix](#conf-matrix "#conf-matrix")
- [Additional outputs for native document models](#train-class-output-native "#train-class-output-native")

## Confusion matrix

When you train a custom classifier model, Amazon Comprehend creates a confusion matrix that provides metrics on how well
the model performed in training. This matrix shows a matrix of labels that the model predicted, compared to the
actual document labels. Amazon Comprehend uses a portion of the training data to create the confusion matrix.

A confusion matrix provides an indication of which classes could use more data to improve model performance. A
class with a high fraction of correct predictions has the highest number of results along the diagonal of the
matrix. If the number on the diagonal is a lower number, the class has a lower fraction of correct predictions.
You can add more training examples for this class and train the model again. For example, if 40 percent of label A
samples get classified as label D, adding more samples for label A and label D enhances the classifier's
performance.

After Amazon Comprehend creates the classifier model, the confusion matrix is available in the
`confusion_matrix.json` file in the S3 output location.

The format of the confusion matrix varies, depending on whether you trained your classifier using multi-class mode or multi-label mode.

###### Topics

- [Confusion matrix for multi-class mode](#m-c-matrix "#m-c-matrix")
- [Confusion matrix for multi-label mode](#m-l-matrix "#m-l-matrix")

### Confusion matrix for multi-class mode

In multi-class mode, the individual classes are mutually exclusive, so classification assigns one label to
each document. For example, an animal can be a dog or a cat, but not both at the same time.

Consider the following example of a confusion matrix for a multi-class trained classifier:

```
  A B X Y <-(predicted label)
A 1 2 0 4
B 0 3 0 1
X 0 0 1 0
Y 1 1 1 1
^
|
(actual label)
```

In this case, the model predicted the following:

- One "A" label was accurately predicted, two "A" labels were incorrectly predicted as "B" labels, and four "A"
  labels were incorrectly predicted as "Y" labels.
- Three "B" labels were accurately predicted, and one "B" label was incorrectly predicted as a "Y" label.
- One "X" was accurately predicted.
- One "Y" label was accurately predicted, one was incorrectly predicted as an "A" label, one was incorrectly
  predicted as a "B" label, and one was incorrectly predicted as an "X" label.

The diagonal line in the matrix (A:A, B:B, X:X, and Y:Y) shows the accurate predictions. The prediction
errors are the values outside of the diagonal. In this case, the matrix shows the following prediction error
rates:

- A labels: 86%
- B labels: 25%
- X labels: 0%
- Y labels: 75%

The classifier returns the confusion matrix as a file in JSON format. The following JSON file represents the
matrix for the previous example.

```
{
 "type": "multi_class",
 "confusion_matrix": [
 [1, 2, 0,4],
 [0, 3, 0, 1],
 [0, 0, 1, 0],
 [1, 1, 1, 1]],
 "labels": ["A", "B", "X", "Y"],
 "all_labels": ["A", "B", "X", "Y"]
}
```

### Confusion matrix for multi-label mode

In multi-label mode, classification can assign one or more classes to a document. Consider the following
example of a confusion matrix for a multi-class trained classifier.

In this example, there are three possible labels: `Comedy`, `Action`, and
`Drama`. The multi-label confusion matrix creates one 2x2 matrix for each label.

```
Comedy                   Action                   Drama
     No Yes                   No Yes                   No Yes   <-(predicted label)
 No  2   1                No  1   1                No  3   0
Yes  0   2               Yes  2   1               Yes  1   1
 ^                        ^                        ^
 |                        |                        |
 |-----------(was this label actually used)--------|

```

In this case, the model returned the following for the `Comedy` label:

- Two instances where a `Comedy` label was accurately predicted to be present. True positive
  (TP).
- Two instances where a `Comedy` label was accurately predicted to be absent. True negative
  (TN).
- Zero instances where a `Comedy` label was incorrectly predicted to be present. False positive
  (FP).
- One instance where a `Comedy` label was incorrectly predicted to be absent. False negative
  (FN).

As with a multi-class confusion matrix, the diagonal line in each matrix shows the accurate
predictions.

In this case, the model accurately predicted `Comedy` labels 80% of the time (TP plus TN) and
incorrectly predicted them 20% of the time (FP plus FN).

The classifier returns the confusion matrix as a file in JSON format. The following JSON file represents the
matrix for the previous example.

```
{
"type": "multi_label",
"confusion_matrix": [
 [[2, 1],
 [0, 2]],
 [[1, 1],
 [2, 1]],
 [[3, 0],
 [1, 1]]
],
"labels": ["Comedy", "Action", "Drama"]
"all_labels": ["Comedy", "Action", "Drama"]
}
```

## Additional outputs for native document models

Amazon Comprehend can create additional output files when you train a native document model.

### Amazon Textract output

If Amazon Comprehend invoked the Amazon Textract APIs to extract text for any of the training documents, it saves the
Amazon Textract output files in the S3 output location. It uses the following directory structure:

- **Training documents:**

`amazon-textract-output/train/<file_name>/<page_num>/textract_output.json`

- **Test documents:**

`amazon-textract-output/test/<file_name>/<page_num>/textract_output.json`

Amazon Comprehend populates the test folder if you provided test documents in the API request.

### Document annotation failures

Amazon Comprehend creates the following files in the Amazon S3 output location (in the **skipped_documents/** folder) if there are any failed annotations:

- failed_annotations_train.jsonl

File exists if any annotations failed in the training data.

- failed_annotations_test.jsonl

File exists if the request included test data and any annotations failed in the test data.

The failed annotation files are JSONL files with the following format:

```
{
     "File": "String", "Page": Number, "ErrorCode": "...", "ErrorMessage": "..."}
    {"File": "String", "Page": Number, "ErrorCode": "...", "ErrorMessage": "..."
  }
```
