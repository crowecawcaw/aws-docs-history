# Installing and

using kernels and libraries in EMR Studio

Each EMR notebook comes with a set of pre-installed libraries and kernels. You
can install additional libraries and kernels in an EMR cluster if the cluster has
access to the repository where the kernels and libraries are located. For example, for
clusters in private subnets, you might need to conﬁgure network address translation
(NAT) and provide a path for the cluster to access the public PyPI repository to install
a library. For more information about configuring external access for different network
configurations, see [Scenarios and examples](../../../vpc/latest/userguide/VPC_Scenarios.md "../../../vpc/latest/userguide/VPC_Scenarios.md") in the
_Amazon VPC User Guide_.

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

EMR Serverless applications come with the following pre-installed libraries for
Python and PySpark:

- Python libraries –
  ggplot, matplotlib, numpy,
  pandas, plotly, bokeh,
  scikit-learn, scipy,
  scipy
- PySpark libraries –
  ggplot, matplotlib, numpy,
  pandas, plotly, bokeh,
  scikit-learn, scipy,
  scipy

## Installing kernels and Python

libraries on a cluster primary node

With Amazon EMR release version 5.30.0 and later, excluding 6.0.0, you can install
additional Python libraries and kernels on the primary node of the cluster. After
installation, these kernels and libraries are available to any user running an
EMR notebook attached to the cluster. Python libraries installed this way
are available only to processes running on the primary node. The libraries are not
installed on core or task nodes and are not available to executors running on those
nodes.

###### Note

For Amazon EMR versions 5.30.1, 5.31.0, and 6.1.0, you must take additional steps
in order to install kernels and libraries on the primary node of a cluster.

To enable the feature, do the following:

1. Make sure that the permissions policy attached to the service role for
   EMR Notebooks allows the following action:

`elasticmapreduce:ListSteps`

For more information, see [Service
role for EMR Notebooks](emr-managed-notebooks-service-role.md "emr-managed-notebooks-service-role.md"). 2. Use the AWS CLI to run a step on the cluster that sets up EMR Notebooks as
shown in the following example. You must use the step name
`EMRNotebooksSetup`. Replace
`us-east-1` with the Region in which your
cluster resides. For more information, see [Adding steps to a cluster
using the AWS CLI](add-step-cli.md "add-step-cli.md").

```
`aws emr add-steps --cluster-id `MyClusterID` --steps Type=CUSTOM_JAR,Name=EMRNotebooksSetup,ActionOnFailure=CONTINUE,Jar=s3://`us-east-1`.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://awssupportdatasvcs.com/bootstrap-actions/EMRNotebooksSetup/emr-notebooks-setup.sh"]`
```

You can install kernels and libraries using `pip` or `conda`
in the `/emr/notebook-env/bin` directory on the primary node.

###### Example – Installing Python libraries

From the Python3 kernel, run the `%pip` magic as a command from
within a notebook cell to install Python libraries.

```
%pip install pmdarima
```

You may need to restart the kernel to use updated packages. You can also use
the [`%%sh`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-sh "https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-sh") Spark magic to invoke
`pip`.

```
%%sh
/emr/notebook-env/bin/pip install -U matplotlib
/emr/notebook-env/bin/pip install -U pmdarima
```

When using a PySpark kernel, you can either install libraries on the cluster
using `pip` commands or use notebook-scoped libraries from within a
PySpark notebook.

To run `pip` commands on the cluster from the terminal, first
connect to the primary node using SSH, as the following commands
demonstrate.

```
sudo pip3 install -U matplotlib
sudo pip3 install -U pmdarima
```

Alternatively, you can use notebook-scoped libraries. With notebook-scoped
libraries, your library installation is limited to the scope of your session and
occurs on all Spark executors. For more information, see [Using Notebook
Scoped Libraries](#emr-managed-notebooks-custom-libraries-limitations "#emr-managed-notebooks-custom-libraries-limitations").

If you want to package multiple Python libraries within a PySpark kernel, you
can also create an isolated Python virtual environment. For examples, see [Using Virtualenv](https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-virtualenv "https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-virtualenv").

To create a Python virtual environment in a session, use the Spark property
`spark.yarn.dist.archives` from the `%%configure`
magic command in the first cell in a notebook, as the following example
demonstrates.

```
%%configure -f
{
   "conf": {
   "spark.yarn.appMasterEnv.PYSPARK_PYTHON":"./environment/bin/python",
   "spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON":"./environment/bin/python",
   "spark.yarn.dist.archives":"s3://`amzn-s3-demo-bucket`/`prefix`/my_pyspark_venv.tar.gz#environment",
   "spark.submit.deployMode":"cluster"
   }
}
```

You can similarly create a Spark executor environment.

```
%%configure -f
{
   "conf": {
   "spark.yarn.appMasterEnv.PYSPARK_PYTHON":"./environment/bin/python",
   "spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON":"./environment/bin/python",
   "spark.executorEnv.PYSPARK_PYTHON":"./environment/bin/python",
   "spark.yarn.dist.archives":"s3://`amzn-s3-demo-bucket`/`prefix`/my_pyspark_venv.tar.gz#environment",
   "spark.submit.deployMode":"cluster"
   }
}
```

You can also use `conda` to install Python libraries. You don't
need sudo access to use `conda`. You must connect to the primary node
with SSH, and then run `conda` from the terminal. For more
information, see [Connect to the Amazon EMR cluster primary node using
SSH](emr-connect-master-node-ssh.md "emr-connect-master-node-ssh.md").

###### Example – Installing kernels

The following example demonstrates installing the Kotlin kernel using a
terminal command while connected to the primary node of a cluster:

```
sudo /emr/notebook-env/bin/conda install kotlin-jupyter-kernel -c jetbrains
```

###### Note

These instructions do not install kernel dependencies. If your kernel has
third-party dependencies, you may need to take additional setup steps before
you can use the kernel with your notebook.

## Considerations

and limitations with notebook-scoped libraries

When you use notebook-scoped libraries, consider the following:

- Notebook-scoped libraries are available for clusters that you create with
  Amazon EMR releases 5.26.0 and higher.
- Notebook-scoped libraries are intended to be used only with the PySpark
  kernel.
- Any user can install additional notebook-scoped libraries from within a
  notebook cell. These libraries are only available to that notebook user
  during a single notebook session. If other users need the same libraries, or
  the same user needs the same libraries in a different session, the library
  must be re-installed.
- You can uninstall only the libraries that were installed with the
  `install_pypi_package` API. You cannot uninstall any
  libraries that were pre-installed on the cluster.
- If the same libraries with different versions are installed on the cluster
  and as notebook-scoped libraries, the notebook-scoped library version
  overrides the cluster library version.

## Working with

Notebook-scoped libraries

To install libraries, your Amazon EMR cluster must have access to the PyPI repository
where the libraries are located.

The following examples demonstrate simple commands to list, install, and uninstall
libraries from within a notebook cell using the PySpark kernel and APIs. For
additional examples, see [Install Python libraries on a running cluster with EMR Notebooks](https://aws.amazon.com/blogs/big-data/install-python-libraries-on-a-running-cluster-with-emr-notebooks/ "https://aws.amazon.com/blogs/big-data/install-python-libraries-on-a-running-cluster-with-emr-notebooks/") post on
the AWS Big Data Blog.

###### Example – Listing current libraries

The following command lists the Python packages available for the current
Spark notebook session. This lists libraries installed on the cluster and
notebook-scoped libraries.

```
sc.list_packages()
```

###### Example – Installing the Celery library

The following command installs the [Celery](https://pypi.org/project/celery/ "https://pypi.org/project/celery/") library as a
notebook-scoped library.

```
sc.install_pypi_package("celery")
```

After installing the library, the following command confirms that the library
is available on the Spark driver and executors.

```
import celery
sc.range(1,10000,1,100).map(lambda x: celery.__version__).collect()
```

###### Example – Installing the Arrow library, specifying the version and

repository

The following command installs the [Arrow](https://pypi.org/project/arrow/ "https://pypi.org/project/arrow/") library as a
notebook-scoped library, with a specification of the library version and
repository URL.

```
sc.install_pypi_package("arrow==0.14.0", "https://pypi.org/simple")
```

###### Example – Uninstalling a library

The following command uninstalls the Arrow library, removing it as a
notebook-scoped library from the current session.

```
sc.uninstall_package("arrow")
```
