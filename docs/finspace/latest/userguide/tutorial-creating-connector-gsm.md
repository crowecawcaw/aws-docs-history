After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Tutorial: Creating a connector for

Goldman Sachs Financial Cloud for Data

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

This tutorial guides you through the steps to create a data connector for the Goldman Sachs Financial Cloud for Data (GSFCD) provider.

## Prerequisites

Before you proceed, make sure that you have the following available:

- Goldman Sachs Financial Cloud for Data API credentials –
  These credentials will be used to connect to the GSFCD. The credentials will be
  stored in AWS Secrets Manager so that the data connector can use them securely.
  - Registered users for Goldman Sachs Financial Cloud for Data can obtain new API credentials from [Goldman Sachs Developer website](https://developer.gs.com/go/apps/view "https://developer.gs.com/go/apps/view").
  - New users can submit a request to obtain API credentials at [Goldman Sachs Financial Cloud for Data](https://developer.gs.com/discover/data " https://developer.gs.com/discover/data").

- A FinSpace environment – You can only
  use a data connector in the FinSpace environment where it was created. For more
  information, see [Create an Amazon FinSpace environment](create-an-amazon-finspace-environment.md "create-an-amazon-finspace-environment.md").

## Step 1: Add connector details

###### To add connector details

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, choose **Data Providers**.

###### Tip

Alternatively, you can also perform the following steps:

    1. In the left pane, choose **Environments**.
    2. From the list of environments, choose the name of the environment
     where you want to create a data connector.
    3. On the environment details page, scroll down to **Data
     Connectors** and choose **Create
     connector**. The **Data Providers** page
     opens.

3. On the **Data Providers** page, for the
   **Goldman Sachs Financial Cloud for Data** provider, choose **Add
   connector**.
4. On the **Connector details** page, provide a unique **Connector
   name**, and choose an account with superuser to run the connector.
5. For **Scheduled runs**, select this option if you want to schedule automatic connector runs. The data connector will run daily at 00:00 UTC.

Clear this option if you don't want to schedule automatic runs. You will
need to manually start the data connector run from the console. For more
information, see [Running a data connector](connector-summary.md#running-data-connectors "connector-summary.md#running-data-connectors"). 6. Choose **Next** and proceed to [Step 2: Add a secret name](#step-2-secret-name-gsm "#step-2-secret-name-gsm").

## Step 2: Add a secret name

FinSpace uses AWS Secrets Manager to store the API credentials that your FinSpace environment will use to connect to the Goldman Sachs Financial Cloud for Data API. For more information, see [Secrets Manager concepts](../../../secretsmanager/latest/userguide/getting-started.md#getting-started_concepts "../../../secretsmanager/latest/userguide/getting-started.md#getting-started_concepts") in the _AWS Secrets Manager User Guide_.

When you choose **Next** on the **Connector
details** page in the previous step, the **Secret name**
page opens. You can choose an existing secret name or create a new one.

###### To add a secret name

1. On the **Secret name** page, choose an existing secret name from the dropdown
   list.
2. You can also create a new secret name on this page by choosing the **Create new secret** option from the list.
   1. Under the **Create new secret** section, for **Secret name**, enter a unique name for the secret.
   2. Enter the key-value pair for your secret in **Client ID** and
      **Client secret**, respectively.
   3. Choose an encryption AWS KMS key. This key will be used by AWS Secrets Manager to encrypt your
      secret. You can select an existing KMS key from the dropdown or create a
      new one by using the AWS Key Management Service. For more information, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/concepts.md#kms_keys "../../../kms/latest/developerguide/concepts.md#kms_keys").

   ###### Note

   By default, this field displays the KMS key that you used to create
   the environment where you're creating this data connector.

3. Choose **Next** and proceed to [Step 3: Add customer IAM role](#step-3-customer-iam-role-gsm "#step-3-customer-iam-role-gsm").

###### Note

You can also create a secret directly from the AWS Secrets Manager console. For more information, see [Create a secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.

## Step 3: Add customer IAM role

In FinSpace, you can securely control access to data connectors by creating IAM
policies and attaching them to roles. A policy is an object in AWS that, when
associated with an identity or resource, defines their permissions. AWS evaluates
these policies when a principal uses an IAM entity (user or role) to make a request.
For more information, see [Roles terms and
concepts](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") in the _IAM User Guide_.

When you choose **Next** on the **Secret
name** page in the previous step, the **Customer IAM
role** page opens. You can select an existing role or create a new
one.

###### To add a customer IAM role

1. On the **Customer IAM role** page, choose an existing role ARN from the
   dropdown list.
2. You can also create a new role on this page by choosing the **Create new customer IAM role** option from list.

First create a permissive IAM policy and then create an IAM role. Then
attach the new policy to it.

**To create an IAM policy**

    1. Under the **Create a policy** section, choose **Copy code**
     to copy the policy code. You will use this code to create an IAM
     permissions policy.
    2. Choose **Go to policy creation form**. This button opens the **Create policy** page in a new tab.


    ###### Note

    Do not close the **Customer IAM role** tab.
    3. On the **Create policy** page, choose the **JSON** tab.
     Delete any prepopulated JSON code, and then paste the policy code that you
     copied in previous step.
    4. Choose **Next: Tags**. (Optional) Add metadata to the policy by attaching tags as key-value pairs.
    5. Choose **Next: Review**.
    6. On the **Review policy**
     page, enter a **Name** and a
     **Description** (optional) for the policy that you're
     creating. Review the policy **Summary** to see the
     permissions that are granted by your policy. Then choose **Create
     policy** to save your work.


    ###### Note

    Remember this policy name because you will need it while creating a role.**To create an IAM role**




    1. Return to the **Select customer IAM role** tab. Under the **Create a customer IAM role** section, choose **Copy code** to copy the trust relationship code.
    2. Choose **Go to customer IAM role form**. This button opens the **Create role** setup in a new tab.


    ###### Note

    Do not close the **Customer IAM role** tab.
    3. On the **Select trusted entity** page, for **Trusted entity type**, choose **Custom trust policy**.
    4. Under the **Custom trust policy** section, delete any prepopulated code, and
     then paste the trust relationship code that you copied in the previous
     step.
    5. Choose **Next**.
    6. On the **Add permissions** page, for **Permissions policy**,
     search for the policy name that you created in [step f](#policy-name-gsm "#policy-name-gsm") in "To add a customer IAM role". Select the
     policy check box and choose **Next**.
    7. On the **Name, review, and create** page, add a role name. Review the policy and permission details and choose **Create role**.


    ###### Note

    Remember this role name because you will need it in the next step.

3. Return to the **Select customer IAM role** tab. For **Customer IAM role**, enter the name of the role you created in the previous step.
4. Choose **Next** and proceed to [Step 4: Review and create](#step-4-review-gsm "#step-4-review-gsm").

###### Note

You can also create the IAM role and policy directly from the AWS Identity and Access Management
console. For more information, see [Creating an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console "../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console") in the
_IAM User Guide_.

## Step 4: Review and create

Review the connector details, secret name, and customer IAM role, and then
choose **Create connector**.

After the new data connector is created, the connector details page opens where
you can perform other operations using a data connector. To verify that the new
connector setup is complete, see the **Connector summary** section and
ensure that the **Status** is **Active**. The
connector will start syncing automatically when it's connected. For more information,
see [Connector details](connector-summary.md "connector-summary.md").

###### Note

- If you create multiple GSFCD data connectors for a single Amazon FinSpace
  environment, duplicate datasets are created in FinSpace if the GSFCD client access
  credentials that you use have an overlap in the datasets they have access to.
  To avoid this, only create multiple connectors with credentials that don't have
  overlapping access to datasets.
- Datasets that are created when a GSFCD connector runs are placed in a system-generated
  permission group. You can't add them to other permission groups.
