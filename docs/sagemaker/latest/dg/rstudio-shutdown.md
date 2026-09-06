

# Shut down RStudio
<a name="rstudio-shutdown"></a>

**Important**  
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).  
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

To shut down and restart your Posit Workbench and the associated RStudioServerPro app, you must first shut down all of your existing RSessions. You can shut down the RSessionGateway apps from within RStudio. You can then shut down the RStudioServerPro app using the AWS CLI. After the RStudioServerPro app is shut down, you must reopen RStudio through the SageMaker AI console.

Any unsaved notebook information is lost in the process. The user data in the Amazon EFS volume isn't impacted.

**Note**  
If you are using a custom image with RStudio, ensure that your docker image is using an RStudio version that is compatible with the version of Posit Workbench being used by SageMaker AI after you restart your RStudioServerPro app.

The following topics show how to shut down the RSessionGateway and RStudioServerPro apps and restart them.

## Suspend your RSessions
<a name="rstudio-suspend"></a>

Complete the following procedure to suspend all of your RSessions.

1. From the RStudio Launcher, identify the RSession that you want to suspend. 

1. Select **Suspend** for the session. 

1. Repeat this for all RSessions.

## Delete your RSessions
<a name="rstudio-delete"></a>

Complete the following procedure to shut down all of your RSessions.

1. From the RStudio Launcher, identify the RSession that you want to delete. 

1. Select **Quit** for the session. This opens a new **Quit Session** window. 

1. From the **Quit Session** window, select **Force Quit**, to end all child processes in the session.

1. Select **Quit Session** to confirm deletion of the session.

1. Repeat this for all RSessions.

## Delete your RStudioServerPro app
<a name="rstudio-delete-restart"></a>

Run the following commands from the AWS CLI to delete and restart your RStudioServerPro app.

1. Delete the RStudioServerPro application by using your current domain id. 

   ```
   aws sagemaker delete-app \
       --domain-id {{<domainId>}} \
       --user-profile-name domain-shared \
       --app-type RStudioServerPro \
       --app-name default
   ```

1. Re-create the RStudioServerPro application. 

   ```
   aws sagemaker create-app \
       --domain-id {{<domainId>}} \
       --user-profile-name domain-shared \
       --app-type RStudioServerPro \
       --app-name default
   ```