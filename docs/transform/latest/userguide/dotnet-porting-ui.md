

# Porting UI layer code

AWS Transform can port the UI layer of ASP.NET websites to UI frameworks compatible with ASP.NET Core, which can run on Linux. The following transformations are available. To change the default target, give the agent instructions via chat, editing the modernization plan, or uploading a steering document.


| From (ASP.NET) | To (ASP.NET Core) | 
| --- | --- | 
| MVC Razor views (C\#, VB.NET) | → MVC Razor views (default), Blazor, or Razor Pages (C\#) | 
| Web Forms (C\#, VB.NET) | → Blazor (default), MVC Razor views, or Razor Pages (C\#) | 

ASP.NET Core does not support VB.NET. If your front end UI layer projects are written in VB.NET, AWS Transform will convert them to C\# automatically.

## MVC Razor UI porting
<a name="dotnet-mvc-razor-porting"></a>

ASP.NET MVC projects with Razor views UI can be ported to MVC Razor views on ASP.NET Core, remaining on the same UI framework. Although Razor views are similar between ASP.NET and ASP.NET Core, there are differences that require porting code changes:
+ ASP.NET MVC Razor views use the System.Web.Mvc namespace and are closely tied to the .NET Framework.
+ ASP.NET Core Razor views are modular, built on Microsoft.AspNetCore.Mvc, with improved dependency injection.
+ ASP.NET Core has new features including Tag Helpers and View Components.

AWS Transform detects and ports common incompatible components and constructs in Razor views.

## Web Forms to Blazor UI porting
<a name="dotnet-webforms-blazor-porting"></a>

ASP.NET Web Forms UI does not have a counterpart on ASP.NET Core. AWS Transform can rewrite the Web Forms UI layer code to Blazor Server on ASP.NET Core.

### Transformation details
<a name="dotnet-transformation-details"></a>

Your Web Forms project is converted to a Blazor project with server-side hosting. The following project and file changes are made during transformation:


**File transformation mapping**  

| From | To | Description | 
| --- | --- | --- | 
| \*.aspx, \*.ascx | \*.razor | .aspx pages and .ascx custom controls become .razor files | 
| Web.config | appsettings.json | Web.config settings become appsettings.json settings | 
| Global.asax | Program.cs | Global.asax code becomes Program.cs code | 
| \*.master | \*layout.razor | Master files become layout.razor files | 

### Post-transformation project structure
<a name="dotnet-post-transformation-structure"></a>

After transformation, the transformed files reside in the following project locations:
+ **Components folder:** All razor components (\*.razor) reside in a Components folder created at the same level as the project's .csproj file.
  + **Controls:** Web Forms controls (\*.ascx) reside in Components/Controls.
  + **Layout pages:** Layout pages reside in Components/Layout.
  + **Pages:** Web Forms pages (\*.aspx) reside in Components/Pages.

## Third-party vendor UI libraries
<a name="dotnet-third-party-ui-libraries"></a>

If your original front-end projects use proprietary UI components (from vendors such as DevExpress, Infragistics, or Telerik by Progress), you can:
+ **Convert to native controls (default):** Replace with native and open source components in the target UI framework.
+ **Stay with vendor libraries:** Adapt UI controls to use an equivalent vendor library for the target UI framework. AWS Transform leaves code comments and Next Steps instructions for porting. You'll need to arrange licensing of the target UI library and complete porting in an AI code companion.

The modernization plan lists each vendor control, what it becomes, and its status.

To change the default behavior, revise the modernization plan.

## Next Steps file
<a name="dotnet-ui-porting-next-steps-file"></a>

For user interface components that cannot be ported or verified by AWS Transform, the Next Steps markdown file will contain tasks for follow-up in an AI code companion.

## Limitations and unsupported features
<a name="dotnet-limitations-unsupported"></a>

The following features are not supported at present. If your workloads use these features, that code will need to be ported manually or with an AI code companion post-transformation.
+ .svc files (service files)
+ .ashx files (generic handler files)
+ Service references & web references (reference.map, reference.cs, .wsdl files)
+ Mixtures of .aspx (Web Forms) files and .cshtml (Razor) files in the same project
+ Dependencies on project types not yet supported by AWS Transform for .NET
+ Web Site projects

Only Web Application projects (containing a .csproj file) are supported. To convert a Web Site project to a Web Application project, see [Converting a Web Site Project to a Web Application Project](https://devblogs.microsoft.com/dotnet/converting-a-web-site-project-to-a-web-application-project/) on the Microsoft website.