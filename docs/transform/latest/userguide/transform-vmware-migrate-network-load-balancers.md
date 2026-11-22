

# Migrate source load balancers

Move your load balancing to AWS without rebuilding each virtual server by hand. AWS Transform reads the configuration of your load balancer and maps each virtual server to an Application Load Balancer (ALB) or a Network Load Balancer (NLB), with its listeners and target groups. Before anything deploys, you see which virtual servers migrate, which don't, and what behaves differently on AWS.

Choose **Include load balancers** when your source environment uses a supported load balancer and you are mapping a source network to new VPCs. AWS Transform adds the load balancers to your network design, and you review and deploy them with the network. You make this choice while you work through [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md). Load balancer migration is available when you upload a source network file.

The following table lists the supported source load balancers and their configuration files.


| Source load balancer | Configuration file | 
| --- | --- | 
| [F5 BIG-IP Local Traffic Manager (LTM)](#transform-vmware-lb-f5) | bigip.conf, or an archive of the configuration files | 

You can include one source load balancer in a job.

AWS Transform guides you through the following steps, handling the analysis and generation while you make the decisions:

1. Provide your load balancer configuration file.

1. Review the load balancer plan.

1. Continue the network migration.

1. Finish setup after deployment.

## Step 1: Provide your load balancer configuration file
<a name="transform-vmware-lb-config-file"></a>

After AWS Transform processes your source network file, it asks whether you also use a supported load balancer. Choose **Include load balancers** and provide the configuration file that you exported from your load balancer. The load balancer configuration must be a separate file from your source network file.

As with the source network file, you can enter the name of a file from User Uploads, or upload a new file directly in the chat.

Then select a network topology and a security groups mapping strategy, the same as for any source network, and start network mapping. AWS Transform maps the load balancers together with the network. For more information, see [Network topologies](transform-vmware-migrate-network-new-vpcs.md#network-topologies) and [Security groups mapping](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-security-group-association) in [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md).

## Step 2: Review the load balancer plan
<a name="transform-vmware-lb-plan"></a>

When network mapping completes, AWS Transform shows a load balancer migration plan with your network design. The plan summarizes the following:
+ How many virtual servers (VIPs) migrate, and how many ALBs and NLBs they become.
+ How many virtual servers don't migrate, and why.
+ The differences between your source load balancer and AWS, and how many need your acknowledgement.

HTTP and HTTPS virtual servers become ALBs. TCP and UDP virtual servers become NLBs.

To see each load balancer, ask for the full details. The details list each load balancer with its type, scheme, listeners, target groups, and status. Target groups deploy empty. When you launch test and cutover instances, AWS Transform asks whether to register them as targets. For more information, see the [Test](transform-vmware-ms-testing.md) and [Cutover](transform-vmware-ms-cutover.md) steps in [Migrate servers](transform-vmware-migrate-servers.md). AWS Transform also creates a targets security group that admits the load balancer and attaches it to your servers.

### Differences from your source load balancer
<a name="transform-vmware-lb-differences"></a>

A source load balancer and Elastic Load Balancing don't work the same way. ALBs and NLBs are managed services with their own features and defaults, so AWS Transform can't always reproduce your source configuration exactly. It approximates a setting where AWS has a close equivalent, leaves it out where there is none, and applies AWS defaults for addressing and access. Review each difference so you know what changes when traffic moves.

AWS Transform reports the differences in three groups:
+ **Behavior changes:** Source behavior that changes on AWS. You must acknowledge each one before AWS Transform includes the load balancers. The behavior changes depend on your source load balancer. See [Source-specific details](#transform-vmware-lb-sources).
+ **Warnings:** Items that need your attention.
+ **Information notes:** Items that need no action.

Warnings include the following:
+ **Address conflict risk:** AWS assigns load balancer addresses when the load balancers deploy, before your servers launch, and you can't choose them. A server that keeps its address can fail to launch if a load balancer took that address first. After deployment, compare the load balancer addresses with the addresses your servers keep. If an address clashes, assign the affected server a different address before you launch it. For more information, see [IP assignment strategy](transform-vmware-ms-setup-wave.md#transform-vmware-ms-ip-assignment).
+ **Missing HTTPS listener:** Virtual servers that terminate TLS on the source load balancer deploy without an HTTPS listener. Add it after deployment, as described in [Step 4](#transform-vmware-lb-finish).

Information notes include the following:
+ **Client ranges:** The load balancers admit only the workload VPC ranges and the mapped on-premises ranges as clients, even if your source load balancer accepted any source. Clients outside those ranges can't connect until you add them to the load balancer security group.
+ **Internal scheme:** All load balancers are internal, so they are reachable only from your networks. A service that must face the internet needs a new internet-facing load balancer.
+ **Cross-zone balancing:** An NLB keeps the VIP address as mapped to AWS, unless the plan notes otherwise. That address is in one Availability Zone. Cross-zone balancing is on so the NLB can reach targets in other zones. Cross-zone traffic is charged.
+ **Quotas:** Check the Elastic Load Balancing quotas in the target Region for the number of ALBs and NLBs that the plan needs.

### Virtual servers that don't migrate
<a name="transform-vmware-lb-not-migrating"></a>

AWS Transform doesn't generate a load balancer for virtual servers that are disabled on the source load balancer. It also skips a virtual server whose pool spans network segments, and an ALB that would have subnets in fewer than two Availability Zones. Other reasons depend on your source load balancer. See [Source-specific details](#transform-vmware-lb-sources). The load balancer plan lists every virtual server that doesn't migrate and why.

### Include the load balancers
<a name="transform-vmware-lb-include"></a>

AWS Transform asks whether to include the load balancers. To include them, acknowledge the behavior changes. You can ask AWS Transform to explain any difference before you acknowledge it.

You can also create a gaps summary file (.md). It lists the virtual servers that don't migrate and why, every behavior change with its acknowledgement status, and the warnings and information notes, each with an explanation. AWS Transform shares a download link for the file in the chat.

## Step 3: Continue the network migration
<a name="transform-vmware-lb-continue"></a>

After you include the load balancers, the remaining steps are the same as for any source network: review and optimize the network, optionally generate a network diagram, configure resource tagging, and deploy. AWS Transform deploys the load balancers with the network, or includes them in the CloudFormation and AWS CDK L1 output that it generates for self-deployment. With AWS Transform-managed deployment, the same deployment approvals apply. Load balancers are in the CloudFormation and AWS CDK L1 output only. They are not in the AWS CDK L2, Terraform, or Landing Zone Accelerator output.

For more information, see [Review and optimize your network](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-review-vpc-configs), [Network diagram](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-network-diagram), [Configure resource tagging](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-tag-network-resources), and [Deploy your network](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-deploy-network) in [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md).

## Step 4: Finish setup after deployment
<a name="transform-vmware-lb-finish"></a>

When the deployment succeeds, AWS Transform lists the deployed load balancers and what is left to do. Complete the following:
+ **Add HTTPS listeners:** Import the certificate, key, and chain from the TLS configuration of your source load balancer into AWS Certificate Manager (ACM). Then add an HTTPS listener on the virtual server's port that forwards to the generated target group.
+ **Update DNS:** ALBs don't keep the source virtual server address, so point your DNS records at the load balancer DNS names. Clients that connect to an ALB by IP address must change. NLBs keep the VIP address as mapped to AWS, unless the plan notes otherwise. If an NLB can't use that address, it gets a new one and the plan flags it. If clients connect by IP address, check the plan for the mapped address.
+ **Configure security groups:** AWS Transform creates a targets security group that admits the load balancer and attaches it to your servers, even if you proceeded without security groups. If you proceeded without security groups, configure security groups for your workloads before you migrate servers.
+ **Register targets:** Target groups deploy empty, so your load balancers send no traffic until you register instances. When you launch test and cutover instances, AWS Transform asks in the chat whether to register the launched instance in the same target group as its source server. For more information, see the [Test](transform-vmware-ms-testing.md) and [Cutover](transform-vmware-ms-cutover.md) steps in [Migrate servers](transform-vmware-migrate-servers.md).

## Source-specific details
<a name="transform-vmware-lb-sources"></a>

Each source load balancer has its own configuration file, terminology, behavior changes, and virtual servers that don't migrate.

### F5 BIG-IP Local Traffic Manager (LTM)
<a name="transform-vmware-lb-f5"></a>

AWS Transform migrates the Local Traffic Manager (LTM) module of F5 BIG-IP: its virtual servers, with their pools and monitors. AWS Transform doesn't migrate other BIG-IP modules.

**Configuration file:** Provide the `bigip.conf` configuration file that you export from your F5 BIG-IP system, or an archive (zip or tar) of the configuration files, including `bigip_base.conf` and partition files. F5 calls each entry that receives client traffic a virtual server, identified by a VIP.

**Behavior changes:** You must acknowledge each F5 behavior change before AWS Transform includes the load balancers.

The following table lists examples of F5 behavior changes.


| Difference | What changes | 
| --- | --- | 
| Client IP | Servers see the ALB address. The client address is only in the X-Forwarded-For header. Update any application logic or logging that relies on the source IP. | 
| Health checks | An F5 monitor with no receive string treats any reply as healthy. An ALB health check accepts only HTTP 200 to 499, so a target that returns a 5xx response is marked unhealthy. A monitor with a receive string becomes a check for HTTP 200, without content matching. | 
| Balancing algorithm | Least connections becomes least outstanding requests on an ALB, and round-robin becomes a per-flow hash on an NLB. Traffic spreads across targets similarly but not identically. | 
| Session persistence | An F5 persistence profile with no ALB equivalent isn't translated, so sessions don't stay on one server. | 
| Cookie duration | An F5 session cookie always becomes a load balancer cookie with a duration of 86,400 seconds (one day). A cookie with its own expiry keeps it, from 1 second to 7 days. Clients stay on one server for up to that long, even across browser restarts. | 

**HTTPS listeners:** Virtual servers that use an F5 client-ssl profile deploy without an HTTPS listener. Import the certificate, key, and chain named in the profile into ACM, then add the listener on the virtual server's port.

**Virtual servers that don't migrate:** In addition to disabled virtual servers, AWS Transform doesn't generate a load balancer for virtual servers that have iRules or LTM policies attached, or that use IPv6 VIPs. AWS Transform doesn't translate iRule logic. Rebuild it manually if you still need it.