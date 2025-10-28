# Automations concepts

Here are some concepts and terms to know when defining and configuring your app's business logic using automations in App Studio.

## Automations

**Automations** are how you define the business logic of your application.
The main components of an automation are: triggers that start the automation, a sequence of one or more actions, input parameters used to pass data to the automation, and an output.

## Actions

An automation action, commonly referred to as an **action**,
is an individual step of logic that make up an automation. Each action performs a specific task, whether it's sending an email, creating a data record, invoking a Lambda function,
or calling APIs. Actions are added to automations from the action library, and can be grouped into conditional statements or loops.

## Automation input parameters

**Automation input parameters** are dynamic input values that you can pass in from components to automations to make them
flexible and reusable. Think of parameters as variables for your automation, instead of hard-coding values into an automation,
you can define parameters and provide different values when needed.
Parameters allow you to use the same automation with different inputs each time it is run.

## Mocked output

Some actions interact with external resources or services using connectors. When using
the preview environment, applications do not interact with external services. To test actions that use
connectors in the preview environment, you can use **mocked output** to simulate the
connector's behavior and output. The mocked output is configured using JavaScript, and the result is stored
in an action's results, just as the connector's response is stored in a published app.

By using mocking, you can use the preview environment to test various scenarios and their impact on other actions with the automation
such as simulating different result values, error scenarios, edge cases, or unhappy paths without calling the external
service through connectors.

## Automation output

An **automation output** is used to pass values from one automation to other resources of an app,
such as components or other automations. Automation outputs are configured as expressions, and the expression can return a static
value or a dynamic value computed from automation parameters and actions. By default, automations do not return any data, including the results of
actions within the automation.

A couple of examples of how automation outputs can be used:

- You can configure an automation output to return an array, and pass that array to populate a data component.
- You can use an automation to calculate a value, and pass that value into multiple other automations as a way to
  centralize and reuse business logic.

## Triggers

A **trigger** determines when, and on what conditions, an automation will run. Some examples of triggers are
`On click` for buttons and `On select` for text inputs. The type of component determines the list of available triggers for that component.
Triggers are added to [components](concepts.md#concepts-component "concepts.md#concepts-component") and configured in the application studio.
