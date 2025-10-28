# Input and Output interface for the CatBoost

algorithm

Gradient boosting operates on tabular data, with the rows representing observations,
one column representing the target variable or label, and the remaining columns
representing features.

The SageMaker AI implementation of CatBoost supports CSV for training and inference:

- For **Training ContentType**, valid inputs must be
  _text/csv_.
- For **Inference ContentType**, valid inputs must be
  _text/csv_.

###### Note

For CSV training, the algorithm assumes that the target variable is in the first
column and that the CSV does not have a header record.

For CSV inference, the algorithm assumes that CSV input does not have the label
column.

**Input format for training data, validation data, and categorical
features**

Be mindful of how to format your training data for input to the CatBoost model. You
must provide the path to an Amazon S3 bucket that contains your training and validation data.
You can also include a list of categorical features. Use both the `training`
and `validation` channels to provide your input data. Alternatively, you can
use only the `training` channel.

**Use both the `training` and `validation`
channels**

You can provide your input data by way of two S3 paths, one for the
`training` channel and one for the `validation` channel. Each
S3 path can either be an S3 prefix that points to one or more CSV files or a full S3
path pointing to one specific CSV file. The target variables should be in the first
column of your CSV file. The predictor variables (features) should be in the remaining
columns. If multiple CSV files are provided for the `training` or
`validation` channels, the CatBoost algorithm concatenates the files.
The validation data is used to compute a validation score at the end of each boosting
iteration. Early stopping is applied when the validation score stops improving.

If your predictors include categorical features, you can provide a JSON file named
`categorical_index.json` in the same location as your training data file
or files. If you provide a JSON file for categorical features, your
`training` channel must point to an S3 prefix and not a specific CSV
file. This file should contain a Python dictionary where the key is the string
`"cat_index_list"` and the value is a list of unique integers. Each
integer in the value list should indicate the column index of the corresponding
categorical features in your training data CSV file. Each value should be a positive
integer (greater than zero because zero represents the target value), less than the
`Int32.MaxValue` (2147483647), and less than the total number of columns.
There should only be one categorical index JSON file.

**Use only the `training` channel**:

You can alternatively provide your input data by way of a single S3 path for the
`training` channel. This S3 path should point to a directory with a
subdirectory named `training/` that contains one or more CSV files. You can
optionally include another subdirectory in the same location called
`validation/` that also has one or more CSV files. If the validation data
is not provided, then 20% of your training data is randomly sampled to serve as the
validation data. If your predictors include categorical features, you can provide a JSON
file named `categorical_index.json` in the same location as your data
subdirectories.

###### Note

For CSV training input mode, the total memory available to the algorithm (instance
count multiplied by the memory available in the `InstanceType`) must be
able to hold the training dataset.

SageMaker AI CatBoost uses the `catboost.CatBoostClassifier` and
`catboost.CatBoostRegressor` modules to serialize or deserialize the
model, which can be used for saving or loading the model.

###### To use a model trained with SageMaker AI CatBoost with `catboost`

- Use the following Python code:

```
import tarfile
from catboost import CatBoostClassifier

t = tarfile.open('model.tar.gz', 'r:gz')
t.extractall()

file_path = os.path.join(model_file_path, "model")
model = CatBoostClassifier()
model.load_model(file_path)

# prediction with test data
# dtest should be a pandas DataFrame with column names feature_0, feature_1, ..., feature_d
pred = model.predict(`dtest`)
```
