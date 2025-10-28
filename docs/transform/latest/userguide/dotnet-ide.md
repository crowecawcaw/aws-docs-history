# Modernizing .NET in the IDE

AWS Transform for .NET is a new generative AI-powered agent designed to modernize legacy .NET applications. For more information, see Modernizing .NET with AWS Transform. You can modernize your legacy .NET code by using the AWS Transform web application or the Visual Studio AWS Toolkit extension. Use AWS Transform in integrated development environments (IDEs) to get assistance with your software development needs. In IDEs, AWS Transform includes capabilities to provide guidance and support across various aspects of .NET code modernization.

To transform a .NET solution or project, the AWS Transform agent analyzes your codebase, determines the necessary updates to port your application, and generates a transformation plan before the transformation begins. During this analysis, the AWS Transform agent divides your .NET solution or project into code groups that you can view in the transformation plan. A code group is a project and all its dependencies that together generate a buildable unit of code such as a dynamic link library (DLL) or an executable.

During the transformation, the AWS Transform agent provides step-by-step updates in the AWS **Transformation Hub** window where you can monitor progress. After transforming your application, AWS Transform generates a summary with the proposed changes in a diff view for you to optionally verify the changes before you accept them. When you accept the changes, AWS Transform makes in-place updates to your .NET solution or project.

AWS Transform performs four keys tasks to port .NET applications to Linux:

- Upgrades language version – Replaces outdated C# versions of code with Linux-compatible C# versions.
- Migrates from .NET Framework to cross-platform .NET – Migrates projects and packages from Windows dependent .NET Framework to cross-platform .NET compatible with Linux.
- Rewrites code for Linux compatibility – Refactors and rewrites deprecated and inefficient code components.
- Generates a Linux compatibility readiness report – For open-ended tasks where user intervention is needed to make the code build and run on Linux, AWS Transform provides a detailed report of actions needed to configure your application after transformation.
  For more information about how AWS Transform performs .NET transformations, see [How AWS Transform modernizes .NET applications](dotnet-ide-how.md "dotnet-ide-how.md").

###### Quotas

For AWS Transform .NET transformation quotas in the IDE, see [Quotas for AWS Transform](transform-limits.md "transform-limits.md").

To modernize your .NET code using the AWS Transform, part of the Visual Studio AWS Toolkit extension, see the following:

- [Modernizing .NET using AWS Transform in Visual Studio](dotnet-ide-vs.md "dotnet-ide-vs.md")
- [How AWS Transform modernizes .NET applications](dotnet-ide-how.md "dotnet-ide-how.md")
- [Troubleshooting issues with .NET transformations in the IDE](dotnet-ide-troubleshoot.md "dotnet-ide-troubleshoot.md")
