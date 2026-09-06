

# Configure the `DebuggerHookConfig` API to save tensors
<a name="debugger-configure-tensor-hook"></a>

**Note**  
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md). 

Use the [DebuggerHookConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html                 #sagemaker.debugger.DebuggerHookConfig) API to create a `debugger_hook_config` object using the `collection_configs` object you created in the previous step.

```
from sagemaker.core.debugger import DebuggerHookConfig

debugger_hook_config=DebuggerHookConfig(
    collection_configs=collection_configs
)
```

Debugger saves the model training output tensors into the default S3 bucket. The format of the default S3 bucket URI is `s3://amzn-s3-demo-bucket-sagemaker-<region>-<12digit_account_id>/<training-job-name>/debug-output/.`

If you want to specify an exact S3 bucket URI, use the following code example:

```
from sagemaker.core.debugger import DebuggerHookConfig

debugger_hook_config=DebuggerHookConfig(
    s3_output_path="{{specify-uri}}",
    collection_configs=collection_configs
)
```

For more information, see [DebuggerHookConfig](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html#sagemaker.debugger.DebuggerHookConfig) in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable).