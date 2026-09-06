# Using Python virtual environments with AWS Glue

Starting with AWS Glue 5.0, you can run your ETL jobs in a Python virtual environment (venv). Virtual
environments remove runtime dependency resolution from your job runs, ensure that each run uses the
same packages, and prevent failures caused by upstream package changes.

AWS Glue supports two ways to use a virtual environment:

- **Service-generated virtual environment** – Available in
  AWS Glue 6.0 and later. You add the `--python-virtual-env-storage-prefix` parameter, and
  AWS Glue builds the virtual environment for you and caches it in Amazon S3 for later job runs. No local
  build is required.
- **Manually built virtual environment** – Available in
  AWS Glue 5.0 and later. You build the virtual environment on your local machine or in a CI/CD
  pipeline, upload it to Amazon S3, and reference it with the `--python-virtual-env`
  parameter.

This topic describes how to migrate jobs that use `--additional-python-modules` to either
approach. For information about other methods of managing Python dependencies, see
[Using Python libraries with AWS Glue](aws-glue-programming-python-libraries.md "aws-glue-programming-python-libraries.md").

## Key differences from --additional-python-modules

The following table compares `--additional-python-modules` with a manually built
virtual environment.

| Feature                                                     | `--additional-python-modules`                       | `--python-virtual-env`                                             |
| ----------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------ |
| Base container libraries (boto3, numpy, pandas, and others) | Available automatically                             | Not available. You must include all required packages in the venv. |
| Dependency resolution                                       | Occurs at runtime                                   | Occurs at build time on your machine                               |
| Runtime isolation                                           | Partial. Packages install on top of base libraries. | Full. Replaces the Python environment entirely.                    |

###### Important

When you migrate to `--python-virtual-env`, you must include every Python package
that your job needs in the virtual environment. This includes packages that were previously
available from the AWS Glue base container, such as boto3, numpy, and pandas. These packages are no
longer implicitly available.

## Choosing an approach

Use the following table to decide which approach fits your job.

| Scenario                                                                                 | Recommended approach                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Simple jobs with few pip packages, where you want no build overhead                      | Service-generated venv (add `--python-virtual-env-storage-prefix`).<br>Requires AWS Glue 6.0 or later.                                                                                                                                                                                     |
| Complex dependency trees, full reproducibility, or a CI/CD pipeline that builds the venv | Manually built venv (`--python-virtual-env`). Requires AWS Glue 5.0 or<br>later.                                                                                                                                                                                                           |
| Migrating from `--additional-python-modules` with minimal changes                        | Service-generated venv (add<br>`--python-virtual-env-storage-prefix`). Requires AWS Glue 6.0 or later. On AWS Glue 5.0<br>and 5.1, use a manually built virtual environment instead.                                                                                                       |
| Private PyPI index with custom packages                                                  | Either approach. The service-generated venv requires AWS Glue 6.0 or later and works<br>with [--python-modules-installer-option](aws-glue-programming-etl-glue-arguments.md#python-modules-installer-option "aws-glue-programming-etl-glue-arguments.md#python-modules-installer-option"). |

## Using a service-generated virtual environment with Amazon S3 caching

Starting with AWS Glue 6.0, you can use the `--python-virtual-env-storage-prefix`
parameter to have AWS Glue build the virtual environment and cache it in Amazon S3. This approach combines
the simplicity of `--additional-python-modules` with the performance benefit of a cached
virtual environment.

### How it works

When you provide `--python-virtual-env-storage-prefix`, AWS Glue does the following:

- **On the first run (cache miss)** – AWS Glue creates a
  virtual environment with `--system-site-packages`, which inherits container
  packages such as numpy, pandas, and pyarrow. AWS Glue then installs the packages from
  [--additional-python-modules](aws-glue-programming-etl-glue-arguments.md#additional-python-modules "aws-glue-programming-etl-glue-arguments.md#additional-python-modules") with pip, packages the virtual environment as a
  `.tar.gz` file, and uploads it to your Amazon S3 prefix for later reuse.
- **On later runs (cache hit)** – AWS Glue downloads the
  cached `.tar.gz` file from Amazon S3, extracts it, and configures the Spark
  driver and executors to use the virtual environment. No pip installation occurs.

### Differences from a manually built virtual environment

The following table compares the service-generated virtual environment with the manually
built approach.

| Feature              | Service-generated venv                                                | Manually built venv                                            |
| -------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- |
| Build responsibility | AWS Glue builds the venv automatically                                | You build the venv in Docker                                   |
| Container packages   | Inherited through `--system-site-packages`                            | You must include all packages explicitly                       |
| First-run latency    | Additional time for pip installation, packaging, and Amazon S3 upload | None, because the venv is pre-built                            |
| Later-run latency    | Additional time for Amazon S3 download and extraction                 | Additional time for Amazon S3 download and extraction          |
| Determinism          | We recommend that you pin package versions                            | Fully deterministic, because versions are locked at build time |
| PyPI access          | Required on the first run                                             | Not required, because the venv is built offline                |

### Configuring a service-generated virtual environment

The `--python-virtual-env-storage-prefix` parameter specifies the Amazon S3 location
where AWS Glue stores the virtual environment that it builds, in the form
`s3://`path`/`. AWS Glue caches the virtual environment at this
prefix on the first job run and reuses it on later runs.

To enable a service-generated virtual environment, add the
`--python-virtual-env-storage-prefix` parameter to your job and keep your existing
`--additional-python-modules` parameter.

```
"--additional-python-modules": "requests==2.32.3,scikit-learn==1.5.0"
"--python-virtual-env-storage-prefix": "s3://`amzn-s3-demo-bucket`/venv-cache/"
```

You can also use the following optional parameters:

- `--python-virtual-env-version` – A version identifier for the cached
  virtual environment. Change this value to invalidate the cache and force AWS Glue to rebuild the
  virtual environment. The value is a string, so you can use whichever versioning scheme suits
  your workflow, such as an incrementing number, a date, or a build identifier. The default
  value is `0`.
- [--python-modules-installer-option](aws-glue-programming-etl-glue-arguments.md#python-modules-installer-option "aws-glue-programming-etl-glue-arguments.md#python-modules-installer-option") – Pass options to pip, such as
  `--no-deps` or `--index-url`.

To enable caching for an existing job, add the storage prefix parameter. The first run takes
longer because AWS Glue builds and uploads the virtual environment, but later runs use the cached
virtual environment and perform no pip resolution.

```
# Before
"--additional-python-modules": "requests==2.32.3"

# After
"--additional-python-modules": "requests==2.32.3"
"--python-virtual-env-storage-prefix": "s3://`amzn-s3-demo-bucket`/venv-cache/"
```

### How AWS Glue caches the virtual environment

AWS Glue keys the cache by your job configuration. The configuration includes the modules from
`--additional-python-modules`, the value of
`--python-modules-installer-option`, the AWS Glue version, and the value of
`--python-virtual-env-version`.

An unchanged configuration results in a cache hit. If you change any of these values, AWS Glue
builds a new virtual environment and creates a new cache entry.

AWS Glue stores each cached virtual environment under a separate key in your storage prefix.
Jobs that use the same modules and installer options share the same cache entry.

### Limitations

- Requires AWS Glue 6.0 or later.
- The first run requires access to PyPI, or to your private index, for dependency
  resolution.
- Container packages such as numpy and pandas are inherited but not version-pinned. If your
  job requires exact versions of container packages, use `--python-virtual-env`
  instead.
- The cache is keyed by configuration. Changing any module or version creates a new cache
  entry, and earlier entries remain in Amazon S3 until you remove them.

## Building your own virtual environment

In AWS Glue 5.0 and later, you can build a virtual environment yourself and reference it with the
`--python-virtual-env` parameter. Use this approach when you need full reproducibility,
exact versions of container packages, or a build that runs in a CI/CD pipeline.

### Prerequisites

Before you begin, make sure that you have the following:

- [Docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/") from the
  Docker website, installed on your local machine, so that you can build the
  virtual environment in an AWS Glue-compatible environment
- An Amazon S3 bucket to upload the packaged virtual environment
- The AWS CLI configured with permissions to upload to Amazon S3 and update AWS Glue job
  parameters

For Python version and platform compatibility details for each AWS Glue version, see
[Appendix B: AWS Glue environment details](aws-glue-programming-python-libraries.md#glue-python-libraries-environment-details "aws-glue-programming-python-libraries.md#glue-python-libraries-environment-details").

### Step 1: Create your requirements files

Create two requirements files that define the packages for your virtual environment.

1. Download `base-requirements.txt` for your AWS Glue version from the
   aws-glue-libs repository on the GitHub website. This file
   lists the packages that the standard AWS Glue container provides. For the same list in this
   guide, see [Python modules already provided in AWS Glue](aws-glue-programming-python-libraries.md#glue-modules-provided "aws-glue-programming-python-libraries.md#glue-modules-provided").

   - AWS Glue 5.0 – [base-requirements.txt](https://raw.githubusercontent.com/awslabs/aws-glue-libs/glue-5.0/base-requirements.txt "https://raw.githubusercontent.com/awslabs/aws-glue-libs/glue-5.0/base-requirements.txt") on the GitHub
     website
   - AWS Glue 5.1 – [base-requirements.txt](https://raw.githubusercontent.com/awslabs/aws-glue-libs/glue-5.1/base-requirements.txt "https://raw.githubusercontent.com/awslabs/aws-glue-libs/glue-5.1/base-requirements.txt") on the GitHub
     website
   - AWS Glue 6.0 – [base-requirements.txt](https://raw.githubusercontent.com/awslabs/aws-glue-libs/main/base-requirements.txt "https://raw.githubusercontent.com/awslabs/aws-glue-libs/main/base-requirements.txt") on the GitHub
     website

2. Create `additional-requirements.txt`. Add the packages from your existing
   `--additional-python-modules` parameter, one per line. For example:

```
cryptography
requests-oauthlib
sqlalchemy
```

###### Important

If your job uses the AWS Glue Python library, such as `GlueContext` or
`DynamicFrame`, you must also include the
[AWSGlueDataplanePython](https://pypi.org/project/AWSGlueDataplanePython/ "https://pypi.org/project/AWSGlueDataplanePython/")
package from the PyPI website. Use the version that matches your AWS Glue version,
as shown in the following table.

| AWS Glue version | Package version                 |
| ---------------- | ------------------------------- |
| 5.0              | `AWSGlueDataplanePython==5.0.0` |
| 5.1              | `AWSGlueDataplanePython==5.1.0` |
| 6.0              | `AWSGlueDataplanePython==6.0.0` |

### Step 2: Create a Dockerfile

Create a Dockerfile that matches the environment of your target AWS Glue version. For platform
and Python version details, see
[Appendix B: AWS Glue environment details](aws-glue-programming-python-libraries.md#glue-python-libraries-environment-details "aws-glue-programming-python-libraries.md#glue-python-libraries-environment-details").

AWS Glue 5.0 and 5.1 use Python 3.11 on Amazon Linux 2023.

```
FROM --platform=linux/amd64 public.ecr.aws/amazonlinux/amazonlinux:2023-minimal

RUN dnf install -y python3.11 zip && \
    dnf clean all

WORKDIR /build
```

AWS Glue 6.0 uses Python 3.13 on Amazon Linux 2023.

```
FROM --platform=linux/amd64 public.ecr.aws/amazonlinux/amazonlinux:2023-minimal

RUN dnf install -y python3.13 zip && \
    dnf clean all

WORKDIR /build
```

### Step 3: Build and start the container

Build the Docker image. Then start a container with your requirements files and job script mounted.

```
docker build --platform linux/amd64 -t glue-venv-builder .

docker run --platform linux/amd64 \
  -v $(pwd)/base-requirements.txt:/working_dir/base-requirements.txt:ro \
  -v $(pwd)/additional-requirements.txt:/working_dir/additional-requirements.txt:ro \
  -v $(pwd)/my_glue_script/:/working_dir/my_glue_script/:ro \
  -v $(pwd):/output \
  -w /working_dir \
  -it glue-venv-builder bash
```

This command mounts your requirements files and your AWS Glue job script directory. The following
step uses the script directory for import analysis.

### Step 4: Build a temporary venv and discover required packages

Inside the container, build a temporary venv that mirrors the AWS Glue runtime. Then use static
analysis to find the minimal set of packages your job needs.

For AWS Glue 5.0 and 5.1, which use Python 3.11, run the following commands.

```
# Create a temporary venv to reproduce the AWS Glue runtime environment
python3.11 -m venv temp_venv
source temp_venv/bin/activate

python3.11 -m pip install --upgrade pip

# Install base container libraries (mirrors what the AWS Glue container provides)
python3.11 -m pip install -r base-requirements.txt

# Install additional Python modules on top (mirrors how AWS Glue installs them at runtime)
python3.11 -m pip install -r additional-requirements.txt

# Freeze the full resolved environment
pip freeze > full-requirements.txt

# Install analysis tools
python3.11 -m pip install pipreqs pip-tools

# Use pipreqs to discover what the script actually imports
# --mode no-pin outputs package names without versions
pipreqs --mode no-pin --savepath discovered-requirements.txt /working_dir/my_glue_script

# Remove packages provided by the Spark runtime
sed -i '/pyspark/d' discovered-requirements.txt
sed -i '/py4j/d' discovered-requirements.txt

# Remove awsglue - install AWSGlueDataplanePython in Step 5 instead
sed -i '/awsglue/d' discovered-requirements.txt

# Use pip-compile to resolve the full dependency tree of the discovered packages,
# constrained to the versions from the temporary venv
pip-compile discovered-requirements.txt -c full-requirements.txt -o final-requirements.txt

echo "=== Final requirements.txt ==="
cat final-requirements.txt

# Deactivate and discard the temporary venv
deactivate
rm -rf temp_venv
```

For AWS Glue 6.0, which uses Python 3.13, run the following commands.

```
# Create a temporary venv to reproduce the AWS Glue runtime environment
python3.13 -m venv temp_venv
source temp_venv/bin/activate

python3.13 -m pip install --upgrade pip

# Install base container libraries (mirrors what the AWS Glue container provides)
python3.13 -m pip install -r base-requirements.txt

# Install additional Python modules on top (mirrors how AWS Glue installs them at runtime)
python3.13 -m pip install -r additional-requirements.txt

# Freeze the full resolved environment
pip freeze > full-requirements.txt

# Install analysis tools
python3.13 -m pip install pipreqs pip-tools

# Use pipreqs to discover what the script actually imports
# --mode no-pin outputs package names without versions
pipreqs --mode no-pin --savepath discovered-requirements.txt /working_dir/my_glue_script

# Remove packages provided by the Spark runtime
sed -i '/pyspark/d' discovered-requirements.txt
sed -i '/py4j/d' discovered-requirements.txt

# Remove awsglue - install AWSGlueDataplanePython in Step 5 instead
sed -i '/awsglue/d' discovered-requirements.txt

# Use pip-compile to resolve the full dependency tree of the discovered packages,
# constrained to the versions from the temporary venv
pip-compile discovered-requirements.txt -c full-requirements.txt -o final-requirements.txt

echo "=== Final requirements.txt ==="
cat final-requirements.txt

# Deactivate and discard the temporary venv
deactivate
rm -rf temp_venv
```

###### Note

Review `final-requirements.txt` to verify that it looks correct. If your job uses dynamic
imports or conditional imports, pipreqs might not detect them. Add those packages to the file manually.

### Step 5: Build the production venv

Create the final venv with only the packages your job needs. Then package it as a tarball.

For AWS Glue 5.0 and 5.1, which use Python 3.11, run the following commands.

```
python3.11 -m venv pyspark_venv
source pyspark_venv/bin/activate

python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r final-requirements.txt

# Install the AWS Glue Python library that matches your AWS Glue version (see the version
# table in Step 1). Use 5.0.0 for AWS Glue 5.0, or 5.1.0 for AWS Glue 5.1.
python3.11 -m pip install AWSGlueDataplanePython==`5.0.0`

python3.11 -m pip install venv-pack
venv-pack -f -o pyspark_venv.tar.gz

cp pyspark_venv.tar.gz /output/
exit
```

For AWS Glue 6.0, which uses Python 3.13, run the following commands.

```
python3.13 -m venv pyspark_venv
source pyspark_venv/bin/activate

python3.13 -m pip install --upgrade pip
python3.13 -m pip install -r final-requirements.txt

# Install the AWS Glue Python library (see version table in Step 1)
python3.13 -m pip install AWSGlueDataplanePython==6.0.0

python3.13 -m pip install venv-pack
venv-pack -f -o pyspark_venv.tar.gz

cp pyspark_venv.tar.gz /output/
exit
```

### Step 6: Upload to Amazon S3

Upload the packaged virtual environment to your Amazon S3 bucket.

```
aws s3 cp pyspark_venv.tar.gz s3://`amzn-s3-demo-bucket`/`path`/pyspark_venv.tar.gz
```

### Step 7: Update job parameters

Update your AWS Glue job configuration to use `--python-virtual-env` instead of
`--additional-python-modules`.

Remove the `--additional-python-modules` parameter and add the
`--python-virtual-env` parameter pointing to your uploaded tarball.

```
# Before
"--additional-python-modules": "cryptography"

# After (remove --additional-python-modules entirely)
"--python-virtual-env": "s3://`amzn-s3-demo-bucket`/`path`/pyspark_venv.tar.gz"
```

## Automating the migration with Kiro

If you prefer an automated approach, you can use
[Kiro](https://kiro.dev "https://kiro.dev"), available on the Kiro
website, to run the migration described in
[Building your own virtual environment](#python-venv-migration-procedure "#python-venv-migration-procedure")
from the command line. With a Kiro skill, Kiro analyzes your AWS Glue job
configuration, builds the virtual environment in Docker, and produces the packaged
tarball.

### How it works

When you ask Kiro to migrate your AWS Glue job from `--additional-python-modules` to
`--python-virtual-env`, Kiro does the following:

1. Extracts the AWS Glue version, the value of `--additional-python-modules`, and
   your job script from your request.
2. Retrieves the base container module list for your AWS Glue version from the AWS Glue
   documentation.
3. Creates the build artifacts in a working directory, including
   `base-requirements.txt`,
   `additional-requirements.txt`, a Dockerfile, and a build script.
4. Builds the Docker image for an AWS Glue-compatible environment.
5. Runs the discovery and packaging workflow in a non-interactive container.
6. Produces `pyspark_venv.tar.gz`, prompts you for an Amazon S3 destination,
   and uploads the tarball.
7. Shows you the updated job parameters.

### Example request

Provide your AWS Glue version, your additional Python modules, and your job script. For
example:

```
I have a Glue 5.1 job with the following:
--additional-python-modules: ephem, awscli

Glue job script:
import awscli
import ephem

Help me migrate to using --python-virtual-env.
```

### Getting the Kiro skill

The `venv-migration` skill file is maintained in the
aws-glue-libs repository rather than in this guide. For the skill file and
installation instructions, see [venv-migration skill](https://github.com/awslabs/aws-glue-libs/blob/main/.kiro/skills/venv-migration/skill.md "https://github.com/awslabs/aws-glue-libs/blob/main/.kiro/skills/venv-migration/skill.md") on the GitHub
website.

### Limitations

- Kiro requires Docker to be available in the command line environment.
- Dynamic imports and conditional imports that are not visible in your script source are
  not detected automatically. Review the generated
  `final-requirements.txt` file and add any missing packages
  manually.
- If your job uses a private pip index with `--index-url`, you must configure
  network access to that index in the Docker container.
- Pip conflicts during the build might require manual resolution. For more information,
  see [Troubleshooting](#python-venv-troubleshooting "#python-venv-troubleshooting").

## Troubleshooting

Use the following sections to resolve common issues when using Python virtual environments
with AWS Glue.

### Resolving pip version conflicts

A pip version conflict means that two packages require incompatible versions of the same
dependency. To find and fix the conflict, do the following:

1. Read the pip error output. When resolution fails outright, the output names each
   conflicting requirement and the package that introduced it.
2. Preview what pip would resolve without installing anything. Add `--dry-run
 --report install-report.json` to your install command, as in the following
   example.

```
pip install -r additional-requirements.txt --dry-run --report install-report.json
```

3. Inspect `install-report.json`. The report lists every package that
   pip selected, which reveals silent downgrades.
4. Relax the version pins on non-critical packages, or remove the constraints.

### Resolving ModuleNotFoundError

This error indicates that your virtual environment does not include a required package.
Common causes include the following:

- You did not include a base container library that your job requires. A manually built
  virtual environment does not inherit packages from the AWS Glue container.
- Your job uses a dynamic import that pipreqs could not detect during static analysis.
- Your job requires a PySpark dependency on executor nodes.

To resolve this issue, add the missing package and rebuild the virtual environment. The
steps depend on which approach your job uses.

- **Manually built venv** – Add the package to
  `final-requirements.txt`, then rebuild the virtual environment and
  upload it again.
- **Service-generated venv** – Add the package to
  `--additional-python-modules`. The new module list changes the cache key, so
  AWS Glue builds a new virtual environment on the next job run.

### Reducing venv tarball size

If your packaged virtual environment is too large, reduce its size with the following approaches:

- Remove unnecessary packages that your script does not import, such as test frameworks
  and development tools.
- Use `pip install --no-deps` for packages where you want to control transitive
  dependencies manually.
- Include only the packages that your script directly imports, and let pip-compile resolve
  the minimum required transitive dependencies.

### Resolving platform compatibility errors

These errors occur when packages in the venv were built for a different operating system or architecture.
To avoid these errors:

- Always build the virtual environment inside a Docker container using the
  `--platform linux/amd64` flag.
- Verify that wheel platform tags match your target AWS Glue version. For example, AWS Glue 5.0
  and 5.1 require `manylinux2014_x86_64` or compatible platform tags.
- Do not build the virtual environment directly on macOS or Windows without Docker.
