# Augmented Manifest File Format for Pipe Mode Training

Augmented manifest format enables you to do training in Pipe mode using files without
needing to create RecordIO files. You need to specify both train and validation channels
as values for the `InputDataConfig` parameter of the [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") request. Augmented manifest files are
supported only for channels using Pipe input mode. For each channel, the data is
extracted from its augmented manifest file and streamed (in order) to the algorithm
through the channel's named pipe. Pipe mode uses the first in first out (FIFO) method,
so records are processed in the order in which they are queued. For information about
Pipe input mode, see [`Input Mode`](../APIReference/API_Channel.md#SageMaker-Type-Channel-InputMode "../APIReference/API_Channel.md#SageMaker-Type-Channel-InputMode").

Attribute names with a `"-ref"` suffix point to preformatted binary data.
In some cases, the algorithm knows how to parse the data. In other cases, you might need
to wrap the data so that records are delimited for the algorithm. If the algorithm is
compatible with [RecordIO-formatted data](https://mxnet.apache.org/api/architecture/note_data_loading#data-format "https://mxnet.apache.org/api/architecture/note_data_loading#data-format"), specifying `RecordIO` for
`RecordWrapperType` solves this issue. If the algorithm is not compatible
with `RecordIO` format, specify `None` for
`RecordWrapperType` and make sure that your data is parsed correctly for
your algorithm.

Using the `["image-ref", "is-a-cat"]` example, if you use RecordIO
wrapping, the following stream of data is sent to the queue:

`recordio_formatted(s3://amzn-s3-demo-bucket/foo/image1.jpg)recordio_formatted("1")recordio_formatted(s3://amzn-s3-demo-bucket/bar/image2.jpg)recordio_formatted("0")`

Images that are not wrapped with RecordIO format, are streamed with the corresponding
`is-a-cat` attribute value as one record. This can cause a problem
because the algorithm might not delimit the images and attributes correctly. For more
information about using augmented manifest files for image classification, see [Train with Augmented Manifest Image Format](image-classification.md#IC-augmented-manifest-training "image-classification.md#IC-augmented-manifest-training").

With augmented manifest files and Pipe mode in general, size limits of the EBS volume
do not apply. This includes settings that otherwise must be within the EBS volume size
limit such as [`S3DataDistributionType`](../APIReference/API_S3DataSource.md#SageMaker-Type-S3DataSource-S3DataDistributionType "../APIReference/API_S3DataSource.md#SageMaker-Type-S3DataSource-S3DataDistributionType") . For more information about Pipe mode
and how to use it, see [Using Your Own Training Algorithms - Input Data
Configuration](your-algorithms-training-algo.md#your-algorithms-training-algo-running-container-inputdataconfig "your-algorithms-training-algo.md#your-algorithms-training-algo-running-container-inputdataconfig").
