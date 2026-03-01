# How AWS App Studio works

There are a few key concepts to understand when using AWS App Studio to build
applications. This topic covers the basics of the following concepts or resources:

- Using _connectors_ to connect to other services to use their resources or
  API calls in your application. For example, you can use connectors to store and access data, or
  send notifications from your app.
- Using _entities_ to configure the data model of your application, which connects your application with your external data source.
- Using _pages_ and _components_ to build the user interface (UI) of your application.
- Using _automations_ and _actions_ to implement the logic or behavior of your application.
- The application development lifecycle in App Studio: building, testing, and publishing.
  For more information about App Studio concepts, see [AWS App Studio concepts](concepts.md "concepts.md").

The following image is a simple diagram of how App Studio and its resources are
organized.

![A simple diagram that shows the organization of resources in an App Studio application.](images/app-studio-diagram.png)
Within an app in App Studio, pages, automations, and entities all interact with one
another. You use connectors to connect these resources to external services such as data, storage,
or notification providers. To successfully build an app, it’s crucial to understand how all of
these concepts and resources interact with one another.

## Connecting your application to other services

One of the biggest benefits of using App Studio to build applications is being able to
easily integrate your app with other services. In App Studio, you connect to other services by
using connectors that are specific to the service and the resources or API calls you want to use
with your application.

You create connectors at the App Studio instance level, and not in individual apps. After
you create connectors, you can use them in various parts of applications, depending on the
connected service and the application.

The following are examples of functionality in applications that use connectors to
connect to other services:

- The most common use case, used in almost all applications, is to store and access data used in
  the application by connecting to AWS data services such as Amazon Redshift, Amazon DynamoDB, or
  Amazon Aurora.
- An application that allows uploading and viewing images, such as receipts, can use Amazon S3 to store and access the image files.
- A text summarizer app can send a text input to Amazon Bedrock and show the returned summary.

###### Note

You must have the Admin role in App Studio to create connectors. When creating connectors,
you must include proper credentials and information about the resources or API calls that you
want to use.

## Configuring the data model of your application

Your application’s data is the information that powers the application. In
App Studio, you create and use _entities_ that represent the different types
of data that you store and work with. For example, in a tracking application for customer
meetings, you might have three entities that represent customer meetings, the agendas, and the
attendees.

Entities contain fields that have types, such as integer or string, that describe the
data being stored. Although you use entities to define your data model, you must connect your
entity to an external data storage service such as Amazon Redshift or Amazon DynamoDB to store the data. You can
think of an entity as an intermediary between your App Studio application and the data in the
external service.

You can use data actions to interact with the data in your application from components
and automations. The two most common data actions to use are a `getAll` action and a
`getByID` action. For example, your application could use the `getAll`
data action to populate a table with your data, and a `getByID` action to populate a
detail component with more information about a specific data entry.

You can also add sample data to your entity to more easily test your application without needing to call external services.

## Building your application's UI

In App Studio, you build your application’s UI with _pages_ and
_components_. Pages are individual screens of your application and are
containers for components. Components are the building blocks of your application’s UI. There are
many types of components, such as tables, forms, image viewers, and buttons.

The following image shows the **Pages** tab of the application studio,
where you add or configure pages and components in your application. The following key areas are
highlighted and numbered:

1. The left-side **Pages** panel. This is where you manage pages, the
   application header, and the navigation settings. You can view all of the pages and components
   of your application.
2. The **canvas**, which displays the current page’s components. You can choose the components in the
   canvas to configure their properties.
3. The right-side **Components** or **Properties** panel. With
   nothing selected, the Components panel is shown, which displays the list of components that can
   be added to your page. If you select a page or component, the Properties panel is shown, where
   you configure the page or component.
4. The bottom **Errors** and **Warnings** panels. These panels
   display any errors or warnings in your application, which are most commonly from configuration
   issues. You can choose the panel to expand it and see the messages.

![A view of the Pages tab of the application studio that is displayed while you edit an app.](images/pages-components.png)

As an example, applications where users have to input information might have the
following pages and components:

- An input page that includes a form component that users use to fill out and submit
  information.
- A list view page that contains a table component with information about each input.
- A detailed view page that contains a detail component with more information about each
  input.

Components can include static information or data, such as a form with defined fields.
They can also include dynamic information by using automations, such as an image viewer that
retrieves an image from an Amazon S3 bucket and displays it to the user.

It's important to understand the concept of _page parameters_. You use
page parameters to send information from one page to another. A common example of a use case for
page parameters is searching and filtering, where the search term from one page is sent to the
table or list of items to filter on in another page. Another use case example is viewing item
details, where the item identifier is sent to a detailed viewer page.

## Implementing the logic or behavior of your application

You can think of the logic or behavior of your application as the functionality of the
application. You can define what happens when a user chooses a button, submits information,
navigates to a new page, or interacts in other ways. In App Studio, you define the logic of your
application with _automations_ and _actions_. Automations
are containers for actions, which are the building blocks of the functionality of
automations.

The following image shows the **Automations** tab of the application
studio, where you add or configure automations and their actions in your application. The
following key areas are highlighted and numbered:

- The left-side **Automations** panel. This is where you manage automations.
  You can view all of the automations and actions of your application.
- The **canvas**, which displays the current automation. It displays the
  configured automation parameters (which are explained later in this section) and actions. You
  can choose the components in the canvas to configure their properties.
- The right-side **Actions** and **Properties** panels. With
  nothing selected, the Actions panel is shown. It displays the list of actions that can be added
  to your automation. If you select an automation, you can view and configure its properties,
  such as the input and output of the automation. If you select an action, you can view and
  configure the action’s properties.
- The bottom **Errors** and **Warnings** panels. This panel
  displays any errors or warnings in your application (most commonly from configuration issues).
  You can choose the panel to expand it and see the messages.

![The Automations tab of the application studio, where you can create, configure, and manage automations and actions while editing an app.](images/automations-actions.png)

Automations can be simple (such as adding numbers and returning the result), or more
powerful (such as sending an input to another service and returning the result). The main
components of an automation are as follows:

- A _trigger_, which defines when the automation is run. An example is
  when the user presses a button in the UI.
- An _automation input_, which sends information to the
  automation. You define automation inputs with _automation parameters_. For
  example, if you want to use Amazon Bedrock to return a summary of text to the user, you configure the
  text to be summarized as an automation parameter.
- _Actions_, which are the building blocks of an automation’s
  functionality. You can think of each action as a step in the automation. Actions can call APIs,
  invoke custom JavaScript, create data records, and perform other functions. You can also group
  actions into loops or conditions to further customize the functionality. You can also invoke
  other automations with an action.
- An _automation output_, which you can use in components or even other
  automations. For example, the automation output could be text that is shown in a text
  component, an image to be shown in an image viewer component, or the input to another
  automation.

## The development lifecycle of your application

The development lifecycle of your application includes the following stages: building, testing, and publishing. It’s called a cycle,
because you will likely be iterating through and between these stages as you create and iterate upon your application.

The following image shows a simplified timeline of the application development
lifecycle in App Studio:

![A timeline diagram of the application development lifecycle, which includes building, previewing, testing, production, and sharing.](images/app-studio-development-lifecycle.png)

App Studio offers various tools to support the lifecycle of your application. These
tools include the following three distinct environments, which are shown in the previous
diagram:

- The Preview environment, where you can preview your application to see how it looks to end
  users, and test specific functionality. Use the Preview environment to quickly test and iterate
  on your application without needing to publish it. Applications in the preview environment
  don't communicate or transfer data with external services. This means that you can't test
  interactions and functionality that rely on external services in the Preview
  environment.
- The Testing environment, where you can test your application’s connection and interactions
  with external services. This is also where you can do end-user testing by sharing the version
  published to the Testing environment to groups of testers.
- The Production environment, where you can perform final testing of new apps before sharing
  them with end users. After the apps are shared, the version of the application that is
  published to the Production environment is the version that end users will view and use.

## Learn more

Now that you know the basics of how application development works in App Studio, you can either start building
an application of your own, or dive deeper into learning more about concepts and resources.

To start building, we recommend that you try one of the getting started
tutorials:

- Follow [Tutorial: Generate an app using AI](getting-started-tutorial-ai.md "getting-started-tutorial-ai.md") to learn how to use the AI builder assistant to get a head start on building an app.
- Follow [Tutorial: Start building from an empty app](getting-started-tutorial-empty.md "getting-started-tutorial-empty.md") to learn how to build an app from scratch while
  learning the basics.

To learn more about the resources or concepts mentioned in this topic, see the following topics:

- [Connect App Studio to other services with connectors](connectors.md "connectors.md")
- [Entities and data actions: Configure your app's data model](data.md "data.md")
- [Pages and components: Build your app's user interface](pages-components-ux.md "pages-components-ux.md")
- [Automations and actions: Define your app's business logic](automations.md "automations.md")
- [Previewing, publishing, and sharing applications](applications-preview-publish-share.md "applications-preview-publish-share.md")
