# Logging parameters and metrics with

Amazon SageMaker Experiments

This guide show how to log parameters and metrics with Amazon SageMaker Experiments. A SageMaker AI
experiment consists of runs, and each run consists of all the inputs, parameters,
configurations and results for a single model training interaction.

You can log parameters and metrics from a remote function using either the @remote
decorator or the `RemoteExecutor` API.

To log parameters and metrics from a remote function, choose one of the following
methods:

- Instantiate a SageMaker AI experiment run inside a remote function using
  `Run` from the SageMaker Experiments library. For more information,
  see [Create an Amazon SageMaker AI
  Experiment](experiments-create.md "experiments-create.md").
- Use the `load_run` function inside a remote function from the SageMaker AI
  Experiments library. This will load a `Run` instance that is declared
  outside of the remote function.
  The following sections show how to create and track lineage with SageMaker AI experiment runs
  by using the previous listed methods. The sections also describe cases that are not
  supported by SageMaker training.

## Use the @remote

decorator to integrate with SageMaker Experiments

You can either instantiate an experiment in SageMaker AI, or load a current SageMaker AI
experiment from inside a remote function. The following sections show you show to
use either method.

### Create an

experiment with SageMaker Experiments

You can create an experiment run in SageMaker AI experiment. To do this you pass your
experiment name, run name, and other parameters into your remote
function.

The following code example imports the name of your experiment, the name of
the run, and the parameters to log during each run. The parameters
`param_1` and `param_2` are logged over time inside a
training loop. Common parameters may include batch size or epochs. In this
example, the metrics `metric_a` and `metric_b` are logged
for a run over time inside a training loop. Other common metrics may include
`accuracy` or `loss`.

```
from sagemaker.remote_function import remote
from sagemaker.experiments.run import Run

# Define your remote function
@remote
def train(`value_1`, `value_2`, `exp_name`, `run_name`):
    ...
    ...
    #Creates the experiment
    with Run(
        experiment_name=exp_name,
        run_name=run_name,
    ) as run:
        ...
        #Define values for the parameters to log
        run.log_parameter("`param_1`", value_1)
        run.log_parameter("`param_2`", value_2)
        ...
        #Define metrics to log
        run.log_metric("`metric_a`", 0.5)
        run.log_metric("`metric_b`", 0.1)


# Invoke your remote function
train(1.0, 2.0, "my-exp-name", "my-run-name")
```

### Load

current SageMaker Experiments with a job initiated by the @remote
decorator

Use the `load_run()` function from the SageMaker Experiments library to
load the current run object from the run context. You can also use the
`load_run()` function within your remote function. Load the run
object initialized locally by the `with` statement on the run object
as shown in the following code example.

```
from sagemaker.experiments.run import Run, load_run

# Define your remote function
@remote
def train(`value_1`, `value_2`):
    ...
    ...
    with load_run() as run:
        run.log_metric("`metric_a`", value_1)
        run.log_metric("`metric_b`", value_2)


# Invoke your remote function
with Run(
    experiment_name="`my-exp-name`",
    run_name="`my-run-name`",
) as run:
    train(0.5, 1.0)
```

## Load a current experiment

run within a job initiated with the `RemoteExecutor` API

You can also load a current SageMaker AI experiment run if your jobs were initiated with
the `RemoteExecutor` API. The following code example shows how to use
`RemoteExecutor` API with the SageMaker Experiments `load_run`
function. You do this to load a current SageMaker AI experiment run and capture metrics in
the job submitted by `RemoteExecutor`.

```
from sagemaker.experiments.run import Run, load_run

def square(x):
    with load_run() as run:
        result = x * x
        run.log_metric("result", result)
    return result


with RemoteExecutor(
    max_parallel_job=2,
    instance_type="`ml.m5.large`"
) as e:
    with Run(
        experiment_name="`my-exp-name`",
        run_name="`my-run-name`",
    ):
        future_1 = e.submit(square, 2)
```

## Unsupported uses

for SageMaker Experiments while annotating your code with an @remote
decorator

SageMaker AI does not support passing a `Run` type object to an @remote
function or using global `Run` objects. The following examples show code
that will throw a `SerializationError`.

The following code example attempts to pass a `Run` type object to an
@remote decorator, and it generates an error.

```
@remote
def func(run: Run):
    run.log_metrics("metric_a", 1.0)

with Run(...) as run:
    func(run) ---> SerializationError caused by NotImplementedError
```

The following code example attempts to use a global `run` object
instantiated outside of the remote function. In the code example, the
`train()` function is defined inside the `with Run`
context, referencing a global run object from within. When `train()` is
called, it generates an error.

```
with Run(...) as run:
    @remote
    def train(`metric_1`, `value_1`, `metric_2`, `value_2`):
        run.log_parameter(metric_1, value_1)
        run.log_parameter(metric_2, value_2)

    train("p1", 1.0, "p2", 0.5) ---> SerializationError caused by NotImplementedError
```
