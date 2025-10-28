# Using Amazon Neptune with graph notebooks

To work with Neptune graphs you can use a Neptune graph notebook or create a new Neptune database using an AWS CloudFormation [template](get-started-cfn-create.md "get-started-cfn-create.md").

Whether you're new to graphs and want to learn and experiment, or
you're experienced and want to refine your queries, the Neptune [workbench](#graph-notebooks-workbench "#graph-notebooks-workbench") offers an interactive
development environment (IDE) that can boost your productivity when you're building
graph applications. The Workbench provides a user-friendly interface for interacting with your Neptune database, writing queries, and visualizing your data.

By using the AWS CloudFormation template to set up your Neptune database, and the Workbench to develop your graph applications, you can get started with Neptune quickly and efficiently, without the need for additional tooling. This allows you to focus on building your applications rather than setting up the underlying infrastructure.

###### Note

Neptune notebooks, managed through Amazon SageMaker AI, is not currently available in the Asia Pacific (Malaysia) (ap-southeast-5)
region. However, you can still deploy Neptune notebooks through alternative non-managed options. Refer to
[Setting up Neptune notebooks manually](#graph-notebook-manual-setup "#graph-notebook-manual-setup") for deploying notebooks manually.

Neptune provides [Jupyter](https://jupyter-notebook.readthedocs.io/en/stable/ "https://jupyter-notebook.readthedocs.io/en/stable/")
and [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html "https://jupyterlab.readthedocs.io/en/stable/index.html")
notebooks in the open-source [Neptune
graph notebook](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook") project on GitHub, and in the Neptune workbench. These notebooks
offer sample application tutorials and code snippets in an interactive coding environment
where you can learn about graph technology and Neptune. You can use them to walk through
setting up, configuring, populating and querying graphs using different query languages,
different data sets, and even different databases on the back end.

You can host these notebooks in several different ways:

- The [Neptune workbench](#graph-notebooks-workbench "#graph-notebooks-workbench") lets you run Jupyter notebooks
  in a fully managed environment, hosted in Amazon SageMaker AI, and automatically loads the latest release of the
  Neptune [graph notebook project](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook") for you. It is
  easy to set up the workbench in the [Neptune console](https://console.aws.amazon.com/neptune "https://console.aws.amazon.com/neptune") when you create a new Neptune database.

###### Note

When creating a Neptune notebook instance, you are provided with two options for network access: Direct access
through Amazon SageMaker AI (the default) and access through a VPC. In either option, the notebook requires access to the
internet to fetch package dependencies for installing the Neptune workbench. Lack of internet access will cause
the creation of a Neptune notebook instance to fail.

- You can also [install
  Jupyter locally](#graph-notebooks-local "#graph-notebooks-local"). This lets you run the notebooks from
  your laptop, connected either to Neptune or to a local instance of one
  of the open-source graph databases. In the latter case, you can experiment
  with graph technology as much as you want before you spend a penny. Then,
  when you're ready, you can move smoothly to the managed production
  environment that Neptune offers.

## Using the Neptune workbench to host Neptune notebooks

Neptune offers `T3` and `T4g` instance types that you
can get started with for less than $0.10 per hour. You are billed for workbench
resources through Amazon SageMaker AI, separately from your Neptune billing. See [the Neptune pricing page](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").
Jupyter and JupyterLab notebooks created on the Neptune workbench all use
an Amazon Linux 2 and JupyterLab 4 environment. For more information about
JupyterLab notebook support, see the [Amazon SageMaker AI
documentation](../../../sagemaker/latest/dg/nbi-jl.md "../../../sagemaker/latest/dg/nbi-jl.md").

You can create a Jupyter or JupyterLab notebook using the Neptune
workbench in the AWS Management Console in either of two ways:

- Use the **Notebook configuration** menu when
  creating a new Neptune DB cluster. To do this, follow the steps outlined in
  [Launching a Neptune DB cluster using the AWS Management Console](manage-console-launch-console.md "manage-console-launch-console.md").
- Use the **Notebooks** menu in the left
  navigation pane after your DB cluster has already been created. To do this,
  follow the steps below.

###### To create a Jupyter or JupyterLab notebook using the **Notebooks** menu

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane on the left, choose **Notebooks**.
3. Choose **Create notebook**.
4. Choose **Database** as the Neptune service.
5. In the **Cluster** list, choose your Neptune DB cluster. If you don't yet
   have a DB cluster, choose **Create cluster** to create one.
6. Select a **Notebook instance type**.
7. Give your notebook a name, and optionally a description.
8. Unless you already created an AWS Identity and Access Management (IAM) role for your notebooks, choose
   **Create an IAM role**, and enter an IAM role name.

###### Note

If you do choose to re-use an IAM role created for a previous notebook,
the role policy must contain the correct permissions to access the Neptune DB cluster
that you're using. You can verify this by checking that the components in the resource
ARN under the `neptune-db:*` action match that cluster. Incorrectly
configured permissions result in connection errors when you try to run notebook
magic commands. 9. Choose **Create notebook**. The creation process may
take 5 to 10 minutes before everything is ready. 10. After your notebook is created, select it and then choose **Open
Jupyter** or **Open JupyterLab**.

The console can create an AWS Identity and Access Management (IAM) role for your notebooks, or you
can create one yourself. The policy for this role should include the following:

Note that the second statement in the policy above lists one or more Neptune
[cluster resource IDs](iam-data-resources.md "iam-data-resources.md").

Also, the role should establish the following trust relationship:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Again, getting everything ready to go can take 5 to 10 minutes.

You can configure your new notebook to work with Neptune ML, as explained in
[Manually configuring a Neptune notebook for Neptune ML](ml-manual-setup-notebooks.md "ml-manual-setup-notebooks.md").

### Using Python to connect a generic SageMaker AI notebook to Neptune

Connecting a notebook to Neptune is easy if you have installed the Neptune
magics, but it is also possible to connect a SageMaker AI notebook to Neptune using Python,
even if you are not using a Neptune notebook.

###### Steps to take to connect to Neptune in a SageMaker AI notebook cell

1. Install the Gremlin Python client:

```
!pip install gremlinpython
```

Neptune notebooks install the Gremlin Python client for you, so this
step is only necessary if you're using a plain SageMaker AI notebook. 2. Write code such as the following to connect and issue a Gremlin query:

```
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.driver.aiohttp.transport import AiohttpTransport
from gremlin_python.process.traversal import *
import os

port = 8182
server = '`(your server endpoint)`'

endpoint = f'wss://{server}:{port}/gremlin'

graph=Graph()

connection = DriverRemoteConnection(endpoint,'g',
                 transport_factory=lambda:AiohttpTransport(call_from_event_loop=True))

g = graph.traversal().withRemote(connection)

results = (g.V().hasLabel('airport')
                .sample(10)
                .order()
                .by('code')
                .local(__.values('code','city').fold())
                .toList())

# Print the results in a tabular form with a row index
for i,c in enumerate(results,1):
    print("%3d %4s %s" % (i,c[0],c[1]))

connection.close()
```

###### Note

If you happen to be using a version of the Gremlin Python client that is
older than 3.5.0, this line:

```
connection = DriverRemoteConnection(endpoint,'g',
                 transport_factory=lambda:AiohttpTransport(call_from_event_loop=True))
```

Would just be:

```
connection = DriverRemoteConnection(endpoint,'g')
```

## Enabling CloudWatch logs on Neptune Notebooks

CloudWatch logs are now enabled by default for Neptune Notebooks. If you have an older
notebook that is not producing CloudWatch logs, follow these steps to enable them manually:

1. Sign in to the AWS Management Console and open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/home "https://console.aws.amazon.com/sagemaker/home").
2. On the navigation pane on the left, choose **Notebook**,
   then **Notebook Instances**. Look for the name of the Neptune
   notebook for which you would like to enable logs.
3. Go to the details page by selecting the name of that notebook instance.
4. If the notebook instance is running, select the **Stop**
   button, at the top right of the notebook details page.
5. Under **Permissions and encryption** there is a field
   for **IAM role ARN**. Select the link in this field to go to
   the IAM role that this notebook instance runs with.
6. Create the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DeleteLogDelivery",
 "logs:Describe*",
 "logs:GetLogDelivery",
 "logs:GetLogEvents",
 "logs:ListLogDeliveries",
 "logs:PutLogEvents",
 "logs:PutResourcePolicy",
 "logs:UpdateLogDelivery"
 ],
 "Resource": "*"
 }
 ]
}`

```

7. Save this new policy and attach it to the IAM Role found in Step 4.
8. Click **Start** at the top right of the
   SageMaker AI notebook instance details page.
9. When logs start flowing, you should see a **View Logs**
   link beneath the field labeled **Lifecycle configuration** near
   the bottom left of the **Notebook instance settings** section
   of the details page.

If a notebook fails to start, there will be a message from the in the notebook
details page on the SageMaker AI console, stating that the notebook instance took over 5
minutes to start. CloudWatch logs relevant to this issue can be found under this name:

```
`(your-notebook-name)`/LifecycleConfigOnStart
```

## Setting up graph notebooks on your local machine

The graph-notebook project has instructions for setting up Neptune notebooks on
your local machine:

- [Prerequisites](https://github.com/aws/graph-notebook/#prerequisites "https://github.com/aws/graph-notebook/#prerequisites")
- [Jupyter and JupyterLab installation](https://github.com/aws/graph-notebook/#installation "https://github.com/aws/graph-notebook/#installation")
- [Connecting to
  a graph database](https://github.com/aws/graph-notebook/#connecting-to-a-graph-database "https://github.com/aws/graph-notebook/#connecting-to-a-graph-database").

You can connect your local notebooks either to a Neptune DB cluster, or to a
local or remote instance of an open-source graph database.

### Using Neptune notebooks with Neptune clusters

If you are connecting to a Neptune cluster on the back end, you may want to run
the notebooks in Amazon SageMaker AI. Connecting to Neptune from SageMaker AI can be more convenient
than from a local installation of the notebooks, and it will let you work more easily
with [Neptune ML](machine-learning.md "machine-learning.md").

For instructions about how to set up notebooks in SageMaker AI, see [Launching
graph-notebook using Amazon SageMaker](https://github.com/aws/graph-notebook/blob/main/additional-databases/sagemaker/README.md "https://github.com/aws/graph-notebook/blob/main/additional-databases/sagemaker/README.md").

For instructions about how to set up and configure Neptune itself,
see [Setting up Amazon Neptune](neptune-setup.md "neptune-setup.md").

You can also connect a local installation of the Neptune notebooks
to a Neptune DB cluster. This can be somewhat more complicated because
Amazon Neptune DB clusters can only be created in an Amazon Virtual Private Cloud (VPC), which
is by design isolated from the outside world. There are a number ways to connect
into a VPC from the outside it. One is to use a load balancer. Another is
to use VPC peering (see the [Amazon Virtual Private Cloud
Peering Guide](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md")).

The most convenient way for most people, however, is to connect to set up
an Amazon EC2 proxy server within the VPC and then use [SSH tunnelling](https://www.ssh.com/ssh/tunneling/ "https://www.ssh.com/ssh/tunneling/") (also called port
fowarding), to connect to it. You can find instructions about how to set up at [Connecting graph notebook
locally to Amazon Neptune](https://github.com/aws/graph-notebook/tree/main/additional-databases/neptune "https://github.com/aws/graph-notebook/tree/main/additional-databases/neptune") in the `additional-databases/neptune`
folder of the [graph-notebook](https://github.com/aws/graph-notebook/ "https://github.com/aws/graph-notebook/")
GitHub project.

### Using Neptune notebooks with open-source graph databases

To get started with graph technology at no cost, you can also use Neptune
notebooks with various open-source databases
on the back end. Examples are the TinkerPop [Gremlin
server](https://tinkerpop.apache.org/docs/current/reference/#gremlin-server "https://tinkerpop.apache.org/docs/current/reference/#gremlin-server"), and the [Blazegraph](https://blazegraph.com/ "https://blazegraph.com/")
database.

To use Gremlin Server as your back-end database, follow these steps:

- The [Connecting graph-notebook to a Gremlin Server](https://github.com/aws/graph-notebook/blob/main/additional-databases/gremlin-server/README.md#connecting-graph-notebook-to-a-gremlin-server "https://github.com/aws/graph-notebook/blob/main/additional-databases/gremlin-server/README.md#connecting-graph-notebook-to-a-gremlin-server") GitHub folder.
- The [graph-notebook Gremlin
  configuration](https://github.com/aws/graph-notebook/#gremlin-server "https://github.com/aws/graph-notebook/#gremlin-server") GitHub folder.

To use a local instance of [Blazegraph](https://github.com/blazegraph/database "https://github.com/blazegraph/database")
as your back-end database, follow these steps:

- Review the [Blazegraph
  quick-start instructions](https://github.com/blazegraph/database/wiki/Quick_Start "https://github.com/blazegraph/database/wiki/Quick_Start") to understand the basic setup and configuration required for running a Blazegraph instance.
- Access the [graph-notebook Blazegraph
  configuration](https://github.com/aws/graph-notebook/#blazegraph "https://github.com/aws/graph-notebook/#blazegraph") GitHub folder containing the necessary files and instructions for setting up a local Blazegraph instance.
  .
- Within the GitHub repository, navigate to the "blazegraph" directory and follow the provided instructions to set up your local Blazegraph instance. This includes steps for downloading the Blazegraph software, configuring the necessary files, and starting the Blazegraph server.

Once you have a local Blazegraph instance running, you can integrate it with your application as the backend database for your graph-based data and queries. Refer to the documentation and example code provided in the graph-notebook repository to learn how to connect your application to the Blazegraph instance.

## Migrating Neptune notebooks to JupyterLab 4.x

This section outlines various approaches for migrating your Neptune notebooks to JupyterLab 4.x and newer Amazon Linux environments. For detailed information about JupyterLab versioning, see [Amazon SageMaker AI JupyterLab Versioning](../../../sagemaker/latest/dg/nbi-jl.md "../../../sagemaker/latest/dg/nbi-jl.md").

### Migration approaches

#### Fresh installation

If you don't need to preserve existing workspace files or configurations, you can:

1. Create a new notebook instance running JupyterLab 4.x (notebook-al2-v3)
2. Verify the new setup works as expected
3. Stop and delete your old notebook instance

#### File transfer migration

This method uses your local system or Amazon S3 as intermediate storage.

###### Best for

- [Direct internet access through Amazon SageMaker AI networking configuration](../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md#appendix-notebook-and-internet-access-default "../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md#appendix-notebook-and-internet-access-default").
- A moderate volume of data to migrate
- Specific files to preserve rather than entire workspace configurations.

##### Method 1: Using JupyterLab UI

###### Best for

- Small number of files
- Selective file migration
- Prefer simple drag-and-drop operations

###### Steps

1. Download files from source JupyterLab instance:
   - Navigate and select the files you want to migrate to the new instance in JupyterLab
   - Right-click and select **Download**

2. Upload to new JupyterLab instance:
   - Use the upload button in JupyterLab and select all files that you want to copy to the new instance
   - (Or) drag and drop files directly

##### Method 2: Using Amazon S3

###### Best for

- Large number of files
- Preserving your folder structures
- Bulk migrations

###### Prerequisites

Ensure that the role associated with the notebook has appropriate permissions to upload and access the Amazon S3
bucket:

```
{
"Effect": "Allow",
"Action": ["s3:PutObject", "s3:GetObject", "s3:ListBucket"],
"Resource": ["arn:aws:s3:::your-bucket-name/*", "arn:aws:s3:::your-bucket-name"]
}
```

###### Note

[AWS CLI](../../../https:/awscli.amazonaws.com/v2/documentation/api/latest/index.md "../../../https:/awscli.amazonaws.com/v2/documentation/api/latest/index.md") should be pre-installed on SageMaker AI notebooks.

###### Steps

1. Open a terminal in JupyterLab or type the terminal commands in a notebook cell with `!`
   prefix.
2. Copy files from your old JupyterLab instance to S3 using either
   [Amazon S3 cp](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md") or
   [Amazon S3 sync](../../../cli/latest/reference/s3/sync.md "../../../cli/latest/reference/s3/sync.md")
   CLI commands:

```
# using AWS s3 cp
aws s3 cp /home/ec2-user/SageMaker/your-folder s3://your-bucket/backup/ --recursive

# (OR) using AWS s3 sync
aws s3 sync /home/ec2-user/SageMaker/your-folder s3://your-bucket/backup/
```

3. Copy files from S3 to your new JupyterLab instance:

```
# using AWS s3 cp
aws s3 cp s3://your-bucket/backup/ /home/ec2-user/SageMaker/your-folder --recursive

# (OR) using AWS s3 sync
aws s3 sync s3://your-bucket/backup/ /home/ec2-user/SageMaker/your-folder
```

###### Note

Use `sync` for maintaining folder structures and incremental updates and `cp` for
one-time transfers.

#### Amazon EFS migration

###### Best for

- [VPC-only](../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md#appendix-notebook-and-internet-access-default-vpc "../../../sagemaker/latest/dg/appendix-notebook-and-internet-access.md#appendix-notebook-and-internet-access-default-vpc") networking configuration
- Large data volumes

###### Steps

Follow the [Mount an EFS file system to an Amazon SageMaker AI notebook](https://aws.amazon.com/blogs/machine-learning/mount-an-efs-file-system-to-an-amazon-sagemaker-notebook-with-lifecycle-configurations/ "https://aws.amazon.com/blogs/machine-learning/mount-an-efs-file-system-to-an-amazon-sagemaker-notebook-with-lifecycle-configurations/")
blog to use an Amazon EFS file system with your notebook instances.

In addition, there are also a few more steps that apply specifically to migrating Neptune notebooks to the
new environment:

1. During [Neptune notebook creation in the console](graph-notebooks.md#graph-notebooks-workbench "graph-notebooks.md#graph-notebooks-workbench") , select
   **Create a new lifecycle configuration** under Lifecycle configuration
2. In the template lifecycle config, append your Amazon EFS mount command (`sudo mount -t nfs ...`)
   after the install.sh script

This ensures your Amazon EFS filesystem is automatically mounted each time your notebook instance starts or restarts.
For troubleshooting mount issues, refer to
[Amazon EFS troubleshooting document](../../../efs/latest/ug/troubleshooting.md "../../../efs/latest/ug/troubleshooting.md").

###### Advantages

- Seamless access to files across instances
- Direct file access without intermediary transfers
- Efficient handling of large datasets

#### Amazon EBS volume migration

###### Best for when you need to preserve

- Complete workspace configurations
- Hidden files
- System settings
- Preserving complete workspace configurations, hidden files and system settings

Follow the [AWS SageMaker AI migration guide for
Amazon EBS volumes](../../../sagemaker/latest/dg/nbi-upgrade.md "../../../sagemaker/latest/dg/nbi-upgrade.md") to transfer files from the Amazon EBS volume associated with the notebook instances.

In addition, there are also a few more steps that apply specifically to migrating Neptune notebooks to
the new environment.

## Neptune-specific prerequisites

In the source Neptune notebook's IAM role, add all of the following permissions:

```
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:ListBucket",
    "s3:CreateBucket",
    "s3:PutObject"
  ],
  "Resource": [
    "arn:aws:s3:::`(your ebs backup bucket name)`",
    "arn:aws:s3:::`(your ebs backup bucket name)`/*"
  ]
},
{
  "Effect": "Allow",
  "Action": [
    "sagemaker:ListTags"
  ],
  "Resource": [
    "*"
  ]
}
```

Be sure to specify the correct ARN for the S3 bucket you will use for backing up.

## Neptune-specific lifecycle configuration

When creating the second Lifecycle configuration script for restoring the backup
(from `on-create.sh`) as described in the blog post, the Lifecycle name
must follow the `aws-neptune-*` format, like `aws-neptune-sync-from-s3`.
This ensures that the LCC can be selected during notebook creation in the Neptune
console.

## Neptune-specific synchronization from a snapshot to a new instance

In the steps described in the blog post for synchronizing from a snapshot to
a new instance, here are the Neptune-specific changes:

- On step 4, choose **notebook-al2-v3**.
- On step 5, re-use the IAM role from the source Neptune notebook.
- Between steps 7 and 8:
  - In **Notebook instance settings**, set a name
    that uses the `aws-neptune-*` format.
  - Open the **Network** settings accordion and
    select the same VPC, Subnet, and Security group as in the source notebook.

## Neptune-specific steps after the new notebook has been created

1. Select the **Open Jupyter** button for the notebook.
   Once the `SYNC_COMPLETE` file shows up in the main directory, proceed
   to the next step.
2. Go to the notebook instance page in the SageMaker AI console.
3. Stop the notebook.
4. Select **Edit**.
5. In the notebook instance settings, edit the **Lifecycle
   configuration** field by selecting the source Neptune notebook's original
   Lifecycle. Note that this is not the EBS backup Lifecycle.
6. Select **Update notebook settings**.
7. Start the notebook again.

With the modifications described here to the steps outlined in the blog post,
your graph notebooks should now be migrated onto a new Neptune notebook instance
that uses the Amazon Linux 2 and JupyterLab 4 environment. They'll show up for
access and management on the Neptune page in the AWS Management Console, and you can now
continue your work from where you left off by selecting either
**Open Jupyter** or **Open JupyterLab**.

## Create a Neptune notebook in Amazon SageMaker AI instances

######

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the navigation pane, expand **Notebook**, then
   choose **Notebook instances**.
3. Choose **Create notebook instance**.
4. In **Notebook instance settings**, under
   **Notebook instance name**, give the notebook a name prefixed
   by `aws-neptune-` (for example, `aws-neptune-my-test-notebook`).
5. Under **Platform identifier**, select **Amazon Linux 2,
   JupyterLab 4**.
6. Select **Additional configuration**.
7. Under **Lifecycle configuration**, choose
   **Create a new lifecycle configuration**.
8. In **Configuration**, under **Name** enter
   the notebook instance name from step 4.
9. In **Scripts**, under **Start notebook**,
   replace the existing script with this:

```
#!/bin/bash

sudo -u ec2-user -i <<'EOF'

echo "export GRAPH_NOTEBOOK_AUTH_MODE=IAM" >> ~/.bashrc
echo "export GRAPH_NOTEBOOK_SSL=True" >> ~/.bashrc
echo "export GRAPH_NOTEBOOK_SERVICE=`neptune-db for Neptune, or neptune-graph for Neptune Analytics`" >> ~/.bashrc
echo "export GRAPH_NOTEBOOK_HOST=`(Neptune Analytics graph endpoint, public or private)`" >> ~/.bashrc
echo "export GRAPH_NOTEBOOK_PORT=8182" >> ~/.bashrc
echo "export NEPTUNE_LOAD_FROM_S3_ROLE_ARN=" >> ~/.bashrc
echo "export AWS_REGION=`(AWS region)`" >> ~/.bashrc

aws s3 cp s3://aws-neptune-notebook-`(AWS region)`/graph_notebook.tar.gz /tmp/graph_notebook.tar.gz
rm -rf /tmp/graph_notebook
tar -zxvf /tmp/graph_notebook.tar.gz -C /tmp
/tmp/graph_notebook/install_jl4x.sh

EOF
```

10. Select **Create configuration**.
11. In **Permissions and encryption**, under **IAM
    Role**, select the role you created above.
12. In **Network**, if you are using a private graph endpoint:
    1.  Under **VPC**, select the VPC where the Neptune Analytics graph resides.
    2.  Under **Subnet**, select a subnet associated with the Neptune Analytics graph.
    3.  Under **Security Group(s)**, select all the security groups
        associated with the Neptune Analytics graph.

13. Choose **Create notebook instance**.
14. After 5 or 10 minutes, when your new notebook reaches `Ready` status,
    select it. Choose **Open Jupyter** or **Open JupyterLab**.

## Setting up Neptune notebooks manually

You can also use the AWS open-source packages available for graph-notebook and graph-explorer to set up a
Neptune notebook environment. While there are multiple ways to set up a notebook using open-source packages,
the recommended approach is to:

- Set up [graph-notebook](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook") on your local machine and an Amazon EC2
  SSH tunnel that connects your local machine to a Neptune cluster on the same VPC as the Amazon EC2 instance.
- Set up [graph-explorer](https://github.com/aws/graph-explorer "https://github.com/aws/graph-explorer") on an Amazon EC2 instance within your VPC.

For detailed instructions on setting up the open-source
[graph-notebooks](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook") and
[graph-explorer](https://github.com/aws/graph-explorer "https://github.com/aws/graph-explorer") packages, refer to the following official AWS
documentation and GitHub repositories:

- [https://docs.aws.amazon.com/neptune/latest/userguide/graph-notebooks.html#graph-notebooks-local](graph-notebooks.md#graph-notebooks-local "graph-notebooks.md#graph-notebooks-local")
- [https://docs.aws.amazon.com/neptune/latest/userguide/get-started-connect-ec2-same-vpc.html](get-started-connect-ec2-same-vpc.md "get-started-connect-ec2-same-vpc.md")
- [https://github.com/aws/graph-notebook/tree/main/additional-databases/neptune](https://github.com/aws/graph-notebook/tree/main/additional-databases/neptune "https://github.com/aws/graph-notebook/tree/main/additional-databases/neptune")
- [https://github.com/aws/graph-explorer/blob/main/additionaldocs/getting-started/README.md#amazon-ec2-setup](https://github.com/aws/graph-explorer/blob/main/additionaldocs/getting-started/README.md#amazon-ec2-setup "https://github.com/aws/graph-explorer/blob/main/additionaldocs/getting-started/README.md#amazon-ec2-setup")

###### Security configuration

When setting up your environment, please ensure the following security configurations are set accordingly:

- **Neptune cluster security group** - Allow incoming TCP traffic on port 8182 from
  your Amazon EC2 instance's security group.
- **Amazon EC2 instance security group** - Configure inbound HTTPS rules to enable Graph Explorer
  access.

We recommend using a single security group for both your Neptune cluster and Amazon EC2 instance. This simplifies
configuration and reduces potential connectivity issues. However, remember to add a self-referencing rule to allow
communication between resources within the group.
