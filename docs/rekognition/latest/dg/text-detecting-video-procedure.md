# Detecting text in a stored

video

Amazon Rekognition Video text detection in stored videos is an asynchronous operation. To start
detecting text, call [StartTextDetection](../APIReference/API_StartTextDetection.md "../APIReference/API_StartTextDetection.md").
Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon SNS topic. If the video analysis is
successful, call [GetTextDetection](../APIReference/API_GetTextDetection.md "../APIReference/API_GetTextDetection.md")
to get the analysis results. For
more information about starting video analysis and getting the results, see [Calling Amazon Rekognition Video operations](api-video.md "api-video.md").

This procedure expands on the code in [Analyzing a video stored in an Amazon S3
bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md"). It uses an Amazon SQS queue to get the
completion status of a video analysis request.

###### To detect text in a video stored in an Amazon S3 bucket (SDK)

1. Perform the steps in [Analyzing a video stored in an Amazon S3
   bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md").
2. Add the following code to the class `VideoDetect` in step 1.

Java

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)


private static void StartTextDetection(String bucket, String video) throws Exception{

    NotificationChannel channel= new NotificationChannel()
            .withSNSTopicArn(snsTopicArn)
            .withRoleArn(roleArn);

    StartTextDetectionRequest req = new StartTextDetectionRequest()
            .withVideo(new Video()
                    .withS3Object(new S3Object()
                        .withBucket(bucket)
                        .withName(video)))
            .withNotificationChannel(channel);


    StartTextDetectionResult startTextDetectionResult = rek.startTextDetection(req);
    startJobId=startTextDetectionResult.getJobId();

}

private static void GetTextDetectionResults() throws Exception{

    int maxResults=10;
    String paginationToken=null;
    GetTextDetectionResult textDetectionResult=null;

    do{
        if (textDetectionResult !=null){
            paginationToken = textDetectionResult.getNextToken();

        }


        textDetectionResult = rek.getTextDetection(new GetTextDetectionRequest()
             .withJobId(startJobId)
             .withNextToken(paginationToken)
             .withMaxResults(maxResults));

        VideoMetadata videoMetaData=textDetectionResult.getVideoMetadata();

        System.out.println("Format: " + videoMetaData.getFormat());
        System.out.println("Codec: " + videoMetaData.getCodec());
        System.out.println("Duration: " + videoMetaData.getDurationMillis());
        System.out.println("FrameRate: " + videoMetaData.getFrameRate());


        //Show text, confidence values
        List<TextDetectionResult> textDetections = textDetectionResult.getTextDetections();


        for (TextDetectionResult text: textDetections) {
            long seconds=text.getTimestamp()/1000;
            System.out.println("Sec: " + Long.toString(seconds) + " ");
            TextDetection detectedText=text.getTextDetection();

            System.out.println("Text Detected: " + detectedText.getDetectedText());
                System.out.println("Confidence: " + detectedText.getConfidence().toString());
                System.out.println("Id : " + detectedText.getId());
                System.out.println("Parent Id: " + detectedText.getParentId());
                System.out.println("Bounding Box" + detectedText.getGeometry().getBoundingBox().toString());
                System.out.println("Type: " + detectedText.getType());
                System.out.println();
        }
    } while (textDetectionResult !=null && textDetectionResult.getNextToken() != null);


}
```

In the function `main`, replace the lines:

```
        StartLabelDetection(amzn-s3-demo-bucket, video);

        if (GetSQSMessageSuccess()==true)
        	GetLabelDetectionResults();
```

with:

```
        StartTextDetection(amzn-s3-demo-bucket, video);

        if (GetSQSMessageSuccess()==true)
        	GetTextDetectionResults();
```

Java V2
This code is taken from the AWS Documentation SDK examples
GitHub repository. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoDetectText.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoDetectText.java").

```
//snippet-start:[rekognition.java2.recognize_video_text.import]
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.S3Object;
import software.amazon.awssdk.services.rekognition.model.NotificationChannel;
import software.amazon.awssdk.services.rekognition.model.Video;
import software.amazon.awssdk.services.rekognition.model.StartTextDetectionRequest;
import software.amazon.awssdk.services.rekognition.model.StartTextDetectionResponse;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.GetTextDetectionResponse;
import software.amazon.awssdk.services.rekognition.model.GetTextDetectionRequest;
import software.amazon.awssdk.services.rekognition.model.VideoMetadata;
import software.amazon.awssdk.services.rekognition.model.TextDetectionResult;
import java.util.List;
//snippet-end:[rekognition.java2.recognize_video_text.import]

/**
* Before running this Java V2 code example, set up your development environment, including your credentials.
*
* For more information, see the following documentation topic:
*
* https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
*/
public class DetectTextVideo {

 private static String startJobId ="";
 public static void main(String[] args) {

     final String usage = "\n" +
         "Usage: " +
         "   <bucket> <video> <topicArn> <roleArn>\n\n" +
         "Where:\n" +
         "   bucket - The name of the bucket in which the video is located (for example, (for example, amzn-s3-demo-bucket). \n\n"+
         "   video - The name of video (for example, people.mp4). \n\n" +
         "   topicArn - The ARN of the Amazon Simple Notification Service (Amazon SNS) topic. \n\n" +
         "   roleArn - The ARN of the AWS Identity and Access Management (IAM) role to use. \n\n" ;

     if (args.length != 4) {
         System.out.println(usage);
         System.exit(1);
     }

     String bucket = args[0];
     String video = args[1];
     String topicArn = args[2];
     String roleArn = args[3];

     Region region = Region.US_EAST_1;
     RekognitionClient rekClient = RekognitionClient.builder()
         .region(region)
         .credentialsProvider(ProfileCredentialsProvider.create("profile-name"))
         .build();

     NotificationChannel channel = NotificationChannel.builder()
         .snsTopicArn(topicArn)
         .roleArn(roleArn)
         .build();

     startTextLabels(rekClient, channel, bucket, video);
     GetTextResults(rekClient);
     System.out.println("This example is done!");
     rekClient.close();
 }

 // snippet-start:[rekognition.java2.recognize_video_text.main]
 public static void startTextLabels(RekognitionClient rekClient,
                                NotificationChannel channel,
                                String bucket,
                                String video) {
     try {
         S3Object s3Obj = S3Object.builder()
             .bucket(bucket)
             .name(video)
             .build();

         Video vidOb = Video.builder()
             .s3Object(s3Obj)
             .build();

         StartTextDetectionRequest labelDetectionRequest = StartTextDetectionRequest.builder()
             .jobTag("DetectingLabels")
             .notificationChannel(channel)
             .video(vidOb)
             .build();

         StartTextDetectionResponse labelDetectionResponse = rekClient.startTextDetection(labelDetectionRequest);
         startJobId = labelDetectionResponse.jobId();

     } catch (RekognitionException e) {
         System.out.println(e.getMessage());
         System.exit(1);
     }
 }

 public static void GetTextResults(RekognitionClient rekClient) {

     try {
         String paginationToken=null;
         GetTextDetectionResponse textDetectionResponse=null;
         boolean finished = false;
         String status;
         int yy=0 ;

         do{
             if (textDetectionResponse !=null)
                 paginationToken = textDetectionResponse.nextToken();

             GetTextDetectionRequest recognitionRequest = GetTextDetectionRequest.builder()
                 .jobId(startJobId)
                 .nextToken(paginationToken)
                 .maxResults(10)
                 .build();

             // Wait until the job succeeds.
             while (!finished) {
                 textDetectionResponse = rekClient.getTextDetection(recognitionRequest);
                 status = textDetectionResponse.jobStatusAsString();

                 if (status.compareTo("SUCCEEDED") == 0)
                     finished = true;
                 else {
                     System.out.println(yy + " status is: " + status);
                     Thread.sleep(1000);
                 }
                 yy++;
             }

             finished = false;

             // Proceed when the job is done - otherwise VideoMetadata is null.
             VideoMetadata videoMetaData=textDetectionResponse.videoMetadata();
             System.out.println("Format: " + videoMetaData.format());
             System.out.println("Codec: " + videoMetaData.codec());
             System.out.println("Duration: " + videoMetaData.durationMillis());
             System.out.println("FrameRate: " + videoMetaData.frameRate());
             System.out.println("Job");

             List<TextDetectionResult> labels= textDetectionResponse.textDetections();
             for (TextDetectionResult detectedText: labels) {
                 System.out.println("Confidence: " + detectedText.textDetection().confidence().toString());
                 System.out.println("Id : " + detectedText.textDetection().id());
                 System.out.println("Parent Id: " + detectedText.textDetection().parentId());
                 System.out.println("Type: " + detectedText.textDetection().type());
                 System.out.println("Text: " + detectedText.textDetection().detectedText());
                 System.out.println();
             }

         } while (textDetectionResponse !=null && textDetectionResponse.nextToken() != null);

     } catch(RekognitionException | InterruptedException e) {
         System.out.println(e.getMessage());
         System.exit(1);
     }
 }
 // snippet-end:[rekognition.java2.recognize_video_text.main]
}
```

Python

```
#Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

    def StartTextDetection(self):
        response=self.rek.start_text_detection(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
            NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn})

        self.startJobId=response['JobId']
        print('Start Job Id: ' + self.startJobId)

    def GetTextDetectionResults(self):
        maxResults = 10
        paginationToken = ''
        finished = False

        while finished == False:
            response = self.rek.get_text_detection(JobId=self.startJobId,
                                            MaxResults=maxResults,
                                            NextToken=paginationToken)

            print('Codec: ' + response['VideoMetadata']['Codec'])

            print('Duration: ' + str(response['VideoMetadata']['DurationMillis']))
            print('Format: ' + response['VideoMetadata']['Format'])
            print('Frame rate: ' + str(response['VideoMetadata']['FrameRate']))
            print()

            for textDetection in response['TextDetections']:
                text=textDetection['TextDetection']

                print("Timestamp: " + str(textDetection['Timestamp']))
                print("   Text Detected: " + text['DetectedText'])
                print("   Confidence: " +  str(text['Confidence']))
                print ("      Bounding box")
                print ("        Top: " + str(text['Geometry']['BoundingBox']['Top']))
                print ("        Left: " + str(text['Geometry']['BoundingBox']['Left']))
                print ("        Width: " +  str(text['Geometry']['BoundingBox']['Width']))
                print ("        Height: " +  str(text['Geometry']['BoundingBox']['Height']))
                print ("   Type: " + str(text['Type']) )
                print()

            if 'NextToken' in response:
                paginationToken = response['NextToken']
            else:
                finished = True
```

In the function `main`, replace the lines:

```
    analyzer.StartLabelDetection()
    if analyzer.GetSQSMessageSuccess()==True:
        analyzer.GetLabelDetectionResults()
```

with:

```
    analyzer.StartTextDetection()
    if analyzer.GetSQSMessageSuccess()==True:
        analyzer.GetTextDetectionResults()
```

CLI
Run the following AWS CLI command to start detecting text in a
video.

```
 aws rekognition start-text-detection --video "{"S3Object":{"Bucket":"amzn-s3-demo-bucket","Name":"video-name"}}"\
 --notification-channel "{"SNSTopicArn":"topic-arn","RoleArn":"role-arn"}" \
 --region region-name --profile profile-name
```

Update the following values:

    * Change `amzn-s3-demo-bucket` and
     `video-name` to the Amazon S3 bucket name and file
     name that you specified in step 2.
    * Change `region-name` to the AWS region that
     you're using.
    * Replace the value of `profile-name` with the
     name of your developer profile.
    * Change `topic-ARN` to the ARN of the Amazon SNS
     topic you created in step 3 of [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").
    * Change `role-ARN` to the ARN of the IAM
     service role you created in step 7 of [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").

If you are accessing the CLI on a Windows device, use double
quotes instead of single quotes and escape the inner double quotes
by backslash (i.e. \) to address any parser errors you may
encounter. For an example, see below:

```
aws rekognition start-text-detection --video \
 "{\"S3Object\":{\"Bucket\":\"amzn-s3-demo-bucket\",\"Name\":\"video-name\"}}" \
 --notification-channel "{\"SNSTopicArn\":\"topic-arn\",\"RoleArn\":\"role-arn\"}" \
 --region region-name --profile profile-name
```

After running the proceeding code example, copy down the returned
`jobID` and provide it to the following
`GetTextDetection` command below to get your results,
replacing `job-id-number` with the `jobID` you
previously received:

```
aws rekognition get-text-detection --job-id job-id-number --profile profile-name
```

###### Note

If you've already run a video example other than [Analyzing a video stored in an Amazon S3
bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md"), the code to replace might be
different. 3. Run the code. Text that was detected in the video is shown in a list.

## Filters

Filters are optional request parameters that can be used when you call
`StartTextDetection`. Filtering by text region, size and confidence
score provides you with additional flexibility to control your text detection
output. By using regions of interest, you an easily limit text detection to the
regions that are relevant, for example, a bottom third region for graphics or a top
left corner for reading scoreboards in a soccer game. Word bounding box size filter
can be used to avoid small background text which may be noisy or irrelevant. And
lastly, word confidence filter enables you to remove results that may be unreliable
due to being blurry or smudged.

For information regarding filter values, see `DetectTextFilters`.

You can use the following filters:

- **MinConfidence** –Sets the confidence
  level of word detection. Words with detection confidence below this level
  are excluded from the result. Values should be between 0 and 100.
- **MinBoundingBoxWidth** – Sets the
  minimum width of the word bounding box. Words with bounding boxes that are
  smaller than this value are excluded from the result. The value is relative
  to the video frame width.
- **MinBoundingBoxHeight** – Sets the
  minimum height of the word bounding box. Words with bounding box heights
  less than this value are excluded from the result. The value is relative to
  the video frame height.
- **RegionsOfInterest** – Limits
  detection to a specific region of the frame. The values are relative to the
  frame dimensions. For objects only partially within the regions, the
  response is undefined.

## GetTextDetection response

`GetTextDetection` returns an array (`TextDetectionResults`)
that contains information about the text detected in the video. An array element,
[TextDetection](../APIReference/API_TextDetection.md "../APIReference/API_TextDetection.md"), exists
for each time a word or line is detected in the video. The array elements are sorted
by time (in milliseconds) since the start of the video.

The following is a partial JSON response from `GetTextDetection`. In
the response, note the following:

- **Text information** – The
  `TextDetectionResult` array element contains information
  about the detected text ([TextDetection](../APIReference/API_TextDetection.md "../APIReference/API_TextDetection.md"))
  and the time that the text was
  detected in the video (`Timestamp`).
- **Paging information** – The example
  shows one page of text detection information. You can specify how many text
  elements to return in the `MaxResults` input parameter for
  `GetTextDetection`. If more results than
  `MaxResults` exist, or there are more results than the
  default maximum, `GetTextDetection` returns a token
  (`NextToken`) that's used to get the next page of results.
  For more information, see [Getting Amazon Rekognition Video analysis results](api-video.md#api-video-get "api-video.md#api-video-get").
- **Video information** – The response
  includes information about the video format (`VideoMetadata`) in
  each page of information that's returned by
  `GetTextDetection`.

```

{
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 174441,
        "Format": "QuickTime / MOV",
        "FrameRate": 29.970029830932617,
        "FrameHeight": 480,
        "FrameWidth": 854
    },
    "TextDetections": [
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Twinkle Twinkle Little Star",
                "Type": "LINE",
                "Id": 0,
                "Confidence": 99.91780090332031,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.8337579369544983,
                        "Height": 0.08365312218666077,
                        "Left": 0.08313830941915512,
                        "Top": 0.4663468301296234
                    },
                    "Polygon": [
                        {
                            "X": 0.08313830941915512,
                            "Y": 0.4663468301296234
                        },
                        {
                            "X": 0.9168962240219116,
                            "Y": 0.4674469828605652
                        },
                        {
                            "X": 0.916861355304718,
                            "Y": 0.5511001348495483
                        },
                        {
                            "X": 0.08310343325138092,
                            "Y": 0.5499999523162842
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Twinkle",
                "Type": "WORD",
                "Id": 1,
                "ParentId": 0,
                "Confidence": 99.98338317871094,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.2423887550830841,
                        "Height": 0.0833333358168602,
                        "Left": 0.08313817530870438,
                        "Top": 0.46666666865348816
                    },
                    "Polygon": [
                        {
                            "X": 0.08313817530870438,
                            "Y": 0.46666666865348816
                        },
                        {
                            "X": 0.3255269229412079,
                            "Y": 0.46666666865348816
                        },
                        {
                            "X": 0.3255269229412079,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.08313817530870438,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Twinkle",
                "Type": "WORD",
                "Id": 2,
                "ParentId": 0,
                "Confidence": 99.982666015625,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.2423887550830841,
                        "Height": 0.08124999701976776,
                        "Left": 0.3454332649707794,
                        "Top": 0.46875
                    },
                    "Polygon": [
                        {
                            "X": 0.3454332649707794,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.5878220200538635,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.5878220200538635,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.3454332649707794,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Little",
                "Type": "WORD",
                "Id": 3,
                "ParentId": 0,
                "Confidence": 99.8787612915039,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.16627635061740875,
                        "Height": 0.08124999701976776,
                        "Left": 0.6053864359855652,
                        "Top": 0.46875
                    },
                    "Polygon": [
                        {
                            "X": 0.6053864359855652,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.7716627717018127,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.7716627717018127,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.6053864359855652,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Star",
                "Type": "WORD",
                "Id": 4,
                "ParentId": 0,
                "Confidence": 99.82640075683594,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.12997658550739288,
                        "Height": 0.08124999701976776,
                        "Left": 0.7868852615356445,
                        "Top": 0.46875
                    },
                    "Polygon": [
                        {
                            "X": 0.7868852615356445,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.9168618321418762,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.9168618321418762,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.7868852615356445,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        }
    ],
    "NextToken": "NiHpGbZFnkM/S8kLcukMni15wb05iKtquu/Mwc+Qg1LVlMjjKNOD0Z0GusSPg7TONLe+OZ3P",
    "TextModelVersion": "3.0"
}

```
