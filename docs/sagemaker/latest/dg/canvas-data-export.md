# Automate data preparation in SageMaker Canvas

After you transform your data in data flow, you can export the transforms to your machine learning workflows. When you export your transforms, SageMaker Canvas creates a Jupyter notebook.
You must run the notebook within Amazon SageMaker Studio Classic. For information about getting started with Studio Classic, contact your administrator.

## Automate data preparation using Pipelines

When you want to build and deploy large-scale machine learning (ML) workflows, you can
use Pipelines to create workflows that manage and deploy SageMaker AI jobs. With Pipelines, you can
build workflows that manage your SageMaker AI data preparation, model training, and model
deployment jobs. You can use the first-party algorithms that SageMaker AI offers by using Pipelines.
For more information on Pipelines, see [SageMaker Pipelines](pipelines.md "pipelines.md").

When you export one or more steps from your data flow to Pipelines, Data Wrangler creates a Jupyter
notebook that you can use to define, instantiate, run, and manage a pipeline.

### Use a Jupyter Notebook to

Create a Pipeline

Use the following procedure to create a Jupyter notebook to export your Data Wrangler flow to
Pipelines.

Use the following procedure to generate a Jupyter notebook and run it to export
your Data Wrangler flow to Pipelines.

1. Choose the **+** next to the node that you want to
   export.
2. Choose **Export data flow**.
3. Choose **Pipelines (via Jupyter Notebook)**.
4. Download the Jupyter notebook or copy it to an Amazon S3 location. We recommend copying it to an Amazon S3 location that you can access within Studio Classic. Contact your administrator if you need guidance on a suitable location.
5. Run the Jupyter notebook.

You can use the Jupyter notebook that Data Wrangler produces to define a pipeline. The
pipeline includes the data processing steps that are defined by your Data Wrangler flow.

You can add additional steps to your pipeline by adding steps to the
`steps` list in the following code in the notebook:

```
pipeline = Pipeline(
    name=pipeline_name,
    parameters=[instance_type, instance_count],
    steps=[step_process], #Add more steps to this list to run in your Pipeline
)
```

For more information on defining pipelines, see [Define SageMaker AI
Pipeline](define-pipeline.md "define-pipeline.md").

## Automate data preparation using an inference endpoint

Use your Data Wrangler flow to process data at the time of inference by creating a SageMaker AI serial inference pipeline from your Data Wrangler flow. An inference pipeline is a series of steps that results in a trained model making predictions on new data. A serial inference pipeline within Data Wrangler transforms the raw data and provides it to the machine learning model for a prediction.
You create, run, and manage the inference pipeline from a Jupyter notebook within Studio Classic. For more information about accessing the notebook, see [Use a Jupyter notebook to
create an inference endpoint](#canvas-inference-notebook "#canvas-inference-notebook").

Within the notebook, you can either train a machine learning model or specify one that you've already trained. You can either use Amazon SageMaker Autopilot or XGBoost to train the model using the data that you've transformed in your Data Wrangler flow.

The pipeline provides the ability to perform either batch or real-time inference. You can also add the Data Wrangler flow to SageMaker Model Registry. For more information about hosting models, see [Multi-model endpoints](multi-model-endpoints.md "multi-model-endpoints.md").

###### Important

You can't export your Data Wrangler flow to an inference endpoint if it has the following transformations:

- Join
- Concatenate
- Group by
  If you must use the preceding transforms to prepare your data, use the following procedure.

###### To prepare your data for inference with unsupported transforms

1. Create a Data Wrangler flow.
2. Apply the preceding transforms that aren't supported.
3. Export the data to an Amazon S3 bucket.
4. Create a separate Data Wrangler flow.
5. Import the data that you've exported from the preceding flow.
6. Apply the remaining transforms.
7. Create a serial inference pipeline using the Jupyter notebook that we provide.
   For information about exporting your data to an Amazon S3 bucket see [Export data](canvas-export-data.md "canvas-export-data.md"). For information about opening the Jupyter notebook used to create the serial inference pipeline, see [Use a Jupyter notebook to
   create an inference endpoint](#canvas-inference-notebook "#canvas-inference-notebook").

Data Wrangler ignores transforms that remove data at the time of inference.
For example, Data Wrangler ignores the [Handle Missing Values](canvas-transform.md#canvas-transform-handle-missing "canvas-transform.md#canvas-transform-handle-missing") transform if you use the **Drop missing** configuration.

If you've refit transforms to your entire dataset, the transforms carry over to your inference pipeline. For example, if you used the median value to impute missing values, the median value from refitting the transform is applied to your inference requests.
You can either refit the transforms from your Data Wrangler flow when you're using the Jupyter notebook or when you're exporting your data to an inference pipeline.
.

The serial inference pipeline supports the following data types for the input and output strings. Each data type has a set of requirements.

###### Supported datatypes

- `text/csv` – the datatype for CSV strings

      + The string can't have a header.
      + Features used for the inference pipeline must be in the same order as features in the training dataset.
      + There must be a comma delimiter between features.
      + Records must be delimited by a newline character.

  The following is an example of a validly formatted CSV string that you can provide in an inference request.

```

abc,0.0,"Doe, John",12345\ndef,1.1,"Doe, Jane",67890

```

- `application/json` – the datatype for JSON strings

      + The features used in the dataset for the inference pipeline must be in the same order as the features in the training dataset.
      + The data must have a specific schema. You define schema as a single `instances` object that has a set of `features`. Each `features` object represents an observation.

  The following is an example of a validly formatted JSON string that you can provide in an inference request.

```
{
    "instances": [
        {
            "features": ["abc", 0.0, "Doe, John", 12345]
        },
        {
            "features": ["def", 1.1, "Doe, Jane", 67890]
        }
    ]
}

```

### Use a Jupyter notebook to

create an inference endpoint

Use the following procedure to export your Data Wrangler
flow to create an inference pipeline.

To create an inference pipeline using a Jupyter notebook, do the following.

1. Choose the **+** next to the node that you want to
   export.
2. Choose **Export data flow**.
3. Choose **SageMaker AI Inference Pipeline (via Jupyter Notebook)**.
4. Download the Jupyter notebook or copy it to an Amazon S3 location. We recommend copying it to an Amazon S3 location that you can access within Studio Classic. Contact your administrator if you need guidance on a suitable location.
5. Run the Jupyter notebook.

When you run the Jupyter notebook, it creates an inference flow artifact. An inference flow artifact is a Data Wrangler flow file with additional metadata used to create the serial inference pipeline.
The node that you're exporting encompasses all of the transforms from the preceding nodes.

###### Important

Data Wrangler needs the inference flow artifact to run the inference pipeline. You can't use your own flow file as the artifact. You must create it by using the preceding procedure.

## Automate data preparation using Python Code

To export all steps in your data flow to a Python file that you can manually
integrate into any data processing workflow, use the following procedure.

Use the following procedure to generate a Jupyter notebook and run it to export your
Data Wrangler flow to Python code.

1. Choose the **+** next to the node that you want to
   export.
2. Choose **Export data flow**.
3. Choose **Python Code**.
4. Download the Jupyter notebook or copy it to an Amazon S3 location. We recommend copying it to an Amazon S3 location that you can access within Studio Classic. Contact your administrator if you need guidance on a suitable location.
5. Run the Jupyter notebook.

You might need to configure the Python script to make it run in your pipeline. For
example, if you're running a Spark environment, make sure that you are running the
script from an environment that has permission to access AWS resources.
