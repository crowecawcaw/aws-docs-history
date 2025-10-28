# Run Training with EFA

SageMaker AI provides integration with [EFA](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") devices to accelerate High Performance
Computing (HPC) and machine learning applications. This integration allows you to leverage an
EFA device when running your distributed training jobs. You can add EFA integration to an existing Docker container that you bring to
SageMaker AI. The following information outlines how to configure your own container to use an EFA
device for your distributed training jobs.

## Prerequisites

Your container must satisfy the [SageMaker Training
container specification](your-algorithms-training-algo-dockerfile.md "your-algorithms-training-algo-dockerfile.md"). 

## Install EFA and required

packages

Your container must download and install the [EFA software](../../../AWSEC2/latest/UserGuide/efa-start.md "../../../AWSEC2/latest/UserGuide/efa-start.md"). This allows your
container to recognize the EFA device, and provides compatible versions of Libfabric and Open
MPI.

Any tools like MPI and NCCL must be installed and managed inside the container to be used
as part of your EFA-enabled training job. For a list of all available EFA versions, see [Verify the EFA installer
using a checksum](../../../AWSEC2/latest/UserGuide/efa-verify.md "../../../AWSEC2/latest/UserGuide/efa-verify.md"). The following example shows how to modify the Dockerfile of your
EFA-enabled container to install EFA, MPI, OFI, NCCL, and NCCL-TEST.

###### Note

When using PyTorch with EFA on your container, the NCCL version of your container should
match the NCCL version of your PyTorch installation. To verify the PyTorch NCCL version, use
the following command:

```
torch.cuda.nccl.version()
```

```
ARG OPEN_MPI_PATH=/opt/amazon/openmpi/
ENV NCCL_VERSION=2.7.8
ENV EFA_VERSION=1.30.0
ENV BRANCH_OFI=1.1.1

#################################################
## EFA and MPI SETUP
RUN cd $HOME \
  && curl -O https://s3-us-west-2.amazonaws.com/aws-efa-installer/aws-efa-installer-${EFA_VERSION}.tar.gz \
  && tar -xf aws-efa-installer-${EFA_VERSION}.tar.gz \
  && cd aws-efa-installer \
  && ./efa_installer.sh -y --skip-kmod -g \

ENV PATH="$OPEN_MPI_PATH/bin:$PATH"
ENV LD_LIBRARY_PATH="$OPEN_MPI_PATH/lib/:$LD_LIBRARY_PATH"

#################################################
## NCCL, OFI, NCCL-TEST SETUP
RUN cd $HOME \
  && git clone https://github.com/NVIDIA/nccl.git -b v${NCCL_VERSION}-1 \
  && cd nccl \
  && make -j64 src.build BUILDDIR=/usr/local

RUN apt-get update && apt-get install -y autoconf
RUN cd $HOME \
  && git clone https://github.com/aws/aws-ofi-nccl.git -b v${BRANCH_OFI} \
  && cd aws-ofi-nccl \
  && ./autogen.sh \
  && ./configure --with-libfabric=/opt/amazon/efa \
       --with-mpi=/opt/amazon/openmpi \
       --with-cuda=/usr/local/cuda \
       --with-nccl=/usr/local --prefix=/usr/local \
  && make && make install

RUN cd $HOME \
  && git clone https://github.com/NVIDIA/nccl-tests \
  && cd nccl-tests \
  && make MPI=1 MPI_HOME=/opt/amazon/openmpi CUDA_HOME=/usr/local/cuda NCCL_HOME=/usr/local
```

## Considerations when creating

your container

The EFA device is mounted to the container as `/dev/infiniband/uverbs0` under
the list of devices accessible to the container. On P4d instances, the container has access to
4 EFA devices. The EFA devices can be found in the list of devices accessible to the container
as:

- `/dev/infiniband/uverbs0`
- `/dev/infiniband/uverbs1`
- `/dev/infiniband/uverbs2`
- `/dev/infiniband/uverbs3`

To get information about hostname, peer hostnames, and network interface (for MPI) from
the `resourceconfig.json` file provided to each container instances, see [Distributed Training Configuration](your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training "your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training"). Your container handles regular TCP traffic
among peers through the default Elastic Network Interfaces (ENI), while handling OFI (kernel
bypass) traffic through the EFA device.

## Verify that your EFA device is

recognized

 To verify that the EFA device is recognized, run the following command from within your
container.

```
/opt/amazon/efa/bin/fi_info -p efa
```

Your output should look similar to the following.

```
provider: efa
    fabric: EFA-fe80::e5:56ff:fe34:56a8
    domain: efa_0-rdm
    version: 2.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA
provider: efa
    fabric: EFA-fe80::e5:56ff:fe34:56a8
    domain: efa_0-dgrm
    version: 2.0
    type: FI_EP_DGRAM
    protocol: FI_PROTO_EFA
provider: efa;ofi_rxd
    fabric: EFA-fe80::e5:56ff:fe34:56a8
    domain: efa_0-dgrm
    version: 1.0
    type: FI_EP_RDM
    protocol: FI_PROTO_RXD
```

## Running a training job with EFA

Once you’ve created an EFA-enabled container, you can run a training job with EFA using a
SageMaker AI Estimator the same way as you would with any other Docker image. For more information on
registering your container and using it for training, see [Adapting Your
Own Training Container](adapt-training-container.md#byoc-training-step5 "adapt-training-container.md#byoc-training-step5").
