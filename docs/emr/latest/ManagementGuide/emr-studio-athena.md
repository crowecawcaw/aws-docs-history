# Use the Amazon Athena SQL editor in EMR Studio

## Overview

You can use Amazon EMR Studio to develop and run interactive
queries on Amazon Athena. That means that you can perform SQL analytics on Athena from the same
EMR Studio interface that you use to run your Spark, Scala, and other workloads. With
this integration, you can use auto-completion to develop queries quickly, browse data in
your AWS Glue Data Catalog, create saved queries, view your query history, and more.

For more information on using Amazon Athena, see [Using Athena SQL](../../../athena/latest/ug/using-athena-sql.md "../../../athena/latest/ug/using-athena-sql.md") in the
_Amazon Athena User Guide_.

## Use the Athena SQL editor in EMR Studio

Use the following steps to develop and run interactive queries on Amazon Athena from your
EMR Studio:

1. Add the required permissions to the user role for the users who access the
   Workspaces in this Studio. The permissions are listed in the [AWS Identity and Access Management permissions for
   EMR Studio users](emr-studio-user-permissions.md#emr-studio-iam-permissions-table "emr-studio-user-permissions.md#emr-studio-iam-permissions-table") table in the column
   **Access Amazon Athena SQL editor from your EMR Studio**.
   Alternatively, you can choose to copy the **Advanced** policy contents
   from the [Example user policies](emr-studio-user-permissions.md#emr-studio-example-policies "emr-studio-user-permissions.md#emr-studio-example-policies") to grant users full permissions to
   EMR Studio capabilities including this one.
2. [Set up](emr-studio-set-up.md "emr-studio-set-up.md") and [create an EMR Studio](emr-studio-create-studio.md "emr-studio-create-studio.md").
3. Navigate to your Studio and select **Query editor** from the
   sidebar.

You should now see the familiar Athena editor UI. For information on getting started and
using Athena SQL to run interactive queries, see [Getting started](../../../athena/latest/ug/getting-started.md "../../../athena/latest/ug/getting-started.md") and [Using Athena SQL](../../../athena/latest/ug/using-athena-sql.md "../../../athena/latest/ug/using-athena-sql.md")
in the _Amazon Athena User Guide_.

###### Note

If you have enabled trusted identity propagation through IAM Identity Center for
your EMR Studio, then you must use Athena workgroups to control query access, and the
workgroup that you use must also use trusted identity propagation. For steps to set up
Identity Center and enable trusted identity propagation for your workgroup, see [Using IAM Identity Center
enabled Athena workgroups](../../../athena/latest/ug/workgroups-identity-center.md "../../../athena/latest/ug/workgroups-identity-center.md") in the _Amazon Athena User Guide_.

## Considerations for using the Athena SQL

editor in EMR Studio

- Integration with Athena is available in all commercial Regions where EMR Studio
  and Athena are available.
- The following Athena features are not available in EMR Studio:
  - Admin features like creating or updating Athena workgroups, data sources, or
    capacity reservations
  - Athena for Spark or Spark notebooks
  - Amazon DataZone integration
  - Cost Based Optimizer (CBO)
  - Step functions
