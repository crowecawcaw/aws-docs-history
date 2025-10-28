# Build your application with AWS SAM

After you have added your infrastructure as code (IaC) to your AWS SAM template, you’ll be ready to start building your application using the
**sam build** command. This command creates build artifacts from the files in your application project directory (that is, your AWS SAM template file, application
code, and any applicable language-specific files and dependencies).
These build artifacts prepare your serverless application for later steps of your application's development, such as local testing and deploying to the AWS Cloud. Both testing and deploying use
build artifacts as inputs.

You can use **sam build** to build your entire serverless application. Additionally, you can create customized builds, like one's with specific functions, layers, or custom runtimes.
To read more on how and why you use **sam build**, see the topics in this section.
For an introduction to using the `sam build` command, see [Introduction to building with AWS SAM](using-sam-cli-build.md "using-sam-cli-build.md").

###### Topics

- [Introduction to building with AWS SAM](using-sam-cli-build.md "using-sam-cli-build.md")
- [Default build with AWS SAM](serverless-sam-cli-using-build.md "serverless-sam-cli-using-build.md")
- [Customize builds with AWS SAM](building-lambda-functions.md "building-lambda-functions.md")
