

# Point in time (PIT) policy
<a name="point-in-time"></a>

AWS Elastic Disaster Recovery allows you to select the number of days for which point in time snapshots are retained through the **Point in time (PIT) policy** field. 

You can select to save PIT snapshots for 1 to 365 days. Saving PIT snapshots for more days allows you more recovery options, but also results in increased costs. [Learn more about Point in time.](CloudEndure-Concepts.md#point-in-time-faq) 

**Important**  
The PIT policy must contain exactly three rules: one for MINUTE, one for HOUR, and one for DAY. The snapshot frequency intervals and retention durations for the MINUTE rule (`interval=10`, `retentionDuration=60`) and HOUR rule (`interval=1`, `retentionDuration=24`) are fixed and cannot be modified. Only the DAY rule's `retentionDuration` is configurable, with a value from 1 to 365 days.

------
#### [ DRS Console ]

**Adjusting PIT Retention Rate**

1.  Navigate to the AWS Elastic Disaster Recovery Console. In the left navigation pane, select **Source Servers** 

1.  Select one or more source servers, then select **Replication**. 

1.  Select **Edit replication settings**. 

1.  Navigate to **Point in time (PIT) policy**. 

1.  Enter a new Integer from 1 to 365 in **Snapshot retention (in days)**. 

1.  Select **Save replication settings**. 

------
#### [ Command Line ]

**Adjusting PIT Retention Rate**
+  [update-replication-configuration](https://docs.aws.amazon.com/cli/latest/reference/drs/update-replication-configuration.html) (AWS CLI) 

  ```
  aws drs update-replication-configuration --source-server-id {{s-123456789abcdefgh}} --pit-policy enabled=true,interval=10,retentionDuration=60,ruleID=1,units="MINUTE" enabled=true,interval=1,retentionDuration=24,ruleID=2,units="HOUR" enabled=true,interval=1,retentionDuration={{14}},ruleID=3,units="DAY" 
  ```

------