

# Setting up DynamoDB local (downloadable version)

**For new local development and testing, we recommend ExtendDB**  
ExtendDB is an open-source adapter compatible with the Amazon DynamoDB API, released by AWS under the Apache License 2.0. It runs as a single container, needs no Java runtime, and verifies every request with AWS Signature Version 4 (SigV4), like the DynamoDB web service. For more information, see [Setting up ExtendDB](ExtendDB.md).

 With the downloadable version of Amazon DynamoDB, you can develop and test applications without accessing the DynamoDB web service. Instead, the database is self-contained on your computer. When you're ready to deploy your application in production, you remove the local endpoint in the code, and then it points to the DynamoDB web service. 

 Having this local version helps you save on throughput, data storage, and data transfer fees. In addition, you don't need an internet connection while you develop your application. 

 DynamoDB local is available as a [download](DynamoDBLocal.DownloadingAndRunning.md#DynamoDBLocal.DownloadingAndRunning.title) (requires JRE), as an [ Apache Maven dependency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#apache-maven), or as a [Docker image](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#docker). 

If you prefer to use the Amazon DynamoDB web service instead, see [Setting up DynamoDB (web service)](SettingUp.DynamoWebService.md).

**Topics**
+ [Deploying DynamoDB locally on your computer](DynamoDBLocal.DownloadingAndRunning.md)
+ [DynamoDB local usage notes](DynamoDBLocal.UsageNotes.md)
+ [Release history for DynamoDB local](DynamoDBLocalHistory.md)
+ [Telemetry in DynamoDB local](DynamoDBLocalTelemetry.md)