# Editing a training data configuration file

The Neptune export process exports Neptune ML data from a Neptune DB cluster
into an S3 bucket. It exports nodes and edges separately into a `nodes/`
and an `edges/` folder. It also creates a JSON training data configuration
file, named `training-data-configuration.json` by default. This file contains
information about the schema of the graph, the types of its features, feature transformation
and normalization operations, and the target feature for a classification or regression task.

There might be cases when you want to modify the configuration file directly.
One such case is when you want to change the way features are processed or how the graph
is constructed, without needing to rerun the export every time you want to modify the
specification for the machine learning task you're solving.

###### To edit the training data configuration file

1. **Download the file to your local machine.**

Unless you specified one or more named jobs in the `additionalParams/neptune_ml`
parameter passed to the export process, the file will have the default name, which is
`training-data-configuration.json`. You can use an AWS CLI command like
this to download the file:

```
aws s3 cp \
  s3://`(your Amazon S3 bucket)`/`(path to your export folder)`/training-data-configuration.json \
  ./
```

2. **Edit the file using a text editor.**
3. **Upload the modified file.** Upload the modified file
   back to the same location in Amazon S3 from which you downloaded it, using use an AWS CLI
   command like this:

```
aws s3 cp \
  training-data-configuration.json \
  s3://`(your Amazon S3 bucket)`/`(path to your export folder)`/training-data-configuration.json
```
