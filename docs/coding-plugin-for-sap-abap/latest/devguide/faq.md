

# AWS Coding Plugin for SAP ABAP FAQ
<a name="faq"></a>

Common questions about AWS Coding Plugin for SAP ABAP ("Coding Plugin"). Each answer links to the chapter that covers the topic in full.

## Getting started
<a name="faq-getting-started"></a>

<a name="faq-cost"></a> **What does the plug-in cost, and what is a credit?** 

There is no charge for the plug-in itself. The Kiro work you do through it draws *credits* from your Kiro plan, where a credit is the unit Kiro meters its work in. See [Pricing](pricing.md).

<a name="faq-model"></a> **Can I use my own AI model?** 

No. Kiro runs the model, and the model and mode you can choose come from what your Kiro backend offers, shown in the chat panel’s selector bar. You cannot point the plug-in at an arbitrary external model. See [The selector bar](using-chat.md#using-chat-selector).

<a name="faq-conventions"></a> **How do I ask the agent to write code that matches our conventions?** 

Create steering describing your conventions. If your team already has a document or webpage describing your conventions, have Kiro read it and extract it into steering. The `/workspace-init` skill will interview you about this. See [Customizing Coding Plugin](customizing.md).

<a name="faq-other-kiro-features"></a> **Can I use other Kiro features, such as powers and hooks?** 

Coding Plugin surfaces many Kiro capabilities in the Eclipse UI, including steering, skills, specs, MCP servers, Kiro Permissions, and the model and mode selector. Kiro capabilities that have no dedicated UI in the plug-in, such as hooks, are configured through files under the `.kiro/` folder in your project. For what Kiro offers and how to configure it, see the [Kiro documentation](https://kiro.dev/docs/) on the Kiro website.

## Working with SAP
<a name="faq-sap"></a>

<a name="faq-abap-objects"></a> **What SAP ABAP objects can the agent create and change?** 

The agent can work with any SAP ABAP object that ADT exposes. This includes classes, programs, function modules, Core Data Services (CDS) views, DDIC objects, and ABAP RESTful Application Programming Model (RAP) artifacts. Capabilities vary depending on the ABAP system version. See [Working with ABAP](abap-capabilities.md).

<a name="faq-adt-mcp"></a> **Do I need SAP’s ADT MCP server?** 

Recommended, not required. The plug-in’s own ABAP Development Tools (ADT) tools reach SAP through your ADT connection independently of SAP’s Model Context Protocol (MCP) server, but SAP’s server alone offers Joule AI fixes for ABAP Test Cockpit (ATC) findings and Open Data Protocol (OData) service discovery. See [Architecture](architecture.md).

<a name="faq-other-languages"></a> **Can I use Coding Plugin for languages other than SAP ABAP?** 

Coding Plugin is an SAP ABAP specialist persona and is not suited to other languages. Development for non-ABAP scenarios, such as the SAP Cloud Application Programming Model (CAP), is better suited to SAP-provided tools such as SAP Joule for Developers.

<a name="faq-sap-notes"></a> **Can I read and implement SAP Notes with Coding Plugin?** 

The SAP ADT plug-in cannot implement Notes the way `SNOTE` does, so the Coding Plugin cannot either.

SAP ADT cannot read Note text. However, you can download Notes as PDF documents and ask Kiro to read them from your Downloads directory, or attach them to your prompt. In this way, Coding Plugin can analyze short dumps and compare them to symptoms documented in specific Notes you download.

<a name="faq-basis-tasks"></a> **Can I perform Basis tasks with Coding Plugin?** 

Coding Plugin can read short dumps and gateway errors to help diagnose certain kinds of Basis errors, but it is not a general-purpose Basis tool.

SAP ADT does not expose Basis tasks such as scheduling background jobs or editing RFC destinations, so Coding Plugin cannot perform these tasks.

<a name="faq-temporary-code"></a> **How does the plug-in use temporary programs?** 

When writing conventional code such as Java and Python, Kiro knows how to create temporary programs to test unknowns such as library behavior. This technique works in ABAP too, where Kiro can create a temporary executable ABAP class to test the behavior of a BAPI or other API that it is unfamiliar with. We recommend steering Kiro to put these in `$TMP` or another `$` package so that they are not transported to production, and to limit itself to read-only operations unless you explicitly approve the test of a write operation.

<a name="faq-speed"></a> **How can I get Kiro to implement my spec faster?** 

The speed of agentic processing depends largely on the inference latency of the LLM. Larger models reason more deeply but take longer to process. Lighter models can process much faster and perform well when executing a well-defined task list (for example, implementing a spec). Kiro supports running up to five concurrent subagents, so when developing a spec, ask Kiro to emphasize parallelism in the task sequencing.

<a name="faq-accuracy"></a> **How can I get Kiro to write better SAP ABAP?** 

Unlike SAP Joule, the underlying Kiro engine does not have the benefit of a purpose-built model trained specifically in ABAP and SAP knowledge. But today’s commodity LLMs show strong ABAP knowledge, and Kiro can look up live information from the web. To add your own expertise on SAP ABAP or specific SAP APIs, create a steering document such as `sap-abap.md` and add your knowledge there.

<a name="faq-aws-sdk"></a> **Can Kiro write SAP ABAP code that calls AWS services?** 

Yes. With the AWS SDK for SAP ABAP, ABAP programs can call more than 240 AWS services in pure SAP ABAP. To give Kiro detailed knowledge of the SDK’s modules and APIs, add the AWS SDK for SAP ABAP Knowledge MCP server to your `mcp.json` file. For setup, see [Using the AWS SDK for SAP ABAP Knowledge MCP Server](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/mcp-server.html) in the * AWS SDK for SAP ABAP Developer Guide*. For more about the SDK, see [What is AWS SDK for SAP ABAP?](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/home.html).

## Security and data
<a name="faq-security"></a>

<a name="faq-data"></a> **Does my SAP ABAP code leave my machine?** 

Yes. Your prompts, and the code context the agent gathers, are sent by Kiro CLI to the Kiro backend service, which runs the model. For how Kiro handles your data, see [Privacy and security](https://kiro.dev/docs/privacy-and-security/) in the Kiro documentation and [What data leaves your machine](security.md#security-data).

<a name="faq-limit-agent"></a> **How do I limit what the agent can do in my SAP system?** 

The agent runs as your SAP user, so your SAP authorizations are the real limit, and Kiro Permissions gates every action behind your approval. See [Reaching your SAP system](security.md#security-sap) and [Kiro Permissions](kiro-permissions.md).

<a name="faq-third-party-steering"></a> **Can I use third-party steering or MCP servers for SAP ABAP?** 

 AWS does not make recommendations on third-party or open source tooling. Subject any third-party steering or agentic tooling to a security review before you use it. For more information, see [MCP security](https://kiro.dev/docs/mcp/security/) in the Kiro documentation and [Agentic AI security](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/introduction.html) in the AWS Prescriptive Guidance.