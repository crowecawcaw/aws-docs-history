# What is AWS AppFabric for productivity?

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

###### Note

Powered by Amazon Bedrock: AWS implements automated abuse [detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md"). Because AWS AppFabric for productivity is
built on Amazon Bedrock, users inherit the controls implemented in Amazon Bedrock to enforce safety,
security, and the responsible use of AI.

AWS AppFabric for productivity (preview) helps reimagine end-user productivity in third-party applications by
generating insights and actions with context from multiple applications. App developers recognize
that accessing user data from other apps is important in creating a more productive app
experience, but they don’t want to build and manage integrations with each application. With
AppFabric for productivity, application developers gain access to generative AI-powered APIs that generate
cross-app data insights and actions so they can provide richer end-user experiences through new or
existing generative AI assistants. AppFabric for productivity integrates data from multiple applications removing
the need for developers to build or maintain point-to-point integrations. Application developers
can embed AppFabric for productivity directly into their application’s UI, maintaining a consistent experience for
their end users while surfacing relevant context from other applications.

AppFabric for productivity connects data from commonly used applications such as Asana,
Atlassian Jira Suite, Google Workspace, Microsoft
365, Miro, Slack, Smartsheet, and more.
AppFabric for productivity gives app developers an easier way to build more personalized app experiences that
improve user adoption, satisfaction, and loyalty. Meanwhile, end users benefit from accessing
insights they need from across their applications without interrupting their flow of work.

###### Topics

- [Benefits](#benefits "#benefits")
- [Use cases](#use-cases "#use-cases")
- [Accessing AppFabric for productivity](#acessing-appfabric "#acessing-appfabric")
- [Get started with AppFabric for productivity
  (preview) for application developers](getting-started-appdeveloper-productivity.md "getting-started-appdeveloper-productivity.md")
- [Get started with AppFabric for productivity (preview) for
  end users](getting-started-users-productivity.md "getting-started-users-productivity.md")
- [AppFabric for productivity APIs (preview)](productivity-apis.md "productivity-apis.md")
- [Data processing in AppFabric](productivity-data-processing.md "productivity-data-processing.md")

## Benefits

With AppFabric for productivity, application developers gain access to APIs that generate cross-app data
insights and actions so they can provide richer end-user experiences through new or existing
generative AI assistants.

- **Single source of cross-app user data**: AppFabric for productivity
  integrates data from multiple applications removing the need for developers to build or
  maintain point-to-point integrations. SaaS app data is processed for use in other applications
  by automatically normalizing disparate data types into a format understandable by any
  application, allowing app developers to incorporate more data that actually improves end users’
  productivity.
- **Full control of user experience**: Developers embed
  AppFabric for productivity directly into their application’s UI, retaining full control of the user experience
  while providing personalized insights and recommended actions to end users with context from
  across their applications. This makes AppFabric for productivity available in end users’ preferred SaaS
  application and is accessible in the app they prefer to complete their tasks. End users spend
  less time switching between apps, and can stay in the flow of their work.
- **Accelerate time to market**: In a single API call, app
  developers can receive user-level insights across a user’s data that is generated without
  having to fine-tune a model, write a custom prompt, or build integrations across multiple
  applications. AppFabric abstracts out this complexity to enable app developers to build, embed, or
  enrich generative AI capabilities faster. This allows app developers to focus on their
  resources on the most important tasks.
- **Artifact references to build user trust**: As part of the
  output, AppFabric for productivity will surface relevant artifacts or source files used to generate the
  insights to build end-user trust in the LLM outputs.
- **Simplified user permissions**: User artifacts used to
  generate insights are based on what a user has access to. AppFabric for productivity uses the an ISV’s
  permission and access control as the source of truth.

## Use cases

App developers can use AppFabric for productivity to reimagine productivity inside their applications.
AppFabric for productivity offers two APIs focused on the following use cases to help their end users be more
productive:

- Prioritize your day
  - The actionable insights API helps users best manage their day by surfacing timely
    insights from across their applications including emails, calendar, messages, tasks, and
    more. Additionally, users can execute cross-app actions such as creating emails, scheduling
    meetings, and creation action items from their preferred application. For example, an
    employee who had customer escalation overnight will not only see a summary of the overnight
    conversations, but will also be able to see a recommended action to schedule a meeting with
    the customer Account Manager. Actions are pre-populated with required fields (such as tasks
    name and owner, or email sender/recipient), with the ability to edit pre-populated content
    before executing the action.

- Prepare for upcoming meetings
  - The meeting preparation API helps users best prepare for meetings by summarizing the
    meeting purpose and surfacing relevant cross-app artifacts such as emails, messages, and
    more. Users can quickly prepare for meetings now and don’t waste time switching between apps
    to find content.

## Accessing AppFabric for productivity

AppFabric for productivity is currently launched as a preview and available in the US East (N. Virginia)
AWS Region. For more information about AWS Regions, see [AWS AppFabric endpoints and quotas](../../../general/latest/gr/appfabric.md "../../../general/latest/gr/appfabric.md") in the
_AWS General Reference_.

In each Region, you can access AppFabric for productivity in any of the following ways:

- As an app developer
  - [Get started with AppFabric for productivity
    (preview) for application developers](getting-started-appdeveloper-productivity.md "getting-started-appdeveloper-productivity.md")

- As an end user
  - [Get started with AppFabric for productivity (preview) for
    end users](getting-started-users-productivity.md "getting-started-users-productivity.md")
