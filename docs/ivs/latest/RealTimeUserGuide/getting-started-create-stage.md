# Step 2: Create a Stage with Optional

Participant Recording

A stage is a virtual space where participants can exchange video in real time. It is
the foundational resource of the Real-Time Streaming API. You can create a stage using
either the console or the CreateStage operation.

We recommend that where possible, you create a new stage for each logical session and
delete it when done, rather than keeping around old stages for possible reuse. If stale
resources (old stages, not to be reused) are not cleaned up, you're likely to hit the
limit of the maximum number of stages faster.

You can create a stage — with or without individual participant recording — through
the Amazon IVS console or the AWS CLI. Stage creation and recording are discussed
below.

## Individual Participant

Recording

You have the option of enabling individual participant recording for a stage. If
the individual participant recording to S3 feature is enabled, all individual
participant broadcasts to the stage are recorded and saved to an Amazon S3 storage
bucket that you own. Subsequently, the recording is available for on-demand
playback.

_Setting this up is an advanced option._ By default, recording
is disabled when a stage is created.

Before you can set up a stage for recording, you must create a _storage
configuration_. This is a resource which specifies an Amazon S3
location where the recorded streams for the stage are stored. You can create and
manage storage configurations using the console or CLI; both procedures are given
below. After you create the storage configuration, you associate it with a stage
either when you create the stage (as described below) or later, by updating an
existing stage. (In the API, see [CreateStage](../RealTimeAPIReference/API_CreateStage.md "../RealTimeAPIReference/API_CreateStage.md") and [UpdateStage](../RealTimeAPIReference/API_UpdateStage.md "../RealTimeAPIReference/API_UpdateStage.md").) You can associate multiple stages with the same storage
configuration. You can delete a storage configuration that is no longer associated
with any stages.

Keep in mind the following constraints:

- You must own the S3 bucket. That is, the account that sets up a stage to
  be recorded must own the S3 bucket where recordings will be stored.
- The stage, storage configuration, and S3 location must be in the same
  AWS region. If you create stages in other regions and want to record them,
  you must also set up storage configurations and S3 buckets in those
  regions.

Recording to your S3 bucket requires authorization with your AWS credentials. To
give IVS the required access, an AWS IAM [Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") (SLR) is created automatically when the recording
configuration is created: the SLR is limited to give IVS write permission only on
the specific bucket.

Note that network issues between the streaming location and AWS or within AWS
could result in some data loss while recording your stream. In these cases, Amazon
IVS prioritizes the live stream over the recording. For redundancy, record locally
via your streaming tool.

For more information (including how to set up post-processing or VOD playback on
your recorded files), see [Individual Participant Recording](rt-individual-participant-recording.md "rt-individual-participant-recording.md").

### How to Disable

Recording

To disable Amazon S3 recording on an existing stage:

- Console — On the details page for the relevant stage, in the
  **Record individual participants**
  streams section, toggle off **Enable automatic
  recording** under **Auto-record to
  S3** and then choose **Save
  changes**. This removes the storage configuration’s
  association with the stage; streams on that stage will no longer be
  recorded.
- CLI — Run the `update-stage` command and pass in the
  recording-configuration ARN as an empty string:

```
aws ivs-realtime update-stage --arn arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh --auto-participant-recording-configuration storageConfigurationArn=""
```

This returns a stage object with an empty string for
`storageConfigurationArn`, indicating that the
recording is disabled.

## Console Instructions for

Creating an IVS Stage

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").

(You also can access the Amazon IVS console through the [AWS Management
Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").) 2. On the left navigation pane, select **Stages**, then select **Create
stage**. The **Create stage**
window appears.

![Use the Create stage window to create a new stage and a participant token for it.](images/Create_Stage_Console_IPR.png) 3. Optionally enter a **Stage name**. 4. If you want to enable individual participant recording, complete the steps
in [Set Up Automatic
Individual Participant Recording to Amazon S3 (Optional)](#getting-started-create-stage-ipr "#getting-started-create-stage-ipr")
below. 5. Select **Create stage** to create the stage.
The stage details page appears, for the new stage.

### Set Up Automatic Individual

Participant Recording to Amazon S3 (Optional)

Follow these steps to enable individual participant recording while creating a
stage:

1. On the **Create stage** page, under
   **Record individual participants**,
   turn on **Enable automatic recording**.
   Additional fields display, to choose **Recorded
   media types**, to choose an existing **Storage configuration** or create a new one, and to choose
   whether to record thumbnails at an interval.

![Use the Record individual participants dialog to configure individual participant recording for a stage.](images/Create_Stage_Console_enable_IPR.png) 2. Choose which media types to record. 3. Choose **Create storage configuration**.
A new window opens, with options for creating an Amazon S3 bucket and
attaching it to the new recording configuration.

![Use the Create storage configuration window to create a new storage configuration for a stage.](images/Create_Storage_Configuration_IPR.png) 4. Fill out the fields:

    1. Optionally enter a **Storage configuration
     name**.
    2. Enter a **Bucket name**.

5. Choose **Create storage configuration**,
   to create a new storage-configuration resource with a unique ARN.
   Typically, creation of the recording configuration takes a few seconds,
   but it can be up to 20 seconds. When the storage configuration is
   created, you are returned to the **Create
   stage** window. There, the **Record
   individual participants** area shows your new **Storage configuration** and the S3 bucket
   (**Storage**) that you created.

![Create a stage using the IVS Console: New storage configuration created.](images/Create_Stage_Console_Storage_Configuration.png) 6. You can optionally enable other non-default options such as recording participant replicas,
merging individual participant recordings, and thumbnail recording.

![Create a stage using the IVS Console: enable advanced options like thumbnail recording and IPR stitching.](images/Create_Stage_Console_IPR_Stitching.png)

## CLI Instructions for Creating an

IVS Stage

To install the AWS CLI, see [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

Now you can use the CLI to create and manage resources following one of the two
procedures below, depending on whether you want to create a stage with or without
individual participant recording enabled.

### Create a Stage

without Individual Participant Recording

The stage API is under the ivs-realtime namespace. For example, to create a
stage:

```
aws ivs-realtime create-stage --name "test-stage"
```

The response is:

```
{
   "stage": {
      "arn": "arn:aws:ivs:us-west-2:376666121854:stage/VSWjvX5XOkU3",
      "name": "test-stage"
   }
}
```

### Create a Stage with

Individual Participant Recording

To create a stage with individual participant recording enabled:

```
aws ivs-realtime create-stage --name "test-stage-participant-recording" --auto-participant-recording-configuration storageConfigurationArn=arn:aws:ivs:us-west-2:123456789012:storage-configuration/LKZ6QR7r55c2,mediaTypes=AUDIO_VIDEO
```

Optionally, pass the `thumbnailConfiguration` parameter to manually
set the thumbnail storage and recording mode, and thumbnail interval
seconds:

```
aws ivs-realtime create-stage --name "test-stage-participant-recording" --auto-participant-recording-configuration storageConfigurationArn=arn:aws:ivs:us-west-2:123456789012:storage-configuration/LKZ6QR7r55c2,mediaTypes=AUDIO_VIDEO,thumbnailConfiguration="{targetIntervalSeconds=10,storage=[SEQUENTIAL,LATEST],recordingMode=INTERVAL}"
```

Optionally, pass the `recordingReconnectWindowSeconds` parameter to
enable merge fragmented individual participant recordings:

```
aws ivs-realtime create-stage --name "test-stage-participant-recording" --auto-participant-recording-configuration "storageConfigurationArn=arn:aws:ivs:us-west-2:123456789012:storage-configuration/LKZ6QR7r55c2,mediaTypes=AUDIO_VIDEO,thumbnailConfiguration="{targetIntervalSeconds=10,storage=[SEQUENTIAL,LATEST],recordingMode=INTERVAL}",recordingReconnectWindowSeconds=60"
```

The response is:

```
{
   "stage": {
      "arn": "arn:aws:ivs:us-west-2:123456789012:stage/VSWjvX5XOkU3",
      "autoParticipantRecordingConfiguration": {
         "hlsConfiguration": {
             "targetSegmentDurationSeconds": 6
         },
         "mediaTypes": [
            "AUDIO_VIDEO"
         ],
         "recordingReconnectWindowSeconds": 60,
         "recordParticipantReplicas": true,
         "storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/LKZ6QR7r55c2",
         "thumbnailConfiguration": {
            "recordingMode": "INTERVAL",
            "storage": [
               "SEQUENTIAL",
               "LATEST"
            ],
            "targetIntervalSeconds": 10
         }
      },
      "endpoints": {
         "events": "<events-endpoint>",
         "rtmp": "<rtmp-endpoint>",
         "rtmps": "<rtmps-endpoint>",
         "whip": "<whip-endpoint>"
      },
      "name": "test-stage-participant-recording"
   }
}
```
