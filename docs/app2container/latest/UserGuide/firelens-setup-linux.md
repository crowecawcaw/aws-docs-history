AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# FireLens log routing for Linux

Before starting these configuration steps, you should have an understanding of the
App2Container containerization phases – Initialize, Analyze, Transform, and Deploy. To
learn more about the containerization phases and the commands that run during each phase,
see the [App2Container command reference](a2c-commands.md "a2c-commands.md") in this user
guide.

Follow these steps to set up log file routing with FireLens for Amazon ECS for
your Linux application containers:

###### FireLens configuration

- [Prerequisites](#firelens-setup-prereq "#firelens-setup-prereq")
- [Step 1: Identify log locations for the container](#firelens-setup-step1 "#firelens-setup-step1")
- [Step 2: Configure log deployment parameters](#firelens-setup-step2 "#firelens-setup-step2")
- [Step 3: Validate deployment artifacts](#firelens-setup-step3 "#firelens-setup-step3")
- [Step 4: Deploy your application to Amazon ECS](#firelens-setup-step4 "#firelens-setup-step4")
- [Step 5: Verify log routing](#firelens-setup-step5 "#firelens-setup-step5")

## Prerequisites

Prior to setting up FireLens log routing for your application,
you must have completed the following prerequisites:

- You have root access on the application server
  (and worker machine, if using).
- You successfully completed all of the steps from the
  [Prerequisites: Set up your servers](start-intro.md#start-containerize-prereq "start-intro.md#start-containerize-prereq") section
  of this user guide.
- You have initialized the App2Container environment by successfully running the
  **[init](cmd-init.md "cmd-init.md")** command.
- The application must be running on the application server,
  and must have a valid application ID assigned by the
  **[inventory](cmd-inventory.md "cmd-inventory.md")** command.

## Step 1: Identify log locations for the container

Run the **[analyze](cmd-analyze.md "cmd-analyze.md")** command for
your application, and then update the following parameters in your
`analysis.json` file:

- Update the `logLocations` array to include a
  list of log files or directory locations where log files can
  be picked up for routing with FireLens.
- Set the `enableDynamicLogging` parameter to
  _true_ to map application logs to `stdout` as
  they are created. If your application appends to specific log files such as
  `info.log` or `error.log`, set the
  `enableDynamicLogging` parameter to
  _false_.

The `analysis.json` file is stored in the
application folder, for example:
`/root/app2container/java-tomcat-9e8e4799`.
For more information on `analysis.json` fields and configuration,
see [Configuring application containers](config-containers.md "config-containers.md") in the
**Configuring your application** section of this user guide.

###### Example:

The following example shows container parameters in the
`analysis.json` file for logging.

```
`"containerParameters": {
 ...
 "logFiles": ["error.log", "info.log"],
 "logDirectory": "/var/app/logs/",
 "logLocations": ["error.log", "info.log", "/var/app/logs/"],
 "enableDynamicLogging": true,
 ...
},`
```

## Step 2: Configure log deployment parameters

Run the **[containerize](cmd-containerize.md "cmd-containerize.md")** command, and
then edit the `deployment.json` file to set
the `fireLensParameters`. The
`deployment.json` file is stored in the
application folder, for example:
`/root/app2container/java-tomcat-9e8e4799`.

There must be at least one valid log destination defined for the
`logDestinations` array, with valid values for each of
the parameters it contains. For more information on
`deployment.json` fields and configuration,
including how to target deployment to AWS Fargate with the
`deployTarget` parameter, see
[Configuring container deployment](config-deployment.md "config-deployment.md")
in the **Configuring your application** section of this user guide.

- Set `enableFirelensLogging` to
  _true_.
- Configure one or more valid `logDestinations`
  as follows:
  - service – the
    AWS service to route logs to. _Valid values are
    "cloudwatch", "firehose", and "kinesis"._
  - regexFilter (string)
    – the pattern to match against log content using
    a Ruby regular expression to determine where to route the log.

  ###### Note

  Ruby regular expressions begin and end with a
  forward slash, with the pattern to match specified in
  between the slashes. Patterns often begin with a
  caret (^), which starts matching at the
  beginning of the line, and end with a dollar sign ($),
  which stops matching at the end of the line.

  The `regexFilter` parameter in the
  `deployment.json` file represents
  only the matching pattern. Be sure to test your
  matching pattern using one of the many applications
  available for your desktop or online, such as
  [Rubular](https://rubular.com/ "https://rubular.com/"). For
  more information about Ruby regular expressions, see
  [Mastering
  Ruby Regular Expressions](https://www.rubyguides.com/2015/06/ruby-regex/ "https://www.rubyguides.com/2015/06/ruby-regex/").
  - streamName (string) – the name
    of the log delivery stream that will be created at the destination.

###### Examples:

The following example shows FireLens parameters in the
`deployment.json` file for logging to a single destination -
CloudWatch – using a Ruby regular expression.

```
`"fireLensParameters": {
 "enableFireLensLogging": true,
 "logDestinations": [
 {
 "service": "cloudwatch",
 "regexFilter": "^.*INFO.*$",
 "streamName": "Info"
 }
 ]
},`
```

This example shows FireLens parameters in the `deployment.json`
file for logging to a single destination – Firehose – using a Ruby regular
expression.

```
`"fireLensParameters": {
 "enableFireLensLogging": true,
 "logDestinations": [
 {
 "service": "firehose",
 "regexFilter": "^.*INFO.*$",
 "streamName": "Info"
 }
 ]
},`
```

This example shows FireLens parameters in the
`deployment.json` file for routing
separate log files to different destinations in CloudWatch,
using Ruby regular expressions.

```
`"fireLensParameters": {
 "enableFireLensLogging": true,
 "logDestinations": [
 {
 "service": "cloudwatch",
 "regexFilter": "^.*INFO.*$",
 "streamName": "Info"
 },
 {
 "service": "cloudwatch",
 "regexFilter": "^.*WARNING.*$",
 "streamName": "Warning"
 }
 ]
},`
```

## Step 3: Validate deployment artifacts

The last step before deployment is to ensure that your
Amazon ECS task definitions and CloudFormation templates are configured as
expected after running the **generate app-deployment**
command, and that your log destinations were created, if applicable.

###### Note

- Deployment artifacts are stored in the Amazon ECS or Amazon EKS deployment folder within
  the application folder that App2Container created for you. For example:
  `/root/app2container/java-tomcat-9e8e4799`
- If you are routing to CloudWatch, your routing destination is not created
  prior to deployment.

1. Run the **[generate app-deployment](cmd-generate-appdeploy.md "cmd-generate-appdeploy.md")**
   command to generate container deployment artifacts.
2. Verify that the Amazon ECS task definitions include the
   parameters that you specified and that the values
   are correct. For an example of FireLens parameters in
   an Amazon ECS task definition, see
   [Example: Amazon ECS task definition FireLens parameters](#firelens-example-ecs-task-def "#firelens-example-ecs-task-def")
3. Verify that the CloudFormation template includes the parameters
   that you specified and that the values are correct. For
   an example of FireLens parameters in a CloudFormation template,
   expand the following section:
   [Example: CloudFormation template FireLens parameters](#firelens-example-ecs-cfn-template "#firelens-example-ecs-cfn-template")
4. If you are routing logs to Kinesis Data Streams or Firehose, verify that the streams have been
   created for you by using the AWS Management Console.
   1. Sign in to the AWS Management Console and open the Kinesis console at
      [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
   2. From the Amazon Kinesis dashboard, choose
      **Data streams** or
      **Delivery streams** from the
      navigation pane.
   3. Verify that your stream **Status**
      is `Active`.

This example shows excerpts from an Amazon ECS task
definition file that was generated for logging to CloudWatch.

```
`"executionRoleArn": arn:aws:iam::
 &lt;YOUR_ACCOUNT_ID&gt;:role/A2CEcsFirelensRole",
"containerDefinitions": [
 {
 ...
 "logConfiguration": {
 "logDriver": "awsfirelens",
 "secretOptions": null,
 "options": {
 "include-pattern": "^.*INFO.*$",
 "log_group_name": "java-tomcat-c770eed9-logs",
 "log_stream_name": "java-tomcat-c770eed9-Info",
 "auto_create_group": "true",
 "region": "us-east-1",
 "Name": "cloudwatch"
 }
 },
 ...
 "name": "java-tomcat-c770eed9"
 },
 {
 "dnsSearchDomains": null,
 "environmentFiles": null,
 "logConfiguration": {
 "logDriver": "awslogs",
 "secretOptions": null,
 "options": {
 "awslogs-group": "/ecs/containerization",
 "awslogs-region": "us-east-1",
 "awslogs-create-group": "true",
 "awslogs-stream-prefix": "firelens"
 }
 },
 ...
 "firelensConfiguration": {
 "type": "fluentbit",
 "options": null
 },
 ...
 "name": "java-tomcat-c770eed9-log-router"
 }
 ],
 ...
 "taskRoleArn": arn:aws:iam::
 &lt;YOUR_ACCOUNT_ID&gt;:role/A2CEcsFirelensRole",
 "compatibilities": [
 "EC2",
 "FARGATE"
 ],
 ...
 "requiresAttributes": [
 {
 "targetId": null,
 "targetType": null,
 "value": null,
 "name": "ecs.capability.execution-role-awslogs"
 },
 ...
 {
 "targetId": null,
 "targetType": null,
 "value": null,
 "name": "com.amazonaws.ecs.capability.logging-driver.awsfirelens"
 },
 ...
 {
 "targetId": null,
 "targetType": null,
 "value": null,
 "name": "com.amazonaws.ecs.capability.logging-driver.awslogs"
 },
 ...
 {
 "targetId": null,
 "targetType": null,
 "value": null,
 "name": "ecs.capability.firelens.fluentbit"
 }
 ],`
```

This example shows excerpts from a CloudFormation template
file that was generated for logging to CloudWatch.

```
`Metadata:
 AWS::CloudFormation::Interface:
 ParameterGroups:
...
- Label:
 default: Logging Parameters for the application being deployed, check ecs-lb-webapp.yml for usage
 Parameters:
 - TaskLogDriver
 - MultipleDests
 - SingleDestName
 - IncludePattern
 - LogGrpName
 - LogStrmName
 - AutoCrtGrp
 - FirehoseStream
 - KinesisStream
 - KinesisAppendNewline
 - FirelensName
 - FirelensImage
 - ConfigType
 - ConfigPath
 - UsingCloudwatchLogs
 - UsingFirehoseLogs
 - UsingKinesisLogs
...
Parameters:
...
# Firelens Parameters for the application being deployed
 TaskLogDriver:
 Type: String
 Default: awsfirelens
 MultipleDests:
 Type: String
 AllowedValues: [true, false]
 Default: false
 SingleDestName:
 Type: String
 Default: cloudwatch
 IncludePattern:
 Type: String
 Default: ^.*INFO.*$
 LogGrpName:
 Type: String
 Default: java-tomcat-c770eed9-logs
 LogStrmName:
 Type: String
 Default: java-tomcat-c770eed9-Info
 AutoCrtGrp:
 Type: String
 Default: true
 FirehoseStream:
 Type: String
 Default: ""
 KinesisStream:
 Type: String
 Default: ""
 KinesisAppendNewline:
 Type: String
 Default: ""
 FirelensName:
 Type: String
 Default: java-tomcat-c770eed9-log-router
 FirelensImage:
 Type: String
 Default: 906394416424.dkr.ecr.us-east-1.amazonaws.com/aws-for-fluent-bit:latest
 ConfigType:
 Type: String
 Default: ""
 ConfigPath:
 Type: String
 Default: ""
 UsingCloudwatchLogs:
 Type: String
 Default: true
 UsingFirehoseLogs:
 Type: String
 Default: false
 UsingKinesisLogs:
 Type: String
 Default: false
...
Rules:
 FirelensSingleCloudwatch:
 RuleCondition: !And
 - !Equals [ !Ref MultipleDests, 'false']
 - !Equals [ !Ref UsingCloudwatchLogs, 'true']
 Assertions:
 - AssertDescription: You cannot use any other firelens destination if a single cloudwatch stream is desired
 Assert: !And
 - !Equals [ !Ref UsingFirehoseLogs, 'false']
 - !Equals [ !Ref UsingKinesisLogs, 'false']
 - !Equals [ !Ref SingleDestName, "cloudwatch" ]
 - !Not [ !Equals [ !Ref LogGrpName, "" ]]
 - !Not [ !Equals [ !Ref LogStrmName, "" ]]
 - !Not [ !Equals [ !Ref AutoCrtGrp, "" ]]
 FirelensSingleFirehose:
 RuleCondition: !And
 - !Equals [ !Ref MultipleDests, 'false']
 - !Equals [ !Ref UsingFirehoseLogs, 'true']
 Assertions:
 - AssertDescription: You cannot use any other firelens destination if a single firehose stream is desired
 Assert: !And
 - !Equals [ !Ref UsingCloudwatchLogs, 'false']
 - !Equals [ !Ref UsingKinesisLogs, 'false']
 - !Equals [ !Ref SingleDestName, "firehose" ]
 - !Not [ !Equals [ !Ref FirehoseStream, "" ]]
 FirelensSingleKinesis:
 RuleCondition: !And
 - !Equals [ !Ref MultipleDests, 'false']
 - !Equals [ !Ref UsingKinesisLogs, 'true']
 Assertions:
 - AssertDescription: You cannot use any other firelens destination if a single kinesis stream is desired
 Assert: !And
 - !Equals [ !Ref UsingCloudwatchLogs, 'false']
 - !Equals [ !Ref UsingFirehoseLogs, 'false']
 - !Equals [ !Ref SingleDestName, "kinesis" ]
 - !Not [ !Equals [ !Ref KinesisStream, "" ]]
 - !Not [ !Equals [ !Ref KinesisAppendNewline, "" ]]
 MultipleDestinations:
 RuleCondition: !Equals [ !Ref MultipleDests, 'true']
 Assertions:
 - AssertDescription: You must supply a configuration file location and filepath if multiple firelens destinations are being used
 Assert: !And
 - !Not [ !Equals [ !Ref ConfigType, "" ] ]
 - !Not [ !Equals [ !Ref ConfigPath, "" ] ]
 - !Equals [ !Ref SingleDestName, ""]
 - !Equals [ !Ref IncludePattern, ""]
 - !Equals [ !Ref LogGrpName, ""]
 - !Equals [ !Ref LogStrmName, ""]
 - !Equals [ !Ref AutoCrtGrp, ""]
 - !Equals [ !Ref FirehoseStream, ""]
 - !Equals [ !Ref KinesisStream, ""]
 - !Equals [ !Ref KinesisAppendNewline, ""]
...
Conditions:
...
Resources:
 PrivateAppStack:
 Type: AWS::CloudFormation::Stack
 Condition: DoNotCreatePublicLoadBalancer
 Properties:
 TemplateURL: !Sub 'https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${S3KeyPrefix}/ecs-private-app.yml'
 Tags:
 - Key: "a2c-generated"
 Value: !Sub 'ecs-app-${AWS::StackName}'
 Parameters:
...
 TaskLogDriver: !Ref TaskLogDriver
 MultipleDests: !Ref MultipleDests
 SingleDestName: !Ref SingleDestName
 IncludePattern: !Ref IncludePattern
 LogGrpName: !Ref LogGrpName
 LogStrmName: !Ref LogStrmName
 AutoCrtGrp: !Ref AutoCrtGrp
 FirehoseStream: !Ref FirehoseStream
 KinesisStream: !Ref KinesisStream
 KinesisAppendNewline: !Ref KinesisAppendNewline
 FirelensName: !Ref FirelensName
 FirelensImage: !Ref FirelensImage
 ConfigType: !Ref ConfigType
 ConfigPath: !Ref ConfigPath
 UsingCloudwatchLogs: !Ref UsingCloudwatchLogs
 UsingFirehoseLogs: !Ref UsingFirehoseLogs
 UsingKinesisLogs: !Ref UsingKinesisLogs
...`
```

## Step 4: Deploy your application to Amazon ECS

Deploy your application using the **[generate app-deployment](cmd-generate-appdeploy.md "cmd-generate-appdeploy.md")** command
with the `--deploy` option.

````
`$` `sudo app2container generate app-deployment --deploy --application-id `java-tomcat-9e8e4799```√ AWS prerequisite check succeeded
√ Docker prerequisite check succeeded
√ Created ECR Repository
√ Registered ECS Task Definition with ECS
√ Uploaded CloudFormation resources to S3 Bucket: app2container-example
√ Generated CloudFormation Master template at: /root/app2container/java-tomcat-9e8e4799/EcsDeployment/ecs-master.yml
√ Initiated CloudFormation stack creation. This may take a few minutes. Please visit the CloudFormation Console to track progress.
ECS deployment successful for application java-tomcat-9e8e4799

The URL to your Load Balancer Endpoint is:
<your endpoint>.us-east-1.elb.amazonaws.com
Successfully created ECS stack app2container-java-tomcat-9e8e4799-ECS. Check the CloudFormation Console for additional details.`
````

Alternatively, you can deploy your application's CloudFormation template using the AWS CLI as
follows.

```
`$` `sudo aws cloudformation deploy --template-file /root/app2container/java-tomcat-9e8e4799/EcsDeployment/ecs-master.yml --capabilities CAPABILITY_NAMED_IAM --stack-name app2container-java-tomcat-9e8e4799-ECS`
```

## Step 5: Verify log routing

After you deploy your application to Amazon ECS, you can verify that your
logs are routing to their intended destinations.
