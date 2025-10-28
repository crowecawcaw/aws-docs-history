# Tutorial: Start building from an empty

app

In this tutorial, you'll build an internal Customer Meeting Request application using
AWS App Studio. You'll learn about how to build apps in App Studio, while focusing on real-world
use cases and hands-on examples. Also, you'll learn about defining data structures, UI design, and
app deployment.

###### Note

This tutorial details how to build an app from scratch, starting with an empty app.
Typically, it's much quicker and easier to use AI to help generate an app and its resources by
providing a description of the app you want to create. For more information, see [Tutorial: Generate an app using AI](getting-started-tutorial-ai.md "getting-started-tutorial-ai.md").

The key to understanding how to build applications with App Studio is to understand the
following four core concepts and how they work together: **components**, **automations**, **data**, and **connectors**.

- **Components**: Components are the building blocks of your
  application's user interface. They represent visual elements like tables, forms, and buttons.
  Each component has its own set of properties, which you can customize to fit your specific
  requirements.
- **Automations**: With automations, you can define the logic
  and workflows that govern how your application behaves. You can use automations to create,
  update, read, or delete rows in a data table or to interact with objects in an Amazon S3 bucket. You
  can also use them to handle tasks like data validation, notifications, or integrations with
  other systems.
- **Data**: Data is the information that powers your
  application. In App Studio, you can define data models, called _entities_.
  Entities represent the different types of data that you need to store and work with, such as
  customer meeting requests, agendas, or attendees. You can connect these data models to a variety
  of data sources, including AWS services and external APIs, by using App Studio
  connectors.
- **Connectors**: App Studio provides connections with a wide
  range of data sources, which include AWS services such as Aurora, DynamoDB, and Amazon Redshift. The data
  sources also include third-party services such as Salesforce, or many others using OpenAPI or
  generic API connectors. You can use App Studio connectors to easily incorporate data and
  functionality from these enterprise-grade services and external applications into your
  applications.
  As you progress through the tutorial, you'll explore how the key concepts of components,
  data, and automation come together to build your internal Customer Meeting Request application.

The following are high-level steps that describe what you'll do in this tutorial:

1. **Start with data**: Many applications begin with a data
   model, so this tutorial begins with data as well. To build the Customer Meeting Request app,
   you'll start by creating a `MeetingRequests` entity. This entity represents the data
   structure for storing all the relevant meeting request information, such as customer name,
   meeting date, agenda, and attendees. This data model serves as the foundation for your
   application, and powers the various components and automations you'll build.
2. **Create your user interface (UI)**: With the data model in
   place, the tutorial then guides you through building the user interface (UI). In App Studio,
   you build the UI by adding _pages_ and adding _components_
   to them. You'll add components like _Tables_, _Detail
   views_, and _Calendars_ to a meeting request dashboard page. These
   components will be designed to display and interact with the data stored in the
   `MeetingRequests` entity. This allows your users to view, manage, and schedule
   customer meetings. You will also create a meeting request creation page. This page includes a
   _Form_ component to collect data and a _Button_ component
   to submit it.
3. **Add business logic with automations**: To enhance the
   functionality of your application, you'll configure some of the components to enable user
   interactions. Some examples are navigating to a page or creating a new meeting request record in
   the `MeetingRequests` entity.
4. **Enhance with validation and expressions**: To ensure the
   integrity and accuracy of your data, you'll add validation rules to the
   _Form_ component. This will help make sure that users provide complete and
   valid information when creating new meeting request records. Also, you'll use expressions to
   reference and manipulate data within your application so you can display dynamic and contextual
   information throughout your user interface.
5. **Preview and test**: Before deploying your application,
   you'll have the opportunity to preview and test it thoroughly. This will allow you to verify
   that the components, data, and automations are all working together seamlessly. This provides
   your users with a smooth and intuitive experience.
6. **Publish the application**: Finally, you'll deploy your
   completed internal Customer Meeting Request application and make it accessible to your users.
   With the power of the low-code approach in App Studio, you'll have built a custom application
   that meets the specific needs of your organization, without the need for extensive programming
   expertise.

###### Contents

- [Prerequisites](getting-started-tutorial-empty.md#getting-started-tutorial-prerequisites "getting-started-tutorial-empty.md#getting-started-tutorial-prerequisites")
- [Step 1: Create an
  application](getting-started-tutorial-empty.md#getting-started-tutorial-steps-create-application "getting-started-tutorial-empty.md#getting-started-tutorial-steps-create-application")
- [Step 2: Create an entity to define
  your app's data](getting-started-tutorial-empty.md#getting-started-tutorial-steps-create-entity "getting-started-tutorial-empty.md#getting-started-tutorial-steps-create-entity")
  - [Create a managed
    entity](getting-started-tutorial-empty.md#getting-started-tutorial-steps-create-managed-entity "getting-started-tutorial-empty.md#getting-started-tutorial-steps-create-managed-entity")
  - [Add fields to your entity](getting-started-tutorial-empty.md#getting-started-tutorial-steps-add-fields "getting-started-tutorial-empty.md#getting-started-tutorial-steps-add-fields")

- [Step 3: Design the user interface
  (UI) and logic](getting-started-tutorial-empty.md#getting-started-tutorial-steps-user-interface "getting-started-tutorial-empty.md#getting-started-tutorial-steps-user-interface")
  - [Add a meeting
    request dashboard page](getting-started-tutorial-empty.md#getting-started-tutorial-steps-user-interface-create-page "getting-started-tutorial-empty.md#getting-started-tutorial-steps-user-interface-create-page")
  - [Add a
    meeting request creation page](getting-started-tutorial-empty.md#getting-started-tutorial-steps-user-interface-add-create-customer-page "getting-started-tutorial-empty.md#getting-started-tutorial-steps-user-interface-add-create-customer-page")

- [Step 4: Preview the application](getting-started-tutorial-empty.md#getting-started-tutorial-steps-preview "getting-started-tutorial-empty.md#getting-started-tutorial-steps-preview")
- [Step 5: Publish the application to the
  Testing environment](getting-started-tutorial-empty.md#getting-started-tutorial-steps-publish "getting-started-tutorial-empty.md#getting-started-tutorial-steps-publish")
- [Next steps](getting-started-tutorial-empty.md#getting-started-tutorial-next-steps "getting-started-tutorial-empty.md#getting-started-tutorial-next-steps")

## Prerequisites

Before you get started, review and complete the following prerequisites:

- Access to AWS App Studio. For more information, see [Setting up and signing in to AWS App Studio](setting-up.md "setting-up.md").
- Optional: Review [AWS App Studio concepts](concepts.md "concepts.md") to familiarize
  yourself with important App Studio concepts.
- Optional: An understanding of basic web development concepts, such as JavaScript
  syntax.
- Optional: Familiarity with AWS services.

## Step 1: Create an

application

1. Sign in to App Studio.
2. In the left-hand navigation, choose **Builder hub** and choose
   **+ Create app**.
3. Choose **Start from scratch**.
4. In the **App name** field, provide a name for your app, such as
   `Customer Meeting Requests`.
5. If asked to select data sources or a connector, choose **Skip** for the
   purposes of this tutorial.
6. Choose **Next** to proceed.
7. (Optional): Watch the video tutorial for a quick overview of building apps in
   App Studio.
8. Choose **Edit app**, which brings you into the App Studio app
   builder.

## Step 2: Create an entity to define

your app's data

Entities represent tables that hold your application's data, similar to tables in a
database. Instead of your application's user interface (UI) and automations connecting directly
to data sources, they connect to entities first. Entities act as an intermediary between your
actual data source and your App Studio app, and provide a single place to manage and access your
data.

There are four ways to create an entity. For this tutorial, you will use the App Studio
managed entity.

### Create a managed

entity

Creating a managed entity also creates a corresponding DynamoDB table that App Studio
manages. When changes are made to the entity in the App Studio app, the DynamoDB table is updated
automatically. With this option, you don't have to manually create, manage, or connect to a
third-party data source, or designate mapping from entity fields to table columns.

When creating an entity, you must define a **primary key**
field. A primary key serves as a unique identifier for each record or row in the entity. This
ensures that each record can be easily identified and retrieved without ambiguity. The primary
key consists of the following properties:

- Primary key name: A name for the primary key field of the entity.
- Primary key data type: The type of the primary key field. In App Studio, supported
  primary key types are **String** for text and **Float** for
  a number. A text primary key (like `meetingName`) would have a type
  of **String**, and a numerical primary key (like
  `meetingId`) would have a type of **Float**.

The primary key is a crucial component of an entity because it enforces data integrity,
prevents data duplication, and enables efficient data retrieval and querying.

###### To create a managed entity

1. Choose **Data** from the top bar menu.
2. Choose **+ Create entity**.
3. Choose **Create App Studio managed entity**.
4. In the **Entity name** field, provide a name for your entity. For this
   tutorial, enter `MeetingRequests`.
5. In the **Primary key** field, enter the primary key name label to give
   to the primary key column in your entity. For this tutorial, enter
   `requestID`.
6. For **Primary key data type**, choose **Float**.
7. Choose **Create entity**.

### Add fields to your entity

For each field, you will specify the **display name**, which is the label
that is visible to app users. The display name can contain spaces and special characters, but it
must be unique within the entity. The display name serves as a user-friendly label for the
field, and helps users easily identify and understand its purpose.

Next, you’ll provide the **system name**, a unique identifier used
internally by the application to reference the field. The system name should be concise, with no
spaces or special characters. The system name allows the application to make changes to the
field's data. It acts as a unique reference point for the field within the application.

Finally, you’ll select the **data type** that best represents the kind of
data you want to store in the field, such as String (text), Boolean (true/false), Date, Decimal,
Float, Integer, or DateTime. Defining the appropriate data type ensures data integrity and
enables proper handling and processing of the field's values. For instance, if you're storing
customer names in your meeting request, you would select the `String` data type to
accommodate text values.

###### To add fields to your `MeetingRequests` entity

- Choose **+ Add field** to add the following four fields:
  1.  Add a field that represents a customer's name with the following information:
      - **Display name**: `Customer name`
      - **System name**: `customerName`
      - **Data type**: `String`

  2.  Add a field that represents the meeting date with the following information:
      - **Display name**: `Meeting date`
      - **System name**: `meetingDate`
      - **Data type**: `DateTime`

  3.  Add a field that represents the meeting agenda with the following information:
      - **Display name**: `Agenda`
      - **System name**: `agenda`
      - **Data type**: `String`

  4.  Add a field to represent the meeting attendees with the following information:
      - **Display name**: `Attendees`
      - **System name**: `attendees`
      - **Data type**: `String`

You can add sample data to your entity that you can use to test and preview your
application before publishing it. By adding up to 500 rows of mock data, you can simulate
real-world scenarios and examine how your application handles and displays various types of
data, without relying on actual data or connecting to external services. This helps you to
identify and resolve any issues or inconsistencies early in the development process. This
ensures that your application functions as intended when dealing with actual data.

###### To add sample data to your entity

1. Choose the **Sample data** tab in the banner.
2. Choose **Generate more sample data**.
3. Choose **Save**.

Optionally, choose **Connection** in the banner to review the details
about the connector and the DynamoDB table created for you.

## Step 3: Design the user interface

(UI) and logic

### Add a meeting

request dashboard page

In App Studio, each page represents a screen of your application's user interface (UI)
that your users will interact with. Within these pages, you can add various components such as
tables, forms, and buttons to create the desired layout and functionality.

Newly created applications come with a default page, so you'll rename that one instead of
adding a new one to use as a simple meeting request dashboard page.

###### To rename the default page

1. In the top bar navigation menu, choose **Pages**.
2. In the left-side panel, double-click **Page1**, rename it to
   `MeetingRequestsDashboard`, and press **Enter**.

Now, add a table component to the page that will be used to display meeting
requests.

###### To add a table component to the meeting requests dashboard page

1. In the right-hand **Components** panel, locate the
   **Table** component and drag it onto the canvas.
2. Choose the table in the canvas to select it.
3. In the right-side **Properties** panel, update the following
   settings:
   1. Choose the pencil icon to rename the table to
      `meetingRequestsTable`.
   2. In the **Source** dropdown, choose **Entity**.
   3. In the **Data actions** dropdown, choose the entity you created
      (`MeetingRequests`) and choose **+ Add data
      actions**.

4. If prompted, choose **getAll**.

###### Note

The **getAll** data action is a specific type of data
action that retrieves all the records (rows) from a specified entity. When you associate the
getAll data action with a table component, for example, the table automatically populates
with all the data from the connected entity, and displays each record as a row in the
table.

### Add a

meeting request creation page

Next, create a page that contains a form that end users will use to create meeting
requests. You will also add a submit button that creates the record in the
`MeetingRequests` entity, and then navigates the end user back to the
`MeetingRequestsDashboard` page.

###### To add a meeting request creation page

1. In the top banner, choose **Pages**.
2. In the left-side panel, choose **+ Add**.
3. In the right-side properties panel, select the pencil icon and rename the page to
   `CreateMeetingRequest`.

Now that the page is added, you will add a form to the page that end users will use to
input information to create a meeting request in the `MeetingRequests` entity.
App Studio offers a method of generating a form from an existing entity, which autopopulates
the form fields based on the entity's fields and also generates a submit button for creating a
record in the entity with the form inputs.

###### To automatically generate a form from an entity on the meeting request creation

page

1. On the right-side **Components** menu, find the
   **Form** component and drag it onto the canvas.
2. Select **Generate form**.
3. From the dropdown, select the `MeetingRequests` entity.
4. Choose **Generate**.
5. Choose the **Submit** button on the canvas to select it.
6. In the right-side properties panel, in the **Triggers** section, choose
   **+ Add**.
7. Choose **Navigate**.
8. In the right-side properties panel, change the **Action name** to
   something descriptive, such as `Navigate to
MeetingRequestsDashboard`.
9. Change the **Navigation type** to page. In the **Navigate
   to** dropdown, choose `MeetingRequestsDashboard`.

Now that we have a meeting request creation page and form, we want to make it easy to
navigate to this page from the `MeetingRequestsDashboard` page, so that end users
reviewing the dashboard can easily create meeting requests. Use the following procedure to
create a button on the `MeetingRequestsDashboard` page that navigates to the
`CreateMeetingRequest` page.

###### To add a button to navigate from `MeetingRequestsDashboard` to

`CreateMeetingRequest`

1. In the top banner, choose **Pages**.
2. Choose the `MeetingRequestsDashboard` page.
3. In the right-side **Components** panel, find the
   **Button** component, drag it onto the canvas, and place it above the
   table.
4. Choose the newly added button to select it.
5. In the right-side **Properties** panel, update the following
   settings:
   1. Select the pencil icon to rename the button to
      `createMeetingRequestButton`.
   2. **Button label**: `Create Meeting Request`. This
      is the name that end users will see.
   3. In the **Icon** dropdown, select **+ Plus**.
   4. Create a trigger that navigates the end user to the
      `MeetingRequestsDashboard` page:
      1. In the **Triggers** section, choose **+
         Add**.
      2. In **Action Type**, select **Navigate**.
      3. Choose the trigger that you just created to configure it.
      4. In **Action name**, provide a descriptive name such as
         `NavigateToCreateMeetingRequest`.
      5. In the **Navigate type** dropdown, select
         **Page**.
      6. In the **Navigate to** dropdown, select the
         `CreateMeetingRequest` page.

## Step 4: Preview the application

You can preview an application in App Studio to see how it will appear to users. Also, you
can test its functionality by using it and checking logs in a debug panel.

The application preview environment doesn't support displaying live data. It also doesn't
support the connection with external resources with connectors, such as data sources. Instead,
you can use sample data and mocked output to test functionality.

###### To preview your app for testing

1. In the top-right corner of the app builder, choose **Preview**.
2. Interact with the `MeetingRequestsDashboard` page, and test the table, form,
   and buttons.

## Step 5: Publish the application to the

**Testing** environment

Now that you're done creating, configuring, and testing your application, it's time to
publish it to the **Testing** environment to perform final testing and then
share it with users.

###### To publish your app to the Testing environment

1. In the top-right corner of the app builder, choose **Publish**.
2. Add a version description for the Testing environment.
3. Review and select the checkbox regarding the SLA.
4. Choose **Start**. Publishing might take up to 15 minutes.
5. (Optional) When you're ready, you can give others access by choosing
   **Share** and following the prompts.

###### Note

To share apps, an Admin must have created end-user groups.

After testing, choose **Publish** again to promote the application to the
Production environment. For more information about the different application environments, see
[Application environments](applications-publish.md#application-environments "applications-publish.md#application-environments").

## Next steps

Now that you've created your first app, here are some next steps:

1.  Keep building the tutorial app. Now that you have data, some pages, and an automation
    configured, you can add additional pages and add components to learn more about building
    apps.
2.  To learn more about building apps, see the [Builder documentation](builder-documentation.md "builder-documentation.md"). Specifically, the following topics might be useful to
    explore:

        * [Automation actions reference](automations-actions-reference.md "automations-actions-reference.md")
        * [Components reference](components-reference.md "components-reference.md")
        * [Interacting with Amazon Simple Storage Service with components and automations](automations-s3.md "automations-s3.md")
        * [Security considerations and mitigations](security-considerations-and-mitigations.md "security-considerations-and-mitigations.md")

    In addition, the following topics contain more information about concepts discussed in the
    tutorial:

        * [Previewing, publishing, and sharing applications](applications-preview-publish-share.md "applications-preview-publish-share.md")
        * [Creating an entity in an App Studio app](data-entities-create.md "data-entities-create.md")
