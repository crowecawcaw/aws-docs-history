# Fine-tuning

Fine-tuning is a process of continuously training pre-trained models to improve
performance for specific use cases.

Fine-tuning small models that fit fully on a single GPU, or those that fit 8 copies of
model fully on CPUs is straightforward. It requires no special change to regular FSDP
training. In the realm of models larger than this, you need to consider using the
delayed parameter initialization functionality, which can be tricky.

To address this, the SMP library loads the full model on one of the ranks while the
rest of the ranks create models with empty weights on a meta device. Then, PyTorch FSDP
initializes the weights on non-zero ranks using the `init_weights` function,
and synchronizes the weights on all ranks to the weights on the 0th rank with
`sync_module_states` set to `True`. The following code snippet
shows how you should set it up in your training script.

```
import torch.distributed as dist
from transformers import AutoModelForCasalLM
from accelerate import init_empty_weights
**from torch.sagemaker.delayed\_param import DelayedParamIniter**

if dist.get_rank() == 0:
    model = AutoModelForCasalLM.from_pretrained(..., low_cpu_mem_usage=True)
else:
    with init_empty_weights():
        model = AutoModelForCasalLM.from_config(AutoConfig.from_pretrained(...))
    delayed_initer = **DelayedParamIniter(model)**

model = FSDP(
    model,
    ...,
    sync_module_states=True,
    param_init_fn=delayed_initer.get_param_init_fn() if dist.get_rank() > 0 else None
)
```

## Fine-tuning a pre-trained Hugging Face Transformer model with SMP tensor

parallelism

This section discusses loading Transformer models for two use cases: fine-tuning
small Transformer models and fine-tuning large Transformer models. For smaller
models without delayed parameter initialization, wrap the model with the
`torch.sagemaker.transform` API before wrapping it with PyTorch
FSDP.

```
import functools
from transformers import AutoModelForCausalLM
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp.wrap import transformer_auto_wrap_policy
**from torch.sagemaker import transform**

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", low_cpu_mem_usage=True)

# Transform model while loading state dictionary from rank 0.
**tp\_model = transform(model, load\_state\_dict\_from\_rank0=True)**

# Wrap with FSDP.
model = FSDP(
    tp_model,
    ...
    sync_module_states=True,
)
```

For larger models, the preceding approach causes to run out of CPU memory. We
recommend that you use delayed parameter initialization to avoid such CPU memory
issues. In this case, you can apply the `torch.sagemaker.transform` API
and the `torch.sagemaker.delayed_param.DelayedParamIniter` API as shown
in the following code example.

```
from transformers import AutoModelForCausalLM
**from torch.sagemaker import transform
from torch.sagemaker.delayed\_param import DelayedParamIniter**

# Create one instance of model without delayed param
# on CPU, on one rank.
if dist.get_rank() == 0:
    model = AutoModelForCasalLM.from_pretrained(...,low_cpu_mem_usage=True)
else:
    with init_empty_weights():
        model = AutoModelForCasalLM.from_config(AutoConfig.from_pretrained(...))

# Transform model while loading state dictionary from rank 0
**model = transform(model, load\_state\_dict\_from\_rank0=True)**

**if dist.get\_rank() != 0: # For fine-tuning, delayed parameter on non-zero ranks
 delayed\_initer = DelayedParamIniter(model)**
else:
    delayed_initer = None

**with (
 delayed\_initer.validate\_params\_and\_buffers\_inited() if delayed\_initer else nullcontext()
):**
    # Wrap the model with FSDP
    model = FSDP(
        model,
        ...,
        sync_module_states=True,
        param_init_fn=**delayed\_initer.get\_param\_init\_fn() if delayed\_initer else None**
    )
```
