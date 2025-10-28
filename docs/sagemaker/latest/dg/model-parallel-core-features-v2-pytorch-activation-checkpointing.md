# Activation checkpointing

_Activation checkpointing_ is a technique to reduce
memory usage by clearing activations of certain layers and recomputing them during the
backward pass. Effectively, this trades extra computation time for reducing memory
usage. If a module is checkpointed, at the end of a forward pass, only the initial
inputs to the module and final outputs from the module stay in memory. PyTorch releases
any intermediate tensors that are part of the computation inside that module during the
forward pass. During the backward pass of the checkpointed modules, PyTorch recomputes
these tensors. At this point, the layers beyond this checkpointed module have finished
their backward pass, so the peak memory usage with checkpointing becomes lower.

SMP v2 supports the PyTorch activation checkpointing module, [`apply_activation_checkpointing`](https://pytorch.org/blog/scaling-multimodal-foundation-models-in-torchmultimodal-with-pytorch-distributed/#activation-checkpointing "https://pytorch.org/blog/scaling-multimodal-foundation-models-in-torchmultimodal-with-pytorch-distributed/#activation-checkpointing"). The following are examples
of activation checkpointing of the Hugging Face GPT-NeoX model.

**Checkpointing Transformer layers of the Hugging Face GPT-NeoX
model**

```
from transformers.models.gpt_neox import GPTNeoXLayer
from torch.distributed.algorithms._checkpoint.checkpoint_wrapper import (
    apply_activation_checkpointing
)

# check_fn receives a module as the arg,
# and it needs to return whether the module is to be checkpointed
def is_transformer_layer(module):
    from transformers.models.gpt_neox import GPTNeoXLayer
    return isinstance(submodule, GPTNeoXLayer)

apply_activation_checkpointing(model, check_fn=is_transformer_layer)
```

**Checkpointing every other Transformer layer of the Hugging Face
GPT-NeoX model**

```
# check_fn receives a module as arg,
# and it needs to return whether the module is to be checkpointed
# here we define that function based on global variable (transformer_layers)
from transformers.models.gpt_neox import GPTNeoXLayer
from torch.distributed.algorithms._checkpoint.checkpoint_wrapper import (
    apply_activation_checkpointing
)

transformer_layers = [
    m for m model.modules() if isinstance(m, GPTNeoXLayer)
]

def is_odd_transformer_layer(module):
    return transformer_layers.index(module) % 2 == 0

apply_activation_checkpointing(model, check_fn=is_odd_transformer_layer)
```

Alternatively, PyTorch also has the `torch.utils.checkpoint` module for
checkpointing, which is used by a subset of Hugging Face Transformers models. This
module also works with SMP v2. However, it requires you to have access to the model
definition for adding the checkpoint wrapper. Therefore, we recommend you to use the
`apply_activation_checkpointing` method.
