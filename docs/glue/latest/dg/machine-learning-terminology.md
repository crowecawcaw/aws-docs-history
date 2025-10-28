# Machine learning measurements

To understand the measurements that are used to tune your machine learning transform, you
should be familiar with the following terminology:

**True positive (TP)**

A match in the data that the transform correctly found, sometimes called a
_hit_.

**True negative (TN)**

A nonmatch in the data that the transform correctly rejected.

**False positive (FP)**

A nonmatch in the data that the transform incorrectly classified as a match, sometimes
called a _false alarm_.

**False negative (FN)**

A match in the data that the transform didn't find, sometimes called a
_miss_.

For more information about the terminology that is used in machine learning, see [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix "https://en.wikipedia.org/wiki/Confusion_matrix") in
Wikipedia.

To tune your machine learning transforms, you can change the value of the following
measurements in the **Advanced properties** of the transform.

- **Precision** measures how well the transform finds true positives
  among the total number of records that it identifies as positive (true positives and false
  positives). For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall") in
  Wikipedia.
- **Recall** measures how well the transform finds true positives from
  the total records in the source data. For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall") in
  Wikipedia.
- **Accuracy** measures how well the transform finds true positives and
  true negatives. Increasing accuracy requires more machine resources and cost. But it also
  results in increased recall. For more information, see [Accuracy
  and precision](https://en.wikipedia.org/wiki/Accuracy_and_precision#In_information_systems "https://en.wikipedia.org/wiki/Accuracy_and_precision#In_information_systems") in Wikipedia.
- **Cost** measures how many compute resources (and thus money) are
  consumed to run the transform.
