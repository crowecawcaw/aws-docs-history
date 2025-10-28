# Custom model development in Neptune ML

A good way to start custom model development is by following [Neptune
ML toolkit examples](https://github.com/awslabs/neptuneml-toolkit/tree/main/examples/custom-models/introduction "https://github.com/awslabs/neptuneml-toolkit/tree/main/examples/custom-models/introduction") to structure and write your training module.
The Neptune ML toolkit also implements modularized graph ML model components in the [modelzoo](https://github.com/awslabs/neptuneml-toolkit/tree/main/src/neptuneml_toolkit/modelzoo "https://github.com/awslabs/neptuneml-toolkit/tree/main/src/neptuneml_toolkit/modelzoo")
that you can stack and use to create your custom model.

In addition, the toolkit provides utility functions that help you generate the
necessary artifacts during model training and model transform. You can import this
Python package in your custom implementation. Any functions or modules provided in
the toolkit are also available in the Neptune ML training environment.

If your Python module has additional external dependencies, you can include these
additional dependencies by creating a `requirements.txt` file in your module's
directory. The packages listed in the `requirements.txt` file will then
be installed before your training script is run.

At a minimum, the Python module that implements your custom model needs to contain
the following:

- A training script entry point
- A transform script entry point
- A `model-hpo-configuration.json` file

## Custom model training script development in Neptune ML

Your custom model training script should be an executable Python script
like the Neptune ML toolkit's [`train.py`](https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/train.py "https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/train.py")
example. It must accept hyperparameter names and values as command-line arguments.
During model training, the hyperparameter names are obtained from the
`model-hpo-configuration.json` file. The hyperparameter values either fall
within the valid hyperparameter range if the hyperparameter is tunable, or take the
default hyperparameter value if it is not tunable.

Your training script is run on a SageMaker AI training instance using a syntax like this:

```
python3 `(script entry point)` --`(1st parameter)` `(1st value)` --`(2nd parameter)` `(2nd value)` `(...)`
```

For all tasks, the Neptune ML AutoTrainer sends several required parameters
to your training script in addition to the hyperparameters that you specify, and
your script must be able to handle these additional parameters in order to work
properly.

These additional required parameters vary somewhat by task:

###### For node classification or node regression

- **`task`**   –  
  The task type used internally by Neptune ML. For node classification
  this is `node_class`, and for node regression it is
  `node_regression`.
- **`model`**   –  
  The model name used internally by Neptune ML, which is `custom`
  in this case.
- **`name`**   –  
  The name of the task used internally by Neptune ML, which is
  `node_class-custom` for node classification in this case,
  and `node_regression-custom` for node regression.
- **`target_ntype`**   –  
  The name of the node type for classification or regression.
- **`property`**   –  
  The name of the node property for classification or regression.

###### For link prediction

- **`task`**   –  
  The task type used internally by Neptune ML. For link prediction, this
  is `link_predict`.
- **`model`**   –  
  The model name used internally by Neptune ML, which is `custom`
  in this case.
- **`name`**   –  
  The name of the task used internally by Neptune ML, which is
  `link_predict-custom` in this case.

###### For edge classification or edge regression

- **`task`**   –  
  The task type used internally by Neptune ML. For edge classification
  this is `edge_class`, and for edge regression it is
  `edge_regression`.
- **`model`**   –  
  The model name used internally by Neptune ML, which is `custom`
  in this case.
- **`name`**   –  
  The name of the task used internally by Neptune ML, which is
  `edge_class-custom` for edge classification in this case,
  and `edge_regression-custom` for edge regression.
- **`target_etype`**   –  
  The name of the edge type for classification or regression.
- **`property`**   –  
  The name of the edge property for classification or regression.

Your script should save the model parameters, as well as any other artifacts
that will be needed to at the end of training.

You can use Neptune ML toolkit utility functions to determine the location
of the processed graph data, the location where the model parameters should be
saved, and what GPU devices are available on the training instance. See the [train.py](https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/train.py "https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/train.py")
sample training script for examples of how to use these utility functions.

## Custom model transform script development in Neptune ML

A transform script is needed to take advantage of the Neptune ML [incremental workflow](machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-incremental "machine-learning-overview-evolving-data-incremental.md#machine-learning-overview-incremental") for model
inference on evolving graphs without retraining the model. Even if all the artifacts
necessary for model deployment are generated by the training script, you still need
to provide a transform script if you want to generate updated models without retraining
the model.

###### Note

[Real-time inductive
inference](machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference "machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference") is not currently supported for custom models.

Your custom model transform script should be an executable Python script like the Neptune ML toolkit's [transform.py](https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/transform.py "https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/transform.py")
example script. Because this script is invoked during model training with no command line arguments,
any command line arguments that the script does accept must have defaults.

The script runs on a SageMaker AI training instance with a syntax like this:

```
python3 `(your transform script entry point)`
```

Your transform script will need various pieces of information, such as:

- The location of the processed graph data.
- The location where the model parameters are saved and where new
  model artifacts should be saved.
- The devices available on the instance.
- The hyperparameters that generated the best model.

These inputs are obtained using Neptune ML utility functions that your
script can call. See the toolkit's sample [transform.py](https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/transform.py "https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/transform.py")
script for examples of how to do that.

The script should save the node embeddings, node ID mappings, and any other artifacts
necessary for model deployment for each task. See the [model artifacts documentation](machine-learning-model-artifacts.md "machine-learning-model-artifacts.md") for more
information about the model artifacts required for different Neptune ML tasks.

## Custom `model-hpo-configuration.json` file in Neptune ML

The `model-hpo-configuration.json` file defines hyperparameters for your custom
model. It is in the same [format](machine-learning-customizing-hyperparams.md "machine-learning-customizing-hyperparams.md")
as the `model-hpo-configuration.json` file used with the Neptune ML built-in models,
and takes precedence over the version that is auto-generated by Neptune ML and uploaded to
the location of your processed data.

When you add a new hyperparameter to your model, you must also add an entry for the hyperparameter
in this file so that the hyperparameter is passed to your training script.

You must provide a range for a hyperparameter if you want it to be tunable, and set it as a
`tier-1`, `tier-2`, or `tier-3` param. The hyperparameter will be
tuned if the total number of training jobs configured allow for tuning hyperparameters in its tier.
For a non-tunable parameter, you must provide a default value and add the hyperparameter to the
`fixed-param` section of the file. See the toolkit's sample [sample
`model-hpo-configuration.json` file](https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/model-hpo-configuration.json "https://github.com/awslabs/neptuneml-toolkit/blob/main/examples/custom-models/introduction/movie-lens-rgcn/node-class/src/model-hpo-configuration.json") for an example of how to do that.

You must also provide the metric definition that the SageMaker AI HyperParameter Optimization job
will use to evaluate the candidate models trained. To do this, you add an `eval_metric`
JSON object to the `model-hpo-configuration.json` file like this:

```
"eval_metric": {
  "tuning_objective": {
      "MetricName": "`(metric_name)`",
      "Type": "Maximize"
  },
  "metric_definitions": [
    {
      "Name": "`(metric_name)`",
      "Regex": "`(metric regular expression)`"
    }
  ]
},
```

The `metric_definitions` array in the `eval_metric` object lists metric definition
objects for each metric that you want SageMaker AI to extract from the training instance. Each
metric definition object has a `Name` key that lets you provide a name for
the metric (such as "accuracy", "f1", and so on) The `Regex` key lets you provide a
regular expression string that matches how that particular metric is printed in the
training logs. See the [SageMaker AI
HyperParameter Tuning page](../../../sagemaker/latest/dg/automatic-model-tuning-define-metrics.md "../../../sagemaker/latest/dg/automatic-model-tuning-define-metrics.md") for more details on how to define metrics.

The `tuning_objective` object in `eval_metric` then allows you
to specify which of the metrics in `metric_definitions` should be used as the
evaluation metric that serves as the objective metric for hyperparameter optimization.
The value for the `MetricName` must match the value of a `Name` in one of
the definitions in `metric_definitions`. The value for `Type`
should be either "Maximize" or "Minimize" depending on whether the metric should be
interpreted as greater-is-better (like "accuracy") or less-is-better (like "mean-squared-error".

Errors in this section of the `model-hpo-configuration.json` file can result
in failures of the Neptune ML model training API job, because the SageMaker AI HyperParameter Tuning
job will not be able to select the best model.

## Local testing of your custom model implementation in Neptune ML

You can use the Neptune ML toolkit Conda environment to run your code locally
in order to test and validate your model. If you're developing on a Neptune Notebook
instance, then this Conda environment will be pre-installed on the Neptune Notebook
instance. If you’re developing on a different instance, then you need to follow the
[local
setup instructions](https://github.com/awslabs/neptuneml-toolkit#local-installation "https://github.com/awslabs/neptuneml-toolkit#local-installation") in the Neptune ML toolkit.

The Conda environment accurately reproduces the environment where your model will
run when you call the [model training
API](machine-learning-api-modeltraining.md "machine-learning-api-modeltraining.md"). All of the example training scripts and transform scripts allow you to pass
a command line `--local` flag to run the scripts in a local environment
for easy debugging. This is a good practice while developing your own model because
it allows you to interactively and iteratively test your model implementation.
During model training in the Neptune ML production training environment, this
parameter is omitted.
