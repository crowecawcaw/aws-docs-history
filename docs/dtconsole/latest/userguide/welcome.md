

# What are notifications?
<a name="welcome"></a>

The notifications feature in the Developer Tools console is a notifications manager for subscribing to events in AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy and AWS CodePipeline. It has its own API, AWS CodeStar Notifications. You can use the notifications feature to quickly notify users about events in the repositories, build projects, deployment applications, and pipelines that are most important to their work. A notifications manager helps make users aware of events that occur on repositories, builds, deployments, or pipelines so that they can quickly take action, such as approving changes or correcting errors. 

## What can I do with notifications?
<a name="welcome-what-can-I-do"></a>

You can use the notifications feature to create and manage notification rules to notify users of important changes to their resources, including:
+ Build successes and failures in CodeBuild build projects.
+ Deployment successes and failures in CodeDeploy applications.
+ Creation of and updates in pull requests, including comments on code, in CodeCommit repositories.
+ Manual approval statuses and pipeline runs in CodePipeline.

You can set up notifications so that they go to user email addresses that are subscribed to an Amazon SNS topic. You can also integrate this feature with [AWS Chatbot](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) and have notifications delivered to Slack channels, Microsoft Teams channel, or Amazon Chime chatrooms.

## How do notifications work?
<a name="welcome-how-it-works"></a>

When you configure a notification rule for a supported resource, such as a repository, build project, application, or pipeline, the notifications feature creates an Amazon EventBridge rule that monitors for the events you specify. When an event of that type occurs, the notification rule sends notifications to the Amazon SNS topics specified as targets for that rule. Subscribers to those targets receive notifications about those events. 

## How do I get started with notifications?
<a name="welcome-get-started"></a>

To get started, here are some useful topics to review:
+ **Learn** about the [concepts](concepts.md) for notifications.
+ **Set up** the [resources you need](setting-up.md) to start working with notifications.
+ **Get started** with your [first notification rules](getting-started.md) and receive your first notifications.