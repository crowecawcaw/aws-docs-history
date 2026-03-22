# Setting up DynamoDB local (downloadable version)

With the downloadable version of Amazon DynamoDB, you can develop and test applications
without accessing the DynamoDB web service. Instead, the database is self-contained on your
computer. When you're ready to deploy your application in production, you remove the
local endpoint in the code, and then it points to the DynamoDB web service.

Having this local version helps you save on throughput, data storage, and data
transfer fees. In addition, you don't need an internet connection while you develop your
application.

DynamoDB local is available as a [download](DynamoDBLocal.DownloadingAndRunning.md#DynamoDBLocal.DownloadingAndRunning.title "DynamoDBLocal.DownloadingAndRunning.md#DynamoDBLocal.DownloadingAndRunning.title") (requires JRE),
as an [Apache Maven dependency](DynamoDBLocal.DownloadingAndRunning.md#apache-maven "DynamoDBLocal.DownloadingAndRunning.md#apache-maven"), or as a [Docker image](DynamoDBLocal.DownloadingAndRunning.md#docker "DynamoDBLocal.DownloadingAndRunning.md#docker").

If you prefer to use the Amazon DynamoDB web service instead, see [Setting up DynamoDB (web service)](SettingUp.DynamoWebService.md "SettingUp.DynamoWebService.md").

###### Topics

- [Deploying DynamoDB locally on your computer](DynamoDBLocal.DownloadingAndRunning.md "DynamoDBLocal.DownloadingAndRunning.md")
- [DynamoDB local usage notes](DynamoDBLocal.UsageNotes.md "DynamoDBLocal.UsageNotes.md")
- [Release history for DynamoDB local](DynamoDBLocalHistory.md "DynamoDBLocalHistory.md")
- [Telemetry in DynamoDB local](DynamoDBLocalTelemetry.md "DynamoDBLocalTelemetry.md")
