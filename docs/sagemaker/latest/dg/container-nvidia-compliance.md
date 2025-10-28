# Updating inference containers to comply with

the NVIDIA Container Toolkit

As of versions 1.17.4 and higher, the NVIDIA Container Toolkit no longer mounts CUDA
compatibility libraries automatically. This change in behavior could affect your SageMaker AI
inference workloads. Your SageMaker AI endpoints and batch transform jobs might use containers that
are incompatible with the latest versions of the NVIDIA Container Toolkit. To ensure that
your workloads comply with the latest requirements, you might need to update your endpoints
or configure your batch transform jobs.

## Updating SageMaker AI endpoints for compliance

We recommend that you update your existing SageMaker AI endpoints or create new ones that
support the latest default behavior.

To ensure your endpoint is compatible with latest versions of the NVIDIA Container
Toolkit, follow these steps:

1. Update how you set up the CUDA compatibility libraries if you bring your own
   container.
2. Specify an inference Amazon Machine Image (AMI) that supports the latest
   NVIDIA Container Toolkit behavior. You specify an AMI when you update an
   existing endpoint or create a new one.

### Updating the CUDA compatibility setup if you

bring your own container

The CUDA compatibility libraries enable forward compatibility. This compatibility
applies to any CUDA toolkit versions that are newer than the NVIDIA driver provided
by the SageMaker AI instance.

You must enable the CUDA compatibility libraries only when the NVIDIA driver that
the SageMaker AI instance uses has an older version than the CUDA toolkit in the model
container. If your model container does not require CUDA compatibility, you can skip
this step. For example, you can skip this step if you don't plan to use a newer CUDA
toolkit than those provided by SageMaker AI instances.

Because of the changes introduced in the NVIDIA Container Toolkit version 1.17.4,
you can explicitly enable CUDA compatibility libraries, if needed, by adding them to
`LD_LIBRARY_PATH` in the container.

We suggest that you enable the CUDA compatibility based on the detected NVIDIA
driver version. To enable it, add the code snippet below to the container startup
shell script. Add this code at the `ENTRYPOINT` script.

The following script demonstrates how to dynamically switch the use of the CUDA
compatibility based on the detected NVIDIA driver version on the deployed host for
your model container.

```
#!/bin/bash

verlt() {
    [ "$1" = "$2" ] && return 1 || [ "$1" = "$(echo -e "$1\n$2" | sort -V | head -n1)" ]
}

if [ -f /usr/local/cuda/compat/libcuda.so.1 ]; then
    CUDA_COMPAT_MAX_DRIVER_VERSION=$(readlink /usr/local/cuda/compat/libcuda.so.1 | cut -d'.' -f 3-)
    echo "CUDA compat package should be installed for NVIDIA driver smaller than ${CUDA_COMPAT_MAX_DRIVER_VERSION}"
    NVIDIA_DRIVER_VERSION=$(sed -n 's/^NVRM.*Kernel Module *\([0-9.]*\).*$/\1/p' /proc/driver/nvidia/version 2>/dev/null || true)
    echo "Current installed NVIDIA driver version is ${NVIDIA_DRIVER_VERSION}"
    if verlt $NVIDIA_DRIVER_VERSION $CUDA_COMPAT_MAX_DRIVER_VERSION; then
        echo "Adding CUDA compat to LD_LIBRARY_PATH"
        export LD_LIBRARY_PATH=/usr/local/cuda/compat:$LD_LIBRARY_PATH
        echo $LD_LIBRARY_PATH
    else
        echo "Skipping CUDA compat setup as newer NVIDIA driver is installed"
    fi
else
    echo "Skipping CUDA compat setup as package not found"
fi
```

### Specifying an Inference AMI that complies

with the NVIDIA Container Toolkit

In the `InferenceAmiVersion` parameter of the
`ProductionVariant` data type, you can select the AMI for a SageMaker AI
endpoint. Each of the supported AMIs is a preconfigured image. Each image is
configured by AWS with a set of software and driver versions.

By default, the SageMaker AI AMIs follow the legacy behavior. They automatically mount
CUDA compatibility libraries in the container. To make an endpoint use the new
behavior, you must specify an inference AMI version that is configured for the new
behavior.

The following inference AMI versions currently follow the new behavior. They don't
mount CUDA compatibility libraries automatically.

al2-ami-sagemaker-inference-gpu-2-1

- NVIDIA driver version: 535.54.03
- CUDA version: 12.2

al2-ami-sagemaker-inference-gpu-3-1

- NVIDIA driver version: 550.144.01
- CUDA version: 12.4

### Updating an existing endpoint

Use the following example to update an existing endpoint. The example uses an
inference AMI version that disables automatic mounting of CUDA compatibility
libraries.

```
ENDPOINT_NAME="<endpoint name>"
INFERENCE_AMI_VERSION="al2-ami-sagemaker-inference-gpu-3-1"

# Obtaining current endpoint configuration
CURRENT_ENDPOINT_CFG_NAME=$(aws sagemaker describe-endpoint --endpoint-name "$ENDPOINT_NAME" --query "EndpointConfigName" --output text)
NEW_ENDPOINT_CFG_NAME="${CURRENT_ENDPOINT_CFG_NAME}new"

# Copying Endpoint Configuration with AMI version specified
aws sagemaker describe-endpoint-config \
    --endpoint-config-name ${CURRENT_ENDPOINT_CFG_NAME} \
    --output json | \
jq "del(.EndpointConfigArn, .CreationTime) | . + {
    EndpointConfigName: \"${NEW_ENDPOINT_CFG_NAME}\",
    ProductionVariants: (.ProductionVariants | map(.InferenceAmiVersion = \"${INFERENCE_AMI_VERSION}\"))
}" > /tmp/new_endpoint_config.json

# Make sure all fields in the new endpoint config look as expected
cat /tmp/new_endpoint_config.json

# Creating new endpoint config
aws sagemaker create-endpoint-config \
   --cli-input-json file:///tmp/new_endpoint_config.json

# Updating the endpoint
aws sagemaker update-endpoint \
    --endpoint-name "$ENDPOINT_NAME" \
    --endpoint-config-name "$NEW_ENDPOINT_CFG_NAME" \
    --retain-all-variant-properties
```

### Creating a new endpoint

Use the following example to create a new endpoint. The example uses an inference
AMI version that disables automatic mounting of CUDA compatibility libraries.

```
INFERENCE_AMI_VERSION="al2-ami-sagemaker-inference-gpu-3-1"

aws sagemakercreate-endpoint-config \
 --endpoint-config-name "<endpoint_config>" \
 --production-variants '[{ \
    ....
    "InferenceAmiVersion":  "${INFERENCE_AMI_VERSION}", \
    ...
    "}]'

aws sagemaker create-endpoint \
--endpoint-name "<endpoint_name>" \
--endpoint-config-name "<endpoint_config>"
```

## Running compliant batch transform jobs

_Batch transform_ is the inference option that's best
suited for requests to process large amounts of data offline. To create batch transform
jobs, you use the `CreateTransformJob` API action. For more information, see
[Batch transform for inference with Amazon SageMaker AI](batch-transform.md "batch-transform.md").

The changed behavior of the NVIDIA Container Toolkit affects batch transform jobs.
To run a batch transform that complies with the NVIDIA Container Toolkit
requirements, do the following:

1. If you want to run batch transform with a model for which you've brought your
   own container, first, update the container for CUDA compatibility. To update it,
   follow the process in [Updating the CUDA compatibility setup if you
   bring your own container](#cuda-compatibility "#cuda-compatibility").
2. Use the `CreateTransformJob` API action to create the batch
   transform job. In your request, set the
   `SAGEMAKER_CUDA_COMPAT_DISABLED` environment variable to
   `true`. This parameter instructs to the container not to
   automatically mount CUDA compatibility libraries.

For example, when you create a batch transform job by using the AWS CLI, you set
the environment variable with the `--environment` parameter:

```
aws sagemaker create-transform-job \
    --environment '{"SAGEMAKER_CUDA_COMPAT_DISABLED": "true"}'\
    . . .
```
