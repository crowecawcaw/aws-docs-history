# Resources for using SageMaker AI Spark for

Python (PySpark) examples

Amazon SageMaker AI provides an Apache Spark Python library ([SageMaker AI
PySpark](https://github.com/aws/sagemaker-spark/tree/master/sagemaker-pyspark-sdk "https://github.com/aws/sagemaker-spark/tree/master/sagemaker-pyspark-sdk")) that you can use to integrate your Apache Spark applications with
SageMaker AI. This topic contains examples to help you get started with PySpark. For information
about the SageMaker AI Apache Spark library, see [Apache Spark with Amazon SageMaker AI](apache-spark.md "apache-spark.md").

**Download PySpark**

You can download the source code for both Python Spark (PySpark) and Scala libraries
from the [SageMaker AI Spark](https://github.com/aws/sagemaker-spark "https://github.com/aws/sagemaker-spark") GitHub
repository.

For instructions on installing the SageMaker AI Spark library, use any the following options
or visit [SageMaker AI
PySpark](https://github.com/aws/sagemaker-spark/tree/master/sagemaker-pyspark-sdk "https://github.com/aws/sagemaker-spark/tree/master/sagemaker-pyspark-sdk").

- Install using pip:

```
pip install sagemaker_pyspark
```

- Install from the source:

```
git clone git@github.com:aws/sagemaker-spark.git
cd sagemaker-pyspark-sdk
python setup.py install
```

- You can also create a new notebook in a notebook instance that uses either the
  `Sparkmagic (PySpark)` or the `Sparkmagic (PySpark3)`
  kernel and connect to a remote Amazon EMR cluster.

###### Note

The Amazon EMR cluster must be configured with an IAM role that has the
`AmazonSageMakerFullAccess` policy attached. For information
about configuring roles for an EMR cluster, see [Configure IAM Roles for Amazon EMR Permissions to AWS
Services](../../../emr/latest/ManagementGuide/emr-iam-roles.md "../../../emr/latest/ManagementGuide/emr-iam-roles.md") in the _Amazon EMR Management
Guide_.
**PySpark examples**

For examples on using SageMaker AI PySpark, see:

- [Using Amazon SageMaker AI with Apache Spark](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-spark/index.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-spark/index.html") in Read the Docs.
- [SageMaker AI Spark](https://github.com/aws/sagemaker-spark "https://github.com/aws/sagemaker-spark") GitHub
  repository.
