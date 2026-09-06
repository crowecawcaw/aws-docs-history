

# Managing annotations
<a name="annotations-managing"></a>

You can add, retrieve, and delete annotations on your Amazon S3 objects using the AWS Management Console, AWS CLI, or AWS SDKs. The following sections describe how to perform each operation.

## Adding or updating an annotation
<a name="annotations-managing-add"></a>

You can add a new annotation to an object or update an existing annotation by replacing its payload.

### Using the S3 console
<a name="annotations-managing-add-console"></a>

**To add an annotation to an object**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Buckets** list, choose the name of the bucket that contains the object.

1. In the **Objects** list, choose the name of the object that you want to annotate.

1. Choose the **Properties** tab.

1. Scroll to the **Annotations** section and choose **Add annotation**.

1. For **Name**, enter a name for the annotation (for example, `ml.sentiment`). Names must be 1–512 bytes and can contain Unicode letters, digits, underscores, periods, and hyphens. Names cannot start with `aws` or `s3`.

1. Choose **Choose file** to upload the annotation content. The file must be UTF-8 encodable and up to 1 MB in size.

**To complete the annotation**

1. (Optional) Under **Checksums**, choose a checksum algorithm.

1. Choose **Add annotation**.

**Note**  
To view the content of an annotation after it is created, you must download the annotation. The S3 console does not display annotation content inline.

### Using the AWS CLI
<a name="annotations-managing-add-cli"></a>

To add or update an annotation on an object, use the `put-object-annotation` command. The `--annotation-payload` parameter accepts a file path.

```
aws s3api put-object-annotation \
    --bucket amzn-s3-demo-bucket \
    --key myDocument.pdf \
    --annotation-name "ml.sentiment" \
    --annotation-payload /tmp/sentiment.json
```

To write the annotation only if the object has not been overwritten since you last read it, specify the `--object-if-match` parameter with the object's current ETag.

```
aws s3api put-object-annotation \
    --bucket amzn-s3-demo-bucket \
    --key myDocument.pdf \
    --annotation-name "ml.sentiment" \
    --annotation-payload /tmp/sentiment.json \
    --object-if-match "\"d6eb32081c822ed572b70567826d9d9d\""
```

### Using the AWS SDKs
<a name="annotations-managing-add-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to add an annotation to an object.

```
import boto3
import json

s3 = boto3.client('s3')

s3.put_object_annotation(
    Bucket='amzn-s3-demo-bucket',
    Key='myDocument.pdf',
    AnnotationName='ml.sentiment',
    AnnotationPayload=json.dumps({
        'score': 0.95,
        'label': 'positive',
        'model': 'sentiment-v3'
    }).encode('utf-8')
)
```

## Retrieving annotations
<a name="annotations-managing-get"></a>

You can retrieve a specific annotation or list all annotations on an object.

### Using the S3 console
<a name="annotations-managing-get-console"></a>

**To retrieve an annotation**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Buckets** list, choose the name of the bucket that contains the object.

1. In the **Objects** list, choose the name of the object.

1. Choose the **Properties** tab and scroll to the **Annotations** section.

1. To view annotation content, choose **Download** next to the annotation name.

### Using the AWS CLI
<a name="annotations-managing-get-cli"></a>

To retrieve a specific annotation, use the `get-object-annotation` command.

```
aws s3api get-object-annotation \
    --bucket amzn-s3-demo-bucket \
    --key myDocument.pdf \
    --annotation-name "ml.sentiment" \
    output.json
```

To list all annotations on an object, use the `list-object-annotations` command.

```
aws s3api list-object-annotations \
    --bucket amzn-s3-demo-bucket \
    --key myDocument.pdf
```

### Using the AWS SDKs
<a name="annotations-managing-get-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to retrieve and list annotations.

```
import boto3
import json

s3 = boto3.client('s3')

# Retrieve a specific annotation
response = s3.get_object_annotation(
    Bucket='amzn-s3-demo-bucket',
    Key='myDocument.pdf',
    AnnotationName='ml.sentiment'
)
content = json.loads(response['AnnotationPayload'].read())

# List all annotations on an object
response = s3.list_object_annotations(
    Bucket='amzn-s3-demo-bucket',
    Key='myDocument.pdf'
)
for annotation in response['Annotations']:
    print(f"{annotation['AnnotationName']} - {annotation['Size']} bytes")
```

## Deleting annotations
<a name="annotations-managing-delete"></a>

You can delete a specific annotation from an object. Annotation deletion is permanent and cannot be undone.

### Using the S3 console
<a name="annotations-managing-delete-console"></a>

**To delete an annotation**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the **Buckets** list, choose the name of the bucket that contains the object.

1. In the **Objects** list, choose the name of the object.

1. Choose the **Properties** tab and scroll to the **Annotations** section.

1. Select the annotation that you want to delete.

1. Choose **Delete**, then confirm the deletion.

### Using the AWS CLI
<a name="annotations-managing-delete-cli"></a>

To delete a specific annotation, use the `delete-object-annotation` command.

```
aws s3api delete-object-annotation \
    --bucket amzn-s3-demo-bucket \
    --key myDocument.pdf \
    --annotation-name "ml.sentiment"
```

### Using the AWS SDKs
<a name="annotations-managing-delete-sdk"></a>

The following example uses the AWS SDK for Python (Boto3) to delete an annotation.

```
import boto3

s3 = boto3.client('s3')

s3.delete_object_annotation(
    Bucket='amzn-s3-demo-bucket',
    Key='myDocument.pdf',
    AnnotationName='ml.sentiment'
)
```