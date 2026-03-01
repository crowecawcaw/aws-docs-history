# Tutorial: Generate an app using AI

AWS App Studio contains generative AI features throughout the service to help speed up
application building. In this tutorial, you'll learn how to generate an app using AI by describing
your app using natural language.

Using AI to generate an app is a great way to start building because many of the app's
resources are created for you. It's typically much easier to start building from a generated app
with existing resources than to start from an empty app.

###### Note

You can view the blog post [Build enterprise-grade applications with natural language using AWS App Studio
(preview)](https://aws.amazon.com/blogs/aws/build-custom-business-applications-without-cloud-expertise-using-aws-app-studio-preview "https://aws.amazon.com/blogs/aws/build-custom-business-applications-without-cloud-expertise-using-aws-app-studio-preview") to view a similar walkthrough that includes images. The blog post also
contains information about setting up and configuring administrator-related resources, but you
can skip to the portion about building applications if desired.

When App Studio generates an app with AI, it creates the app with the following resources
that are tailored to the app that you described:

- **Pages and components**: _Components_ are
  the building blocks of your application's user interface. They represent visual elements like
  tables, forms, and buttons. Each component has its own set of properties, and you can customize
  a component to fit your specific requirements. _Pages_ are the containers for
  components.
- **Automations**: You use _automations_ to
  define the logic and workflows that govern how your application behaves. For example, you can
  use automations to create, update, read, or delete rows in a data table or to interact with
  objects in an Amazon S3 bucket. You can also use them to handle tasks like data validation,
  notifications, or integrations with other systems.
- **Entities**: Data is the information that powers your
  application. The generated app creates _entities_, which are similar to
  tables. Entities represent the different types of data that you need to store and work with,
  such as customers, products, or orders. You can connect these data models to a variety of data
  sources, including AWS services and external APIs, by using App Studio connectors.

###### Contents

- [Prerequisites](getting-started-tutorial-ai.md#getting-started-tutorial-ai-prerequisites "getting-started-tutorial-ai.md#getting-started-tutorial-ai-prerequisites")
- [Step 1: Create an application](getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-create-application "getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-create-application")
- [Step 2: Explore your new application](getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore "getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore")
  - [Explore pages and components](getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore-pages "getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore-pages")
  - [Explore automations and actions](getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore-automations "getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore-automations")
  - [Explore data with entities](getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore-data-entities "getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-explore-data-entities")

- [Step 3: Preview your application](getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-preview "getting-started-tutorial-ai.md#getting-started-tutorial-ai-steps-preview")
- [Next steps](getting-started-tutorial-ai.md#getting-started-tutorial-ai-next-steps "getting-started-tutorial-ai.md#getting-started-tutorial-ai-next-steps")

## Prerequisites

Before you get started, review and complete the following prerequisites:

- Access to AWS App Studio. For more information, see [Setting up and signing in to AWS App Studio](setting-up.md "setting-up.md").
- Optional: Review [AWS App Studio concepts](concepts.md "concepts.md") to familiarize
  yourself with important App Studio concepts.

## Step 1: Create an application

The first step in generating an app is to describe the app that you want to create to the AI
assistant in App Studio. You can review the application that will be generated, and iterate as
desired before generating it.

###### To generate your app using AI

1. Sign in to App Studio.
2. In the left-hand navigation, choose **Builder hub** and choose **+ Create app**.
3. Choose **Generate an app with AI**.
4. In the **App name** field, provide a name for your app.
5. In the **Select data sources** dialog box, choose
   **Skip**.
6. You can start defining the app that you want to generate by describing it in the text box,
   or by choosing **Customize** on a sample prompt. After you describe your app,
   App Studio generates the app requirements and details for you to review. This includes use
   cases, user flows, and data models.
7. Use the text box to iterate with your app as needed until you're satisfied with the
   requirements and details.
8. When you're ready to generate your app and start building, choose **Generate
   app**.
9. Optionally, you can view a short video that details how to navigate around your new
   app.
10. Choose **Edit app** to enter the Development environment for your
    app.

## Step 2: Explore your new application

In the Development environment, you'll find the following resources:

- A canvas that you use to view or edit your application. The canvas changes depending on
  the resource that is selected.
- Navigation tabs at the top of the canvas. The tabs are described in the following
  list:
  - **Pages**: Where you use pages and components to design the UI of your
    app.
  - **Automations**: Where you use actions in automations to define the
    business logic of your app.
  - **Data**: Where you define entities, their fields, sample data, and
    data actions to define the data models of your app.
  - **App settings**: Where you define settings for your app, including app
    roles, which you use to define role-based visibility of pages for your end users.

- A left-side navigation menu, which contains resources based on which tab you're
  viewing.
- A right-side menu that lists resources and properties for selected resources in the
  **Pages** and **Automations** tabs.
- A debug console that displays warnings and errors at the bottom of the builder. There
  might be errors present in your generated app. This is likely due to automations that require a
  configured connector to perform actions, such as sending an email with Amazon Simple Email Service.
- An **Ask AI** chat window to get contextual help from the AI builder
  assistant.

Let's take a closer look at the **Pages**,
**Automations**, and **Data** tabs.

### Explore pages and components

The **Pages** tab shows pages and their components that were generated for
you.

Each page represents a screen of your application's user interface (UI) that your users
will interact with. On these pages, you can find various components (such as tables, forms, and
buttons) to create the desired layout and functionality.

Take some time to view the pages and their components by using the left-side navigation
menu. When you select a page or component, you can choose **Properties** on the
right-side menu.

### Explore automations and actions

The **Automations** tab shows automations and their actions that were
generated for you.

Automations define the business logic of your app, such as creating, viewing, updating, or
deleting data entries, sending emails, or even invoking APIs or Lambda functions.

Take some time to view the automations by using the left-side navigation menu. When you
choose an automation, you can view its properties on the right-side
**Properties** menu. An automation contains the following resources:

- Automations are made up of individual actions, which are the building blocks of your
  app's business logic. You can view the actions of an automation on the left-side navigation
  menu, or in the canvas of a selected automation. When you select an action, you can view its
  properties on the right-side **Properties** menu.
- Automation parameters are how data is passed into an automation. Parameters act as
  placeholders that are replaced with actual values when the automation is run. This allows you
  to use the same automation with different inputs each time.
- Automation output is where you configure the result of an automation. By default, an
  automation has no output, so to use an automation's result in components or other automations,
  you must define them here.

For more information, see [Automations concepts](automations-concepts.md "automations-concepts.md").

### Explore data with entities

The **Data** tab shows entities that were generated for you.

Entities represent tables that hold your application's data, similar to tables in a
database. Instead of connecting your application's user interface (UI) and automations directly
to data sources, they connect to entities first. Entities act as an intermediary between your
actual data source and your App Studio app. This provides a single place to manage and access
your data.

Take some time to view the entities that were generated by choosing them from the left-side
navigation menu. You can review the following details:

- The **Configuration** tab shows the entity name and its fields, which
  represent the columns of your entity.
- The **Data actions** tab shows the data actions that were generated with
  your entity. Components and automations can use data actions to fetch data from your
  entity.
- The **Sample data** tab shows sample data, which you can use to test
  your app in the Development environment (which doesn't communicate with external services).
  For more information about environments, see [Application environments](applications-publish.md#application-environments "applications-publish.md#application-environments").
- The **Connection** tab shows information about the external data sources
  that the entity is connected to. App Studio provides a managed data storage solution that
  uses a DynamoDB table. For more information, see [Managed data entities in AWS App Studio](managed-data-entities.md "managed-data-entities.md").

## Step 3: Preview your application

You can preview an application in App Studio to see how it appears to users. You can also
test its functionality by using it and checking logs in a debug panel.

The application preview environment doesn't support displaying live data or the connection
with external resources with connectors, such as data sources. Instead, you can use sample data
and mocked output to test functionality.

###### To preview your app for testing

1. In the top-right corner of the app builder, choose **Preview**.
2. Interact with the pages of your app.

## Next steps

Now that you've created your first app, here are some next steps:

- For another getting started walkthrough that includes images, see the blog post [Build enterprise-grade applications with natural language using AWS App Studio
  (preview)](https://aws.amazon.com/blogs/aws/build-custom-business-applications-without-cloud-expertise-using-aws-app-studio-preview "https://aws.amazon.com/blogs/aws/build-custom-business-applications-without-cloud-expertise-using-aws-app-studio-preview").
- Apps use connectors to send and receive data, or to communicate with external services
  (both AWS services and third-party services). It's necessary to learn more about connectors
  and how to configure them to build apps. Note that you must have the **Admin**
  role to manage connectors. To learn more, see [Connect App Studio to other services with connectors](connectors.md "connectors.md").
- To learn more about previewing, publishing, and eventually sharing your app to end users,
  see [Previewing, publishing, and sharing applications](applications-preview-publish-share.md "applications-preview-publish-share.md").
- Keep exploring and updating the app that you generated for some hands-on
  experience.
- To learn more about building apps, check out the [Builder documentation](builder-documentation.md "builder-documentation.md"). Specifically, the following topics might be useful to
  explore:
  - [Automation actions reference](automations-actions-reference.md "automations-actions-reference.md")
  - [Components reference](components-reference.md "components-reference.md")
  - [Interacting with Amazon Simple Storage Service with components and automations](automations-s3.md "automations-s3.md")
  - [Security considerations and mitigations](security-considerations-and-mitigations.md "security-considerations-and-mitigations.md")
