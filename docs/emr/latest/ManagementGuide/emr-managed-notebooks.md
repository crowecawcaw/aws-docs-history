# Amazon EMR Notebooks overview

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

You can use Amazon EMR Notebooks along with Amazon EMR clusters running [Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") to
create and open [Jupyter](https://jupyter.org "https://jupyter.org") Notebook and JupyterLab
interfaces within the Amazon EMR console. An EMR notebook is a "serverless" notebook that
you can use to run queries and code. Unlike a traditional notebook, the contents of an
EMR notebook — the equations, queries, models, code, and narrative text
within notebook cells — run in a client. The commands are executed using a kernel on
the EMR cluster. Notebook contents are also saved to Amazon S3 separately from cluster data for
durability and flexible re-use.

You can start a cluster, attach an EMR notebook for analysis, and then terminate
the cluster. You can also close a notebook attached to one running cluster and switch to
another. Multiple users can attach notebooks to the same cluster simultaneously and share
notebook files in Amazon S3 with each other. These features let you run clusters on-demand to
save cost, and reduce the time spent re-configuring notebooks for different clusters and
datasets.

You can also execute an EMR notebook programmatically using the Amazon EMR API, without
the need to interact with Amazon EMR console ("headless execution"). You need to include a cell
in the EMR notebook that has a parameters tag. That cell allows a script to pass new
input values to the notebook. Parameterized notebooks can be re-used with different sets of
input values. There's no need to make copies of the same notebook to edit and execute with
new input values. Amazon EMR creates and saves the output notebook on S3 for each run of the
parameterized notebook. For EMR notebook API code samples, see [Sample programmatic commands for EMR Notebooks](emr-managed-notebooks-headless.md "emr-managed-notebooks-headless.md").

###### Important

The EMR Notebooks capability supports clusters that use Amazon EMR releases 5.18.0 and
higher. We recommend that you use EMR Notebooks with clusters that use the latest version
of Amazon EMR, or at least 5.30.0, 5.32.0, or 6.2.0. With these releases, Jupyter kernels run
on the attached cluster rather than on a Jupyter instance. This improves performance and
enhances your ability to customize kernels and libraries. For more information, see
[Differences in capabilities by
cluster release version](emr-managed-notebooks-considerations.md#considerations-cluster-version "emr-managed-notebooks-considerations.md#considerations-cluster-version").

Applicable charges for Amazon S3 storage and for Amazon EMR clusters apply.
