# Drill Planning for AWS Elastic Disaster Recovery

**Drills vs Planned DR Events:** In some situations, the disaster recovery test will be a failover of the production environment in a planned event, with apps running in production in the recovery Region. It is advised to do a full production test on an annual basis to capture any blockers, and to be familiar with the process in the event of an actual disaster.

Testing your disaster recovery implementation is the only way to validate that your RPO and RTO objectives can be met when a real disaster occurs. Elastic Disaster Recovery natively supports the ability to launch drills without affecting your production environment. However, conducting a drill and launching a server as an EC2 instance is not
adequate to declare success. It’s important to test at an application or business process level to ensure that the end-to-end service can be delivered when the disaster recovery plan is activated. It is a best practice to perform drills regularly. There are a few things to note
before launching a Elastic Disaster Recovery drill:

- When launching a drill or recovery, you can launch up to 500 source servers in a single operation. Additional source servers can be launched in subsequent operations.
- It is a best practice to perform drills regularly. After launching drill instances, use either SSH (Linux) or RDP (Windows) to connect to your instance and ensure that everything is working correctly.
- Take into consideration that once a drill instance is launched, actual resources will be created in your AWS account and you will be billed for these resources. You can terminate the operation of launched Recovery
  instances once you verify that they are working properly without impact to data replication.
- We recommend that you test as often as possible. Test once a year at a minimum, even if it means reducing scope
  and testing a portion of the application or business function portfolio. This ensures the team is comfortable with the disaster recovery plan while also allowing them to identify any issues or required changes.
  When preparing for a disaster recovery test, it is critical to ensure that your Drill environment is configured properly. A drill will be conducted
  while the production environment remains intact. In order to minimize impact to the production environment we recommend the following:

- Network Considerations
  - Subnet configuration
    - CIDR range
      - You will want to ensure that your Drill subnet is configured with the same CIDR range size as your Failover subnet. This will ensure that the subnets are sized properly and any IP adjustments to the Drill/Failover machines remains the same.
      - With this in mind, you will want to ensure that the subnet where you are launching Drill instances is in an isolated network with no route to the source environment or production systems. This will ensure there are
        no IP address or routing conflicts during testing. We also recommend configuring security groups and access control lists to further reinforce these boundaries.

  - Routing
    - If your Drill requires access to services or dependencies outside of the Drill subnet, you should ensure the appropriate routing policies and
      rules are configured in the Drill subnet to support this connectivity.
    - Updating Launch Template to the Drill subnet
      - By default, you will want to have the Launch Templates configured for your Failover subnet. During a Drill, you will need to change that
        section of the Launch Template to the Drill subnet. Refer to the
        [EC2 launch template](../../../drs/latest/userguide/ec2-launch.md "../../../drs/latest/userguide/ec2-launch.md") for steps to complete. Additionally, launch settings can be
        changed for a single server or for multiple servers through the Elastic Disaster Recovery console. This option allows you to quickly make changes to multiple servers at once. Refer to
        [Configuring launch settings in AWS Elastic Disaster Recovery](../../../drs/latest/userguide/launching-target-servers.md "../../../drs/latest/userguide/launching-target-servers.md") for more details on making bulk changes to your Launch Templates.

- Infrastructure Services (such as AD and DNS)

      + Depending on the criteria for a successful Drill, you may need your Drill servers to connect to services such as Active Directory or other infrastructure services in order to complete a Drill. This might require additional scripting (or usage of appropriate SSM documents to automate the usage of AD after launch)




      	- With Elastic Disaster Recovery, you can replicate all applications and services, including Active Directory. With this approach, it is recommended to launch the drill version of AD first and wait until the service is up and running. Once the service is up, you can start to
      	launch the other applications or servers. This will ensure that the AD servers are ready to provide critical functions and services like authentication and authorization.
      	- An alternative approach is to extend Active Directory to the Drill subnet. It is advised to work with your system administrators to define the best method for your use case.

  Prior to launching a drill instance, ensure that your source servers are ready for testing by looking for the following indicators on the **Source servers** page:

1. Under the **Ready for Recovery** column, the server should show **Ready**. This means that the initial sync has been completed and all data from the source server has been replicated to AWS.
2. Under the **Data Replication Status** column, the server should show the **Healthy** status, but you can also launch the source server if the system is undergoing **Lag** or even **Stall**, but in that case the data may not be up to date. You can still launch a drill instance from a
   previous Point In Time.
3. Under the **Pending Actions** column, the server should show **Initiative Recovery Drill** if no drill instances have ever been launched for the server. Otherwise, the column will be blank. This helps you identify
   whether the server has had a recent drill launch.

## Launching drill instances

To launch a drill instance for a single source server or multiple source servers:

1. Go to the **Source servers** page and check the box to the left of each server for which you want to launch a drill instance.
2. Open the **Initiate recovery job** menu and select **Initiate drill**.
3. Select the Point in time snapshot from which to launch the drill instance for the selected source server. You can either select the **Use most recent data** option to use the latest snapshot available or select an earlier specific Point-in-time snapshot. You may opt to select an
   earlier snapshot in case you wish to return to a specific server configuration before a disaster occurred.
4. After you have selected the Point in Time snapshot, select **Initiate drill**.

The Elastic Disaster Recovery Console will indicate **Recovery job is creating drill instance for X source servers** when the drill has started.

Choose **View job details** on the dialog box to view the specific Job for the test launch in the **Recovery job history** tab.

## Successful drill instance launch indicators

You can tell that the Drill instance launch started successfully through several indicators on the **Source servers** page.

1. The **Last recovery result** column will show the status of the recovery launch and the time of the launch. A successful drill instance launch will show the **Successful** status. A launch that is still in progress
   will show the **Pending** status.
2. The launched Drill instance will also appear on the **Recovery instances** page.
