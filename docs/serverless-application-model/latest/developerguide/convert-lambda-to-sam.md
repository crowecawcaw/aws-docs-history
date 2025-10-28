# Converting Lambda Functions to AWS SAM Applications

If you have a function in the Lambda console that you want to manage in VS Code as infrastructure as code (IaC), you can transfer it to VS Code and then convert it to an AWS SAM template.
With your function converted to an AWS SAM template, you can control the versioning of your infrastructure, automate deployments, remotely debug functions, and maintain consistent environments across your development lifecycle.
With local and remote debugging capabilities, you can also troubleshoot issues more effectively by stepping through your code, inspecting variables, and setting breakpoints both locally and in the AWS cloud.

For instructions on moving your functions from the console and setting up local development,
see [Developing Lambda functions locally with VS Code](../../../lambda/latest/dg/foundation-iac-local-development.md "../../../lambda/latest/dg/foundation-iac-local-development.md") in the _AWS Lambda Developer Guide_.
Follow these instructions to move a Lambda function from the console to VS Code
and then convert it to an AWS SAM template. After doing this, you can:

- **Remotely debug your function in the AWS cloud.** For details, see [Remotely debug Lambda functions with VS Code](../../../lambda/latest/dg/debugging.md "../../../lambda/latest/dg/debugging.md") in the _AWS Lambda Developer Guide_.
- **Manage associated resources and permissions as infrastructure as code.** For details, see [Using Lambda with infrastructure as code (IaC)](../../../lambda/latest/dg/foundation-iac.md "../../../lambda/latest/dg/foundation-iac.md") in the _AWS Lambda Developer Guide_
- **Deploy and update your application using the AWS SAM CLI.** For details, see [AWS SAM CLI](using-sam-cli.md "using-sam-cli.md").
- **Visually design your serverless architecture using Infrastructure Composer.** For details, refer to [the Infrastructure Composer Developer Guide](../../../application-composer/latest/dg/what-is-composer.md "../../../application-composer/latest/dg/what-is-composer.md").

## Learn more

To continue learning about AWS SAM, see the following resources:

- **[The Complete AWS SAM
  Workshop](https://s12d.com/sam-ws-en-intro "https://s12d.com/sam-ws-en-intro")** – A workshop designed to teach you many of the major features that AWS SAM
  provides.
- **[Sessions with SAM](https://www.youtube.com/playlist?list=PLJo-rJlep0ED198FJnTzhIB5Aut_1vDAd "https://www.youtube.com/playlist?list=PLJo-rJlep0ED198FJnTzhIB5Aut_1vDAd")** – Video series created by our AWS Serverless Developer
  Advocate team on using AWS SAM.
- **[Serverless Land](https://serverlessland.com/ "https://serverlessland.com/")** –
  Site that brings together the latest information, blogs, videos, code, and learning resources for AWS
  serverless.
