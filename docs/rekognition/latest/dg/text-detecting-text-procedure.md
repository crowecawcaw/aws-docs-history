# Detecting text in an image

You can provide an input image as an image byte array (base64-encoded image bytes), or
as an Amazon S3 object. In this procedure, you upload a JPEG or PNG image to your S3 bucket
and specify the file name.

###### To

detect text in an image (API)

1. If you haven't already, complete the following prerequisites.
   1. Create or update a user with
      `AmazonRekognitionFullAccess` and
      `AmazonS3ReadOnlyAccess` permissions. For more
      information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS Command Line Interface and the AWS SDKs. For more
      information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Upload the image that contains text to your S3 bucket.

For instructions, see [Uploading Objects into
Amazon S3](../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md "../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md") in the _Amazon Simple Storage Service User Guide_. 3. Use the following examples to call the `DetectText`
operation.

Java
The following example code displays lines and words that were
detected in an image.

Replace the values of
`amzn-s3-demo-bucket`
and `photo` with the names of the S3
bucket and image that you used in step 2.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

package aws.example.rekognition.image;
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
import com.amazonaws.services.rekognition.model.Image;
import com.amazonaws.services.rekognition.model.S3Object;
import com.amazonaws.services.rekognition.model.DetectTextRequest;
import com.amazonaws.services.rekognition.model.DetectTextResult;
import com.amazonaws.services.rekognition.model.TextDetection;
import java.util.List;



public class DetectText {

   public static void main(String[] args) throws Exception {


      String photo = "inputtext.jpg";
      String bucket = "bucket";

      AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();



      DetectTextRequest request = new DetectTextRequest()
              .withImage(new Image()
              .withS3Object(new S3Object()
              .withName(photo)
              .withBucket(bucket)));


      try {
         DetectTextResult result = rekognitionClient.detectText(request);
         List<TextDetection> textDetections = result.getTextDetections();

         System.out.println("Detected lines and words for " + photo);
         for (TextDetection text: textDetections) {

                 System.out.println("Detected: " + text.getDetectedText());
                 System.out.println("Confidence: " + text.getConfidence().toString());
                 System.out.println("Id : " + text.getId());
                 System.out.println("Parent Id: " + text.getParentId());
                 System.out.println("Type: " + text.getType());
                 System.out.println();
         }
      } catch(AmazonRekognitionException e) {
         e.printStackTrace();
      }
   }
}
```

Java V2
This code is taken from the AWS Documentation SDK examples
GitHub repository. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectText.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectText.java").

```
/**
*  To run this code example, ensure that you perform the Prerequisites as stated in the Amazon Rekognition Guide:
*  https://docs.aws.amazon.com/rekognition/latest/dg/video-analyzing-with-sqs.html
*
* Also, ensure that set up your development environment, including your credentials.
*
* For information, see this documentation topic:
*
* https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
*/

//snippet-start:[rekognition.java2.detect_text.import]
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.DetectTextRequest;
import software.amazon.awssdk.services.rekognition.model.Image;
import software.amazon.awssdk.services.rekognition.model.DetectTextResponse;
import software.amazon.awssdk.services.rekognition.model.TextDetection;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.List;
//snippet-end:[rekognition.java2.detect_text.import]

/**
* Before running this Java V2 code example, set up your development environment, including your credentials.
*
* For more information, see the following documentation topic:
*
* https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
*/
public class DetectTextImage {

 public static void main(String[] args) {

     final String usage = "\n" +
         "Usage: " +
         "   <sourceImage>\n\n" +
         "Where:\n" +
         "   sourceImage - The path to the image that contains text (for example, C:\\AWS\\pic1.png). \n\n";

   if (args.length != 1) {
         System.out.println(usage);
         System.exit(1);
     }

     String sourceImage = args[0] ;
     Region region = Region.US_WEST_2;
     RekognitionClient rekClient = RekognitionClient.builder()
         .region(region)
         .credentialsProvider(ProfileCredentialsProvider.create("default"))
         .build();

     detectTextLabels(rekClient, sourceImage );
     rekClient.close();
 }

 // snippet-start:[rekognition.java2.detect_text.main]
 public static void detectTextLabels(RekognitionClient rekClient, String sourceImage) {

     try {
         InputStream sourceStream = new FileInputStream(sourceImage);
         SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);
         Image souImage = Image.builder()
             .bytes(sourceBytes)
             .build();

         DetectTextRequest textRequest = DetectTextRequest.builder()
             .image(souImage)
             .build();

         DetectTextResponse textResponse = rekClient.detectText(textRequest);
         List<TextDetection> textCollection = textResponse.textDetections();
         System.out.println("Detected lines and words");
         for (TextDetection text: textCollection) {
             System.out.println("Detected: " + text.detectedText());
             System.out.println("Confidence: " + text.confidence().toString());
             System.out.println("Id : " + text.id());
             System.out.println("Parent Id: " + text.parentId());
             System.out.println("Type: " + text.type());
             System.out.println();
         }

     } catch (RekognitionException | FileNotFoundException e) {
         System.out.println(e.getMessage());
         System.exit(1);
     }
 }
 // snippet-end:[rekognition.java2.detect_text.main]
```

AWS CLI
This AWS CLI command displays the JSON output for the
`detect-text` CLI operation.

Replace the values of `amzn-s3-demo-bucket` and `Name`
with the names of the S3 bucket and image that you used in step 2.

Replace the value of `profile_name` with the name of
your developer profile.

```
aws rekognition detect-text  --image "{"S3Object":{"Bucket":"amzn-s3-demo-bucket","Name":"image-name"}}" --profile default
```

If you are accessing the CLI on a Windows device, use double
quotes instead of single quotes and escape the inner double quotes
by backslash (i.e. \) to address any parser errors you may
encounter. For an example, see the following:

```
aws rekognition detect-text  --image "{\"S3Object\":{\"Bucket\":\"amzn-s3-demo-bucket\",\"Name\":\"image-name\"}}" --profile default
```

Python
The following example code displays lines and words detected in an
image.

Replace the values of `amzn-s3-demo-bucket` and `photo`
with the names of the S3 bucket and image that you used in step 2.
Replace the value of `profile_name` in the line that creates the Rekognition session with the name of your developer profile.

```
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def detect_text(photo, bucket):

    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})

    textDetections = response['TextDetections']
    print('Detected text\n----------')
    for text in textDetections:
        print('Detected text:' + text['DetectedText'])
        print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print('Parent Id: {}'.format(text['ParentId']))
        print('Type:' + text['Type'])
        print()
    return len(textDetections)

def main():
    bucket = 'amzn-s3-demo-bucket'
    photo = 'photo-name'
    text_count = detect_text(photo, bucket)
    print("Text detected: " + str(text_count))

if __name__ == "__main__":
    main()
```

.NET
The following example code displays lines and words detected in an
image.

Replace the values of `amzn-s3-demo-bucket` and `photo`
with the names of the S3 bucket and image that you used in step 2.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

using System;
using Amazon.Rekognition;
using Amazon.Rekognition.Model;

public class DetectText
{
    public static void Example()
    {
        String photo = "input.jpg";
        String bucket = "amzn-s3-demo-bucket";

        AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();

        DetectTextRequest detectTextRequest = new DetectTextRequest()
        {
            Image = new Image()
            {
                S3Object = new S3Object()
                {
                    Name = photo,
                    Bucket = bucket
                }
            }
        };

        try
        {
            DetectTextResponse detectTextResponse = rekognitionClient.DetectText(detectTextRequest);
            Console.WriteLine("Detected lines and words for " + photo);
            foreach (TextDetection text in detectTextResponse.TextDetections)
            {
                Console.WriteLine("Detected: " + text.DetectedText);
                Console.WriteLine("Confidence: " + text.Confidence);
                Console.WriteLine("Id : " + text.Id);
                Console.WriteLine("Parent Id: " + text.ParentId);
                Console.WriteLine("Type: " + text.Type);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
```

Node.JS
The following example code displays lines and words detected in an
image.

Replace the values of `amzn-s3-demo-bucket` and `photo`
with the names of the S3 bucket and image that you used in step 2.
Replace the value of `region` with the region found in
your .aws credentials. Replace the value of `profile_name` in the line that creates the Rekognition session with the name of your developer profile.

```
var AWS = require('aws-sdk');

const bucket = 'bucket' // the bucketname without s3://
const photo  = 'photo' // the name of file

const config = new AWS.Config({
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
})
AWS.config.update({region:'region'});
const client = new AWS.Rekognition();
const params = {
  Image: {
    S3Object: {
      Bucket: bucket,
      Name: photo
    },
  },
}
client.detectText(params, function(err, response) {
  if (err) {
    console.log(err, err.stack); // handle error if an error occurred
  } else {
    console.log(`Detected Text for: ${photo}`)
    console.log(response)
    response.TextDetections.forEach(label => {
      console.log(`Detected Text: ${label.DetectedText}`),
      console.log(`Type: ${label.Type}`),
      console.log(`ID: ${label.Id}`),
      console.log(`Parent ID: ${label.ParentId}`),
      console.log(`Confidence: ${label.Confidence}`),
      console.log(`Polygon: `)
      console.log(label.Geometry.Polygon)
    }
    )
  }
});
```

## DetectText operation request

In the `DetectText` operation, you supply an input image either as a
base64-encoded byte array or as an image stored in an Amazon S3 bucket. The following
example JSON request shows the image loaded from an Amazon S3 bucket.

```
{
    "Image": {
        "S3Object": {
            "Bucket": "amzn-s3-demo-bucket",
            "Name": "inputtext.jpg"
        }
    }
}
```

### Filters

Filtering by text region, size and confidence score provides you with
additional flexibility to control your text detection output. By using regions
of interest, you can easily limit text detection to the regions that are
relevant to you, for example, the top right of profile photo or a fixed location
in relation to a reference point when reading parts numbers from an image of a
machine. Word bounding box size filter can be used to avoid small background
text which may be noisy or irrelevant. Word confidence filter enables you to
remove results that may be unreliable due to being blurry or smudged.

For information regarding filter values, see `DetectTextFilters`.

You can use the following filters:

- **MinConfidence** –Sets the
  confidence level of word detection. Words with detection confidence
  below this level are excluded from the result. Values should be between
  0 and 100.
- **MinBoundingBoxWidth** – Sets the
  minimum width of the word bounding box. Words with bounding boxes that
  are smaller than this value are excluded from the result. The value is
  relative to the image frame width.
- **MinBoundingBoxHeight** – Sets
  the minimum height of the word bounding box. Words with bounding box
  heights less than this value are excluded from the result. The value is
  relative to the image frame height.
- **RegionsOfInterest** – Limits
  detection to a specific region of the image frame. The values are
  relative to the frame's dimensions. For text only partially within a
  region, the response is undefined.

## DetectText operation response

The `DetectText` operation analyzes the image and returns an array,
TextDetections, where each element (`TextDetection`) represents a line or word detected in the
image. For each element, `DetectText` returns the following information:

- The detected text (`DetectedText`)
- The relationships between words and lines (`Id` and
  `ParentId`)
- The location of text on the image (`Geometry`)
- The confidence Amazon Rekognition has in the accuracy of the detected text and
  bounding box (`Confidence`)
- The type of the detected text (`Type`)

### Detected text

Each `TextDetection` element contains recognized text (words or
lines) in the `DetectedText` field. A word is one or more script
characters not separated by spaces. `DetectText` can detect up to 100
words in an image. Returned text might include characters that make a word
unrecognizable. For example, _C@t_ instead of
_Cat_. To determine whether a `TextDetection`
element represents a line of text or a word, use the `Type`
field.

Each `TextDetection` element includes a percentage value that
represents the degree of confidence that Amazon Rekognition has in the accuracy of the
detected text and of the bounding box that surrounds the text.

### Word and line relationships

Each `TextDetection` element has an identifier field,
`Id`. The `Id` shows the word's position in a line. If
the element is a word, the parent identifier field, `ParentId`,
identifies the line where the word was detected. The `ParentId` for a
line is null. For example, the line "but keep" in the example image has the
following the `Id` and `ParentId` values:

| Text     | ID  | Parent ID |
| -------- | --- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| but keep | 3   |           |
| but      | 8   | 3         |
| keep     | 9   | 3         | ### Text location on an image To determine where the recognized text is on an image, use the bounding box ([Geometry](../APIReference/API_Geometry.md "../APIReference/API_Geometry.md")) information that's returned by `DetectText`. The `Geometry` object contains two types of bounding box information for detected lines and words: <br>• An axis-aligned coarse rectangular outline in a [BoundingBox](../APIReference/API_BoundingBox.md "../APIReference/API_BoundingBox.md") object <br>• A finer-grained polygon that's made up of multiple X and Y coordinates in a [Point](../APIReference/API_Point.md "../APIReference/API_Point.md") array The bounding box and polygon coordinates show where the text is located on the source image. The coordinate values are a ratio of the overall image size. For more information, see [BoundingBox](../APIReference/API_BoundingBox.md "../APIReference/API_BoundingBox.md"). The following JSON response from the `DetectText` operation shows the words and lines that were detected in the following image. ![Smiling coffee mug next to text that says "It's Monday but keep Smiling" on a brick background, with text bounding boxes.](images/text.png) `{ 'TextDetections': [{'Confidence': 99.35693359375, 'DetectedText': "IT'S", 'Geometry': {'BoundingBox': {'Height': 0.09988046437501907, 'Left': 0.6684935688972473, 'Top': 0.18226495385169983, 'Width': 0.1461552083492279}, 'Polygon': [{'X': 0.6684935688972473, 'Y': 0.1838926374912262}, {'X': 0.8141663074493408, 'Y': 0.18226495385169983}, {'X': 0.8146487474441528, 'Y': 0.28051772713661194}, {'X': 0.6689760088920593, 'Y': 0.2821454107761383}]}, 'Id': 0, 'Type': 'LINE'}, {'Confidence': 99.6207275390625, 'DetectedText': 'MONDAY', 'Geometry': {'BoundingBox': {'Height': 0.11442459374666214, 'Left': 0.5566731691360474, 'Top': 0.3525116443634033, 'Width': 0.39574965834617615}, 'Polygon': [{'X': 0.5566731691360474, 'Y': 0.353712260723114}, {'X': 0.9522717595100403, 'Y': 0.3525116443634033}, {'X': 0.9524227976799011, 'Y': 0.4657355844974518}, {'X': 0.5568241477012634, 'Y': 0.46693623065948486}]}, 'Id': 1, 'Type': 'LINE'}, {'Confidence': 99.6160888671875, 'DetectedText': 'but keep', 'Geometry': {'BoundingBox': {'Height': 0.08314694464206696, 'Left': 0.6398131847381592, 'Top': 0.5267938375473022, 'Width': 0.2021435648202896}, 'Polygon': [{'X': 0.640289306640625, 'Y': 0.5267938375473022}, {'X': 0.8419567942619324, 'Y': 0.5295097827911377}, {'X': 0.8414806723594666, 'Y': 0.609940767288208}, {'X': 0.6398131847381592, 'Y': 0.6072247624397278}]}, 'Id': 2, 'Type': 'LINE'}, {'Confidence': 88.95134735107422, 'DetectedText': 'Smiling', 'Geometry': {'BoundingBox': {'Height': 0.4326171875, 'Left': 0.46289217472076416, 'Top': 0.5634765625, 'Width': 0.5371078252792358}, 'Polygon': [{'X': 0.46289217472076416, 'Y': 0.5634765625}, {'X': 1.0, 'Y': 0.5634765625}, {'X': 1.0, 'Y': 0.99609375}, {'X': 0.46289217472076416, 'Y': 0.99609375}]}, 'Id': 3, 'Type': 'LINE'}, {'Confidence': 99.35693359375, 'DetectedText': "IT'S", 'Geometry': {'BoundingBox': {'Height': 0.09988046437501907, 'Left': 0.6684935688972473, 'Top': 0.18226495385169983, 'Width': 0.1461552083492279}, 'Polygon': [{'X': 0.6684935688972473, 'Y': 0.1838926374912262}, {'X': 0.8141663074493408, 'Y': 0.18226495385169983}, {'X': 0.8146487474441528, 'Y': 0.28051772713661194}, {'X': 0.6689760088920593, 'Y': 0.2821454107761383}]}, 'Id': 4, 'ParentId': 0, 'Type': 'WORD'}, {'Confidence': 99.6207275390625, 'DetectedText': 'MONDAY', 'Geometry': {'BoundingBox': {'Height': 0.11442466825246811, 'Left': 0.5566731691360474, 'Top': 0.35251158475875854, 'Width': 0.39574965834617615}, 'Polygon': [{'X': 0.5566731691360474, 'Y': 0.3537122905254364}, {'X': 0.9522718787193298, 'Y': 0.35251158475875854}, {'X': 0.9524227976799011, 'Y': 0.4657355546951294}, {'X': 0.5568241477012634, 'Y': 0.46693626046180725}]}, 'Id': 5, 'ParentId': 1, 'Type': 'WORD'}, {'Confidence': 99.96778869628906, 'DetectedText': 'but', 'Geometry': {'BoundingBox': {'Height': 0.0625, 'Left': 0.6402802467346191, 'Top': 0.5283203125, 'Width': 0.08027780801057816}, 'Polygon': [{'X': 0.6402802467346191, 'Y': 0.5283203125}, {'X': 0.7205580472946167, 'Y': 0.5283203125}, {'X': 0.7205580472946167, 'Y': 0.5908203125}, {'X': 0.6402802467346191, 'Y': 0.5908203125}]}, 'Id': 6, 'ParentId': 2, 'Type': 'WORD'}, {'Confidence': 99.26438903808594, 'DetectedText': 'keep', 'Geometry': {'BoundingBox': {'Height': 0.0818721204996109, 'Left': 0.7344760298728943, 'Top': 0.5280686020851135, 'Width': 0.10748066753149033}, 'Polygon': [{'X': 0.7349520921707153, 'Y': 0.5280686020851135}, {'X': 0.8419566750526428, 'Y': 0.5295097827911377}, {'X': 0.8414806127548218, 'Y': 0.6099407076835632}, {'X': 0.7344760298728943, 'Y': 0.6084995269775391}]}, 'Id': 7, 'ParentId': 2, 'Type': 'WORD'}, {'Confidence': 88.95134735107422, 'DetectedText': 'Smiling', 'Geometry': {'BoundingBox': {'Height': 0.4326171875, 'Left': 0.46289217472076416, 'Top': 0.5634765625, 'Width': 0.5371078252792358}, 'Polygon': [{'X': 0.46289217472076416, 'Y': 0.5634765625}, {'X': 1.0, 'Y': 0.5634765625}, {'X': 1.0, 'Y': 0.99609375}, {'X': 0.46289217472076416, 'Y': 0.99609375}]}, 'Id': 8, 'ParentId': 3, 'Type': 'WORD'}], 'TextModelVersion': '3.0'}` |
