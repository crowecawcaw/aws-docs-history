

# Test a canary locally
<a name="CloudWatch_Synthetics_Debug_Locally"></a>

This section explains how to modify, test, and debug CloudWatch Synthetics canaries directly within the Microsoft Visual Studio code editor or the JetBrains IDE code editor. The local debugging environment uses a Serverless Application Model (SAM) container to simulate a Lambda function to emulate the behavior of a Synthetics canary. 

**Note**  
It is impractical to perform locally debug canaries that rely on visual monitoring. Visual monitoring rely on capturing base screenshots during an initial run, and then comparing these screenshots to the screenshots from subsequent runs. In a local development environment, runs are not stored or tracked, and each iteration is an independent, standalone run. The absence of a canary run history makes it impractical to debug canaries that rely on visual monitoring.

 **Prerequisites** 

1. Choose or create an Amazon S3 bucket to use to store artifacts from local canary test runs, such as HAR files and screenshots. This requires you to be provisioned with IAM. If you skip setting up Amazon S3 buckets you can still test your canary locally, but you will see an error message about the missing bucket and you won't have access to canary artifacts.

   If you use an Amazon S3 bucket, we recommend that you set the bucket lifecycle to delete objects after a few days, to save costs. For more information, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).

1. Set up a default AWS profile for your AWS account. For more information, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

1. Set the debug environment's default AWS Region to your preferred Region, such as ` us-west-2`.

1. Install the AWS SAM CLI. For more information, see [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

1. Install Visual Studio Code Editor or JetBrains IDE. For more information, see [Visual Studio Code](https://code.visualstudio.com/) or [JetBrains IDE](https://www.jetbrains.com/ides/)

1. Install Docker to work with the AWS SAM CLI. Make sure to start the docker daemon. For more information, see [Installing  Docker to use with the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html).

   Alternatively, You can install other container management software such as  Rancher, as long as it uses the Docker runtime.

1. Install an AWS toolkit extension for your preferred editor. For more information, see [Installing the AWS Toolkit for Visual Studio Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html) or [Installing the AWS Toolkit for JetBrains](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/setup-toolkit.html).

**Topics**
+ [Set up the testing and debugging environment](#CloudWatch_Synthetics_Debug_Environment)
+ [Use Visual Studio Code IDE](#CloudWatch_Synthetics_Debug_VS)
+ [Use JetBrains IDE](#CloudWatch_Synthetics_Debug_JetBrains)
+ [Run a canary locally with the SAM CLI](#CloudWatch_Synthetics_Run_Locally)
+ [Integrate your local testing environment into an existing canary package](#CloudWatch_Synthetics_Debug_Integrate)
+ [Change the CloudWatch Synthetics runtime](#CloudWatch_Synthetics_Debug_DifferentRuntime)
+ [Common errors](#CloudWatch_Synthetics_Debug_Errors)

## Set up the testing and debugging environment
<a name="CloudWatch_Synthetics_Debug_Environment"></a>

First, clone the Github repository that AWS provides by entering the following command. The repository contains code samples for both Node.js canaries and Python canaries. 

```
git clone https://github.com/aws-samples/synthetics-canary-local-debugging-sample.git
```

Then do one of the following, depending on the language of your canaries.

**For Node.js canaries**

1. Go to the Node.js canary source directory by entering the following command.

   ```
   cd synthetics-canary-local-debugging-sample/nodejs-canary/src
   ```

1. Enter the following command to install canary dependencies.

   ```
   npm install
   ```

**For Python canaries**

1. Go to the Python canary source directory by entering the following command.

   ```
   cd synthetics-canary-local-debugging-sample/python-canary/src
   ```

1. Enter the following command to install canary dependencies.

   ```
   pip3 install -r requirements.txt -t .
   ```

## Use Visual Studio Code IDE
<a name="CloudWatch_Synthetics_Debug_VS"></a>

The Visual Studio launch configuration file is located at ` .vscode/launch.json`. It contains configurations to allow the template file to be discovered by Visual Studio code. It defines a Lambda payload with required parameters to invoke the canary successfully. Here's the launch configuration for a Node.js canary: 

```
{
            ...
            ...
            "lambda": {
                "payload": {
                    "json": {
                        // Canary name. Provide any name you like.
                        "canaryName": "LocalSyntheticsCanary",
                        // Canary artifact location
                        "artifactS3Location": {
                            "s3Bucket": "cw-syn-results-123456789012-us-west-2",
                            "s3Key": "local-run-artifacts",
                        },
                        // Your canary handler name
                        "customerCanaryHandlerName": "heartbeat-canary.handler"
                    }
                },
                // Environment variables to pass to the canary code
                "environmentVariables": {}
            }
        }
    ]
}
```

You can also optionally provide the following fields in the payload JSON:
+ `s3EncryptionMode` Valid values: `SSE_S3` \| `SSE_KMS`
+ `s3KmsKeyArn` Valid value: {{KMS Key ARN}}
+ `activeTracing` Valid values: `true` \| `false`
+ `canaryRunId` Valid value: {{UUID}} This parameter is required if active tracing is enabled.

To debug the canary in Visual Studio, add breakpoints in the canary code where you want to pause execution. To add a breakpoint, choose the editor margin and go to **Run and Debug** mode in the editor. Run the canary by clicking on the play button. When the canary runs, the logs will be tailed in the debug console, providing you with real-time insights into the canary's behavior. If you added breakpoints, the canary execution will pause at each breakpoint, allowing you to step through code and inspect variable values, instance methods, object attributes, and the function call stack.

There is no cost incurred for running and debugging canaries locally, except for the artifacts stored in the Amazon S3 bucket and the CloudWatch metrics generated by each local run.

![Visual Studio Code interface showing JavaScript code for a heartbeat canary function.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/DebugCanaryVS.png)


## Use JetBrains IDE
<a name="CloudWatch_Synthetics_Debug_JetBrains"></a>

After you have the AWS Toolkit for JetBrains extension installed, be sure that the Node.js plugin and JavaScript debugger are enabled to run, if you are debugging a Node.js canary. Then follow these steps.

**Debug a canary using JetBrains IDE**

1. In the left navigation pane of JetBrains IDE, choose **Lambda**, then choose the local configuration template.

1. Enter a name for the run configuration, such as **LocalSyntheticsCanary**

1. Choose **From template**, choose the file browser in the template field, then select the **template.yml** file from the project, either from the **nodejs** directory or the **python** directory.

1. In the **Input** section, enter the payload for the canary as shown in the following screen.

   ```
   {
    "canaryName": "LocalSyntheticsCanary",
    "artifactS3Location": {
        "s3Bucket": "cw-syn-results-123456789012-us-west-2",
        "s3Key": "local-run-artifacts"
    },
    "customerCanaryHandlerName": "heartbeat-canary.handler"
   }
   ```

   You can also set other environment variables in the payload JSON, as listed in [Use Visual Studio Code IDE](#CloudWatch_Synthetics_Debug_VS).

![Run/Debug Configurations interface for AWS Lambda with LocalSyntheticsCanary settings.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/DebugCanaryIntellij.png)


## Run a canary locally with the SAM CLI
<a name="CloudWatch_Synthetics_Run_Locally"></a>

Use the one of the following procedures to run your canary locally using the Serverless Application Model (SAM) CLI. Be sure to specify your own Amazon S3 bucket name for `s3Bucket` in `event.json`

**To use the SAM CLI to run a Node.js canary**

1. Go to the source directory by entering the following command.

   ```
   cd synthetics-canary-local-debugging-sample/nodejs-canary
   ```

1. Enter the following commands.

   ```
   sam build
   sam local invoke -e ../event.json
   ```

**To use the SAM CLI to run a Python canary**

1. Go to the source directory by entering the following command.

   ```
   cd synthetics-canary-local-debugging-sample/python-canary
   ```

1. Enter the following commands.

   ```
   sam build
   sam local invoke -e ../event.json
   ```

## Integrate your local testing environment into an existing canary package
<a name="CloudWatch_Synthetics_Debug_Integrate"></a>

You can integrate local canary debugging into your existing canary package by copying three files:
+ Copy the `template.yml` file into your canary package root. Be sure to modify the path for `CodeUri` to point to the directory where your canary code exists.
+ If you're working with a Node.js canary, copy the `cw-synthetics.js` file to your canary source directory. If you're working with a Python canary, copy the ` cw-synthetics.py` to your canary source directory.
+ Copy the launch configuration file .`vscode/launch.json` into the package root. Make sure to put it inside the `.vscode` directory; create it if it doesn't exist already.

## Change the CloudWatch Synthetics runtime
<a name="CloudWatch_Synthetics_Debug_DifferentRuntime"></a>

As part of your debugging, you might want to try running a canary with a different CloudWatch Synthetics runtime, instead of the latest runtime. To do so, find the runtime that you want to use from one of the following tables. Be sure to select the runtime for the correct Region. Then paste the ARN for that runtime into the appropriate place in your ` template.yml` file, and then run the canary.

### Node.js and Puppeteer runtimes
<a name="Synthetics_NodeJS_Puppeteer_Runtime_ARNs"></a>

#### ARNs for syn-nodejs-puppeteer-17.0
<a name="syn-nodejs-puppeteer-17.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-17.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:23` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:85` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:85` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:58` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:65` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:39` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:56` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:39` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:23` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:69` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:86` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:87` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:46` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:30` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:114` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:84` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:84` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:58` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:57` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:55` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:31` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:50` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:84` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:78` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:79` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 



#### ARNs for syn-nodejs-puppeteer-16.1
<a name="syn-nodejs-puppeteer-16.1"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-16.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:84` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:84` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:57` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:38` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:55` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:38` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:22` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:85` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:86` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:45` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:29` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:113` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:57` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:56` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:54` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:30` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:78` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 



#### ARNs for syn-nodejs-puppeteer-16.0
<a name="syn-nodejs-puppeteer-16.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-16.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:56` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:63` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:37` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:54` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:37` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:21` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:84` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:85` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:44` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:112` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:56` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:55` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:53` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:29` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 



#### ARNs for syn-nodejs-puppeteer-15.1
<a name="syn-nodejs-puppeteer-15.1"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-15.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:79` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:82` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:55` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:62` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:36` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:53` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:36` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:20` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:66` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:83` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:84` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:79` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:43` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:27` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:111` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:79` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:79` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:55` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:54` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:52` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:28` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:81` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:19` 



#### ARNs for syn-nodejs-puppeteer-15.0
<a name="syn-nodejs-puppeteer-15.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-15.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:78` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:78` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:51` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:58` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:32` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:49` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:32` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:16` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:62` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:79` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:80` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:39` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:23` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:107` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:51` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:50` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:48` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 



#### ARNs for syn-nodejs-puppeteer-14.0
<a name="syn-nodejs-puppeteer-14.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-14.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:50` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:57` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:31` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:48` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:31` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:15` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:61` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:78` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:79` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:38` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:22` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:106` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:50` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:49` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:47` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:23` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:50` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:70` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 



#### ARNs for syn-nodejs-puppeteer-13.1
<a name="syn-nodejs-puppeteer-13.1"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-13.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:49` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:56` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:30` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:47` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:30` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:14` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:60` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:77` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:78` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:37` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:105` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:49` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:48` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:46` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:22` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:49` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:69` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:70` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:13` 



#### ARNs for syn-nodejs-puppeteer-13.0
<a name="syn-nodejs-puppeteer-13.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-13.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:74` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:47` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:54` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:28` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:45` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:28` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:12` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:58` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:75` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:76` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:35` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:103` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:47` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:46` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:44` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:47` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:73` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:11` 



#### ARNs for syn-nodejs-puppeteer-12.0
<a name="syn-nodejs-puppeteer-12.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-12.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:70` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:70` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:490290609897:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:865491513039:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:43` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:378461160691:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:50` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:490290609897:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:654654156625:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:41` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:491585149102:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:565803892007:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:8` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:54` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:865491513039:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:71` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:296224022648:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:72` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:960282847306:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:635750524965:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:31` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:654654156625:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:15` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:654654156625:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:213485871058:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:99` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:453652488670:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:69` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:69` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:282507446575:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:43` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:378461160691:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:42` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:378461160691:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:40` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:378461160691:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:16` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:491585149102:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:43` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:491585149102:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:69` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:756306329178:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:63` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:488211338238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:488211338238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:7` 



#### ARNs for syn-nodejs-puppeteer-11.0
<a name="syn-nodejs-puppeteer-11.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-11.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:63` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:66` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:66` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:39` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:46` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:37` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:4` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:50` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:67` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:68` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:63` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:27` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:11` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:95` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:63` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:65` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:63` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:65` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:39` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:64` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:38` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:36` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:12` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:63` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:39` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:65` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:59` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:60` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPuppeteer-Firefox:3` 



#### ARNs for syn-nodejs-puppeteer-10.0
<a name="syn-nodejs-puppeteer-10.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-10.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:58`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:61`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:59`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:61`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:59`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:59`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:34`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:41`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:15`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:32`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:59`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:18`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:45`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:62`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:63`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:58`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:24`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:6`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:59`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:59`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:90`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:58`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:59`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:59`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:60`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:58`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:60`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:59`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:34`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:59`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:33`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:31`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:7`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:58`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:34`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:60`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:54`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:55`  | 

#### ARNs for syn-nodejs-puppeteer-9.1
<a name="syn-nodejs-puppeteer-9.1"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-9.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:53`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:56`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:54`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:56`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:54`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:54`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:29`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:36`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:10`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:27`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:54`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:17`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:40`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:57`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:58`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:53`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:25`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:1`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:54`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:54`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:85`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:54`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:55`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:54`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:55`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:53`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:55`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:54`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:29`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:54`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:28`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:26`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:3`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:53`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:29`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:55`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:50`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:51`  | 

#### ARNs for syn-nodejs-puppeteer-9.0
<a name="syn-nodejs-puppeteer-9.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-9.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:51`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:54`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:52`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:54`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:52`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:52`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:27`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:34`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:8`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:25`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:52`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:16`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:38`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:55`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:56`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:51`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:26`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:52`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:52`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:83`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:52`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:53`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:52`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:53`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:51`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:53`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:52`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:27`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:52`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:26`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:24`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:51`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:27`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:53`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:48`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:49`  | 

#### ARNs for syn-nodejs-puppeteer-8.0
<a name="syn-nodejs-puppeteer-8.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-8.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:48`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:50`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:48`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:51`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:48`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:49`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:24`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:30`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:22`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:48`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics:15`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:34`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:51`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:53`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:48`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics:23`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:48`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:48`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:80`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:49`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:50`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:48`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:50`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:48`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:49`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:48`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:24`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:48`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:23`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:21`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:48`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:23`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:49`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:45`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:46`  | 

#### ARNs for syn-nodejs-puppeteer-7.0
<a name="syn-nodejs-puppeteer-7.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-7.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:44`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:46`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:44`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:47`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:44`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:45`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:20`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:26`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics:7`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:18`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:44`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:30`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:46`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:49`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:44`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics:3`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:44`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:44`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:76`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:45`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:46`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:44`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:46`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:44`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:45`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:44`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:20`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:44`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:19`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:17`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics:4`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:44`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:19`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:45`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:41`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:42`  | 

#### ARNs for syn-nodejs-puppeteer-6.2
<a name="syn-nodejs-puppeteer-6.2"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-6.2` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:41`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:43`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:41`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:44`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:41`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:42`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:17`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:23`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:15`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:41`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:27`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:42`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:46`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:41`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:41`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:41`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:73`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:42`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:43`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:41`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:43`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:41`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:42`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:41`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:17`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:41`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:16`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:14`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:41`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:16`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:42`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:39`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:39`  | 

#### ARNs for syn-nodejs-puppeteer-5.2
<a name="syn-nodejs-puppeteer-5.2"></a>

The following table lists the ARNs to use for version ` syn-nodejs-puppeteer-5.2` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:42`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:44`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:42`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:45`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:42`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:43`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:18`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:24`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:16`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:42`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:28`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:44`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:47`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:42`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:42`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:42`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:74`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:43`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:44`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:42`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:44`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:42`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:43`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:42`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:18`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:42`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:17`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:15`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:42`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:17`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:43`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:40`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:40`  | 

### Node.js and Playwright runtimes
<a name="Synthetics_Playwright_Runtime_ARNs"></a>

#### ARNs for syn-nodejs-playwright-8.0
<a name="syn-nodejs-playwright-8.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-8.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:29` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:23` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:30` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:29` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:14` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 



#### ARNs for syn-nodejs-playwright-7.1
<a name="syn-nodejs-playwright-7.1"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-7.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:22` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:29` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 



#### ARNs for syn-nodejs-playwright-7.0
<a name="syn-nodejs-playwright-7.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-7.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:21` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:28` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 



#### ARNs for syn-nodejs-playwright-6.1
<a name="syn-nodejs-playwright-6.1"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-6.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:20` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:27` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:26` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:25` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:24` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:19` 



#### ARNs for syn-nodejs-playwright-6.0
<a name="syn-nodejs-playwright-6.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-6.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:22` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:16` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:23` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:22` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:15` 



#### ARNs for syn-nodejs-playwright-5.1
<a name="syn-nodejs-playwright-5.1"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-5.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:14` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:21` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 



#### ARNs for syn-nodejs-playwright-5.0
<a name="syn-nodejs-playwright-5.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-5.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:13` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:20` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:17` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:17` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:17` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:19` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:18` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:17` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:17` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:12` 



#### ARNs for syn-nodejs-playwright-4.0
<a name="syn-nodejs-playwright-4.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-4.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:14` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:8` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:15` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:12` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:12` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:11` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:6` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:14` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:13` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:12` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:12` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:7` 



#### ARNs for syn-nodejs-playwright-3.0
<a name="syn-nodejs-playwright-3.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-3.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.



- ** US East (N. Virginia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** US East (Ohio) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** US West (N. California) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** US West (Oregon) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Africa (Cape Town) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Hong Kong) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Hyderabad) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Jakarta) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Malaysia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Melbourne) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Mumbai) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (New Zealand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:5` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:2` 

- ** Asia Pacific (Osaka) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Seoul) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Singapore) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Sydney) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Taipei) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Thailand) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:6` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Asia Pacific (Tokyo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Canada (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Canada West (Calgary) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** China (Beijing) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:6` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** China (Ningxia) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:6` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (Frankfurt) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (Ireland) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (London) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (Milan) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (Paris) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (Spain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (Stockholm) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Europe (Zurich) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Israel (Tel Aviv) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Mexico (Central) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:8` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Middle East (Bahrain) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** Middle East (UAE) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** South America (São Paulo) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:7` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:1` 

- ** AWS GovCloud (US-East) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:8` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:3` 

- ** AWS GovCloud (US-West) **
  - **Browser:** Chrome / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:8` 
  - **Browser:** Firefox / **ARN:**  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright-Firefox:3` 



#### ARNs for syn-nodejs-playwright-2.0
<a name="syn-nodejs-playwright-2.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-2.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| US East (Ohio) |  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| US West (N. California) |  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| US West (Oregon) |  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Africa (Cape Town) |  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Hong Kong) |  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Hyderabad) |  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Mumbai) |  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:7`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Asia Pacific (Taipei) |  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:9`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:3`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Canada West (Calgary) |  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:3`  | 
| China (Ningxia); |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:3`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Europe (Ireland) |  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Europe (London) |  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Europe (Milan) |  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Europe (Paris) |  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Europe (Spain) |  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Europe (Stockholm) |  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:5`  | 
| Middle East (Bahrain) |  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| Middle East (UAE) |  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| South America (São Paulo) |  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:4`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:3`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:3`  | 

#### ARNs for syn-nodejs-playwright-1.0
<a name="syn-nodejs-playwright-1.0"></a>

The following table lists the ARNs to use for version ` syn-nodejs-playwright-1.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  ` arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| US East (Ohio) |  ` arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| US West (N. California) |  ` arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| US West (Oregon) |  ` arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Africa (Cape Town) |  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Hong Kong) |  ` arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Hyderabad) |  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Mumbai) |  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJsPlaywright:8`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Taipei) |  ` arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJsPlaywright:10`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Canada West (Calgary) |  ` arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| China (Ningxia); |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (Ireland) |  ` arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (London) |  ` arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (Milan) |  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (Paris) |  ` arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (Spain) |  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (Stockholm) |  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJsPlaywright:3`  | 
| Middle East (Bahrain) |  ` arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| Middle East (UAE) |  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| South America (São Paulo) |  ` arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJsPlaywright:1`  | 

### Node.js runtimes
<a name="Synthetics_NodeJS_Runtime_ARNs"></a>

#### ARNs for syn-nodejs-5.2
<a name="syn-nodejs-5.2"></a>

The following table lists the ARNs to use for version ` syn-nodejs-5.2` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJs:10`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:18`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:18`  | 

#### ARNs for syn-nodejs-5.1
<a name="syn-nodejs-5.1"></a>

The following table lists the ARNs to use for version `syn-nodejs-5.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:17`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:17`  | 

#### ARNs for syn-nodejs-5.0
<a name="syn-nodejs-5.0"></a>

The following table lists the ARNs to use for version `syn-nodejs-5.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:16`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:16`  | 

#### ARNs for syn-nodejs-4.2
<a name="syn-nodejs-4.2"></a>

The following table lists the ARNs to use for version `syn-nodejs-4.2` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Africa (Cape Town) |  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Hyderabad) |  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Mumbai) |  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (Milan) |  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (Spain) |  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (Stockholm) |  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:15`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:15`  | 

#### ARNs for syn-nodejs-4.1
<a name="syn-nodejs-4.1"></a>

The following table lists the ARNs to use for version `syn-nodejs-4.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Africa (Cape Town) |  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Hyderabad) |  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Mumbai) |  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (Milan) |  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (Spain) |  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (Stockholm) |  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:12`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:12`  | 

#### ARNs for syn-nodejs-4.0
<a name="syn-nodejs-4.0"></a>

The following table lists the ARNs to use for version `syn-nodejs-4.0` of the CloudWatch Synthetics runtimein each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Africa (Cape Town) |  ` arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Hyderabad) |  ` arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Mumbai) |  ` arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (Milan) |  ` arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (Spain) |  ` arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (Stockholm) |  ` arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:11`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:11`  | 

#### ARNs for syn-nodejs-3.1
<a name="syn-nodejs-3.1"></a>

The following table lists the ARNs to use for version `syn-nodejs-3.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| Middle East (UAE) |  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:9`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:9`  | 

#### ARNs for syn-nodejs-3.0
<a name="syn-nodejs-3.0"></a>

The following table lists the ARNs to use for version `syn-nodejs-3.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| Middle East (UAE) |  ` arn:aws:lambda:me-central-1:239544149032:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:AWS-CW-SyntheticsNodeJs:1`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:AWS-CW-SyntheticsNodeJs:1`  | 

### Python and Selenium runtimes
<a name="Synthetics_Python_Runtime_ARNs"></a>

#### ARNs for syn-python-selenium-12.0
<a name="syn-python-selenium-12.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-12.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:69`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:72`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:70`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:71`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:70`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:69`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:57`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:64`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:39`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:55`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:70`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:45`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:68`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:73`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:74`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:69`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:32`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:30`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:70`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:70`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:113`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:68`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:68`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:70`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:71`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:69`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:71`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:70`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:57`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:70`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:56`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:54`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:31`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:49`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:71`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:66`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:67`  | 

#### ARNs for syn-python-selenium-11.1
<a name="syn-python-selenium-11.1"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-11.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:68`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:71`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:69`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:70`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:69`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:68`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:56`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:63`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:38`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:54`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:69`  | 
| Asia Pacific (New Zealand) |  `arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:44`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:67`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:72`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:73`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:68`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:31`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:29`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:69`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:69`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:112`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:67`  | 
| China (Ningxia) |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:67`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:69`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:70`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:68`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:70`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:69`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:56`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:69`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:55`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:53`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:30`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:70`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:65`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:66`  | 

#### ARNs for syn-python-selenium-11.0
<a name="syn-python-selenium-11.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-11.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:66`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:69`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:67`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:68`  | 
| Africa (Cape Town) |  ` arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:67`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:66`  | 
| Asia Pacific (Hyderabad) |  ` arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:54`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:61`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:36`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:52`  | 
| Asia Pacific (Mumbai) |  ` arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:67`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:42`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:65`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:70`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:71`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:66`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:29`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:27`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:67`  | 
| Canada (Central) |  ` arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:67`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:110`  | 
| China (Beijing) |  ` arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:65`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:65`  | 
| Europe (Frankfurt) |  ` arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:67`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:68`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:66`  | 
| Europe (Milan) |  ` arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:68`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:67`  | 
| Europe (Spain) |  ` arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:54`  | 
| Europe (Stockholm) |  ` arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:67`  | 
| Europe (Zurich) |  ` arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:53`  | 
| Israel (Tel Aviv) |  ` arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:51`  | 
| Mexico (Central) |  ` arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:28`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:68`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:63`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:64`  | 

#### ARNs for syn-python-selenium-10.0
<a name="syn-python-selenium-10.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-10.0` of the CloudWatch Synthetics runtimein each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:62`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:65`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:63`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:64`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:63`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:62`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:50`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:57`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:32`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:48`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:63`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:38`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:61`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:66`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:67`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:62`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:25`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:23`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:63`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:63`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:106`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:61`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:61`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:63`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:64`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:62`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:64`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:63`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:50`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:63`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:49`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:47`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:24`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:64`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:59`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:60`  | 

#### ARNs for syn-python-selenium-9.0
<a name="syn-python-selenium-9.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-9.0` of the CloudWatch Synthetics runtimein each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:61`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:64`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:62`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:63`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:62`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:61`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:49`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:56`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:31`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:47`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:62`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:37`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:60`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:65`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:66`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:61`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:24`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:22`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:62`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:62`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:105`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:60`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:60`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:62`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:63`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:61`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:63`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:62`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:49`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:62`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:48`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:46`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:23`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:61`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:49`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:63`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:58`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:59`  | 

#### ARNs for syn-python-selenium-8.0
<a name="syn-python-selenium-8.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-8.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:57`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:60`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:58`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:59`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:58`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:57`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:45`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:52`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:27`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:43`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:58`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:33`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:56`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:61`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:62`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:57`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:20`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:18`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:58`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:58`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:101`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:56`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:56`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:58`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:59`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:57`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:59`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:58`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:45`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:58`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:44`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:42`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:19`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:57`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:45`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:59`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:54`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:55`  | 

#### ARNs for syn-python-selenium-7.0
<a name="syn-python-selenium-7.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-7.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:49`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:52`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:50`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:51`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:50`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:49`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:37`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:44`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:19`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:35`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:50`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:25`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:48`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:53`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:54`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:49`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:12`  | 
| Asia Pacific (Thailand) |  ` arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:10`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:50`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:50`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:93`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:48`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:48`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:50`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:51`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:49`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:51`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:50`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:37`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:50`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:36`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:34`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:11`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:49`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:37`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:51`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:46`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:47`  | 

#### ARNs for syn-python-selenium-6.0
<a name="syn-python-selenium-6.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-6.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:47`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:50`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:48`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:49`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:48`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:47`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:35`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:42`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:17`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:33`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:48`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:25`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:46`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:51`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:52`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:47`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:10`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:8`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:48`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:48`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:91`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:46`  | 
| China (Ningxia) |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:46`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:48`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:49`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:47`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:49`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:48`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:35`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:48`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:34`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:32`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:9`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:47`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:35`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:49`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:44`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:45`  | 

#### ARNs for syn-python-selenium-5.1
<a name="syn-python-selenium-5.1"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-5.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:45`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:48`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:46`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:47`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:46`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:45`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:33`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:40`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:15`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:31`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:46`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:24`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:44`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:49`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:50`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:45`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:8`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:6`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:46`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:44`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:89`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:44`  | 
| China (Ningxia); |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:44`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:46`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:47`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:45`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:47`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:46`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:33`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:46`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:32`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:30`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:7`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:45`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:33`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:47`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:42`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:43`  | 

#### ARNs for syn-python-selenium-5.0
<a name="syn-python-selenium-5.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-5.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:43`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:46`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:44`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:45`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:44`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:43`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:31`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:38`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:13`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:29`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:44`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:23`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:42`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:47`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:48`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:43`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:3`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:4`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:44`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:44`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:87`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:43`  | 
| China (Ningxia); |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:43`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:44`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:45`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:43`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:45`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:44`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:31`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:44`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:30`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:28`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:5`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:43`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:31`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:45`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:41`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:42`  | 

#### ARNs for syn-python-selenium-4.1
<a name="syn-python-selenium-4.1"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-4.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:40`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:43`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:41`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:42`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:41`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:40`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:28`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:35`  | 
| Asia Pacific (Malaysia) |  ` arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:10`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:26`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:41`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:22`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:39`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:44`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:45`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:40`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:4`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:1`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:41`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:41`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:84`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:40`  | 
| China (Ningxia); |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:40`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:41`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:42`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:40`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:42`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:41`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:28`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:41`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:27`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:25`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:3`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:40`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:28`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:42`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:38`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:39`  | 

#### ARNs for syn-python-selenium-4.0
<a name="syn-python-selenium-4.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-4.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:38`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:41`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:39`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:40`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:39`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:38`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:26`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:33`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:8`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:24`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:39`  | 
| Asia Pacific (New Zealand) |  ` arn:aws:lambda:ap-southeast-6:779414629109:layer:Synthetics_Selenium:21`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:37`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:42`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:43`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:38`  | 
| Asia Pacific (Taipei) |  `arn:aws:lambda:ap-east-2:471112897378:layer:Synthetics_Selenium:5`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:39`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:39`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:82`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:38`  | 
| China (Ningxia); |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:38`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:39`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:40`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:38`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:40`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:39`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:26`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:39`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:25`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:23`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:38`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:26`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:40`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:36`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:37`  | 

#### ARNs for syn-python-selenium-3.0
<a name="syn-python-selenium-3.0"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-3.0` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics_Selenium:32`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics_Selenium:34`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics_Selenium:32`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics_Selenium:34`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics_Selenium:32`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics_Selenium:32`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics_Selenium:20`  | 
| Asia Pacific (Jakarta) |  ` arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics_Selenium:26`  | 
| Asia Pacific (Malaysia) |  `arn:aws:lambda:ap-southeast-5:035872523913:layer:Synthetics_Selenium:7`  | 
| Asia Pacific (Melbourne) |  ` arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics_Selenium:18`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics_Selenium:32`  | 
| Asia Pacific (Osaka) |  ` arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics_Selenium:30`  | 
| Asia Pacific (Seoul) |  ` arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics_Selenium:34`  | 
| Asia Pacific (Singapore) |  ` arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics_Selenium:37`  | 
| Asia Pacific (Sydney) |  ` arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics_Selenium:32`  | 
| Asia Pacific (Thailand) |  `arn:aws:lambda:ap-southeast-7:851725245975:layer:Synthetics_Selenium:3`  | 
| Asia Pacific (Tokyo) |  ` arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics_Selenium:32`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics_Selenium:32`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics_Selenium:76`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics_Selenium:32`  | 
| China (Ningxia); |  ` arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics_Selenium:32`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics_Selenium:32`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics_Selenium:34`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics_Selenium:32`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics_Selenium:33`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics_Selenium:32`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics_Selenium:20`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics_Selenium:32`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics_Selenium:19`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics_Selenium:17`  | 
| Mexico (Central) |  `arn:aws:lambda:mx-central-1:654654265476:layer:Synthetics_Selenium:4`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics_Selenium:32`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics_Selenium:19`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics_Selenium:33`  | 
| AWS GovCloud (US-East) |  ` arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics_Selenium:30`  | 
| AWS GovCloud (US-West) |  ` arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics_Selenium:31`  | 

#### ARNs for syn-python-selenium-2.1
<a name="syn-python-selenium-2.1"></a>

The following table lists the ARNs to use for version ` syn-python-selenium-2.1` of the CloudWatch Synthetics runtime in each AWS Region where it is available.


| Region | ARN | 
| --- | --- | 
| US East (N. Virginia) |  `arn:aws:lambda:us-east-1:378653112637:layer:Synthetics:29`  | 
| US East (Ohio) |  `arn:aws:lambda:us-east-2:772927465453:layer:Synthetics:31`  | 
| US West (N. California) |  `arn:aws:lambda:us-west-1:332033056316:layer:Synthetics:29`  | 
| US West (Oregon) |  `arn:aws:lambda:us-west-2:760325925879:layer:Synthetics:31`  | 
| Africa (Cape Town) |  `arn:aws:lambda:af-south-1:461844272066:layer:Synthetics:29`  | 
| Asia Pacific (Hong Kong) |  `arn:aws:lambda:ap-east-1:129828061636:layer:Synthetics:29`  | 
| Asia Pacific (Hyderabad) |  `arn:aws:lambda:ap-south-2:280298676434:layer:Synthetics:17`  | 
| Asia Pacific (Jakarta) |  `arn:aws:lambda:ap-southeast-3:246953257743:layer:Synthetics:23`  | 
| Asia Pacific (Melbourne) |  `arn:aws:lambda:ap-southeast-4:200724813040:layer:Synthetics:15`  | 
| Asia Pacific (Mumbai) |  `arn:aws:lambda:ap-south-1:724929286329:layer:Synthetics:29`  | 
| Asia Pacific (Osaka) |  `arn:aws:lambda:ap-northeast-3:608016332111:layer:Synthetics:27`  | 
| Asia Pacific (Seoul) |  `arn:aws:lambda:ap-northeast-2:989515803484:layer:Synthetics:30`  | 
| Asia Pacific (Singapore) |  `arn:aws:lambda:ap-southeast-1:068035103298:layer:Synthetics:34`  | 
| Asia Pacific (Sydney) |  `arn:aws:lambda:ap-southeast-2:584677157514:layer:Synthetics:29`  | 
| Asia Pacific (Tokyo) |  `arn:aws:lambda:ap-northeast-1:172291836251:layer:Synthetics:29`  | 
| Canada (Central) |  `arn:aws:lambda:ca-central-1:236629016841:layer:Synthetics:29`  | 
| Canada West (Calgary) |  `arn:aws:lambda:ca-west-1:944448206667:layer:Synthetics:73`  | 
| China (Beijing) |  `arn:aws-cn:lambda:cn-north-1:422629156088:layer:Synthetics:29`  | 
| China (Ningxia); |  `arn:aws-cn:lambda:cn-northwest-1:474974519687:layer:Synthetics:29`  | 
| Europe (Frankfurt) |  `arn:aws:lambda:eu-central-1:122305336817:layer:Synthetics:29`  | 
| Europe (Ireland) |  `arn:aws:lambda:eu-west-1:563204233543:layer:Synthetics:31`  | 
| Europe (London) |  `arn:aws:lambda:eu-west-2:565831452869:layer:Synthetics:29`  | 
| Europe (Milan) |  `arn:aws:lambda:eu-south-1:525618516618:layer:Synthetics:30`  | 
| Europe (Paris) |  `arn:aws:lambda:eu-west-3:469466506258:layer:Synthetics:29`  | 
| Europe (Spain) |  `arn:aws:lambda:eu-south-2:029793053121:layer:Synthetics:17`  | 
| Europe (Stockholm) |  `arn:aws:lambda:eu-north-1:162938142733:layer:Synthetics:29`  | 
| Europe (Zurich) |  `arn:aws:lambda:eu-central-2:224218992030:layer:Synthetics:16`  | 
| Israel (Tel Aviv) |  `arn:aws:lambda:il-central-1:313249807427:layer:Synthetics:14`  | 
| Middle East (Bahrain) |  `arn:aws:lambda:me-south-1:823195537320:layer:Synthetics:29`  | 
| Middle East (UAE) |  `arn:aws:lambda:me-central-1:239544149032:layer:Synthetics:16`  | 
| South America (São Paulo) |  `arn:aws:lambda:sa-east-1:783765544751:layer:Synthetics:30`  | 
| AWS GovCloud (US-East) |  `arn:aws-us-gov:lambda:us-gov-east-1:946759330430:layer:Synthetics:29`  | 
| AWS GovCloud (US-West) |  `arn:aws-us-gov:lambda:us-gov-west-1:946807836238:layer:Synthetics:29`  | 

## Common errors
<a name="CloudWatch_Synthetics_Debug_Errors"></a>

 **Error: Running AWS SAM projects locally requires Docker. Have you got it installed and running?** 

Make sure to start Docker on your computer.

 **SAM local invoke failed: An error occurred (ExpiredTokenException) when calling the GetLayerVersion operation: The security token included in the request is expired** 

Make sure that the AWS default profile is set up.

 **More common errors** 

For more information about common errors with the SAM, see [AWS SAM CLI troubleshooting ](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-troubleshooting.html).