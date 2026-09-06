

# Building your App Studio app with generative AI
<a name="generative-ai"></a>

AWS App Studio provides integrated generative AI capabilities to accelerate development and streamline common tasks. You can leverage generative AI to generate and edit apps, data models, sample data, and even get contextual help while building apps.

## Generating your app
<a name="generative-ai-generate-app"></a>

For an accelerated start, you can generate entire applications using natural language prompts powered by AI. This capability allows you to describe your desired app functionality, and AI will automatically build out the data models, user interfaces, workflows, and connectors. For more information about generating an app with AI, see [Creating an application](applications-create.md).

## Building or editing your app
<a name="generative-ai-build-app"></a>

While editing your application, you can use the chat to describe changes you want to make and your app is updated automatically. You can choose from the existing sample prompts or enter your own prompt. The chat can be used to add, edit, and remove supported components, and also create and configure automations and actions. Use the following procedure to use AI to edit or build your application.

**To edit your app with AI**

1. If necessary, edit your app to navigate to the application studio.

1. (Optional) Select the page or component that you want to edit with AI.

1. Choose **Build with AI** in the bottom left corner to open the chat.

1. Enter the changes that you want to make, or choose from the sample prompts.

1. Review the changes to be made. If you want the changes to be made, choose **Confirm**. Otherwise, enter another prompt.

1. Review summary of the changes.

## Generating your data models
<a name="generative-ai-data-model"></a>

You can automatically generate an entity with fields, data types, and data actions based on the provided entity name. For more information about creating entities, including creating entities using GenAi, see [Creating an entity in an App Studio app](data-entities-create.md).

You can also update an existing entity in the following ways:
+ Add more fields to an entity. For more information, see [Adding, editing, or deleting entity fields](data-entities-edit-fields.md).
+ Add data actions to an entity. For more information, see [Creating data actions](data-entities-edit-data-actions.md#data-entities-data-action-add).

## Generating sample data
<a name="generative-ai-generate-sample-data"></a>

You can generate sample data for your entities based on the entity's fields. This is useful to test your application before connecting external data sources, or testing your application in the Development environment, which doesn't communicate to external data sources. For more information, see [Adding or deleting sample data](data-entities-edit-sample-data.md).

Once you publish your app to Testing or Production, your live data sources and connectors are used in those environments.

## Configuring actions for AWS services
<a name="generative-ai-aws-actions-configuration"></a>

When integrating with AWS services like Amazon Simple Email Service, you can use AI to generate an example configuration with pre-populated fields based on the selected service. To try it out, In the **Properties** menu of an **Invoke AWS** automation action, expand the **Configuration** field by choosing the double-sided arrow. Then, choose **Generate sample configuration**.

## Mocking responses
<a name="generative-ai-mock-responses"></a>

You can generate mocked responses for AWS service actions. This is helpful for testing your application in the Development environment, which doesn't communicate to external data sources.

## Asking AI for help while building
<a name="generative-ai-ask-ai"></a>

Within the application studio, you'll find an **Ask AI for help** button on supported resources or properties. Use this to get contextual suggestions, documentation, and guidance related to the current view or selected component. Ask general questions about App Studio, app building best practices, or your specific application use case to receive tailored information and recommendations.