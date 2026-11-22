

# AL2023 notebook instances

SageMaker AI notebook instances support AL2023 operating systems. You can select the operating system that your notebook instance is based on when you create the notebook instance.

SageMaker AI supports notebook instances based on the following AL2023 operating systems.

`notebook-al2023-v1`  
These notebook instances support JupyterLab version 4. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md).

`notebook-al2023-v2`  
These notebook instances support JupyterLab version 4 and come with Python 3.12. For the differences from `notebook-al2023-v1`, see [Differences between notebook-al2023-v1 and notebook-al2023-v2](#nbi-al2023-v2-differences).

**Topics**
+ [Supported instance types](#nbi-al2023-instances)
+ [Available kernels](#nbi-al2023-kernel)
+ [Differences between notebook-al2023-v1 and notebook-al2023-v2](#nbi-al2023-v2-differences)

## Supported instance types
<a name="nbi-al2023-instances"></a>

AL2023 supports instance types listed under **Notebook Instances** in [SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/), with the exception that AL2023 does not support `ml.p2`, `ml.p3`, `ml.p3dn`, `ml.inf1`, and `ml.g3` instances. `notebook-al2023-v2` also does not support `ml.p6-b200` and `ml.g6e` instances.

## Available kernels
<a name="nbi-al2023-kernel"></a>

The following list gives information about the available kernels for SageMaker notebook instances. All of these images are supported on notebook instances based on the `notebook-al2023-v1` operating system.

R  
A kernel used to perform data analysis and visualization using R code from a Jupyter notebook.

Sparkmagic (PySpark)  
A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Python programming language. This kernel comes with Python 3.10.

Sparkmagic (Spark)  
A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Scala programming language. This kernel comes with Python 3.10.

Sparkmagic (SparkR)  
A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the R programming language. This kernel comes with Python 3.10.

conda\_python3  
A conda environment that comes pre-installed with popular packages for data science and machine learning. This kernel comes with Python 3.10.

conda\_pytorch  
A conda environment that comes pre-installed with PyTorch version 2.10.0, as well as popular data science and machine learning packages. This kernel comes with Python 3.10.

The following list gives information about the available kernels on notebook instances based on the `notebook-al2023-v2` operating system.

R  
A kernel used to perform data analysis and visualization using R code from a Jupyter notebook.

Sparkmagic (PySpark)  
A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Python programming language. This kernel comes with Python 3.12.

Sparkmagic (Spark)  
A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Scala programming language. This kernel comes with Python 3.12.

Sparkmagic (SparkR)  
A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the R programming language. This kernel comes with Python 3.12.

conda\_python3  
A conda environment that comes pre-installed with popular packages for data science and machine learning. This kernel comes with Python 3.12.

conda\_pytorch  
A conda environment that comes pre-installed with PyTorch version 2.13.0, as well as popular data science and machine learning packages. This kernel comes with Python 3.12.

## Differences between notebook-al2023-v1 and notebook-al2023-v2
<a name="nbi-al2023-v2-differences"></a>

`notebook-al2023-v2` runs the same operating system and JupyterLab version as `notebook-al2023-v1`. It differs in the following ways:
+ The Jupyter environment and the `conda_python3`, `conda_pytorch`, and Sparkmagic kernels use Python 3.12 instead of Python 3.10.
+ The `conda_pytorch` kernel comes with PyTorch 2.13.0.
+ `notebook-al2023-v2` does not support `ml.p6-b200` and `ml.g6e` instances.

To move an existing notebook instance to `notebook-al2023-v2`, stop the notebook instance, change its platform identifier to `notebook-al2023-v2`, and start the notebook instance. To change the platform identifier with the API, use the [UpdateNotebookInstance operation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateNotebookInstance.html). Your data in `/home/ec2-user/SageMaker/` is preserved. Verify that your lifecycle configuration scripts, and the packages they install into the built-in environments, work with Python 3.12.