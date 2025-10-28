# Terminal manifest file errors

This topic describes the [List of terminal manifest file
errors](tm-debugging.md#tm-error-category-terminal "tm-debugging.md#tm-error-category-terminal").
Manifest file errors do not have an associated error code. The validation results manifests are not created when
a terminal manifest file error occurs.
For more information, see [Understanding the manifest summary](tm-debugging-summary.md "tm-debugging-summary.md").
Terminal manifest errors prevent the reporting of [Non-Terminal JSON Line Validation Errors](tm-debugging-json-line-errors.md "tm-debugging-json-line-errors.md").

## The manifest file extension or contents are invalid.

The training or testing manifest file doesn't have a file extension or its contents are invalid.

###### To fix error _The manifest file extension or contents are invalid._

- Check the following possible causes in both the training and testing manifest files.
  - The manifest file is missing a file extension. By convention the file
    extension is `.manifest`.
  - The Amazon S3 bucket or key for the manifest file couldn't be found.

## The manifest file is empty.

The training or testing manifest file used for training exists, but it is empty.
The manifest file needs a JSON Line for each image that you use for training and testing.

###### To fix error _The manifest file is empty._

1. Check which of the training or testing manifests are empty.
2. Add JSON Lines to the empty manifest file. For more information, see
   [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md"). Alternatively, create
   a new dataset with the console. For more information, see [Creating training and test datasets with images](md-create-dataset.md "md-create-dataset.md").

## The manifest file size exceeds the maximum supported size.

The training or testing manifest file size (in bytes) is too large. For more information, see [Guidelines and quotas in Amazon Rekognition Custom Labels](limits.md "limits.md").
A manifest file can have less than the maximum number of JSON Lines and still exceed the maximum file size.

You can't use the Amazon Rekognition Custom Labels console to fix error _The manifest file size exceeds the maximum supported size_.

###### To fix error _The manifest file size exceeds the maximum supported size._

1. Check which of the training and testing manifests exceed the maximum file size.
2. Reduce the number of JSON Lines in the manifest files that are too large.
   For more information, see [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md").

## The S3 bucket permissions are incorrect.

Amazon Rekognition Custom Labels doesn't have permissions to one or more of the buckets containing the training and testing manifest files.

You can't use the Amazon Rekognition Custom Labels console to fix this error.

###### To fix error _The S3 bucket permissions are incorrect._

- Check the permissions for the bucket(s) containing the training and testing manifests.

For more information, see [Step 2: Set up Amazon Rekognition Custom Labels console permissions](su-console-policy.md "su-console-policy.md").

## Unable to write to output S3 bucket.

The service is unable to generate the training output files.

###### To fix error _Unable to write to output S3 bucket._

- Check that the Amazon S3 bucket information in the
  [OutputConfig](../APIReference/API_OutputConfig.md "../APIReference/API_OutputConfig.md") input parameter to [CreateProjectVersion](../APIReference/API_CreateProjectVersion.md "../APIReference/API_CreateProjectVersion.md") is correct.

You can't use the Amazon Rekognition Custom Labels console to fix this error.
