# Security best practices for Amazon GameLift Servers

If you're using Amazon GameLift Servers FleetIQ as a standalone feature with Amazon EC2, see [Security in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md") in the
_Amazon EC2 User Guide_.

Amazon GameLift Servers provides a number of security features to consider as you develop and implement
your own security policies. The following best practices are general guidelines and don't
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

## Keep fleet runtime environments up to

date

Amazon GameLift Servers highly recommends that you regularly replace managed fleets (including
managed EC2 and managed container fleets) to maintain secure runtime environments for your
game servers. Fleets that run for extended periods without runtime updates can contain
outdated dependencies and security vulnerabilities that could compromise your game servers.
For details on how responsibility is shared for software deployed to Amazon GameLift Servers fleets, see
[Configuration and vulnerability analysis
in Amazon GameLift Servers](vulnerability-analysis-management.md "vulnerability-analysis-management.md").

A managed fleet's runtime environment is determined by its Amazon Machine Image (AMI)
version. When a new fleet is created, Amazon GameLift Servers assigns the latest available AMI version to
the fleet, and all compute instances in that fleet are deployed with that version. To update
the AMI version, you must create a new fleet. For details on current AMI versions, see [Amazon GameLift Servers AMI versions](reference-ec2-ami-version-history.md "reference-ec2-ami-version-history.md").

Recommended practices:

- **Monitor fleet age and replace fleets that are over 30 days
  old** – You can track a fleet's creation date in the Amazon GameLift Servers console
  or use the CLI to retrieve fleet attributes. Amazon GameLift Servers displays warnings in the console
  for fleets that are over 90 days old, and notifies account holders by email for fleets
  that are older than one year.

###### Note

Updating a fleet (such as using [UpdateFleetAttributes](../apireference/API_UpdateFleetAttributes.md "../apireference/API_UpdateFleetAttributes.md") or [UpdateContainerFleet](../apireference/API_UpdateContainerFleet.md "../apireference/API_UpdateContainerFleet.md")) doesn't change the AMI version. You must create a new
fleet.

- **Replace fleets regularly based on security
  health** – Set up a regular schedule to create new fleets and retire old
  fleets. Consider using a service like
  [Amazon Q](../../../amazonq/latest/qdeveloper-ug/code-reviews.md "../../../amazonq/latest/qdeveloper-ug/code-reviews.md")
  to review your game code with the current AMI version,
  detect security issues, and suggest remediation steps.
- **Test server builds with the latest AMI versions before
  deployment** – You might need to modify your server build and upload it
  to Amazon GameLift Servers before creating a new fleet.
- **Manage fleet quotas for your AWS account** –
  You can request limit increases if needed to create replacement fleets. For more
  information, see [Amazon GameLift Servers endpoints and quotas](limits-regions.md "limits-regions.md").
- **Consider automating fleet
  replacement** – You can automate processes to create new fleets and
  migrate player traffic from older fleets. For example:
  - Use AWS CloudFormation to automate fleet creation and management. Maintain your fleet
    configurations as AWS CloudFormation templates and use them to launch resource stacks.
  - Take advantage of the Amazon GameLift Servers alias feature to abstract specific fleet IDs. Fleet aliases
    make it easy to switch player traffic from an existing fleet to a new one with no disruption to
    game sessions in progress. For details, see [Abstract an Amazon GameLift Servers fleet designation with an alias](aliases-intro.md "aliases-intro.md").
  - Use blue/green deployment strategies to reduce migration risk and maintain zero downtime. With
    two identical production environments, you can take advantage of a full
    production-like testing environment, exert greater control over migration process, and
    ensure instant rollbacks.

## Secure your port configurations

We strongly recommend against opening ports to the Internet because doing so poses a security risk.
For example, the following configuration opens a remote desktop port that allows anyone on the Internet to access the instance:

```
{
  "FleetId": "`<fleet identifier>`",
  "InboundPermissionAuthorizations": [
      {
        "FromPort": 3389,
        "IpRange": "0.0.0.0/0",
        "Protocol": "RDP",
        "ToPort": 3389
      }
  ]
}

```

Instead, use [UpdateFleetPortSettings](../apireference/API_UpdateFleetPortSettings.md "../apireference/API_UpdateFleetPortSettings.md") to open a port with a specific IP address or range of
addresses, as shown in this example:

```
{
  "FleetId": "`<fleet identifier>`",
  "InboundPermissionAuthorizations": [
      {
        "FromPort": 3389,
        "IpRange": "54.186.139.221/32",
        "Protocol": "TCP",
        "ToPort": 3389
      }
  ]
}

```

## Additional security resources

For more information about how you can make your use of Amazon GameLift Servers more secure, see the [AWS Well-Architected Tool Security
pillar.](https://wa.aws.amazon.com/wat.pillar.security.en.html "https://wa.aws.amazon.com/wat.pillar.security.en.html").
