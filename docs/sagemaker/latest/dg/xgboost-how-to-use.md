# How to use SageMaker AI XGBoost

With SageMaker AI, you can use XGBoost as a built-in algorithm or framework. When XGBoost as a
framework, you have more flexibility and access to more advanced scenarios because you
can customize your own training scripts. The following sections describe how to use
XGBoost with the SageMaker Python SDK, and the input/output interface for the XGBoost
algorithm. For information on how to use XGBoost from the Amazon SageMaker Studio Classic UI, see [SageMaker JumpStart pretrained models](studio-jumpstart.md "studio-jumpstart.md").

###### Topics

- [Use XGBoost as a framework](#xgboost-how-to-framework "#xgboost-how-to-framework")
- [Use XGBoost as a built-in algorithm](#xgboost-how-to-built-in "#xgboost-how-to-built-in")
- [Input/Output interface for the XGBoost
  algorithm](#InputOutput-XGBoost "#InputOutput-XGBoost")

## Use XGBoost as a framework

Use XGBoost as a framework to run your customized training scripts that can
incorporate additional data processing into your training jobs. In the following
code example, SageMaker Python SDK provides the XGBoost API as a framework. This
functions similarly to how SageMaker AI provides other framework APIs, such as
TensorFlow, MXNet, and PyTorch.

```
import boto3
import sagemaker
from sagemaker.xgboost.estimator import XGBoost
from sagemaker.session import Session
from sagemaker.inputs import TrainingInput

# initialize hyperparameters
hyperparameters = {
        "max_depth":"5",
        "eta":"0.2",
        "gamma":"4",
        "min_child_weight":"6",
        "subsample":"0.7",
        "verbosity":"1",
        "objective":"reg:squarederror",
        "num_round":"50"}

# set an output path where the trained model will be saved
bucket = sagemaker.Session().default_bucket()
prefix = 'DEMO-xgboost-as-a-framework'
output_path = 's3://{}/{}/{}/output'.format(bucket, prefix, 'abalone-xgb-framework')

# construct a SageMaker AI XGBoost estimator
# specify the entry_point to your xgboost training script
estimator = XGBoost(entry_point = "`your_xgboost_abalone_script.py`",
                    framework_version='`1.7-1`',
                    hyperparameters=hyperparameters,
                    role=sagemaker.get_execution_role(),
                    instance_count=1,
                    instance_type='ml.m5.2xlarge',
                    output_path=output_path)

# define the data type and paths to the training and validation datasets
content_type = "libsvm"
train_input = TrainingInput("s3://{}/{}/{}/".format(bucket, prefix, 'train'), content_type=content_type)
validation_input = TrainingInput("s3://{}/{}/{}/".format(bucket, prefix, 'validation'), content_type=content_type)

# execute the XGBoost training job
estimator.fit({'train': train_input, 'validation': validation_input})
```

For an end-to-end example of using SageMaker AI XGBoost as a framework, see [Regression with Amazon SageMaker AI XGBoost](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_abalone_dist_script_mode.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_abalone_dist_script_mode.html").

## Use XGBoost as a built-in algorithm

Use the XGBoost built-in algorithm to build an XGBoost training container as
shown in the following code example. You can automatically spot the XGBoost
built-in algorithm image URI using the SageMaker AI `image_uris.retrieve`
API. If using [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") version 1, use the `get_image_uri`
API. To make sure that the `image_uris.retrieve` API finds the
correct URI, see [Common
parameters for built-in algorithms](sagemaker-algo-docker-registry-paths.md "sagemaker-algo-docker-registry-paths.md"). Then look up
`xgboost` from the full list of built-in algorithm image URIs and
available regions.

After specifying the XGBoost image URI, use the XGBoost container to construct
an estimator using the SageMaker AI Estimator API and initiate a training job. This
XGBoost built-in algorithm mode does not incorporate your own XGBoost training
script and runs directly on the input datasets.

###### Important

When you retrieve the SageMaker AI XGBoost image URI, do not use
`:latest` or `:1` for the image URI tag. You must
specify one of the [Supported versions](xgboost.md#xgboost-supported-versions "xgboost.md#xgboost-supported-versions") to choose the SageMaker AI-managed
XGBoost container with the native XGBoost package version that you want to
use. To find the package version migrated into the SageMaker AI XGBoost containers,
see [Docker Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md"). Then choose your
AWS Region, and navigate to the **XGBoost
(algorithm)** section.

```
import sagemaker
import boto3
from sagemaker import image_uris
from sagemaker.session import Session
from sagemaker.inputs import TrainingInput

# initialize hyperparameters
hyperparameters = {
        "max_depth":"5",
        "eta":"0.2",
        "gamma":"4",
        "min_child_weight":"6",
        "subsample":"0.7",
        "objective":"reg:squarederror",
        "num_round":"50"}

# set an output path where the trained model will be saved
bucket = sagemaker.Session().default_bucket()
prefix = 'DEMO-xgboost-as-a-built-in-algo'
output_path = 's3://{}/{}/{}/output'.format(bucket, prefix, 'abalone-xgb-built-in-algo')

# this line automatically looks for the XGBoost image URI and builds an XGBoost container.
# specify the repo_version depending on your preference.
xgboost_container = sagemaker.image_uris.retrieve("xgboost", region, "`1.7-1`")

# construct a SageMaker AI estimator that calls the xgboost-container
estimator = sagemaker.estimator.Estimator(image_uri=xgboost_container,
                                          hyperparameters=hyperparameters,
                                          role=sagemaker.get_execution_role(),
                                          instance_count=1,
                                          instance_type='ml.m5.2xlarge',
                                          volume_size=5, # 5 GB
                                          output_path=output_path)

# define the data type and paths to the training and validation datasets
content_type = "libsvm"
train_input = TrainingInput("s3://{}/{}/{}/".format(bucket, prefix, 'train'), content_type=content_type)
validation_input = TrainingInput("s3://{}/{}/{}/".format(bucket, prefix, 'validation'), content_type=content_type)

# execute the XGBoost training job
estimator.fit({'train': train_input, 'validation': validation_input})
```

For more information about how to set up the XGBoost as a built-in algorithm,
see the following notebook examples.

- [Managed Spot Training for XGBoost](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_managed_spot_training.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_managed_spot_training.html")
- [Regression with Amazon SageMaker AI XGBoost (Parquet input)](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_parquet_input_training.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_parquet_input_training.html")

## Input/Output interface for the XGBoost

algorithm

Gradient boosting operates on tabular data, with the rows representing
observations, one column representing the target variable or label, and the
remaining columns representing features.

The SageMaker AI implementation of XGBoost supports the following data formats for
training and inference:

- _text/libsvm_ (default)
- _text/csv_
- _application/x-parquet_
- _application/x-recordio-protobuf_

###### Note

There are a few considerations to be aware of regarding training and inference
input:

- For increased performance, we recommend using XGBoost with _File mode_, in which your data from Amazon S3 is
  stored on the training instance volumes.
- For training with columnar input, the algorithm assumes that the
  target variable (label) is the first column. For inference, the
  algorithm assumes that the input has no label column.
- For CSV data, the input should not have a header record.
- For LIBSVM training, the algorithm assumes that subsequent columns
  after the label column contain the zero-based index value pairs for
  features. So each row has the format: : <label>
  <index0>:<value0> <index1>:<value1>.
- For information on instance types and distributed training, see [EC2 instance recommendation for the XGBoost
  algorithm](xgboost.md#Instance-XGBoost "xgboost.md#Instance-XGBoost").

For CSV training input mode, the total memory available to the algorithm must be
able to hold the training dataset. The total memory available is calculated as
`Instance Count * the memory available in the InstanceType`. For libsvm
training input mode, it's not required, but we recommend it.

For v1.3-1 and later, SageMaker AI XGBoost saves the model in the XGBoost internal binary
format, using `Booster.save_model`. Previous versions use the Python
pickle module to serialize/deserialize the model.

###### Note

Be mindful of versions when using an SageMaker AI XGBoost model in open source
XGBoost. Versions 1.3-1 and later use the XGBoost internal binary format while
previous versions use the Python pickle module.

###### To use a model trained with SageMaker AI XGBoost v1.3-1 or later in open source

XGBoost

- Use the following Python code:

```
import xgboost as xgb

xgb_model = xgb.Booster()
xgb_model.load_model(`model_file_path`)
xgb_model.predict(`dtest`)
```

###### To use a model trained with previous versions of SageMaker AI XGBoost in open source

XGBoost

- Use the following Python code:

```
import pickle as pkl
import tarfile

t = tarfile.open('model.tar.gz', 'r:gz')
t.extractall()

model = pkl.load(open(`model_file_path`, 'rb'))

# prediction with test data
pred = model.predict(`dtest`)
```

###### To differentiate the importance of labelled data points use Instance Weight

Supports

- SageMaker AI XGBoost allows customers to differentiate the importance of labelled
  data points by assigning each instance a weight value. For
  _text/libsvm_ input, customers can assign weight values
  to data instances by attaching them after the labels. For example,
  `label:weight idx_0:val_0 idx_1:val_1...`. For
  _text/csv_ input, customers need to turn on the
  `csv_weights` flag in the parameters and attach weight values in
  the column after labels. For example:
  `label,weight,val_0,val_1,...`).
