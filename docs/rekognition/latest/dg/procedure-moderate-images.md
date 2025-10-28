# Detecting inappropriate images

You can use the [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md") operation to determine if an image
contains inappropriate or offensive content. For a list of moderation labels in Amazon Rekognition, see
[Using the image and video moderation APIs](moderation.md#moderation-api "moderation.md#moderation-api").

## Detecting inappropriate content in an image

The image must be in either a .jpg or a .png format. You can provide the input
image as an image byte array (base64-encoded image bytes), or specify an Amazon S3
object. In these procedures, you upload an image (.jpg or .png) to your S3
bucket.

To run these procedures, you need to have the AWS CLI or the appropriate AWS SDK installed. For
more information, see [Getting started with Amazon Rekognition](getting-started.md "getting-started.md"). The AWS account you use must have access
permissions to the Amazon Rekognition API. For more information, see
[Actions Defined by Amazon Rekognition](../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions").

###### To detect moderation labels in an image (SDK)

1. If you haven't already:
   1. Create or update an user with `AmazonRekognitionFullAccess` and
      `AmazonS3ReadOnlyAccess` permissions. For more
      information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS CLI and the AWS SDKs. For more information, see
      [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Upload an image to your S3 bucket.

For instructions, see [Uploading Objects into
Amazon S3](../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md "../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md") in the _Amazon Simple Storage Service User Guide_. 3. Use the following examples to call the `DetectModerationLabels` operation.

JavaThis example outputs detected inappropriate content label names, confidence levels, and the parent label
for detected moderation labels.

Replace the values of `amzn-s3-demo-bucket` and `photo` with the S3 bucket name and the image
file name that you used in step 2.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

package aws.example.rekognition.image;
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
import com.amazonaws.services.rekognition.model.DetectModerationLabelsRequest;
import com.amazonaws.services.rekognition.model.DetectModerationLabelsResult;
import com.amazonaws.services.rekognition.model.Image;
import com.amazonaws.services.rekognition.model.ModerationLabel;
import com.amazonaws.services.rekognition.model.S3Object;

import java.util.List;

public class DetectModerationLabels
{
   public static void main(String[] args) throws Exception
   {
      String photo = "input.jpg";
      String bucket = "bucket";

      AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();

      DetectModerationLabelsRequest request = new DetectModerationLabelsRequest()
        .withImage(new Image().withS3Object(new S3Object().withName(photo).withBucket(bucket)))
        .withMinConfidence(60F);
      try
      {
           DetectModerationLabelsResult result = rekognitionClient.detectModerationLabels(request);
           List<ModerationLabel> labels = result.getModerationLabels();
           System.out.println("Detected labels for " + photo);
           for (ModerationLabel label : labels)
           {
              System.out.println("Label: " + label.getName()
               + "\n Confidence: " + label.getConfidence().toString() + "%"
               + "\n Parent:" + label.getParentName());
          }
       }
       catch (AmazonRekognitionException e)
       {
         e.printStackTrace();
       }
    }
}


```

Java V2
This code is taken from the AWS Documentation SDK examples GitHub repository. See the full example
[here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectModerationLabels.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectModerationLabels.java").

```
//snippet-start:[rekognition.java2.recognize_video_text.import]
//snippet-start:[rekognition.java2.detect_mod_labels.import]
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.Image;
import software.amazon.awssdk.services.rekognition.model.DetectModerationLabelsRequest;
import software.amazon.awssdk.services.rekognition.model.DetectModerationLabelsResponse;
import software.amazon.awssdk.services.rekognition.model.ModerationLabel;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.List;
//snippet-end:[rekognition.java2.detect_mod_labels.import]

/**
* Before running this Java V2 code example, set up your development environment, including your credentials.
*
* For more information, see the following documentation topic:
*
* https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
*/
public class ModerateLabels {

 public static void main(String[] args) {

     final String usage = "\n" +
         "Usage: " +
         "   <sourceImage>\n\n" +
         "Where:\n" +
         "   sourceImage - The path to the image (for example, C:\\AWS\\pic1.png). \n\n";

     if (args.length < 1) {
         System.out.println(usage);
         System.exit(1);
     }

     String sourceImage = args[0];
     Region region = Region.US_WEST_2;
     RekognitionClient rekClient = RekognitionClient.builder()
         .region(region)
         .credentialsProvider(ProfileCredentialsProvider.create("profile-name"))
         .build();

     detectModLabels(rekClient, sourceImage);
     rekClient.close();
 }

 // snippet-start:[rekognition.java2.detect_mod_labels.main]
 public static void detectModLabels(RekognitionClient rekClient, String sourceImage) {

     try {
         InputStream sourceStream = new FileInputStream(sourceImage);
         SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);
         Image souImage = Image.builder()
             .bytes(sourceBytes)
             .build();

         DetectModerationLabelsRequest moderationLabelsRequest = DetectModerationLabelsRequest.builder()
             .image(souImage)
             .minConfidence(60F)
             .build();

         DetectModerationLabelsResponse moderationLabelsResponse = rekClient.detectModerationLabels(moderationLabelsRequest);
         List<ModerationLabel> labels = moderationLabelsResponse.moderationLabels();
         System.out.println("Detected labels for image");

         for (ModerationLabel label : labels) {
             System.out.println("Label: " + label.name()
                 + "\n Confidence: " + label.confidence().toString() + "%"
                 + "\n Parent:" + label.parentName());
         }

     } catch (RekognitionException | FileNotFoundException e) {
         e.printStackTrace();
         System.exit(1);
     }
 }
 // snippet-end:[rekognition.java2.detect_mod_labels.main]
```

AWS CLI
This AWS CLI command displays the JSON output for the
`detect-moderation-labels` CLI operation.

Replace `amzn-s3-demo-bucket` and `input.jpg` with
the S3 bucket name and the image file name that you used in step 2. Replace the value of `profile_name` with the name
of your developer profile. To use an adapter, provide the ARN of
the project version to the `project-version`
parameter.

```
aws rekognition detect-moderation-labels --image "{S3Object:{Bucket:<`amzn-s3-demo-bucket`>,Name:<`image-name`>}}" \
--profile `profile-name` \
--project-version "`ARN`"
```

If you are accessing the CLI on a Windows device, use double
quotes instead of single quotes and escape the inner double
quotes by backslash (i.e. \) to address any parser errors you
may encounter. For an example, see the following:

```
aws rekognition detect-moderation-labels --image "{\"S3Object\":{\"Bucket\":\"amzn-s3-demo-bucket\",\"Name\":\"image-name\"}}" \
--profile profile-name
```

PythonThis example outputs detected inappropriate or offensive content label names, confidence levels, and the parent label
for detected inappropriate content labels.

In the function `main`, replace the values of `amzn-s3-demo-bucket` and `photo` with the S3 bucket name and the image
file name that you used in step 2. Replace the value of `profile_name` in the line that creates the Rekognition session with the name of your developer profile.

```
#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def moderate_image(photo, bucket):

    session = boto3.Session(profile_name='profile-name')
    client = session.client('rekognition')

    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    print('Detected labels for ' + photo)
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
    return len(response['ModerationLabels'])

def main():

    photo='image-name'
    bucket='amzn-s3-demo-bucket'
    label_count=moderate_image(photo, bucket)
    print("Labels detected: " + str(label_count))

if __name__ == "__main__":
    main()
```

.NETThis example outputs detected inappropriate or offensive content label names, confidence levels, and the parent label
for detected moderation labels.

Replace the values of `amzn-s3-demo-bucket` and `photo` with the S3 bucket name and the image
file name that you used in step 2.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

using System;
using Amazon.Rekognition;
using Amazon.Rekognition.Model;

public class DetectModerationLabels
{
    public static void Example()
    {
        String photo = "input.jpg";
        String bucket = "amzn-s3-demo-bucket";

        AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();

        DetectModerationLabelsRequest detectModerationLabelsRequest = new DetectModerationLabelsRequest()
        {
            Image = new Image()
            {
                S3Object = new S3Object()
                {
                    Name = photo,
                    Bucket = bucket
                },
            },
            MinConfidence = 60F
        };

        try
        {
            DetectModerationLabelsResponse detectModerationLabelsResponse = rekognitionClient.DetectModerationLabels(detectModerationLabelsRequest);
            Console.WriteLine("Detected labels for " + photo);
            foreach (ModerationLabel label in detectModerationLabelsResponse.ModerationLabels)
                Console.WriteLine("Label: {0}\n Confidence: {1}\n Parent: {2}",
                    label.Name, label.Confidence, label.ParentName);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
```

## DetectModerationLabels operation request

The input to `DetectModerationLabels` is an image. In this example JSON
input, the source image is loaded from an Amazon S3 bucket. `MinConfidence` is
the minimum confidence that Amazon Rekognition Image must have in the accuracy of the detected label
for it to be returned in the response.

```
{
    "Image": {
        "S3Object": {
            "Bucket": "amzn-s3-demo-bucket",
            "Name": "input.jpg"
        }
    },
    "MinConfidence": 60
}
```

## DetectModerationLabels operation response

`DetectModerationLabels` can retrieve input images from an S3 bucket, or
you can provide them as image bytes. The following example is the response from a
call to `DetectModerationLabels`.

In the following example JSON response, note the following:

- **Inappropriate Image Detection information** –
  The example shows a list of labels for inappropriate or offensive
  content found in the image. The list includes the top-level label and each
  second-level label that are detected in the image.

**Label** – Each label has a name, an
estimation of the confidence that Amazon Rekognition has that the label is
accurate, and the name of its parent label.
The parent name for a top-level label is
`""`.

**Label confidence** – Each label has a
confidence value between 0 and 100 that indicates the percentage
confidence that Amazon Rekognition has that the label is correct. You specify the
required confidence level for a label to be returned in the response in
the API operation request.

```
{
    "ModerationLabels": [
        {
            "Confidence": 99.44782257080078,
            "Name": "Smoking",
            "ParentName": "Drugs & Tobacco Paraphernalia & Use",
            "TaxonomyLevel": 3
        },
        {
            "Confidence": 99.44782257080078,
            "Name": "Drugs & Tobacco Paraphernalia & Use",
            "ParentName": "Drugs & Tobacco",
            "TaxonomyLevel": 2
        },
        {
            "Confidence": 99.44782257080078,
            "Name": "Drugs & Tobacco",
            "ParentName": "",
            "TaxonomyLevel": 1
        }
    ],
    "ModerationModelVersion": "7.0",
    "ContentTypes": [
        {
            "Confidence": 99.9999008178711,
            "Name": "Illustrated"
        }
    ]
}
```
