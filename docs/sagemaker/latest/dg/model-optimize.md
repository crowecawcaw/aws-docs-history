# Inference optimization for Amazon SageMaker AI models

With Amazon SageMaker AI, you can improve the performance of your generative AI models by applying
inference optimization techniques. By optimizing your models, you can attain better
cost-performance for your use case. When you optimize a model, you choose which of the
supported optimization techniques to apply, including quantization, speculative decoding,
and compilation. After your model is optimized, you can run an evaluation to see performance
metrics for latency, throughput, and price.

For many models, SageMaker AI also provides several pre-optimized versions, where each caters to
different applications needs for latency and throughput. For such models, you can deploy one
of the optimized versions without first optimizing the model yourself.

## Optimization techniques

Amazon SageMaker AI supports the following optimization techniques.

### Compilation

_Compilation_ optimizes the model for the best
available performance on the chosen hardware type without a loss in accuracy. You
can apply model compilation to optimize LLMs for accelerated hardware, such as GPU
instances, AWS Trainium instances, or AWS Inferentia instances.

When you optimize a model with compilation, you benefit from ahead-of-time
compilation. You reduce the model's deployment time and auto-scaling latency because
the model weights don't require just-in-time compilation when the model deploys to a
new instance.

If you choose to compile your model for a GPU instance, SageMaker AI uses the TensorRT-LLM
library to run the compilation. If you choose to compile your model for an AWS
Trainium or AWS Inferentia instance, SageMaker AI uses the AWS Neuron SDK to run the
compilation.

### Quantization

_Quantization_ is a technique to reduce the
hardware requirements of a model by using a less precise data type for the weights
and activations. After you optimize a model with quantization, you can host it on
less expensive and more available GPUs. However, the quantized model might be less
accurate than the source model that you optimized.

The data formats that SageMaker AI supports for quantization vary from model to model. The
supported formats include the following:

- INT4-AWQ – A 4-bit data format. Activation-aware Weight
  Quantization (AWQ) is a quantization technique for LLMs that is efficient,
  accurate, low-bit, and weight-only.
- FP8 – 8-bit Floating Point (FP8) is a low-precision format for
  floating point numbers. It balances memory efficiency and model accuracy by
  representing values with fewer bits than standard FP16 floating point
  format.
- INT8-SmoothQuant – AN 8-bit data format. SmoothQuant is a
  mixed-precision quantization method that scales activations and weights
  jointly by balancing their dynamic ranges.

### Speculative decoding

_Speculative decoding_ is a technique to speed up
the decoding process of large LLMs. It optimizes models for latency without
compromising the quality of the generated text.

This technique uses a smaller but faster model called the _draft_ model. The draft model generates candidate tokens, which are
then validated by the larger but slower _target_
model. At each iteration, the draft model generates multiple candidate tokens. The
target model verifies the tokens, and if it finds that a particular token is not
acceptable, it rejects the token and regenerates it. So, the target model both
verifies tokens and generates a small amount of them.

The draft model is significantly faster than the target model. It generates all
the tokens quickly and then sends batches of them to the target model for
verification. The target model evaluate them all in parallel, which speeds up the
final response.

SageMaker AI offers a pre-built draft model that you can use, so you don't have to build
your own. If you prefer to use your own custom draft model, SageMaker AI also supports this
option.

### Fast model loading

The _fast model loading_ technique prepares an
LLM so that SageMaker AI can load it onto an ML instance more quickly.

To prepare the model, SageMaker AI shards it in advance by dividing it into portions that
can each reside on a separate GPU for distributed inference. Also, SageMaker AI stores the
model weights in equal-sized chunks that SageMaker AI can load onto the instance
concurrently.

When SageMaker AI loads the optimized model onto the instance, it streams the model
weights directly from Amazon S3 onto the GPUs of the instance. By streaming the weights,
SageMaker AI omits several time-consuming steps that are normally necessary. These steps
include downloading the model artifacts from Amazon S3 to disk, loading the model
artifacts onto the host memory, and sharding the model on the host before finally
loading the shards onto the GPUs.

After you optimize your model for faster loading, you can deploy it more quickly
to a SageMaker AI endpoint. Also, if you configure the endpoint to use auto scaling, it
scales out more quickly to accommodate increases in traffic.
