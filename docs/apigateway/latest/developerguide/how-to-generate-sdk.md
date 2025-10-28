# Generate SDKs for REST APIs in API Gateway

To call your REST API in a platform- or language-specific way, you must generate the platform- or
language-specific SDK of the API. You generate your SDK after you create, test, and deploy your API to a
stage. Currently, API Gateway supports generating an SDK for an API in Java, JavaScript, Java for Android, Objective-C or
Swift for iOS, and Ruby.

This section explains how to generate an SDK of an API Gateway API. It also demonstrates how to
use the generated SDK in a Java app, a Java for Android app, Objective-C and Swift for iOS
apps, and a JavaScript app.

To facilitate the discussion, we use this API Gateway [API](simple-calc-lambda-api.md "simple-calc-lambda-api.md"), which exposes this [Simple Calculator](simple-calc-nodejs-lambda-function.md "simple-calc-nodejs-lambda-function.md") Lambda function.

Before proceeding, create or import the API and deploy it at least once in API Gateway. For
instructions, see [Deploy REST APIs in API Gateway](how-to-deploy-api.md "how-to-deploy-api.md").

###### Topics

- [Simple calculator Lambda function](simple-calc-nodejs-lambda-function.md "simple-calc-nodejs-lambda-function.md")
- [Simple calculator API in API Gateway](simple-calc-lambda-api.md "simple-calc-lambda-api.md")
- [Simple calculator API OpenAPI definition](simple-calc-lambda-api-swagger-definition.md "simple-calc-lambda-api-swagger-definition.md")
- [Generate the Java SDK of an
  API in API Gateway](generate-java-sdk-of-an-api.md "generate-java-sdk-of-an-api.md")
- [Generate the Android SDK of an API in API Gateway](generate-android-sdk-of-an-api.md "generate-android-sdk-of-an-api.md")
- [Generate the iOS SDK of an API in API Gateway](generate-ios-sdk-of-an-api.md "generate-ios-sdk-of-an-api.md")
- [Generate the JavaScript SDK of a REST API in API Gateway](generate-javascript-sdk-of-an-api.md "generate-javascript-sdk-of-an-api.md")
- [Generate the Ruby SDK of an
  API in API Gateway](generate-ruby-sdk-of-an-api.md "generate-ruby-sdk-of-an-api.md")
- [Generate SDKs for an API using AWS CLI commands in API Gateway](how-to-generate-sdk-cli.md "how-to-generate-sdk-cli.md")
