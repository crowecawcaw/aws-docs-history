# FlashAttention

SMP v2 supports [FlashAttention](https://github.com/HazyResearch/flash-attention "https://github.com/HazyResearch/flash-attention") kernels and makes it easy to apply them to various scenarios
for Hugging Face Transformer models. Note that if you use FlashAttention package v2.0 or
later, SMP uses FlashAttention v2; however, the Triton flash attention defaults to the
flash attention kernel in FlashAttention v1.x, making it exclusively supported in
FlashAttention v1.

The module (`nn.Module`) is a low level API that defines the attention
layers of a model. It should be applied right after model creation, from the
`AutoModelForCausalLM.from_config()` API for example, and before the
model is being transformed or wrapped with FSDP.

## Use

FlashAttention kernels for self attention

The following code snippet shows how to use the [torch.sagemaker.nn.attn.FlashSelfAttention](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-flashselfattention "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-flashselfattention") API
provided by SMP v2.

```
def new_attn(self, q, k, v, attention_mask=None, head_mask=None):
    return (
        self.flashmod((q, k, v), causal=True, cast_dtype=torch.bfloat16, layout="b h s d"),
        None,
    )

for layer in model.gpt_neox.layers:
    layer.attention.flash_mod = **torch.sagemaker.nn.attn.FlashSelfAttention()**
    layer.attention._attn = functools.partial(new_attn, layer.attention)
```

## Use

FlashAttention kernels for grouped-query attention

SMP v2 also supports [FlashAttention](https://github.com/HazyResearch/flash-attention "https://github.com/HazyResearch/flash-attention") kernels for grouped-query attention (GQA) and makes it
easy to apply them to various scenarios for Hugging Face Transformer models.
Different from original attention architecture, GQA equally partitions query heads
into groups, and query heads in the same group share the same key and value heads.
Therefore, q and kv heads are passed into forward call separately. Note: The number
of q heads needs to be divisible by the number of kv heads.

**Example of using
FlashGroupedQueryAttention**

The following code snippet shows how to use the [torch.sagemaker.nn.attn.FlashGroupedQueryAttention](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn")
API provided by SMP v2.

```
from transformers.models.llama.modeling_llama import LlamaAttention
**from torch.sagemaker.nn.attn import FlashGroupedQueryAttention**

class LlamaFlashAttention(LlamaAttention):
    def __init__(self, config: LlamaConfig):
        super().__init__(config)

        self.flash_attn = **FlashGroupedQueryAttention**(
            attention_dropout_prob=0.0,
        )

    def forward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        ...
    ):
        query_states = self.q_proj(hidden_states)
        key_states = self.k_proj(hidden_states)
        value_states = self.v_proj(hidden_states)
        ...
        kv = (key_states, value_states)
        attn_output = self.flash_attn(
            query_states,
            kv,
            attn_mask=attention_mask,
            causal=True,
            layout="b h s d",
        )
        ...
        attn_output = self.o_proj(attn_output)
        ...
        return attn_output
```

The SMP library also provides [torch.sagemaker.nn.huggingface.llama_flashattn.LlamaFlashAttention](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-llamaFlashAttn "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-llamaFlashAttn"), which
uses the [torch.sagemaker.nn.attn.FlashGroupedQueryAttention](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn")
API at low level. Hugging Face Transformers has a similar implementation called
[`LlamaFlashAttention2`](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py "https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py") from v4.36.0. The following code
snippet shows how to use the SMP v2 `LlamaFlashAttention` API or the
Transformers `LlamaFlashAttention2` API to replace the attention layers
of an existing Llama model.

```
**from torch.sagemaker.nn.huggingface.llama\_flashattn import LlamaFlashAttention**
from transformers.models.llama.modeling_llama import LlamaFlashAttention2

**flash\_attn\_class = LlamaFlashAttention** # or flash_attn_class = **LlamaFlashAttention2**

attn_name = "self_attn"
for layer in model.model.layers:
    prev_layer = getattr(layer, attn_name)
    setattr(layer, attn_name, **flash\_attn\_class(model.config)**)
```
