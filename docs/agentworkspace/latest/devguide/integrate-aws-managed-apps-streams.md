

# Integrating AWS-managed applications with Amazon Connect Streams
<a name="integrate-aws-managed-apps-streams"></a>

This guide demonstrates how to integrate AWS-managed applications with your existing applications built using Amazon Connect Streams. This integration extends your custom agent application with AWS-managed applications from the Connect Customer agent workspace. By embedding AWS-managed applications into your custom agent application, you can leverage their features without additional development effort, while maintaining control over application access through Security Profiles.

## Amazon Connect Streams
<a name="integrate-aws-managed-apps-streams-definition"></a>

Amazon Connect Streams is a JavaScript library that integrates the Contact Control Panel (CCP) and other agent functionality into existing web applications. This library enables you to embed the CCP user interface as well as handle agent and contact state events so that you can build a custom agent application. See the [Amazon Connect Streams documentation](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md).

## AWS-managed applications
<a name="integrate-aws-managed-apps-definition"></a>

Amazon Connect provides AWS-managed applications, such as [ Worklist](https://docs.aws.amazon.com/connect/latest/adminguide/worklist-app.html) that are accessible in the [Connect Customer agent workspace](https://docs.aws.amazon.com/connect/latest/adminguide/agent-workspace.html).

## Amazon Connect SDK
<a name="integrate-aws-managed-apps-sdk-definition"></a>

The Amazon Connect SDK is a collection of packages that helps you build applications applications that interact with and extend Amazon Connect’s native functionality. See the [Amazon Connect SDK repository on GitHub. ](https://github.com/amazon-connect/AmazonConnectSDK).

## AppManager
<a name="integrate-aws-managed-apps-appmanager-definition"></a>

AppManager provides APIs to discover, launch, and manage AWS-managed applications. It's available within the Amazon Connect SDK `@amazon-connect/app-manager` package.

## Integration architecture
<a name="integrate-aws-managed-apps-architecture"></a>

The following diagram illustrates the components and integration flow for AWS-managed applications using Streams and AppManager.

![Integration architecture diagram showing AWS-managed applications with Streams and AppManager.](http://docs.aws.amazon.com/agentworkspace/latest/devguide/images/integrate-aws-managed-apps-with-streams.png)


Application launch follows this sequence:

1. Your web application initializes the CCP with the AppManager plugin.

1. The `launchApp` method in AppManager is invoked with the application name or Amazon Resource Name (ARN).

1. AppManager creates an `AppHost` object to manage the application instance.

1. An iframe element is provided to the `AppHost`.

1. AppManager configures the iframe with appropriate URL and security attributes.

1. The application loads and establishes secure communication.