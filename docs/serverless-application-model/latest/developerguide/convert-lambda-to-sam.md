

# Converting Lambda Functions to AWS SAM Applications
<a name="convert-lambda-to-sam"></a>

If you have a function in the Lambda console that you want to manage in VS Code as infrastructure as code (IaC), you can transfer it to VS Code and then convert it to an AWS SAM template. With your function converted to an AWS SAM template, you can control the versioning of your infrastructure, automate deployments, remotely debug functions, and maintain consistent environments across your development lifecycle. With local and remote debugging capabilities, you can also troubleshoot issues more effectively by stepping through your code, inspecting variables, and setting breakpoints both locally and in the AWS cloud. 

For instructions on moving your functions from the console and setting up local development, see [Developing Lambda functions locally with VS Code](https://docs.aws.amazon.com/lambda/latest/dg/foundation-iac-local-development.html) in the *AWS Lambda Developer Guide*. Follow these instructions to move a Lambda function from the console to VS Code and then convert it to an AWS SAM template. After doing this, you can:
+ **Remotely debug your function in the AWS cloud.** For details, see [Remotely debug Lambda functions with VS Code](https://docs.aws.amazon.com/lambda/latest/dg/debugging.html) in the *AWS Lambda Developer Guide*.
+ **Manage associated resources and permissions as infrastructure as code.** For details, see [Using Lambda with infrastructure as code (IaC)](https://docs.aws.amazon.com/lambda/latest/dg/foundation-iac.html) in the *AWS Lambda Developer Guide*
+ **Deploy and update your application using the AWS SAM CLI.** For details, see [AWS SAM CLI](using-sam-cli.md).
+ **Visually design your serverless architecture using Infrastructure Composer.** For details, refer to [the Infrastructure Composer Developer Guide](https://docs.aws.amazon.com/application-composer/latest/dg/what-is-composer.html).

## Learn more
<a name="convert-lambda-to-sam-learn"></a>

To continue learning about AWS SAM, see the following resources:
+ **[The Complete AWS SAM Workshop](https://s12d.com/sam-ws-en-intro)** – A workshop designed to teach you many of the major features that AWS SAM provides.
+ **[ Sessions with SAM](https://www.youtube.com/playlist?list=PLJo-rJlep0ED198FJnTzhIB5Aut_1vDAd)** – Video series created by our AWS Serverless Developer Advocate team on using AWS SAM.
+ **[Serverless Land](https://serverlessland.com/)** – Site that brings together the latest information, blogs, videos, code, and learning resources for AWS serverless.