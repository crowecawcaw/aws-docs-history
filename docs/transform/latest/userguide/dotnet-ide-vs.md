# Modernizing .NET using AWS Transform in Visual Studio

Complete these steps to port a Windows-based .NET
application to a Linux-compatible cross-platform .NET application with AWS Transform in Visual Studio.

## Step 1: Prerequisites

Before you continue, make sure you've [downloaded the AWS toolkit extension in Visual Studio](../../../amazonq/latest/qdeveloper-ug/q-in-IDE-setup.md "../../../amazonq/latest/qdeveloper-ug/q-in-IDE-setup.md") and completed the steps to [Authenticate in Visual Studio](../../../amazonq/latest/qdeveloper-ug/q-in-IDE-setup.md#setup-vs "../../../amazonq/latest/qdeveloper-ug/q-in-IDE-setup.md#setup-vs"). You can log in with an AWS Transform credential or an Amazon Q Developer credential.

Also, see the AWS Transform [capabilities](dotnet.md#capabilities "dotnet.md#capabilities") and [limitations](dotnet.md#limitations "dotnet.md#limitations") for .NET modernization to make sure that your code can be transformed.

## Step 2: Transform your application

To transform your .NET solution or project, complete the following procedure:

1. Open any C# based solution or project in Visual Studio that you want to transform.
2. Open any C# code file in the editor.
3. Choose **Solution Explorer**.
4. From the **Solution Explorer**, right click a solution or project you want to
   transform, and then choose to port or transform the solution or project with AWS Transform.
5. The AWS Transform window appears.

The solution or project you selected will be chosen in the **Choose a solution
or project to transform** dropdown menu. You can expand the menu to choose a
different solution or project to transform.

In the **Choose a .NET target** dropdown menu, choose the
.NET version you want to upgrade to. 6. You can update the Default Settings, or leave them as-is. These include:

    * Exclude .NET Standard projects from the transformation plan


    This setting is selected by default. When selected, AWS Transform excludes any .NET Standard projects from the transformation plan. If you deselect this setting, .NET Standard projects will be transformed, which will make them no longer compatible with the .NET Framework.
    * Transform UI Model-View Controller (MVC) Razor Views
     to ASP.NET Core Razor


    This setting is selected by default. When selected, AWS Transform handles the transformation of any MVC Razor View UI layers into ASP.NET Core Razor Views. If you deselect this option, you must transform these UI layers manually.


    For the UI layer, only the transformation of MVC Razor Views to ASP.NET core is supported. UI Layers for WebForms (.aspx), MVC Views (.cshtml), Windows Presentation Foundation (WPF), WinForms, and Blazor UI components must be transformed manually.
    * Check the NuGet sources and get .NET compatible package versions


    Allow AWS Transform to search for and get .NET compatible package versions for the code that you would like to transform.

7. Choose **Confirm** to begin the transformation.
8. AWS Transform begins transforming your code. You can view the transformation plan
   it generates for details about how it will transform your application.

A **Transformation Hub** opens where you can monitor progress
for the duration of the transformation. After AWS Transform has completed the
**Awaiting job transformation startup** step, you can
navigate away from the project or solution for the duration of the
transformation. 9. After the transformation is complete, navigate to the **Transformation Hub** and
choose **View diffs** to review the proposed changes in a diff view. 10. Choose **View code transformation summary** for a summary of the changes AWS Transform made.
For details about transformation, including changes made, the reason for changes, and actionable error details,
you can download a transformation detail report by choosing **Download Transformation Report**.
Refer to [Transformation Reports](tdotnet-reports.md "tdotnet-reports.md") for more information.

If any of the items in the **Code groups** table require input under the Linux porting status,
you must manually update some files to run your application on Linux.
The transformation detail report includes a Linux readiness report section that
identifies compatibility issues in moving from Windows to Linux that require human attention. 11. To update your files in place, choose **Accept changes** from
the **Actions** dropdown menu.
