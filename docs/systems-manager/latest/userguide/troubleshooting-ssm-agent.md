• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Troubleshooting SSM Agent

If you experience problems running operations on your managed nodes, there might be a
problem with AWS Systems Manager Agent (SSM Agent). Use the following information to help you view
SSM Agent log files and troubleshoot the agent. If your agent appears to be unresponsive
or has reduced communication frequency, see [Understanding SSM Agent hibernation](ssm-agent-technical-details.md#ssm-agent-hibernation "ssm-agent-technical-details.md#ssm-agent-hibernation").

###### Topics

- [SSM Agent is out of date](#ssm-agent-out-of-date "#ssm-agent-out-of-date")
- [Troubleshoot issues using
  SSM Agent log files](#systems-manager-ssm-agent-log-files "#systems-manager-ssm-agent-log-files")
- [Agent log
  files don't rotate (Windows)](#systems-manager-ssm-agent-troubleshooting-log-rotation "#systems-manager-ssm-agent-troubleshooting-log-rotation")
- [Unable
  to connect to SSM endpoints](#systems-manager-ssm-agent-troubleshooting-endpoint-access "#systems-manager-ssm-agent-troubleshooting-endpoint-access")
- [Verify your VPC configuration](#agent-ts-vpc-configuration "#agent-ts-vpc-configuration")
- [Verify your VPC DNS-related
  attributes](#agent-ts-dns-attributes "#agent-ts-dns-attributes")
- [Verify ingress rules on endpoint
  security groups](#agent-ts-ingress-egress-rules "#agent-ts-ingress-egress-rules")
- [Use ssm-cli to troubleshoot managed node
  availability](#agent-ts-ssm-cli "#agent-ts-ssm-cli")

## SSM Agent is out of date

An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
updates are made to existing tools. Failing to use the latest version of the agent can
prevent your managed node from using various Systems Manager tools and features. For that reason, we
recommend that you automate the process of keeping SSM Agent up to date on your machines. For
information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
updates.

## Troubleshoot issues using

SSM Agent log files

SSM Agent logs information in the following files. The information in these files
can also help you troubleshoot problems. For more information about SSM Agent log
files, including how to turn on debug logging, see [Viewing SSM Agent logs](ssm-agent-logs.md "ssm-agent-logs.md").

###### Note

If you choose to view these logs by using Windows File Explorer, be sure to
allow the viewing of hidden files and system files in Folder Options.

###### On Windows

- `%PROGRAMDATA%\Amazon\SSM\Logs\amazon-ssm-agent.log`
- `%PROGRAMDATA%\Amazon\SSM\Logs\errors.log`

###### On Linux and macOS

- `/var/log/amazon/ssm/amazon-ssm-agent.log`
- `/var/log/amazon/ssm/errors.log`

For Linux managed nodes, you might find more information in the
`messages` file written to the following directory:
`/var/log`.

For additional information about troubleshooting using agent logs, see [How do I use SSM Agent logs to
troubleshoot issues with SSM Agent in my managed instance?](https://repost.aws/knowledge-center/ssm-agent-logs "https://repost.aws/knowledge-center/ssm-agent-logs") in the
_AWS re:Post Knowledge Center_.

## Agent log

files don't rotate (Windows)

If you specify date-based log file rotation in the seelog.xml file (on Windows Server
managed nodes) and the logs don't rotate, specify the `fullname=true`
parameter. Here is an example of a seelog.xml configuration file with the
`fullname=true` parameter specified.

```

<seelog type="adaptive" mininterval="2000000" maxinterval="100000000" critmsgcount="500" minlevel="debug">
   <exceptions>
      <exception filepattern="test*" minlevel="error" />
   </exceptions>
   <outputs formatid="fmtinfo">
      <console formatid="fmtinfo" />
      <rollingfile type="date" datepattern="200601021504" maxrolls="4" filename="C:\ProgramData\Amazon\SSM\Logs\amazon-ssm-agent.log" fullname="true" />
      <filter levels="error,critical" formatid="fmterror">
         <rollingfile type="date" datepattern="200601021504" maxrolls="4" filename="C:\ProgramData\Amazon\SSM\Logs\errors.log" fullname="true" />
      </filter>
   </outputs>
   <formats>
      <format id="fmterror" format="%Date %Time %LEVEL [%FuncShort @ %File.%Line] %Msg%n" />
      <format id="fmtdebug" format="%Date %Time %LEVEL [%FuncShort @ %File.%Line] %Msg%n" />
      <format id="fmtinfo" format="%Date %Time %LEVEL %Msg%n" />
   </formats>
</seelog>

```

## Unable

to connect to SSM endpoints

SSM Agent must allow HTTPS (port 443) outbound traffic to the following
endpoints:

- `ssm.`region`.amazonaws.com`
- `ssmmessages.`region`.amazonaws.com`

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

###### Note

Prior to 2024,
`ec2messages.`region`.amazonaws.com` was
also required. For AWS Regions launched before 2024, allowing traffic to
`ssmmessages.`region`.amazonaws.com`
is still required but optional to
`ec2messages.`region`.amazonaws.com`.

For Regions launched in 2024 and later, allowing traffic to
`ssmmessages.`region`.amazonaws.com`
is required, but
`ec2messages.`region`.amazonaws.com`
endpoints are not supported for these Regions.

SSM Agent won't work if it can't communicate with the preceding endpoints, as
described, even if you use AWS provided Amazon Machine Images (AMIs) such as Amazon Linux 2 or
Amazon Linux 2023. Your network configuration must have open internet access or you must
have custom virtual private cloud (VPC) endpoints configured. If you don't plan on
creating a custom VPC endpoint, check your internet gateways or NAT gateways. For
more information about how to manage VPC endpoints, see [Improve the security of EC2 instances by using VPC
endpoints for Systems Manager](setup-create-vpc.md "setup-create-vpc.md").

## Verify your VPC configuration

If you are using a virtual private cloud (VPC), in order to manage EC2 instances
with Systems Manager, your VPC endpoints must be configured properly for
`ssm.`region`.amazonaws.com`,
`ssmmessages.`region`.amazonaws.com`, and
in some cases explained earlier in this topic in [Unable
to connect to SSM endpoints](#systems-manager-ssm-agent-troubleshooting-endpoint-access "#systems-manager-ssm-agent-troubleshooting-endpoint-access"),
`ec2messages.`region`.amazonaws.com`.

###### Note

The alternative to using a VPC endpoint is to allow outbound internet access
on your managed instances. In this case, the managed instances must also allow
HTTPS (port 443) outbound traffic to the following endpoints:

- `ssm.`region`.amazonaws.com`
- `ssmmessages.`region`.amazonaws.com`
- `ec2messages.`region`.amazonaws.com`
  SSM Agent initiates all connections to the Systems Manager service in the cloud. For this
  reason, you don't need to configure your firewall to allow inbound traffic to
  your instances for Systems Manager.

For more information about calls to these endpoints, see [Reference: ec2messages,
ssmmessages, and other API operations](systems-manager-setting-up-messageAPIs.md "systems-manager-setting-up-messageAPIs.md").

To troubleshoot issues with your VPC endpoints, do the following:

- Ensure that VPC endpoints are included at the VPC level. If the VPC
  endpoint with a specific service name is not found on the VPC, first verify
  that DNS support is enabled at the VPC level. Next, create a new VPC
  endpoint and associate it with one subnet in each Availability Zone.
- Ensure that a private DNS name is enabled at the VPC endpoint level.
  Private DNS names are enabled by default but might have been manually
  disabled at some point.
- Ensure that existing VPC endpoints are associated with the proper subnet.
  In addition, ensure that the VPCE is already associated with a subnet in
  that Availability Zone.

For more information, see the following topics:

- [Access an
  AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
  _AWS PrivateLink Guide_
- [Associate a private DNS name](../../../vpc/latest/privatelink/configure-endpoint-service.md#associate-private-dns-name "../../../vpc/latest/privatelink/configure-endpoint-service.md#associate-private-dns-name") in the
  _AWS PrivateLink Guide_
- [Improve the security of EC2 instances by using VPC
  endpoints for Systems Manager](setup-create-vpc.md "setup-create-vpc.md")

## Verify your VPC DNS-related

attributes

If you are using a virtual private cloud (VPC), as part of verifying your VPC
configuration, ensure that the attributes `enableDnsSupport` and
`enableDnsHostnames` are enabled.

You can enable these attributes using the Amazon EC2 [ModifyVPCAttribute](../../../AWSEC2/latest/APIReference/API_ModifyVpcAttribute.md "../../../AWSEC2/latest/APIReference/API_ModifyVpcAttribute.md") API action or the AWS CLI command [modify-vpc-attribute](../../../cli/latest/reference/ec2/modify-vpc-attribute.md "../../../cli/latest/reference/ec2/modify-vpc-attribute.md").

For information about enabling these attributes in the Amazon VPC Console, see [View and
update DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns-updating.md "../../../vpc/latest/userguide/vpc-dns-updating.md") in the
_Amazon VPC User Guide_.

###### Note

The alternative to using a VPC endpoint is to allow outbound internet access
on your managed instances. In this case, the managed instances must also allow
HTTPS (port 443) outbound traffic to the following endpoints:

- `ssm.`region`.amazonaws.com`
- `ssmmessages.`region`.amazonaws.com`
- `ec2messages.`region`.amazonaws.com`
  SSM Agent initiates all connections to the Systems Manager service in the cloud. For this
  reason, you don't need to configure your firewall to allow inbound traffic to
  your instances for Systems Manager.

For more information about calls to these endpoints, see [Reference: ec2messages,
ssmmessages, and other API operations](systems-manager-setting-up-messageAPIs.md "systems-manager-setting-up-messageAPIs.md").

## Verify ingress rules on endpoint

security groups

Ensure that any VPC endpoints you have configured (`ssm`,
`ssmmessages`, and `ec2messages`) include an ingress rule
on their security groups to allow traffic in on port 443. If necessary, you can
create a new security group in the VPC with an ingress rule to allow traffic on port
443 for the Classless Inter-Domain Routing (CIDR) block for the VPC. After you
create the security group, attach it to each VPC endpoint.

For more information, see the following topics:

- [How
  do I create VPC endpoints so that I can use Systems Manager to manage private EC2
  instances without internet access?](https://repost.aws/knowledge-center/ec2-systems-manager-vpc-endpoints "https://repost.aws/knowledge-center/ec2-systems-manager-vpc-endpoints") on AWS re:Post
- [VPC CIDR blocks](../../../vpc/latest/userguide/vpc-cidr-blocks.md "../../../vpc/latest/userguide/vpc-cidr-blocks.md")
  in the _Amazon VPC User Guide_

## Use `ssm-cli` to troubleshoot managed node

availability

Starting with SSM Agent version 3.1.501.0, you can use `ssm-cli` to determine
whether a managed node meets the primary requirements to be managed by Systems Manager, and to
appear in lists of managed nodes in Fleet Manager. The `ssm-cli` is a standalone command
line tool included in the SSM Agent installation. Preconfigured commands are included
that gather the required information to help you diagnose why an Amazon EC2 instance or
non-EC2 machine that you have confirmed is running isn't included in your lists of
managed nodes in Systems Manager. These commands are run when you specify the
`get-diagnostics` option.

For more information, see [Troubleshooting
managed node availability using ssm-cli](troubleshooting-managed-nodes-using-ssm-cli.md "troubleshooting-managed-nodes-using-ssm-cli.md").
