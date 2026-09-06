

# Preparing for recovery
<a name="preparing-failover"></a>

 After installing the AWS Elastic Disaster Recovery Agent on your Source Servers, we recommend validating your Source Server settings and testing (drilling) frequently in preparation of a recovery event. Configuration of the recovery environment includes DRS Launch Settings, EC2 Launch Template, and Post-Launch Actions. 

 Valid and up-to-date configuration and drilling facilitates lowering the [RTO](CloudEndure-Concepts.md#What-is-RTO). 

## Validate launch settings
<a name="preparing-failover-settings"></a>

After successful installation, we recommend validating your individual Source Server Settings to ensure they meet your recovery requirements. These settings can even be modified during the **Initial Sync** phase. 


| Launch Setting | Example Settings | More Information | 
| --- | --- | --- | 
| DRS Launch Settings |  +  Automated Instance type right-sizing. <br />+  Start instance on launch. <br />+  Operating System Licensing.   | [DRS Launch Settings](default-drs-launch-settings.md) | 
| EC2 Launch Template |  +  Instance profile (IAM role attached to the instance). <br />+  Recovery Instance VPC, Subnet, and Security Group configuration.   | [EC2 Launch Template](default-ec2-launch-template.md) | 
| Post Launch Actions |  +  Install CloudWatch agent. Validate HTTP/HTTPS connectivity.   | [Post Launch Actions](post-launch-action-settings-overview.md) | 

## Recovery drill overview
<a name="recovery-drill-overview"></a>

 A Recovery Drill is a non-disruptive test that performs all the same steps as an actual recovery. Recovery Drills run with the same Source Server Launch Settings and Point in Time snapshots that a Recovery would. As a result, we recommend adjusting any Source Server Launch Settings to isolate Drill Instances when necessary to avoid production or business impact. You can use verification post-launch actions when performing a drill to ensure that Launch Settings are accurate. A Recovery Drill can be performed with an individual source server, or it can include as many source servers as necessary to simulate the recovery of an application. 

 Recovery Drills will create EC2 resources in your Target AWS Account upon completion; these resources will be billed by the respective service until deleted. Recovery Drill EC2 resources will automatically be cleaned up if a Recovery Drill is performed again with the same Source Server. 

## Recovery drill objectives
<a name="failback-drill-goals"></a>

 Performing a Recovery Drill will assist in ensuring DRS can fulfill your Recovery Objectives during a failover event. Some Recovery Objectives can include: 
+ Ensuring Recovery Instances obtain Healthy System and Instance [ Status Checks.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html)
+ Ensuring all components in an application can communicate with one another.
+ Ensuring users can interact successfully with the application.

 Frequent and successful Recovery Drills will ensure your team can meet RTO/RPO goals during a failover event. We recommend performing a drill on at least a quarterly basis; individual compliance needs may necessitate more frequent drills. 

## Performing recovery drills
<a name="failback-performing-drill"></a>

 Once a Source Server has reached **Healthy**, a recovery drill can be performed. Recovery Drills should also be performed whenever the last recovery result was not Successful, or it has been a significant amount of time since a Successful Recovery Drill has been performed. 

 As long as Initial Sync has completed, a Recovery Drill can be performed, even if a Source Server is in **Lag** or **Stall** status. 

------
#### [ DRS Console ]

**Performing a Recovery Drill**

1.  Navigate to the AWS Elastic Disaster Recovery Console. In the left navigation pane, select **Source Servers** 

1.  Select one or more source servers, then select **Initiate Recovery Job**. 

1.  Select **Initiate recovery drill** 

1.  Select a Point in Time to recover to: 
   +  Select "Use most recent data" to attempt to create a sub-second RPO snapshot from the source server(s). 
   +  Select a specific time to use snapshots created at that timestamp, or slightly before if a snapshot was unavailable for a particular source server(s). 

1.  Select **Initiate drill**. 

1.  (Optional) Monitor Recovery Drill progress from the AWS Elastic Disaster Recovery Console **Recovery Job History**. 

------
#### [ Command Line ]

**Performing a Recovery Drill**

 Recovery Drills can be started via command line. 

1.  (optional) Obtain Recovery (PIT) Snapshot to recover to: 
   +  [describe-recovery-snapshots](https://docs.aws.amazon.com/cli/latest/reference/drs/describe-recovery-snapshots.html) (AWS CLI) 

     ```
     aws drs describe-recovery-snapshots --source-server-id {{s-123456789abcdefgh}}
     ```
   +  [Get-EDRSRecoverySnapshot](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EDRSRecoverySnapshot.html) (DRS Tools for Windows PowerShell) 

     ```
     Get-EDRSRecoverySnapshot -SourceServerID {{s-123456789abcdefgh}}
     ```

1.  Perform a Recovery Drill, specifying IsDrill: 
   +  [start-recovery](https://docs.aws.amazon.com/cli/latest/reference/drs/start-recovery.html) (AWS CLI) 

      With Recovery Snapshot 

     ```
     aws drs start-recovery --source-servers recoverySnapshotID={{pit-123456789abcdefgh}},sourceServerID={{s-123456789abcdefgh}} --is-drill
     ```

      Attempt to Use Latest Snapshot 

     ```
     aws drs start-recovery --source-servers sourceServerID={{s-123456789abcdefgh}} --is-drill
     ```
   +  [Start-EDRSRecovery](https://docs.aws.amazon.com/powershell/latest/reference/items/Start-EDRSRecovery.html) (DRS Tools for Windows PowerShell) 

      With Recovery Snapshot 

     ```
     $sourceServer = new-object Amazon.Drs.Model.StartRecoveryRequestSourceServer
     $sourceServer.RecoverySnapshotID = {{'pit-123456789abcdefgh'}}
     $sourceServer.SourceServerID = {{'s-123456789abcdefgh'}}
     Start-EDRSRecovery -SourceServer $sourceServer
     ```

      Attempt to Use Latest Snapshot 

     ```
     $sourceServer = new-object Amazon.Drs.Model.StartRecoveryRequestSourceServer;
     $sourceServer.SourceServerID = {{'s-123456789abcdefgh'}}
     Start-EDRSRecovery -SourceServer $sourceServer
     ```

------

## Post recovery drill actions
<a name="failback-cleanup-drill"></a>

Once a Recovery Drill has been successfully completed, we recommend cleaning up the recovery environment. Leaving Recovery Drill resources running may result in increased AWS charges. We recommend cleaning up your environment via AWS Elastic Disaster Recovery to ensure all resources created during the drill are removed.

------
#### [ DRS Console ]

**Performing a Recovery Drill**

1.  Navigate to the AWS Elastic Disaster Recovery Console. In the left navigation pane, select **Recovery instances**. 

1.  Select one or more source servers, then select **Actions**. 

1.  Select **Terminate recovery instances**. 

1.  Select **Terminate** on any dialog boxes. 

------
#### [ Command Line ]

**Cleaning up Recovery Drill**

 Cleaning up Drills can be started via command line. 

1.  Identify any Recovery Instances. 
   +  [describe-recovery-instances](https://docs.aws.amazon.com/cli/latest/reference/drs/describe-recovery-instances.html) (AWS CLI) 

     ```
     aws drs describe-recovery-instances
     ```
   +  [Get-EDRSRecoveryInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EDRSRecoveryInstance.html) (DRS Tools for Windows PowerShell) 

     ```
     Get-EDRSRecoveryInstance
     ```

1.  Terminate the Recovery Instances. 
   +  [terminate-recovery-instances](https://docs.aws.amazon.com/cli/latest/reference/drs/terminate-recovery-instances.html) (AWS CLI) 

     ```
     aws drs terminate-recovery-instances --recovery-instance-ids {{i-123456789abcdefgh}}
     ```
   +  [Stop-EDRSRecoveryInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EDRSRecoveryInstance.html) (DRS Tools for Windows PowerShell) 

     ```
     Stop-EDRSRecoveryInstance -RecoveryInstanceIDs {{'i-123456789abcdefgh'}}
     ```

------