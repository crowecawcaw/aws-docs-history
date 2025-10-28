# Multi-label mode

In multi-label mode, individual classes represent different categories that aren't mutually exclusive.
Multi-label classification assigns one or more classes to each document. For example, you can classify one movie as
Documentary, and another movie as Science fiction, Action, and Comedy.

For training, multi-label mode supports up to 1 million examples containing up to 100 unique
classes.

###### Topics

- [Plain-text models](#prep-multi-label-plaintext "#prep-multi-label-plaintext")
- [Native document models](#prep-multi-label-structured "#prep-multi-label-structured")

## Plain-text models

To train a plain-text model, you can provide labeled training data as a CSV file or as an augmented manifest
file from SageMaker AI Ground Truth.

### CSV file

For general information about using CSV files for training classifiers, see
[CSV files](prep-class-data-format.md#prep-data-csv "prep-class-data-format.md#prep-data-csv").

Provide the training data as a two-column CSV file. For each row, the first column contains the class label
values, and the second column contains an example text document for these classes. To enter more than one class
in the first column, use a delimiter (such as a | ) between each class.

```
CLASS,Text of document 1
CLASS,Text of document 2
CLASS|CLASS|CLASS,Text of document 3
```

The following example shows one row of a CSV file that trains a custom classifier to detect genres in
movie abstracts:

```
COMEDY|MYSTERY|SCIENCE_FICTION|TEEN,"A band of misfit teens become unlikely detectives when they discover troubling clues about their high school English teacher. Could the strange Mrs. Doe be an alien from outer space?"
```

The default delimiter between class names is a pipe (|). However, you can use a different character as a
delimiter. The delimiter must be distinct from all characters in your class names. For example, if your classes
are CLASS_1, CLASS_2, and CLASS_3, the underscore (**\_**) is part of the class
name. So don't use an underscore as the delimiter for separating class names.

### Augmented manifest file

For general information about using augmented manifest files for training classifiers, see
[Augmented manifest file](prep-class-data-format.md#prep-data-annotations "prep-class-data-format.md#prep-data-annotations").

For plain-text documents, each line of the augmented manifest file is a complete JSON object. It contains a
training document, class names, and other metadata from Ground Truth. The following example is an augmented manifest
file for training a custom classifier to detect genres in movie abstracts:

```
{"source":"Document 1 text", "MultiLabelJob":[0,4], "MultiLabelJob-metadata":{"job-name":"labeling-job/multilabeljob", "class-map":{"0":"action", "4":"drama"}, "human-annotated":"yes", "creation-date":"2020-05-21T19:02:21.521882", "confidence-map":{"0":0.66}, "type":"groundtruth/text-classification-multilabel"}}
{"source":"Document 2 text", "MultiLabelJob":[3,6], "MultiLabelJob-metadata":{"job-name":"labeling-job/multilabeljob", "class-map":{"3":"comedy", "6":"horror"}, "human-annotated":"yes", "creation-date":"2020-05-21T19:00:01.291202", "confidence-map":{"1":0.61,"0":0.61}, "type":"groundtruth/text-classification-multilabel"}}
{"source":"Document 3 text", "MultiLabelJob":[1], "MultiLabelJob-metadata":{"job-name":"labeling-job/multilabeljob", "class-map":{"1":"action"}, "human-annotated":"yes", "creation-date":"2020-05-21T18:58:51.662050", "confidence-map":{"1":0.68}, "type":"groundtruth/text-classification-multilabel"}}
```

The following example shows one JSON object from the augmented manifest file, formatted for readability:

```
{
      "source": "A band of misfit teens become unlikely detectives when
                   they discover troubling clues about their high school English teacher.
                     Could the strange Mrs. Doe be an alien from outer space?",
      "MultiLabelJob": [
          3,
          8,
          10,
          11
      ],
      "MultiLabelJob-metadata": {
          "job-name": "labeling-job/multilabeljob",
          "class-map": {
              "3": "comedy",
              "8": "mystery",
              "10": "science_fiction",
              "11": "teen"
          },
          "human-annotated": "yes",
          "creation-date": "2020-05-21T19:00:01.291202",
          "confidence-map": {
              "3": 0.95,
              "8": 0.77,
              "10": 0.83,
              "11": 0.92
          },
          "type": "groundtruth/text-classification-multilabel"
      }
  }
```

In this example, the `source` attribute provides the text of the training document, and the
`MultiLabelJob` attribute assigns the indexes of several classes from a classification list. The
job-name in the `MultiLabelJob` metadata is the name that you defined for the labeling job in Ground Truth.

## Native document models

A native document model is a model that you train with native documents (such as PDF, DOCX , and image
files). You provide labeled training data as a CSV file.

### CSV file

For general information about using CSV files for training classifiers, see
[CSV files](prep-class-data-format.md#prep-data-csv "prep-class-data-format.md#prep-data-csv").

Provide the training data as a three-column CSV file. For each row, the first column contains the class
label values. The second column contains the file name of an example document for these classes. The third
column contains the page number. The page number is optional if the example document is an image.

To enter more than one class in the first column, use a delimiter (such as a | ) between each class.

```
CLASS,input-doc-1.pdf,3
CLASS,input-doc-2.docx,1
CLASS|CLASS|CLASS,input-doc-3.png,2
```

The following example shows one row of a CSV file that trains a custom classifier to detect genres in movie
abstracts. Page 2 of the PDF file contains the example of a comedy/teen movie.

```
COMEDY|TEEN,movie-summary-1.pdf,2
```

The default delimiter between class names is a pipe (|). However, you can use a different character as a
delimiter. The delimiter must be distinct from all characters in your class names. For example, if your classes
are CLASS_1, CLASS_2, and CLASS_3, the underscore (**\_**) is part of the class
name. So don't use an underscore as the delimiter for separating class names.
