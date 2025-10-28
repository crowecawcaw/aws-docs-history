# Real-time analysis for custom classification (API)

You can use the Amazon Comprehend API to run real-time classification with a custom model. First, you create an endpoint to run the real-time analysis.
After you create the endpoint, you run the real-time classification.

The examples in this section use command formats for Unix, Linux, and macOS. For Windows, replace the backslash
(\) Unix continuation character at the end of each line with a caret (^).

For information about provisioning endpoint throughput, and the associated costs, see
[Using Amazon Comprehend endpoints](using-endpoints.md "using-endpoints.md").

###### Topics

- [Creating an endpoint for custom classification](#create-endpoint-api "#create-endpoint-api")
- [Running real-time custom classification](#cc-real-time-analysis-api "#cc-real-time-analysis-api")

## Creating an endpoint for custom classification

The following example shows the [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") API operation using the AWS CLI.

```
aws comprehend create-endpoint \
    --desired-inference-units `number of inference units` \
    --endpoint-name `endpoint name` \
    --model-arn arn:aws:comprehend:`region`:`account-id`:model/`example` \
    --tags Key=`My1stTag`,Value=`Value1`

```

Amazon Comprehend responds with the following:

```
{
   "EndpointArn": "`Arn`"
}

```

## Running real-time custom classification

After you create an endpoint for your custom classification model, you use the endpoint to run
the [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md") API operation. You can provide text input using the `text`
or `bytes` parameter. Enter the other input types using the `bytes` parameter.

For image files and PDF files, you can use the `DocumentReaderConfig` parameter to override the default text extraction actions.
For details, see [Setting text extraction options](idp-set-textract-options.md "idp-set-textract-options.md")

For best results, match the type of input to the classifier model type. The API response includes a warning
if you submit a native document to a plain-text model, or a plain-text file to a native document model.
For more information, see [Training classification models](training-classifier-model.md "training-classifier-model.md").

### Using the AWS Command Line Interface

The following examples demonstrate how to use the _classify-document_ CLI command.

#### Classify text using the AWS CLI

The following example runs real-time classification on a block of text.

```
aws comprehend classify-document \
     --endpoint-arn arn:aws:comprehend:`region`:`account-id`:endpoint/`endpoint name` \
     --text 'From the Tuesday, April 16th, 1912 edition of The Guardian newspaper: The maiden voyage of the White Star liner Titanic,
     the largest ship ever launched ended in disaster. The Titanic started her trip from Southampton for New York on Wednesday. Late
     on Sunday night she struck an iceberg off the Grand Banks of Newfoundland. By wireless telegraphy she sent out signals of distress,
     and several liners were near enough to catch and respond to the call.'

```

Amazon Comprehend responds with the following:

```
{
    "Classes": [
       {
          "Name": "string",
          "Score": 0.9793661236763
       }
    ]
 }
```

#### Classify a semi-structured document using the AWS CLI

To analyze custom classification for a PDF, Word, or image file, run the `classify-document`
command with the input file in the `bytes` parameter.

The following example uses an image as the input file. It uses the `fileb` option to base-64 encode the
image file bytes. For more information, see [Binary large
objects](../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-blob "../../../cli/latest/userguide/cli-usage-parameters-types.md#parameter-type-blob") in the AWS Command Line Interface User Guide.

This example also passes in a JSON file named `config.json` to set the text extraction
options.

```
`$` `aws comprehend classify-document \`
`>` `--endpoint-arn` `arn` `\`
`>` `--language-code` `en` `\`
`>` `--bytes` fileb://image1.jpg   `\`
`>` `--document-reader-config file://config.json`

```

The **config.json** file contains the following content.

```

 {
    "DocumentReadMode": "FORCE_DOCUMENT_READ_ACTION",
    "DocumentReadAction": "TEXTRACT_DETECT_DOCUMENT_TEXT"
 }

```

Amazon Comprehend responds with the following:

```
{
    "Classes": [
       {
          "Name": "string",
          "Score": 0.9793661236763
       }
    ]
 }
```

For more information, see [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md") in the _Amazon Comprehend API Reference_.
