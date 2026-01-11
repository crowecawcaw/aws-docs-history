# Porting UI layer code

AWS Transform can port the UI layer of ASP.NET websites to UI frameworks compatible with ASP.NET Core, which can run on Linux. The following transformations are available:

- MVC Razor UI porting
- Web Forms to Blazor UI porting

## MVC Razor UI porting

ASP.NET MVC projects with Razor Views UI can be ported to MVC Razor Views on ASP.NET Core, remaining on the same UI framework. While Razor views are similar between ASP.NET and ASP.NET Core, there are differences that require porting code changes:

- ASP.NET MVC Razor Views use the System.Web.Mvc namespace and are closely tied to the .NET Framework.
- ASP.NET Core Razor Views are modular, built on Microsoft.AspNetCore.Mvc, with improved dependency injection.
- ASP.NET Core has new features including Tag Helpers and View Components.

AWS Transform detects and ports common incompatible components and constructs in Razor Views.

## Web Forms to Blazor UI porting

ASP.NET Web Forms UI does not have a counterpart on ASP.NET Core. AWS Transform can port Web Forms UI layer code to Blazor Server on ASP.NET Core. UI layer code is rewritten for the target UI framework.

To enable or disable Web Forms to Blazor UI porting, check or clear the Transform UI ASP.NET Web Forms to Blazor job setting.

### Transformation details

Your Web Forms project is converted to a Blazor project with server-side hosting. The following project and file changes are made during transformation:

| File transformation mapping | From             | To                                                        | Description |
| --------------------------- | ---------------- | --------------------------------------------------------- | ----------- |
| \*.aspx, \*.ascx            | \*.razor         | .aspx pages and .ascx custom controls become .razor files |
| Web.config                  | appsettings.json | Web.config settings become appsettings.json settings      |
| Global.asax                 | Program.cs       | Global.asax code becomes Program.cs code                  |
| \*.master                   | \*layout.razor   | Master files become layout.razor files                    |

### Post-transformation project structure

After transformation, the transformed files reside in the following project locations:

- Components folder: All razor components (\*.razor) are placed in a Components folder created at the same level as the project's .csproj file.
- Pages mapping: Web Forms pages (\*.aspx) are converted to Components/Pages folder structure.
- Controls mapping: Web Forms controls (\*.ascx) are placed directly under the Components folder.

### Limitations and unsupported features

Projects with up to 1000 pages (.aspx + .ascx files) can be transformed.

The following features are not supported at present. If your workloads use these features, that code will need to be ported manually or with an AI code companion post-transformation.

- .asmx files (XML web service)
- .svc files (service files)
- .ashx files (generic handler files)
- Service references & web references (reference.map, reference.cs, .wsdl files)
- Mixtures of .aspx (Web Forms) files and .cshtml (Razor) files in the same project
- Dependencies on project types not yet supported by AWS Transform for .NET
- Third-party vendor UI libraries/controls
- Web Site projects

Only Web Application projects (containing a .csproj file) are supported. To convert a Web Site project to a Web Application project,
see Microsoft guidance [Converting a Web Site Project to a Web Application Project](https://devblogs.microsoft.com/dotnet/converting-a-web-site-project-to-a-web-application-project/ "https://devblogs.microsoft.com/dotnet/converting-a-web-site-project-to-a-web-application-project/").
