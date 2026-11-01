

# What is AWS Coding Plugin for SAP ABAP?
<a name="what-is"></a>

 AWS Coding Plugin for SAP ABAP ("Coding Plugin") is an Eclipse plug-in that adds agentic AI development, powered by Kiro, to the SAP ABAP Development Tools (ADT) environment you already use. It provides an AI chat panel, spec-driven development workflows, editor actions, and direct access to your SAP system through your existing ADT connection. For Kiro’s own behavior, including its security model, sign-in, and steering semantics, see the [Kiro documentation](https://kiro.dev/docs/) on the Kiro website.

There is no charge for the plug-in. Using it consumes Kiro credits from your Kiro plan. See [Pricing](pricing.md). The plug-in reaches your SAP system through your own ADT connection, using your SAP user and authorizations. See [Security](security.md).

## Key features
<a name="what-is-features"></a>

Coding Plugin provides the following:
+  **Agentic chat in Eclipse.** A chat panel with multiple tabs where you prompt Kiro and review the resulting changes without leaving the IDE.
+  **Spec-driven development for SAP ABAP.** Kiro generates requirements, design, and task documents, then works through the tasks.
+  **Direct access to your SAP system.** Through your existing ADT connection, Coding Plugin finds, reads, changes, and activates ABAP objects, runs ABAP Unit tests and ABAP Test Cockpit (ATC) checks, and works with transports.
+  **Editor integration.** Context menu actions (Explain, Fix, Optimize, Refactor), inline assist, and clickable `adt://` links that open an object in the Eclipse editor.
+  **An Eclipse-aware context.** Coding Plugin knows which object you have open, reads the Problems view, and opens editors and views on request.
+  **Kiro Permissions in Eclipse.** You approve each action Kiro takes, surfaced as prompts in the Eclipse UI.
+  **Built-in ABAP steering.** The plug-in ships ABAP-aware steering so Kiro’s output fits the way SAP ABAP is developed.

## How AWS Coding Plugin for SAP ABAP works
<a name="what-is-how-it-works"></a>

Coding Plugin runs inside Eclipse, alongside SAP ADT. When you send a prompt from the chat panel, the plug-in passes it to Kiro CLI on your machine, which calls Kiro’s cloud services for model inference. The plug-in gives Kiro a set of MCP tools that reach your SAP system through the ADT connection you have already defined, so it can find objects, read and change source, activate, run ABAP Unit tests and ATC checks, and record changes on a transport. These tools are governed by Kiro’s permission model to ask for approvals from the developer.

For more information about the components involved and how they communicate, see [How AWS Coding Plugin for SAP ABAP works](how-it-works.md) and [Architecture](architecture.md).

## Basic concepts
<a name="what-is-concepts"></a>

The following terms describe how you work with Coding Plugin:

 **Eclipse and SAP ADT**   
Eclipse is an open source integrated development environment (IDE). SAP ABAP Development Tools (ADT) is a set of Eclipse plug-ins that let you develop ABAP in Eclipse instead of SAP GUI. For more information, see [ABAP Development Tools for Eclipse](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6aa39f1ac05441e5a23f484f31e477e7/54dd7126d5b74efeb7a21f6b0bfe5f1a.html?locale=en-US) in the SAP documentation.

 **Agent**   
Kiro is the agent. It reasons about your prompt and acts by calling tools, such as reading an ABAP object or running a test.

 **Spec**   
A spec is a set of requirements, design, and task documents that Kiro writes and then works through, so that you plan a large change before making it. See [Spec-driven development with AWS Coding Plugin for SAP ABAP](spec-driven-development.md).

 **Model Context Protocol (MCP) server**   
An MCP server exposes a set of tools to Kiro. The plug-in wires the SAP-specific MCP servers automatically, so there is nothing to configure. See [Model Context Protocol (MCP)](https://kiro.dev/docs/mcp/) in the Kiro documentation.

 **Steering**   
Steering is written guidance that shapes how Kiro works. The plug-in ships ABAP-aware steering out of the box, and you can add your own. See [Customizing AWS Coding Plugin for SAP ABAP](customizing.md).

 **Kiro Permissions**   
Kiro Permissions is Kiro’s approval mechanism. By default, every tool call waits for your approval. See [Kiro Permissions](kiro-permissions.md).

## Use cases
<a name="what-is-use-cases"></a>

Coding Plugin is designed to be a general-purpose tool that can satisfy a broad set of use cases for SAP ABAP, rather than being targeted at a specific use case. The following are examples of things Coding Plugin can do:
+ Build a new RICEF object (report, interface, conversion, enhancement, or form), Open Data Protocol (OData) service, or other feature from a spec, with Coding Plugin discovering the available tables and APIs in your live system.
+ Add unit tests to existing code and then refactor it for clean core or S/4HANA, iterating through ATC checks.
+ Understand or document legacy code.
+ Perform code reviews for style or correctness.

## Pricing
<a name="what-is-pricing"></a>

There is no separate charge for Coding Plugin. The Kiro work you do through it draws credits from your Kiro plan. For more information, see [AWS Coding Plugin for SAP ABAP pricing](pricing.md).

## Compliance and security
<a name="what-is-compliance-security"></a>

Coding Plugin reaches your SAP system only through the ADT connection you have already defined in Eclipse, using your SAP user and your SAP authorizations. It stores no SAP credentials of its own, and it can do nothing on the system that your SAP user cannot do. Tool calls are subject to Kiro’s permission model. For more information about how the plug-in’s MCP server is secured, and about Kiro’s own security model, see [Security](security.md).

## Related services
<a name="what-is-related-services"></a>
+ Kiro is the agent that powers Coding Plugin. For Kiro’s own behavior, models, and plans, see the [Kiro documentation](https://kiro.dev/docs/) on the Kiro website.
+ With the AWS SDK for SAP ABAP, ABAP programs can call AWS services directly from ABAP. See [What is AWS SDK for SAP ABAP?](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/home.html).

## Next steps
<a name="what-is-next-steps"></a>
+ For instructions on installing the plug-in and running your first spec, see [Set up AWS Coding Plugin for SAP ABAP](getting-started.md).
+ For more information about how specs work in ABAP, see [Spec-driven development](spec-driven-development.md).
+ For more information about what Coding Plugin can do in your SAP system, see [Working with ABAP](abap-capabilities.md).