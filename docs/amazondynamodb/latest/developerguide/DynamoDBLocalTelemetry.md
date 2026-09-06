

# Telemetry in DynamoDB local
<a name="DynamoDBLocalTelemetry"></a>

 At AWS, we develop and launch services based on what we learn from interactions with customers, and we use customer feedback to iterate on our products. Telemetry is additional information that helps us to better understand our customers needs, diagnose issues, and deliver features that improve the customer experience. 

 DynamoDB local collects telemetry, such as generic usage metrics, systems and environment information, and errors. For details about the types of telemetry collected, see [Types of information collected](#DynamoDBLocalTelemetry.TypesOfInformationCollected). 

 DynamoDB local does not collect personal information, such as user names or email addresses. It also does not extract sensitive project-level information. 

 As a customer, you control whether telemetry is turned on, and you can change your settings at any point in time. If telemetry remains on, DynamoDB local sends telemetry data in the background without requiring any additional customer interaction. 

## Turn off telemetry using command line options
<a name="DynamoDBLocalTelemetry.cli"></a>

 You can turn off telemetry using command line options when starting DynamoDB local using the option `-disableTelemetry`. For more information, see [Command line options](DynamoDBLocal.UsageNotes.md#DynamoDBLocal.CommandLineOptions).

## Turn off telemetry for a single session
<a name="DynamoDBLocalTelemetry.TurnOffTelemetrySingleSession"></a>

 In macOS and Linux operating systems, you can turn off telemetry for a single session. To turn off telemetry for your current session, run the following command to set the environment variable `DDB_LOCAL_TELEMETRY` to `false`. Repeat the command for each new terminal or session. 

```
export DDB_LOCAL_TELEMETRY=0
```

## Turn off telemetry for your profile in all sessions
<a name="DynamoDBLocalTelemetry.TurnOffTelemetryForAllSessions"></a>

 Run the following commands to turn off telemetry for all sessions when you're running DynamoDB local on your operating system. 

**To turn off telemetry in Linux**

1.  Run: 

   ```
   echo "export DDB_LOCAL_TELEMETRY=0" >>~/.profile
   ```

1.  Run: 

   ```
   source ~/.profile
   ```

**To turn off telemetry in macOS**

1.  Run: 

   ```
   echo "export DDB_LOCAL_TELEMETRY=0" >>~/.profile
   ```

1.  Run: 

   ```
   source ~/.profile
   ```

**To turn off telemetry in Windows**

1.  Run: 

   ```
   setx DDB_LOCAL_TELEMETRY 0
   ```

1.  Run: 

   ```
   refreshenv
   ```

## Turn off telemetry using DynamoDB local embedded on Maven projects
<a name="DynamoDBLocalTelemetry.maven"></a>

 You can turn off telemetry using DynamoDB local embedded on Maven projects. 

```
boolean disableTelemetry = true;
// AWS SDK v1
 AmazonDynamoDB amazonDynamoDB = DynamoDBEmbedded.create(disableTelemetry).amazonDynamoDB();

// AWS SDK v2
DynamoDbClient ddbClientSDKv2Local = DynamoDBEmbedded.create(disableTelemetry).dynamoDbClient();
```

## Types of information collected
<a name="DynamoDBLocalTelemetry.TypesOfInformationCollected"></a>
+  **Usage information** — The generic telemetry like server start/stop and the API or Operation called. 
+  **System and environment information** — The Java version, operating system (Windows, Linux or macOS), the environment in which DynamoDB local runs (for example, Stand alone JAR, Docker container, or as a Maven Dependency), and hash values of usage attributes. 

## Learn more
<a name="DynamoDBLocalTelemetry.LearnMore"></a>

 The telemetry data that DynamoDB local collects adheres to the AWS data privacy policies. For more information, see the following: 
+  [AWS service terms](https://aws.amazon.com/service-terms/) 
+  [Data privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/) 