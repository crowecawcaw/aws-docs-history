# Getting Started with Multiple Hosts in IVS

This document takes you through the steps involved in getting started using multiple hosts in Amazon IVS.

## Console Instructions

To create a new stage and a participant token for it, follow these steps:

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").

(You can also access the Amazon IVS console through the [AWS Management
Console](https://console.aws.amazon.com "https://console.aws.amazon.com").) 2. On the left navigation pane, select **Stages**, then select **Create
stage**. The **Create stage**
window appears.

![Use the Create stage window to create a new stage and a participant token for it.](images/Create_Stage_Console_IPR.png) 3. Optionally enter a **Stage name**. Select
**Create stage** to create the stage. The
stage details page appears, for the new stage. 4. Select **Create a participant token**. 5. In the **Create a participant token** dialog,
enter a User ID and select **Create a participant
token**. The token appears at the top of the **Participant tokens** table. Click the "Copy token"
icon (to the left of the participant token) to copy the token.

## CLI Instructions

Using the AWS CLI is an advanced option and requires that you first download and
configure the CLI on your machine. For details, see the [AWS
Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

Now you can use the CLI to create and manage resources. The stage API is under the
ivs-realtime namespace. For example, to create a stage:

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

To create a participant token for that stage:

```
aws ivs-realtime create-participant-token --stage-arn arn:aws:ivs:us-west-2:376666121854:stage/VSWjvX5XOkU3
```

The response is:

```
{
   "participant": {
      "participantId": "jFpWmveENolS",
      "expirationTime": "2022-08-26T19:17:00+00:00",
      "token": "eyJhbGciOiJLTVMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE1NDE0MjAsImp0aSI6ImpGcFdtdmVFTm9sUyIsInJlc291cmNlIjoiYXJuOmF3czppdnM6dXMtd2VzdC0yOjM3NjY2NjEyMTg1NDpzdGFnZS9NbzhPUWJ0RGpS123JldmVudHNfdXJsIjoid3NzOi8vdXMtd2VzdC0yLmV2ZW50cy5saXZlLXZpZGVvLm5ldCIsIndoaXBfdXJsIjoiaHR0cHM6Ly82NmY3NjVhYzgzNzcuZ2xvYmFsLndoaXAubGl2ZS12aWRlby5uZXQiLCJjYXBhYmlsaXRpZXMiOnsiYWxsb3dfcHVibGlzaCI6dHJ1ZSwiYWxsb3dfc3Vic2NyaWJlIjp0cnVlfX0.MGQCMGm9affqE3B2MAb_DSpEm0XEv25hfNNhYn5Um4U37FTpmdc3QzQKTKGF90swHqVrDgIwcHHHIDY3c9eanHyQmcKskR1hobD0Q9QK_GQETMQS54S-TaKjllW9Qac6c5xBrdAk"
   }
}
```
