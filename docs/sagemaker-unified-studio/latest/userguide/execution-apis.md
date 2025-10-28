# Execution APIs

Execution APIs provide you the ability to start an execution to run a notebook headlessly within the same user space or on remote compute.

## Local Execution APIs

Use the following APIs to start, stop, get, or list executions within the user's space.

### StartExecution

You can start a notebook execution headlessly within the same user space.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(overrides={
            "execution": {
                "local": True,
            }
        })
sagemaker_studio_api = SageMakerStudioAPI(config)

result = sagemaker_studio_api.execution_client.start_execution(
    execution_name="my-execution",
    input_config={"notebook_config": {
        "input_path": "src/folder2/test.ipynb"}},
    execution_type="NOTEBOOK",
    output_config={"notebook_config": {
        "output_formats": ["NOTEBOOK", "HTML"]
    }}
)
print(result)

```

### GetExecution

You can retrieve details about a local execution using the `GetExecution` API.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(region="us-west-2", overrides={
            "execution": {
                "local": True,
            }
        })
sagemaker_studio_api = SageMakerStudioAPI(config)

get_response = sagemaker_studio_api.execution_client.get_execution(execution_id="asdf-3b998be2-02dd-42af-8802-593d48d04daa")
print(get_response)

```

### ListExecutions

You can use the `ListExecutions` API to list all the executions that ran in the user's space.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(region="us-west-2", overrides={
            "execution": {
                "local": True,
            }
        })
sagemaker_studio_api = SageMakerStudioAPI(config)

list_executions_response = sagemaker_studio_api.execution_client.list_executions(status="COMPLETED")
print(list_executions_response)

```

### StopExecution

You can use the `StopExecution` API to stop an execution that's running in the user space.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(region="us-west-2", overrides={
            "execution": {
                "local": True,
            }
        })
sagemaker_studio_api = SageMakerStudioAPI(config)

stop_response = sagemaker_studio_api.execution_client.stop_execution(execution_id="asdf-3b998be2-02dd-42af-8802-593d48d04daa")
print(stop_response)

```
