# Recipe for bringing your own container

In this section, we provide a step-by-step guide of what you need to bring your own container
(BYOC) to Braket Hybrid Jobs — the scripts, files, and steps to combine them to get up
and running with your custom Docker images. The recipes for two common cases:

1. Install additional software in a Docker image and use only Python algorithm scripts in your jobs.
2. Use algorithm scripts written in a non-Python language with Hybrid Jobs, or a CPU architecture besides x86.
   Defining the _container entry script_ is more complex for case 2.

When Braket runs your Hybrid Job, it launches the requested number and type of Amazon EC2 instances, then
runs the Docker image specified by the image URI input to job creation on them. When using
the BYOC feature, you specify an image URI hosted in a
[private Amazon ECR repository](../../../AmazonECR/latest/userguide/Repositories.md "../../../AmazonECR/latest/userguide/Repositories.md")
that you have Read access to. Braket Hybrid Jobs uses that custom image to run the job.

The specific components you need to build a Docker image that can
be used with Hybrid Jobs. If you are unfamiliar with writing and building `Dockerfiles`, refer to
the [Dockerfile documentation](https://docs.docker.com/reference/dockerfile/ "https://docs.docker.com/reference/dockerfile/")
and the [Amazon ECR
CLI documentation](../../../AmazonECR/latest/userguide/getting-started-cli.md "../../../AmazonECR/latest/userguide/getting-started-cli.md").

###### Requirements:

- [A base image for your Dockerfile](#base-image-dockerfile "#base-image-dockerfile")
- [(Optional) A modified container entry point script](#modified-container-entry-point "#modified-container-entry-point")
- [Install needed software and container script with Dockerfile](#install-docketfile "#install-docketfile")

## A base image for your Dockerfile

If you are using Python and want to install software on top of what is provided
in the Braket provided containers, an option for a base image is one of the Braket
container images, hosted in our
[GitHub repo](https://github.com/amazon-braket/amazon-braket-containers "https://github.com/amazon-braket/amazon-braket-containers")
and on Amazon ECR. You will need to
[authenticate to Amazon ECR](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-authenticate-registry "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-authenticate-registry")
to pull the image and build on top of it. For example, the first line of your BYOC
Docker file could be:
`FROM [IMAGE_URI_HERE]`

Next, fill out the rest of the Dockerfile to install and set up
the software that you want to add to the container. The pre-built Braket images will
already contain the appropriate container entry point script, so you do not need to worry
about including that.

If you want to use a non-Python language, such as C++, Rust, or Julia, or if you want to build
an image for a non-x86 CPU architecture, like ARM, you may need to build on top of a
barebones public image. You can find many such images at the
[Amazon Elastic Container Registry Public Gallery](https://gallery.ecr.aws/ "https://gallery.ecr.aws/"). Make sure you choose
one that is appropriate for the CPU architecture, and if necessary, the GPU you want to use.

## (Optional) A modified container entry point script

###### Note

If you're only adding additional software to a pre-built Braket image, you can skip this section.

To run non-Python code as part of your hybrid job, modify the Python script which
defines the container entry point. For example, the
[`braket_container.py` python script on the Amazon Braket Github](https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py "https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py") . This is the script the images
pre-built by Braket use to launch your algorithm script and set appropriate environment
variables. The container entry point script itself **must** be in Python, but can launch
non-Python scripts. In the pre-built example, you can see that Python algorithm scripts are launched either as a
[Python subprocess](https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py#L274 "https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py#L274")
or as a [fully new process](https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py#L257 "https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py#L257").
By modifying this logic, you can enable the entry point script to launch non-Python algorithm scripts. For example, you could modify
[`thekick_off_customer_script()`](https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py#L139 "https://github.com/amazon-braket/amazon-braket-containers/blob/main/src/braket_container.py#L139")
function to launch Rust processes dependent on the file extension ending.

You can also choose to write a completely new `braket_container.py`. It should copy input data, source archives,
and other necessary files from Amazon S3 into the container, and define the appropriate environment variables.

## Install needed software and container script with `Dockerfile`

###### Note

If you use a pre-built Braket image as your Docker base image, the container script is already present.

If you created a modified container script in the previous step, you'll need to copy it into the container
**and** define the environment variable `SAGEMAKER_PROGRAM` to
`braket_container.py`, or what you have named your new container entry point script.

The following is an example of a `Dockerfile` that allows you to use Julia on GPU-accelerated Jobs instances:

```
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04


 ARG DEBIAN_FRONTEND=noninteractive
 ARG JULIA_RELEASE=1.8
 ARG JULIA_VERSION=1.8.3


 ARG PYTHON=python3.11
 ARG PYTHON_PIP=python3-pip
 ARG PIP=pip


 ARG JULIA_URL = https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_RELEASE}/
 ARG TAR_NAME = julia-${JULIA_VERSION}-linux-x86_64.tar.gz


 ARG PYTHON_PKGS = # list your Python packages and versions here


 RUN curl -s -L ${JULIA_URL}/${TAR_NAME} | tar -C /usr/local -x -z --strip-components=1 -f -


 RUN apt-get update \

    && apt-get install -y --no-install-recommends \

    build-essential \

    tzdata \

    openssh-client \

    openssh-server \

    ca-certificates \

    curl \

    git \

    libtemplate-perl \

    libssl1.1 \

    openssl \

    unzip \

    wget \

    zlib1g-dev \

    ${PYTHON_PIP} \

    ${PYTHON}-dev \




 RUN ${PIP} install --no-cache --upgrade ${PYTHON_PKGS}


 RUN ${PIP} install --no-cache --upgrade sagemaker-training==4.1.3


 # Add EFA and SMDDP to LD library path
 ENV LD_LIBRARY_PATH="/opt/conda/lib/python${PYTHON_SHORT_VERSION}/site-packages/smdistributed/dataparallel/lib:$LD_LIBRARY_PATH"
 ENV LD_LIBRARY_PATH=/opt/amazon/efa/lib/:$LD_LIBRARY_PATH


 # Julia specific installation instructions
 COPY Project.toml /usr/local/share/julia/environments/v${JULIA_RELEASE}/
 RUN JULIA_DEPOT_PATH=/usr/local/share/julia \

    julia -e 'using Pkg; Pkg.instantiate(); Pkg.API.precompile()'
 # generate the device runtime library for all known and supported devices
 RUN JULIA_DEPOT_PATH=/usr/local/share/julia \

    julia -e 'using CUDA; CUDA.precompile_runtime()'


 # Open source compliance scripts
 RUN HOME_DIR=/root \

 && curl -o ${HOME_DIR}/oss_compliance.zip https://aws-dlinfra-utilities.s3.amazonaws.com/oss_compliance.zip \

 && unzip ${HOME_DIR}/oss_compliance.zip -d ${HOME_DIR}/ \

 && cp ${HOME_DIR}/oss_compliance/test/testOSSCompliance /usr/local/bin/testOSSCompliance \

 && chmod +x /usr/local/bin/testOSSCompliance \

 && chmod +x ${HOME_DIR}/oss_compliance/generate_oss_compliance.sh \

 && ${HOME_DIR}/oss_compliance/generate_oss_compliance.sh ${HOME_DIR} ${PYTHON} \

 && rm -rf ${HOME_DIR}/oss_compliance*


 # Copying the container entry point script
 COPY braket_container.py /opt/ml/code/braket_container.py
 ENV SAGEMAKER_PROGRAM braket_container.py
```

This example, downloads and runs scripts provided by AWS to ensure compliance with all relevant
Open-Source licenses. For example, by properly attributing any installed code governed by an MIT license.

If you need to include non-public code, for instance code that is hosted in a private GitHub or GitLab repository,
**do not** embed SSH keys in the Docker image to access it. Instead,
use Docker Compose when you build to allow Docker to access SSH on the host
machine it is built on. For more information, see the
[Securely using SSH keys in Docker to access private
Github repositories](https://www.fastruby.io/blog/docker/docker-ssh-keys.html "https://www.fastruby.io/blog/docker/docker-ssh-keys.html") guide.

**Building and uploading your Docker image**

With a properly defined `Dockerfile`, you are now ready to follow the steps to
[create a private Amazon ECR repository](../../../AmazonECR/latest/userguide/repository-create.md "../../../AmazonECR/latest/userguide/repository-create.md"),
if one does not already exist. You can also build, tag, and upload your container image to the repository.

You are ready to build, tag, and push the image. See the
[Docker build documentation](https://docs.docker.com/reference/cli/docker/buildx/build/ "https://docs.docker.com/reference/cli/docker/buildx/build/") for a full explanation
of options to `docker build` and some examples.

For the sample file defined above, you could run:

```
aws ecr get-login-password --region ${your_region} | docker login --username AWS --password-stdin ${aws_account_id}.dkr.ecr.${your_region}.amazonaws.com
 docker build -t braket-julia .
 docker tag braket-julia:latest ${aws_account_id}.dkr.ecr.${your_region}.amazonaws.com/braket-julia:latest
 docker push ${aws_account_id}.dkr.ecr.${your_region}.amazonaws.com/braket-julia:latest
```

**Assigning appropriate Amazon ECR permissions**

Braket Hybrid Jobs Docker images must be hosted in private Amazon ECR repositories.
By default, a private Amazon ECR repo does **not** provide read
access to the Braket Hybrid Jobs IAM role or to any other users that want to
use your image, such as a collaborator or student. You must
[set a repository policy](../../../AmazonECR/latest/userguide/set-repository-policy.md "../../../AmazonECR/latest/userguide/set-repository-policy.md")
to grant the appropriate permissions. In general, only give permission to
those specific users and IAM roles you want to access your images, rather than allowing anyone with the
image URI to pull them.
