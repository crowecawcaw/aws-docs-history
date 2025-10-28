# Classifier training file formats

For a plain-text model, you can provide classifier training data as a CSV file or as an augmented manifest file
that you create using SageMaker AI Ground Truth. The CSV file or augmented manifest file includes the text for each training
document, and its associated labels.

For a native document model, you provide Classifier training data as a CSV file. The CSV file includes the file
name for each training document, and its associated labels. You include the training documents in the Amazon S3 input
folder for the training job.

## CSV files

You provide labeled training data as UTF-8 encoded text in a CSV file. Don't include a header row. Adding a
header row in your file may cause runtime errors.

For each row in the CSV file, the first column contains one or more class labels, A class label can be any
valid UTF-8 string. We recommend using clear class names that don't overlap in meaning. The name can include white
space, and can consist of multiple words connected by underscores or hyphens.

Do not leave any space characters before or after the commas that separate the values in a row.

The exact content of the CSV file depends on the classifier mode and the type of training data. For details,
see the sections on [Multi-class mode](prep-classifier-data-multi-class.md "prep-classifier-data-multi-class.md") and [Multi-label mode](prep-classifier-data-multi-label.md "prep-classifier-data-multi-label.md").

## Augmented manifest file

An augmented manifest file is a labeled dataset that you create using SageMaker AI Ground Truth. Ground Truth is a data labeling
service that helps you—or a workforce that you employ—to build training datasets for machine learning models.

For more information about Ground Truth and the output that it produces, see [Use SageMaker AI Ground Truth to Label Data](../../../sagemaker/latest/dg/sms.md "../../../sagemaker/latest/dg/sms.md") in the _Amazon SageMaker AI Developer Guide_.

Augmented manifest files are in JSON lines format. In these files, each line is a complete JSON object that
contains a training document and its associated labels. The exact content of each line depends on the classifier
mode. For details, see the sections on [Multi-class mode](prep-classifier-data-multi-class.md "prep-classifier-data-multi-class.md") and [Multi-label mode](prep-classifier-data-multi-label.md "prep-classifier-data-multi-label.md").

When you provide your training data to Amazon Comprehend, you specify one or more label attribute names. How many
attribute names you specify depends on whether your augmented manifest file is the output of a single labeling job
or a chained labeling job.

If your file is the output of a single labeling job, specify the single label attribute
name from the Ground Truth job.

If your file is the output of a chained labeling job, specify the label attribute name for
one or more jobs in the chain. Each label attribute name provides the annotations from an
individual job. You can specify up to 5 of these attributes for augmented manifest files from
chained labeling jobs.

For more information about chained labeling jobs, and for examples of the output that they
produce, see [Chaining Labeling Jobs](../../../sagemaker/latest/dg/sms-reusing-data.md "../../../sagemaker/latest/dg/sms-reusing-data.md") in the Amazon SageMaker AI Developer Guide.
