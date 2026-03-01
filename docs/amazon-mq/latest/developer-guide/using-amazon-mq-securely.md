# Security best practices for Amazon MQ

The following design patterns can improve the security of your Amazon MQ broker.

###### Topics

- [Prefer brokers without public accessibility](#prefer-brokers-without-public-accessibility "#prefer-brokers-without-public-accessibility")
- [Always configure an authorization map](#always-configure-authorization-map "#always-configure-authorization-map")
- [Block unnecessary protocols with VPC security groups](#amazon-mq-vpc-security-groups "#amazon-mq-vpc-security-groups")

For more information about how Amazon MQ encrypts your data, as well as a list of supported protocols, see
[Data Protection](data-protection.md "data-protection.md").

## Prefer brokers without public accessibility

Brokers created without public accessibility can't be accessed from outside of
your [VPC](../../../vpc/latest/userguide/VPC_Introduction.md "../../../vpc/latest/userguide/VPC_Introduction.md"). This greatly
reduces your broker's susceptibility to Distributed Denial of Service (DDoS) attacks
from the public internet. For more information, see [How to Help Prepare for DDoS Attacks by Reducing Your Attack Surface](https://aws.amazon.com/blogs/security/how-to-help-prepare-for-ddos-attacks-by-reducing-your-attack-surface/ "https://aws.amazon.com/blogs/security/how-to-help-prepare-for-ddos-attacks-by-reducing-your-attack-surface/") on
the AWS Security Blog.

## Always configure an authorization map

Because ActiveMQ has no authorization map configured by default, any authenticated
user can perform any action on the broker. Thus, it is a best practice to restrict
permissions _by group_. For more information, see `authorizationEntry`.

###### Important

If you specify an authorization map which doesn't include the
`activemq-webconsole` group, you can't use the ActiveMQ Web Console because the group isn't authorized to send
messages to, or receive messages from, the Amazon MQ broker.

## Block unnecessary protocols with VPC security groups

To improve security for private brokers, you should restrict the connections of unnecessary protocols
and ports by properly configuring your Amazon VPC Security Group. For instance, to
restrict access to most protocols while allowing access to OpenWire and the
web console, you could allow access to only 61617 and 8162. This limits your
exposure by blocking protocols you are not using, while allowing OpenWire and the
web console to function normally.

Allow only the protocol ports that you are using.

- AMQP: 5671
- MQTT: 8883
- OpenWire: 61617
- STOMP: 61614
- WebSocket: 61619

For more information see:

- [Security Groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
- [Default Security Group for Your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup "../../../vpc/latest/userguide/VPC_SecurityGroups.md#DefaultSecurityGroup")
- [Working with Security Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups")
