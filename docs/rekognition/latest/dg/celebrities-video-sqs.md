# Recognizing celebrities in a stored video

Amazon Rekognition Video celebrity recognition in stored videos is an asynchronous operation.
To recognize celebrities in a stored video,
use [StartCelebrityRecognition](../APIReference/API_StartCelebrityRecognition.md "../APIReference/API_StartCelebrityRecognition.md")
to start video analysis. Amazon Rekognition Video publishes the
completion status of the video analysis to an Amazon Simple Notification Service topic. If the video analysis is succesful,
call [GetCelebrityRecognition](../APIReference/API_GetCelebrityRecognition.md "../APIReference/API_GetCelebrityRecognition.md").
to get the analysis results. For more information about starting video analysis and getting the results,
see [Calling Amazon Rekognition Video operations](api-video.md "api-video.md").

This procedure expands on the code in [Analyzing a video stored in an Amazon S3
bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md"), which uses an Amazon SQS queue to get the
completion status of a video analysis request. To run this procedure, you need a
video file that contains one or more celebrity faces.

###### To detect celebrities in a video stored in an Amazon S3 bucket (SDK)

1. Perform [Analyzing a video stored in an Amazon S3
   bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md").
2. Add the following code to the class `VideoDetect` that you created in step 1.

Java

```
        //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
        //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

      // Celebrities=====================================================================
      private static void StartCelebrityDetection(String bucket, String video) throws Exception{

            NotificationChannel channel= new NotificationChannel()
                    .withSNSTopicArn(snsTopicArn)
                    .withRoleArn(roleArn);

           StartCelebrityRecognitionRequest req = new StartCelebrityRecognitionRequest()
                 .withVideo(new Video()
                       .withS3Object(new S3Object()
                             .withBucket(bucket)
                             .withName(video)))
                 .withNotificationChannel(channel);



           StartCelebrityRecognitionResult startCelebrityRecognitionResult = rek.startCelebrityRecognition(req);
           startJobId=startCelebrityRecognitionResult.getJobId();

        }

        private static void GetCelebrityDetectionResults() throws Exception{

           int maxResults=10;
           String paginationToken=null;
           GetCelebrityRecognitionResult celebrityRecognitionResult=null;

           do{
              if (celebrityRecognitionResult !=null){
                 paginationToken = celebrityRecognitionResult.getNextToken();
              }
              celebrityRecognitionResult = rek.getCelebrityRecognition(new GetCelebrityRecognitionRequest()
                    .withJobId(startJobId)
                    .withNextToken(paginationToken)
                    .withSortBy(CelebrityRecognitionSortBy.TIMESTAMP)
                    .withMaxResults(maxResults));


              System.out.println("File info for page");
              VideoMetadata videoMetaData=celebrityRecognitionResult.getVideoMetadata();

              System.out.println("Format: " + videoMetaData.getFormat());
              System.out.println("Codec: " + videoMetaData.getCodec());
              System.out.println("Duration: " + videoMetaData.getDurationMillis());
              System.out.println("FrameRate: " + videoMetaData.getFrameRate());

              System.out.println("Job");

              System.out.println("Job status: " + celebrityRecognitionResult.getJobStatus());


              //Show celebrities
              List<CelebrityRecognition> celebs= celebrityRecognitionResult.getCelebrities();

              for (CelebrityRecognition celeb: celebs) {
                 long seconds=celeb.getTimestamp()/1000;
                 System.out.print("Sec: " + Long.toString(seconds) + " ");
                 CelebrityDetail details=celeb.getCelebrity();
                 System.out.println("Name: " + details.getName());
                 System.out.println("Id: " + details.getId());
                 System.out.println();
              }
           } while (celebrityRecognitionResult !=null && celebrityRecognitionResult.getNextToken() != null);

        }

```

In the function `main`, replace the line:

```
        StartLabelDetection(amzn-s3-demo-bucket, video);

        if (GetSQSMessageSuccess()==true)
        	GetLabelDetectionResults();
```

with:

```
        StartCelebrityDetection(amzn-s3-demo-bucket, video);

        if (GetSQSMessageSuccess()==true)
        	GetCelebrityDetectionResults();

```

Java V2
This code is taken from the AWS Documentation SDK examples GitHub repository. See the full example
[here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoCelebrityDetection.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoCelebrityDetection.java").

```
//snippet-start:[rekognition.java2.recognize_video_celebrity.import]
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.S3Object;
import software.amazon.awssdk.services.rekognition.model.NotificationChannel;
import software.amazon.awssdk.services.rekognition.model.Video;
import software.amazon.awssdk.services.rekognition.model.StartCelebrityRecognitionResponse;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.CelebrityRecognitionSortBy;
import software.amazon.awssdk.services.rekognition.model.VideoMetadata;
import software.amazon.awssdk.services.rekognition.model.CelebrityRecognition;
import software.amazon.awssdk.services.rekognition.model.CelebrityDetail;
import software.amazon.awssdk.services.rekognition.model.StartCelebrityRecognitionRequest;
import software.amazon.awssdk.services.rekognition.model.GetCelebrityRecognitionRequest;
import software.amazon.awssdk.services.rekognition.model.GetCelebrityRecognitionResponse;
import java.util.List;
//snippet-end:[rekognition.java2.recognize_video_celebrity.import]

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

public class RecognizeCelebritiesVideo {

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

  StartCelebrityDetection(rekClient, channel, bucket, video);
  GetCelebrityDetectionResults(rekClient);
  System.out.println("This example is done!");
  rekClient.close();
}

// snippet-start:[rekognition.java2.recognize_video_celebrity.main]
public static void StartCelebrityDetection(RekognitionClient rekClient,
                                           NotificationChannel channel,
                                           String bucket,
                                           String video){
   try {
       S3Object s3Obj = S3Object.builder()
           .bucket(bucket)
           .name(video)
           .build();

       Video vidOb = Video.builder()
           .s3Object(s3Obj)
           .build();

       StartCelebrityRecognitionRequest recognitionRequest = StartCelebrityRecognitionRequest.builder()
           .jobTag("Celebrities")
           .notificationChannel(channel)
           .video(vidOb)
           .build();

       StartCelebrityRecognitionResponse startCelebrityRecognitionResult = rekClient.startCelebrityRecognition(recognitionRequest);
       startJobId = startCelebrityRecognitionResult.jobId();

   } catch(RekognitionException e) {
       System.out.println(e.getMessage());
       System.exit(1);
   }
}

public static void GetCelebrityDetectionResults(RekognitionClient rekClient) {

   try {
       String paginationToken=null;
       GetCelebrityRecognitionResponse recognitionResponse = null;
       boolean finished = false;
       String status;
       int yy=0 ;

       do{
           if (recognitionResponse !=null)
               paginationToken = recognitionResponse.nextToken();

           GetCelebrityRecognitionRequest recognitionRequest = GetCelebrityRecognitionRequest.builder()
               .jobId(startJobId)
               .nextToken(paginationToken)
               .sortBy(CelebrityRecognitionSortBy.TIMESTAMP)
               .maxResults(10)
               .build();

           // Wait until the job succeeds
           while (!finished) {
               recognitionResponse = rekClient.getCelebrityRecognition(recognitionRequest);
               status = recognitionResponse.jobStatusAsString();

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
           VideoMetadata videoMetaData=recognitionResponse.videoMetadata();
           System.out.println("Format: " + videoMetaData.format());
           System.out.println("Codec: " + videoMetaData.codec());
           System.out.println("Duration: " + videoMetaData.durationMillis());
           System.out.println("FrameRate: " + videoMetaData.frameRate());
           System.out.println("Job");

           List<CelebrityRecognition> celebs= recognitionResponse.celebrities();
           for (CelebrityRecognition celeb: celebs) {
               long seconds=celeb.timestamp()/1000;
               System.out.print("Sec: " + seconds + " ");
               CelebrityDetail details=celeb.celebrity();
               System.out.println("Name: " + details.name());
               System.out.println("Id: " + details.id());
               System.out.println();
           }

       } while (recognitionResponse.nextToken() != null);

   } catch(RekognitionException | InterruptedException e) {
       System.out.println(e.getMessage());
       System.exit(1);
   }
}
// snippet-end:[rekognition.java2.recognize_video_celebrity.main]
}
```

Python

```
#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

    # ============== Celebrities ===============
    def StartCelebrityDetection(self):
        response=self.rek.start_celebrity_recognition(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
            NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn})

        self.startJobId=response['JobId']
        print('Start Job Id: ' + self.startJobId)

    def GetCelebrityDetectionResults(self):
        maxResults = 10
        paginationToken = ''
        finished = False

        while finished == False:
            response = self.rek.get_celebrity_recognition(JobId=self.startJobId,
                                                    MaxResults=maxResults,
                                                    NextToken=paginationToken)

            print(response['VideoMetadata']['Codec'])
            print(str(response['VideoMetadata']['DurationMillis']))
            print(response['VideoMetadata']['Format'])
            print(response['VideoMetadata']['FrameRate'])

            for celebrityRecognition in response['Celebrities']:
                print('Celebrity: ' +
                    str(celebrityRecognition['Celebrity']['Name']))
                print('Timestamp: ' + str(celebrityRecognition['Timestamp']))
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
    analyzer.StartCelebrityDetection()
    if analyzer.GetSQSMessageSuccess()==True:
        analyzer.GetCelebrityDetectionResults()
```

Node.JS
In the following Node.Js code example, replace the value of
`amzn-s3-demo-bucket` with the name of the S3 bucket containing
your video and the value of `videoName` with the name of
the video file. You'll also need to replace the value of
`roleArn` with the Arn associated with your IAM
service role. Finally, replace the value of `region` with
the name of the operating region associated with your account.
Replace the value of `profile_name` in the line that creates the Rekognition
session with the name of your developer profile.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

// Import required AWS SDK clients and commands for Node.js
import { CreateQueueCommand, GetQueueAttributesCommand, GetQueueUrlCommand,
  SetQueueAttributesCommand, DeleteQueueCommand, ReceiveMessageCommand, DeleteMessageCommand } from  "@aws-sdk/client-sqs";
import {CreateTopicCommand, SubscribeCommand, DeleteTopicCommand } from "@aws-sdk/client-sns";
import  { SQSClient } from "@aws-sdk/client-sqs";
import  { SNSClient } from "@aws-sdk/client-sns";
import  { RekognitionClient, StartLabelDetectionCommand, GetLabelDetectionCommand,
  StartCelebrityRecognitionCommand, GetCelebrityRecognitionCommand} from "@aws-sdk/client-rekognition";
import { stdout } from "process";
import {fromIni} from '@aws-sdk/credential-providers';

// Set the AWS Region.
const REGION = "region-name"; //e.g. "us-east-1"
// Set the profile name
const profileName = "profile-name"
// Name the collection
// Create SNS service object.
const sqsClient = new SQSClient({ region: REGION,
  credentials: fromIni({profile: profileName,}), });
const snsClient = new SNSClient({ region: REGION,
  credentials: fromIni({profile: profileName,}), });
const rekClient = new RekognitionClient({region: REGION,
  credentials: fromIni({profile: profileName,}),
});

// Set bucket and video variables
const bucket = "bucket-name";
const videoName = "video-name";
const roleArn = "role-arn"
var startJobId = ""

var ts = Date.now();
const snsTopicName = "AmazonRekognitionExample" + ts;
const snsTopicParams = {Name: snsTopicName}
const sqsQueueName = "AmazonRekognitionQueue-" + ts;

 // Set the parameters
 const sqsParams = {
  QueueName: sqsQueueName, //SQS_QUEUE_URL
  Attributes: {
    DelaySeconds: "60", // Number of seconds delay.
    MessageRetentionPeriod: "86400", // Number of seconds delay.
  },
};

const createTopicandQueue = async () => {
  try {
    // Create SNS topic
    const topicResponse = await snsClient.send(new CreateTopicCommand(snsTopicParams));
    const topicArn = topicResponse.TopicArn
    console.log("Success", topicResponse);
    // Create SQS Queue
    const sqsResponse = await sqsClient.send(new CreateQueueCommand(sqsParams));
    console.log("Success", sqsResponse);
    const sqsQueueCommand = await sqsClient.send(new GetQueueUrlCommand({QueueName: sqsQueueName}))
    const sqsQueueUrl = sqsQueueCommand.QueueUrl
    const attribsResponse = await sqsClient.send(new GetQueueAttributesCommand({QueueUrl: sqsQueueUrl, AttributeNames: ['QueueArn']}))
    const attribs = attribsResponse.Attributes
    console.log(attribs)
    const queueArn = attribs.QueueArn
    // subscribe SQS queue to SNS topic
    const subscribed = await snsClient.send(new SubscribeCommand({TopicArn: topicArn, Protocol:'sqs', Endpoint: queueArn}))
    const policy = {
      Version: "2012-10-17",&TCX5-2025-waiver;
      Statement: [
        {
          Sid: "MyPolicy",
          Effect: "Allow",
          Principal: {AWS: "*"},
          Action: "SQS:SendMessage",
          Resource: queueArn,
          Condition: {
            ArnEquals: {
              'aws:SourceArn': topicArn
            }
          }
        }
      ]
    };

    const response = sqsClient.send(new SetQueueAttributesCommand({QueueUrl: sqsQueueUrl, Attributes: {Policy: JSON.stringify(policy)}}))
    console.log(response)
    console.log(sqsQueueUrl, topicArn)
    return [sqsQueueUrl, topicArn]

  } catch (err) {
    console.log("Error", err);
  }
};

const startCelebrityDetection = async(roleArn, snsTopicArn) =>{
  try {
      //Initiate label detection and update value of startJobId with returned Job ID
      const response = await rekClient.send(new StartCelebrityRecognitionCommand({Video:{S3Object:{Bucket:bucket, Name:videoName}},
          NotificationChannel:{RoleArn: roleArn, SNSTopicArn: snsTopicArn}}))
          startJobId = response.JobId
          console.log(`Start Job ID: ${startJobId}`)
          return startJobId
    } catch (err) {
      console.log("Error", err);
    }
  };

const getCelebrityRecognitionResults = async(startJobId) =>{
  try {
      //Initiate label detection and update value of startJobId with returned Job ID
      var maxResults = 10
      var paginationToken = ''
      var finished = false

      while (finished == false){
          var response = await rekClient.send(new GetCelebrityRecognitionCommand({JobId: startJobId, MaxResults: maxResults,
              NextToken: paginationToken}))
          console.log(response.VideoMetadata.Codec)
          console.log(response.VideoMetadata.DurationMillis)
          console.log(response.VideoMetadata.Format)
          console.log(response.VideoMetadata.FrameRate)
          response.Celebrities.forEach(celebrityRecognition => {
              console.log(`Celebrity: ${celebrityRecognition.Celebrity.Name}`)
              console.log(`Timestamp: ${celebrityRecognition.Timestamp}`)
              console.log()
          })
          // Searh for pagination token, if found, set variable to next token
          if (String(response).includes("NextToken")){
              paginationToken = response.NextToken

          }else{
              finished = true
          }
      }
    } catch (err) {
      console.log("Error", err);
    }
  };

// Checks for status of job completion
const getSQSMessageSuccess = async(sqsQueueUrl, startJobId) => {
  try {
    // Set job found and success status to false initially
    var jobFound = false
    var succeeded = false
    var dotLine = 0
    // while not found, continue to poll for response
    while (jobFound == false){
      var sqsReceivedResponse = await sqsClient.send(new ReceiveMessageCommand({QueueUrl:sqsQueueUrl,
        MaxNumberOfMessages:'ALL', MaxNumberOfMessages:10}));
      if (sqsReceivedResponse){
        var responseString = JSON.stringify(sqsReceivedResponse)
        if (!responseString.includes('Body')){
          if (dotLine < 40) {
            console.log('.')
            dotLine = dotLine + 1
          }else {
            console.log('')
            dotLine = 0
          };
          stdout.write('', () => {
            console.log('');
          });
          await new Promise(resolve => setTimeout(resolve, 5000));
          continue
        }
      }

      // Once job found, log Job ID and return true if status is succeeded
      for (var message of sqsReceivedResponse.Messages){
        console.log("Retrieved messages:")
        var notification = JSON.parse(message.Body)
        var rekMessage = JSON.parse(notification.Message)
        var messageJobId = rekMessage.JobId
        if (String(rekMessage.JobId).includes(String(startJobId))){
          console.log('Matching job found:')
          console.log(rekMessage.JobId)
          jobFound = true
          console.log(rekMessage.Status)
          if (String(rekMessage.Status).includes(String("SUCCEEDED"))){
            succeeded = true
            console.log("Job processing succeeded.")
            var sqsDeleteMessage = await sqsClient.send(new DeleteMessageCommand({QueueUrl:sqsQueueUrl, ReceiptHandle:message.ReceiptHandle}));
          }
        }else{
          console.log("Provided Job ID did not match returned ID.")
          var sqsDeleteMessage = await sqsClient.send(new DeleteMessageCommand({QueueUrl:sqsQueueUrl, ReceiptHandle:message.ReceiptHandle}));
        }
      }
    }
  return succeeded
  } catch(err) {
    console.log("Error", err);
  }
};

// Start label detection job, sent status notification, check for success status
// Retrieve results if status is "SUCEEDED", delete notification queue and topic
const runCelebRecognitionAndGetResults = async () => {
  try {
    const sqsAndTopic = await createTopicandQueue();
    //const startLabelDetectionRes = await startLabelDetection(roleArn, sqsAndTopic[1]);
    //const getSQSMessageStatus = await getSQSMessageSuccess(sqsAndTopic[0], startLabelDetectionRes)
    const startCelebrityDetectionRes = await startCelebrityDetection(roleArn, sqsAndTopic[1]);
    const getSQSMessageStatus = await getSQSMessageSuccess(sqsAndTopic[0], startCelebrityDetectionRes)
    console.log(getSQSMessageSuccess)
    if (getSQSMessageSuccess){
      console.log("Retrieving results:")
      const results = await getCelebrityRecognitionResults(startCelebrityDetectionRes)
    }
    const deleteQueue = await sqsClient.send(new DeleteQueueCommand({QueueUrl: sqsAndTopic[0]}));
    const deleteTopic = await snsClient.send(new DeleteTopicCommand({TopicArn: sqsAndTopic[1]}));
    console.log("Successfully deleted.")
  } catch (err) {
    console.log("Error", err);
  }
};

runCelebRecognitionAndGetResults()
```

CLI
Run the following AWS CLI command to start detecting celebrities in
a video.

```
aws rekognition start-celebrity-recognition --video "{"S3Object":{"Bucket":"amzn-s3-demo-bucket","Name":"video-name"}}" \
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
aws rekognition start-celebrity-recognition --video "{\"S3Object\":{\"Bucket\":\"amzn-s3-demo-bucket\",\"Name\":\"video-name\"}}" \
--notification-channel "{\"SNSTopicArn\":\"topic-arn\",\"RoleArn\":\"role-arn\"}" \
--region region-name --profile profile-name

```

After running the proceeding code example, copy down the returned
`jobID` and provide it to the following
`GetCelebrityRecognition` command below to get your
results, replacing `job-id-number` with the
`jobID` you previously received:

```
aws rekognition get-celebrity-recognition --job-id job-id-number --profile profile-name

```

###### Note

If you've already run a video example other than [Analyzing a video stored in an Amazon S3
bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md"), the code to replace
might be different. 3. Run the code. Information about the celebrities recognized in the video is shown.

## GetCelebrityRecognition operation response

The following is an example JSON response. The response includes the following:

- **Recognized celebrities** –
  `Celebrities` is an array of celebrities and the times that
  they are recognized in a video. A
  [CelebrityRecognition](../APIReference/API_CelebrityRecognition.md "../APIReference/API_CelebrityRecognition.md")
  object exists for each time
  the celebrity is recognized in the video. Each
  `CelebrityRecognition` contains information about a
  recognized celebrity ([CelebrityDetail](../APIReference/API_CelebrityDetail.md "../APIReference/API_CelebrityDetail.md"))
  and the time
  (`Timestamp`) the celebrity was recognized in the video.
  `Timestamp` is measured in milliseconds from the start of the
  video.
- **CelebrityDetail** – Contains
  information about a recognized celebrity. It includes the celebrity name
  (`Name`), identifier (`ID`), the celebrity's
  known gender(`KnownGender`), and a list of URLs pointing to
  related content (`Urls`). It also includes the confidence level
  that Amazon Rekognition Video has in the accuracy of the recognition, and details about the
  celebrity's face, [FaceDetail](../APIReference/API_FaceDetail.md "../APIReference/API_FaceDetail.md"). If you need to get the related content
  later, you can use `ID` with [getCelebrityInfo](../APIReference/API_GetCelebrityInfo.md "../APIReference/API_GetCelebrityInfo.md").
- **VideoMetadata** – Information about the video that was analyzed.

```
{
    "Celebrities": [
        {
            "Celebrity": {
                "Confidence": 0.699999988079071,
                "Face": {
                    "BoundingBox": {
                        "Height": 0.20555555820465088,
                        "Left": 0.029374999925494194,
                        "Top": 0.22333332896232605,
                        "Width": 0.11562500149011612
                    },
                    "Confidence": 99.89837646484375,
                    "Landmarks": [
                        {
                            "Type": "eyeLeft",
                            "X": 0.06857934594154358,
                            "Y": 0.30842265486717224
                        },
                        {
                            "Type": "eyeRight",
                            "X": 0.10396526008844376,
                            "Y": 0.300625205039978
                        },
                        {
                            "Type": "nose",
                            "X": 0.0966852456331253,
                            "Y": 0.34081998467445374
                        },
                        {
                            "Type": "mouthLeft",
                            "X": 0.075217105448246,
                            "Y": 0.3811396062374115
                        },
                        {
                            "Type": "mouthRight",
                            "X": 0.10744428634643555,
                            "Y": 0.37407416105270386
                        }
                    ],
                    "Pose": {
                        "Pitch": -0.9784082174301147,
                        "Roll": -8.808176040649414,
                        "Yaw": 20.28228759765625
                    },
                    "Quality": {
                        "Brightness": 43.312068939208984,
                        "Sharpness": 99.9305191040039
                    }
                },
                "Id": "XXXXXX",
                "KnownGender": {
                    "Type": "Female"
                },
                "Name": "Celeb A",
                "Urls": []
            },
            "Timestamp": 367
       },......
    ],
    "JobStatus": "SUCCEEDED",
    "NextToken": "XfXnZKiyMOGDhzBzYUhS5puM+g1IgezqFeYpv/H/+5noP/LmM57FitUAwSQ5D6G4AB/PNwolrw==",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 67301,
        "FileExtension": "mp4",
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 29.970029830932617,
        "FrameWidth": 1920
    }
}
```
