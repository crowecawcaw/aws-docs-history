# Remote Execution APIs

Use the following APIs to start, stop, get, or list executions running on remote
compute.

## StartExecution

You can start a notebook execution headlessly on a remote compute specified in
the `StartExecution` request.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(region="us-west-2")
sagemaker_studio_api = SageMakerStudioAPI(config)

result = sagemaker_studio_api.execution_client.start_execution(
    execution_name="my-execution",
    execution_type="NOTEBOOK",
    input_config={"notebook_config": {"input_path": "src/folder2/test.ipynb"}},
    output_config={"notebook_config": {"output_formats": ["NOTEBOOK", "HTML"]}},
    termination_condition={"max_runtime_in_seconds": 9000},
    compute={
        "instance_type": "ml.c5.xlarge",
        "image_details": {
            # provide either ecr_uri or (image_name and image_version)
            "image_name": "sagemaker-distribution-embargoed-loadtest",
            "image_version": "2.2",
            "ecr_uri": "123456123456.dkr.ecr.us-west-2.amazonaws.com/ImageName:latest",
        }
    }
)
print(result)

```

## GetExecution

You can retrieve details about an execution running on remote compute using
the `GetExecution` API.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(region="us-west-2")
sagemaker_studio_api = SageMakerStudioAPI(config)

get_response = sagemaker_studio_api.execution_client.get_execution(execution_id="asdf-3b998be2-02dd-42af-8802-593d48d04daa")
print(get_response)

```

## ListExecutions

You can use the `ListExecutions` API to list all the headless
executions that ran on remote compute.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(region="us-west-2")
sagemaker_studio_api = SageMakerStudioAPI(config)

list_executions_response = sagemaker_studio_api.execution_client.list_executions(status="COMPLETED")
print(list_executions_response)

```

## StopExecution

You can use the `StopExecution` API to stop an execution that's
running on remote compute.

```

from sagemaker_studio.sagemaker_studio_api import SageMakerStudioAPI
from sagemaker_studio import ClientConfig

config = ClientConfig(region="us-west-2")
sagemaker_studio_api = SageMakerStudioAPI(config)

stop_response = sagemaker_studio_api.execution_client.stop_execution(execution_id="asdf-3b998be2-02dd-42af-8802-593d48d04daa")
print(stop_response)

```
