# Amazon Linux 2 notebook instances

###### Important

On June 30, 2026, Amazon Linux 2 reaches end of support for notebook instances. Existing
in-service instances may continue to function but will not receive security updates
or bug fixes. Starting July 1, 2026, you can no longer create new or restart stopped
AL2 notebook instances. JupyterLab 1 and JupyterLab 3 have been deprecated since
June 30, 2025. For more information, see [JupyterLab version maintenance](nbi-jl.md#nbi-jl-version-maintenance "nbi-jl.md#nbi-jl-version-maintenance").

Amazon Linux 2 is vulnerable to CVE-2026-24747, a security issue in PyTorch versions prior
to 2.10.0 that cannot be patched on AL2 because of operating system constraints.

As of May 15, 2026, `notebook-al2023-v1` is the default platform for all
new notebook instances. We strongly recommend upgrading to AL2023
(`notebook-al2023-v1`) for continued support. To learn more, see
[AL2023 notebook instances](nbi-al2023.md "nbi-al2023.md").

From August 1, 2026 onward, Amazon SageMaker AI will begin upgrading remaining AL2 notebook
instances to AL2023 in phases to ensure continued security and compatibility. The
following platforms will be upgraded:

- `notebook-al2-v1` (JupyterLab 1)
- `notebook-al2-v2` (JupyterLab 3)
- `notebook-al2-v3` (JupyterLab 4)
  Amazon SageMaker notebook instances support Amazon Linux 2 (AL2) operating systems. Amazon Linux 2 is
  deprecated as of July 1, 2026. We recommend that you use AL2023 for all new notebook
  instances.

SageMaker AI supports notebook instances based on the following Amazon Linux 2 operating systems.

- notebook-al2-v1 (deprecated): These notebook instances supported
  JupyterLab version 1. As of June 30, 2025, you can no longer create new instances with this platform identifier. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").
- notebook-al2-v2 (deprecated): These notebook instances supported
  JupyterLab version 3. As of June 30, 2025, you can no longer create new instances with this platform identifier. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").
- notebook-al2-v3 (deprecating July 1, 2026): These notebook instances support
  JupyterLab version 4. As of May 15, 2026, AL2023 is the default platform for
  all new notebook instances. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").
  Notebook instances created before 08/18/2021 automatically run on Amazon Linux (AL1). Notebook
  instances based on AL1 entered a maintenance phase as of 12/01/2022 and are no longer
  available for new notebook instance creation as of 02/01/2023. To replace AL1, you now have
  the option to create Amazon SageMaker notebook instances with AL2023. For more information, see [AL1 Maintenance Phase Plan](#nbi-al2-deprecation "#nbi-al2-deprecation").

###### Topics

- [Supported instance types](#nbi-al2-instances "#nbi-al2-instances")
- [Available kernels](#nbi-al2-kernel "#nbi-al2-kernel")
- [AL2 Maintenance Phase Plan](#nbi-al2-end-of-support "#nbi-al2-end-of-support")
- [AL1 Maintenance Phase Plan](#nbi-al2-deprecation "#nbi-al2-deprecation")

## Supported instance types

Amazon Linux 2 supports instance types listed under **Notebook Instances** in
[Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/") with the
exception that Amazon Linux 2 does not support `ml.p2` instances.

## Available kernels

The following table gives information about the available kernels for SageMaker notebook
instances. All of these images are supported on notebook instances based on the
`notebook-al2-v1`, `notebook-al2-v2`, and
`notebook-al2-v3` operating systems.

SageMaker notebook instance kernels

| Kernel name              | Description                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R                        | A kernel used to perform data analysis and visualization using R code<br>from a Jupyter notebook.                                                                                     |
| Sparkmagic (PySpark)     | A kernel used to do data science with remote Spark clusters from<br>Jupyter notebooks using the Python programming language. This kernel<br>comes with Python 3.10.                   |
| Sparkmagic (Spark)       | A kernel used to do data science with remote Spark clusters from<br>Jupyter notebooks using the Scala programming language. This kernel<br>comes with Python 3.10.                    |
| Sparkmagic (SparkR)      | A kernel used to do data science with remote Spark clusters from<br>Jupyter notebooks using the R programming language. This kernel comes<br>with Python 3.10.                        |
| conda\_python3           | A conda environment that comes pre-installed with popular packages<br>for data science and machine learning. This kernel comes with Python<br>3.10.                                   |
| conda\_pytorch\_p310     | A conda environment that comes pre-installed with PyTorch version<br>2.2.0, as well as popular data science and machine learning packages.<br>This kernel comes with Python 3.10.     |
| conda\_tensorflow2\_p310 | A conda environment that comes pre-installed with TensorFlow version<br>2.16.0, as well as popular data science and machine learning packages.<br>This kernel comes with Python 3.10. |

## AL2 Maintenance Phase Plan

The following table is a timeline for the Amazon Linux 2 end of support on notebook instances.

| Date           | Description                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ |
| May 15, 2026   | The default platform identifier for new notebook instances changes<br>from `notebook-al2-v3` to<br>`notebook-al2023-v1`. |
| June 30, 2026  | AL2 reaches end of support. AL2 notebook instances no longer<br>receive security updates or bug fixes.                   |
| July 1, 2026   | AL2 notebook instances can no longer be created or restarted.                                                            |
| August 1, 2026 | Amazon SageMaker AI begins upgrading remaining AL2 notebook instances to<br>AL2023 in phases.                            |

### Migrating from Amazon Linux 2 to AL2023

If you have existing notebook instances running on Amazon Linux 2 (`notebook-al2-v1`,
`notebook-al2-v2`, or `notebook-al2-v3`), migrate them to AL2023
before July 1, 2026.

Migration is an in-place platform update. Your EBS volume data (notebooks, datasets,
custom files in `/home/ec2-user/SageMaker/`) is preserved.

#### To migrate a notebook instance to AL2023

1. Stop your notebook instance.
2. Call [UpdateNotebookInstance](../APIReference/API_UpdateNotebookInstance.md "../APIReference/API_UpdateNotebookInstance.md") with `PlatformIdentifier` set to
   `notebook-al2023-v1`. Or, in the SageMaker AI console, edit the notebook
   instance and change the **Platform identifier** to
   `notebook-al2023-v1`.
3. Start your notebook instance.
4. Verify your lifecycle configuration scripts and custom environments work
   correctly.

#### Important differences between Amazon Linux 2 and AL2023

- Package manager: `yum` (Amazon Linux 2) → `dnf` (AL2023)
- PyTorch version: 2.6.0 (Amazon Linux 2) → 2.10.0 (AL2023)
- Unsupported instance types: `ml.p2` (Amazon Linux 2) → `ml.p2`,
  `ml.p3`, `ml.p3dn`, `ml.inf1`, `ml.g3`
  (AL2023)

#### Lifecycle configuration script updates

If your notebook instance uses a lifecycle configuration script, update any
`yum` commands to use `dnf`. For example:

```

# AL2 (old)
sudo yum install -y htop

# AL2023 (new)
sudo dnf install -y htop
```

For a detailed comparison of Amazon Linux 2 and AL2023, see [Comparing AL2 and AL2023](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the
_Amazon Linux 2023 User Guide_.

## AL1 Maintenance Phase Plan

The following table is a timeline for when AL1 entered its extended maintenance phase.
The AL1 maintenance phase also coincides with the deprecation of Python 2 and Chainer.
Notebooks based on AL2 do not have managed Python 2 and Chainer kernels.

| Date       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 08/18/2021 | Notebook instances based on AL2 are launched. Newly launched<br>notebook instances still default to AL1. AL1 is supported with<br>security patches and updates, but no new features. You can choose<br>between the two operating systems when launching a new notebook<br>instance.                                                                                                                                                                                                  |
| 10/31/2022 | The default platform identifier for SageMaker notebook instances<br>changes from Amazon Linux (al1-v1) to Amazon Linux 2 (al2-v2). You can choose between<br>the two operating systems when launching a new notebook<br>instance.                                                                                                                                                                                                                                                    |
| 12/01/2022 | AL1 is no longer supported with non-critical security patches and<br>updates. AL1 still receives fixes for [critical](https://nvd.nist.gov/vuln-metrics/cvss# "https://nvd.nist.gov/vuln-metrics/cvss#")<br>security-related issues. You can still launch instances on AL1, but<br>assume the risks associated with using an unsupported operating<br>system.                                                                                                                        |
| 02/01/2023 | AL1 is no longer an available option for new notebook instance<br>creation. After this date, customers can create notebook instances<br>with the AL2 platform identifiers. Existing notebooks with an<br>`INSERVICE` status should be migrated to the latest<br>platform since continuous availability of AL1 notebook instances<br>cannot be guaranteed.                                                                                                                            |
| 03/31/2024 | AL1 reaches its end of life on notebook instances on March 31,<br>2024. After this date, AL1 will no longer receive any security<br>updates, bug fixes, or be available for new notebook instance<br>creation.<br>• Existing AL1 notebook instances with a<br>`STOPPED` status cannot be restarted.<br>• Existing notebooks with an `INSERVICE` status<br>should be migrated to the latest platform since continuous availability<br>of AL1 notebook instances cannot be guaranteed. |

### Migrating from AL1

Your existing AL1 notebook instance is not automatically migrated to AL2023. To
upgrade, you must create a new notebook instance with
`notebook-al2023-v1`, replicate your code and environment, and delete
your old notebook instance.
