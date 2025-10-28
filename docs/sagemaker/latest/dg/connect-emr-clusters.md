# Connect to an Amazon EMR cluster from SageMaker Studio

or Studio Classic

Data scientists and data engineers can discover and then connect to an Amazon EMR cluster
directly from the Studio user interface. Before you begin, ensure that you have
configured the necessary permissions as described in the [Step 4: Set up the permissions to enable
listing and launching Amazon EMR clusters from Studio](studio-notebooks-set-up-emr-templates.md#studio-emr-permissions "studio-notebooks-set-up-emr-templates.md#studio-emr-permissions") section.
These permissions grant Studio the ability to create, start, view, access, and
terminate clusters.

You can connect an Amazon EMR cluster to a new JupyterLab notebook directly from the
Studio UI, or choose to initiate the connection in a notebook of a running
JupyterLab application.

###### Important

You can only discover and connect to Amazon EMR clusters for JupyterLab and Studio Classic
applications that are launched from private spaces. Ensure that the Amazon EMR clusters
are located in the same AWS region as your Studio environment. Your
JupyterLab space must use a SageMaker Distribution image version `1.10` or
higher.

## Connect to an Amazon EMR cluster using

the Studio UI

To connect to your cluster using the Studio or Studio Classic UI, you can either
initiate a connection from the list of clusters accessed in [List Amazon EMR clusters from Studio or
Studio Classic](discover-emr-clusters.md "discover-emr-clusters.md"), or from
a notebook in SageMaker Studio or Studio Classic.

###### To connect an Amazon EMR cluster to a new JupyterLab notebook from the

Studio UI:

1. In the Studio UI's left-side panel, select the
   **Data** node in the left navigation menu. Navigate
   down to **Amazon EMR applications and clusters**. This opens up
   a page listing the Amazon EMR clusters that you can access from Studio in
   the **Amazon EMR clusters** tab.

###### Note

If you or your administrator have configured the permissions to allow
cross-account access to Amazon EMR clusters, you can view a consolidated list
of clusters across all accounts that you have granted access to
Studio. 2. Select an Amazon EMR cluster you want to connect to a new notebook, and then
choose **Attach to notebook**. This opens up a modal window
displaying the list of your JupyterLab spaces. 3. _ Select the space from which you want to launch a JupyterLab
application, and then choose **Open notebook**.
This launches a JupyterLab application from your chosen space and
opens a new notebook. ###### Note
Users of Studio Classic need to select an image and kernel. For a
list of supported images, see [Supported images and
kernels to connect to an Amazon EMR cluster from Studio or Studio Classic](studio-emr-user-guide.md#studio-notebooks-emr-cluster-connect-kernels "studio-emr-user-guide.md#studio-notebooks-emr-cluster-connect-kernels") or refer to [Bring your own image](studio-emr-user-guide.md#studio-notebooks-emr-byoi "studio-emr-user-guide.md#studio-notebooks-emr-byoi").
_ Alternatively, you can create a new private space by choosing the
**Create new space** button at the top of the
modal window. Enter a name for your space and then choose
**Create space and open notebook**. This
creates a private space with the default instance type and latest
SageMaker distribution image available, launches a JupyterLab
application, and opens a new notebook. 4. If the cluster you select does not use Kerberos, LDAP, or runtime role
authentication, Studio prompts you to select the credential type.
Choose from **Http basic authentication** or **No
credentials**, then enter your credentials, if
applicable.

If the cluster you select supports runtime roles, choose the name of the
IAM role that your Amazon EMR cluster can assume for the job run.

###### Important

To successfully connect a JupyterLab notebook to an Amazon EMR cluster
supporting runtime roles, you must first associate the list of runtime
roles with your domain or user profile, as outlined in [Configure IAM runtime roles for Amazon EMR
cluster access in Studio](studio-notebooks-emr-cluster-rbac.md "studio-notebooks-emr-cluster-rbac.md") . Failing to complete
this step will prevent you from establishing the connection.

Upon selection, a connection command populates the first cell of your
notebook and initiates the connection with the Amazon EMR cluster.

Once the connection succeeds, a message confirms the connection and the
start of the Spark application.

###### Alternatively, you can connect to a cluster from a JupyterLab or Studio Classic

notebook.

1. Choose the **Cluster** button at the top of your
   notebook. This opens a modal window listing the Amazon EMR clusters in a
   `Running` state that you can access. You can see the
   `Running` Amazon EMR clusters in the **Amazon EMR
   clusters** tab.

###### Note

For the users of Studio Classic, **Cluster** is only
visible when you use a kernel from [Supported images and
kernels to connect to an Amazon EMR cluster from Studio or Studio Classic](studio-emr-user-guide.md#studio-notebooks-emr-cluster-connect-kernels "studio-emr-user-guide.md#studio-notebooks-emr-cluster-connect-kernels") or
from [Bring your own image](studio-emr-user-guide.md#studio-notebooks-emr-byoi "studio-emr-user-guide.md#studio-notebooks-emr-byoi"). If you cannot see
**Cluster** at the top of your notebook, ensure
that your administrator has [configured the discoverability of your clusters](studio-notebooks-configure-discoverability-emr-cluster.md "studio-notebooks-configure-discoverability-emr-cluster.md") and switch
to a supported kernel. 2. Select the cluster to which you want to connect, then choose
**Connect**. 3. If you configured your Amazon EMR clusters to support [runtime IAM roles](studio-notebooks-emr-cluster-rbac.md "studio-notebooks-emr-cluster-rbac.md"),
you can select your role from the **Amazon EMR execution role**
drop down menu.

###### Important

To successfully connect a JupyterLab notebook to an Amazon EMR cluster
supporting runtime roles, you must first associate the list of runtime
roles with your domain or user profile, as outlined in [Configure IAM runtime roles for Amazon EMR
cluster access in Studio](studio-notebooks-emr-cluster-rbac.md "studio-notebooks-emr-cluster-rbac.md") . Failing to complete
this step will prevent you from establishing the connection.

Otherwise, if the cluster you choose does not use Kerberos, LDAP, or
runtime role authentication, Studio or Studio Classic prompts you to select
the credential type. You can choose **HTTP basic
authentication** or **No credential**. 4. Studio adds and then run a code block to an active cell to establish
the connection. This cell contains the connection magic command to connect
your notebook to your application according to your authentication
type.

Once the connection succeeds, a message confirms the connection and the
start of the Spark application.

## Connect to an Amazon EMR cluster using a

connection command

To establish a connection to an Amazon EMR cluster, you can execute connection commands
within a notebook cell.

When establishing the connection, you can authenticate using [Kerberos](../../../emr/latest/ManagementGuide/emr-kerberos.md "../../../emr/latest/ManagementGuide/emr-kerberos.md"), [Lightweight Directory
Access Protocol (LDAP)](../../../index.md "../../../index.md"), or [runtime IAM
role](studio-notebooks-emr-cluster-rbac.md "studio-notebooks-emr-cluster-rbac.md") authentication. The authentication method you choose depends on
your cluster configuration.

You can refer to this example [Access Apache Livy using a Network Load Balancer on a Kerberos-enabled Amazon EMR
cluster](https://aws.amazon.com/blogs/big-data/access-apache-livy-using-a-network-load-balancer-on-a-kerberos-enabled-amazon-emr-cluster/ "https://aws.amazon.com/blogs/big-data/access-apache-livy-using-a-network-load-balancer-on-a-kerberos-enabled-amazon-emr-cluster/") to set up an Amazon EMR cluster that uses Kerberos authentication.
Alternatively, you can explore the CloudFormation example templates using Kerberos or
LDAP authentication in the [aws-samples/sagemaker-studio-emr](https://github.com/aws-samples/sagemaker-studio-emr/tree/main/cloudformation/getting_started "https://github.com/aws-samples/sagemaker-studio-emr/tree/main/cloudformation/getting_started") GitHub repository.

If your administrator has enabled cross-account access, you can connect to your
Amazon EMR cluster from a Studio Classic notebook, regardless of whether your Studio Classic
application and cluster reside in the same AWS account or different
accounts.

For each of the following authentication types, use the specified command to
connect to your cluster from your Studio or Studio Classic notebook.

- **Kerberos**

Append the `--assumable-role-arn` argument if you need
cross-account Amazon EMR access. Append the `--verify-certificate`
argument if you connect to your cluster with HTTPS.

```
%load_ext sagemaker_studio_analytics_extension.magics
%sm_analytics emr connect --cluster-id `cluster_id` \
--auth-type Kerberos --language python
[--assumable-role-arn `EMR_access_role_ARN` ]
[--verify-certificate `/home/user/certificateKey.pem`]
```

- **LDAP**

Append the `--assumable-role-arn` argument if you need
cross-account Amazon EMR access. Append the `--verify-certificate`
argument if you connect to your cluster with HTTPS.

```
%load_ext sagemaker_studio_analytics_extension.magics
%sm_analytics emr connect --cluster-id `cluster_id` \
--auth-type Basic_Access --language python
[--assumable-role-arn `EMR_access_role_ARN` ]
[--verify-certificate `/home/user/certificateKey.pem`]
```

- **NoAuth**

Append the `--assumable-role-arn` argument if you need
cross-account Amazon EMR access. Append the `--verify-certificate`
argument if you connect to your cluster with HTTPS.

```
%load_ext sagemaker_studio_analytics_extension.magics
%sm_analytics emr connect --cluster-id `cluster_id` \
--auth-type None --language python
[--assumable-role-arn `EMR_access_role_ARN` ]
[--verify-certificate `/home/user/certificateKey.pem`]
```

- **Runtime IAM roles**

Append the `--assumable-role-arn` argument if you need
cross-account Amazon EMR access. Append the `--verify-certificate`
argument if you connect to your cluster with HTTPS.

For more information on connecting to an Amazon EMR cluster using runtime IAM
roles, see [Configure IAM runtime roles for Amazon EMR
cluster access in Studio](studio-notebooks-emr-cluster-rbac.md "studio-notebooks-emr-cluster-rbac.md") .

```
%load_ext sagemaker_studio_analytics_extension.magics
%sm_analytics emr connect --cluster-id `cluster_id` \
--auth-type Basic_Access \
--emr-execution-role-arn arn:aws:iam::`studio_account_id`:role/`emr-execution-role-name`
[--assumable-role-arn `EMR_access_role_ARN`]
[--verify-certificate `/home/user/certificateKey.pem`]
```

## Connect to an Amazon EMR cluster over

HTTPS

If you have configured your Amazon EMR cluster with transit encryption enabled and
Apache Livy server for HTTPS and would like Studio or Studio Classic to communicate
with Amazon EMR using HTTPS, you need to configure Studio or Studio Classic to access
your certificate key.

For self-signed or local Certificate Authority (CA) signed certificates, you can
do this in two steps:

1. Download the PEM file of your certificate to your local file system using
   one of the following options:
   - Jupyter's built-in file upload function.
   - A notebook cell.
   - (For Studio Classic users only) A lifecycle configuration (LCC)
     script.

   For information on how to use an LCC script, see [Customize a Notebook Instance Using a Lifecycle Configuration
   Script](notebook-lifecycle-config.md "notebook-lifecycle-config.md")

2. Enable the validation of the certificate by providing the path to your
   certificate in the `--verify-certificate` argument of your
   connection command.

```
%sm_analytics emr connect --cluster-id `cluster_id` \
--verify-certificate `/home/user/certificateKey.pem` ...
```

For public CA issued certificates, set the certificate validation by setting the
`--verify-certificate` parameter as `true`.

Alternatively, you can disable the certificate validation by setting the
`--verify-certificate` parameter as `false`.

You can find the list of available connection commands to an Amazon EMR cluster in
[Connect to an Amazon EMR cluster using a
connection command](#connect-emr-clusters-manually "#connect-emr-clusters-manually").
