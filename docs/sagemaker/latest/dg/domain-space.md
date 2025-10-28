# Collaboration with shared spaces

An Amazon SageMaker Studio Classic shared space consists of a shared JupyterServer application and a shared
directory. A JupyterLab shared space consists of a shared JupyterLab application and a shared
directory within Amazon SageMaker Studio. All user profiles in a domain have access to all shared spaces
in the domain. Amazon SageMaker AI automatically scopes resources in a shared space within the context of the
Amazon SageMaker Studio Classic application that you launch in that shared space. Resources in a shared space include
notebooks, files, experiments, and models. Use shared spaces to collaborate with other users in
real-time using features like automatic tagging, real time co-editing of notebooks, and
customization.

Shared spaces are available in:

- Amazon SageMaker Studio Classic
- JupyterLab
  A Studio Classic shared space only supports Studio Classic and KernelGateway applications. A shared space only
  supports the use of a JupyterLab 3 image Amazon Resource Name (ARN). For more information, see
  [JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md "studio-jl.md").

Amazon SageMaker AI automatically tags all SageMaker AI resources that you create within the scope of a
shared space. You can use these tags to monitor costs and plan budgets using tools, such as
AWS Budgets.

A shared space uses the same VPC settings as the domain that it's created in.

###### Note

Shared spaces do not support the use of Amazon SageMaker Data Wrangler or Amazon EMR cross-account clusters.

**Automatic tagging**

All resources created in a shared space are automatically tagged with a domain ARN tag and
shared space ARN tag. The domain ARN tag is based on the domain ID, while the shared space ARN tag
is based on the shared space name.

You can use these tags to monitor AWS CloudTrail usage. For more information,
see [Log
Amazon SageMaker API Calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

You can also use these tags to monitor costs with AWS Billing and Cost Management. For
more information, see [Using AWS cost allocation
tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").

**Real time co-editing of notebooks**

A key benefit of a shared space is that it facilitates collaboration between members of the
shared space in real time. Users collaborating in a workspace get access to a shared Studio Classic
application where they can access, read, and edit their notebooks in real time. Real time
collaboration is only supported for JupyterServer applications within a shared space.

Users with access to a shared space can simultaneously open, view, edit, and execute Jupyter
notebooks in the shared Studio Classic or JupyterLab application in that space.

The notebook indicates each co-editing user with a different cursor that shows the user
profile name. While multiple users can view the same notebook, co-editing is best suited for
small groups of two to five users.

To track changes being made by multiple users, we strongly recommended using Studio Classic's
built-in Git-based version control.

**JupyterServer 2**

To use shared spaces in Studio Classic, Jupyter Server version 2 is required. Certain JupyterLab extensions and
packages can forcefully downgrade Jupyter Server to version 1. This prevents the use of shared space.
Run the following from the command prompt to change the version number and continue using
shared spaces.

```
conda activate studio
pip install jupyter-server==2.0.0rc3
```

**Customize a shared space**

To attach a lifecycle configuration or custom image to a shared space, you must use the
AWS CLI. For more information about creating and attaching lifecycle configurations, see [Create and Associate a Lifecycle Configuration with Amazon SageMaker Studio Classic](studio-lcc-create.md "studio-lcc-create.md"). For more information about
creating and attaching custom images, see [Custom Images in Amazon SageMaker Studio Classic](studio-byoi.md "studio-byoi.md").
