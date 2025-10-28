# Using existing IAM roles to fulfill Amazon DataZone

subscriptions

In the current release, Amazon DataZone supports you using your existing IAM roles to get
access to the data. To achieve this, you can create a subscription target in the
Amazon DataZone environment that you're using to fulfill your subscription. To create a
subscription target for an environment in one of the associated AWS accounts, you can
use the following steps:

###### Step 1: Ensure that your Amazon DataZone domain is using version 2 or higher of the

RAM policy

1. Navigate to the **Shared by me : Resource shares** page in
   the AWS RAM console.
2. Because AWS RAM resource shares exist in specific AWS Regions, choose the
   appropriate AWS Region from the dropdown list in the upper-right corner of the
   console.
3. Select the resource share corresponding to your Amazon DataZone domain and then
   choose **Modify**. You can identify the RAM share for the
   Amazon DataZone domain using the name or ID of the domain as the RAM share is created
   with the name:
   `DataZone-<domain-name>-<domain-id>`.
4. Choose **Next** to proceed to the next step where you can
   check the version of the RAM policy and modify it.
5. Make sure that the version of the RAM policy is Version 2 or higher. If not,
   use the dropdown to select Version 2 or higher.
6. Choose **Skip to step 4: Review and update**.
7. Choose **Update resource share**.

###### Step 2: Create a subscription target from an associated account

- In the current release, Amazon DataZone supports creating subscription targets by
  using APIs only. Below are some examples of the payload you can use to create a
  subscription target for fulfilling subscriptions to your AWS Glue tables and
  Amazon Redshift tables or views. For more information, see [CreateSubscriptionTarget](../APIReference/API_CreateSubscriptionTarget.md "../APIReference/API_CreateSubscriptionTarget.md").

Example of subscription target for AWS Glue

```

{
        "domainIdentifier": "<DOMAIN_ID>",
        "environmentIdentifier": "<ENVIRONMENT_ID>",
        "name": "<SUBSCRIPTION_TARGET_NAME>",
        "type": "GlueSubscriptionTargetType",
        "authorizedPrincipals" : ["IAM_ROLE_ARN"],
        "subscriptionTargetConfig" : [{"content": "{\"databaseName\": \"<DATABASE_NAME>\"}", "formName": "GlueSubscriptionTargetConfigForm"}],
        "manageAccessRole": "<GLUE_DATA_ACCESS_ROLE_IN_ASSOCIATED_ACCOUNT_ARN>",
        "applicableAssetTypes" : ["GlueTableAssetType"],
        "provider": "Amazon DataZone"
}

```

Example of subscription target for Amazon Redshift:

```

{
        "domainIdentifier": "<DOMAIN_ID>",
        "environmentIdentifier": "<ENVIRONMENT_ID>",
        "name": "<SUBSCRIPTION_TARGET_NAME>",
        "type": "RedshiftSubscriptionTargetType",
        "authorizedPrincipals" : ["REDSHIFT_DATABASE_ROLE_NAME"],
        "subscriptionTargetConfig" : [{"content": "{\"databaseName\": \"<DATABASE_NAME>\", \"secretManagerArn\": \"<SECRET_MANAGER_ARN>\",\"clusterIdentifier\": \"<CLUSTER_IDENTIFIER>\"}", "formName": "RedshiftSubscriptionTargetConfigForm"}],
        "manageAccessRole": "<REDSHIFT_DATA_ACCESS_ROLE_IN_ASSOCIATED_ACCOUNT_ARN>",
        "applicableAssetTypes" : ["RedshiftViewAssetType", "RedshiftTableAssetType"],
        "provider": "Amazon DataZone"
}

```

###### Important

    + The environmentIdentifier you use in the API call above should
     exist in the same associated account from which you are making the
     API call. Otherwise, the API call will not succeed.
    + The IAM role ARN you use in the "authorizedPrincipals" is the role
     to which Amazon DataZone will grant access to after a subscribed asset is
     added to the subscription target. These authorized principals must
     belong to the same account as the environment in which the
     subscription target is being created.
    + The value for provider field must be "Amazon DataZone" for
     Amazon DataZone to be able to complete subscription fulfillment.
    + The database name provided in subscriptionTargetConfig should
     already exist in the account in which the target is being created.
     Amazon DataZone will not create this database. Also ensure that the
     manage access role has CREATE TABLE permission on this
     database.
    + Also make sure that the roles (IAM role for the AWS Glue and the
     database role for Amazon Redshift) being provided as the authorized
     principals already exist in the environment account. For Amazon
     Redshift subscription targets, additional updates are required for
     the role being assumed while connecting to the cluster. This role
     must have RedshiftDbRoles tag attached to the role. The value of the
     tag can be a comma separated list. The value should be the database
     role that was provided as the authorized principal while creating
     the subscription target.

###### Step 3: Subscribe to a new table and fulfill subscription to the new

target

- Once you have created the subscription target, you can subscribe to a new
  table and Amazon DataZone will fulfill it to the above target.
