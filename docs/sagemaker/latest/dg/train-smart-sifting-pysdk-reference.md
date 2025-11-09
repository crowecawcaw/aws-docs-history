# SageMaker smart sifting Python SDK

reference

This page provides a reference of Python modules you need for applying SageMaker smart sifting to
your training script.

## SageMaker smart sifting

configuration modules

**`*class*
 smart_sifting.sift_config.sift_configs.RelativeProbabilisticSiftConfig()`**

The SageMaker smart sifting configuration class.

**Parameters**

- `beta_value` (float) – A beta (constant) value. It is
  used to calculate the probability of selecting a sample for training based
  on the percentile of the loss in the loss values history. Lowering the beta
  value results in a lower percentage of data sifted, and raising it results
  in a higher percentage of data sifted. There’s no minimum or maximum value
  for the beta value, other than it must be a positive value. The following
  reference table gives information for sifting rates with respect to
  `beta_value`.

| `beta_value` | Proportion of data kept (%) | Proportion of data sifted out (%) |
| ------------ | --------------------------- | --------------------------------- |
| 0.1          | 90.91                       | 9.01                              |
| 0.25         | 80                          | 20                                |
| 0.5          | 66.67                       | 33.33                             |
| 1            | 50                          | 50                                |
| 2            | 33.33                       | 66.67                             |
| 3            | 25                          | 75                                |
| 10           | 9.09                        | 90.92                             |
| 100          | 0.99                        | 99.01                             |

- `loss_history_length` (int) – The number of previous
  training losses to store for the relative threshold loss based
  sampling.
- `loss_based_sift_config` (dict or a `LossConfig`
  object) – Specify a `LossConfig` object that returns the
  SageMaker smart sifting Loss interface configuration.

**`*class*
 smart_sifting.sift_config.sift_configs.LossConfig()`**

The configuration class for the `loss_based_sift_config` parameter of
the `RelativeProbabilisticSiftConfig` class.

**Parameters**

- `sift_config` (dict or a `SiftingBaseConfig` object)
  – Specify a `SiftingBaseConfig` object that returns a
  sifting base configuration dictionary.

**`*class*
 smart_sifting.sift_config.sift_configs.SiftingBaseConfig()`**

The configuration class for the `sift_config` parameter of
`LossConfig`.

**Parameters**

- `sift_delay` (int) – The number of training steps to
  wait for before starting sifting. We recommend that you start sifting after
  all the layers in the model have enough view of the training data. The
  default value is `1000`.
- `repeat_delay_per_epoch` (bool) – Specify whether to
  delay sifting every epoch. The default value is `False`.

## SageMaker smart sifting data

batch transform modules

`*class*
 smart_sifting.data_model.data_model_interface.SiftingBatchTransform`

A SageMaker smart sifting Python module for defining how to perform batch transform. Using
this, you can set up a batch transform class that converts the data format of your
training data to `SiftingBatch` format. SageMaker smart sifting can sift and
accumulate data in this format into a sifted batch.

`*class*
 smart_sifting.data_model.data_model_interface.SiftingBatch`

An interface to define a batch data type that can be sifted and
accumulated.

`*class*
 smart_sifting.data_model.list_batch.ListBatch`

A module for keeping track of a list batch for sifting.

`*class*
 smart_sifting.data_model.tensor_batch.TensorBatch`

A module for keeping track of a tensor batch for sifting.

## SageMaker smart sifting loss

implementation module

`*class*
 smart_sifting.loss.abstract_sift_loss_module.Loss`

A wrapper module for registering the SageMaker smart sifting interface to the loss function of
a PyTorch-based model.

## SageMaker smart sifting

data loader wrapper module

`*class*
 smart_sifting.dataloader.sift_dataloader.SiftingDataloader`

A wrapper module for registering the SageMaker smart sifting interface to the data loader of a
PyTorch-based model.

The Main Sifting Dataloader iterator sifts out training samples from a dataloader
based on a sift configuration.

**Parameters**

- `sift_config` (dict or a
  `RelativeProbabilisticSiftConfig` object) – A
  `RelativeProbabilisticSiftConfig` object.
- `orig_dataloader` (a PyTorch DataLoader object) –
  Specify the PyTorch Dataloader object to be wrapped.
- `batch_transforms` (a `SiftingBatchTransform`
  object) – (Optional) If your data format is not supported by the
  SageMaker smart sifting library’s default transform, you must create a batch transform
  class using the `SiftingBatchTransform` module. This parameter is
  used to pass the batch transform class. This class is used for
  `SiftingDataloader` to convert the data into a format that
  the SageMaker smart sifting algorithm can accept.
- `model` (a PyTorch model object) – The original PyTorch
  model
- `loss_impl` (a sifting loss function of
  `smart_sifting.loss.abstract_sift_loss_module.Loss`) –
  A sifting loss function that is configured with the `Loss` module
  and wraps the PyTorch loss function.
- `log_batch_data` (bool) – Specify whether to log batch
  data. If set to `True`, SageMaker smart sifting logs the details of the
  batches that are kept or sifted. We recommend that you turn it on only for a
  pilot training job. When logging is on, the samples are loaded to GPU and
  transferred to CPU, which introduces overhead. The default value is
  `False`.
