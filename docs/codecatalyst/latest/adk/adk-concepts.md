# Custom actions concepts

Here are some concepts to know about as you work with the Action Development Kit (ADK) to
develop custom actions.

## ADK components

The ADK has two components:

- **ADK command line interface (CLI)** – Tool to
  interact with a set of commands you can use to create, validate, and test actions.
- **ADK software development kit (SDK)** – A set of
  library interfaces you can use to interact with action metadata and CodeCatalyst resources, including
  actions, workflows, secrets, logs, input variables, output variables, artifacts, and reports.

## Action components

An action contains two components:

- **Action definition** – Provides the speciﬁcation for
  integration with Amazon CodeCatalyst CI/CD workflows. It defines the basic configuration for
  the action such as inputs, outputs,
  language, permissions, and run
  entry
  point. This `action.yml` file provides necessary
  information to a CodeCatalyst workflow of what the action interface and the execution profile looks
  like.
- **Action code** – The actual source code that is run when an
  action starts on CodeCatalyst. For the action to succeed, the action code must conform with the
  runtime proﬁle as deﬁned in the action definition. The code then runs on the compute provided
  in the action definition. For example, a runtime profile can include Node.js and the Amazon Elastic Compute Cloud
  (Amazon EC2) compute type.
