# Understand the available interfaces for using Nova Act

Nova Act consists of the Nova Act AWS service for production deployment and monitoring, plus Nova Act developer tools (SDK, CLI, and IDE extension) that support your development journey from exploration to production. The Nova Act Playground provides a separate environment for initial exploration at [nova.amazon.com/act](https://nova.amazon.com/act "https://nova.amazon.com/act").

###### Note

When using the Nova Act Playground and/or choosing Nova Act developer tools with API key authentication, access and use are subject to the nova.amazon.com [Terms of Use](https://www.amazon.com/gp/help/customer/display.html?&nodeId=Tsn7s47ytlgjRBHozK "https://www.amazon.com/gp/help/customer/display.html?&nodeId=Tsn7s47ytlgjRBHozK"). When choosing Nova Act developer tools with AWS IAM authentication and/or deploying workflows to the Nova Act AWS service, your [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") and/or [Customer Agreement](https://aws.amazon.com/agreement/ "https://aws.amazon.com/agreement/") (or other agreement governing your use of the AWS Service) apply.

The following interfaces are available:

**Explore** - Start with the Nova Act playground at [nova.amazon.com/act](https://nova.amazon.com/act "https://nova.amazon.com/act") to test automation ideas without any setup.

**Develop** - Use the Nova Act SDK and IDE extension to build and debug workflows locally.

**Deploy** - Use the Nova Act CLI to package and deploy workflows to AWS.

**Monitor** - Use the Nova Act AWS console to track execution and troubleshoot issues.

Most developers progress through these interfaces as they move from experimentation to production deployment.

## Nova Act playground

The Nova Act playground provides an instant, browser-based environment to explore Nova Act capabilities, without any setup or AWS account. Test automation ideas using natural language commands, watch the agent execute actions in a hosted web browser, and export Python scripts when you’re ready to develop locally.

Access the playground at [nova.amazon.com/act](http://nova.amazon.com/act "http://nova.amazon.com/act") with your Amazon account.

## Nova Act SDK

The Nova Act SDK enables you to build automation workflows quickly using Python. Install with a single command and define agents using Python code, natural language, or both. The SDK provides powerful debugging capabilities, such as setting breakpoints, adding assertions, and iterating rapidly during development. The SDK supports both API Key authentication for quick experimentation and AWS IAM authentication for production development.

To install the SDK:

```
 pip install nova-act
```

Visit the [nova-act](https://github.com/aws/nova-act "https://github.com/aws/nova-act") GitHub repository for install instructions and detailed documentation.

## Nova Act extension

The Nova Act extension brings the complete agent development experience into IDEs such as [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-nova-act-extension "https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-nova-act-extension"), [Cursor](https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension "https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension"), and [Kiro](https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension "https://open-vsx.org/extension/amazonwebservices/amazon-nova-act-extension"). Build, test, and debug agents in a unified environment without switching between tools. Key features include Builder Mode with live browser preview, chat-to-generate scripts, code templates, and integrated deployment capabilities.

Visit the [nova-act-extension](https://github.com/aws/nova-act-extension "https://github.com/aws/nova-act-extension") GitHub repository for installation instructions and detailed documentation.

## Nova Act CLI

The Nova Act CLI automates the deployment process by turning your local scripts into remote workflows on Amazon Bedrock AgentCore Runtime. It handles the complexity of containerization, ECR management, S3 bucket creation, and IAM role creation automatically. Use the CLI to create Nova Act workflow definitions, deploy your scripts, and invoke workflow—all from your command line with account-based configuration management. The CLI is also integrated into the Nova Act extension for seamless deployment as you develop. The CLI requires AWS credentials configured via the AWS CLI or AWS profiles.

Visit the [nova-act](https://github.com/aws/nova-act "https://github.com/aws/nova-act") GitHub repository for install instructions and detailed documentation.

## Nova Act AWS console

The Nova Act AWS console provides a web-based interface to manage and monitor your deployed workflows. Create workflow definitions, view workflow runs with detailed execution traces, and analyze agent behavior through the observability hierarchy (runs → sessions → acts → steps). The console displays step execution data, observation and invocation loops, and provides access to artifacts stored in S3.

Access the Nova Act AWS console through the [AWS Management Console](https://us-east-1.console.aws.amazon.com/nova-act/home "https://us-east-1.console.aws.amazon.com/nova-act/home").
