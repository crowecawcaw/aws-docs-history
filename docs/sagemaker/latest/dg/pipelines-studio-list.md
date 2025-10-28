# View the details of a pipeline

You can view the details of a SageMaker AI pipeline to understand its parameters, the dependencies of
its steps, or monitor its progress and status. This can help you troubleshoot or optimize
your workflow. You can access the details of a
given pipeline using the Amazon SageMaker Studio console and explore its execution history, definition,
parameters, and metadata.

Alternatively, if your pipeline is associated with a SageMaker AI Project, you can access the
pipeline details from the project's details page. For more information, see [View Project Resources](sagemaker-projects-resources.md "sagemaker-projects-resources.md").

To view the details of a SageMaker AI pipeline, complete the following steps based on whether you
use Studio or Studio Classic.

###### Note

Model repacking happens when the pipeline needs to include a custom script in the
compressed model file (model.tar.gz) to be uploaded to Amazon S3 and used to deploy a model to a
SageMaker AI endpoint. When SageMaker AI pipeline trains a model and registers it to the model registry, it
introduces a repack step _if_ the trained model output from
the training job needs to include a custom inference script. The repack step uncompresses
the model, adds a new script, and recompresses the model. Running the pipeline adds the
repack step as a training job.

Studio

1. Open the SageMaker Studio console by following the instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. (Optional) To filter the list of pipelines by name, enter a full or partial
   pipeline name in the search field.
4. Select a pipeline name to view details about the pipeline.
5. Choose one of the following tabs to view pipeline details:
   - **Executions** – Details about the
     executions.
   - **Graph** – The pipeline graph, including all
     steps.
   - **Parameters** – The run parameters and metrics
     related to the pipeline.
   - **Information** – The metadata associated with the
     pipeline, such as tags, the pipeline Amazon Resource Name (ARN), and role ARN.
     You can also edit the pipeline description from this page.

Studio Classic

1. Sign in to Amazon SageMaker Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
2. In the Studio Classic sidebar, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Select **Pipelines** from the menu.
4. To narrow the list of pipelines by name, enter a full or partial pipeline name
   in the search field.
5. Select a pipeline name to view details about the pipeline. The pipeline details
   tab opens and displays a list of pipeline executions. You can start an execution or
   choose one of the other tabs for more information about the pipeline. Use the
   **Property Inspector** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/gears.png)
   ) to choose which columns to display.
6. From the pipeline details page, choose one of the following tabs to view details
   about the pipeline:
   - **Executions** – Details about the executions. You
     can create an execution from this tab or the **Graph**
     tab.
   - **Graph** – The DAG for the pipeline.
   - **Parameters** – Includes the model approval
     status.
   - **Settings** – The metadata associated with the
     pipeline. You can download the pipeline definition file and edit the pipeline
     name and description from this tab.
