# Troubleshooting Python 3.12 Upgrade

**Effective Date:** January 21, 2026

## Overview

Effective January 21, 2026, Amazon Braket upgrades the Python runtime from 3.10 to 3.12 for all [Notebook Instances](https://github.com/amazon-braket/amazon-braket-examples "https://github.com/amazon-braket/amazon-braket-examples") and [managed container images](https://github.com/amazon-braket/amazon-braket-containers/tree/main "https://github.com/amazon-braket/amazon-braket-containers/tree/main") (Base, CUDA-Q, TensorFlow, and PyTorch). This guide provides solutions for common compatibility issues.

###### In this section:

- [Common Error Messages](#braket-troubleshooting-python312-errors "#braket-troubleshooting-python312-errors")
- [Braket Managed Notebooks](#braket-troubleshooting-python312-notebooks "#braket-troubleshooting-python312-notebooks")
- [Hybrid Job Decorator](#braket-troubleshooting-python312-hybrid-job "#braket-troubleshooting-python312-hybrid-job")
- [Bring-Your-Own-Container (BYOC)](#braket-troubleshooting-python312-byoc "#braket-troubleshooting-python312-byoc")
- [Braket Notebook Instance Upgrade](#braket-troubleshooting-python312-notebook-upgrade "#braket-troubleshooting-python312-notebook-upgrade")

## Common Error Messages

### SDK Python Version Mismatch Error

**Error:**

```
RuntimeError: Python version must match between local environment and container. Client is running Python 3.10 locally, but container uses Python 3.12.
```

**Cause:** The Braket SDK detected your notebook is running Python 3.10 but the Hybrid Job container is running Python 3.12.

**Solution:** Either [upgrade your notebook to Python 3.12](#braket-troubleshooting-python312-notebook-upgrade "#braket-troubleshooting-python312-notebook-upgrade") or [pin to Python 3.10 containers](#braket-troubleshooting-python312-option2 "#braket-troubleshooting-python312-option2").

### Cloudpickle Serialization Error

**Error:**

```
TypeError: code() argument 13 must be str, not int
```

**Cause:** If SDK validation is bypassed, cloudpickle fails to serialize code between Python 3.10 and 3.12 due to a CodeType constructor change in Python 3.12.

**Solution:** Ensure your notebook and container use the same Python version.

## Braket Managed Notebooks

If you're running a Braket Notebook Instance on Python 3.10 and submitting Hybrid Jobs, you will encounter version mismatch errors because the job containers now use Python 3.12 by default.

You have two options:

1. [Recommended] Create a new Notebook Instance with Python 3.12 - see [Braket Notebook Instance Upgrade](#braket-troubleshooting-python312-notebook-upgrade "#braket-troubleshooting-python312-notebook-upgrade")
2. Pin to Python 3.10 containers - see [Hybrid Job Decorator](#braket-troubleshooting-python312-hybrid-job "#braket-troubleshooting-python312-hybrid-job")

## Hybrid Job Decorator

To use the `@hybrid_job` decorator, your environment's Python version must match the container's Python version.

### Option 1: Use Python 3.12 Containers (Recommended)

If you've upgraded your environment to Python 3.12, it uses the latest tag (default behavior).

### Option 2: Use Python 3.10 Containers

If you must stay on Python 3.10, explicitly specify the `image_uri` parameter in `@hybrid_job` decorator.

**Python 3.10 Container Tags:**

| Image Name | Tag                                |
| ---------- | ---------------------------------- |
| Base       | 1.0-cpu-py310-ubuntu22.04          |
| CUDA-Q     | 0.12.0-cpu-py310-0.12.0            |
| PyTorch    | 2.2.0-gpu-py310-cu121-ubuntu20.04  |
| TensorFlow | 2.14.1-gpu-py310-cu118-ubuntu20.04 |

The following example is for the us-west-2 Region.

**Full Image URIs:**

```
Base:       292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-base-jobs:1.0-cpu-py310-ubuntu22.04
CUDA-Q:     292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-cudaq-jobs:0.12.0-cpu-py310-0.12.0
PyTorch:    292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-pytorch-jobs:2.2.0-gpu-py310-cu121-ubuntu20.04
TensorFlow: 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-tensorflow-jobs:2.14.1-gpu-py310-cu118-ubuntu20.04
```

**Example:**

```
from braket.jobs.hybrid_job import hybrid_job
from braket.devices import Devices

device_arn = Devices.Amazon.SV1

@hybrid_job(
    device=device_arn,
    image_uri="292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-base-jobs:1.0-cpu-py310-ubuntu22.04"
)
def my_job():
    pass
```

###### Note

- Python 3.10 containers will remain available but will not receive updates.
- See [Define the environment for your algorithm script](braket-jobs-script-environment.md "braket-jobs-script-environment.md").

## Bring-Your-Own-Container (BYOC)

If your Dockerfile uses a Braket managed image with the latest tag, rebuilding after January 21, 2026 will pull Python 3.12 supported images.

To stay on Python 3.10 supported Braket managed images, update your Dockerfile:

**Before (gets Python 3.12 after upgrade):**

```
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-base-jobs:latest
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-cudaq-jobs:latest
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-tensorflow-jobs:latest
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-pytorch-jobs:latest
```

**After (stays on Python 3.10):**

```
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-base-jobs:1.0-cpu-py310-ubuntu22.04
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-cudaq-jobs:0.12.0-cpu-py310-0.12.0
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-pytorch-jobs:2.2.0-gpu-py310-cu121-ubuntu20.04
FROM 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-tensorflow-jobs:2.14.1-gpu-py310-cu118-ubuntu20.04
```

## Braket Notebook Instance Upgrade

Follow these steps to upgrade to Python 3.12:

###### Important

Before deleting your notebook instance, ensure you have downloaded all notebooks and files you want to keep. This data cannot be recovered after deletion.

1. Download any notebooks you created or modified to a local drive.
2. Stop your notebook instance.
3. Delete your notebook instance.
4. Create a new notebook instance with a different name.
5. Upload your notebooks to the new instance.
