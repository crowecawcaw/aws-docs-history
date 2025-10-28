# Amazon Linux 2 notebook instances

###### Important

JupyterLab 1 and JupyterLab 3 are no longer supported as of June 30, 2025. You can no longer create new or restart stopped notebook instances using these versions. Existing in-service instances may continue to function but will not receive security updates or bug fixes. Migrate to JupyterLab 4 notebook instances for continued support. For more information, see [JupyterLab version maintenance](nbi-jl.md#nbi-jl-version-maintenance "nbi-jl.md#nbi-jl-version-maintenance").

###### Note

AL2023 is the latest and recommended operating system available for notebook instances.
To learn more, see [AL2023 notebook instances](nbi-al2023.md "nbi-al2023.md").

Amazon SageMaker notebook instances currently support Amazon Linux 2 (AL2) operating systems. You can
select the operating system that your notebook instance is based on when you create the
notebook instance.

SageMaker AI supports notebook instances based on the following Amazon Linux 2 operating systems.

- notebook-al2-v1 (deprecated): These notebook instances supported
  JupyterLab version 1. As of June 30, 2025, you can no longer create new instances with this platform identifier. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").
- notebook-al2-v2 (deprecated): These notebook instances supported
  JupyterLab version 3. As of June 30, 2025, you can no longer create new instances with this platform identifier. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").
- notebook-al2-v3: These notebook instances support
  JupyterLab version 4. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").
  Notebook instances created before 08/18/2021 automatically run on Amazon Linux (AL1). Notebook
  instances based on AL1 entered a maintenance phase as of 12/01/2022 and are no longer
  available for new notebook instance creation as of 02/01/2023. To replace AL1, you now have
  the option to create Amazon SageMaker notebook instances with AL2. For more information, see [AL1 Maintenance Phase Plan](#nbi-al2-deprecation "#nbi-al2-deprecation").

###### Topics

- [Supported instance types](#nbi-al2-instances "#nbi-al2-instances")
- [Available Kernels](#nbi-al2-kernel "#nbi-al2-kernel")
- [AL1 Maintenance Phase Plan](#nbi-al2-deprecation "#nbi-al2-deprecation")

## Supported instance types

Amazon Linux 2 supports instance types listed under **Notebook Instances** in
[Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") with the
exception that Amazon Linux 2 does not support `ml.p2` instances.

## Available Kernels

The following table gives information about the available kernels for SageMaker notebook
instances. All of these images are supported on notebook instances based on the
`notebook-al2-v1`, `notebook-al2-v2`, and
`notebook-al2-v3` operating systems.

SageMaker notebook instance kernels

| Kernel name            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R                      | A kernel used to perform data analysis and visualization using R code from a Jupyter notebook.                                                                                                                                                                                                                                                                                                                                                                       |
| Sparkmagic (PySpark)   | A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Python programming language. This kernel comes with Python 3.10.                                                                                                                                                                                                                                                                                                        |
| Sparkmagic (Spark)     | A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Scala programming language. This kernel comes with Python 3.10.                                                                                                                                                                                                                                                                                                         |
| Sparkmagic (SparkR)    | A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the R programming language. This kernel comes with Python 3.10.                                                                                                                                                                                                                                                                                                             |
| conda_python3          | A conda environment that comes pre-installed with popular packages for data science and machine learning. This kernel comes with Python 3.10.                                                                                                                                                                                                                                                                                                                        |
| conda_pytorch_p310     | A conda environment that comes pre-installed with PyTorch version 2.2.0, as well as popular data science and machine learning packages. This kernel comes with Python 3.10.                                                                                                                                                                                                                                                                                          |
| conda_tensorflow2_p310 | A conda environment that comes pre-installed with TensorFlow version 2.16.0, as well as popular data science and machine learning packages. This kernel comes with Python 3.10.                                                                                                                                                                                                                                                                                      | ## AL1 Maintenance Phase Plan The following table is a timeline for when AL1 entered its extended maintenance phase. The AL1 maintenance phase also coincides with the deprecation of Python 2 and Chainer. Notebooks based on AL2 do not have managed Python 2 and Chainer kernels.                                                                                                                                                                                                                                                                                                                                        |
| Date                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 08/18/2021             | Notebook instances based on AL2 are launched. Newly launched notebook instances still default to AL1. AL1 is supported with security patches and updates, but no new features. You can choose between the two operating systems when launching a new notebook instance.                                                                                                                                                                                              |
| 10/31/2022             | The default platform identifier for SageMaker notebook instances changes from Amazon Linux (al1-v1) to Amazon Linux 2 (al2-v2). You can choose between the two operating systems when launching a new notebook instance.                                                                                                                                                                                                                                             |
| 12/01/2022             | AL1 is no longer supported with non-critical security patches and updates. AL1 still receives fixes for [critical](https://nvd.nist.gov/vuln-metrics/cvss# "https://nvd.nist.gov/vuln-metrics/cvss#") security-related issues. You can still launch instances on AL1, but assume the risks associated with using an unsupported operating system.                                                                                                                    |
| 02/01/2023             | AL1 is no longer an available option for new notebook instance creation. After this date, customers can create notebook instances with the AL2 platform identifiers. Existing notebooks with an `INSERVICE` status should be migrated to the latest platform since continuous availability of AL1 notebook instances cannot be guaranteed.                                                                                                                           |
| 03/31/2024             | AL1 reaches its end of life on notebook instances on March 31, 2024. After this date, AL1 will no longer receive any security updates, bug fixes, or be available for new notebook instance creation. <br>• Existing AL1 notebook instances with a `STOPPED` status cannot be restarted. <br>• Existing notebooks with an `INSERVICE` status should be migrated to the latest platform since continuous availability of AL1 notebook instances cannot be guaranteed. | ### Migrating to Amazon Linux 2 Your existing AL1 notebook instance is not automatically migrated to Amazon Linux 2. To upgrade your AL1 notebook instance to Amazon Linux 2, you must create a new notebook instance, replicate your code and environment, and delete your old notebook instance. For more information, see the [Amazon Linux 2 migration blog](https://aws.amazon.com/blogs/machine-learning/migrate-your-work-to-amazon-sagemaker-notebook-instance-with-amazon-linux-2/ "https://aws.amazon.com/blogs/machine-learning/migrate-your-work-to-amazon-sagemaker-notebook-instance-with-amazon-linux-2/ "). |
