End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Creating a Python project

## Python custom container

To run your Python-based SimSpace Weaver simulation in the AWS Cloud, you can create
a custom container that includes the necessary dependencies. For more information, see
[Custom containers](working-with_custom-containers.md "working-with_custom-containers.md").

A Python custom container must include the following:

- gcc
- openssl-devel
- bzip2-devel
- libffi-devel
- wget
- tar
- gzip
- make
- Python (version 3.9)

If you use the `PythonBubblesSample` template
to create your project, you can run the
`quick-start.py` script (located in
the `tools` folder of your project) to create
a Docker image with the necessary dependencies. The script
uploads the image to Amazon Elastic Container Registry (Amazon ECR).

The `quick-start.py` script uses the
following `Dockerfile`:

```
FROM public.ecr.aws/amazonlinux/amazonlinux:2
RUN yum -y install gcc openssl-devel bzip2-devel libffi-devel
RUN yum -y install wget
RUN yum -y install tar
RUN yum -y install gzip
RUN yum -y install make
WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
RUN tar xzf Python-3.9.0.tgz
WORKDIR /opt/Python-3.9.0
RUN ./configure --enable-optimizations
RUN make altinstall
COPY requirements.txt ./
RUN python3.9 -m pip install --upgrade pip
RUN pip3.9 install -r requirements.txt

```

You can add your own dependencies to the `Dockerfile`:

```
RUN yum -y install `dependency-name`
```

The `requirements.txt` file contains a list of Python
packages required for the `PythonBubblesSample` sample
simulation:

```
Flask==2.1.1

```

You can add your own Python package dependencies to the
`requirements.txt`:

```
`package-name`==`version-number`
```

The `Dockerfile` and `requirements.txt` are in the `tools`
folder of your project.

###### Important

You technically don't have to use a custom container with your Python simulation,
but we strongly recommend that you use a custom container. The
standard Amazon Linux 2 (AL2) container that we provide doesn't have Python.
Therefore, if you don't use a custom container that has Python,
you must include Python and the required dependencies in each app zip
file that you upload to SimSpace Weaver.
