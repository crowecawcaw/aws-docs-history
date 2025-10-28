# User guide

This section covers how data scientist and data engineers can launch, discover, connect
to, or terminate an Amazon EMR cluster from Studio or Studio Classic.

Before users can list or launch clusters, administrators must have configured the
necessary settings in the Studio environment. For information on how administrators can
configure a Studio environment to allow self-provisioning and listing of Amazon EMR
clusters, see [Admin guide](studio-emr-admin-guide.md "studio-emr-admin-guide.md").

###### Topics

- [Supported images and
  kernels to connect to an Amazon EMR cluster from Studio or Studio Classic](#studio-notebooks-emr-cluster-connect-kernels "#studio-notebooks-emr-cluster-connect-kernels")
- [Bring your own image](#studio-notebooks-emr-byoi "#studio-notebooks-emr-byoi")
- [Launch an Amazon EMR
  cluster from Studio or Studio Classic](studio-notebooks-launch-emr-cluster-from-template.md "studio-notebooks-launch-emr-cluster-from-template.md")
- [List Amazon EMR clusters from Studio or
  Studio Classic](discover-emr-clusters.md "discover-emr-clusters.md")
- [Connect to an Amazon EMR cluster from SageMaker Studio
  or Studio Classic](connect-emr-clusters.md "connect-emr-clusters.md")
- [Terminate an Amazon EMR cluster from Studio or
  Studio Classic](terminate-emr-clusters.md "terminate-emr-clusters.md")
- [Access Spark UI from Studio or
  Studio Classic](studio-notebooks-access-spark-ui.md "studio-notebooks-access-spark-ui.md")

## Supported images and

kernels to connect to an Amazon EMR cluster from Studio or Studio Classic

The following images and kernels come with [sagemaker-studio-analytics-extension](https://pypi.org/project/sagemaker-studio-analytics-extension/ "https://pypi.org/project/sagemaker-studio-analytics-extension/"), the JupyterLab extension that
connects to a remote Spark (Amazon EMR) cluster via the [SparkMagic](https://github.com/jupyter-incubator/sparkmagic "https://github.com/jupyter-incubator/sparkmagic") library
using [Apache Livy](https://livy.apache.org/ "https://livy.apache.org/").

- **For Studio users:** SageMaker Distribution is
  a Docker environment for data science used as the default image of JupyterLab
  notebook instances. All versions of [SageMaker AI
  Distribution](https://github.com/aws/sagemaker-distribution "https://github.com/aws/sagemaker-distribution") come with
  `sagemaker-studio-analytics-extension` pre-installed.
- **For Studio Classic users:** The following images
  come pre-installed with
  `sagemaker-studio-analytics-extension`:
  - DataScience – Python 3 kernel
  - DataScience 2.0 – Python 3 kernel
  - DataScience 3.0 – Python 3 kernel
  - SparkAnalytics 1.0 – SparkMagic and PySpark kernels
  - SparkAnalytics 2.0 – SparkMagic and PySpark kernels
  - SparkMagic – SparkMagic and PySpark kernels
  - PyTorch 1.8 – Python 3 kernels
  - TensorFlow 2.6 – Python 3 kernel
  - TensorFlow 2.11 – Python 3 kernel

To connect to Amazon EMR clusters using another built-in image or your own image, follow
the instructions in [Bring your own image](#studio-notebooks-emr-byoi "#studio-notebooks-emr-byoi").

## Bring your own image

To bring your own image in Studio or Studio Classic and allow your notebooks to
connect to Amazon EMR clusters, install the following [sagemaker-studio-analytics-extension](https://pypi.org/project/sagemaker-studio-analytics-extension/ "https://pypi.org/project/sagemaker-studio-analytics-extension/") extension to your kernel. It supports
connecting SageMaker Studio or Studio Classic notebooks to Spark(Amazon EMR) clusters through the
[SparkMagic](../../../emr/latest/ManagementGuide/emr-studio-magics.md "../../../emr/latest/ManagementGuide/emr-studio-magics.md") library.

```
pip install sparkmagic
pip install sagemaker-studio-sparkmagic-lib
pip install sagemaker-studio-analytics-extension
```

Additionally, to connect to Amazon EMR with [Kerberos](../../../emr/latest/ManagementGuide/emr-kerberos.md "../../../emr/latest/ManagementGuide/emr-kerberos.md") authentication,
you must install the kinit client. Depending on your OS, the command to install the
kinit client can vary. To bring an Ubuntu (Debian based) image, use the `apt-get
 install -y -qq krb5-user` command.

For more information on bringing your own image in SageMaker Studio or Studio Classic, see
[Bring your
own SageMaker image](studio-byoi.md "studio-byoi.md").
