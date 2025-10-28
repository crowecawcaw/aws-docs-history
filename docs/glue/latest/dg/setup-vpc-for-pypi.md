# Setting up a VPC to connect to PyPI for

AWS Glue

The Python Package Index (PyPI) is a repository of software for the Python programming language. This topic addresses the details needed to support the use of pip installed packages (as specified by the session creator using the `--additional-python-modules` flag).

Using AWS Glue interactive sessions with a connector results in the use of VPC network via the subnet specified for the connector. Consequently AWS services and other network destinations are not available unless you set up a special configuration.

The resolutions to this issue include:

- Use of an internet gateway which is reachable by your session.
- Set up and use of an S3 bucket with a PyPI/simple repo containing the transitive closure of a package set's dependencies.
- Use of a CodeArtifact repository which is mirroring PyPI and attached to your VPC.

## Setting up an internet gateway

The technical aspects are detailed in [NAT gateway use cases](../../../vpc/latest/userguide/nat-gateway-scenarios.md "../../../vpc/latest/userguide/nat-gateway-scenarios.md") but note these requirements for using `--additional-python-modules`. Specifically, `--additional-python-modules` requires access to pypi.org which is determined by the configuration of your VPC. Note the following requirements:

1. The requirement of installing additional python modules via pip install for a user's session. If the session uses a connector, your configuration may be affected.
2. When a connector is being used with `--additional-python-modules`, when the session is started the subnet associated with the connector's `PhysicalConnectionRequirements` has to provide a network path for reaching pypi.org.
3. You must determine whether or not your configuration is correct.

## Setting up an Amazon S3 bucket to host a targeted PyPI/simple repo

This example sets up a PyPI mirror in Amazon S3 for a set of packages and their dependencies.

To set up the PyPI mirror for a set of packages:

```
# pip download all the dependencies
pip download -d s3pypi --only-binary :all: plotly gglplot
pip download -d s3pypi --platform manylinux_2_17_x86_64 --only-binary :all: psycopg2-binary
# create and upload the pypi/simple index and wheel files to the s3 bucket
s3pypi -b test-domain-name --put-root-index -v s3pypi/*
```

If you already have an existing artifact repository, it will have an index URL for pip's use that you can provide in place of the example URL for the Amazon S3 bucket as above.

To use the custom index-url, with some example packages:

```
%%configure
{
    "--additional-python-modules": "psycopg2_binary==2.9.5",
    "python-modules-installer-option": "--no-cache-dir --verbose --index-url https://test-domain-name.s3.amazonaws.com/ --trusted-host test-domain-name.s3.amazonaws.com"
}
```

## Setting up a CodeArtifact mirror of pypi attached to your VPC

To set up a mirror:

1. Create a repository in the same region as the subnet used by the connector.

Select `Public upstream repositories` and choose `pypi-store`. 2. Provide access to the repository from the VPC for the subnet. 3. Specify the correct `--index-url` using the `python-modules-installer-option`.

```
%%configure
{
    "--additional-python-modules": "psycopg2_binary==2.9.5",
    "python-modules-installer-option": "--no-cache-dir --verbose --index-url https://test-domain-name.s3.amazonaws.com/ --trusted-host test-domain-name.s3.amazonaws.com"
}
```

For more information, see [Use CodeArtifact from a VPC](../../../codeartifact/latest/ug/use-codeartifact-from-vpc.md "../../../codeartifact/latest/ug/use-codeartifact-from-vpc.md").
