

# Architecture
<a name="architecture"></a>

The architecture consists of five connections:
+  AWS Coding Plugin for SAP ABAP to Kiro CLI, using an stdio pipe and the Agent Client Protocol (ACP) to exchange prompts, statuses, and permission requests
+  AWS Coding Plugin for SAP ABAP to SAP ADT via the SAP ADT SDK
+ Kiro CLI to the Kiro backend service and to your identity provider
+ Kiro CLI to the MCP servers, using the MCP protocol
+ The MCP servers to the SAP system, using the SAP ABAP Development Tools (ADT) SDK

The following diagram shows these connections. The Kiro backend is the Kiro Runtime Service, which runs models on Amazon Bedrock. The identity provider shown, AWS IAM Identity Center, is one of several sign-in options that Kiro supports. The dashed box stands for other MCP servers you can add, such as messaging, documentation, or ticketing servers.

 **Coding Plugin architecture** 

![Eclipse, Kiro CLI, MCP servers, the SAP system, and Kiro cloud services](https://docs.aws.amazon.com/coding-plugin-for-sap-abap/latest/devguide/images/architecture.png)


SAP S/4HANA is the trademark or registered trademark of SAP SE or its affiliates in Germany and in other countries.

Eclipse is a trademark of Eclipse Foundation AISBL.

## How AWS Coding Plugin for SAP ABAP works with Eclipse
<a name="architecture-eclipse"></a>

Coding Plugin is an Eclipse plug-in, so it runs inside your Eclipse environment and has access to Eclipse’s APIs. The Coding Plugin MCP server gives Kiro the same Eclipse access, creating a two-way connection to the IDE. Kiro can read Eclipse’s Problems view, see which object you have open in the editor, and open editors and additional Eclipse views on request. Object references in the chat become clickable `adt://` hyperlinks that open the object in its ADT editor.

## How AWS Coding Plugin for SAP ABAP works with Kiro
<a name="architecture-kiro"></a>

Coding Plugin automatically launches Kiro CLI in the background and connects it to the two built-in MCP servers. All agentic processing happens in Kiro CLI, which supports the full range of Kiro capabilities, such as steering, skills, and specs. The integration is bidirectional: the plug-in sends your prompts and the surrounding context to Kiro, and surfaces Kiro’s responses, permission prompts, and actions in the Eclipse UI.

 **MCP servers.** AWS Coding Plugin for SAP ABAP automatically connects the SAP ADT MCP server and the AWS Coding Plugin for SAP ABAP MCP server, and they do not need to be included in `mcp.json`. Through these two servers, Kiro can do the same things you can do in Eclipse and SAP ADT, using the same mechanisms. You can configure your own additional MCP servers through `mcp.json` files. See [Model Context Protocol (MCP)](https://kiro.dev/docs/mcp/) in the Kiro documentation.
+  *SAP’s ADT server* is SAP’s first-party MCP server. Coding Plugin is designed to favor SAP’s ADT server as the canonical and preferred source of ADT functionality.
+  *The plug-in’s own server* is vastly more functional than SAP’s server and uniquely optimized for agentic use. It includes a broad set of ADT tools, Eclipse integration (reading the Problems view, seeing which object you have open, opening editors), and additional functions for troubleshooting the plug-in itself. The two servers overlap somewhat; for example, both can activate objects, run ABAP Unit tests and ABAP Test Cockpit (ATC) checks, and manage transports.

## How Kiro reaches your SAP system
<a name="architecture-reaching-sap"></a>

Kiro CLI and AWS Coding Plugin for SAP ABAP do not establish a separate connection to your SAP system. They reach it through the SAP connection you already have defined in Eclipse in SAP ADT. Your existing network path, authentication, and SAP authorizations apply. Kiro CLI sends your prompts and the context it gathers to the Kiro backend service, which runs the model. For more information on Kiro data handling, see [Privacy and security](https://kiro.dev/docs/privacy-and-security/) in the Kiro documentation. AWS Coding Plugin for SAP ABAP has no service endpoint of its own.