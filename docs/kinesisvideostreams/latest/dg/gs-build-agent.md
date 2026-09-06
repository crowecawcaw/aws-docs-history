

# Build the Amazon Kinesis Video Streams Edge Agent
<a name="gs-build-agent"></a>

**Build the Amazon Kinesis Video Streams Edge Agent**

1. Download the `tar` file using the link that was provided to you.

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
The jar included with the `kvs-edge-agent.tar.gz` does not have the dependencies. Use the following steps to build those libraries.

   Navigate to the `kvs-edge-agent` folder that contains `pom.xml`. 

   Type `mvn clean package`.

   This generates a jar file containing the dependencies the Amazon Kinesis Video Streams Edge Agent requires at `kvs-edge-agent/target/libs.jar`.

1. Place the `libs.jar` into the folder that contains the component's artifacts.

   Type `mv ./target/libs.jar ./KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}/`.

1. Set environment variables using the values from previous steps. The following table provides descriptions for the variables.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-build-agent.html)

1. Clear the GStreamer cache. Type:

   ```
   rm ~/.cache/gstreamer-1.0/registry.{{your-os-architecture}}.bin
   ```

   For more information, see the [GStreamer registry documentation](https://gstreamer.freedesktop.org/documentation/gstreamer/gstregistry.html?gi-language=c).

1. Prepare and run the java command. The Amazon Kinesis Video Streams Edge Agent accepts the following arguments:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-build-agent.html)

   To set these, add `-D{{java-property-name}}={{value}}` to the java command used to run the jar.

   For example:

   ```
   java -Djava.library.path=/{{download-location}}/kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}} \
     --add-opens java.base/jdk.internal.misc=ALL-UNNAMED \
     -Dio.netty.tryReflectionSetAccessible=true \
     -cp kvs-edge-agent.jar:libs.jar \
     com.amazonaws.kinesisvideo.edge.controller.ControllerApp
   ```
**Important**  
Run the java command above from the same directory as `/{{download-location}}/kvs-edge-agent/KvsEdgeComponent/artifacts/aws.kinesisvideo.KvsEdgeComponent/{{EdgeAgentVersion}}`.

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

   1. To send the file to the Amazon Kinesis Video Streams Edge Agent, type the following in the AWS CLI:

      ```
      aws kinesisvideo start-edge-configuration-update --cli-input-json "file://{{example-edge-configuration}}.json"
      ```

1. Repeat the previous step for each stream for the Amazon Kinesis Video Streams Edge Agent.