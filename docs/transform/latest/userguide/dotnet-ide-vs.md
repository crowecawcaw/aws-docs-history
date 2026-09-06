

# Modernizing .NET using AWS Transform in Visual Studio
<a name="dotnet-ide-vs"></a>

Complete these steps to port a Windows-based .NET application to a Linux-compatible cross-platform .NET application with AWS Transform in Visual Studio 2026 or 2022. 

## Step 1: Prerequisites
<a name="transform-dotnet-prerequisites"></a>

Before you continue, make sure you've downloaded and installed the [AWS Toolkit extension with Amazon Q](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022) from the Visual Studio Marketplace. Review the AWS Transform [capabilities](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html#capabilities) and [limitations](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html#limitations) for .NET modernization to confirm that your code can be transformed. 

## Step 2: Authenticate in Visual Studio
<a name="transform-dotnet-vs-authenticate"></a>

To connect to your AWS accounts from the Toolkit for Visual Studio, open the Getting Started with the AWS Toolkit User Interface (connection UI): 

1. From the Visual Studio main menu, navigate to **Extensions > AWS Toolkit > Getting Started** to open the **Getting Started: AWS Toolkit page**.

1. Select **AWS Transform** authentication.

1. Choose an existing profile or create a new one. When creating a new profile, enter a name for the profile and your AWS Transform start URL, which was emailed to you after you were added to IAM Identity Center by your administrator.

1. Choose **Connect**. Follow the prompts to sign in and grant access permissions through your web browser. In Visual Studio, you should see **Connected with IAM Identity Center**.

1. After signing in, you are taken to the **AWS Transform Dashboard**. From this landing page, you can do the following:
   + Select an AWS Transform profile (region)
   + Select or create a workspace
   + View status of transformation jobs

## Step 3: Transform your application
<a name="transform-dotnet-app"></a>

To transform your .NET solution or project, complete the following procedure:

**Start transformation**

1. Open any C\# or VB.NET based solution or project in Visual Studio that you want to transform. 

1. From **Solution Explorer**, right click a solution or project you want to transform, and choose **Port with AWS Transform**.

1. The **Port with AWS Transform** dialog appears.

   1. In the **Choose a workspace** dropdown, create a workspace or select an existing one. Workspaces make your activity visible in the AWS Transform web application, where you can invite collaborators to view and chat about transformation jobs.

   1. In the **Choose a .NET target** dropdown menu, choose the .NET version you want to upgrade to.

   1. For **Transformation Mode**, select **Autonomous** for unattended transformation or **Interactive** for interactive transformation.

   1. Choose **Start** to begin the transformation.

1. Once the transformation job starts, the **AWS Transform Job Plan**, **Chat**, and **Worklog** windows appear.

**Assessment and transformation plan**

1. After AWS Transform analyzes your code, an assessment report and transformation plan are shown in chat. In interactive mode, chat will pause for you to review them. If you prefer not to review in chat, you can use these alternatives:
   + To view assessment or plan in the code editor, choose **Show assessment** or **Show transformation plan** in the AWS Transform Job Plan window.
   + To download assessment or plan, use the download icon in the Job Plan window.

1. Optionally modify the transformation plan. You can discuss the plan with chat, such as exploring other options. You make plan changes by giving instructions in chat, or by uploading a revised transformation plan using the download icon in the Job Plan window. You can freely add, remove, or modify steps. Chat will confirm its understanding of your instructions with a revised plan.

1. Optionally upload steering documents. In the chat window, use the upload icon to upload steering documents such as application specs, organizational tech stack preferences and conventions, or coding examples. After uploading a steering document, describe it in the chat window to give the agent context.

1. Once you are satisfied with the plan, give approval in chat and the transformation will begin.

1. In interactive mode, you can set checkpoints to stop after a project is transformed for review. The steps under **Transforming code** in the Job Plan window will have round checkpoint icons. All projects have checkpoints enabled by default. Use the check boxes to clear or set a checkpoint.

**Transformation and checkpoint reviews**

1. AWS Transform begins transforming your code. You can monitor progress of transformation steps in the AWS Transform Job Plan window. The Job Plan window displays the estimated maximum time remaining and your Job ID.

1. As projects are transformed, summaries are displayed in chat and code changes are applied.

1. In interactive mode, when a checkpoint is reached, the agent will pause so you can review the results. In the Job Plan window, you'll see a **View Results** button for the step it is paused on where you can review code differences. After reviewing the changes, you can ask for further changes in chat or make code changes yourself in Visual Studio.

1. You can iterate at the checkpoint as much as desired. When you're satisfied, instruct chat to continue, and it will move on to the next project.

**End of transformation**

1. After transforming your projects, the .NET agent will trigger a local build in Visual Studio, to confirm that the code builds successfully on your local machine. If there are errors, it will work to resolve them.

1. Once transformation is completed, there may be additional steps needed — such as transformation tasks AWS Transform could not perform, or changes needed for Linux compatibility. A next steps markdown file (*NextSteps.md*) is available for download which you can use as prompts to an AI code companion. Use the Job Plan window's download icon button to download *NextSteps.md*.

1. You can continue to interact in chat to ask questions or request additional changes.

1. Tell chat when you are ready to end your transformation job.