# Troubleshooting the AWS Marketplace Commerce Analytics Service

You can troubleshoot issues with the AWS Marketplace Commerce Analytics Service, which programmatically provides
product and customers data from AWS Marketplace. You might need to troubleshoot the Commerce Analytics Service when you
encounter errors or other configuration issues. The following sections guide you through the
troubleshooting process, covering steps to diagnose and resolve common problems with the
Commerce Analytics Service.

**I can't access the service because of an allow list issue.**

If you're not yet registered as a seller on the AWS Marketplace, visit [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management") to register. If you
have already registered as a seller on AWS Marketplace, contact the [**AWS Marketplace Seller Operations**](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.

**I can't request datasets for a date in the past, even though the
SDK documentation says it should be available for this date.**

Even though datasets are listed as being available for certain dates in the past, we have
data only since the time that you joined AWS Marketplace. If you believe that this is in error,
contact the [**AWS Marketplace Seller Operations**](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.

**When I call the service, I receive the error message "Could not
connect to the endpoint URL:
https://marketplacecommerceanalytics.eu-central-1.amazonaws.com/”**

The AWS Marketplace Commerce Analytics Service is available only in the US East (N. Virginia) Region. You must make all calls to
the Commerce Analytics Service to the `us-east-1` endpoint.

If you're using the AWS CLI, add the "`--region` flag to each call and specify
the AWS Region as `us-east-1`, as shown in the following
example.

```

aws marketplacecommerceanalytics generate-data-set \
--data-set-type "customer_subscriber_hourly_monthly_subscriptions" \
--data-set-publication-date "2016-04-21T00:00:00Z" \
--role-name-arn "arn:aws:iam::138136086619:role/MarketplaceCommerceAnalyticsRole" \
--destination-s3-bucket-name "marketplace-analytics-service" \
--destination-s3-prefix "test-prefix" \
--sns-topic-arn "arn:aws:sns:eu-central-1:138136086619:Marketplace_Analytics_Service_Notice" \
 **--region us-east-1**

```

**I want to use a different Amazon S3 bucket or Amazon SNS topic than the ones I
selected when I went through the on-boarding process.**

When enrolling in the AWS Marketplace Commerce Analytics Service, you specified an Amazon S3 bucket and Amazon SNS topic. The
onboarding process configures your IAM permissions to allow the service access to only these
specific resources. To use different resources, you need to modify your IAM policy:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** on the left side of the IAM console.
3. Choose **MarketplaceCommerceAnalyticsRole**.
4. Expand the **Inline Roles** section, if not already expanded.
5. Locate the policy with a name that starts with
   _oneClick_MarketplaceCommerceAnalyticsRole_ and
   choose **Edit Policy**.
6. In the policy document, locate the section that specifies actions related to the
   service that you want to modify. For example, to change your Amazon S3 bucket, locate the
   section that includes the actions that start with **s3:**
   and change their respective **Resource** selection to
   specify your new Amazon S3 bucket.
   For additional information about IAM policies, see the following guide: [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")

**I get an `AccessDeniedException` error when I call the
`GenerateDataSet` action**

This can happen if your user doesn't have the permissions necessary to call
`GenerateDataSet`. The following procedure outlines the steps needed to create an
IAM policy with those permissions using the IAM console and add the permissions to your
users, groups, or roles.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "marketplacecommerceanalytics:GenerateDataSet",
      "Resource": "*"
    }
  ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.
To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

**My problem isn't listed here.**

Contact the [**AWS Marketplace Seller Operations**](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.
