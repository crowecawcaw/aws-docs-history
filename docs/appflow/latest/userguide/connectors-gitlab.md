

# GitLab connector for Amazon AppFlow
<a name="connectors-gitlab"></a>

GitLab is an open source code repository and software development platform. If you're a GitLab user, your account contains data about your projects and repositories. You can use Amazon AppFlow to transfer data from GitLab to certain AWS services or other supported applications.

## Amazon AppFlow support for GitLab
<a name="gitlab-support"></a>

Amazon AppFlow supports GitLab as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from GitLab.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to GitLab.

**Supported API version**  
Amazon AppFlow retrieves your data by sending requests to the GitLab v4 REST API.

## Before you begin
<a name="gitlab-prereqs"></a>

To use Amazon AppFlow to transfer data from GitLab to supported destinations, you must meet these requirements:
+ You have a GitLab account and one or more projects that contain the data that you want to transfer. For more information about the GitLab data objects that Amazon AppFlow supports, see [Supported objects](#gitlab-objects).
+ In the settings of your account, you've created either of the following resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account.
  + An application, which provides OAuth 2.0 authentication. For the steps to create an application, see [User owned applications](https://docs.gitlab.com/ee/integration/oauth_provider.html#user-owned-applications) in the GitLab Docs.
  + A personal access token. For the steps to create one, see [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) in the GitLab Docs.

    Your personal access token must permit the `api` scope.
+ If you created an application, you've configured it with the following settings:
  + You've specified a redirect URL for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from GitLab. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
  + You've permitted the scopes that provide access to the data objects that you want to transfer. For information about GitLab OAuth 2.0 scopes, see [Authorized applications](https://docs.gitlab.com/ee/integration/oauth_provider.html#authorized-applications) in the GitLab Docs.

If you created an application, note the application ID and secret. If you created a personal access token, note the token value. You provide these values to Amazon AppFlow when you connect to your GitLab account.

## Connecting Amazon AppFlow to your GitLab account
<a name="gitlab-connecting"></a>

To connect Amazon AppFlow to your GitLab account, provide the credentials from your application, or provide a personal access token. If you haven't yet configured your GitLab account for Amazon AppFlow integration, see [Before you begin](#gitlab-prereqs).

**To connect to GitLab**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **GitLab**.

1. Choose **Create connection**.

1. In the **Connect to GitLab** window, for **Select authentication type**, choose how to authenticate Amazon AppFlow with your GitLab account when it requests to access your data:
   + Choose **OAuth2** to authenticate Amazon AppFlow with the credentials from an application. Then, enter the following values:
     + **Client ID** – The application ID.
     + **Client secret** – The secret.
   + Choose **PersonalAccessToken** to authenticate Amazon AppFlow with a personal access token. Then, enter the token value for **Personal access token**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Depending on the authentication type that you chose, do one of the following:
   + If you chose **OAuth2**, choose **Continue**. Then, in the window that appears, sign in to your GitLab account, and grant access to Amazon AppFlow.
   + If you chose **PersonalAccessToken**, choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses GitLab as the data source, you can select this connection.

## Transferring data from GitLab with a flow
<a name="gitlab-transfer-data"></a>



To transfer data from GitLab, create an Amazon AppFlow flow, and choose GitLab as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for GitLab, see [Supported objects](#gitlab-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#gitlab-destinations).

## Supported destinations
<a name="gitlab-destinations"></a>

When you create a flow that uses GitLab as the data source, you can set the destination to any of the following connectors: 
+ [Amazon Lookout for Metrics](lookout.md)
+ [Amazon Redshift](redshift.md)
+ [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md)
+ [Amazon S3](s3.md)
+ [HubSpot](connectors-hubspot.md)
+ [Marketo](marketo.md)
+ [Salesforce](salesforce.md)
+ [SAP OData](sapodata.md)
+ [Snowflake](snowflake.md)
+ [Upsolver](upsolver.md)
+ [Zendesk](zendesk.md)
+ [Zoho CRM](connectors-zoho-crm.md)

## Supported objects
<a name="gitlab-objects"></a>

When you create a flow that uses GitLab as the data source, you can transfer any of the following data objects to supported destinations:



- ** Branch**
  - **** Field**:** can\_push / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** commit / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** developers\_can\_merge / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** developers\_can\_push / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** merged / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** protected / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 

- ** Commit**
  - **** Field**:** all / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** author\_email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** author\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** authored\_date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** committed\_date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** committer\_email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** committer\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** first\_parent / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** parent\_ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** path / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ref\_name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** short\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** since / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** since\_until / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** trailers / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** until / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** with\_stats / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Group**
  - **** Field**:** auto\_devops\_enabled / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** avatar\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** default\_branch\_protection / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** emails\_disabled / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** file\_template\_project\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** full\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** full\_path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ip\_restriction\_ranges / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ldap\_access / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ldap\_cn / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** lfs\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** mentions\_disabled / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** min\_access\_level / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order\_by / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** owned / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** parent\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** project\_creation\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** request\_access\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** require\_two\_factor\_authentication / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** share\_with\_group\_lock / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** skip\_groups / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** statistics / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** subgroup\_creation\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** top\_level\_only / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** two\_factor\_grace\_period / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** visibility / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** with\_custom\_attributes / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Group Member**
  - **** Field**:** access\_level / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** avatar\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created\_by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** expires\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** group\_saml\_identity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** is\_using\_seat / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** membership\_state / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** query / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** show\_seat\_info / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** skip\_users / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** user\_ids / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** username / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 

- ** Group label**
  - **** Field**:** closed\_issues\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description\_html / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** include\_ancestor\_groups / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** include\_descendant\_groups / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** only\_group\_labels / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** open\_issues\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** open\_merge\_requests\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** subscribed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** text\_color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** with\_counts / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Group milestone**
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** due\_date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** expired / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** group\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iid / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iids / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** include\_parent\_milestones / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** start\_date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** updated\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 

- ** Issue**
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** assignee\_id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** assignee\_username / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** assignees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** author / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** author\_id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** author\_username / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** blocking\_issues\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** closed\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** closed\_by / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** confidential / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created\_after / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created\_before / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created\_before\_after / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discussion\_locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** downvotes / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** due\_date / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** has\_tasks / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iid / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iids / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** issue\_type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** labels / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** merge\_requests\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** milestone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** milestone\_id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** moved\_to\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** my\_reaction\_emoji / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** non\_archived / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** order\_by / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** project\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** references / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** scope / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** service\_desk\_reply\_to / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** severity / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** task\_completion\_status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** task\_status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** time\_stats / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updated\_after / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updated\_before / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated\_before\_after / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** upvotes / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** user\_notes\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** with\_labels\_details / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Job**
  - **** Field**:** allow\_failure / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** artifacts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** artifacts\_expire\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** artifacts\_file / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** commit / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** coverage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** duration / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** failure\_reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** finished\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** pipeline / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** project / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** queued\_duration / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ref / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** runner / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** scope / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** stage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** started\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** tag\_list / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** user / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 

- ** Pipeline**
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iid / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** order\_by / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** project\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ref / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** scope / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** sha / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** updated\_after / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updated\_before / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated\_before\_after / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** username / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** yaml\_errors / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Project**
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** allow\_merge\_on\_skipped\_pipeline / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** analytics\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** archived / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** auto\_cancel\_pending\_pipelines / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** auto\_devops\_deploy\_strategy / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** auto\_devops\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** autoclose\_referenced\_issues / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** avatar\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** build\_timeout / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** builds\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** can\_create\_merge\_request\_in / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ci\_allow\_fork\_pipelines\_to\_run\_in\_parent\_project / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ci\_config\_path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ci\_default\_git\_depth / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ci\_forward\_deployment\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ci\_job\_token\_scope\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ci\_separated\_caches / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** compliance\_frameworks / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** container\_expiration\_policy / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** container\_registry\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** container\_registry\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** container\_registry\_image\_prefix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** creator\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** default\_branch / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** emails\_disabled / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** empty\_Repo / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** enforce\_auth\_checks\_on\_uploads / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** external\_authorization\_classification\_label / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** forking\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** forks\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** http\_url\_to\_repo / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** id\_after / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id\_before / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** import\_status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** imported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** issues\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** issues\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** jobs\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** keep\_latest\_artifact / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** last\_activity\_after / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** last\_activity\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** last\_activity\_before / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** last\_activity\_before\_after / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** lfs\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** membership / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** merge\_commit\_template / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** merge\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** merge\_requests\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** merge\_requests\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** min\_access\_level / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name\_with\_namespace / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** namespace / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** only\_allow\_merge\_if\_all\_discussions\_are\_resolved / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** only\_allow\_merge\_if\_pipeline\_succeeds / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** open\_issues\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** operations\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order\_by / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** owned / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** packages\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** pages\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** path\_with\_namespace / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** permissions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** printing\_merge\_request\_link\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** public\_jobs / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** readme\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** remove\_source\_branch\_after\_merge / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** repository\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** repository\_storage / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** request\_access\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** requirements\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** requirements\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** resolve\_outdated\_diff\_discussions / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** restrict\_user\_defined\_variables / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** runner\_token\_expiration\_interval / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** search\_namespaces / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** security\_and\_compliance\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** security\_and\_compliance\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** service\_desk\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** shared\_runners\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** shared\_with\_groups / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** simple / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** snippets\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** snippets\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** squash\_commit\_template / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** squash\_option / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ssh\_url\_to\_repo / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** star\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** starred / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** statistics / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** suggestion\_commit\_message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tag\_list / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** topic / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** topic\_id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** topics / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** visibility / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** wiki\_access\_level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** wiki\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** with\_custom\_attributes / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** with\_issues\_enabled / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** with\_merge\_requests\_enabled / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** with\_programming\_language / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Project Label**
  - **** Field**:** closed\_issues\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description\_html / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** include\_ancestor\_groups / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** is\_project\_label / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** open\_issues\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** open\_merge\_requests\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** priority / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** subscribed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** text\_color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** with\_counts / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Project Member**
  - **** Field**:** access\_level / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** avatar\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created\_by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** expires\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** group\_saml\_identity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** is\_using\_seat / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** membership\_state / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** query / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** show\_seat\_info / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** skip\_users / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** user\_ids / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** username / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 

- ** Project Merge Request**
  - **** Field**:** allow\_collaboration / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** allow\_maintainer\_to\_push / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** approvals\_before\_merge / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** assignee\_id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** assignees / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** author / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** author\_id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** author\_username / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** blocking\_discussions\_resolved / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** closed\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** closed\_by / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_after / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created\_before / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created\_before\_after / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** deployed\_after / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** deployed\_before / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** deployed\_before\_after / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discussion\_locked / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** downvotes / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** draft / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** environment / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** force\_remove\_source\_branch / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** has\_conflicts / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iid / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** labels / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** merge\_commit\_sha / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** merge\_status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** merge\_user / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** merge\_when\_pipeline\_succeeds / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** merged\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** merged\_by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** milestone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** my\_reaction\_emoji / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** order\_by / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** project\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** references / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** reviewer\_id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** reviewer\_username / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** reviewers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** scope / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** sha / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** should\_remove\_source\_branch / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** source\_branch / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** source\_project\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** squash / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** squash\_commit\_sha / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** target\_branch / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** target\_project\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** task\_completion\_status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** time\_stats / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updated\_after / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updated\_before / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated\_before\_after / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** upvotes / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** user\_notes\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** view / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** wip / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** with\_labels\_details / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** with\_merge\_status\_recheck / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** work\_in\_progress / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Project milestone**
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** due\_date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** expired / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iid / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** iids / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** include\_parent\_milestones / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** project\_id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** start\_date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** updated\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** web\_url / **** Data type**:** String / **** Supported filters**:** 

- ** Release**
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** assets / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** author / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** commit / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** commit\_path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** evidences / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** include\_html\_description / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** milestones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order\_by / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** released\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** tag\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tag\_path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** upcoming\_release / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Tag**
  - **** Field**:** commit / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order\_by / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** protected / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** release / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** target / **** Data type**:** String / **** Supported filters**:** 

