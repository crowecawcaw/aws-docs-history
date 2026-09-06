

# Download a pipeline definition file
<a name="pipelines-studio-download"></a>

You can download the definition file for your SageMaker AI pipeline directly from the Amazon SageMaker Studio UI. You can use this pipeline definition file for:
+ Backup and restoration: Use the downloaded file to create a backup of your pipeline configuration, which you can restore in case of infrastructure failures or accidental changes.
+ Version control: Store the pipeline definition file in a source control system to track changes to the pipeline and revert to previous versions if needed.
+ Programmatic interactions: Use the pipeline definition file as input to the SageMaker SDK or AWS CLI.
+ Integration with automation processes: Integrate the pipeline definition into your CI/CD workflows or other automation processes.

To download the definition file of a pipeline, complete the following steps based on whether you use Studio or Studio Classic.

------
#### [ Studio ]

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, select **Pipelines**.

1. (Optional) To filter the list of pipelines by name, enter a full or partial pipeline name in the search field.

1. Select a pipeline name. The **Executions** page opens and displays a list of pipeline executions.

1. Stay on the **Executions** page or choose the **Graph**, **Information**, or **Parameters** page to the left of the pipeline executions table. You can download the pipeline definition from any of these pages.

1. At the top right of the page, choose the vertical ellipsis and choose **Download pipeline definition (JSON)**.

------
#### [ Studio Classic ]

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-launch.html).

1. In the Studio Classic sidebar, choose the **Home** icon ( ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Select **Pipelines** from the menu.

1. To narrow the list of pipelines by name, enter a full or partial pipeline name in the search field.

1. Select a pipeline name.

1. Choose the **Settings** tab.

1. Choose **Download pipeline definition file**.

------