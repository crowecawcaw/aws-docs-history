# Apply SageMaker smart sifting to

your PyTorch script

These instructions demonstrate how to enable SageMaker smart sifting with your training
script.

1. Configure the SageMaker smart sifting interface.

The SageMaker smart sifting library implements a relative-threshold loss-based
sampling technique that helps filter out samples with lower impact on
reducing the loss value. The SageMaker smart sifting algorithm calculates the loss value
of every input data sample using a forward pass, and calculates its relative
percentile against the loss values of preceding data.

The following two parameters are what you need to specify to the
`RelativeProbabilisticSiftConfig` class for creating a
sifting configuration object.

    * Specify the proportion of data that should be used for training to
     the `beta_value` parameter.
    * Specify the number of samples used in the comparison with the
     `loss_history_length` parameter.

The following code example demonstrates setting up an object of the
`RelativeProbabilisticSiftConfig` class.

```
from smart_sifting.sift_config.sift_configs import (
    RelativeProbabilisticSiftConfig
    LossConfig
    SiftingBaseConfig
)

sift_config=RelativeProbabilisticSiftConfig(
    beta_value=0.5,
    loss_history_length=500,
    loss_based_sift_config=LossConfig(
         sift_config=SiftingBaseConfig(sift_delay=0)
    )
)
```

For more information about the `loss_based_sift_config`
parameter and related classes, see [SageMaker smart sifting
configuration modules](train-smart-sifting-pysdk-reference.md#train-smart-sifting-pysdk-base-config-modules "train-smart-sifting-pysdk-reference.md#train-smart-sifting-pysdk-base-config-modules") in the
SageMaker smart sifting Python SDK reference section.

The `sift_config` object in the preceding code example is used
in step 4 for setting up the `SiftingDataloader` class. 2. (Optional) Configure a SageMaker smart sifting batch transform class.

Different training use cases require different training data formats.
Given the variety of data formats, the SageMaker smart sifting algorithm needs to
identify how to perform sifting on a particular batch. To address this,
SageMaker smart sifting provides a batch transform module that helps convert batches
into standardized formats that it can efficiently sift.

    1. SageMaker smart sifting handles batch transform of training data in the
     following formats: Python lists, dictionaries, tuples, and tensors.
     For these data formats, SageMaker smart sifting automatically handles the batch
     data format conversion, and you can skip the rest of this step. If
     you skip this step, in step 4 for configuring
     `SiftingDataloader`, leave the
     `batch_transforms` parameter of
     `SiftingDataloader` to its default value, which is
     `None`.
    2. If your dataset is not in these format, you should proceed to the
     rest of this step to create a custom batch transform using
     `SiftingBatchTransform`.


    In cases in which your dataset isn’t in one of the supported
     formats by SageMaker smart sifting, you might run into errors. Such data format
     errors can be resolved by adding the `batch_format_index`
     or `batch_transforms` parameter to the
     `SiftingDataloader` class, which you set up in step
     4. The following shows example errors due to an incompatible data
     format and resolutions for them.




    | Error Message | Resolution |
    | --- | --- |
    | Batches of type<br>`{type(batch)}` are not<br>supported by default. | This error indicates the batch format is not<br>supported by default. You should implement a custom<br>batch transform class, and use this by specifying it<br>to the `batch_transforms` parameter of<br>the `SiftingDataloader` class. |
    | Unable to index the batch of type<br>`{type(batch)}` | This error indicates the batch object cannot be<br>indexed normally. User must implement a custom batch<br>transform and pass this using the<br>`batch_transforms` parameter. |
    | Batch size<br>`{batch_size}` does not<br>match dimension 0 or dimension 1 sizes | This error occurs when the provided batch size<br>does not match the 0th or 1st dimensions of the<br>batch. User must implement a custom batch transform<br>and pass this using the<br>`batch_transforms` parameter. |
    | Both dimension 0 and dimension 1 match batch<br>size | This error indicates that since multiple<br>dimensions match the provided batch size, more<br>information is required to sift the batch. The user<br>can provide the `batch_format_index`<br>parameter to indicate if the batch is indexable by<br>sample or feature. Users may also implement a custom<br>batch transform, but this is more work than<br>required. |


    To resolve the aforementioned issues, you need to create a custom
     batch transform class using the `SiftingBatchTransform`
     module. A batch transform class should consist of a pair of
     transform and reverse-transform functions. The function pair
     converts your data format to a format that SageMaker smart sifting algorithm can
     process. After you create a batch transform class, the class returns
     a `SiftingBatch` object that you'll pass to the
     `SiftingDataloader` class in step 4.


    The following are examples of custom batch transform classes of
     the `SiftingBatchTransform` module.




    	* An example of a custom list batch transform implementation
    	 with SageMaker smart sifting for cases where the dataloader chunk has
    	 inputs, masks, and labels.



    	```
    	from typing import Any

    	import torch

    	from smart_sifting.data_model.data_model_interface import SiftingBatchTransform
    	from smart_sifting.data_model.list_batch import ListBatch

    	class `ListBatchTransform`(SiftingBatchTransform):
    	    def transform(self, batch: Any):
    	        inputs = batch[0].tolist()
    	        labels = batch[-1].tolist()  # assume the last one is the list of labels
    	        return ListBatch(inputs, labels)

    	    def reverse_transform(self, list_batch: ListBatch):
    	        a_batch = [torch.tensor(list_batch.inputs), torch.tensor(list_batch.labels)]
    	        return a_batch
    	```
    	* An example of a custom list batch transform implementation
    	 with SageMaker smart sifting for cases where no labels are needed for
    	 reverse transformation.



    	```
    	class `ListBatchTransformNoLabels`(SiftingBatchTransform):
    	    def transform(self, batch: Any):
    	        return ListBatch(batch[0].tolist())

    	    def reverse_transform(self, list_batch: ListBatch):
    	        a_batch = [torch.tensor(list_batch.inputs)]
    	        return a_batch
    	```
    	* An example of a custom tensor batch implementation with
    	 SageMaker smart sifting for cases where the data loader chunk has
    	 inputs, masks, and labels.



    	```
    	from typing import Any

    	from smart_sifting.data_model.data_model_interface import SiftingBatchTransform
    	from smart_sifting.data_model.tensor_batch import TensorBatch

    	class `TensorBatchTransform`(SiftingBatchTransform):
    	    def transform(self, batch: Any):
    	        a_tensor_batch = TensorBatch(
    	            batch[0], batch[-1]
    	        )  # assume the last one is the list of labels
    	        return a_tensor_batch

    	    def reverse_transform(self, tensor_batch: TensorBatch):
    	        a_batch = [tensor_batch.inputs, tensor_batch.labels]
    	        return a_batch
    	```
    After you create a `SiftingBatchTransform`-implemted
     batch transform class, you use this class in step 4 for setting up
     the `SiftingDataloader` class. The rest of this guide
     assumes that a `ListBatchTransform` class is created. In
     step 4, this class is passed to the
     `batch_transforms`.

3. Create a class for implementing the SageMaker smart sifting `Loss`
   interface. This tutorial assumes that the class is named
   `SiftingImplementedLoss`. While setting up this class, we
   recommend that you use the same loss function in the model training loop. Go
   through the following substeps for creating a SageMaker smart sifting `Loss`
   implemented class.
   1. SageMaker smart sifting calculates a loss value for each training data sample,
      as opposed to calculating a single loss value for a batch. To ensure
      that SageMaker smart sifting uses the same loss calculation logic, create a
      smart-sifting-implemented loss function using the SageMaker smart sifting
      `Loss` module that uses your loss function and
      calculates loss per training sample.

   ###### Tip

   SageMaker smart sifting algorithm runs on every data sample, not on the
   entire batch, so you should add an initialization function to
   set the PyTorch loss function without any reduction
   strategy.

   ```
   class `SiftingImplementedLoss`(Loss):
       def __init__(self):
           self.loss = `torch.nn.CrossEntropyLoss`(**reduction='none'**)
   ```

   This is also shown in the following code example. 2. Define a loss function that accepts the
   `original_batch` (or `transformed_batch`
   if you have set up a batch transform in step 2) and the PyTorch
   model. Using the specified loss function with no reduction,
   SageMaker smart sifting runs a forward pass for each data sample to evaluate its
   loss value.The following code is an example of a smart-sifting-implemented
   `Loss` interface named
   `SiftingImplementedLoss`.

```
from typing import Any

import torch
import torch.nn as nn
from torch import Tensor

from smart_sifting.data_model.data_model_interface import SiftingBatch
from smart_sifting.loss.abstract_sift_loss_module import Loss

model=... # a PyTorch model based on torch.nn.Module

class `SiftingImplementedLoss`(Loss):
    # You should add the following initializaztion function
    # to calculate loss per sample, not per batch.
    def __init__(self):
        self.`loss_no_reduction` = `torch.nn.CrossEntropyLoss`(**reduction='none'**)

    def loss(
        self,
        model: torch.nn.Module,
        transformed_batch: SiftingBatch,
        original_batch: Any = None,
    ) -> torch.Tensor:
        device = next(model.parameters()).device
        batch = [t.to(device) for t in original_batch] # use this if you use original batch and skipped step 2
        # batch = [t.to(device) for t in transformed_batch] # use this if you transformed batches in step 2

        # compute loss
        outputs = model(batch)
        return self.`loss_no_reduction`(outputs.logits, batch[2])
```

Before the training loop hits the actual forward pass, this sifting loss
calculation is done during the data loading phase of fetching a batch in
each iteration. The individual loss value is then compared to previous loss
values, and its relative percentile is estimated per the object of
`RelativeProbabilisticSiftConfig` you have set up in step

1.
2. Wrap the PyTroch data loader by the SageMaker AI `SiftingDataloader`
   class.

Finally, use all the SageMaker smart sifting implemented classes you configured in the
previous steps to the SageMaker AI `SiftingDataloder` configuration
class. This class is a wrapper for PyTorch [`DataLoader`](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader"). By wrapping PyTorch
`DataLoader`, SageMaker smart sifting is registered to run as part of
data loading in each iteration of a PyTorch training job. The following code
example demonstrates implementing SageMaker AI data sifting to a PyTorch
`DataLoader`.

```
from smart_sifting.dataloader.sift_dataloader import SiftingDataloader
from torch.utils.data import DataLoader

train_dataloader = DataLoader(...) # PyTorch data loader

# Wrap the PyTorch data loader by SiftingDataloder
train_dataloader = SiftingDataloader(
    sift_config=`sift_config`, # config object of RelativeProbabilisticSiftConfig
    orig_dataloader=`train_dataloader`,
    batch_transforms=`ListBatchTransform`(), # Optional, this is the custom class from step 2
    loss_impl=`SiftingImplementedLoss`(), # PyTorch loss function wrapped by the Sifting Loss interface
    model=`model`,
    log_batch_data=`False`
)
```
