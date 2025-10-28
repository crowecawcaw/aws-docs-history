# Invoke a remote function

To invoke a function inside the @remote decorator, use either of the following
methods:

- [Use an @remote
  decorator to invoke a function](#train-remote-decorator-invocation-decorator "#train-remote-decorator-invocation-decorator").
- [Use the
  RemoteExecutor API to invoke a function](#train-remote-decorator-invocation-api "#train-remote-decorator-invocation-api").
  If you use the @remote decorator method to invoke a function, the training job will
  wait for the function to complete before starting a new task. However, if you use the
  `RemoteExecutor` API, you can run more than one job in parallel. The
  following sections show both ways of invoking a function.

## Use an @remote

decorator to invoke a function

You can use the @remote decorator to annotate a function. SageMaker AI will transform the
code inside the decorator into a SageMaker training job. The training job will then
invoke the function inside the decorator and wait for the job to complete. The
following code example shows how to import the required libraries, start a SageMaker AI
instance, and annotate a matrix multiplication with the @remote decorator.

```
from sagemaker.remote_function import remote
import numpy as np

@remote(instance_type="`ml.m5.large`")
def matrix_multiply(a, b):
    return np.matmul(a, b)

a = np.array([[1, 0],
             [0, 1]])
b = np.array([1, 2])

assert (matrix_multiply(a, b) == np.array([1,2])).all()
```

The decorator is defined as follows.

```
def remote(
    *,
    **kwarg):
        ...
```

When you invoke a decorated function, SageMaker Python SDK loads any exceptions raised
by an error into local memory. In the following code example, the first call to the
divide function completes successfully and the result is loaded into local memory.
In the second call to the divide function, the code returns an error and this error
is loaded into local memory.

```
from sagemaker.remote_function import remote
import pytest

@remote()
def divide(a, b):
    return a/b

# the underlying job is completed successfully
# and the function return is loaded
assert divide(10, 5) == 2

# the underlying job fails with "AlgorithmError"
# and the function exception is loaded into local memory
with pytest.raises(ZeroDivisionError):
    divide(10, 0)
```

###### Note

The decorated function is run as a remote job. If the thread is interrupted,
the underlying job will not be stopped.

### How to

change the value of a local variable

The decorator function is run on a remote machine. Changing a non-local
variable or input arguments inside a decorated function will not change the
local value.

In the following code example, a list and a dict are appended inside the
decorator function. This does not change when the decorator function is
invoked.

```
a = []

@remote
def func():
    a.append(1)

# when func is invoked, a in the local memory is not modified
func()
func()

# a stays as []

a = {}
@remote
def func(a):
    # append new values to the input dictionary
    a["key-2"] = "value-2"

a = {"key": "value"}
func(a)

# a stays as {"key": "value"}
```

To change the value of a local variable declared inside of a decorator
function, return the variable from the function. The following code example
shows that the value of a local variable is changed when it is returned from the
function.

```
a = {"key-1": "value-1"}

@remote
def func(a):
    a["key-2"] = "value-2"
    return a

a = func(a)

-> {"key-1": "value-1", "key-2": "value-2"}
```

### Data

serialization and deserialization

When you invoke a remote function, SageMaker AI automatically serializes your function
arguments during the input and output stages. Function arguments and returns are
serialized using [cloudpickle](https://github.com/cloudpipe/cloudpickle "https://github.com/cloudpipe/cloudpickle"). SageMaker AI supports serializing the following Python objects
and functions.

- Built-in Python objects including dicts, lists, floats, ints, strings,
  boolean values and tuples
- Numpy arrays
- Pandas Dataframes
- Scikit-learn datasets and estimators
- PyTorch models
- TensorFlow models
- The Booster class for XGBoost

The following can be used with some limitations.

- Dask DataFrames
- The XGBoost Dmatrix class
- TensorFlow datasets and subclasses
- PyTorch models

The following section contains best practices for using the previous Python
classes with some limitations in your remote function, information about where
SageMaker AI stores your serialized data and how to manage access to it.

#### Best practices for Python classes with limited support for remote data

serialization

You can use the Python classes listed in this section with limitations.
The next sections discuss best practices for how to use the following Python
classes.

- [Dask](https://www.dask.org/ "https://www.dask.org/") DataFrames
- The XGBoost DMatric class
- TensorFlow datasets and subclasses
- PyTorch models

[Dask](https://www.dask.org/ "https://www.dask.org/") is an open-source
library used for parallel computing in Python. This section shows
the following.

- How to pass a Dask DataFrame into your remote
  function
- How to convert summary statistics from a Dask DataFrame
  into a Pandas DataFrame

##### How to pass a Dask DataFrame into your remote

function

[Dask DataFrames](https://docs.dask.org/en/latest/dataframe.html "https://docs.dask.org/en/latest/dataframe.html") are often used to process large
datasets because they can hold datasets that require more memory
than is available. This is because a Dask DataFrame does not
load your local data into memory. If you pass a Dask DataFrame
as a function argument to your remote function, Dask may pass a
reference to the data in your local disk or cloud storage,
instead of the data itself. The following code shows an example
of passing a Dask DataFrame inside your remote function that
will operate on an empty DataFrame.

```
#Do not pass a Dask DataFrame  to your remote function as follows
def clean(df: dask.DataFrame ):
    cleaned = df[] \ ...
```

Dask will load the data from the Dask DataFrame into memory
only when you use the DataFrame . If you want to use a Dask
DataFrame inside a remote function, provide the path to the data
. Then Dask will read the dataset directly from the data path
that you specify when the code runs.

The following code example shows how to use a Dask DataFrame
inside the remote function `clean`. In the code
example, `raw_data_path` is passed to clean instead
of the Dask DataFrame. When the code runs, the dataset is read
directly from the location of an Amazon S3 bucket specified in
`raw_data_path`. Then the `persist`
function keeps the dataset in memory to facilitate the
subsequent `random_split` function and written back
to the output data path in an S3 bucket using Dask DataFrame API
functions.

```
import dask.dataframe as dd

@remote(
   instance_type='`ml.m5.24xlarge`',
   volume_size=`300`,
   keep_alive_period_in_seconds=`600`)
#pass the data path to your remote function rather than the Dask DataFrame  itself
def clean(raw_data_path: str, output_data_path: str: split_ratio: list[float]):
    df = dd.read_parquet(raw_data_path) #pass the path to your DataFrame
    cleaned = df[(df.column_a >= 1) & (df.column_a < 5)]\
        .drop(['column_b', 'column_c'], axis=1)\
        .persist() #keep the data in memory to facilitate the following random_split operation

    train_df, test_df = cleaned.random_split(split_ratio, random_state=10)

    train_df.to_parquet(os.path.join(output_data_path, 'train')
    test_df.to_parquet(os.path.join(output_data_path, 'test'))

clean("`s3://amzn-s3-demo-bucket/raw/`", "`s3://amzn-s3-demo-bucket/cleaned/`", split_ratio=`[0.7, 0.3]`)
```

##### How to convert summary statistics from a Dask DataFrame

into a Pandas DataFrame

Summary statistics from a Dask DataFrame can be converted into
a Pandas DataFrame by invoking the `compute` method
as shown in the following example code. In the example, the S3
bucket contains a large Dask DataFrame that cannot fit into
memory or into a Pandas dataframe. In the following example, a
remote function scans the data set and returns a Dask DataFrame
containing the output statistics from `describe` to a
Pandas DataFrame.

```
executor = RemoteExecutor(
    instance_type='`ml.m5.24xlarge`',
    volume_size=`300`,
    keep_alive_period_in_seconds=`600`)

future = executor.submit(lambda: dd.read_parquet("`s3://amzn-s3-demo-bucket/raw/`").describe().compute())

future.result()
```

DMatrix is an internal data structure used by XGBoost to load
data. A DMatrix object can’t be pickled in order to move easily
between compute sessions. Directly passing DMatrix instances will
fail with a `SerializationError`.

##### How to pass a data object to your remote function and train

with XGBoost

To convert a Pandas DataFrame into a DMatrix instance and use
it for training in your remote function, pass it directly to the
remote function as shown in the following code example.

```
import xgboost as xgb

@remote
def train(df, params):
    #Convert a pandas dataframe into a DMatrix DataFrame and use it for training
    dtrain = DMatrix(df)
    return xgb.train(dtrain, params)
```

TensorFlow datasets and subclasses are internal objects used by
TensorFlow to load data during training. TensorFlow datasets and
subclasses can’t be pickled in order to move easily between compute
sessions. Directly passing Tensorflow datasets or subclasses will
fail with a `SerializationError`. Use the Tensorflow I/O
APIs to load data from the storage, as shown in the following code
example.

```
import tensorflow as tf
import tensorflow_io as tfio

@remote
def train(data_path: str, params):

    dataset = tf.data.TextLineDataset(tf.data.Dataset.list_files(f"{data_path}/*.txt"))
    ...

train("`s3://amzn-s3-demo-bucket/data`", {})
```

PyTorch models are serializable and can be passed between your
local environment and remote function. If your local environment and
remote environment have different device types, such as (GPUs and
CPUs), you cannot return a trained model to your local environment.
For example, if the following code is developed in a local
environment without GPUs but run in an instance with GPUs, returning
the trained model directly will lead to a
`DeserializationError`.

```
# Do not return a model trained on GPUs to a CPU-only environment as follows

@remote(instance_type='`ml.g4dn.xlarge`')
def train(...):
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu") # a device without GPU capabilities

    model = Net().to(device)

    # train the model
    ...

    return model

model = train(...) #returns a DeserializationError if run on a device with GPU
```

To return a model trained in a GPU environment to one that
contains only CPU capabilities, use the PyTorch model I/O APIs
directly as shown in the code example below.

```
import s3fs

model_path = "`s3://amzn-s3-demo-bucket/folder/`"

@remote(instance_type='`ml.g4dn.xlarge`')
def train(...):
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    model = Net().to(device)

    # train the model
    ...

    fs = s3fs.FileSystem()
    with fs.open(os.path.join(model_path, 'model.pt'), 'wb') as file:
        torch.save(model.state_dict(), file) #this writes the model in a device-agnostic way (CPU vs GPU)

train(...) #use the model to train on either CPUs or GPUs

model = Net()
fs = s3fs.FileSystem()with fs.open(os.path.join(model_path, 'model.pt'), 'rb') as file:
    model.load_state_dict(torch.load(file, map_location=torch.device('cpu')))
```

#### Where SageMaker AI stores your serialized data

When you invoke a remote function, SageMaker AI automatically serializes your
function arguments and return values during the input and output stages.
This serialized data is stored under a root directory in your S3 bucket. You
specify the root directory, `<s3_root_uri>`, in a
configuration file. The parameter `job_name` is automatically
generated for you.

Under the root directory, SageMaker AI creates a `<job_name>`
folder, which holds your current work directory, serialized function, the
arguments for your serialized function, results and any exceptions that
arose from invoking the serialized function.

Under `<job_name>`, the directory `workdir`
contains a zipped archive of your current working directory. The zipped
archive includes any Python files in your working directory and the
`requirements.txt` file, which specifies any dependencies
needed to run your remote function.

The following is an example of the folder structure under an S3 bucket
that you specify in your configuration file.

```
`<s3_root_uri>`/ # specified by s3_root_uri or S3RootUri
    <job_name>/ #automatically generated for you
        workdir/workspace.zip # archive of the current working directory (workdir)
        function/ # serialized function
        arguments/ # serialized function arguments
        results/ # returned output from the serialized function including the model
        exception/ # any exceptions from invoking the serialized function
```

The root directory that you specify in your S3 bucket is not meant for
long term storage. The serialized data are tightly tied to the Python
version and machine learning (ML) framework version that were used during
serialization. If you upgrade the Python version or ML framework, you may
not be able to use your serialized data. Instead, do the following.

- Store your model and model artifacts in a format that is agnostic
  to your Python version and ML framework.
- If you upgrade your Python or ML framework, access your model
  results from your long-term storage.

###### Important

To delete your serialized data after a specified amount of time, set a
[lifetime configuration](../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md "../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md") on your S3 bucket.

###### Note

Files that are serialized with the Python [pickle](https://docs.python.org/3/library/pickle.html "https://docs.python.org/3/library/pickle.html")
module can be less portable than other data formats including CSV,
Parquet and JSON. Be wary of loading pickled files from unknown
sources.

For more information about what to include in a configuration file for a
remote function, see [Configuration File](train-remote-decorator-config.md "train-remote-decorator-config.md").

#### Access to your serialized data

Administrators can provide settings for your serialized data, including
its location and any encryption settings in a configuration file. By
default, the serialized data are encrypted with an AWS Key Management Service (AWS KMS) Key.
Administrators can also restrict access to the root directory that you
specify in your configuration file with a [bucket
policy](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md"). The configuration file can be shared and used across
projects and jobs. For more information, see [Configuration File](train-remote-decorator-config.md "train-remote-decorator-config.md").

## Use the

`RemoteExecutor` API to invoke a function

You can use the `RemoteExecutor` API to invoke a function. SageMaker AI Python
SDK will transform the code inside the `RemoteExecutor` call into a SageMaker AI
training job. The training job will then invoke the function as an asynchronous
operation and return a future. If you use the `RemoteExecutor` API, you
can run more than one training job in parallel. For more information about futures
in Python, see [Futures](https://docs.python.org/3/library/asyncio-future.html "https://docs.python.org/3/library/asyncio-future.html").

The following code example shows how to import the required libraries, define a
function, start a SageMaker AI instance, and use the API to submit a request to run
`2` jobs in parallel.

```
from sagemaker.remote_function import RemoteExecutor

def matrix_multiply(a, b):
    return np.matmul(a, b)


a = np.array([[1, 0],
             [0, 1]])
b = np.array([1, 2])

with RemoteExecutor(max_parallel_job=2, instance_type="`ml.m5.large`") as e:
    future = e.submit(matrix_multiply, a, b)

assert (future.result() == np.array([1,2])).all()
```

The `RemoteExecutor` class is an implementation of the [concurrent.futures.Executor](https://docs.python.org/3/library/concurrent.futures.html "https://docs.python.org/3/library/concurrent.futures.html") library.

The following code example shows how to define a function and call it using the
`RemoteExecutorAPI`. In this example, the `RemoteExecutor`
will submit `4` jobs in total, but only `2` in parallel. The
last two jobs will reuse the clusters with minimal overhead.

```
from sagemaker.remote_function.client import RemoteExecutor

def divide(a, b):
    return a/b

with RemoteExecutor(max_parallel_job=2, keep_alive_period_in_seconds=60) as e:
    futures = [e.submit(divide, a, 2) for a in [3, 5, 7, 9]]

for future in futures:
    print(future.result())
```

The `max_parallel_job` parameter only serves as a rate limiting
mechanism without optimizing compute resource allocation. In the previous code
example, `RemoteExecutor` doesn’t reserve compute resources for the two
parallel jobs before any jobs are submitted. For more information about
`max_parallel_job` or other parameters for the @remote decorator, see
[Remote function classes and methods specification](https://sagemaker.readthedocs.io/en/stable/remote_function/sagemaker.remote_function.html "https://sagemaker.readthedocs.io/en/stable/remote_function/sagemaker.remote_function.html").

### Future class for

the `RemoteExecutor` API

A future class is a public class that represents the return function from the
training job when it is invoked asynchronously. The future class implements the
[concurrent.futures.Future](https://docs.python.org/3/library/concurrent.futures.html "https://docs.python.org/3/library/concurrent.futures.html") class. This class can be used to do
operations on the underlying job and load data into memory.
