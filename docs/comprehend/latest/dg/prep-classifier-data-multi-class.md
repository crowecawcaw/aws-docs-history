# Multi-class mode

In multi-class mode, classification assigns one class for each document. The individual classes are mutually
exclusive. For example, you can classify a movie as comedy or science fiction, but not both.

###### Note

The Amazon Comprehend console refers to multi-class mode as single-label mode.

###### Topics

- [Plain-text models](#prep-multi-class-plaintext "#prep-multi-class-plaintext")
- [Native document models](#prep-multi-class-structured "#prep-multi-class-structured")

## Plain-text models

To train a plain-text model, you can provide labeled training data as a CSV file or as an augmented manifest
file from SageMaker AI Ground Truth.

### CSV file

For general information about using CSV files for training classifiers, see
[CSV files](prep-class-data-format.md#prep-data-csv "prep-class-data-format.md#prep-data-csv").

Provide the training data as a two-column CSV file. For each row, the first column contains the class
label value. The second column contains an example text document for that class. Each row must end with \n or \r\n characters.

The following example shows a CSV file containing three documents.

```
CLASS,Text of document 1
CLASS,Text of document 2
CLASS,Text of document 3
```

The following example shows one row of a CSV file that trains a custom classifier to detect whether an
email message is spam:

```
SPAM,"Paulo, your $1000 award is waiting for you! Claim it while you still can at http://example.com."
```

### Augmented manifest file

For general information about using augmented manifest files for training classifiers, see
[Augmented manifest file](prep-class-data-format.md#prep-data-annotations "prep-class-data-format.md#prep-data-annotations").

For plain-text documents, each line of the augmented manifest file is a complete JSON object that contains
a training document, a single class name, and other metadata from Ground Truth. The following example is an augmented
manifest file for training a custom classifier to recognize spam email messages:

```
{"source":"Document 1 text", "MultiClassJob":0, "MultiClassJob-metadata":{"confidence":0.62, "job-name":"labeling-job/multiclassjob", "class-name":"not_spam", "human-annotated":"yes", "creation-date":"2020-05-21T17:36:45.814354", "type":"groundtruth/text-classification"}}
{"source":"Document 2 text", "MultiClassJob":1, "MultiClassJob-metadata":{"confidence":0.81, "job-name":"labeling-job/multiclassjob", "class-name":"spam", "human-annotated":"yes", "creation-date":"2020-05-21T17:37:51.970530", "type":"groundtruth/text-classification"}}
{"source":"Document 3 text", "MultiClassJob":1, "MultiClassJob-metadata":{"confidence":0.81, "job-name":"labeling-job/multiclassjob", "class-name":"spam", "human-annotated":"yes", "creation-date":"2020-05-21T17:37:51.970566", "type":"groundtruth/text-classification"}}
```

The following example shows one JSON object from the augmented manifest file, formatted for readability:

```
{
   "source": "Paulo, your $1000 award is waiting for you! Claim it while you still can at http://example.com.",
   "MultiClassJob": 0,
   "MultiClassJob-metadata": {
       "confidence": 0.98,
       "job-name": "labeling-job/multiclassjob",
       "class-name": "spam",
       "human-annotated": "yes",
       "creation-date": "2020-05-21T17:36:45.814354",
       "type": "groundtruth/text-classification"
   }
}
```

In this example, the `source` attribute provides the text of the training document, and the
`MultiClassJob` attribute assigns the index of a class from a classification list. The
`job-name` attribute is the name that you defined for the labeling job in Ground Truth.

When you start the classifier training job in Amazon Comprehend, you specify the same labeling job name.

## Native document models

A native document model is a model that you train with native documents (such as PDF, DOCX , and images). You
provide the training data as a CSV file.

### CSV file

For general information about using CSV files for training classifiers, see
[CSV files](prep-class-data-format.md#prep-data-csv "prep-class-data-format.md#prep-data-csv").

Provide the training data as a three-column CSV file. For each row, the first column contains the class
label value. The second column contains the file name of an example document for this class. The third column
contains the page number. The page number is optional if the example document is an image.

The following example shows a CSV file that references three input documents.

```
CLASS,input-doc-1.pdf,3
CLASS,input-doc-2.docx,1
CLASS,input-doc-3.png
```

The following example shows one row of a CSV file that trains a custom classifier to detect whether an email
message is spam. Page 2 of the PDF file contains the spam example.

```
SPAM,email-content-3.pdf,2
```
