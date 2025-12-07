# Test your serverless

application with AWS SAM

After writing and building your application, you will be ready to test your application to verify that it functions correctly. With the AWS SAM command line interface (CLI),
you can locally test your serverless application before uploading it to the AWS Cloud. Testing your application helps you confirm the application’s functionality, reliability,
and performance all while identifying issues (bugs) that will need to be addressed.

This section provides guidance on common practices you can follow to test your application.
The topics in this section focus mostly on the local testing you can do before deploying in the AWS Cloud.
Testing before deploying helps you identify issues proactively, reducing unnecessary costs associated with deployment issues.
Each topic in this section describes a test you can perform, tells yoxi include href?
u the advantages of using it, and includes examples
showing you how to perform the test. After testing your application, you’ll be ready to debug any issues you’ve found.

###### Topics

- [Introduction to testing with the sam local command](using-sam-cli-local.md "using-sam-cli-local.md")
- [Locally invoke Lambda functions with AWS SAM](serverless-sam-cli-using-invoke.md "serverless-sam-cli-using-invoke.md")
- [Locally run API Gateway with AWS SAM](serverless-sam-cli-using-start-api.md "serverless-sam-cli-using-start-api.md")
- [Introduction to cloud testing with sam remote test-event](using-sam-cli-remote-test-event.md "using-sam-cli-remote-test-event.md")
- [Introduction to testing in the cloud with sam remote invoke](using-sam-cli-remote-invoke.md "using-sam-cli-remote-invoke.md")
- [Automate local integration tests with AWS SAM](serverless-sam-cli-using-automated-tests.md "serverless-sam-cli-using-automated-tests.md")
- [Generate sample event
  payloads with AWS SAM](serverless-sam-cli-using-generate-event.md "serverless-sam-cli-using-generate-event.md")
- [Testing and debugging durable functions](test-and-debug-durable-functions.md "test-and-debug-durable-functions.md")
