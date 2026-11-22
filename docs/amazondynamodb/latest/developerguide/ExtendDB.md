

# Setting up ExtendDB

[ExtendDB](https://extenddb.org/) is an open-source adapter that is compatible with the Amazon DynamoDB API. ExtendDB serves the DynamoDB API from a storage backend such as SQLite or PostgreSQL, and you can run it on your computer for local development and testing. It is an independent project managed by AWS. ExtendDB is not DynamoDB and contains no DynamoDB source code.

ExtendDB speaks the DynamoDB wire protocol. AWS SDKs, the AWS Command Line Interface (AWS CLI), and other tools that work with DynamoDB also work with ExtendDB. You change only the endpoint URL and the credentials that you use to sign requests.

For local development and testing, use the `extenddb/extenddb-dev` image. This single-container image needs no external database and no Java runtime. The image serves plain HTTP and verifies every request with AWS Signature Version 4 (SigV4). Use it for local development and continuous integration only, not for production or shared networks.

If you prefer to use the Amazon DynamoDB web service, see [Setting up DynamoDB (web service)](SettingUp.DynamoWebService.md).

**Topics**
+ [Starting extenddb-dev](ExtendDB.Starting.md)
+ [Signing requests](ExtendDB.Credentials.md)
+ [Connecting your application](ExtendDB.Endpoint.md)
+ [ExtendDB behavior differences from DynamoDB](ExtendDB.Differences.md)