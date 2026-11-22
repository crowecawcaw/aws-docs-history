

# Orchestrate end-to-end business processes using AWS Quick Automate

## Overview
<a name="automate-overview"></a>

AWS Quick Automate is an AI-powered application that creates sophisticated automations using natural language or documentation. AWS Quick Automate revolutionizes enterprise workflow by transforming complex processes into intelligent, adaptive automations.

**Availability**  
AWS Quick Automate is available only for AWS Quick accounts provisioned through the AWS Management Console. It is not available for Free or Plus accounts created at [aws.com/quick](https://aws.com/quick).

Enterprises struggle to automate end-to-end business processes due to the growing complexity of their application ecosystems and the limitations of traditional automation tools. AWS Quick Automate provides the easiest way for businesses to build, deploy, and continuously maintain workflow automations with the set of capabilities needed to support complex use cases that span multiple applications, data sources, and departments.

You can provide your process requirements by uploading process documents or by describing your business process in natural language. From the documents or description, AWS Quick Automate creates a plan with steps and actions for your automation. You can expand upon the plan by adding additional steps or actions or modify the existing steps or actions. You can add additional steps by dragging actions or steps from an extensive Actions library.

AWS Quick Automate's intelligent agents can seamlessly navigate and interact with web applications, make contextual decisions based on real-time data, execute API calls, and even generate custom code to handle complex scenarios. When human oversight is required, the system can create human-in-the-loop tasks for manual review or approval.

## Choosing between Quick Flows and Quick Automate
<a name="flows-vs-automate"></a>

The right choice depends on the scope and complexity of what you need to automate. Quick Flows is documented as part of the Customize experience. For more information about Quick Flows, see [Flows](working-with-flows.md).
+ **User and ownership model.** Choose Quick Flows for personal and team productivity tasks, run by individual users. Choose Quick Automate for centralized, enterprise-wide automations, especially those that need to run independently of an individual user.
+ **Workflow scope and duration.** Use Quick Flows for shorter-running tasks such as generating reports, drafting content, or responding to tickets. Use Quick Automate for long-running and high-volume processes such as managing loan applications, processing invoices, and validating new vendor compliance.
+ **Customization.** Quick Flows offers a simple but powerful set of no-code building blocks for your workflows. Quick Automate gives additional advanced options for power users such as control flow logic, case management, error handling, custom code, and more.

## Key concepts
<a name="automate-key-concepts"></a>

**Automation groups**  
Automation groups create logical groupings for automations, allowing organizations to manage permissions and resources efficiently across different departments or projects. These groups provide a way to organize your automations and setup permissions based on business units, functional areas, or project teams.  
By organizing automations into groups, you can apply consistent access controls, resource restrictions, and governance policies. This organizational structure supports scalable automation management as your organization's automation needs grow and evolve.

**Project**  
A *project* is the primary container that encapsulates all metadata, assets, and contextual information related to an automation initiative. It serves as the foundational unit for organizing, authoring, testing, deploying, and maintaining automations across their lifecycle.

**Lifecycle of a project**  
+ **Create a project:** Define the automation's scope including its name, purpose, business case, and attach process documentation.
+ **Build automation:** Within the project, build and test an automation.
+ **Version and deploy:** Publish automation versions for testing or production. Projects maintain version history and deployment status.
+ **Monitor and iterate:** Review logs and metrics for each run, and iterate on the automation. Each iteration creates traceable project-level change history.

**Automations**  
An *automation* is a visual artifact that represents the executable logic of a process. It is created using the *Visual Designer* within AWS Quick, where you define the sequence of actions, decisions, and agent interactions needed to complete a business process. Each automation serves as the operational blueprint for how work is performed, combining AI-powered agents, system actions, and human inputs in a unified flow.

**Actions**  
Actions are the building blocks for your automations. Each action performs a specific task, from reading data to interacting with external systems.

**Agents**  
An *agent* is an AI-powered action that can understand natural language input, reason through scenarios, and perform complex tasks on your behalf. Agents bring intelligence and adaptability to automations by interpreting intent, handling variability, and executing actions dynamically.  
+ **UI agent** is a native agent that understands natural language instructions to perform complex browser actions. It can autonomously navigate websites, click, type, read data, and produce structured outputs optimized for downstream automation steps.
+ **Custom agent** is an AI-powered action that processes natural language inputs to automate complex steps using integrated tool-calling capabilities. It primarily uses integrations as its tool interface, while offering extensibility to use Code as tool, and other native actions like human-in-the-loop task. The agent delivers structured, predictable outputs optimized for seamless integration into downstream automation steps.