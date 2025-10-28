# How to use AWS Serverless Application Model (AWS SAM)

The primary tools you use to develop your application are the **AWS SAM CLI** and the **AWS SAM template and AWS SAM project**
(which is your application project directory).
You use these tools to:

1. [Develop your application](chapter-create-application.md "chapter-create-application.md") (this includes initializing your application, defining your resources, and building your application).
2. [Test your application](serverless-test-and-debug.md "serverless-test-and-debug.md").
3. [Debug your application](debug-application.md "debug-application.md").
4. [Deploy your application and resources](serverless-deploying.md "serverless-deploying.md").
5. [Monitor your application](serverless-monitoring.md "serverless-monitoring.md").
   AWS SAM creates your AWS SAM project after you run the **sam init** command and complete its subsequent workflow.
   You define your serverless application by adding code to your AWS SAM project. While your AWS SAM project consists of a set of files and folders,
   the most important file in it is your AWS SAM template (named `template.yaml`). In this template, you write your code to express resources,
   event source mappings, and other properties that define your serverless application.

The AWS SAM CLI contains a repository of commands you use on your AWS SAM project.
More specifically, the AWS SAM CLI is what you use to build, transform, deploy, debug, package, initialize, and sync your AWS SAM project.
In other words, it’s what you use to turn your AWS SAM project into your serverless application.

For more details on these tools, see the following chapters:

[AWS SAM CLI](using-sam-cli.md "using-sam-cli.md") - Learn about the AWS SAM CLI and how to use it to build and run your serverless applications.

[AWS SAM project and AWS SAM template](sam-specification.md "sam-specification.md") - Learn about the AWS SAM project structure and how to use the AWS SAM template to define your serverless application.
