

# How to work with the .NET agent
<a name="dotnet-work-with-agent"></a>

## Experiences
<a name="experiences"></a>

AWS Transform .NET modernization is available in several experiences:
+ **Web console**: For large-scale transformation of repositories.
+ **Visual Studio IDE**: Developer-led transformation of a solution or project working alongside agent interactively and iteratively. Requires a Windows development machine.
+ **Command line**: [Transform .NET solutions with the ATX CLI](#dotnet-atx-cli) using an AWS-managed transformation.

You can also invoke AWS Transform from AI code companions:
+ **Kiro**: transform from Kiro using the [AWS Transform for Kiro power](https://kiro.dev/).
+ **Other AI code companions**: transform from your preferred AI coding assistants using [AWS Transform MCP agents](https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server).

A common pattern is to first modernize with AWS Transform for .NET, then [hand off to an AI code companion](dotnet-next-steps.md) for last mile work.


| Area | Web application | Visual Studio IDE | ATX CLI | 
| --- | --- | --- | --- | 
| Target role | IT professional | Developer | Developer | 
| Operating system | Any | Windows | Linux, macOS, Windows | 
| Source control access | + Repository (AWS CodeConnections)<br />+ Repository (Personal Access Token)<br />+ Code zip file (Amazon S3)<br />+ Code zip file (Direct Upload) | Local file system | Local Git repository | 
| Job scope | Up to 5,000 repositories per job | One solution at a time | One solution at a time | 
| Transformed code location | Written to a new writeable repository branch | Replaces original code on your file system | Replaces original code on your file system | 
| Unit of work | Repository | Project | Project | 
| Assessment | + Analyze repositories<br />+ Assessment reports (multiple formats)<br />+ Global modernization plan | + Analyze projects<br />+ Assessment report<br />+ Modernization plan | + Analyze projects<br />+ Assessment report<br />+ Modernization plan | 
| Customize modernization plan | + Customize global plan<br />+ Upload steering docs | + Customize plan<br />+ Upload steering docs | + Customize plan<br />+ Provide steering doc | 
| Transformation modes | Autonomous or Interactive | Autonomous or Interactive | Autonomous or Interactive | 
| Checkpoint reviews | Review each repository after transformation | Review each project after transformation | Review each project after transformation | 
| Iterative modernization | + Ask for changes at checkpoint<br />+ Ask for changes after transformation<br />+ Retry repo with revised instructions<br />+ Assess additional repos in same job | + Ask for changes at checkpoint<br />+ Ask for changes after transformation<br />+ Retry project with revised instructions<br />+ Review code diffs<br />+ Edit code at checkpoint | + Ask for changes at checkpoint<br />+ Ask for changes after transformation<br />+ Retry project with revised instructions<br />+ Review code diffs | 
| Downloadable artifacts | + Transformed code<br />+ Assessment report<br />+ Modernization plan<br />+ Transformation report<br />+ Next Steps markdown | + Transformed code<br />+ Assessment report<br />+ Modernization plan<br />+ Transformation report<br />+ Next Steps markdown | + Assessment report<br />+ Modernization plan<br />+ Transformation report<br />+ Next Steps markdown | 
| Unit test validation | Ports and runs existing unit tests | + Ports and runs existing unit tests<br />+ Generates missing unit tests for modernized code | Ports and runs existing unit tests | 

## Recommended experiences
<a name="objectives-and-recommended-experiences"></a>

Use the experience that best fits your scenario.


| Scenario | Recommended experience | 
| --- | --- | 
| Work at repository level when transforming | Web application | 
| Perform large-scale transformations | Web application | 
| Transform from a Mac | Web application | 
| Transform unattended | Web or IDE, autonomous mode | 
| Work at project level when transforming | Visual Studio IDE | 
| Local build to confirm transformed code builds on local environment | Visual Studio IDE | 
| Agent leads the modernization, I review | Web or IDE, autonomous mode | 
| I lead the modernization, agent assists | Web or IDE, interactive mode, customize plan | 
| Complex modernization | IDE, interactive mode | 
| Portfolio owner starts transformation, hands off to developers for review | Web application; use [beaming](dotnet-web-final-summary.md#beam-transformed-repository) to hand off repositories to developers, who review in the IDE | 
| Script modernization in an existing pipeline or workflow | ATX CLI | 

## Transform .NET solutions with the ATX CLI
<a name="dotnet-atx-cli"></a>

You can modernize a .NET solution from the command line using the ATX CLI (AWS Transform custom) and the [AWS-managed transformation](transform-aws-customs.md) `AWS/dotnet-modernization`.

Use the following command form:

```
atx custom def exec -n AWS/dotnet-modernization -p <path-to-solution> [-q] [-x] [-t]
```

The following command-line options are available:
+ **-q** (quiet): show agent conversation only, hide tool execution details
+ **-x** (autonomous): run in autonomous mode without user interaction
+ **-t** (trust): trust all tools without prompts

The following table shows example commands.


| Command line example | Description | 
| --- | --- | 
| atx custom def exec -n AWS/dotnet-modernization -p C:\\dev\\InventoryService -t -q | Transform the solution in interactive mode, showing agent conversation only, and trust tool updates. | 
| atx custom def exec -n AWS/dotnet-modernization -p C:\\dev\\InventoryService -t | Transform the solution in interactive mode, showing all tool activity, and trust tool updates. | 
| atx custom def exec -n AWS/dotnet-modernization -p C:\\dev\\InventoryService -t -x | Transform the solution in autonomous mode and trust tool updates. | 