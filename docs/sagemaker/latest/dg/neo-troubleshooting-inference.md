

# Troubleshoot Neo Inference Errors
<a name="neo-troubleshooting-inference"></a>

This section contains information about how to prevent and resolve some of the common errors you might encounter upon deploying and/or invoking the endpoint. This section applies to **PyTorch 1.4.0 or later** and **MXNet v1.7.0 or later**. 
+ Make sure the first inference (warm-up inference) on a valid input data is done in `model_fn()`, if you defined a `model_fn` in your inference script, otherwise the following error message may be seen on the terminal when [`predict API`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_serve.html) is called: 

  ```
  An error occurred (ModelError) when calling the InvokeEndpoint operation: Received server error (0) from <users-sagemaker-endpoint> with message "Your invocation timed out while waiting for a response from container model. Review the latency metrics for each container in Amazon CloudWatch, resolve the issue, and try again."                
  ```
+ Make sure that the environment variables in the following table are set. If they are not set, the following error message might show up: 

  **On the terminal:**

  ```
  An error occurred (ModelError) when calling the InvokeEndpoint operation: Received server error (503) from <users-sagemaker-endpoint> with message "{ "code": 503, "type": "InternalServerException", "message": "Prediction failed" } ".
  ```

  **In CloudWatch:**

  ```
  W-9001-model-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle - AttributeError: 'NoneType' object has no attribute 'transform'
  ```


<table>
<thead>
  <tr><th>Key</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>SAGEMAKER_PROGRAM</td><td>inference.py</td></tr>
  <tr><td>SAGEMAKER_SUBMIT_DIRECTORY</td><td>/opt/ml/model/code</td></tr>
  <tr><td>SAGEMAKER_CONTAINER_LOG_LEVEL</td><td>20</td></tr>
  <tr><td>SAGEMAKER_REGION</td><td>&lt;your region&gt;</td></tr>
</tbody>
</table>

+ Make sure that the `MMS_DEFAULT_RESPONSE_TIMEOUT` environment variable is set to 500 or a higher value while creating the Amazon SageMaker AI model; otherwise, the following error message may be seen on the terminal: 

  ```
  An error occurred (ModelError) when calling the InvokeEndpoint operation: Received server error (0) from <users-sagemaker-endpoint> with message "Your invocation timed out while waiting for a response from container model. Review the latency metrics for each container in Amazon CloudWatch, resolve the issue, and try again."
  ```