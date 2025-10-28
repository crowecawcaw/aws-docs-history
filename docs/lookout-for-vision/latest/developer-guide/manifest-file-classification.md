End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Defining JSON lines for

image classification

You define a JSON line for each image that you want to use in an
Amazon Lookout for Vision manifest file. If you want to create a classification model, the
JSON line must include an image classification that is either normal
or an anomaly. A JSON line is in SageMaker AI Ground Truth [Classification Job Output](../../../sagemaker/latest/dg/sms-data-output.md#sms-output-class "../../../sagemaker/latest/dg/sms-data-output.md#sms-output-class") format. A manifest file is made of
one or more JSON lines, one for each image that you want to import.

###### To create a manifest file for classified images

1. Create an empty text file.
2. Add a JSON line for each image the that you want to import. Each
   JSON line should look similar to the following:

```
{"source-ref":"s3://lookoutvision-console-us-east-1-nnnnnnnnnn/gt-job/manifest/IMG_1133.png","anomaly-label":1,"anomaly-label-metadata":{"confidence":0.95,"job-name":"labeling-job/testclconsolebucket","class-name":"normal","human-annotated":"yes","creation-date":"2020-04-15T20:17:23.433061","type":"groundtruth/image-classification"}}

```

3. Save the file.

###### Note

You can use the extension `.manifest`, but
it is not required. 4. Create a dataset using the manifest file that you created. For
more information, see [Creating a manifest file](manifest-files.md "manifest-files.md").

## Classification JSON

lines

In this section, you learn how to create a JSON line that classifies an image as
normal or anomalous.

### Anomaly JSON line

The following JSON line shows an image that is labeled as an
anomaly. Note that the value of `class-name` is
`anomaly`.

```

{
    "source-ref": "s3: //bucket/image/anomaly/abnormal-1.jpg",
    "`anomaly-label`-metadata": {
        "confidence": `1`,
        "job-name": "`labeling-job/auto-label`",
        "class-name": "`anomaly`",
        "human-annotated": "`yes`",
        "creation-date": "`2020-11-10T03:37:09.600`",
        "type": "groundtruth/image-classification"
    },
    "`anomaly-label`": `1`
}


```

### Normal JSON line

The following JSON line shows an image labeled as normal. Note
that the value of `class-name` is
`normal`.

```
{
    "source-ref": "s3: //bucket/image/normal/2020-10-20_12-14-55_613.jpeg",
    "`anomaly-label`-metadata": {
        "confidence": `1`,
        "job-name": "`labeling-job/auto-label`",
        "class-name": "`normal`",
        "human-annotated": "`yes`",
        "creation-date": "`2020-11-10T03:37:09.603`",
        "type": "groundtruth/image-classification"
    },
    "`anomaly-label`": 0
}
```

## JSON line keys and values

The following information describes the keys and values in an
Amazon Lookout for Vision JSON line.

### source-ref

(Required) The Amazon S3 location of the image. The format is
`"s3://`BUCKET`/`OBJECT_PATH`"`.
Images in an imported dataset must be stored in the same Amazon S3
bucket.

### anomaly-label

(Required) The label attribute. Use the key
`anomaly-label`, or another key name that you choose.
The key value (`0` in the preceding example) is required
by Amazon Lookout for Vision, but it isn't used. The output manifest created by
Amazon Lookout for Vision converts the value to `1` for an anomalous
image and a value of `0` for a normal image. The value of
`class-name` determines if the image is normal or
anomalous.

There must be corresponding metadata identified by the field name
with _-metadata_ appended. For example,
`"anomaly-label-metadata"`.

### anomaly-label-metadata

(Required) Metadata about the label attribute. The field name must
be the same as the label attribute with
_-metadata_ appended.

_confidence_

(Optional) Currently not used by Amazon Lookout for Vision. If you do
specify a value, use a value of `1`.

_job-name_

(Optional) A name that you choose for the job that
processes the image.

_class-name_

(Required) If the image contains normal content,
specify `normal`, otherwise specify
`anomaly`. If the value of
`class-name` is any other value, the
image is added to the dataset as an unlabeled image. To
label an image, see [Adding images to your dataset](edit-dataset.md "edit-dataset.md").

_human-annotated_

(Required) Specify `"yes"`, if the
annotation was completed by a human. Otherwise, specify
`"no"`.

_creation-date_

(Optional) The Coordinated Universal Time (UTC) date
and time that the label was created.

_type_

(Required) The type of processing that should be
applied to the image. For image-level anomaly labels,
the value is
`"groundtruth/image-classification"`.
