

# Lift-and-shift Python code with the @step decorator
<a name="pipelines-step-decorator"></a>

The `@step` decorator is a feature that converts your local machine learning (ML) code into one or more pipeline steps. You can write your ML function as you would for any ML project. Once tested locally or as a training job using the `@remote` decorator, you can convert the function to a SageMaker AI pipeline step by adding a `@step` decorator. You can then pass the output of the `@step`-decorated function call as a step to Pipelines to create and run a pipeline. You can chain a series of functions with the `@step` decorator to create a multi-step directed acyclic graph (DAG) pipeline as well.

The setup to use the `@step` decorator is the same as the setup to use the `@remote` decorator. You can refer to the remote function documentation for details about how to [setup the environment](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator.html#train-remote-decorator-env) and [use a configuration file](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-config.html) to set defaults. For more information about the `@step` decorator, see [sagemaker.workflow.function\_step.step](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.function_step.step).

To view to sample notebooks that demonstrate the use of `@step` decorator, see [@step decorator sample notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines/step-decorator).

The following sections explain how you can annotate your local ML code with a `@step` decorator to create a step, create and run a pipeline using the step, and customize the experience for your use case.

**Topics**
+ [Create a pipeline with `@step`-decorated functions](pipelines-step-decorator-create-pipeline.md)
+ [Run a pipeline](pipelines-step-decorator-run-pipeline.md)
+ [Configure your pipeline](pipelines-step-decorator-cfg-pipeline.md)
+ [Best Practices](pipelines-step-decorator-best.md)
+ [Limitations](pipelines-step-decorator-limit.md)