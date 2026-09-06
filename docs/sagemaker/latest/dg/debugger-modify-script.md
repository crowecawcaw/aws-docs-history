

# Adapting your training script to register a hook
<a name="debugger-modify-script"></a>

**Note**  
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md). 

Amazon SageMaker Debugger comes with a client library called the [`sagemaker-debugger` Python SDK](https://sagemaker-debugger.readthedocs.io/en/website). The `sagemaker-debugger` Python SDK provides tools for adapting your training script before training and analysis tools after training. In this page, you'll learn how to adapt your training script using the client library. 

The `sagemaker-debugger` Python SDK provides wrapper functions that help register a hook to extract model tensors, without altering your training script. To get started with collecting model output tensors and debug them to find training issues, make the following modifications in your training script.

**Tip**  
While you're following this page, use the [`sagemaker-debugger` open source SDK documentation](https://sagemaker-debugger.readthedocs.io/en/website/index.html) for API references.

**Topics**
+ [Adapt your PyTorch training script](debugger-modify-script-pytorch.md)
+ [Adapt your TensorFlow training script](debugger-modify-script-tensorflow.md)