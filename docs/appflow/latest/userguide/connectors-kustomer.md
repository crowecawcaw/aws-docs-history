

# Kustomer connector for Amazon AppFlow
<a name="connectors-kustomer"></a>

Kustomer is a Customer Relationship Management (CRM) service that helps companies create and maintain operational solutions with customers. If you’re a Kustomer user, your account contains customer data across a number of digital channels. You can use Amazon AppFlow to transfer data from Kustomer to certain AWS services or other supported applications.

## Amazon AppFlow support for Kustomer
<a name="kustomer-support"></a>

Amazon AppFlow supports Kustomer as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Kustomer.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Kustomer.

## Before you begin
<a name="kustomer-prereqs"></a>

To use Amazon AppFlow to transfer data from Kustomer to supported destinations, you must meet these requirements:
+ You have an account with Kustomer that contains the data that you want to transfer. For more information about the Kustomer data objects that Amazon AppFlow supports, see [Supported objects](#kustomer-objects).
+ In the API keys settings for your account, you've created an API key for Amazon AppFlow, and you have the token value. Amazon AppFlow uses the API key token to make authenticated calls to your account and securely access your data. For the steps to create a key, see [API keys](https://help.kustomer.com/api-keys-SJs5YTIWX) in the Kustomer Help Center.

To connect Amazon AppFlow to your Kustomer account, you provide the token of your API key. You can view and copy this token only when you create the API key. If you don't have the token value, create a new API key.

## Connecting Amazon AppFlow to your Kustomer account
<a name="kustomer-connecting"></a>

To connect Amazon AppFlow to your Kustomer account, provide details from your Kustomer project so that Amazon AppFlow can access your data. If you haven't yet configured your Kustomer project for Amazon AppFlow integration, see [Before you begin](#kustomer-prereqs).

**To connect to Kustomer**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Kustomer**.

1. Choose **Create connection**.

1. In the **Connect to Kustomer** window, enter the following information:
   + **Access token** – The access token that you created earlier.
   + **Instance URL** – The URL of the instance where you want to run the operation, for example, https://domain.api.kustomerapp.com.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Kustomer account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Kustomer as the data source, you can select this connection.

## Transferring data from Kustomer with a flow
<a name="kustomer-transfer-data"></a>

To transfer data from Kustomer, create an Amazon AppFlow flow, and choose Kustomer as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Kustomer, see [Supported objects](#kustomer-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#kustomer-destinations).

## Supported destinations
<a name="kustomer-destinations"></a>

When you create a flow that uses Kustomer as the data source, you can set the destination to any of the following connectors: 
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
<a name="kustomer-objects"></a>

When you create a flow that uses Kustomer as the data source, you can transfer any of the following data objects to supported destinations:



- ** Apps**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** actions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** autoUpdate / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** cards / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** commands / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** current / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** dataSubscriptions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** disabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** events / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** hooks / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** inboundHookUris / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** klasses / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** kviews / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** meta / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** outboundWebhooks / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** roles / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** settingsPageConfig / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** shortcuts / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** statusAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** templates / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** triggers / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** widgets / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** workflows / **** Data type**:** Struct / **** Supported filters**:** 

- ** Audit Logs**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** changes / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** client / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** eventName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** eventVerb / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** expiresAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ip / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** objectId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** objectType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** org / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** publishedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** userId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** userType / **** Data type**:** String / **** Supported filters**:** 

- ** Auth Customer Settings**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** corsWhitelist / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** secret / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Auth Roles**
  - **** Field**:** ID
  - **** Data type**:** String
  - **** Supported filters**:** 

- ** Auth Tokens**
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** cidr / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** expireAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ipAddress / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** lastAccessedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** lastTokenChars / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** roles / **** Data type**:** List / **** Supported filters**:** 

- ** Brands**
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** iconUrl / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 

- ** Cards**
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** contexts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** url / **** Data type**:** String / **** Supported filters**:** 

- ** Categories**
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** categoryPositions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** hash / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** langs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** positions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** published / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** root / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Chat Settings**
  - **** Field**:** autoreply / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** closableChat / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** colors / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** disableAttachments / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** embedIconColor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** embedIconUrl / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** fallbackEmailIntroduction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** fallbackEmailSubject / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** greeting / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** noHistory / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** offhoursImageUrl / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** offhoursMessage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** outboundChatEnabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** pushSettings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** settingsVersion / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** showBrandingIdentifier / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** showEmailInputBanner / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** showTypingIndicatorCustomerWeb / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** showTypingIndicatorWeb / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** singleSessionChat / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** suppressConversationReopen / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** teamName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** version / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** volumeControl / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** widgetType / **** Data type**:** String / **** Supported filters**:** 

- ** Companies**
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Domains / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Emails / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Locations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ModifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Phones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** RoleGroupVersions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Socials / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Urls / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Whatsapps / **** Data type**:** List / **** Supported filters**:** 

- ** Conversation**
  - **** Field**:** accessOverride / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** assignedTeams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** assignedUsers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** assistant / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** channels / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** direction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ended / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** endedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** endedByType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** endedReason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** firstDone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** firstMessageIn / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** firstMessageOut / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** firstResponse / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** firstResponseSinceLastDone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** importedAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** inboundMessageCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** lastActivityAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** lastDone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lastMessageAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** lastMessageDirection / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** lastMessageIn / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lastMessageOut / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lastMessageUnrespondedTo / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lastMessageUnrespondedToSinceLastDone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lastResponse / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** matchedTimeBasedRules / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** messageCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** noteCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** outboundMessageCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** phase / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** predictions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** preview / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** priority / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** roleGroupVersions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** satisfaction / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** satisfactionLevel / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** sentiment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** skills / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** spam / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** suggestedShortcuts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** suggestedTags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Customers**
  - **** Field**:** Display Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Display Icon / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ExternalId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ExternalIds / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** accessOverride / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** activeUsers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** companyName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** conversationCounts / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** defaultLang / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** emails / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** facebookIds / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** firstName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** gender / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** instagramIds / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** lastActivityAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** lastConversation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lastName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** locations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** phones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** preview / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** progressiveStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** recentItems / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** recentLocation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** roleGroupVersions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** satisfactionLevel / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** sharedEmails / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** sharedExternalIds / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** sharedPhones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** sharedSocials / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** socials / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** timeZone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** urls / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** verified / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** watchers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** whatsapps / **** Data type**:** List / **** Supported filters**:** 

- ** Customers Searches**
  - **** Field**:** accessTeams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** accessUsers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** badgeColor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** cacheable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** dataHash / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** defaultVisibility / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** icon / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** position / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** private / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** showBadge / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** teamVisibilities / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** userVisibilities / **** Data type**:** List / **** Supported filters**:** 

- ** Customers Searches Pinned**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** 

- ** Customers Searches Positions**
  - **** Field**:** children / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** positions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Hooks Email**
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** debug / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** eventName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** hash / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Hooks Web**
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** debug / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** eventName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** hash / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** version / **** Data type**:** Integer / **** Supported filters**:** 

- ** KB Articles**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** categories / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** deletedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** hash / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** knowledgeBases / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** langVersions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** latestLangs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** metaDescription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metaKeywords / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** metaTitle / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** publishedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** scope / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** KB Forms**
  - **** Field**:** advanced / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** channel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** componentsV2 / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** conditions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** deflection / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** formHookEnabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** hash / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** klass / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** layout / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** layoutV2 / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** published / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** publishedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** recaptcha / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** replyFrom / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** snippets / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** wcag / **** Data type**:** Boolean / **** Supported filters**:** 

- ** KB Routes**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** routableId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** routableType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** url / **** Data type**:** String / **** Supported filters**:** 

- ** KB Tags**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** KB Templates**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** beta / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** images / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** jsxSnippets / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** manifest / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** version / **** Data type**:** String / **** Supported filters**:** 

- ** KB Themes**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** configSnippets / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** custom / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** jsxSnippets / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** lastFileUpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** manifest / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** templateTitle / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** templateVersion / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** templateVersionId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Kviews**
  - **** Field**:** advanced / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** appDisabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** components / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** conditions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** context / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** layout / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** meta / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** resource / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** template / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Messages**
  - **** Field**:** app / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** assignedTeams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** assignedUsers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** auto / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** channel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** createdByTeams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** direction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** directionType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** errorAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** externalId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** intentDetections / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** meta / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** preview / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reactions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** redacted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** sentAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** size / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** subject / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Notes**
  - **** Field**:** body / **** Data type**:** String / **** Supported filters**:** CONTAINS
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** createdByTeams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Notifications**
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** event / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Outbound Accounts**
  - **** Field**:** account / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** aliasUsername / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** app / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** channel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 

- ** Outbound Webhooks**
  - **** Field**:** appDisabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** consecutiveErrorsCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** events / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** headers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** isError / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** token / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** url / **** Data type**:** String / **** Supported filters**:** 

- ** Outbound Webhooks Events**
  - **** Field**:** events
  - **** Data type**:** List
  - **** Supported filters**:** 

- ** Outbound Webhooks Transactions**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** eventName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** nextRetry / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** sentAt / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** webhookId / **** Data type**:** String / **** Supported filters**:** 

- ** Routing Queue Rules**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** criteria / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** String / **** Supported filters**:** 

- ** Routing Queues**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** displayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** itemSize / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** priority / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** restrictTransfersByUsers / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** system / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Routing Settings**
  - **** Field**:** capacity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** externalQueues / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** workItemCapacity / **** Data type**:** Integer / **** Supported filters**:** 

- ** Routing Statuses**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** routable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** selectable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** statusType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** system / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Routing Work Items**
  - **** Field**:** channel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** completedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** firstEnterQueueAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** handle / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** hasSkills / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** itemSize / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ivr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lastRevision / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** paused / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** priority / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** queuedCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** resource / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** resourceCreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** resourceDirection / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** resourceFirstQueueTime / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** resourceRev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** resourceType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** skills / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** workItemNumber / **** Data type**:** Integer / **** Supported filters**:** 

- ** Routing Work Sessions**
  - **** Field**:** capacity / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** capacityRemaining / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** capacityStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** handledConversationCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** handledItemCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** hasPendingItem / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** hasSkills / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** idleSince / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** lastRevision / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** pausedWorkItemCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** routable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** signedInAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** signedOutAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** skills / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** statusType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** totalAvailable / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** totalAvailableAtCapacity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** totalAvailableIdleCapacity / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** totalCapacity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** totalTimeByStatus / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** totalUnavailable / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** totalUnavailableAtCapacity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** workItemCount / **** Data type**:** Integer / **** Supported filters**:** 

- ** Satisfaction**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** allQuestions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** channel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** criteria / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** delayTime / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** followUpType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** formType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** from / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** introduction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metaDescription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metaTitle / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** negativeQuestions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** positiveQuestions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** questions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ratingPrompt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** scale / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Schedules**
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** hours / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** timezone / **** Data type**:** String / **** Supported filters**:** 

- ** Settings**
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** app / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** value / **** Data type**:** String / **** Supported filters**:** 

- ** Shortcuts**
  - **** Field**:** appDisabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** conversation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** draft / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** isPrivate / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payload / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** rev / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Shortcuts Categories**
  - **** Field**:** categoryPositions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** root / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** shortcutPositions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Snippets**
  - **** Field**:** app / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** langs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** 

- ** Snoozes**
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** value / **** Data type**:** String / **** Supported filters**:** 

- ** Spam Senders**
  - **** Field**:** channel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** list / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** sender / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Teams**
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** displayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** icon / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** members / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** modifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** roleGroups / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Users**
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** DisplayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** EmailVerifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** FirstEmailVerifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ModifiedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Password / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** RoleGroups / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Roles / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** UserType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** firstLoginAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** isEmailValid / **** Data type**:** Boolean / **** Supported filters**:** 

- ** klasses**
  - **** Field**:** appDisabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createdAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** icon / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** s3DataUrl / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updatedAt / **** Data type**:** DateTime / **** Supported filters**:** 

