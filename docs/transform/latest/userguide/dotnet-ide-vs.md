# Modernizing .NET using AWS Transform in Visual Studio

Complete these steps to port a Windows-based .NET
application to a Linux-compatible cross-platform .NET application with AWS Transform in Visual Studio 2026 or 2022.

## Step 1: Prerequisites

Before you continue, make sure you've downloaded and installed the
[AWS Toolkit extension with Amazon Q](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022 "https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022")
from the Visual Studio Marketplace. Review the AWS Transform [capabilities](dotnet.md#capabilities "dotnet.md#capabilities") and
[limitations](dotnet.md#limitations "dotnet.md#limitations") for .NET modernization to confirm that your code can be transformed.

## Step 2: Authenticate in Visual Studio

To connect to your AWS accounts from the Toolkit for Visual Studio, open the Getting Started with the AWS Toolkit User Interface (connection UI):

1. From the Visual Studio main menu, navigate to **Extensions > AWS Toolkit > Getting Started** to open the **Getting Started: AWS Toolkit page**.
2. Select either **AWS Transform** or **Amazon Q Developer** authentication.
3. Choose an existing profile or create a new one. When creating a new profile, enter a name for the
   profile and your AWS Transform start URL, which was emailed to you after you were added to IAM Identity Center by your administrator.
4. Choose **Connect**. Follow the prompts to sign in and grant access permissions through your web browser.
   In Visual Studio, you should see **Connected with IAM Identity Center**.

## Step 3: Transform your application

To transform your .NET solution or project, complete the following procedure:

1. Open any C# based solution or project in Visual Studio that you want to transform.
2. Open any C# code file in the editor.
3. Choose **Solution Explorer**.
4. From the **Solution Explorer**, right click a solution or project you want to
   transform, and then choose to port or transform the solution or project with AWS Transform.
5. The AWS Transform window appears.

The solution or project you selected will be chosen in the **Choose a solution
or project to transform** dropdown menu. You can expand the menu to choose a
different solution or project to transform. 6. In the **Choose a workspace** dialog, create a workspace or select an existing one.
Workspaces make your activity visible in the AWS Transform web application, where you can invite collaborators to view and chat about transformation jobs. 7. In the **Choose a .NET target** dropdown menu, choose the
.NET version you want to upgrade to. 8. You can update the Default Settings, or leave them as-is. These include:

    * Exclude .NET Standard projects from the transformation plan


    This setting is selected by default. When selected, AWS Transform excludes any .NET Standard projects from the transformation plan. If you deselect this setting, .NET Standard projects will be transformed, which will make them no longer compatible with the .NET Framework.
    * Check the NuGet sources and get .NET compatible package versions


    Allow AWS Transform to search for and get .NET compatible package versions for the code that you would like to transform.

9. Choose **Start** to begin the transformation.
10. Wait while AWS Transform analyzes your code and generates an assessment report and a code transformation plan.

You will be prompted with **View Transformation Plan?** **Choose Edit Plan** to review or edit the transformation plan,
or **Start transformation** to transform with the existing plan. 11. If you choose to edit the plan, a _transformation-plan.md_ markdown file will open in the code editor.
The transformation plan describes the objective and details of the transformation in a series of steps. Refer to the instruction comments
at the end if the plan. You can modify this plan in the following ways:

    * **Transformation steps and substeps**: change, add, or remove
     steps and substeps to control structural transformation and package update
     details
    * **Preview Project Transformation**: Add experimental
     transformation of WinForms desktop projects, WPF projects, Xamarin projects, or
     projects written in VB.NET


    ###### Note

    Other project transformations are a preview feature, available only in the US East (N. Virginia) Region.
    * **Customization section**: add customization instructions, such as dependency injection instructions or coding pattern examples.


    ###### Note

    Coding pattern examples are a preview feature, available only in the US East (N. Virginia) Region.After saving any plan changes, choose **Start Transformation** to start the transformation.

12. AWS Transform begins transforming your code.

An **AWS Transformation Hub** opens where you can monitor
progress for the duration of the transformation. Here you can see
estimated time remaining, a Job ID you can copy to the clipboard, and
transformation steps. Choose a step to see the worklog for that step, which explains
the current transformation activity.

Once AWS Transform
has started the **Transforming code** step you
can navigate away from the project or solution for the duration of the
transformation. 13. After the transformation is complete, navigate to the **Transformation Hub** and
choose **View diffs** to review the proposed changes in a diff view. To update your files in place,
choose **Accept changes** from the Actions dropdown menu. 14. Choose **View code transformation summary** for a summary of the changes AWS Transform made.
For details about transformation, including changes made, the reason for changes, and actionable error details,
you can download a transformation detail report by choosing **Download transformation report**.
Refer to [Transformation Reports](tdotnet-reports.md "tdotnet-reports.md") for more information.
The transformation detail report includes a Linux readiness report section that identifies compatibility issues in moving from
Windows to Linux that require human attention.

If any of the items in the **Code groups** table require input under the Linux porting status,
you must manually update some files to run your application on Linux.
The transformation detail report includes a Linux readiness report section that
identifies compatibility issues in moving from Windows to Linux that require human attention. 15. AWS Transform generates a _NextSteps.md_ file, which describes any
remaining porting work needed. To download the report, choose the **Download next steps**
button at the top of the transformation detail report. You can use the NextSteps.md
file to transform the project again with AWS Transform and a revised plan, or use it as input
to an AI code companion. 16. To update your files in place, choose **Accept changes** from
the **Actions** dropdown menu.
