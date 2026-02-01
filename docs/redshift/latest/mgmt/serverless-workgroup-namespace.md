Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Workgroups and namespaces

To isolate workloads and manage different resources in Amazon Redshift Serverless, you can
create namespaces and workgroups and manage storage and compute resources
separately.

A namespace is a collection of database objects and users. The storage-related
namespace groups together schemas, tables, users, or AWS Key Management Service keys for encrypting data.
Storage properties include the database name and password of the admin user,
permissions, and encryption and security. Other resources that are grouped under
namespaces include datashares, recovery points, and usage limits. You can configure
these storage properties using the Amazon Redshift Serverless console, the AWS Command Line Interface, or the Amazon Redshift Serverless
APIs for the specific resource.

Workgroup is a collection of compute resources. The compute-related workgroup groups
together compute resources like RPUs, VPC subnet groups, and security groups. Properties
for the workgroup include network and security settings. Other resources that are
grouped under workgroups include access and usage limits. You can configure these
compute properties using the Amazon Redshift Serverless console, the AWS Command Line Interface, or the Amazon Redshift Serverless
APIs.

You can create one or more namespaces and workgroups. Each namespace can have only one
workgroup associated with it. Conversely, each workgroup can be associated with only one
namespace.

## Workgroups and namespaces

using the console

Setting up Amazon Redshift Serverless involves walking through several configuration steps. When
you follow the steps to set up Amazon Redshift Serverless, you create a namespace and workgroup, and
associate them with each other. To get started setting Amazon Redshift Serverless configuration using
the Amazon Redshift Serverless console, you can choose **Get started with
Amazon Redshift Serverless** to set up Amazon Redshift Serverless and begin to interact with it. You can
choose an environment with default settings, which makes for quicker setup, or
explicitly configure the settings per your organization's requirements.During this
process, you specify settings for your workgroup and namespace.

After you set up the environment, [Workgroup properties](serverless-console-workgroups.md#serverless-workgroup-describe "serverless-console-workgroups.md#serverless-workgroup-describe") and [Namespace properties](serverless-console-configure-namespace-working.md#serverless-console-namespace-config "serverless-console-configure-namespace-working.md#serverless-console-namespace-config") help you get familiar with
the settings.

## Workgroups and namespaces

using the AWS Command Line Interface and Amazon Redshift Serverless API

Aside from using the AWS console, you can also use the AWS CLI or the Amazon Redshift Serverless
API to interact with workgroups and namespaces. The table below lists the API and
CLI operations you can use to manage snapshots and recovery points.

| API operation                                                                                                                                                        | CLI command      | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CreateNamespace](../../../redshift-serverless/latest/APIReference/API_CreateNamespace.md "../../../redshift-serverless/latest/APIReference/API_CreateNamespace.md") | create-namespace | Creates a namespace. By default, Amazon Redshift Serverless creates<br>namespaces with a default AWS Key Management Service key, but you can specify<br>another key to encrypt your data. You can also create a<br>namespace by restoring a snapshot. See [Working with snapshots and recovery points](serverless-snapshots-recovery.md "serverless-snapshots-recovery.md") for more<br>information. |
| [UpdateNamespace](../../../redshift-serverless/latest/APIReference/API_UpdateNamespace.md "../../../redshift-serverless/latest/APIReference/API_UpdateNamespace.md") | update-namespace | Updates a namespace.                                                                                                                                                                                                                                                                                                                                                                                 |
| [GetNamespace](../../../redshift-serverless/latest/APIReference/API_GetNamespace.md "../../../redshift-serverless/latest/APIReference/API_GetNamespace.md")          | get-namespace    | Retrieves information about a namespace                                                                                                                                                                                                                                                                                                                                                              |
| [ListNamepaces](../../../redshift-serverless/latest/APIReference/API_ListNamespaces.md "../../../redshift-serverless/latest/APIReference/API_ListNamespaces.md")     | list-namespaces  | Retrieves information about a list of<br>namespaces.                                                                                                                                                                                                                                                                                                                                                 |
| [DeleteNamespace](../../../redshift-serverless/latest/APIReference/API_DeleteNamespace.md "../../../redshift-serverless/latest/APIReference/API_DeleteNamespace.md") | delete-namespace | Deletes a namespace.                                                                                                                                                                                                                                                                                                                                                                                 |
| [CreateWorkgroup](../../../redshift-serverless/latest/APIReference/API_CreateWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_CreateWorkgroup.md") | create-workgroup | Creates a workgroup. When creating a workgroup, make sure<br>that you have an existing namespace that you can associate with<br>the workgroup. When creating the workgroup, you can specify<br>compute resources such as subnets, security groups, and<br>RPUs.                                                                                                                                      |
| [UpdateWorkgroup](../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_UpdateWorkgroup.md") | update-workgroup | Updates a workgroup.                                                                                                                                                                                                                                                                                                                                                                                 |
| [GetWorkgroup](../../../redshift-serverless/latest/APIReference/API_GetWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_GetWorkgroup.md")          | get-workgroup    | Retrieves information about a workgroup.                                                                                                                                                                                                                                                                                                                                                             |
| [ListWorkgroups](../../../redshift-serverless/latest/APIReference/API_ListWorkgroups.md "../../../redshift-serverless/latest/APIReference/API_ListWorkgroups.md")    | list-workgroups  | Retrieves information about a list of<br>workgroups.                                                                                                                                                                                                                                                                                                                                                 |
| [DeleteWorkgroup](../../../redshift-serverless/latest/APIReference/API_DeleteWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_DeleteWorkgroup.md") | delete-workgroup | Deletes a workgroup.                                                                                                                                                                                                                                                                                                                                                                                 |
