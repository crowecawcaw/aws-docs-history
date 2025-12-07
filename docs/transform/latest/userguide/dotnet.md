# Modernizing .NET with AWS Transform

The AWS Transform agent for .NET can help you modernize your .NET applications to be compatible with cross-platform .NET. This capability is called .NET modernization. After [AWS Transform environment](transform-environment.md "transform-environment.md") in AWS Transform, you can create a .NET modernization transformation job.

## Capabilities and key features

- Analyze .NET Framework codebases from your source control systems, which includes private NuGet support, identifying cross repository dependencies, and providing an analysis report.
- Automated transformation of legacy .NET Framework applications to cross-platform .NET, email notifications, and a transformation summary report.
- Easy integration with the source control platforms (BitBucket, GitHub, and GitLab) to ingest existing code and commit transformed code to a new branch.
- Validation of transformed code through unit tests.

## Supported versions and project types

AWS Transform supports transformation for these versions of .NET:

- .NET Framework 3.5+
- .NET Core 3.1
- .NET 5.x+
- .NET 8

AWS Transform can transform to these target .NET versions:

- .NET 8
- .NET 10

AWS Transform supports transformation of these types of projects (C# only):

- Class libraries
- Console applications
- ASP.NET:
  - Model View Controller (MVC), including front-end Razor Views
  - Single Page Application (SPA) back-ends (business logic layers)
  - Web API
  - Web Forms

- Unit test projects (NUnit, xUnit, and MSTest)
- Windows Communication Foundation (WCF) services
- Projects with provided cross-platform versions for third-party or private NuGet packages. If a cross-platform equivalent is missing or unavailable, AWS Transform for .NET will attempt a best-effort conversion.

AWS Transform can also transform the following project types to modern .NET. This is a preview feature, available only in the US East (N. Virginia) Region.

- WinForms desktop projects. This is a preview feature, available only in the US East (N. Virginia) Region.
- WPF desktop projects. This is a preview feature, available only in the US East (N. Virginia) Region.
- Xamarin mobile projects. This is a preview feature, available only in the US East (N. Virginia) Region.
- Projects written in VB.NET. This is a preview feature, available only in the US East (N. Virginia) Region.

## Limitations

For more information on quotas and limitations for AWS Transform, see [Quotas for AWS Transform](transform-limits.md "transform-limits.md").

AWS Transform does not transform the following:

- Blazor UI components
- Win32 DLLs that don't have core compatible libraries
- Applications written in VB.NET
- Repositories that do not contain any solutions.
- AWS Transform will not modify the original repo branches, and can only write to a separate target branch specified in your transformation plan.

## Human intervention

During the porting of .NET Framework applications to cross-platform .NET, you may be requested to provide input or approvals in the following scenarios:

- Set up a connector to your source code and permissions
- Validate the proposed modernization plan
- Upload missing package dependencies as NuGets
- Review and accept the transformed code

## More information

You can modernize your .NET code by using either the AWS Transform web application or the AWS Toolkit for Visual Studio.

- [Modernizing your .NET code by using the AWS Transform web application](dotnet-web-app.md "dotnet-web-app.md")
- [Modernizing .NET in the IDE](dotnet-ide.md "dotnet-ide.md")
