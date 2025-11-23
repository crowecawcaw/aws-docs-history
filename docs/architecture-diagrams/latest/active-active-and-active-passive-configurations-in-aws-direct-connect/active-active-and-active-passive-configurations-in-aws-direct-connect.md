# Active/Active and Active/Passive Configurations in AWS Direct Connect

Publication date: **September 21, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

**Service Level Agreement (SLA)**

Amazon Web Services offers customers the ability to achieve highly-resilient network connections
between Amazon Virtual Private Cloud (Amazon VPC) and their on-premises infrastructure. The
[AWS Direct Connect Resiliency Toolkit](../../../directconnect/latest/UserGuide/resiliency_toolkit.md "../../../directconnect/latest/UserGuide/resiliency_toolkit.md")
provides a connection wizard with multiple resiliency models. These models help you
to determine and then place an order for the number of dedicated connections
to achieve your SLA objective.

This reference architecture focuses on the Maximum Resiliency model, which
provides you with a way to order dedicated connections to achieve an SLA
of 99.99%. You can find the requirements in the
[Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/ "https://aws.amazon.com/directconnect/sla/").

**Link aggregation groups (LAGs) and Equal Cost Multi Path (ECMP)**

For Active/Active mode, you can leverage [LAGs](../../../directconnect/latest/UserGuide/lags.md "../../../directconnect/latest/UserGuide/lags.md") for dedicated Direct Connect connections,
terminating on the same Direct Connect endpoint. This will load balance traffic
across all connections in the LAG on layer 2. This will not protect
against failure on the Direct Connect endpoint or the whole Direct Connect location.

With ECMP, you can load balance traffic across multiple connections and
Direct Connect locations on layer 3. You can influence path behaviour by
longest prefix match and Border Gateway Protocol (BGP) attributes.
This allows for setting up Active/Active or Active/Passive configurations.

## Active/Active with Private/Transit VIF Diagram

Build Active/Active configuration with Transit/Private Virtual Interface
(VIF) for max resiliency. Have redundant Direct Connect connections inside
each Direct Connect location as well as across locations, customer data
centers, and devices. This configuration offers customers max resilience
to failure. Such a topology ensures resilience to connectivity failure
due to a fiber cut or a device failure as well as a complete
location failure.

- **Transit/Private VIF**: You can create
  Active/Active by ensuring advertised prefixes, local preference,
  autonomous system (AS) path, and Multi-Exit Discriminator (MED)
  values are the same. With that you influence incoming traffic
  from AWS. These options are not mutually exclusive and can be
  used together.
- **Active/Active**: Traffic is
  load-shared between interfaces based on flow via ECMP. If
  one connection becomes unavailable, then all traffic is routed
  through the other connections.

![Diagram showing the active/active with private/transit VIF model.](images/1-active-active-with-private-transit-vif.png)

1. **AWS Direct Connect** gateway is a global
   construct and AWS takes care of its availability.
2. When you request multiple ports at the same **Direct Connect**
   location, they will be provisioned on redundant AWS equipment.
3. **Direct Connect** supports multipathing to multiple
   virtual interfaces within the same location, and traffic is load-shared
   between interfaces based on flow. If one connection becomes unavailable,
   all traffic is routed through the other connection.
4. Have the redundant **Direct Connect** connections
   terminate on different customer/partner routers inside the **Direct Connect**
   location.
5. **Direct Connect** connections have to be brought
   down for regular scheduled maintenance. Therefore, use multiple connections.
6. Have the redundant **Direct Connect** connections
   terminate on different routers inside your data center.
7. Use multiple **Direct Connect** connections
   across multiple **Direct Connect** locations.
8. Use multiple **Direct Connect** connections
   across multiple customer sites.
9. Advertise the same prefixes across all **Direct Connect**
   connections for Active/Active setup.
10. If prefixes are the same, a higher local preference is preferred. By
    using BGP communities you can set the local preference from
    7224:7100/7200/7300 where 7100 is low, 7200 is medium, and 7300 is
    high preference. Use the same local preference across all
    **Direct Connect** connections for an
    Active/Active setup.
11. If local preference is the same, shortest AS paths are preferred
    across **Direct Connect** connections
    associated with the same AWS Region. Use the same AS path
    length across all **Direct Connect** connections
    for an Active/Active setup.
12. If AS path lengths are the same, a lower MED value will be
    preferred. For an Active/Active setup, use the same MED
    value for all **Direct Connect** connections.
13. You can create LAGs for dedicated connections terminating
    at the same **Direct Connect**
    endpoint. All connections in a LAG operate in Active/Active mode.

## Active/Passive with Private/Transit VIF Diagram

Build Active/Passive configuration with Transit/Private VIF for max
resiliency. Have redundant Direct Connect connections inside each
Direct Connect location as well as across locations, customer
data centers and devices. This configuration offers customers
max resilience to failure. Such a topology ensures resilience
to connectivity failure due to a fiber cut or a device
failure as well as a complete location failure.

- **Transit/Private VIF**: You can
  create Active/Passive setups in multiple ways by controlling
  advertised prefixes, local preference, AS path and MED value.
  With that you influence incoming traffic from AWS. These options
  are not mutually exclusive and can be used together.
- **Active/Passive**: One connection
  handles traffic, and the others are on standby. If the active
  connection becomes unavailable, then all traffic is routed
  through the passive connections.

![Diagram showing the active/passive with private/transit VIF model.](images/2-active-passive-with-private-transit-vif.png)

1. **Direct Connect** gateway is a global construct
   and AWS takes care of its availability.
2. When you request multiple ports at the same **Direct Connect**
   location, they will be provisioned on redundant AWS equipment.
3. Have the redundant **Direct Connect** connections
   terminate on different customer/partner routers inside the
   **Direct Connect** location.
4. **Direct Connect** connections have to be
   brought down for regular scheduled maintenance. Therefore, use
   multiple connections.
5. Have the redundant **Direct Connect** connections
   terminate on different routers inside your data center.
6. Leverage multiple **Direct Connect** connections
   across multiple **Direct Connect** locations.
7. Leverage multiple **Direct Connect** connections
   across multiple customer sites.
8. By advertising more specific prefixes you can prefer
   one **Direct Connect** connection over the others.
9. If prefixes are the same, a higher local preference is preferred.
   By using BGP communities you can set a local preference
   from 7224:7100/7200/7300 where 7100 is low, 7200 is medium,
   and 7300 is high preference. Use a higher local preference to
   prefer a specific **Direct Connect**
   connection over others.
10. If local preference is the same, shortest AS paths are
    preferred. You can use AS path prepending for
    **Direct Connect** connections
    associated with the same AWS Region. AWS will prefer
    the shorter AS path for multiple virtual interfaces in a
    Region.
11. Use a lower MED value to prefer a specific
    **Direct Connect** connection.

## Active/Active with Public VIF Diagram

Build Active/Active configuration with Public VIF for max resiliency. Have
redundant Direct Connect connections inside each Direct Connect location as well as
across locations, customer data centers, and devices. This configuration
offers customers max resilience to failure. Such a topology ensures resilience
to connectivity failure due to a fiber cut or a device failure as well
as a complete location failure.

- **Public VIF**: You can create
  Active/Active with a public Autonomous System Number (ASN) by
  ensuring advertised prefixes, Local Preference and AS path
  values are the same. These options are not mutually exclusive
  and can be used together.
- **Active/Active**: Traffic is
  load-shared between interfaces based on flow via ECMP. If one
  connection becomes unavailable, then all traffic is routed
  through the other connection(s).

If you're using a private ASN, load balancing on a public virtual interface is not supported.

![Diagram showing the active/active with public VIF model.](images/3-active-active-with-public-vif.png)

1. When you request multiple ports at the same
   **Direct Connect** location,
   they will be provisioned on redundant AWS equipment.
2. **Direct Connect** supports multipathing
   to multiple virtual interfaces within the same location, and traffic
   is load-shared between interfaces based on flow. If one
   connection becomes unavailable, all traffic is routed through
   the other connection.
3. Have the redundant **Direct Connect** connections
   terminate on different customer/partner routers inside the
   **Direct Connect** location.
4. **Direct Connect** connections have to be
   brought down for regular scheduled maintenance. Therefore, use
   multiple connections.
5. Have the redundant **Direct Connect** connections
   terminate on different routers inside your data center.
6. Leverage multiple **Direct Connect**
   connections across multiple **Direct Connect** locations.
7. Leverage multiple **Direct Connect** connections
   across multiple customer sites.
8. Advertise the same prefixes across all **Direct Connect**
   connections for Active/Active setup.
9. If prefixes are the same, shortest AS paths are preferred. Use
   the same AS path length across all **Direct Connect**
   connections for an Active/Active setup.

## Active/Passive with Public VIF Diagram

Build Active/Passive configuration with Public VIF for max resiliency.
Have redundant Direct Connect connections inside each Direct Connect location as well
as across locations, customer data centers and devices. This configuration
offers customers max resilience to failure. Such a topology ensures
resilience to connectivity failure due to a fiber cut or a device failure
as well as a complete location failure.

- **Public VIF**: You can create
  Active/Passive with a _public_ ASN by controlling advertised
  prefixes and AS path. You can create Active/Passive with a
  _private_ ASN by controlling advertised prefixes.
- **Active/Passive**: One connection
  handles traffic, and the others are on standby. If the active
  connection becomes unavailable, then all traffic is routed
  through the passive connections.

![Diagram showing the active/passive with public VIF model.](images/4-active-passive-with-public-vif.png)

1. When you request multiple ports at the same **Direct Connect**
   location, they will be provisioned on redundant AWS equipment.
2. Have the redundant **Direct Connect** connections
   terminate on different customer/partner routers inside the
   **Direct Connect** location.
3. **Direct Connect** connections have to be brought
   down for regular scheduled maintenance. Therefore, use multiple connections.
4. Have the redundant **Direct Connect** connections
   terminate on different routers inside your data center.
5. Leverage multiple **Direct Connect** connections
   across multiple **Direct Connect** locations.
6. Leverage multiple **Direct Connect** connections
   across multiple customer sites.
7. By advertising more specific prefixes, you can prefer one
   **Direct Connect** connection over the others.
8. For public ASNs, if prefixes are the same, shortest AS paths are preferred.
   Use shorter AS path length to prefer a specific **Direct Connect**
   connection over the others.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/active-active-and-active-passive-configurations-in-aws-direct-connect.md "samples/active-active-and-active-passive-configurations-in-aws-direct-connect.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Contributors

Contributors to this reference architecture diagram include:

- Michael Graumann, Senior Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date               |
| ------------------- | ----------------------------------------------- | ------------------ |
| Update              | Reference architecture diagram updated          | September 21, 2023 |
| Initial publication | Reference architecture diagram first published. | July 18, 2022      |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
