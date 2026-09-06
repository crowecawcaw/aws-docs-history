

# Modernizing .NET in the IDE
<a name="dotnet-ide"></a>

AWS Transform includes an interactive, agentic AI assistant in the AWS Toolkit for Visual Studio. It enables you to modernize applications through a conversational, step-by-step guided experience directly in your IDE. To transform a .NET solution or project, the AWS Transform agent analyzes your codebase, determines the necessary updates to port your application, and generates an assessment report and transformation plan before the transformation begins.

The Visual Studio IDE experience supports authentication by IAM Identity Center only. For more information, see [Adding users in IAM Identity Center](transform-user-management.md#transform-add-idc-users).

The IDE experience offers autonomous and interactive modes. Use autonomous mode for unattended transformation, suitable for overnight or long-running jobs. Use interactive mode to work alongside the agent in chat, with high visibility into transformation, a customizable transformation plan, and step-by-step review of each project. You can iterate to refine results or change direction until satisfied.

When a transformation job is active, you can interact with three windows:
+ The **Chat** window is your primary interaction point with the transformation agent. Use chat to ask questions, discuss options, steer the transformation, and iterate.
+ The **AWS Transform Job Plan** window shows progress steps and is where you can download or upload artifacts or view code change differences.
+ The **Worklog** window shows a log of transformation activity in natural language.

AWS Transform performs four key tasks to port .NET applications to Linux:
+ Upgrades .NET and language versions – Upgrades older .NET C\# code to current .NET and language versions.
+ Migrates from .NET Framework to cross-platform .NET – Migrates projects and packages from Windows dependent .NET Framework to cross-platform .NET compatible with Linux.
+ Rewrites code for Linux compatibility – Refactors and rewrites deprecated and inefficient code components.
+ Generates a Linux compatibility readiness report – For open-ended tasks where user intervention is needed to make the code build and run on Linux, AWS Transform provides a detailed report of actions needed to configure your application after transformation.

For more information about how AWS Transform performs .NET transformations, see [How AWS Transform modernizes .NET applications](dotnet-ide-how.md).

To modernize your .NET code using AWS Transform from Visual Studio IDE, refer to the following:
+ [Modernizing .NET using AWS Transform in Visual Studio](dotnet-ide-vs.md)
+ [How AWS Transform modernizes .NET applications](dotnet-ide-how.md)
+ [Troubleshooting issues with .NET transformations in the IDE](dotnet-ide-troubleshoot.md)

**Quotas**  
For AWS Transform .NET transformation quotas in the IDE, see [Quotas for AWS Transform](transform-limits.md).