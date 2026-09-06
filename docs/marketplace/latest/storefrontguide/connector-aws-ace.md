

# AWS ACE connector
<a name="connector-aws-ace"></a>

Use the AWS ACE connector to synchronize co-selling opportunities with the AWS Partner Network.

## AWS ACE connector
<a name="aws-ace"></a>

The AWS ACE (AWS Customer Engagements) connector synchronizes co-selling opportunities between AWS Marketplace Storefront and the AWS Partner Network co-selling program.

### Prerequisites
<a name="aws-ace-prerequisites"></a>
+ An active AWS Partner Network (APN) membership
+ ACE program enrollment
+ Owner or Admin role at the organization level

### To connect AWS ACE
<a name="aws-ace-to-connect-aws-ace"></a>

The AWS Partner Central ACE Integration wizard has three steps: Connect, Generate keys, and Configure. Each step shows a status of Pending, Successful, or Failed.

1. In the top-right corner, choose your profile avatar, choose **Organization Settings**, then choose the **Connectors** tab.

1. Find **AWS ACE** and choose **Connect**.

1. Choose the account you want to connect.

1. Choose **Save**.

### Configuration
<a name="aws-ace-configuration"></a>

After connecting, the wizard advances to the Generate keys step.

#### Generate keys
<a name="aws-ace-generate-keys"></a>

On the Generate keys step, the connector issues an API key and a uuid. After you generate the keys, the Generate Keys button is disabled because keys are issued only once.

#### Configure
<a name="aws-ace-configure-step"></a>

On the Configure step, set the sync behavior:


| Setting | Description | 
| --- | --- | 
| Sync Mode | Choose a Sync Mode, for example CRM Unidirectional (CRM > ACE). | 
| Unidirectional Sync | To restrict the connector to a one-way flow, select Unidirectional Sync. | 
| Sync frequency | Real-time or scheduled (hourly, daily) | 
| Opportunity stage mapping | Map your pipeline stages to ACE stages | 
| Auto-accept referrals | Automatically accept inbound opportunities from AWS | 

### What syncs
<a name="aws-ace-what-syncs"></a>


| Direction | Data | 
| --- | --- | 
| Storefront → ACE | New opportunities, stage updates, revenue changes, close dates | 
| ACE → Storefront | Inbound referrals, AWS feedback, opportunity status changes | 

### To view sync logs
<a name="aws-ace-to-view-sync-logs"></a>

1. In the ACE connector settings, choose **Logs**.

1. View the sync history including:
   + Timestamp
   + Direction (inbound/outbound)
   + Record count
   + Status (success/error)
   + Error details (if applicable)

### Troubleshooting
<a name="aws-ace-troubleshooting"></a>


| Issue | Resolution | 
| --- | --- | 
| Connection test fails | Verify your account is active and APN membership is current | 
| Opportunities not syncing | Check sync frequency setting and connector status | 
| Duplicate opportunities | Verify field mapping for opportunity ID matching | 

### Related topics
<a name="aws-ace-related-topics"></a>
+ Creating co-selling opportunities
+ Co-selling automation
+ Connector overview