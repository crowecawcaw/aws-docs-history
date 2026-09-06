# Modernizing .NET with AWS Transform

AWS Transform for .NET is a generative AI-powered agent that helps you modernize your .NET applications. You can modernize legacy .NET Framework applications to cross-platform .NET, and upgrade .NET applications to later versions.

## Multiple experiences

AWS Transform is available in multiple experiences, including a [web application](dotnet-web-app.md "dotnet-web-app.md"), [Visual Studio IDE](dotnet-ide.md "dotnet-ide.md"), or [AI code companions via MCP](https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server "https://github.com/awslabs/mcp/tree/main/src/aws-transform-mcp-server"). Refer to [How to work with the .NET agent](dotnet-work-with-agent.md "dotnet-work-with-agent.md") for recommendations based on role and scenario.

## Capabilities and key features

The scope of the .NET agent is .NET-to-.NET code transformation. If your transformation needs include non-.NET languages and frameworks, such as Web Forms to React, use [AWS Transform custom](custom.md "custom.md").

AWS Transform for .NET has these capabilities:

- Modernize legacy .NET Framework applications to modern cross-platform .NET
- Update modern .NET applications to later versions
- Integrate with source control platforms (Azure Repos, Bitbucket, GitHub, GitLab)
- Produce assessment reports and customizable modernization plan before transformation
- Produce transformation reports and next steps guidance after transformation
- Validate transformed code with local builds and unit test porting

## Supported versions and project types

The .NET agent can transform the following versions, languages, and project types:

|                         |                                                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Transform from          | .NET Framework 3.5, .NET Core 3.1, .NET 5.x+ through .NET 10                                                                                                 |
| Transform to            | .NET 8, .NET 10, .NET Standard (class libraries)                                                                                                             |
| Languages               | C#, VB.NET (preview feature)                                                                                                                                 |
| Supported project types | Class libraries, Console apps, ASP.NET (MVC, Web API, Web Forms), Unit test projects (NUnit, xUnit, MSTest), Windows Communication Foundation (WCF) services |
| Preview project types   | Desktop (WinForms, WPF), mobile (Xamarin), ASMX web service                                                                                                  |

## Limitations

For more information on quotas and limitations for AWS Transform, see [Quotas for AWS Transform](transform-limits.md "transform-limits.md").

AWS Transform does not transform the following:

- Blazor UI components
- Win32 DLLs that don't have core compatible libraries
- Repositories that do not contain any .NET solutions.
- Web site projects without a project file (must be converted to a Web application).

## Human intervention

During the porting of .NET Framework applications to cross-platform .NET, you may be requested to provide input or approvals in the following scenarios:

- Set up a connector to your source code and permissions
- Validate the proposed modernization plan
- Upload missing package dependencies as NuGets
- Review and accept the transformed code

## More information

You can modernize your .NET code by using either the AWS Transform web application or the AWS Toolkit for Visual Studio.

- [Modernizing .NET code with the AWS Transform web application](dotnet-web-app.md "dotnet-web-app.md")
- [Modernizing .NET in the IDE](dotnet-ide.md "dotnet-ide.md")
- [Best practices for .NET transformations](dotnet-best-practices.md "dotnet-best-practices.md")
