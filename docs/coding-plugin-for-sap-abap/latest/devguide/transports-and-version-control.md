

# Managing change and code reviews
<a name="transports-and-version-control"></a>

 AWS Coding Plugin for SAP ABAP ("Coding Plugin") gives Kiro the tools to assign your changes to transports and to work with your SAP system’s Change and Transport System. It adds no version history of its own. You review and revert the changes it makes with your SAP system’s own version control, exactly as you would review and revert your own.

## Working with transports
<a name="transports-and-version-control-transports"></a>

Coding Plugin gives Kiro tools to check whether an object needs a transport, list and search your transports, create a transport, add objects to it, and release it. Coding Plugin’s default steering guides it to ask before creating a transport, and to ask first whether you want to reuse an existing one — such as one created by Change Request Management (ChaRM). You should provide additional steering on how your organization handles transports.

Avoid commingling human-written and agentically written code in the same transport. This facilitates a code review by the developer after a spec has been implemented.

Note the following limits:
+ Older ABAP systems do not offer ADT tools to release transports. On these systems Coding Plugin works around this by invoking SAP GUI to present SAP’s standard release dialog instead.
+ As with all tool calls, creating or releasing a transport is subject to Kiro’s permissions gates. You can deny Kiro permission to release a transport (see [Kiro Permissions](kiro-permissions.md)).

## Reviewing and reverting changes
<a name="transports-and-version-control-reviewing"></a>

Coding Plugin and Kiro have no built-in code review process. To review and undo the changes Coding Plugin made, use your SAP system’s own version control, which gives you two options.

### Native ABAP version control
<a name="transports-and-version-control-native"></a>

SAP’s [Change and Transport System (CTS)](https://support.sap.com/en/tools/software-logistics-tools/change-and-transport-system.html) manages how changes move between SAP systems. Its native version control records a version of an object when its transport is released. You can compare an object to a previous version and revert to it. It works through transports, so it does not cover local (`$TMP`) objects.

To use it effectively:

1. Release your previous transports before the Coding Plugin begins its work, so your current code has a recorded version to compare to.

1. Ask Kiro to keep its work in a single transport, so the transport collects the changes to compare and revert.

1. After the work is released, use ADT functions to view the object history and compare the changed objects to their previous versions. For code objects, the Coding Plugin can read past versions and help you compare them to the current version.

1. If you need to revert, use ABAP version control to restore the previous version.

### abapGit
<a name="transports-and-version-control-abapgit"></a>

abapGit gives you Git-controlled version history and diff on a per-package basis. Push entire packages to a Git repository such as AWS CodeCommit, make your changes with the plug-in, and diff the result with abapGit.

The Coding Plugin Model Context Protocol (MCP) server supports certain abapGit operations when they are available as ADT tools, enabling Kiro to add and pull repositories for you. ADT tools for abapGit are built into BTP ABAP.