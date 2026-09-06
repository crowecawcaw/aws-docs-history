# Define the environment for your algorithm script

Amazon Braket supports environments defined by containers for your
algorithm script:

- A base container (the default, if no `image_uri` is specified)
- A container with CUDA-Q
- A container with TensorFlow and PennyLane
- A container with PyTorch, PennyLane, and CUDA-Q
  The following table provides details about the containers and the libraries they
  include.

Amazon Braket containers| Type | Base | CUDA-Q | TensorFlow | PyTorch |
| --- | --- | --- | --- | --- |
| **Image URI** | 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-base-jobs:latest | 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-cudaq-jobs:latest | 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-tensorflow-jobs:latest | 292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-pytorch-jobs:latest |
| **Base image** | public.ecr.aws/lts/ubuntu:24.04 | public.ecr.aws/lts/ubuntu:24.04 | AWS Deep Learning Container tensorflow-training:2.19.0-gpu-py312-cu125-ubuntu22.04 | AWS Deep Learning Container pytorch-training:2.8.0-gpu-py312-cu129-ubuntu22.04 |
| **Python version** | 3.12 | 3.12 | 3.12 | 3.12 |
| **Preinstalled packages** | • amazon-braket-default-simulator<br>• amazon-braket-pennylane-plugin<br>• amazon-braket-schemas<br>• amazon-braket-sdk<br>• awscli<br>• boto3<br>• botocore<br>• dask<br>• matplotlib<br>• mpi4py<br>• numpy<br>• pandas<br>• pennylane<br>• pennylane-lightning<br>• qiskit<br>• qiskit-braket-provider<br>• sagemaker-training<br>• scikit-learn<br>• scipy | • amazon-braket-default-simulator<br>• amazon-braket-pennylane-plugin<br>• amazon-braket-schemas<br>• amazon-braket-sdk<br>• awscli<br>• boto3<br>• botocore<br>• cuda-quantum-cu12<br>• cudaq-qec-cu12<br>• cudaq-solvers-cu12<br>• dask<br>• matplotlib<br>• mpi4py<br>• numpy<br>• pandas<br>• pennylane<br>• pennylane-lightning<br>• qiskit<br>• qiskit-braket-provider<br>• sagemaker-training<br>• scikit-learn<br>• scipy | • amazon-braket-default-simulator<br>• amazon-braket-pennylane-plugin<br>• amazon-braket-schemas<br>• amazon-braket-sdk<br>• awscli<br>• boto3<br>• botocore<br>• dask<br>• h5py<br>• ipykernel<br>• jupyterlab<br>• matplotlib<br>• notebook<br>• numpy<br>• openfermion<br>• pandas<br>• pennylane<br>• pennylane-lightning<br>• pydantic<br>• sagemaker-training<br>• scikit-learn<br>• scipy<br>• tensorflow | • amazon-braket-default-simulator<br>• amazon-braket-pennylane-plugin<br>• amazon-braket-schemas<br>• amazon-braket-sdk<br>• awscli<br>• boto3<br>• botocore<br>• cuda-quantum-cu12<br>• cudaq-qec-cu12<br>• cudaq-solvers-cu12<br>• dask<br>• h5py<br>• ipykernel<br>• matplotlib<br>• numpy<br>• openfermion<br>• pandas<br>• pennylane<br>• pennylane-lightning[gpu]<br>• pydantic<br>• sagemaker-training<br>• scikit-learn<br>• scipy<br>• torch |

You can view and access the open source container definitions at [amazon-braket/amazon-braket-containers](https://github.com/amazon-braket/amazon-braket-containers "https://github.com/amazon-braket/amazon-braket-containers") on GitHub. Choose the container that best matches your use
case. You can use any of the available AWS Regions in Braket (us-east-1, us-west-1, us-west-2,
eu-north-1, eu-west-2), but the container Region must match the Region for your hybrid job. Specify
the container image when you create a hybrid job by adding one of the following four arguments to
your `create(…​)` call in the hybrid job script. You can install additional
dependencies into the container you choose at runtime (at the cost of startup or runtime)
because the Amazon Braket containers have internet connectivity. The
following example is for the us-west-2 Region.

- **Base image:**
  image\_uri="292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-base-jobs:latest"
- **CUDA-Q image:**
  image\_uri="292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-cudaq-jobs:latest"
- **TensorFlow image:**
  image\_uri="292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-tensorflow-jobs:latest"
- **PyTorch image:**
  image\_uri="292282985366.dkr.ecr.us-west-2.amazonaws.com/amazon-braket-pytorch-jobs:latest"
  The `image-uris` can also be retrieved using the
  `retrieve_image()` function in the Amazon Braket SDK. The
  following example shows how to retrieve them from the us-west-2 AWS Region.

```
from braket.jobs.image_uris import retrieve_image, Framework

image_uri_base = retrieve_image(Framework.BASE, "us-west-2")
image_uri_cudaq = retrieve_image(Framework.CUDAQ, "us-west-2")
image_uri_tf = retrieve_image(Framework.PL_TENSORFLOW, "us-west-2")
image_uri_pytorch = retrieve_image(Framework.PL_PYTORCH, "us-west-2")
```
