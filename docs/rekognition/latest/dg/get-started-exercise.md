# Step 3: Getting started using the AWS CLI and AWS

SDK API

After you've set up the AWS CLI and AWS SDKs that you want to use, you can build
applications that use Amazon Rekognition. Most interactions with Amazon Rekognition happen by using the
API operations, although a select few Amazon Rekognition's features have console
workflows.

The following topics show you how to get started with Amazon Rekognition Image and Amazon Rekognition Video via the
AWS CLI or the AWS SDKs.

- [Working with images](images.md "images.md") – Covers the process of
  analyzing images with Amazon Rekognition Image.
- [Working with stored video analysis operations](video.md "video.md") - Covers the process of
  analyzing stored, non-streaming video with Amazon Rekognition Video.
- [Working with streaming video events](streaming-video.md "streaming-video.md") - Covers the
  process of analyzing streaming video with Amazon Rekognition Video.
  The sections listed above have examples which use the AWS CLI. If you intend to use the AWS CLI, see the
  following section for information on how to format your API calls.

## Formatting the AWS CLI examples

The AWS CLI examples in this guide are formatted for the Linux operating system. To
use the samples with Microsoft Windows, you need to change the JSON formatting of
the `--image` parameter, and change the line breaks from backslashes (\)
to carets (^). For more information about JSON formatting, see [Specifying Parameter Values for the AWS
Command Line Interface](../../../cli/latest/userguide/cli-using-param.md "../../../cli/latest/userguide/cli-using-param.md").

The following is an example AWS CLI command that's formatted for Microsoft Windows
(note that these commands will not run as is, they are just formatting
examples):

```
aws rekognition detect-labels ^
  --image "{\"S3Object\":{\"Bucket\":\"`photo-collection`\",\"Name\":\"`photo`.jpg\"}}" ^
  --region `region-name`
```

You can also provide a shorthand version of the JSON that works on both Microsoft
Windows and Linux.

```
aws rekognition detect-labels --image "S3Object={Bucket=`photo-collection`,Name=`photo`.jpg}" --region `region-name`
```

For more information, see [Using
Shorthand Syntax with the AWS Command Line Interface](../../../cli/latest/userguide/shorthand-syntax.md "../../../cli/latest/userguide/shorthand-syntax.md").

## Next step

[Step 4: Getting started using the Amazon Rekognition console](getting-started-console.md "getting-started-console.md")
