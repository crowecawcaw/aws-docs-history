

# Deploy the Amazon Kinesis Video Streams Edge Agent AWS IoT Greengrass component on the device
<a name="gs-deploy-edge"></a>

Do the following to deploy the Amazon Kinesis Video Streams Edge Agent AWS IoT Greengrass component on the device:

**Deploy the component**

1. Download the `tar` file using the provided link.

   If you completed the Amazon Kinesis Video Streams Edge Agent interest form, check your email for the download link. If you haven't completed the form, complete it [here](https://pages.awscloud.com/GLOBAL-launch-DL-KVS-Edge-2023-learn.html).

1. Verify the checksum.

1. Extract the binaries and jar in your device.

   Type: `tar -xvf kvs-edge-agent.tar.gz`.

   After extraction, your folder structure will look like the following:

   ```
   kvs-edge-agent/LICENSE
   kvs-edge-agent/THIRD-PARTY-LICENSES
   kvs-edge-agent/pom.xml
   kvs-edge-agent/KvsEdgeComponent
   kvs-edge-agent/KvsEdgeComponent/recipes
   kvs-edge-agent/KvsEdgeComponent/recipes/recipe.yaml
   kvs-edge-agent/KvsEdgeComponent/artifacts
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/edge_log_config                   
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/kvs-edge-agent.jar
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/libgstkvssink.so
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/libIngestorPipelineJNI.so
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/lib
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/lib/libcproducer.so
   kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/lib/libKinesisVideoProducer.so
   ```
**Note**  
The release folder name should be set up in a way that reflects the latest binary release number. For example, a 1.0.0 release will have the folder name set as 1.0.0. 

1. Build the dependencies jar. 
**Note**  
The jar included with the kvs-edge-agent.tar.gz does not have the dependencies. Use the following steps to build those libraries.

   Navigate to the `kvs-edge-agent` folder that contains `pom.xml`. 

   Type `mvn clean package`.

   This will generate a jar file containing the dependencies the Amazon Kinesis Video Streams Edge Agent requires at `kvs-edge-agent/target/libs.jar`.

1. Place the libs.jar into the folder that contains the component’s artifacts.

   Type `mv ./target/libs.jar ./KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/`.

1. **Optional.** Configure properties. The Amazon Kinesis Video Streams Edge Agent accepts the following environment variables in AWS IoT Greengrass mode:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-deploy-edge.html)

   Open `kvs-edge-agent/KvsEdgeComponent/recipes/recipe.yaml` and modify the run script to add any of the preceding environment variables.
**Important**  
Make sure that the modified run script doesn't contain any **tab** characters. The AWS IoT Greengrass core software won't be able to read the recipe.

1. Deploy the Amazon Kinesis Video Streams Edge Agent AWS IoT Greengrass component. 

   Type:

   ```
   sudo /greengrass/v2/bin/greengrass-cli deployment create \
     --recipeDir <download location>/kvs-edge-agent/KvsEdgeComponent/recipes/ \
     --artifactDir <download location>/kvs-edge-agent/KvsEdgeComponent/artifacts/ \
     --merge "aws.kinesisvideo.KvsEdgeComponent={{EdgeAgentVersion}}"
   ```

   For additional information, see the following sections in the *AWS IoT Greengrass Version 2 Developer Guide*:
   + [AWS IoT Greengrass CLI commands](https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-cli-reference.html)
   + [Deploy AWS IoT Greengrass components to devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html)

1. Send configurations to the application using the AWS CLI.

   1. Create a new file, `{{example-edge-configuration}}.json`. 

      Paste the following code into the file. This is a sample configuration that records daily from 9:00:00 AM to 4:59:59 PM (according to the system time on your AWS IoT device). It also uploads the recorded media daily from 7:00:00 PM to 9:59:59 PM.

      For more information, see [StartEdgeConfigurationUpdate](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_StartEdgeConfigurationUpdate.html).

      ```
      {
          "StreamARN": "arn:aws:kinesisvideo:{{your-region}}:{{your-account-id}}:stream/{{your-stream}}/{{0123456789012}}",
          "EdgeConfig": {
              "HubDeviceArn": "arn:aws:iot:{{your-region}}:{{your-account-id}}:thing/{{kvs-edge-agent-demo}}",
              "RecorderConfig": {
                  "MediaSourceConfig": {
                      "MediaUriSecretArn": "arn:aws:secretsmanager:{{your-region}}:{{your-account-id}}:secret:{{your-secret}}-{{dRbHJQ}}",
                      "MediaUriType": "RTSP_URI"
                  },
                  "ScheduleConfig": {
                      "ScheduleExpression": "0 0 9,10,11,12,13,14,15,16 ? * * *",
                      "DurationInSeconds": 3599
                  }
              },
              "UploaderConfig": {
                  "ScheduleConfig": {
                      "ScheduleExpression": "0 0 19,20,21 ? * * *",
                      "DurationInSeconds": 3599
                  }
              },
              "DeletionConfig": {
                  "EdgeRetentionInHours": 15,
                  "LocalSizeConfig": {
                    "MaxLocalMediaSizeInMB": 2800,
                    "StrategyOnFullSize": "DELETE_OLDEST_MEDIA"
                  },
                  "DeleteAfterUpload": true
              }
          }
      }
      ```

   1. Type the following in the AWS CLI to send the file to the Amazon Kinesis Video Streams Edge Agent:

      ```
      aws kinesisvideo start-edge-configuration-update --cli-input-json "file://{{example-edge-configuration}}.json"
      ```

1. Repeat the previous step for each stream for the Amazon Kinesis Video Streams Edge Agent.