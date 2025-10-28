# Detecting faces in an image

Amazon Rekognition Image provides the [DetectFaces](../APIReference/API_DetectFaces.md "../APIReference/API_DetectFaces.md")
operation that looks for key facial features such as eyes, nose, and mouth to detect
faces in an input image. Amazon Rekognition Image detects the 100 largest faces in an image.

You can provide the input image as an image byte array (base64-encoded image bytes),
or specify an Amazon S3 object. In this procedure, you upload an image (JPEG or PNG) to your
S3 bucket and specify the object key name.

###### To detect faces in an image

1. If you haven't already:
   1. Create or update a user with `AmazonRekognitionFullAccess`
      and `AmazonS3ReadOnlyAccess` permissions. For more
      information, see [Step 1: Set up an AWS account and create a
      User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   2. Install and configure the AWS CLI and the AWS SDKs. For more
      information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Upload an image (that contains one or more faces) to your S3 bucket.

For instructions, see [Uploading Objects into
Amazon S3](../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md "../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md") in the _Amazon Simple Storage Service User Guide_. 3. Use the following examples to call `DetectFaces`.

Java
This example displays the estimated age range for detected faces,
and lists the JSON for all detected facial attributes. Change the
value of `photo` to the image file name. Change the value
of `amzn-s3-demo-bucket` to the Amazon S3 bucket where the image is
stored.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

package aws.example.rekognition.image;

import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
import com.amazonaws.services.rekognition.model.Image;
import com.amazonaws.services.rekognition.model.S3Object;
import com.amazonaws.services.rekognition.model.AgeRange;
import com.amazonaws.services.rekognition.model.Attribute;
import com.amazonaws.services.rekognition.model.DetectFacesRequest;
import com.amazonaws.services.rekognition.model.DetectFacesResult;
import com.amazonaws.services.rekognition.model.FaceDetail;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.List;


public class DetectFaces {


   public static void main(String[] args) throws Exception {

      String photo = "input.jpg";
      String bucket = "bucket";

      AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();


      DetectFacesRequest request = new DetectFacesRequest()
         .withImage(new Image()
            .withS3Object(new S3Object()
               .withName(photo)
               .withBucket(bucket)))
         .withAttributes(Attribute.ALL);
      // Replace Attribute.ALL with Attribute.DEFAULT to get default values.

      try {
         DetectFacesResult result = rekognitionClient.detectFaces(request);
         List < FaceDetail > faceDetails = result.getFaceDetails();

         for (FaceDetail face: faceDetails) {
            if (request.getAttributes().contains("ALL")) {
               AgeRange ageRange = face.getAgeRange();
               System.out.println("The detected face is estimated to be between "
                  + ageRange.getLow().toString() + " and " + ageRange.getHigh().toString()
                  + " years old.");
               System.out.println("Here's the complete set of attributes:");
            } else { // non-default attributes have null values.
               System.out.println("Here's the default set of attributes:");
            }

            ObjectMapper objectMapper = new ObjectMapper();
            System.out.println(objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(face));
         }

      } catch (AmazonRekognitionException e) {
         e.printStackTrace();
      }

   }

}


```

Java V2
This code is taken from the AWS Documentation SDK examples
GitHub repository. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectFaces.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectFaces.java").

```
import java.util.List;

//snippet-start:[rekognition.java2.detect_labels.import]
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.S3Object;
import software.amazon.awssdk.services.rekognition.model.DetectFacesRequest;
import software.amazon.awssdk.services.rekognition.model.DetectFacesResponse;
import software.amazon.awssdk.services.rekognition.model.Image;
import software.amazon.awssdk.services.rekognition.model.Attribute;
import software.amazon.awssdk.services.rekognition.model.FaceDetail;
import software.amazon.awssdk.services.rekognition.model.AgeRange;

//snippet-end:[rekognition.java2.detect_labels.import]

public class DetectFaces {

    public static void main(String[] args) {
        final String usage = "\n" +
            "Usage: " +
            "   <bucket> <image>\n\n" +
            "Where:\n" +
            "   bucket - The name of the Amazon S3 bucket that contains the image (for example, ,amzn-s3-demo-bucket)." +
            "   image - The name of the image located in the Amazon S3 bucket (for example, Lake.png). \n\n";

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String bucket = args[0];
        String image = args[1];
        Region region = Region.US_WEST_2;
        RekognitionClient rekClient = RekognitionClient.builder()
            .region(region)
            .credentialsProvider(ProfileCredentialsProvider.create("profile-name"))
            .build();

        getLabelsfromImage(rekClient, bucket, image);
        rekClient.close();
    }

    // snippet-start:[rekognition.java2.detect_labels_s3.main]
    public static void getLabelsfromImage(RekognitionClient rekClient, String bucket, String image) {

        try {
            S3Object s3Object = S3Object.builder()
                .bucket(bucket)
                .name(image)
                .build() ;

            Image myImage = Image.builder()
                .s3Object(s3Object)
                .build();

            DetectFacesRequest facesRequest = DetectFacesRequest.builder()
                    .attributes(Attribute.ALL)
                    .image(myImage)
                    .build();

                DetectFacesResponse facesResponse = rekClient.detectFaces(facesRequest);
                List<FaceDetail> faceDetails = facesResponse.faceDetails();
                for (FaceDetail face : faceDetails) {
                    AgeRange ageRange = face.ageRange();
                    System.out.println("The detected face is estimated to be between "
                                + ageRange.low().toString() + " and " + ageRange.high().toString()
                                + " years old.");

                    System.out.println("There is a smile : "+face.smile().value().toString());
                }

        } catch (RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }
 // snippet-end:[rekognition.java2.detect_labels.main]
}
```

AWS CLI
This example displays the JSON output from the
`detect-faces` AWS CLI operation. Replace
`file` with the name of an image file. Replace
`amzn-s3-demo-bucket` with the name of the Amazon S3 bucket that
contains the image file.

```
aws rekognition detect-faces --image "{"S3Object":{"Bucket":"amzn-s3-demo-bucket,"Name":"image-name"}}"\
                             --attributes "ALL" --profile profile-name --region region-name

```

If you are accessing the CLI on a Windows device, use double
quotes instead of single quotes and escape the inner double quotes
by backslash (i.e. \) to address any parser errors you may
encounter. For an example, see the following:

```

aws rekognition detect-faces --image "{\"S3Object\":{\"Bucket\":\"amzn-s3-demo-bucket\",\"Name\":\"image-name\"}}" --attributes "ALL"
--profile profile-name --region region-name

```

Python
This example displays the estimated age range and other attributes
for detected faces, and lists the JSON for all detected facial
attributes. Change the value of `photo` to the image file
name. Change the value of `amzn-s3-demo-bucket` to the Amazon S3 bucket
where the image is stored. Replace the value of
`profile_name` in the line that creates the Rekognition
session with the name of your developer profile.

```
import boto3
import json

def detect_faces(photo, bucket, region):

    session = boto3.Session(profile_name='profile-name',
                            region_name=region)
    client = session.client('rekognition', region_name=region)

    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                   Attributes=['ALL'])

    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))

        # Access predictions for individual face details and print them
        print("Gender: " + str(faceDetail['Gender']))
        print("Smile: " + str(faceDetail['Smile']))
        print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        print("Face Occluded: " + str(faceDetail['FaceOccluded']))
        print("Emotions: " + str(faceDetail['Emotions'][0]))

    return len(response['FaceDetails'])

def main():
    photo='photo'
    bucket='amzn-s3-demo-bucket'
    region='region'
    face_count=detect_faces(photo, bucket, region)
    print("Faces detected: " + str(face_count))

if __name__ == "__main__":
    main()

```

.NET
This example displays the estimated age range for detected faces,
and lists the JSON for all detected facial attributes. Change the
value of `photo` to the image file name. Change the value
of `amzn-s3-demo-bucket` to the Amazon S3 bucket where the image is
stored.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

using System;
using System.Collections.Generic;
using Amazon.Rekognition;
using Amazon.Rekognition.Model;

public class DetectFaces
{
    public static void Example()
    {
        String photo = "input.jpg";
        String bucket = "amzn-s3-demo-bucket";

        AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();

        DetectFacesRequest detectFacesRequest = new DetectFacesRequest()
        {
            Image = new Image()
            {
                S3Object = new S3Object()
                {
                    Name = photo,
                    Bucket = bucket
                },
            },
            // Attributes can be "ALL" or "DEFAULT".
            // "DEFAULT": BoundingBox, Confidence, Landmarks, Pose, and Quality.
            // "ALL": See https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Rekognition/TFaceDetail.html
            Attributes = new List<String>() { "ALL" }
        };

        try
        {
            DetectFacesResponse detectFacesResponse = rekognitionClient.DetectFaces(detectFacesRequest);
            bool hasAll = detectFacesRequest.Attributes.Contains("ALL");
            foreach(FaceDetail face in detectFacesResponse.FaceDetails)
            {
                Console.WriteLine("BoundingBox: top={0} left={1} width={2} height={3}", face.BoundingBox.Left,
                    face.BoundingBox.Top, face.BoundingBox.Width, face.BoundingBox.Height);
                Console.WriteLine("Confidence: {0}\nLandmarks: {1}\nPose: pitch={2} roll={3} yaw={4}\nQuality: {5}",
                    face.Confidence, face.Landmarks.Count, face.Pose.Pitch,
                    face.Pose.Roll, face.Pose.Yaw, face.Quality);
                if (hasAll)
                    Console.WriteLine("The detected face is estimated to be between " +
                        face.AgeRange.Low + " and " + face.AgeRange.High + " years old.");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
```

Ruby
This example displays the estimated age range for detected faces,
and lists various facial attributes. Change the value of
`photo` to the image file name. Change the value of
`amzn-s3-demo-bucket` to the Amazon S3 bucket where the image is
stored.

```


   # Add to your Gemfile
   # gem 'aws-sdk-rekognition'
   require 'aws-sdk-rekognition'
   credentials = Aws::Credentials.new(
      ENV['AWS_ACCESS_KEY_ID'],
      ENV['AWS_SECRET_ACCESS_KEY']
   )
   bucket = 'bucket' # the bucketname without s3://
   photo  = 'input.jpg'# the name of file
   client   = Aws::Rekognition::Client.new credentials: credentials
   attrs = {
     image: {
       s3_object: {
         bucket: bucket,
         name: photo
       },
     },
     attributes: ['ALL']
   }
   response = client.detect_faces attrs
   puts "Detected faces for: #{photo}"
   response.face_details.each do |face_detail|
     low  = face_detail.age_range.low
     high = face_detail.age_range.high
     puts "The detected face is between: #{low} and #{high} years old"
     puts "All other attributes:"
     puts "  bounding_box.width:     #{face_detail.bounding_box.width}"
     puts "  bounding_box.height:    #{face_detail.bounding_box.height}"
     puts "  bounding_box.left:      #{face_detail.bounding_box.left}"
     puts "  bounding_box.top:       #{face_detail.bounding_box.top}"
     puts "  age.range.low:          #{face_detail.age_range.low}"
     puts "  age.range.high:         #{face_detail.age_range.high}"
     puts "  smile.value:            #{face_detail.smile.value}"
     puts "  smile.confidence:       #{face_detail.smile.confidence}"
     puts "  eyeglasses.value:       #{face_detail.eyeglasses.value}"
     puts "  eyeglasses.confidence:  #{face_detail.eyeglasses.confidence}"
     puts "  sunglasses.value:       #{face_detail.sunglasses.value}"
     puts "  sunglasses.confidence:  #{face_detail.sunglasses.confidence}"
     puts "  gender.value:           #{face_detail.gender.value}"
     puts "  gender.confidence:      #{face_detail.gender.confidence}"
     puts "  beard.value:            #{face_detail.beard.value}"
     puts "  beard.confidence:       #{face_detail.beard.confidence}"
     puts "  mustache.value:         #{face_detail.mustache.value}"
     puts "  mustache.confidence:    #{face_detail.mustache.confidence}"
     puts "  eyes_open.value:        #{face_detail.eyes_open.value}"
     puts "  eyes_open.confidence:   #{face_detail.eyes_open.confidence}"
     puts "  mout_open.value:        #{face_detail.mouth_open.value}"
     puts "  mout_open.confidence:   #{face_detail.mouth_open.confidence}"
     puts "  emotions[0].type:       #{face_detail.emotions[0].type}"
     puts "  emotions[0].confidence: #{face_detail.emotions[0].confidence}"
     puts "  landmarks[0].type:      #{face_detail.landmarks[0].type}"
     puts "  landmarks[0].x:         #{face_detail.landmarks[0].x}"
     puts "  landmarks[0].y:         #{face_detail.landmarks[0].y}"
     puts "  pose.roll:              #{face_detail.pose.roll}"
     puts "  pose.yaw:               #{face_detail.pose.yaw}"
     puts "  pose.pitch:             #{face_detail.pose.pitch}"
     puts "  quality.brightness:     #{face_detail.quality.brightness}"
     puts "  quality.sharpness:      #{face_detail.quality.sharpness}"
     puts "  confidence:             #{face_detail.confidence}"
     puts "------------"
     puts ""
   end
```

Node.js
This example displays the estimated age range for detected faces,
and lists various facial attributes. Change the value of
`photo` to the image file name. Change the value of
`amzn-s3-demo-bucket` to the Amazon S3 bucket where the image is
stored.

Replace the value of `profile_name` in the line that
creates the Rekognition session with the name of your developer profile.

If you are using TypeScript definitions, you may need to use
`import AWS from 'aws-sdk'` instead of `const
 AWS = require('aws-sdk')`, in order to run the program
with Node.js. You can consult the [AWS
SDK for Javascript](../../../AWSJavaScriptSDK/latest.md "../../../AWSJavaScriptSDK/latest.md") for more details. Depending on how
you have your configurations set up, you also may need to specify
your region with
`AWS.config.update({region:`region`});`.

```


// Load the SDK
var AWS = require('aws-sdk');
const bucket = 'bucket-name' // the bucketname without s3://
const photo  = 'photo-name' // the name of file

var credentials = new AWS.SharedIniFileCredentials({profile: 'profile-name'});
AWS.config.credentials = credentials;
AWS.config.update({region:'region-name'});

const client = new AWS.Rekognition();
const params = {
  Image: {
    S3Object: {
      Bucket: bucket,
      Name: photo
    },
  },
  Attributes: ['ALL']
}

client.detectFaces(params, function(err, response) {
    if (err) {
      console.log(err, err.stack); // an error occurred
    } else {
      console.log(`Detected faces for: ${photo}`)
      response.FaceDetails.forEach(data => {
        let low  = data.AgeRange.Low
        let high = data.AgeRange.High
        console.log(`The detected face is between: ${low} and ${high} years old`)
        console.log("All other attributes:")
        console.log(`  BoundingBox.Width:      ${data.BoundingBox.Width}`)
        console.log(`  BoundingBox.Height:     ${data.BoundingBox.Height}`)
        console.log(`  BoundingBox.Left:       ${data.BoundingBox.Left}`)
        console.log(`  BoundingBox.Top:        ${data.BoundingBox.Top}`)
        console.log(`  Age.Range.Low:          ${data.AgeRange.Low}`)
        console.log(`  Age.Range.High:         ${data.AgeRange.High}`)
        console.log(`  Smile.Value:            ${data.Smile.Value}`)
        console.log(`  Smile.Confidence:       ${data.Smile.Confidence}`)
        console.log(`  Eyeglasses.Value:       ${data.Eyeglasses.Value}`)
        console.log(`  Eyeglasses.Confidence:  ${data.Eyeglasses.Confidence}`)
        console.log(`  Sunglasses.Value:       ${data.Sunglasses.Value}`)
        console.log(`  Sunglasses.Confidence:  ${data.Sunglasses.Confidence}`)
        console.log(`  Gender.Value:           ${data.Gender.Value}`)
        console.log(`  Gender.Confidence:      ${data.Gender.Confidence}`)
        console.log(`  Beard.Value:            ${data.Beard.Value}`)
        console.log(`  Beard.Confidence:       ${data.Beard.Confidence}`)
        console.log(`  Mustache.Value:         ${data.Mustache.Value}`)
        console.log(`  Mustache.Confidence:    ${data.Mustache.Confidence}`)
        console.log(`  EyesOpen.Value:         ${data.EyesOpen.Value}`)
        console.log(`  EyesOpen.Confidence:    ${data.EyesOpen.Confidence}`)
        console.log(`  MouthOpen.Value:        ${data.MouthOpen.Value}`)
        console.log(`  MouthOpen.Confidence:   ${data.MouthOpen.Confidence}`)
        console.log(`  Emotions[0].Type:       ${data.Emotions[0].Type}`)
        console.log(`  Emotions[0].Confidence: ${data.Emotions[0].Confidence}`)
        console.log(`  Landmarks[0].Type:      ${data.Landmarks[0].Type}`)
        console.log(`  Landmarks[0].X:         ${data.Landmarks[0].X}`)
        console.log(`  Landmarks[0].Y:         ${data.Landmarks[0].Y}`)
        console.log(`  Pose.Roll:              ${data.Pose.Roll}`)
        console.log(`  Pose.Yaw:               ${data.Pose.Yaw}`)
        console.log(`  Pose.Pitch:             ${data.Pose.Pitch}`)
        console.log(`  Quality.Brightness:     ${data.Quality.Brightness}`)
        console.log(`  Quality.Sharpness:      ${data.Quality.Sharpness}`)
        console.log(`  Confidence:             ${data.Confidence}`)
        console.log("------------")
        console.log("")
      }) // for response.faceDetails
    } // if
  });
```

## DetectFaces operation request

The input to `DetectFaces` is an image. In this example, the image is
loaded from an Amazon S3 bucket. The `Attributes` parameter specifies that all
facial attributes should be returned. For more information, see [Working with images](images.md "images.md").

```
{
    "Image": {
        "S3Object": {
            "Bucket": "amzn-s3-demo-bucket",
            "Name": "input.jpg"
        }
    },
    "Attributes": [
        "ALL"
    ]
}
```

## DetectFaces operation response

`DetectFaces` returns the following information for each detected
face:

- **Bounding box** – The coordinates of
  the bounding box that surrounds the face.
- **Confidence** – The level of
  confidence that the bounding box contains a face.
- **Facial landmarks** – An array of
  facial landmarks. For each landmark (such as the left eye, right eye, and
  mouth), the response provides the x and y coordinates.
- **Facial attributes** – A set of facial
  attributes, such as whether the face is occluded, returned as a
  `FaceDetail` object. The set includes: AgeRange, Beard,
  Emotions, EyeDirection, Eyeglasses, EyesOpen, FaceOccluded, Gender,
  MouthOpen, Mustache, Smile, and Sunglasses. For each such attribute, the
  response provides a value. The value can be of different types, such as a
  Boolean type (whether a person is wearing sunglasses), a string (whether the
  person is male or female), or an angular degree value (for pitch/yaw of eye
  gaze directions). In addition, for most attributes, the response also
  provides a confidence in the detected value for the attribute. Note that
  while FaceOccluded and EyeDirection attributes are supported when using
  `DetectFaces`, they aren't supported when analyzing videos
  with `StartFaceDetection` and
  `GetFaceDetection`.
- **Quality** – Describes the brightness
  and the sharpness of the face. For information about ensuring the best
  possible face detection, see [Recommendations for facial
  comparison input images](recommendations-facial-input-images.md "recommendations-facial-input-images.md").
- **Pose** – Describes the rotation of
  the face inside the image.

The request can depict an array of facial attributes you want to be returned. A
`DEFAULT` subset of facial attributes - `BoundingBox`,
`Confidence`, `Pose`, `Quality`, and
`Landmarks` - will always be returned. You can request the return of
specific facial attributes (in addition to the default list) - by using
`["DEFAULT", "FACE_OCCLUDED", "EYE_DIRECTION"]` or just one
attribute, like `["FACE_OCCLUDED"]`. You can request for all facial
attributes by using `["ALL"]`. Requesting more attributes may increase
response time.

The following is an example response of a `DetectFaces` API call:

```
{
  "FaceDetails": [
    {
      "BoundingBox": {
        "Width": 0.7919622659683228,
        "Height": 0.7510867118835449,
        "Left": 0.08881539851427078,
        "Top": 0.151064932346344
      },
      "AgeRange": {
        "Low": 18,
        "High": 26
      },
      "Smile": {
        "Value": false,
        "Confidence": 89.77348327636719
      },
      "Eyeglasses": {
        "Value": true,
        "Confidence": 99.99996948242188
      },
      "Sunglasses": {
        "Value": true,
        "Confidence": 93.65237426757812
      },
      "Gender": {
        "Value": "Female",
        "Confidence": 99.85968780517578
      },
      "Beard": {
        "Value": false,
        "Confidence": 77.52591705322266
      },
      "Mustache": {
        "Value": false,
        "Confidence": 94.48904418945312
      },
      "EyesOpen": {
        "Value": true,
        "Confidence": 98.57169342041016
      },
      "MouthOpen": {
        "Value": false,
        "Confidence": 74.33953094482422
      },
      "Emotions": [
        {
          "Type": "SAD",
          "Confidence": 65.56403350830078
        },
        {
          "Type": "CONFUSED",
          "Confidence": 31.277774810791016
        },
        {
          "Type": "DISGUSTED",
          "Confidence": 15.553778648376465
        },
        {
          "Type": "ANGRY",
          "Confidence": 8.012762069702148
        },
        {
          "Type": "SURPRISED",
          "Confidence": 7.621500015258789
        },
        {
          "Type": "FEAR",
          "Confidence": 7.243380546569824
        },
        {
          "Type": "CALM",
          "Confidence": 5.8196024894714355
        },
        {
          "Type": "HAPPY",
          "Confidence": 2.2830512523651123
        }
      ],
      "Landmarks": [
        {
          "Type": "eyeLeft",
          "X": 0.30225440859794617,
          "Y": 0.41018882393836975
        },
        {
          "Type": "eyeRight",
          "X": 0.6439348459243774,
          "Y": 0.40341562032699585
        },
        {
          "Type": "mouthLeft",
          "X": 0.343580037355423,
          "Y": 0.6951127648353577
        },
        {
          "Type": "mouthRight",
          "X": 0.6306480765342712,
          "Y": 0.6898072361946106
        },
        {
          "Type": "nose",
          "X": 0.47164231538772583,
          "Y": 0.5763645172119141
        },
        {
          "Type": "leftEyeBrowLeft",
          "X": 0.1732882857322693,
          "Y": 0.34452149271965027
        },
        {
          "Type": "leftEyeBrowRight",
          "X": 0.3655243515968323,
          "Y": 0.33231860399246216
        },
        {
          "Type": "leftEyeBrowUp",
          "X": 0.2671719491481781,
          "Y": 0.31669262051582336
        },
        {
          "Type": "rightEyeBrowLeft",
          "X": 0.5613729953765869,
          "Y": 0.32813435792922974
        },
        {
          "Type": "rightEyeBrowRight",
          "X": 0.7665090560913086,
          "Y": 0.3318614959716797
        },
        {
          "Type": "rightEyeBrowUp",
          "X": 0.6612788438796997,
          "Y": 0.3082450032234192
        },
        {
          "Type": "leftEyeLeft",
          "X": 0.2416982799768448,
          "Y": 0.4085965156555176
        },
        {
          "Type": "leftEyeRight",
          "X": 0.36943578720092773,
          "Y": 0.41230902075767517
        },
        {
          "Type": "leftEyeUp",
          "X": 0.29974061250686646,
          "Y": 0.3971870541572571
        },
        {
          "Type": "leftEyeDown",
          "X": 0.30360740423202515,
          "Y": 0.42347756028175354
        },
        {
          "Type": "rightEyeLeft",
          "X": 0.5755768418312073,
          "Y": 0.4081145226955414
        },
        {
          "Type": "rightEyeRight",
          "X": 0.7050536870956421,
          "Y": 0.39924031496047974
        },
        {
          "Type": "rightEyeUp",
          "X": 0.642906129360199,
          "Y": 0.39026668667793274
        },
        {
          "Type": "rightEyeDown",
          "X": 0.6423097848892212,
          "Y": 0.41669243574142456
        },
        {
          "Type": "noseLeft",
          "X": 0.4122826159000397,
          "Y": 0.5987403392791748
        },
        {
          "Type": "noseRight",
          "X": 0.5394935011863708,
          "Y": 0.5960900187492371
        },
        {
          "Type": "mouthUp",
          "X": 0.478581964969635,
          "Y": 0.6660456657409668
        },
        {
          "Type": "mouthDown",
          "X": 0.483366996049881,
          "Y": 0.7497162818908691
        },
        {
          "Type": "leftPupil",
          "X": 0.30225440859794617,
          "Y": 0.41018882393836975
        },
        {
          "Type": "rightPupil",
          "X": 0.6439348459243774,
          "Y": 0.40341562032699585
        },
        {
          "Type": "upperJawlineLeft",
          "X": 0.11031254380941391,
          "Y": 0.3980775475502014
        },
        {
          "Type": "midJawlineLeft",
          "X": 0.19301874935626984,
          "Y": 0.7034031748771667
        },
        {
          "Type": "chinBottom",
          "X": 0.4939905107021332,
          "Y": 0.8877836465835571
        },
        {
          "Type": "midJawlineRight",
          "X": 0.7990140914916992,
          "Y": 0.6899225115776062
        },
        {
          "Type": "upperJawlineRight",
          "X": 0.8548634648323059,
          "Y": 0.38160091638565063
        }
      ],
      "Pose": {
        "Roll": -5.83309268951416,
        "Yaw": -2.4244730472564697,
        "Pitch": 2.6216139793395996
      },
      "Quality": {
        "Brightness": 96.16363525390625,
        "Sharpness": 95.51618957519531
      },
      "Confidence": 99.99872589111328,
      "FaceOccluded": {
        "Value": true,
        "Confidence": 99.99726104736328
      },
      "EyeDirection": {
        "Yaw": 16.299732,
        "Pitch": -6.407457,
        "Confidence": 99.968704
      }
    }
  ],
  "ResponseMetadata": {
    "RequestId": "8bf02607-70b7-4f20-be55-473fe1bba9a2",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "8bf02607-70b7-4f20-be55-473fe1bba9a2",
      "content-type": "application/x-amz-json-1.1",
      "content-length": "3409",
      "date": "Wed, 26 Apr 2023 20:18:50 GMT"
    },
    "RetryAttempts": 0
  }
}
```

Note the following:

- The `Pose` data describes the rotation of the face detected.
  You can use the combination of the `BoundingBox` and
  `Pose` data to draw the bounding box around faces that your
  application displays.
- The `Quality` describes the brightness and the sharpness of the
  face. You might find this useful to compare faces across images and find the
  best face.
- The preceding response shows all facial `landmarks` the service
  can detect, all facial attributes and emotions. To get all of these in the
  response, you must specify the `attributes` parameter with value
  `ALL`. By default, the `DetectFaces` API returns
  only the following five facial attributes: `BoundingBox`,
  `Confidence`, `Pose`, `Quality` and
  `landmarks`. The default landmarks returned are:
  `eyeLeft`, `eyeRight`, `nose`,
  `mouthLeft`, and `mouthRight`.
