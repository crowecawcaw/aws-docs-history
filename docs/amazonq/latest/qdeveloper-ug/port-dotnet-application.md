# Porting a .NET application with Amazon Q Developer in Visual Studio

Complete these steps to port a Windows-based .NET
application to a Linux-compatible cross-platform .NET application with Amazon Q Developer in Visual Studio.

## Step 1: Prerequisites

Before you continue, make sure you’ve completed the steps in
[Set
up Amazon Q in your IDE](q-in-IDE.md "q-in-IDE.md").

Make sure that the following prerequisites for your application are met before you begin a .NET transformation job:

- Your application contains only .NET projects written in C#.
- Your application only has Microsoft-authored NuGet package dependencies
- Your application only uses UTF-8 characters. If your application uses
  non-UTF-8 characters, Amazon Q will still attempt to transform your
  code.
- If your application is dependent on Internet Information Services (IIS), only default IIS configurations are used
- Amazon Q
  will evaluate the type of the project you selected and its dependencies to
  create a code group. Your code group can only have the following project
  types:
  - Console application
  - Class library
  - Web API
  - WCF Service
  - Business logic layers of Model View Controller (MVC) and Single Page Application (SPA)
  - Test projects

###### Note

Amazon Q doesn’t support transforming UI layer components such as
Razor views or WebForms ASPX files. If Amazon Q detects UI layer
components in your solution or project, it will perform a partial transformation by
excluding UI layer components, and you might need to refactor further to make your
code buildable on the target .NET version.

## Step 2: Transform your application

To transform your .NET solution or project, complete the following procedure:

1. Open any C# based solution or project in Visual Studio that you want to transform.
2. Open any C# code file in the editor.
3. Choose **Solution Explorer**.
4. From the Solution Explorer, right click a solution or project you want to
   transform, and then choose **Port with Amazon Q Developer**.
5. The
   **Port with Amazon Q Developer** window appears.

The solution or project you selected will be chosen in the **Choose a solution
or project to transform** dropdown menu. You can expand the menu to choose a
different solution or project to transform.

In the **Choose a .NET target** dropdown menu, choose the
.NET version you want to upgrade to. 6. Choose **Confirm** to begin the transformation. 7. Amazon Q begins transforming your code. You can view the transformation plan
it generates for details about how it will transform your application.

A **Transformation Hub** opens where you can monitor progress
for the duration of the transformation. After Amazon Q has completed the
**Awaiting job transformation startup** step, you can
navigate away from the project or solution for the duration of the
transformation. 8. After the transformation is complete, navigate to the **Transformation Hub** and
choose **View diffs** to review the proposed changes from Amazon Q in a diff view. 9. Choose **View code transformation summary** for details about the changes
Amazon Q made. You can also download the transformation summary by choosing
**Download summary as .md**.

If any of the items in the **Code groups** table
require input under the Linux porting status, you must manually update some
files to run your application on Linux.

    1. From the **Actions** dropdown menu, choose **Download Linux readiness report**.
    2. A .csv file opens with any changes to your project or solution that you must
     complete before your application is Linux compatible. It includes the
     project and file that need to be updated, a description of the item to
     be updated, and an explanation of the issue. Use the **Recommendation**
     column for ideas on how to address a Linux readiness issue.

10. To update your files in place, choose **Accept changes** from
    the **Actions** dropdown menu.
