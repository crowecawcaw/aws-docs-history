Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Onboarding

## Redshift cluster registration

Redshift supports creating a new cluster or restoring a cluster from snapshot with AWS Glue Data Catalog (GDC)
registration. You can specify the GDC catalog name part of this registration. To support IdC
identity propagation you can specify a Redshift IdC application arn of Lakehouse
type to enable IdC identity propagation.

**Create a new cluster with Glue data catalog registration**

CLI
To automatically register your newly created cluster with Data Catalog, provide the catalog-name
that will be used to create and register your Data Catalog. The `redshift-idc-application-arn`
parameter is optional - include it if you want to link your cluster with the
Redshift IdC Application of type Lakehouse. You can also establish this IdC application
association at a later time.

```
aws redshift create-cluster \
    --cluster-identifier 'redshift-cluster' \
   --catalog-name 'glue-data-catalog-name' \
   --redshift-idc-application-arn 'arn:aws:redshift:us-east-1:012345678912:redshiftidcapplication:3f966e50-f1b7-495c-8ace-bd0d6c3c3b17' \
   --<other_configurations_as_needed>
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the provisioned clusters dashboard and select **Create cluster**.
3. Configure your general cluster settings.
4. In Register with AWS Glue Data Catalog section, select **Register with Amazon Redshift federated permissions**.
   - Input a catalog name identifier.
   - (Recommended) Select Amazon Redshift federated permissions using AWS IAM Identity Center to associate with Redshift IDC application.

5. Complete the remaining cluster settings and choose **Create cluster**.

**Restore a new cluster with AWS Glue Data Catalog registration**

CLI
To restore a snapshot into a new cluster with AWS Glue Data Catalog integration, provide the catalog-name
that will be used to create and register your AWS Glue catalog. The `redshift-idc-application-arn`
parameter is optional - include it if you want to link your cluster with the Redshift IdC
Application of type Lakehouse. You can also establish this IdC aspplication association at a later time.

```
aws redshift restore-from-cluster-snapshot \
   --cluster-identifier 'redshift-cluster' \
   --catalog-name 'glue-data-catalog-name' \
   --snapshot-identifier 'redshift-cluster-snapshot' \
   --redshift-idc-application-arn 'arn:aws:redshift:us-east-1:012345678912:redshiftidcapplication:3f966e50-f1b7-495c-8ace-bd0d6c3c3b17' \
   --<other_configurations_as_needed>
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the provisioned snapshots page. From the snapshots table, select **Restore to
   provisioned cluster** from the **Restore snapshot** drop-down menu.
3. Configure general cluster settings.
4. In Register with AWS Glue Data Catalog section, select **Register with Amazon Redshift federated permissions**.
   - Input a catalog name identifier.
   - (Recommended) Select Amazon Redshift federated permissions using AWS IAM Identity Center to associate with Redshift IDC application.

5. Complete the remaining cluster settings and choose **Create cluster**.

**Modify an existing cluster with AWS Glue Data Catalog registration**

If your Redshift cluster is already associated to a Redshift IdC Application of type non-lakehouse, the
following occurs during AWS Glue Data Catalog registration:

- When no Redshift IdC Application ARN is provided, the existing Redshift IdC Application in your catalog will be set to disabled status.
- When a Redshift IdC Application of type Lakehouse from different AWS IAM Identity Center instance is specified, the current IdC provider becomes disabled
- When a Redshift IdC Application of type Lakehouse from the same AWS IAM Identity Center instance is provided
  - The Redshift IdC Application ARN in your catalog will be changed to the ARN of the Redshift
    IdC Application of type Lakehouse. The updated catalog can be checked by querying the
    svv_identity_providers. For more information about the svv_identity_providers,
    see [svv_identity_providers](r_SVV_IDENTITY_PROVIDERS.md "r_SVV_IDENTITY_PROVIDERS.md").
  - AWS IAM Identity Center federated users who previously had access to the Redshift cluster,
    must be explicitly granted CONNECT privileges by the Admins to access the cluster. For more
    information about granting CONNECT privileges, see [Connect privileges](federated-permissions-prereqs.md#federated-permissions-prereqs-connect "federated-permissions-prereqs.md#federated-permissions-prereqs-connect").
  - After registering with AWS Glue Data Catalog, your existing AWS IAM Identity Center federated identities
    and their owned resources remain unchanged. The namespace associations for these
    federated identities are also preserved.

CLI
You can use `modify-lakehouse-configuration` command to register your cluster to
AWS Glue Data Catalog, the the `catalog-name` is used to create and register your AWS Glue catalog.
To support IdC identity propagation, specify the arn of your lakehouse type RedshiftIdcApplication,
this requires a Redshift IdC Application of type Lakehouse, please
refer to [Create a new Lakehouse type Redshift IdC application: Identity Center Application Configuration for Redshift
Warehouse with federated permissions](federated-permissions-prereqs.md#federated-permissions-prereqs-configuration "federated-permissions-prereqs.md#federated-permissions-prereqs-configuration").

```
aws redshift modify-lakehouse-configuration \
    --cluster-identifier 'redshift-cluster' \
    --lakehouse-registration Register \
    --catalog-name 'glue-data-catalog-name' \
    --lakehouse-idc-registration Associate \
    --lakehouse-idc-application-arn 'arn:aws:redshift:us-east-1:012345678912:redshiftidcapplication:3f966e50-f1b7-495c-8ace-bd0d6c3c3b17' \
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the provisioned cluster that you want to register and select it.
3. From the cluster’s details page, select **Register with AWS Glue Data Catalog** from the **Actions**
   drop-down menu.
4. Select **Register with Amazon Redshift federated permissions** option and
   - Input a catalog name identifier.
   - (Recommended) Select Amazon Redshift federated permissions using AWS IAM Identity Center to associate with Redshift IDC application and choose **Register**.

## Redshift Serverless namespace registration

Redshift Serverless enables workgroup-attached Serverless namespaces to register with AWS Glue Data Catalog. Note that your
database will restart during this update.

If your Redshift Serverless Namespace is already associated to a Redshift IdC Application of type non-lakehouse,
the following occurs during Glue Data Catalog registration:

- When no Redshift IdC Application ARN is provided, the existing Redshift IdC Application in your catalog will be set to disabled status.
- When a Redshift IdC Application of type Lakehouse from different AWS IAM Identity Center instance is specified, the current IdC provider becomes disabled
- When a Redshift IdC Application of type Lakehouse from the same AWS IAM Identity Center instance is provided
  - The Redshift IdC Application ARN in your catalog will be changed to the ARN of the Redshift
    IdC Application of type Lakehouse. The updated catalog can be checked by querying the
    svv_identity_providers. For more information about the svv_identity_providers,
    see [svv_identity_providers](r_SVV_IDENTITY_PROVIDERS.md "r_SVV_IDENTITY_PROVIDERS.md").
  - AWS IAM Identity Center federated users who previously had access to the Redshift cluster,
    must be explicitly granted CONNECT privileges by the Admins to access the cluster. For more
    information about granting CONNECT privileges, see [Connect privileges](federated-permissions-prereqs.md#federated-permissions-prereqs-connect "federated-permissions-prereqs.md#federated-permissions-prereqs-connect").
  - After registering with AWS Glue Data Catalog, your existing AWS IAM Identity Center federated identities
    and their owned resources remain unchanged. The namespace associations for these
    federated identities are also preserved.

CLI
You can use `update-lakehouse-configuration` command to register your Redshift Serverless namespace to
AWS Glue Data Catalog, the `catalog-name` is used to create and register your glue catalog. To support IdC identity propagation, specify the arn of a Redshift Idc Application of type Lakehouse.

```
aws redshift-serverless update-lakehouse-configuration \
    --namespace-name 'serverless-namespace-name' \
    --lakehouse-registration Register \
    --catalog-name 'glue-data-catalog-name' \
    --lakehouse-idc-registration Associate \
    --lakehouse-idc-application-arn 'arn:aws:redshift:us-east-1:012345678912:redshiftidcapplication:3f966e50-f1b7-495c-8ace-bd0d6c3c3b17'

```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the provisioned cluster that you want to register and select it.
3. From the cluster’s details page, select **Register with AWS Glue Data Catalog** from the **Actions**
   drop-down menu.
4. Select **Register with Amazon Redshift federated permissions** option and
   - Input a catalog name identifier.
   - (Recommended) Select Amazon Redshift federated permissions using AWS IAM Identity Center to associate with Redshift IDC application and choose **Register**.

## Enable AWS IAM Identity Center identity propagation

Amazon Redshift supports Identity Center (IdC) identity propagation to seamlessly pass IdC user identities
between Redshift instances and AWS Lake Formation/AWS Glue services.

**Prerequisites**

- You have created an Amazon Redshift IdC Application of type Lakehouse, refer to
  [AWS IAM Identity Center application configuration for Redshift warehouse with federated permissions](federated-permissions-prereqs.md#federated-permissions-prereqs-configuration "federated-permissions-prereqs.md#federated-permissions-prereqs-configuration").
- You have an Amazon Redshift Cluster or Amazon Redshift Serverless Namespace that is registered with AWS Glue Data Catalog.
  - Redshift Serverless Namespace requires workgroup attached to perform the related operations.

If your Redshift Cluster or Redshift Serverless Namespace is already associated to a Redshift IdC Application
of type other than Lakehouse, the following occurs during AWS Glue Data Catalog registration:

- When no Redshift IdC Application ARN is provided, the existing Redshift IdC Application in your catalog will be set to disabled status.
- When a Redshift IdC Application of type Lakehouse from different AWS IAM Identity Center instance is specified, the current IdC provider becomes disabled
- When a Redshift IdC Application of type Lakehouse from the same AWS IAM Identity Center instance is provided
  - The Redshift IdC Application ARN in your catalog will be changed to the ARN of the Redshift
    IdC Application of type Lakehouse. The updated catalog can be checked by querying the
    svv_identity_providers. For more information about the svv_identity_providers,
    see [svv_identity_providers](r_SVV_IDENTITY_PROVIDERS.md "r_SVV_IDENTITY_PROVIDERS.md").
  - AWS IAM Identity Center federated users who previously had access to the Redshift cluster,
    must be explicitly granted CONNECT privileges by the Admins to access the cluster. For more
    information about granting CONNECT privileges, see [Connect privileges](federated-permissions-prereqs.md#federated-permissions-prereqs-connect "federated-permissions-prereqs.md#federated-permissions-prereqs-connect").
  - After registering with AWS Glue Data Catalog, your existing AWS IAM Identity Center federated identities
    and their owned resources remain unchanged. The namespace associations for these
    federated identities are also preserved.

### Enable AWS IAM Identity Center identity propagation for Amazon Redshift provisioned clusters

For Amazon Redshift Provisioned Cluster that registered its namespace to AWS Glue Data Catalog, it requires Lakehouse
Amazon Redshift IdC Application which doesn’t require explicitly AWS IAM Identity Center Identity user assignment to the
application, the IdC users login privilege is managed by CONNECT privilege on the Redshift warehouse.

CLI
You can use `modify-lakehouse-configuration` command to enable IdC identity propagation for your clusters with
Redshift federated permissions, specify the arn of your lakehouse type RedshiftIdcApplication,
this requires a Redshift Lakehouse IdC Application please refer to [Create a new Lakehouse type Redshift IdC application: Identity Center Application Configuration for Redshift
Warehouse with federated permissions](federated-permissions-prereqs.md#federated-permissions-prereqs-configuration "federated-permissions-prereqs.md#federated-permissions-prereqs-configuration").

```
aws redshift modify-lakehouse-configuration \
    --cluster-identifier 'redshift-cluster' \
    --lakehouse-idc-registration Associate \
    --lakehouse-idc-application-arn 'arn:aws:redshift:us-east-1:012345678912:redshiftidcapplication:3f966e50-f1b7-495c-8ace-bd0d6c3c3b17' \

```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the provisioned cluster that you want to register and select it.
3. From the cluster’s details page, select **Register with AWS Glue Data Catalog** from the **Actions**
   drop-down menu.
4. Select **Enable** from the Amazon Redshift federated permissions using AWS IAM Identity Center drop-down to associate IDC application and choose **Save changes**.

### Enable AWS IAM Identity Center identity propagation for Amazon Redshift Serverless namespaces

CLI
You can use `modify-lakehouse-configuration` command to enable IdC identity propagation for your namespace with
Redshift federated permissions, specify the arn of your lakehouse type RedshiftIdcApplication,
this requires a Redshift Lakehouse IdC Application please refer to [Create a new Lakehouse type Redshift IdC application: Identity Center Application Configuration for Redshift
Warehouse with federated permissions](federated-permissions-prereqs.md#federated-permissions-prereqs-configuration "federated-permissions-prereqs.md#federated-permissions-prereqs-configuration").

```
aws redshift modify-lakehouse-configuration \
    --cluster-identifier 'redshift-cluster' \
    --lakehouse-idc-registration Associate \
    --lakehouse-idc-application-arn 'arn:aws:redshift:us-east-1:012345678912:redshiftidcapplication:3f966e50-f1b7-495c-8ace-bd0d6c3c3b17' \

```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the serverless namespace that you want to edit registration for and select it.
3. From the cluster’s details page, select **Edit AWS Glue Data Catalog registration** from the **Actions**
   drop-down menu.
4. Select **Enable** from the Amazon Redshift federated permissions using AWS IAM Identity Center drop-down to associate IDC application and choose **Save changes**.

## ALTER USER SET GLOBAL IDENTITY

In addition to IAM and AWS IAM Identity Center credentials, the user running queries against Redshift Warehouses with
federated permissions can authenticate using an IAM role. A superuser can set an IAM role for another non-federated user to associate automatically at session establishment, and this
IAM role will be assumed when making queries against Redshift Warehouses with Federated Permissions. This functionality is provided to allow AWS IdC users to authenticate non-interactively.

This feature is useful for following use cases:

- Customers that have large and complex setups with existing local warehouse user in addition to users with global identity.
- Customers who use IdC, but who wish to be able to log in automatically without interactive browser action to log in.

Requirements and limitations:

- Only super user can set the IAM role by `ALTER USER`.
- IAM role must be attached to the cluster.
- IAM role must have permissions to access resources needed to run queries on Redshift warehouses with federated permissions.
  We recommend using `AmazonRedshiftFederatedAuthorization` AWS managed policy.
- The users authenticating via GLOBAL IDENTITY IAM role can query views in Redshift Warehouses with Federated Permissions, but cannot CREATE, ALTER, REFRESH or DROP them.

### Syntax

The following syntax describes the `ALTER USER SET GLOBAL IDENTITY` command used to set IAM role for a non-federated database user to run queries against Redshift Warehouses with Federated Permissions.

```
ALTER USER `username` SET
GLOBAL IDENTITY IAM_ROLE 'arn:aws:iam::<AWS-account-id>:role/<role-name>'
```

Now when authenticated as the target user (by connecting directly as `username`, or by using [SET SESSION AUTHORIZATION](r_SET_SESSION_AUTHORIZATION.md "r_SET_SESSION_AUTHORIZATION.md") ), you can check global identity role using

```
SHOW GLOBAL IDENTITY
```

Note, the global identity role is associated with the user on session establishment. If you set the global identity for the currently logged in user, that user will need to reconnect for global identity to take effect.

The following command can be used to remove the associated IAM role.

```
ALTER USER `username` RESET GLOBAL IDENTITY
```

### Parameters

username

Name of the user. Cannot be a federated users, like IAM user or AWS IdC user.

IAM_ROLE 'arn:aws:iam::<account-id>:role/<role-name>'

Use the Amazon Resource Name (ARN) for an IAM role that your cluster uses for authentication
and authorization when user `username` runs queries on Redshift
warehouses with federated permissions. This role needs to have the required permissions to run the query.
We recommend using `AmazonRedshiftFederatedAuthorization` AWS Managed Policy.
