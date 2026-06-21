# AWS ACE connector

Use the AWS ACE connector to synchronize co-selling opportunities with the AWS Partner Network.

## AWS ACE connector

The AWS ACE (AWS Customer Engagements) connector synchronizes co-selling opportunities between AWS Marketplace Storefront and the AWS Partner Network co-selling program.

### Prerequisites

- An active AWS Partner Network (APN) membership
- ACE program enrollment
- Owner or Admin role at the organization level

### To connect AWS ACE

The AWS Partner Central ACE Integration wizard has three steps: Connect, Generate keys, and Configure. Each step shows a status of Pending, Successful, or Failed.

1. In the top-right corner, choose your profile avatar, choose **Organization Settings**, then choose the **Connectors** tab.
2. Find **AWS ACE** and choose **Connect**.
3. Choose the account you want to connect.
4. Choose **Save**.

### Configuration

After connecting, the wizard advances to the Generate keys step.

#### Generate keys

On the Generate keys step, the connector issues an API key and a uuid. After you generate the keys, the Generate Keys button is disabled because keys are issued only once.

#### Configure

On the Configure step, set the sync behavior:

| Setting                   | Description                                                              |
| ------------------------- | ------------------------------------------------------------------------ |
| Sync Mode                 | Choose a Sync Mode, for example CRM Unidirectional (CRM > ACE).          |
| Unidirectional Sync       | To restrict the connector to a one-way flow, select Unidirectional Sync. |
| Sync frequency            | Real-time or scheduled (hourly, daily)                                   |
| Opportunity stage mapping | Map your pipeline stages to ACE stages                                   |
| Auto-accept referrals     | Automatically accept inbound opportunities from AWS                      |

### What syncs

| Direction        | Data                                                           |
| ---------------- | -------------------------------------------------------------- |
| Storefront → ACE | New opportunities, stage updates, revenue changes, close dates |
| ACE → Storefront | Inbound referrals, AWS feedback, opportunity status changes    |

### To view sync logs

1. In the ACE connector settings, choose **Logs**.
2. View the sync history including:

   - Timestamp
   - Direction (inbound/outbound)
   - Record count
   - Status (success/error)
   - Error details (if applicable)

### Troubleshooting

| Issue                     | Resolution                                                  |
| ------------------------- | ----------------------------------------------------------- |
| Connection test fails     | Verify your account is active and APN membership is current |
| Opportunities not syncing | Check sync frequency setting and connector status           |
| Duplicate opportunities   | Verify field mapping for opportunity ID matching            |

### Related topics

- Creating co-selling opportunities
- Co-selling automation
- Connector overview
