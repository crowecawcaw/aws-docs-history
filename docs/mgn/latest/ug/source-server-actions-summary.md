

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Source server actions summary
<a name="source-server-actions-summary"></a>

The following table summarizes the actions available on source servers at each phase of the migration lifecycle.


**Source server actions by migration phase**  

| **Action** | **Migration phase** | **Description** | 
| --- | --- | --- | 
| Edit replication settings | Before migration | Configure how data is replicated to the AWS staging area. | 
| Edit launch settings | Before migration | Configure how the migrated server will be launched as an Amazon EC2 instance. | 
| Add or manage tags | Before migration | Organize and identify source servers using tags. | 
| Configure post-launch actions | Before migration | Set up scripts or SSM documents to run after a test or cutover launch. | 
| Assign to application | Before migration | Group related servers into an application for coordinated migration. | 
| Start data replication | During migration | Start or restart data replication from the source server to AWS. | 
| Pause data replication | During migration | Temporarily stop replication to reduce costs. Lag will accumulate. | 
| Resume data replication | During migration | Resume replication after a pause. A resync will be performed. | 
| Launch test instance | During migration | Launch a non-disruptive test instance to validate the migrated server. | 
| Finalize test | During migration | Mark the test as complete and advance the server to the ready-for-cutover state. | 
| Launch cutover instance | During migration | Perform the final migration by launching the cutover instance in AWS. | 
| Monitor replication health | During migration | View replication status, lag, and alerts for each source server. | 
| Finalize cutover | After migration | Mark the migration as complete and stop data replication. | 
| Disconnect from service | After migration | Remove the server from active AWS Transform MGN management. | 
| Archive server | After migration | Move the server to the archived view to keep the console organized. | 
| Delete server | After migration | Permanently remove the server record from AWS Transform MGN. | 