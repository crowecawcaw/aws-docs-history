# Notebook job workflows

Since a notebook job runs your custom code, you can create a pipeline that includes one or
more notebook job steps. ML workflows often contain multiple steps, such as a processing step
to preprocess data, a training step to build your model, and a model evaluation step, among
others. One possible use of notebook jobs is to handle preprocessing—you might have a
notebook that performs data transformation or ingestion, an EMR step that performs data
cleaning, and another notebook job that performs featurization of your inputs before
initiating a training step. A notebook job may require information from previous steps in the
pipeline or from user-specified customization as parameters in the input notebook. For
examples that show how to pass environment variables and parameters to your notebook and
retrieve information from prior steps, see [Pass information to and from your
notebook step](create-notebook-auto-run-dag-seq.md "create-notebook-auto-run-dag-seq.md").

In another use case, one of your notebook jobs might call another notebook to perform some
tasks during your notebook run—in this scenario you need to specify these sourced
notebooks as dependencies with your notebook job step. For information about how to call
another notebook, see [Invoke another notebook in your notebook
job](create-notebook-auto-run-dag-call.md "create-notebook-auto-run-dag-call.md").

To view sample notebooks that demonstrate how to schedule notebook jobs with the SageMaker AI
Python SDK, see [notebook job sample notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines/notebook-job-step "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines/notebook-job-step").
