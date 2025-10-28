# Create an Amazon SageMaker notebook instance

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

An Amazon SageMaker notebook instance is a ML compute instance running the Jupyter Notebook
application. SageMaker AI manages creating the instance and related resources. Use Jupyter
notebooks in your notebook instance to:

- prepare and process data
- write code to train models
- deploy models to SageMaker AI hosting
- test or validate your models
  To create a notebook instance, use either the SageMaker AI console or the [`CreateNotebookInstance`](../APIReference/API_CreateNotebookInstance.md "../APIReference/API_CreateNotebookInstance.md") API.

The notebook instance type you choose depends on how you use your notebook instance.
Ensure that your notebook instance is not bound by memory, CPU, or IO. To load a dataset
into memory on the notebook instance for exploration or preprocessing, choose an
instance type with enough RAM memory for your dataset. This requires an instance with at
least 16 GB of memory (.xlarge or larger). If you plan to use the notebook for compute
intensive preprocessing, we recommend you choose a compute-optimized instance such as a
c4 or c5.

A best practice when using a SageMaker notebook is to use the notebook instance to
orchestrate other AWS services. For example, you can use the notebook instance to
manage large dataset processing. To do this, make calls to AWS Glue for ETL (extract,
transform, and load) services or Amazon EMR for mapping and data reduction using Hadoop.
You can use AWS services as temporary forms of computation or storage for your
data.

You can store and retrieve your training and test data using an Amazon Simple Storage Service bucket. You
can then use SageMaker AI to train and build your model. As a result, the instance type of your
notebook would have no bearing on the speed of your model training and testing.

After receiving the request, SageMaker AI does the following:

- **Creates a network interface**—If you
  choose the optional VPC configuration, SageMaker AI creates the network interface in
  your VPC. It uses the subnet ID that you provide in the request to determine
  which Availability Zone to create the subnet in. SageMaker AI associates the security
  group that you provide in the request with the subnet. For more information, see
  [Connect a Notebook Instance in a
  VPC to External Resources](appendix-notebook-and-internet-access.md "appendix-notebook-and-internet-access.md").
- **Launches an ML compute instance**—SageMaker AI
  launches an ML compute instance in a SageMaker AI VPC. SageMaker AI performs the configuration
  tasks that allow it to manage your notebook instance. If you specified your VPC,
  SageMaker AI enables traffic between your VPC and the notebook instance.
- **Installs Anaconda packages and libraries for common deep
  learning platforms**—SageMaker AI installs all of the Anaconda
  packages that are included in the installer. For more information, see [Anaconda package
  list](https://docs.anaconda.com/free/anaconda/pkg-docs/ "https://docs.anaconda.com/free/anaconda/pkg-docs/"). SageMaker AI also installs the TensorFlow and Apache MXNet deep
  learning libraries.
- **Attaches an ML storage volume**—SageMaker AI
  attaches an ML storage volume to the ML compute instance. You can use the volume
  as a working area to clean up the training dataset or to temporarily store
  validation, test, or other data. Choose any size between 5 GB and 16384 GB, in 1
  GB increments, for the volume. The default is 5 GB. ML storage volumes are
  encrypted, so SageMaker AI can't determine the amount of available free space on the
  volume. Because of this, you can increase the volume size when you update a
  notebook instance, but you can't decrease the volume size. If you want to
  decrease the size of the ML storage volume in use, create a new notebook
  instance with the desired size.

Only files and data saved within the `/home/ec2-user/SageMaker`
folder persist between notebook instance sessions. Files and data that are saved
outside this directory are overwritten when the notebook instance stops and
restarts. Each notebook instance's /tmp directory provides a minimum of 10 GB of
storage in an instance store. An instance store is temporary, block-level
storage that isn't persistent. When the instance is stopped or restarted, SageMaker AI
deletes the directory's contents. This temporary storage is part of the root
volume of the notebook instance.

If the instance type used by the notebook instance has NVMe support, customers
can use the NVMe instance store volumes available for that instance type. For
instances with NVMe store volumes, all instance store volumes are automatically
attached to the instance at launch. For more information about instance types
and their associated NVMe store volumes, see the [Amazon Elastic Compute Cloud Instance Type Details](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

To make the attached NVMe store volume available for your notebook instance,
complete the steps in [Make instance store volumes available on your instance](../../../AWSEC2/latest/UserGuide/add-instance-store-volumes.md#making-instance-stores-available-on-your-instances "../../../AWSEC2/latest/UserGuide/add-instance-store-volumes.md#making-instance-stores-available-on-your-instances") . Complete
the steps with root access or by using a lifecycle configuration script.

###### Note

NVMe instance store volumes are not persistent storage. This storage is
short-lived with the instance and must be reconfigured every time an
instance with this storage is launched.

###### To create a SageMaker AI notebook instance:

1.  Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2.  Choose **Notebook instances**, then choose **Create
    notebook instance**.
3.  On the **Create notebook instance** page, provide the
    following information:
    1. For **Notebook instance name**, type a name for your
       notebook instance.
    2. For **Notebook instance type**, choose an instance
       size suitable for your use case. For a list of supported instance types
       and quotas, see [Amazon SageMaker AI
       Service Quotas](../../../general/latest/gr/sagemaker.md#limits_sagemaker "../../../general/latest/gr/sagemaker.md#limits_sagemaker").
    3. For **Platform Identifier**, choose a platform type
       to create the notebook instance on. This platform type dictates the
       Operating System and the JupyterLab version that your notebook instance
       is created with. The latest and recommended version is
       `notebook-al2023-v1`, for an Amazon Linux 2023 notebook instance.
       As of June 30, 2025, only JupyterLab 4 is supported
       for new instances. For information about platform identifier types, see
       [AL2023 notebook instances](nbi-al2023.md "nbi-al2023.md") and
       [Amazon Linux 2 notebook instances](nbi-al2.md "nbi-al2.md"). For information
       about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").

    ###### Important

    JupyterLab 1 and JupyterLab 3 are no longer supported as of June 30, 2025. You can no longer create new or restart stopped notebook instances using these versions. Existing in-service instances may continue to function but will not receive security updates or bug fixes. Migrate to JupyterLab 4 notebook instances for continued support. For more information, see [JupyterLab version maintenance](nbi-jl.md#nbi-jl-version-maintenance "nbi-jl.md#nbi-jl-version-maintenance"). 4. (Optional) **Additional configuration** lets advanced
    users create a shell script that can run when you create or start the
    instance. This script, called a lifecycle configuration script, can be
    used to set the environment for the notebook or to perform other
    functions. For information, see [Customization of a SageMaker notebook instance
    using an LCC script](notebook-lifecycle-config.md "notebook-lifecycle-config.md"). 5. (Optional) **Additional configuration** also lets you
    specify the size, in GB, of the ML storage volume that is attached to
    the notebook instance. You can choose a size between 5 GB and 16,384 GB,
    in 1 GB increments. You can use the volume to clean up the training
    dataset or to temporarily store validation or other data. 6. (Optional) For **Minimum IMDS Version**, select a
    version from the dropdown list. If this value is set to v1, both
    versions can be used with the notebook instance. If v2 is selected, then
    only IMDSv2 can be used with the notebook instance. For information
    about IMDSv2, see [Use IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md").

    ###### Note

    Starting October 31, 2022, the default minimum IMDS Version for
    SageMaker notebook instances changes from IMDSv1 to IMDSv2.

    Starting February 1, 2023, IMDSv1 is no longer be available for
    new notebook instance creation. After this date, you can create
    notebook instances with a minimum IMDS version of 2. 7. For **IAM role**, choose either an existing IAM
    role in your account with the necessary permissions to access SageMaker AI
    resources or **Create a new role**. If you choose
    **Create a new role**, SageMaker AI creates an IAM role
    named
    `AmazonSageMaker-ExecutionRole-`YYYYMMDD`T`HHmmSS``.
 The AWS managed policy `AmazonSageMakerFullAccess`
    is attached to the role. The role provides permissions that allow the
    notebook instance to call SageMaker AI and Amazon S3. 8. For **Root access**, to give root access for all
    notebook instance users, choose **Enable**. To remove
    root access for users, choose **Disable**.If you give
    root access, all notebook instance users have administrator privileges
    and can access and edit all files on it. 9. (Optional) **Encryption key** lets you encrypt data
    on the ML storage volume attached to the notebook instance using an
    AWS Key Management Service (AWS KMS) key. If you plan to store sensitive information on the
    ML storage volume, consider encrypting the information. 10. (Optional) **Network** lets you put your notebook
    instance inside a Virtual Private Cloud (VPC). A VPC provides additional
    security and limits access to resources in the VPC from sources outside
    the VPC. For more information on VPCs, see [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

    **To add your notebook instance to a
    VPC:**

        1. Choose the **VPC** and a
         **SubnetId**.
        2. For **Security Group**, choose your VPC's
         default security group.
        3. If you need your notebook instance to have internet access,
         enable direct internet access. For **Direct internet
         access**, choose **Enable**.
         Internet access can make your notebook instance less secure. For
         more information, see [Connect a Notebook Instance in a
         VPC to External Resources](appendix-notebook-and-internet-access.md "appendix-notebook-and-internet-access.md").

    11. (Optional) To associate Git repositories with the notebook instance,
        choose a default repository and up to three additional repositories. For
        more information, see [Git repositories with SageMaker AI Notebook Instances](nbi-git-repo.md "nbi-git-repo.md").
    12. Choose **Create notebook instance**.

    In a few minutes, Amazon SageMaker AI launches an ML compute instance—in
    this case, a notebook instance—and attaches an ML storage volume
    to it. The notebook instance has a preconfigured Jupyter notebook server
    and a set of Anaconda libraries. For more information, see the [`CreateNotebookInstance`](../APIReference/API_CreateNotebookInstance.md "../APIReference/API_CreateNotebookInstance.md") API.

4.  When the status of the notebook instance is `InService`, in the
    console, the notebook instance is ready to use. Choose **Open
    Jupyter** next to the notebook name to open the classic Jupyter
    dashboard.

###### Note

To augment the security of your Amazon SageMaker notebook instance, all regional
``notebook`.`region`.sagemaker.aws`  domains are registered in the internet [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For
 further security, we recommend that you use cookies with a
 `\_\_Host-` prefix to set sensitive cookies for the domains of
your SageMaker notebook instances. This helps to defend your domain against
cross-site request forgery attempts (CSRF). For more information, see the
[Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the [mozilla.org](https://www.mozilla.org/en-GB/?v=1 "https://www.mozilla.org/en-GB/?v=1") developer
documentation website.

You can choose **Open JupyterLab** to open the JupyterLab
dashboard. The dashboard provides access to your notebook instance.

For more information about Jupyter notebooks, see [The Jupyter
notebook](https://jupyter-notebook.readthedocs.io/en/stable/ "https://jupyter-notebook.readthedocs.io/en/stable/").
