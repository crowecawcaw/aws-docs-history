# Augmented Manifest Files for Training Jobs

To include metadata with your dataset in a training job, use an augmented manifest file.
When using an augmented manifest file, your dataset must be stored in Amazon Simple Storage Service (Amazon S3), and
you must configure your training job to use the dataset stored there. You specify the
location and format of this dataset for one or more [`Channel`](../APIReference/API_Channel.md "../APIReference/API_Channel.md"). Augmented manifests can only support Pipe input mode. See
the section, **InputMode** in [`Channel`](../APIReference/API_Channel.md "../APIReference/API_Channel.md") to learn more about pipe input mode.

When specifying a channel's parameters, you specify a path to the file, called a
`S3Uri`. Amazon SageMaker AI interprets this URI based on the specified
`S3DataType` in [`S3DataSource`](../APIReference/API_S3DataSource.md "../APIReference/API_S3DataSource.md"). The `AugmentedManifestFile` option defines
a manifest format that includes metadata with the input data. Using an augmented manifest
file is an alternative to preprocessing when you have labeled data. For training jobs using
labeled data, you typically need to preprocess the dataset to combine input data with
metadata before training. If your training dataset is large, preprocessing can be time
consuming and expensive.

## Augmented Manifest File Format

An augmented manifest file must be formatted in [JSON Lines](http://jsonlines.org/ "http://jsonlines.org/") format. In JSON Lines format, each line in the file is a
complete JSON object followed by a newline separator.

During training, SageMaker AI parses each JSON line and sends some or all of its attributes on
to the training algorithm. You specify which attribute contents to pass and the order in
which to pass them with the `AttributeNames` parameter of the [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") API. The `AttributeNames`
parameter is an ordered list of attribute names that SageMaker AI looks for in the JSON object
to use as training input.

For example, if you list `["line", "book"]` for
`AttributeNames`, the input data must include the attribute names of
`line` and `book` in the specified order. For this example,
the following augmented manifest file content is valid:

```
{"author": "Herman Melville", "line": "Call me Ishmael", "book": "Moby Dick"}
{"line": "It was love at first sight.", "author": "Joseph Heller", "book": "Catch-22"}
```

SageMaker AI ignores unlisted attribute names even if they precede, follow, or are in between
listed attributes.

When using augmented manifest files, observe the following guidelines:

- The order of the attributes listed in the `AttributeNames`
  parameter determines the order of the attributes passed to the algorithm in the
  training job.
- The listed `AttributeNames` can be a subset of all of the
  attributes in the JSON line. SageMaker AI ignores unlisted attributes in the
  file.
- You can specify any type of data allowed by the JSON format in
  `AttributeNames`, including text, numerical, data arrays, or
  objects.
- To include an S3 URI as an attribute name, add the suffix `-ref` to
  it.

If an attribute name contains the suffix `-ref`, the attribute's value must
be an S3 URI to a data file that is accessible to the training job. For example, if
`AttributeNames` contains `["image-ref", "is-a-cat"]`, the
following example shows a valid augmented manifest file:

```
{"image-ref": "s3://amzn-s3-demo-bucket/sample01/image1.jpg", "is-a-cat": 1}
{"image-ref": "s3://amzn-s3-demo-bucket/sample02/image2.jpg", "is-a-cat": 0}
```

In case of the first JSON line of this manifest file, SageMaker AI retrieves the
`image1.jpg` file from `s3://amzn-s3-demo-bucket/sample01/` and the
string representation of the `is-a-cat` attribute `"1"` for image
classification.

###### Tip

To create an augmented manifest file, use Amazon SageMaker Ground Truth and create a labeling job. For
more information about the output from a labeling job, see [Labeling job output data](sms-data-output.md "sms-data-output.md").

## Use an Augmented Manifest File

The following sections show you how to use augmented manifest files in your
Amazon SageMaker training jobs, either with the SageMaker AI console or programmatically using the
SageMaker Python SDK.

### Use an Augmented Manifest File

(Console)

To complete this procedure, you need:

- The URL of the S3 bucket where you've stored the augmented manifest
  file.
- To store the data that is listed in the augmented manifest file in an S3
  bucket.
- The URL of the S3 bucket where you want to store the output of the job.

###### To use an augmented manifest file in a training job (console)

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the navigation pane, choose **Training**, then choose
   **Training jobs**.
3. Choose **Create training job**.
4. Provide a name for the training job. The name must be unique within an AWS
   Region in an AWS account. It can have 1 to 63 characters. Valid characters:
   a-z, A-Z, 0-9, and . : + = @ \_ % - (hyphen).
5. Choose the algorithm that you want to use. For information about supported
   built-in algorithms, see [Built-in algorithms and pretrained models in Amazon SageMaker](algos.md "algos.md"). If you
   want to use a custom algorithm, make sure that it is compatible with Pipe
   mode.
6. (Optional) For **Resource configuration**, either accept the
   default values or, to reduce computation time, increase the resource
   consumption.
   1. (Optional) For **Instance type**, choose the ML
      compute instance type that you want to use. In most cases,
      **ml.m4.xlarge** is sufficient.
   2. For **Instance count**, use the default,
      `1`.
   3. (Optional) For **Additional volume per instance
      (GB)**, choose the size of the ML storage volume that you
      want to provision. In most cases, you can use the default,
      `1`. If you are using a large dataset, use a larger
      size.

7. Provide information about the input data for the training dataset.
   1. For **Channel name**, either accept the default
      (`train`) or enter a more meaningful name, such
      as `training-augmented-manifest-file`.
   2. For **InputMode**, choose
      **Pipe**.
   3. For **S3 data distribution type**, choose
      **FullyReplicated**. When training incrementally,
      fully replicating causes each ML compute instance to use a complete copy
      of the expanded dataset. For neural-based algorithms, such as [Neural Topic Model (NTM) Algorithm](ntm.md "ntm.md"), choose
      `ShardedByS3Key`.
   4. If the data specified in the augmented manifest file is uncompressed,
      set the **Compression type** to
      **None**. If the data is compressed using gzip, set
      it to **Gzip**.
   5. (Optional) For **Content type**, specify the
      appropriate MIME type. Content type is the multipurpose internet mail
      extension (MIME) type of the data.
   6. For **Record wrapper**, if the dataset specified in
      the augmented manifest file is saved in RecordIO format, choose
      **RecordIO**. If your dataset is not saved as a
      RecordIO-formatted file, choose **None**.
   7. For **S3 data type**, choose
      **AugmentedManifestFile**.
   8. For **S3 location**, provide the path to the bucket
      where you stored the augmented manifest file.
   9. For **AugmentedManifestFile attribute names**,
      specify the name of an attribute that you want to use. The attribute
      name must be present within the augmented manifest file, and is
      case-sensitive.
   10. (Optional) To add more attribute names, choose **Add
       row** and specify another attribute name for each
       attribute.
   11. (Optional) To adjust the order of attribute names, choose the up or
       down buttons next to the names. When using an augmented manifest file,
       the order of the specified attribute names is important.
   12. Choose **Done**.

8. For **Output data configuration**, provide the following
   information:
   1. For **S3 location**, type the path to the S3 bucket
      where you want to store the output data.
   2. (Optional) You can use your AWS Key Management Service (AWS KMS) encryption key to
      encrypt the output data at rest. For **Encryption
      key**, provide the key ID or its Amazon Resource Number (ARN).
      For more information, see [KMS-Managed Encryption Keys](../../../AmazonS3/latest/dev/UsingKMSEncryption.md "../../../AmazonS3/latest/dev/UsingKMSEncryption.md").

9. (Optional) For **Tags**, add one or more tags to the training
   job. A _tag_ is metadata that you can define and assign to
   AWS resources. In this case, you can use tags to help you manage your training
   jobs. A tag consists of a key and a value, which you define. For example, you
   might want to create a tag with `Project` as a key and a
   value that refers to a project that is related to the training job, such as
   `Home value forecasts`.
10. Choose **Create training job**. SageMaker AI creates and runs the
    training job.

After the training job has finished, SageMaker AI stores the model artifacts in the bucket
whose path you provided for **S3 output path** in the **Output
data configuration** field. To deploy the model to get predictions, see
[Deploy the model to Amazon EC2](ex1-model-deployment.md "ex1-model-deployment.md").

### Use an Augmented Manifest File

(API)

The following shows how to train a model with an augmented manifest
file
using the SageMaker AI high-level Python library:

```
import sagemaker

# Create a model object set to using "Pipe" mode.
model = sagemaker.estimator.Estimator(
    `training_image`,
    role,
    instance_count=1,
    instance_type='ml.p3.2xlarge',
    volume_size = 50,
    max_run = 360000,
    input_mode = 'Pipe',
    output_path=`s3_output_location`,
    sagemaker_session=`session`
)

# Create a train data channel with S3_data_type as 'AugmentedManifestFile' and attribute names.
train_data = sagemaker.inputs.TrainingInput(
    `your_augmented_manifest_file`,
    distribution='FullyReplicated',
    content_type='application/x-recordio',
    s3_data_type='AugmentedManifestFile',
    attribute_names=[`'source-ref'`, `'annotations'`],
    input_mode='Pipe',
    record_wrapping='RecordIO'
)

data_channels = {'train': train_data}

# Train a model.
model.fit(inputs=data_channels, logs=True)
```

After the training job has finished, SageMaker AI stores the model artifacts in the bucket
whose path you provided for **S3 output path** in the **Output
data configuration** field. To deploy the model to get predictions, see
[Deploy the model to Amazon EC2](ex1-model-deployment.md "ex1-model-deployment.md").
