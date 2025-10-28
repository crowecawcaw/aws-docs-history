# Delayed parameter

initialization

Initialization of a large model for training is not always possible with the limited
GPU memory. To resolve this problem of insufficient GPU memory, you can initialize the
model on CPU memory. However, for larger models with more than 20 or 40 billion
parameters, even CPU memory might not be enough. For such case, we recommend that you
initialize the model on what PyTorch calls a _meta
device_, which allows the creation of tensors without any data attached to
them. A tensor on a meta device only needs the shape information, and this allows to
create a large model with its parameters on meta devices. [Hugging Face Accelerate](https://huggingface.co/docs/accelerate/index "https://huggingface.co/docs/accelerate/index")
provides the context manager `init_empty_weights` to help create such model
on meta devices while initializing the buffers on a regular device. Before training
starts, PyTorch FSDP initializes the model parameters.
This delayed parameter initialization feature of SMP v2 delays this creation of model
parameters to happen after PyTorch FSDP performs parameter sharding.
PyTorch FSDP accepts a parameter initialization function (`param_init_fn`)
when sharding the modules, and it calls `param_init_fn` for each module. The
`param_init_fn` API takes a module as an argument and initializes all the
parameters in it, not including the parameters of any child module. Note that this
behavior _differs_ from the native PyTorch v2.0.1 which
has a bug causing the parameters to be initialized multiple times.

SMP v2 provides the [torch.sagemaker.delayed_param.DelayedParamIniter](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-delayed-param-init "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-delayed-param-init") API for
applying delayed parameter initialization.

The following code snippets show how to apply the
`torch.sagemaker.delayed_param.DelayedParamIniter` API to your training
script.

Assume that you have a PyTorch FSDP training script as follows.

```
# Creation of model on meta device
from accelerate import init_empty_weights
with init_empty_weights():
    model = create_model()

# Define a param init fn, below is an example for Hugging Face GPTNeoX.
def init_weights(module):
    d = torch.cuda.current_device()
    # Note that below doesn't work if you have buffers in the model
    # buffers will need to reinitialized after this call
    module.to_empty(device=d, recurse=False)
    if isinstance(module, (nn.Linear, Conv1D)):
        module.weight.data.normal_(mean=0.0, std=args.initializer_range)
        if module.bias:
            module.bias.data.zero_()
    elif isinstance(module, nn.Embedding):
        module.weight.data.normal_(mean=0.0, std=args.initializer_range)
        if module.padding_idx:
            module.weight.data[module.padding_idx].zero_()
    elif isinstance(module, nn.LayerNorm):
        module.bias.data.zero_()
        module.weight.data.fill_(1.0)

# Changes to FSDP wrapper.
model = FSDP(
    model,
    ...,
    param_init_fn=init_weights
)

# At this point model is initialized and sharded for sharded data parallelism.
```

Note that the delayed parameter initialization approach is not model agnostic. To
resolve this issue, you need to write an `init_weights` function as shown in
the preceding example to match the initialization in the original model definition, and
it should cover all the parameters of the model. To simplify this process of preparing
such `init_weights` function, SMP v2 implements this initialization function
for the following models: GPT-2, GPT-J, GPT-NeoX, and Llama from Hugging Face
Transformers. The `torch.sagemaker.delayed_param.DelayedParamIniter` API also
works with the SMP tensor parallel implementation,
`torch.sagemaker.tensor_parallel.transformer.TransformerLMHead` model,
that you can call after the [torch.sagemaker.transform](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform") API call.

Using the `torch.sagemaker.delayed_param.DelayedParamIniter` API, you can
adapt your PyTorch FSDP script as follows. After creating a model with empty weights,
register the `torch.sagemaker.delayed_param.DelayedParamIniter` API to the
model, and define an object of it. Pass the object to the `param_init_fn` of
the PyTorch FSDP class.

```
**from torch.sagemaker.delayed\_param import DelayedParamIniter**
from accelerate import init_empty_weights

with init_empty_weights():
    model = create_model()

**delayed\_initer = DelayedParamIniter(model)**

**with delayed\_initer.validate\_params\_and\_buffers\_inited():**
    model = FSDP(
        model,
        ...,
        param_init_fn=**delayed\_initer.get\_param\_init\_fn()**
    )
```

**Notes on tied weights**

When training models with tied weights, we need to take special care to tie the
weights after initializing the weights with delayed parameter initialization. PyTorch
FSDP does not have a mechanism to tie the weights after initializing them using
`param_init_fn` as above. To address such cases we added API to allow a
`post_init_hook_fn`, which can be used to tie the weights. You can pass
any function in there which accepts the module as argument, but we also have a
predefined `post_param_init_fn` defined in `DelayedParamIniter`
which calls `tie_weights` method of the module if it exists. Note that it’s
safe to always pass in `post_param_init_fn` even if there’s no
`tie_weights` method for the module.

```
with delayed_initer.validate_params_and_buffers_inited():
    model = FSDP(
        model,
        ...,
        param_init_fn=delayed_initer.get_param_init_fn(),
        post_param_init_fn=delayed_initer.get_post_param_init_fn()
    )
```
