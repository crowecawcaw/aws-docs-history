

# View action details in a pipeline (console)
<a name="pipelines-view-details-console"></a>

You can view details for a pipeline, including details for actions in each stage.

**Note**  
After an hour, the detailed view of a pipeline stops refreshing automatically in your browser. To view current information, refresh the page.

**To view action details in a pipeline**

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home).

   The **Pipelines** page displays.

1. On any action, choose **View details** to open a dialog box with details about the action execution, logs, and action configuration.
**Note**  
The **Logs** tab is available for CodeBuild and CloudFormation actions.

1. To see the action summary for an action in a stage of a pipeline, choose **View details** on the action, and then choose the **Summary** tab.  
![The Summary tab shows information for the action summary.](http://docs.aws.amazon.com/codepipeline/latest/userguide/images/details-summary-tab.png)

1. To see the action logs for an action with logs, choose **View details** on the action, and then choose the **Logs** tab.  
![The Logs tab shows information for the action logs.](http://docs.aws.amazon.com/codepipeline/latest/userguide/images/details-logs-tab.png)

1. To see the configuration details for an action, choose the **Configuration** tab.  
![The Configuration tab shows information for the action configuration.](http://docs.aws.amazon.com/codepipeline/latest/userguide/images/details-configuration-tab.png)