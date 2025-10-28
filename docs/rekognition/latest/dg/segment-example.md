# Example: Detecting segments in a stored video

The following procedure shows how to detect technical cue segments and shot detection
segments in a video stored in an Amazon S3 bucket. The procedure also shows how to filter
detected segments based on the confidence that Amazon Rekognition Video has in the accuracy of the
detection.

The example expands on the code in [Analyzing a video stored in an Amazon S3
bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md") which uses an Amazon Simple Queue Service queue to get the
completion status of a video analysis request.

###### To detect segments in a video stored in an Amazon S3 bucket (SDK)

1. Perform [Analyzing a video stored in an Amazon S3
   bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md").
2. Add the following to the code that you used in step 1.

Java

    1. Add the following imports.



    ```
    import com.amazonaws.services.rekognition.model.GetSegmentDetectionRequest;
    import com.amazonaws.services.rekognition.model.GetSegmentDetectionResult;
    import com.amazonaws.services.rekognition.model.SegmentDetection;
    import com.amazonaws.services.rekognition.model.SegmentType;
    import com.amazonaws.services.rekognition.model.SegmentTypeInfo;
    import com.amazonaws.services.rekognition.model.ShotSegment;
    import com.amazonaws.services.rekognition.model.StartSegmentDetectionFilters;
    import com.amazonaws.services.rekognition.model.StartSegmentDetectionRequest;
    import com.amazonaws.services.rekognition.model.StartSegmentDetectionResult;
    import com.amazonaws.services.rekognition.model.StartShotDetectionFilter;
    import com.amazonaws.services.rekognition.model.StartTechnicalCueDetectionFilter;
    import com.amazonaws.services.rekognition.model.TechnicalCueSegment;
    import com.amazonaws.services.rekognition.model.AudioMetadata;

    ```
    2. Add the following code to the class
     `VideoDetect`.



    ```
        //Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
        //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)


        private static void StartSegmentDetection(String bucket, String video) throws Exception{

            NotificationChannel channel= new NotificationChannel()
                    .withSNSTopicArn(snsTopicArn)
                    .withRoleArn(roleArn);

            float minTechnicalCueConfidence = 80F;
            float minShotConfidence = 80F;

            StartSegmentDetectionRequest req = new StartSegmentDetectionRequest()
                    .withVideo(new Video()
                            .withS3Object(new S3Object()
                                    .withBucket(bucket)
                                    .withName(video)))
                    .withSegmentTypes("TECHNICAL_CUE" , "SHOT")
                    .withFilters(new StartSegmentDetectionFilters()
                            .withTechnicalCueFilter(new StartTechnicalCueDetectionFilter()
                                    .withMinSegmentConfidence(minTechnicalCueConfidence))
                            .withShotFilter(new StartShotDetectionFilter()
                                    .withMinSegmentConfidence(minShotConfidence)))
                    .withJobTag("DetectingVideoSegments")
                    .withNotificationChannel(channel);

            StartSegmentDetectionResult startLabelDetectionResult = rek.startSegmentDetection(req);
            startJobId=startLabelDetectionResult.getJobId();

        }

        private static void GetSegmentDetectionResults() throws Exception{

            int maxResults=10;
            String paginationToken=null;
            GetSegmentDetectionResult segmentDetectionResult=null;
            Boolean firstTime=true;


            do {
                if (segmentDetectionResult !=null){
                    paginationToken = segmentDetectionResult.getNextToken();
                }

                GetSegmentDetectionRequest segmentDetectionRequest= new GetSegmentDetectionRequest()
                        .withJobId(startJobId)
                        .withMaxResults(maxResults)
                        .withNextToken(paginationToken);

                segmentDetectionResult = rek.getSegmentDetection(segmentDetectionRequest);

                if(firstTime) {
                    System.out.println("\nStatus\n------");
                    System.out.println(segmentDetectionResult.getJobStatus());
                    System.out.println("\nRequested features\n------------------");
                     for (SegmentTypeInfo requestedFeatures : segmentDetectionResult.getSelectedSegmentTypes()) {
                        System.out.println(requestedFeatures.getType());
                    }
                     int count=1;
                     List<VideoMetadata> videoMetaDataList = segmentDetectionResult.getVideoMetadata();
                     System.out.println("\nVideo Streams\n-------------");
                     for (VideoMetadata videoMetaData: videoMetaDataList) {
                         System.out.println("Stream: " + count++);
                         System.out.println("\tFormat: " + videoMetaData.getFormat());
                         System.out.println("\tCodec: " + videoMetaData.getCodec());
                         System.out.println("\tDuration: " + videoMetaData.getDurationMillis());
                         System.out.println("\tFrameRate: " + videoMetaData.getFrameRate());
                     }


                     List<AudioMetadata> audioMetaDataList = segmentDetectionResult.getAudioMetadata();
                     System.out.println("\nAudio streams\n-------------");

                     count=1;
                     for (AudioMetadata audioMetaData: audioMetaDataList) {
                         System.out.println("Stream: " + count++);
                         System.out.println("\tSample Rate: " + audioMetaData.getSampleRate());
                         System.out.println("\tCodec: " + audioMetaData.getCodec());
                         System.out.println("\tDuration: " + audioMetaData.getDurationMillis());
                         System.out.println("\tNumber of Channels: " + audioMetaData.getNumberOfChannels());
                     }
                     System.out.println("\nSegments\n--------");

                    firstTime=false;
                }


                //Show segment information

                List<SegmentDetection> detectedSegments= segmentDetectionResult.getSegments();

                for (SegmentDetection detectedSegment: detectedSegments) {

                   if (detectedSegment.getType().contains(SegmentType.TECHNICAL_CUE.toString())) {
                        System.out.println("Technical Cue");
                        TechnicalCueSegment segmentCue=detectedSegment.getTechnicalCueSegment();
                        System.out.println("\tType: " + segmentCue.getType());
                        System.out.println("\tConfidence: " + segmentCue.getConfidence().toString());
                    }
                   if (detectedSegment.getType().contains(SegmentType.SHOT.toString())) {
                        System.out.println("Shot");
                        ShotSegment segmentShot=detectedSegment.getShotSegment();
                        System.out.println("\tIndex " + segmentShot.getIndex());
                        System.out.println("\tConfidence: " + segmentShot.getConfidence().toString());
                    }
                    long seconds=detectedSegment.getDurationMillis();
                    System.out.println("\tDuration : " + Long.toString(seconds) + " milliseconds");
                    System.out.println("\tStart time code: " + detectedSegment.getStartTimecodeSMPTE());
                    System.out.println("\tEnd time code: " + detectedSegment.getEndTimecodeSMPTE());
                    System.out.println("\tDuration time code: " + detectedSegment.getDurationSMPTE());
                    System.out.println();

                 }

            } while (segmentDetectionResult !=null && segmentDetectionResult.getNextToken() != null);

        }

    ```
    3. In the function `main`, replace the lines:



    ```
            StartLabelDetection(amzn-s3-demo-bucket, video);

            if (GetSQSMessageSuccess()==true)
            	GetLabelDetectionResults();
    ```

    with:



    ```
            StartSegmentDetection(amzn-s3-demo-bucket, video);

            if (GetSQSMessageSuccess()==true)
            	GetSegmentDetectionResults();
    ```

Java V2

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
public class DetectVideoSegments {

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

     Region region = Region.US_WEST_2;
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

    1. Add the following code to the class
     `VideoDetect` that you created in step
     1.



    ```
    # Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
    # PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

        def StartSegmentDetection(self):

            min_Technical_Cue_Confidence = 80.0
            min_Shot_Confidence = 80.0
            max_pixel_threshold = 0.1
            min_coverage_percentage = 60

            response = self.rek.start_segment_detection(
                Video={"S3Object": {"Bucket": self.bucket, "Name": self.video}},
                NotificationChannel={
                    "RoleArn": self.roleArn,
                    "SNSTopicArn": self.snsTopicArn,
                },
                SegmentTypes=["TECHNICAL_CUE", "SHOT"],
                Filters={
                    "TechnicalCueFilter": {
                        "BlackFrame": {
                            "MaxPixelThreshold": max_pixel_threshold,
                            "MinCoveragePercentage": min_coverage_percentage,
                        },
                        "MinSegmentConfidence": min_Technical_Cue_Confidence,
                    },
                    "ShotFilter": {"MinSegmentConfidence": min_Shot_Confidence},
                }
            )

            self.startJobId = response["JobId"]
            print(f"Start Job Id: {self.startJobId}")

        def GetSegmentDetectionResults(self):
            maxResults = 10
            paginationToken = ""
            finished = False
            firstTime = True

            while finished == False:
                response = self.rek.get_segment_detection(
                    JobId=self.startJobId, MaxResults=maxResults, NextToken=paginationToken
                )

                if firstTime == True:
                    print(f"Status\n------\n{response['JobStatus']}")
                    print("\nRequested Types\n---------------")
                    for selectedSegmentType in response['SelectedSegmentTypes']:
                        print(f"\tType: {selectedSegmentType['Type']}")
                        print(f"\t\tModel Version: {selectedSegmentType['ModelVersion']}")

                    print()
                    print("\nAudio metadata\n--------------")
                    for audioMetadata in response['AudioMetadata']:
                        print(f"\tCodec: {audioMetadata['Codec']}")
                        print(f"\tDuration: {audioMetadata['DurationMillis']}")
                        print(f"\tNumber of Channels: {audioMetadata['NumberOfChannels']}")
                        print(f"\tSample rate: {audioMetadata['SampleRate']}")
                    print()
                    print("\nVideo metadata\n--------------")
                    for videoMetadata in response["VideoMetadata"]:
                        print(f"\tCodec: {videoMetadata['Codec']}")
                        print(f"\tColor Range: {videoMetadata['ColorRange']}")
                        print(f"\tDuration: {videoMetadata['DurationMillis']}")
                        print(f"\tFormat: {videoMetadata['Format']}")
                        print(f"\tFrame rate: {videoMetadata['FrameRate']}")
                        print("\nSegments\n--------")

                    firstTime = False

                for segment in response['Segments']:

                    if segment["Type"] == "TECHNICAL_CUE":
                        print("Technical Cue")
                        print(f"\tConfidence: {segment['TechnicalCueSegment']['Confidence']}")
                        print(f"\tType: {segment['TechnicalCueSegment']['Type']}")

                    if segment["Type"] == "SHOT":
                        print("Shot")
                        print(f"\tConfidence: {segment['ShotSegment']['Confidence']}")
                        print(f"\tIndex: " + str(segment["ShotSegment"]["Index"]))

                    print(f"\tDuration (milliseconds): {segment['DurationMillis']}")
                    print(f"\tStart Timestamp (milliseconds): {segment['StartTimestampMillis']}")
                    print(f"\tEnd Timestamp (milliseconds): {segment['EndTimestampMillis']}")

                    print(f"\tStart timecode: {segment['StartTimecodeSMPTE']}")
                    print(f"\tEnd timecode: {segment['EndTimecodeSMPTE']}")
                    print(f"\tDuration timecode: {segment['DurationSMPTE']}")

                    print(f"\tStart frame number {segment['StartFrameNumber']}")
                    print(f"\tEnd frame number: {segment['EndFrameNumber']}")
                    print(f"\tDuration frames: {segment['DurationFrames']}")

                    print()

                if "NextToken" in response:
                    paginationToken = response["NextToken"]
                else:
                    finished = True
    ```
    2. In the function `main`, replace the
     lines:



    ```
        analyzer.StartLabelDetection()
        if analyzer.GetSQSMessageSuccess()==True:
            analyzer.GetLabelDetectionResults()
    ```

    with:



    ```
        analyzer.StartSegmentDetection()
        if analyzer.GetSQSMessageSuccess()==True:
            analyzer.GetSegmentDetectionResults()
    ```

###### Note

If you've already run a video example other than [Analyzing a video stored in an Amazon S3
bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md"), the code to replace might be
different. 3. Run the code. Information about the segments detected in the input video are
displayed.
