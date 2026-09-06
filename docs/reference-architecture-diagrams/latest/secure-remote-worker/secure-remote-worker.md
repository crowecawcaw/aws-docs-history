

# Secure Remote Worker Environment
<a name="secure-remote-worker"></a>

Publication date: **January 31, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to build a secure desktop environment for remote workers. Workers can access key line-of-business applications and data.

## Secure Remote Worker Environment
<a name="diagram1"></a>

![Architecture diagram showing a secure remote worker environment with Amazon WorkSpaces.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/secure-remote-worker/images/secure-remote-worker.png)


1. Users connect to their desktop by using the [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) application with a username, password, and MFA code.

1. The Amazon WorkSpaces authentication gateway authenticates against [Amazon DynamoDB Streams](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html).

1. The MFA code authenticates against the MFA service's RADIUS server (for example, OneLogin).

1. Users connect to their desktop through Amazon WorkSpaces.

1. Users access core systems and files hosted on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) and [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html).

1. Group policy in Active Directory prevents unwanted activities, such as printing to local printers from Amazon WorkSpaces.

1. Domain Controller DNS forwards to Route 53 VPC DNS resolver with applied Route 53 Resolver DNS Firewall rules.

1. [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) filters outbound internet traffic, then routes it through a NAT gateway and internet gateway to the public internet.

1. Firewall rules block outbound traffic to unwanted sites (such as file-sharing platforms) to prevent data leaks.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon WorkSpaces product page](https://aws.amazon.com/workspaces/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 31, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.