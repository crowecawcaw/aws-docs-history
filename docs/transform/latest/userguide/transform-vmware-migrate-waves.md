# Prepare and migrate waves

At this stage, you will see migration waves in the **Job Plan**
pane. For each wave, perform the following steps. In some of these steps you will
have the option of importing an updated inventory file. AWS Transform allows one import
to a given target AWS account and target AWS Region at a time. This means that
if you work on more than one wave simultaneously, or if there is more than one
migration job running with the same target account, you must wait for an import to
finish before you can perform another import in a different wave or job.

## Prepare waves

Each wave includes a **Set up migration wave** task. On its **Collaboration** tab you can configure the wave's settings.

###### Set up migration wave

1. In the **Job Plan** pane, expand the step **Set
   up migration waves**, and then choose **Set EC2
   recommendation preferences**. Follow the instructions in the
   right pane, and then choose **Continue**. Learn more about Amazon EC2 recommendations in [Generating Amazon EC2 recommendations in AWS Migration Hub](../../../migrationhub/latest/ug/generating-ec2-recommendations.md "../../../migrationhub/latest/ug/generating-ec2-recommendations.md").
2. In the **Staging area subnet** section, you can choose a staging area subnet from the dropdown menu of the available subnets.

Only subnets that are tagged in VPCs _that are also tagged_ with these tag key-value pairs appear in the list.
Learn more in [VPC and subnet tags](#transform-tag-vpc-subnets "#transform-tag-vpc-subnets"). 3. For each wave, choose your [IP assigment approach](../../../AWSQT/flexible_ip/transform-vmware-migrate-network.md#vmware-migration-ip "../../../AWSQT/flexible_ip/transform-vmware-migrate-network.md#vmware-migration-ip"):

    * **Use source IP or the converted IP from the new CIDR**
    * **Use new IP using DHCP**

4. In the **Job Plan** pane, choose **Confirm
   inventory for `wave-name`**. Download
   the inventory file and review the list of servers and Amazon EC2 configurations.
   Modify the file if necessary, but do not remove columns or change the
   titles of the existing columns. You can control the operating system licensing
   options (BYOL / LI) and tenancy by specifying the configuration in columns with these headers: mgn:launch:placement:operating-system-licensing and mgn:launch:placement:tenancy. Learn more in
   [Import parameters](../../../mgn/latest/ug/import-main.md#import-parameters "../../../mgn/latest/ug/import-main.md#import-parameters") in the _Application Migration Service user guide_. After you choose whether to continue with
   the file you downloaded or to upload a version of the file that you updated,
   choose **Continue**.

###### Note

AWS Transform provides Amazon EC2 recommendations based on the utilization
specification of your source VMs. You can modify the suggested Amazon EC2 instance
types to include recommendations from the [Migration
Evaluator](https://aws.amazon.com/migration-evaluator/ "https://aws.amazon.com/migration-evaluator/"), [AWS Optimization and Licensing Assessment (OLA)](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/aws-ola.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/aws-ola.md"), or a [Migration assessment](transform-app-assessments.md "transform-app-assessments.md") job.

### VPC and subnet tags

Your VPCs and their subnets are automatically tagged with these tags so that their subnets appear in AWS Transform's list of available subnets:

- **Key:**
  `CreatedFor`
  **Value:**
  `AWSTransform`
- **Key:**
  `ATWorkspace`
  **Value:**
  `workspace ID`

## Migrate waves

When you migrate a wave, AWS Transform keeps you informed of the progress by providing a table in the **Collaboration** pane. You can also ask AWS Transform about the status of the migration in natural language, for example:

- What is the status of my servers?
- What's the status of my wave?
- What's the status of the step that I'm currently in?

###### Deploy replication agents

1.  In the **Job Plan** pane, expand **Deploy
    replication agents**, and then choose **Start
    replication agent deployment**. You have two options:

        * ****Use AWS Transform to automate
         deployment**:** To automate the deployment
         of the agents on the source servers in this wave, AWS Transform uses an
         MGN connector already deployed in your account. For information
         about how to deploy an MGN connector in your account, see [Set up
         the MGN Connector](../../../mgn/latest/ug/mgn-connector-setup-instructions.md "../../../mgn/latest/ug/mgn-connector-setup-instructions.md") in the *Application Migration Service User
         Guide*.


        To use this option, perform the following steps:



        	1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
        	2. In the left navigation pane, under **Node
        	 Tools**, choose **Fleet
        	 Manager**.
        	3. Choose the name of the managed instance of the MGN
        	 connector that you want AWS Transform to use for this
        	 wave.
        	4. Tag the managed instance with the following key-value
        	 pairs.




        		+ Key: `CreatedFor` Value: `AWSTransform`
        		+ Key: `ATWorkspace`  Value: `workspace ID`
        	Find your workspace ID in the AWS Transform web app URL, https:// ... /workspace/`workspace-id`/job/job-id
        	5. In AWS Transform, choose **Use AWS Transform to automate
        	 deployment**.
        	6. Specify the MGN connector that you tagged and the
        	 AWS Secrets Manager secret that you want AWS Transform to use for this
        	 wave. You must create a single set of credentials for the
        	 MGN connector to use for deploying replication agents on all
        	 servers in a particular wave. For information about setting
        	 up the secret, see [Register server credentials](../../../mgn/latest/ug/connector-register-server-credentials.md "../../../mgn/latest/ug/connector-register-server-credentials.md").
        	7. If AWS Transform encounters errors during the deployment of
        	 the agent, you will see those errors in the **Job
        	 Plan** pane. Choose each error in the
        	 **Job Plan** pane to view its details
        	 in the **Collaboration** tab.
        	8. After you resolve all errors, you can track the
        	 replication status for the wave by choosing **Review
        	 replication status** in the **Job
        	 Plan** pane.
        * ****Deploy replication agents on your
         own**:** You can deploy the replication
         agents on the source servers manually. Alternatively, you can use
         the MGN connector or another automation framework to deploy them on
         your own. For information about how to set up the MGN connector, see
         [Set up
         the MGN Connector](../../../mgn/latest/ug/mgn-connector-setup-instructions.md "../../../mgn/latest/ug/mgn-connector-setup-instructions.md") in the *Application Migration Service User
         Guide*.


        To deploy the replication agents manually, or use an automation
         framework other than the MGN Connector to deploy them, perform the
         following steps.




        	1. Go to the AWS Application Migration Service console, and export a list of your
        	 servers. For instructions, see [Exporting your data
        	 inventory](../../../mgn/latest/ug/export-main.md "../../../mgn/latest/ug/export-main.md").
        	2. Filter the list by wave to obtain a list of the servers in
        	 the current wave.
        	3. Follow the instructions under [Installing
        	 the AWS Replication Agent](../../../mgn/latest/ug/agent-installation.md "../../../mgn/latest/ug/agent-installation.md"). Specify the
        	 `user-provided-id` parameter, and for every
        	 server set its value to the server's
        	 `mgn:server:user-provided-id` as it appears
        	 in the .csv file that you exported from AWS Application Migration Service. AWS Transform
        	 connects the replication agent with the imported server
        	 using this parameter. If it's not provided, MGN will create
        	 a separate instance of source server for each agent that is
        	 installed.

    **To see the replication agent installation
    status**, check the AWS Systems Manager run command history at agent
    installation time. For information, see [Understanding command statuses](../../../systems-manager/latest/userguide/monitor-commands.md "../../../systems-manager/latest/userguide/monitor-commands.md") in the
    _AWS Systems Manager User Guide_.

**To see the replication status in
real-time**, go to the AWS Application Migration Service console. Status updates in the
AWS Transform web app are delayed.

**For quotas related to replication**, see
[AWS Application Migration Service service quota limits](../../../mgn/latest/ug/MGN-service-limits.md "../../../mgn/latest/ug/MGN-service-limits.md") in the _Application Migration Service User
Guide_.

###### Note

AWS Transform does not support MGN agentless replication. For information
about agentless replication, see [Agentless
replication overview](../../../mgn/latest/ug/installing-vcenter-overview-mgn.md "../../../mgn/latest/ug/installing-vcenter-overview-mgn.md") in the _Application Migration Service User
Guide_. 2. When replication is complete, expand **Review the replication
status** in the **Job Plan** pane. In the
right pane you can see the status of the replication and resolve replication
alerts.

###### Note

To proceed, you must install the MGN replication agent on all servers in a
wave. Disconnect and archive servers on which you don't install the replication
agent. You can use the [disconnect-from-service](../../../cli/latest/reference/mgn/disconnect-from-service.md "../../../cli/latest/reference/mgn/disconnect-from-service.md") command to disconnect servers. To archive
disconnected servers, use the [mark-as-archived](../../../cli/latest/reference/mgn/mark-as-archived.md "../../../cli/latest/reference/mgn/mark-as-archived.md") command. The archiving command only works for
source servers whose lifecycle state is `DISCONNECTED`.

###### Launch test instances

1. In the **Job Plan** pane, under **Launch test
   instances**, choose **Confirm instance
   launch**.
2. Download the inventory file, review it, and choose whether to continue
   with the current file or upload a modified one, then choose
   **Launch test instances**. You can change the launch
   settings within the inventory file, but don't modify the list of source
   servers and applications.

###### Mark applications as ready for cutover

1. In the **Job Plan** pane, expand **Mark
   applications as ready for cutover**, and choose
   **Mark applications as ready for cutover**.
2. In the **Collaboration** tab, review the replication
   status of each application, and resolve replication alerts.
3. Choose **Mark for cutover**.

###### Launch cutover instances

1. In the **Job Plan** pane, under **Launch cutover
   instances**, choose **Confirm instance
   launch**.
2. Download and open the inventory file, review the inventory, and choose
   whether to continue with the current inventory or upload a modified one. At
   this step, don't modify the list of source servers and applications listed
   in the inventory file. You can only change the launch settings within the
   inventory file.
3. Choose whether to continue with the current inventory or upload a modified
   one, and then choose **Continue**.
4. Choose **Launch cutover instances**.

###### Finalize cutover

1. (Optional) Review the launched Amazon EC2 cutover instances, validate
   connectivity and run acceptance tests. If you want to fix anything because
   there's a connectivity issue or a problem in the testing, you need to revert
   the cutover. This is the time to revert it.
2. In the **Job Plan** pane, expand **Finalize
   cutover**, and then choose **Start finalizing
   cutover**. Finalizing the cutover removes the replication
   agents. After you finalize the cutover you cannot make any changes, you
   cannot fix any connectivity issues, or anything else, and you cannot revert
   the cutover.
3. Choose **Finalize cutover**.

### Manage server status

During wave migration you can ask AWS Transform to update or change the status of a server. For example, if 9 out of 10 of the servers in
your wave passed the test phase but one failed, you can allow AWS Transform to continue to move the 9 into the next phase, and ask to put re-run the test on the tenth.

Lifecycle states include:

- **Not ready** – The server is undergoing the initial sync process
  and is not yet ready for testing. Data replication can only commence
  once all of the initial sync steps have been completed.
- **Ready for testing** – The server has been successfully added
  and data replication has started. test
  or cutover instances can now be launched for this server.
- **Test in progress** – A Test instance is currently being
  launched for this server.
- **Ready for cutover** – This server has been tested and is now
  ready for a cutover instance to be launched.
- **Cutover in progress** – A cutover instance is currently being
  launched for this server.
- **Cutover complete** – This server has been cutover. All of the
  data on this server has been migrated to the AWS cutover
  instance.
- **Disconnected** – This server has been disconnected.
