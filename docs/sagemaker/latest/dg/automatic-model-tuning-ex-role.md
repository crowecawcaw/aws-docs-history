# Get the SageMaker AI Execution Role

Get the execution role for the notebook instance. This is the IAM role that you
created for your notebook instance.

To find the ARN of the IAM execution role attached to a notebook instance:

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the left navigation pane, choose **Notebook** then
   **Notebook instances**.
3. From the list of notebooks, select the notebook that you want to view.
4. The ARN is in the **Permissions and encryption** section.
   Alternatively, [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") users can retrieve the ARN of the execution role
   attached to their user profile or a notebook instance by running the following code:

```
from sagemaker import get_execution_role

role = get_execution_role()
print(role)
```

For more information about using `get_execution_role` in the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"), see [Session](https://sagemaker.readthedocs.io/en/stable/api/utility/session.html "https://sagemaker.readthedocs.io/en/stable/api/utility/session.html"). For more information about roles, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").

## Next Step

[Use an Amazon S3 bucket for input and
output](automatic-model-tuning-ex-bucket.md "automatic-model-tuning-ex-bucket.md")
