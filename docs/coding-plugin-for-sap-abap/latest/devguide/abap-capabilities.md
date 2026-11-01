

# Working with ABAP
<a name="abap-capabilities"></a>

 AWS Coding Plugin for SAP ABAP ("Coding Plugin") works directly in your SAP ABAP system through the SAP ABAP Development Tools (ADT) connection you already use in Eclipse. These ABAP tools come from SAP’s first-party ADT Model Context Protocol (MCP) server, the canonical and preferred source of ADT functionality, and from the plug-in’s own MCP server, which is vastly more functional and uniquely optimized for agentic use. The two overlap somewhat (see [Architecture](architecture.md)).

## What the agent can do in your ABAP system
<a name="abap-capabilities-what"></a>

Coding Plugin works with SAP ABAP objects the way you do in SAP ADT: it finds objects, reads their source, changes and activates them, verifies them, and places them on transports. It uses your existing ADT connection, so every action runs as your SAP user. Coding Plugin also verifies its own work through the self-correcting loop. It activates the object and runs ABAP Unit tests and ABAP Test Cockpit (ATC) checks, then corrects what it finds and repeats (see [The self-correcting loop](abap-development.md#abap-development-self-correcting-loop)).

Every tool call is gated by Kiro Permissions, Kiro’s per-call approval mechanism (see [Kiro Permissions](kiro-permissions.md)), and is bounded by your SAP user’s own authorizations.

## Areas the agent works in
<a name="abap-capabilities-areas"></a>

Coding Plugin works across these areas of your ABAP system. For how a whole object is read, why large objects go through a local file, and how a change stays inactive until you activate it, see [ABAP development](abap-development.md).
+  **Find and navigate.** Search the repository by name pattern, object type, or package, find where an object is used, and jump to a definition or its references.
+  **Source code.** Read and edit the source of classes, programs, function modules, Core Data Services (CDS) views, and other object types. Run a syntax check. Format with the ABAP pretty printer or the CDS formatter. Lock and unlock objects.
+  **Object creation.** Create classes, interfaces, programs, function groups and modules, DDIC objects (domains, data elements, structures, tables, and table types), CDS views, ABAP RESTful Application Programming Model (RAP) artifacts, packages, and transformations.
+  **Activation.** Activate objects and list what is still inactive.
+  **Transports.** Check whether an object needs a transport, search transports, create one and add objects, and set the owner. For releasing, reviewing, and reverting work, see [Managing change and code reviews](transports-and-version-control.md).
+  **Version control.** Read native ABAP version history, and work with abapGit. abapGit support is available by default in BTP ABAP.
+  **Runtime errors.** List and read ABAP short dumps, including the program, timestamp, category, runtime error, and call stack.
+  **Data.** Run read-only SQL queries and preview the contents of tables and CDS views.
+  **RAP and OData services.** Generate RAP objects, and define, bind, and publish Open Data Protocol (OData) services.
+  **System information.** Report installed components, system and client details, and the system’s users.
+  **SAP GUI.** Display, edit, or run an object, or start a transaction. This requires SAP GUI to be installed.

## Eclipse integration
<a name="abap-capabilities-eclipse"></a>

Coding Plugin makes Kiro aware of your Eclipse workbench. Through the plug-in’s own MCP server (see [Architecture](architecture.md)), Kiro has a two-way connection to the IDE. It reads the state of your workbench and acts on it with your approval through Kiro Permissions (see [Kiro Permissions](kiro-permissions.md)).
+  **Active editor.** Coding Plugin reports which object is open. The active editor is pinned to your prompt, so a request such as "Run an ATC check on this program" understands what you are referring to.
+  **Opening objects and views.** Coding Plugin opens an ABAP object in its ADT editor, and opens other Eclipse views, on request. This helps it walk you through a code review.
+  **Project Explorer.** The Coding Plugin creates a filesystem-based project in the Project Explorer. This project contains the `.kiro/` folder and makes it visible, so its settings, steering, skills, and specs sit alongside your ABAP projects.
+  **Problems view.** Coding Plugin reads the syntax errors and warnings Eclipse reports on an object.

## Limitations
<a name="abap-capabilities-cannot"></a>

The ADT services available depend on the connected SAP system.
+ Older systems expose fewer ADT services, so certain functionality is not available. For example, the system refuses transport release on systems whose ADT cannot release transports (such as SAP NetWeaver 7.40). Coding Plugin offers SAP’s own release dialog instead.
+ The SAP BTP ABAP environment runs ABAP Cloud and supports a different set of functionality than a standard on-premises SAP system.