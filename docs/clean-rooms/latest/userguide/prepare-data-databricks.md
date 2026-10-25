

# Preparing data tables in Databricks
<a name="prepare-data-databricks"></a>

You can query data tables that are stored in Databricks by sharing them with AWS Clean Rooms through the Delta Sharing open protocol. AWS Clean Rooms connects to Databricks using JSON Web Token (JWT) exchange, so you don't need to store any long-lived secrets.

When you create the configured table, AWS Clean Rooms infers the schema automatically. You only supply the column names that you want to be visible to query runners.

Preparing your data tables in Databricks involves the following steps:

**Topics**
+ [Step 1: Complete the prerequisites](#prepare-data-databricks-prereq)
+ [Step 2: Set up token exchange with an IAM role](#prepare-data-databricks-federation)
+ [Step 3: Share your table through Delta Sharing](#prepare-data-databricks-share)
+ [Step 4: (Optional) Configure an IP access list](#prepare-data-databricks-ip-allowlist)
+ [Step 5: Next steps](#prepare-data-databricks-next)

## Step 1: Complete the prerequisites
<a name="prepare-data-databricks-prereq"></a>

To prepare your data tables for use with AWS Clean Rooms, you must complete the following prerequisites:
+ You have an AWS account with the proper permissions granted to read your data tables. For more information, see [Create a service role to read data from Databricks](setting-up-roles.md#create-service-role-databricks).
+ Your data tables use the [supported data types for AWS Clean Rooms](data-formats.md#data-types).
+ Your data table is stored in a Databricks workspace. For more information, see the [Databricks documentation](https://docs.databricks.com/en/index.html).
+ You have permissions in Databricks to enable Delta Sharing and to create shares and recipients.

## Step 2: Set up token exchange with an IAM role
<a name="prepare-data-databricks-federation"></a>

AWS Clean Rooms accesses your Databricks table by assuming an IAM role in your account. It then exchanges temporary credentials for a JWT that Databricks trusts. To set this up, complete the following steps. You enable outbound identity federation, create an IAM role, and note the identity token issuer for the next step. For more information about outbound identity federation, see [Getting started with outbound identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html) in the *AWS Identity and Access Management User Guide*.

**To set up token exchange**

1. Enable outbound identity federation for your AWS account.

   1. Open the IAM console, and then choose **Account settings**.

   1. Under **Outbound identity federation**, choose **Enable**.

   1. Note the token issuer URL that is generated (for example, **https://<uuid>.tokens.sts.global.api.aws**). This URL is the identity of your AWS account to external services such as Databricks. You use it in the next step.

1. Create an IAM role that AWS Clean Rooms assumes to generate the JWT, with a permissions policy that allows `sts:GetWebIdentityToken` and a trust policy that allows AWS Clean Rooms to assume the role only in the context of your collaboration memberships. For the exact policies, see [Create a service role to read data from Databricks](setting-up-roles.md#create-service-role-databricks).

   Note the role ARN for the next steps.

## Step 3: Share your table through Delta Sharing
<a name="prepare-data-databricks-share"></a>

In Databricks, enable Delta Sharing, create a recipient that trusts your AWS identity, and add your table to a share.

**To share your table**

1. Enable Delta Sharing (Open Sharing) for your metastore. In the Databricks catalog settings, under **Delta Sharing**, enable Open Sharing. This is a one-time, metastore-level setting.

1. Create a recipient that uses OIDC federation.

   1. Create a recipient of type **Open** with OIDC federation.

   1. Add a federation policy with the following values:
      + **Issuer** – The token issuer URL for your AWS account (from Step 2).
      + **Subject claim** – `sub`.
      + **Subject** – The ARN of the IAM role that you created in Step 2.
      + **Audiences** – Your Databricks workspace URL.

      This federation policy is analogous to an IAM trust policy. It tells Databricks to trust JWTs from this issuer, for this subject, with this audience.

1. Create a share, add your table to it, and grant the recipient access. Run the following commands in the Databricks SQL editor, replacing the placeholder names with your own.

   ```
   CREATE SHARE my_share;
   ALTER SHARE my_share ADD TABLE my_catalog.my_schema.my_table;
   GRANT SELECT ON SHARE my_share TO RECIPIENT my_recipient;
   ```

1. Get the Delta Sharing endpoint URL for the recipient. In the Databricks console, open the recipient and copy the endpoint URL. It has one of the following formats:

   ```
   https://<workspace>.cloud.databricks.com/api/2.0/delta-sharing/metastores/<metastore-id>/recipients/<recipient-id>
   
   https://<recipient-id>.opensharing.<region>.cloud.databricks.com/api/2.0/opensharing/metastores/<metastore-id>/recipients/<recipient-id>
   ```

   Note the Delta Sharing endpoint and the share name. You provide them when you create the configured table.

## Step 4: (Optional) Configure an IP access list
<a name="prepare-data-databricks-ip-allowlist"></a>

(Optional) To restrict access to your Databricks recipient so that only AWS Clean Rooms can connect, add an IP access list to the recipient. The IP access list allows the AWS Clean Rooms egress IP address range for the AWS Region of your collaboration.

In the Databricks console, open the recipient, choose the **IP access list** tab, and add the AWS Clean Rooms egress IP address range for your Region. For the list of ranges, see [AWS Clean Rooms egress IP address ranges](egress-ip-addresses.md).

## Step 5: Next steps
<a name="prepare-data-databricks-next"></a>

Now that you have prepared your data tables in Databricks, you are ready to: 
+ [Create a configured table](create-configured-table.md)

The tables can be queried after: 
+ The collaboration creator has set up a collaboration in AWS Clean Rooms. For more information, see [Creating a collaboration](create-collaboration.md).
+ The collaboration creator has sent the collaboration ID to you as a participant in the collaboration.