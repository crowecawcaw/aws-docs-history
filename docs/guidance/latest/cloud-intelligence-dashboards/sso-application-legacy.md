

# SSO Application (Legacy Guide)
<a name="sso-application-legacy"></a>

## Last Updated
<a name="last-updated"></a>

January 2024

## Authors
<a name="authors"></a>
+ Veaceslav Mindru, Sr. Technical Account Manager, AWS
+ Stephanie Gooch, Sr. Commercial Architect, AWS OPTICS

## Introduction
<a name="introduction"></a>

Cloud Intelligence Dashboards (CID) helps you to visualize and understand AWS cost and usage data in your organization by exploring interactive dashboards. To simplify access for users you can now set up an SSO application for them to enter into. We recommend combining this with the Row Level Security customization to ensure they see the data that really matters to them.

**Important**  
This is a legacy guide, for a new fresh setup of Quick Sight we recommend setting up Quick Sight with IAM Identity Center integration. Please follow [Publishing as single sign-on (SSO) Application](publishing-as-sso-application.md) guide

## Prerequisite
<a name="prerequisite"></a>

For this solution you must have the following:
+ Access to your AWS Organizations and ability to tag resources
+ An [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) (CUR) or if from the multiple payers these must be replicated into a bucket, more info [here](https://wellarchitectedlabs.com/cost/100_labs/100_1_aws_account_setup/3_cur/#option-2-replicate-the-cur-bucket-to-your-cost-optimization-account-consolidate-multi-payer-curs) 
+ A CID deployed over this CUR data, checkout the new single deployment method [here](deployment-in-global-regions.md).
+ A list of users and what level of access they require. This can be member accounts, organizational units (OU) or payers.
+ Enable IAM Identity Center

## Step 1: Quick Sight Check
<a name="step-1-quick-sight-check"></a>

1. Login into your Cost Account where your CID is deployed and go into Amazon Quick Sight

![Images/sso_sso_quicksight.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_quicksight.png?classes=lab_picture_small)


1. Select your CID and open it

![Images/sso_qs_dashboard.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_qs_dashboard.png?classes=lab_picture_small)


1. On the top right click on the Share icon then Share Dashboard

![Images/sso_qs_share_button.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_qs_share_button.png?classes=lab_picture_small)


1. Share your CID Dashboard in Amazon Quick Sight with all users by clicking on the toggle **Everyone in this account** 

![Images/sso_qs_share.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_qs_share.png?classes=lab_picture_small)


1. Copy the Dashboard URL to somewhere local as we will use this later

![Images/sso_cudos_url.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_cudos_url.png?classes=lab_pictures_small)


## Step 2: Create Users and Group
<a name="step-2-create-users-and-group"></a>

1. Open the **IAM Identity Centre**. Click on **Groups** on the left then **Create group** 

1. Under Group name, give the name **CID** then click **Create group** 

![Images/sso_user_group.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_user_group.png?classes=lab_picture_small)


1. Click on **Users** then **Add user** 

![Images/sso_user_users.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_user_users.png?classes=lab_picture_small)


1. Fill out the details using the same email that will be used for Amazon Quick Sight. Click **Next**.

![Images/sso_user_user_email.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_user_user_email.png?classes=lab_picture_small)


1. Click on the box next to the **CID** group you made earlier. Then Click **Next**.

![Images/sso_user_add_to_group.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_user_add_to_group.png?classes=lab_picture_small)


1. Scroll down and click **Add user** 

## Step 3: IAM Identity Centre
<a name="step-3-iam-identity-centre"></a>

1. Open the **IAM Identity Centre** and select **Applications** on the left and Click **Add application** 

![Images/sso_iic_add_app.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_add_app.png?classes=lab_picture_small)


1. Search in Preintegrated applications for **Amazon Quick Sight** then click **Next** 

![Images/sso_iic_qs.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_qs.png?classes=lab_picture_small)


1. Type a Display name **Billing Dashboard**. Under **IAM Identity Center metadata** Download IAM Identity Center **SAML metadata file**.

![Images/sso_iic_config.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_config.png?classes=lab_picture_small)


1. Under **Application properties** paste your CID Link under Relay state. Click **Submit** 

![Images/sso_iic_qs_url.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_qs_url.png?classes=lab_picture_small)


1. Click into your application and click **Assign Users** 

![Images/sso_iic_assign.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_assign.png?classes=lab_picture_small)


1. Click on the **Groups** tab and select the CID group then click the **Assign Users** button

![Images/sso_iic_group.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_group.png?classes=lab_picture_small)


## Step 4: Provider
<a name="step-4-provider"></a>

Note: This step is done in the target account where the CID lives, this may differ from the SSO account.

1. Open IAM, on the left click **Identity providers** then click the **Add provider** button

![Images/sso_iam_provider.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_provider.png?classes=lab_picture_small)


1. Under Provider type choose **SAML**, give it the name **Quick SightProvider** then upload the SAML file you downloaded earlier using the **Choose file** button. Click **Add provider** 

![Images/sso_iam_provider_saml.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_provider_saml.png?classes=lab_picture_small)


1. Click into your new provider

![Images/sso_iam_provider_qs.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_provider_qs.png?classes=lab_picture_small)


1. Click the button **Assign role** and choose **Create a new role** and click Next

![Images/sso_iam_provider_create_role.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_provider_create_role.png?classes=lab_picture_small)


1. Ensure SAML 2.0 federation is clicked at the top then click the **Allow programmatic and AWS Management Console access** radio button and click **Next: Permissions** 

![Images/sso_iam_role_saml.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_role_saml.png?classes=lab_picture_small)


1. Click **Create policy** 

![Images/sso_iam_policy.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_policy.png?classes=lab_picture_small)


1. Select the JSON tab and paste in the below code replacing your `ACCOUNT_ID` with your `CID Quick Sight` account `ID`. Click Next.

   ```
            {
               "Version": "2012-10-17",		 	 	 
               "Statement": [
                    {
                    "Action": [
                            "quicksight:CreateReader"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                            "*"
                    ]
                    }
            ]
            }
   ```

![Images/sso_policy_json.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_policy_json.png?classes=lab_picture_small)


1. Click through **Next** 

1. For Name call it **Quick SightSAMLPolicy** then click **Create Policy** 

![Images/sso_iam_policy_name.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_policy_name.png?classes=lab_picture_small)


1. Go back to previous IAM tab to attach permissions, refresh the list then search for **Quick SightSAMLPolicy** and click the tick box. Click **Next** 

![Images/sso_iam_add_policy.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_add_policy.png?classes=lab_picture_small)


1. Provide a Role name as **Quick SightSAMLRole** and click Create role

![Images/sso_iam_role_name.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_role_name.png?classes=lab_picture_small)


1. Search for your new role and click into it. Select the **Trust relationships** tab and click **Edit trust policy** 

![Images/sso_iam_tr.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_tr.png?classes=lab_picture_small)


1. Replace the json with the below, replacing your `ACCOUNT_ID` with your `CID Quick Sight` account `ID`.

   ```
           {
           "Version": "2012-10-17",		 	 	 
           "Statement": [
                   {
                   "Effect": "Allow",
                   "Principal": {
                           "Federated": "arn:aws:iam::ACCOUNT_ID:saml-provider/Quick SightProvider"
                   },
                   "Action": "sts:AssumeRoleWithSAML",
                   "Condition": {
                           "StringEquals": {
                           "SAML:aud": "https://signin.aws.amazon.com/saml"
                           }
                   }
                   },
                   {
                   "Effect": "Allow",
                   "Principal": {
                           "Federated": "arn:aws:iam::ACCOUNT_ID:saml-provider/Quick SightProvider"
                   },
                   "Action": "sts:TagSession",
                   "Condition": {
                           "StringLike": {
                           "aws:RequestTag/Email": "*"
                           }
                   }
                   }
   
           ]
           }
   ```

![Images/sso_iam_tp_edit.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iam_tp_edit.png?classes=lab_picture_small)


## Update Attribute Mappings
<a name="update-attribute-mappings"></a>

1. Return to your **IAM Identity Center** and find your Amazon Quick Sight application for CID and click into it.

![Images/sso_iic_app.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_app.png?classes=lab_picture_small)


1. Click the **Actions** button and select **Edit attribute mapping** 

![Images/sso_iic_edit_mapping.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_edit_mapping.png?classes=lab_picture_small)


1. Add two new mappings by clicking on **Add new attribute mapping**, replacing your `ACCOUNT_ID` with your `CID Quick Sight` account `ID`.
   + ADD **Attribute:** `https://aws.amazon.com/SAML/Attributes/Role` **Value:** `arn:aws:iam::111122223333:role/Quick SightSAMLRole, arn:aws:iam::111122223333:saml-provider/Quick SightProvider` 
   + ADD: **Attribute:** `https://aws.amazon.com/SAML/Attributes/PrincipalTag:Email` **Value** `${user:email}` 

![Images/sso_iic_mapping_update.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_iic_mapping_update.png?classes=lab_picture_small)


1. After this step is done, a new ICON will appear in SSO, give it 5 minutes to start

![Images/sso_screenshot.png](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/customizations/sso_legacy/sso_screenshot.png?classes=lab_picture_small)
