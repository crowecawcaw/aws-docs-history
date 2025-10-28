# Apply SageMaker smart sifting to your Hugging Face Transformers script

There are two ways to implement the SageMaker smart sifting into the Transformers
`Trainer` class.

###### Note

If you use one of the DLCs for PyTorch with the SageMaker smart sifting package installed,
note that you need to install the `transformers` library. You can
install additional packages by [extending the DLCs](prebuilt-containers-extend.md "prebuilt-containers-extend.md") or passing `requirements.txt` to the
training job launcher class for PyTorch ([`sagemaker.pytorch.PyTorch`](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html")) in the SageMaker AI Python
SDK.

## Simple setup

The simplest way to implement SageMaker smart sifting into the Transformers
`Trainer` class is to use the `enable_sifting`
function. This function accepts an existing `Trainer` object, and
wraps the existing `DataLoader` object with
`SiftingDataloader`. You can continue using the same training
object. See the following example usage.

```
from smart_sifting.integrations.trainer import enable_sifting
from smart_sifting.loss.abstract_sift_loss_module import Loss
from smart_sifting.sift_config.sift_configs import (
    RelativeProbabilisticSiftConfig
    LossConfig
    SiftingBaseConfig
)

class `SiftingImplementedLoss`(Loss):
   def loss(self, model, transformed_batch, original_batch):
        loss_fct = MSELoss(reduction="none") # make sure to set reduction to "none"
        logits = model.bert(**original_batch)
        return loss_fct(logits, original_batch.get("labels"))

sift_config = RelativeProbabilisticSiftConfig(
    beta_value=`0.5`,
    loss_history_length=`500`,
    loss_based_sift_config=LossConfig(
         sift_config=SiftingBaseConfig(sift_delay=0)
    )
)

trainer = Trainer(...)
enable_sifting(trainer, `sift_config`, loss=`SiftingImplementedLoss`()) # updates the trainer with Sifting Loss and config
trainer.train()
```

The `SiftingDataloader` class is an iterable data loader. The exact
size of the resulting dataset is not known beforehand due to the random sampling
during sifting. As a result, the Hugging Face `Trainer` expects the
[`max_steps` training argument](https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments.max_steps "https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments.max_steps"). Note that this
argument overrides the epoch configuration parameter
`num_train_epochs`. If your original data loader was also
iterable, or your training uses `max_steps` and a single epoch, then
the `SiftingDataloader` performs the same as the existing dataloader.
If the original dataloader was not iterable or `max_steps` was not
provided, the Hugging Face Trainer might throw an error message similar to the
following.

```
args.max_steps must be set to a positive value if dataloader does not have a length,
was -1
```

To address this, the `enable_sifting` function provides an optional
`set_epochs` parameter. This enables training with epochs, using
the number of epochs provided by [num_train_epochs argument](https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments.num_train_epochs(float, "https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments.num_train_epochs(float,") of the `Trainer` class, and
sets `max_steps` to the maximum system integer, allowing training to
progress until the specified epochs have completed.

## Custom setup

For a custom integration of the SageMaker smart sifting dataloader, you can utilize a
custom Hugging Face `Trainer` class. Within any subclass of
`Trainer`, the `get_train_dataloader()` function can
be overridden to return an object of the `SiftingDataloader` class
instead. For cases with existing custom trainers, this approach might be less
intrusive but requires code changes than the simple setup option. The following
is an example implementation of SageMaker smart sifting into a custom Hugging Face
`Trainer` class.

```
from smart_sifting.sift_config.sift_configs import (
    RelativeProbabilisticSiftConfig
    LossConfig
    SiftingBaseConfig
)
from smart_sifting.dataloader.sift_dataloader import SiftingDataloader
from smart_sifting.loss.abstract_sift_loss_module import Loss
from smart_sifting.data_model.data_model_interface import SiftingBatch, SiftingBatchTransform
from smart_sifting.data_model.list_batch import ListBatch

class `SiftingListBatchTransform`(SiftingBatchTransform):
    def transform(self, batch: Any):
        inputs = batch[0].tolist()
        labels = batch[-1].tolist()  # assume the last one is the list of labels
        return ListBatch(inputs, labels)

    def reverse_transform(self, list_batch: ListBatch):
        a_batch = [torch.tensor(list_batch.inputs), torch.tensor(list_batch.labels)]
        return a_batch

class `SiftingImplementedLoss`():
    # You should add the following initializaztion function
    # to calculate loss per sample, not per batch.
    def __init__(self):
        self.celoss = torch.nn.`CrossEntropyLoss`(reduction='none')

    def loss(
        self,
        model: torch.nn.Module,
        transformed_batch: SiftingBatch,
        original_batch: Any = None,
    ) -> torch.Tensor:
        device = next(model.parameters()).device
        batch = [t.to(device) for t in original_batch]

        # compute loss
        outputs = model(batch)
        return self.celoss(outputs.logits, batch[2])

class `SiftingImplementedTrainer`(Trainer):
    def get_train_dataloader(self):
        `dl` = super().get_train_dataloader()

        sift_config = RelativeProbabilisticSiftConfig(
            beta_value=`0.5`,
            loss_history_length=`500`,
            loss_based_sift_config=LossConfig(
                sift_config=SiftingBaseConfig(sift_delay=0)
            )
        )

        return SiftingDataloader(
                sift_config=sift_config,
                orig_dataloader=`dl`,
                batch_transforms=`SiftingListBatchTransform`(),
                loss_impl=`SiftingImplementedLoss`(),
                model=self.model
        )
```

Using the wrapped `Trainer` class, create an object of it as
follows.

```
trainer = `SiftingImplementedTrainer`(
    model=`model`,
    args=`training_args`,
    train_dataset=`small_train_dataset`,
    eval_dataset=`small_eval_dataset`
)

trainer.train()
```
