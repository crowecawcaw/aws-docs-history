

# AWS App Studio concepts
<a name="concepts"></a>

Get familiar with the key App Studio concepts to help speed up creating applications and automating processes for your team. These concepts include terms used throughout App Studio for both administrators and builders.

**Topics**
+ [Admin role](#concepts-administrator)
+ [Application (app)](#concepts-application)
+ [Automation](#concepts-automation)
+ [Automation actions](#concepts-action)
+ [Builder role](#concepts-builder)
+ [Component](#concepts-component)
+ [Connector](#concepts-connector)
+ [Development environment](#concepts-development-environment)
+ [Entity](#concepts-entity)
+ [Instance](#concepts-instance)
+ [Page](#concepts-page)
+ [Trigger](#concepts-trigger)

## Admin role
<a name="concepts-administrator"></a>

**Admin** is a role that can be assigned to a group in App Studio. Admins can manage users and groups within App Studio, add and manage connectors, and manage applications created by builders. Additionally, users with the Admin role have all of the permissions included with the Builder role.

Only users with the Admin role have access to the **Admin Hub**, which contains tools to manage roles, data sources, and applications.

## Application (app)
<a name="concepts-application"></a>

An **application** (app) is a single software program that is developed for end-users to accomplish specific tasks. Apps in App Studio include assets such as UI pages and components, automations, and data sources that users can interact with.

## Automation
<a name="concepts-automation"></a>

**Automations** are how you define the business logic of your application. The main components of an automation are: triggers that start the automation, a sequence of one or more actions, input parameters used to pass data to the automation, and an output.

## Automation actions
<a name="concepts-action"></a>

An automation action, commonly referred to as an **action**, is an individual step of logic that make up an automation. Each action performs a specific task, whether it's sending an email, creating a data record, invoking a Lambda function, or calling APIs. Actions are added to automations from the action library, and can be grouped into conditional statements or loops.

## Builder role
<a name="concepts-builder"></a>

**Builder** is a role that can be assigned to a group in App Studio. Builders can create and build applications. Builders cannot manage users or groups, add or edit connector instances, or manage other builders' applications.

Users with the Builder role have access to the **Builder Hub**, which contains details about resources such as the applications that the builder has access to along with helpful information such as learning resources.

## Component
<a name="concepts-component"></a>

**Components** are individual functional items within the UI of your application. Components are contained in pages, and some components can serve as a container for other components. Components combine UI elements with the business logic you want that UI element to perform. For example, one type of component is a form, where users can enter information in fields and, once submitted, that information is added as a database record.

## Connector
<a name="concepts-connector"></a>

A **connector** is a connection between App Studio and other AWS services, such as AWS Lambda and Amazon Redshift, or third-party services. Once a connector is created and configured, builders can use it and the resources it connects to App Studio in their applications.

Only users with the Admin role can create, manage, or delete connectors.

## Development environment
<a name="concepts-development-environment"></a>

The **Development environment** is a visual tool to build applications. This environment includes the following tabs for building apps:
+ Pages: Where builders design their applications with [pages](#concepts-page) and [components](#concepts-component).
+ Automations: Where builders design their application's business logic with [automations](#concepts-automation).
+ Data: Where builders design their application's data model with [entities](#concepts-entity).

The Development environment also contains a debug console, and an AI chat window to get contextual help while building. Builders can preview their in-progress applications from the Development environment.

## Entity
<a name="concepts-entity"></a>

**Entities** are data tables in App Studio. Entities interact directly with tables in data sources. Entities include fields to describe the data in them, queries to locate and return data, and mapping to connect the entity's fields to a data source's columns.

## Instance
<a name="concepts-instance"></a>

An **instance** is a logical container for all of your App Studio resources. It represents you, your company, team, or organization, and contains all of your App Studio resources, such as applications, connectors, and role assignments for users and groups. Larger organizations or enterprises commonly have multiple App Studio instances, for example: a sandbox, testing, and production instance. You create an instance as part of setting up App Studio.

## Page
<a name="concepts-page"></a>

**Pages** are containers for [components](#concepts-component), which make up the UI of an application in App Studio. Each page represents a screen of your application's user interface (UI) that your users will interact with. Pages are created and edited in the **Pages** tab of the application studio.

## Trigger
<a name="concepts-trigger"></a>

A **trigger** determines when, and on what conditions, an automation will run. Some examples of triggers are `On click` for buttons and `On select` for text inputs. The type of component determines the list of available triggers for that component. Triggers are added to [components](#concepts-component) and configured in the application studio. 