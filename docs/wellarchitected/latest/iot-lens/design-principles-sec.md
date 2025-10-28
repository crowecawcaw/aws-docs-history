# Design principles

In addition to the overall Well-Architected Framework security
design principles, there are specific design principles for IoT
security:

- **Manage device security lifecycle
  holistically**: Device security starts at the design
  phase, and ends with the retirement, re-purposing, and
  destruction of the hardware and data. It is important to take
  an end-to-end approach to the security lifecycle of your IoT
  solution in order to maintain your competitive advantage and
  retain customer trust.
- **Verify least privilege
  permissions**: Devices should all have fine-grained
  access permissions. For example, while using MQTT
  communications, use device instance specific MQTT topics and
  access permissions which limit which MQTT topics a device can
  use for communication. By restricting access, a compromised
  device will less chance of affecting other devices. This
  reduces the risk of your application. There can be a trade-off
  when a large numbers of devices are in use. In such cases,
  select MQTT topic spaces and access permissions to limit the
  the scope of affected devices if a device is compromised.
- **Secure device credentials at
  rest**: Devices should securely store credential
  information at rest using mechanisms such as a dedicated
  secure cryptographic element built into the device or secure
  flash.
- **Implement device identity lifecycle
  management**: Devices maintain a device identity from
  creation through end of life (retirement or destruction). A
  well-designed identity system will keep track of a device's
  identity, track the validity of the identity, and proactively
  adjust or revoke IoT permissions over time. Device identity
  lifecycle management will enable re-purposing or
  re-commissioning devices, either within the same
  application or account or in a separate, un-related
  application or account.
- **Take a holistic view of data
  security**: IoT deployments involving a large number
  of remotely deployed devices extend the risks of unintended
  data exposure as well as data privacy. Use a model such as the
  [Open
  Trusted Technology Provider Standard](https://en.wikipedia.org/wiki/Open_Trusted_Technology_Provider_Standard "https://en.wikipedia.org/wiki/Open_Trusted_Technology_Provider_Standard") to systemically
  review your supply chain and solution design for risk and then
  apply appropriate mitigations.
- **Preserve safety and reliability when
  used in critical OT/IIoT environments**: IIoT
  cybersecurity differs from the IT cybersecurity model because
  it is not only concerned with data protection, but also with
  the preservation of safety and reliability of production
  systems and the environment. When devices are used in OT/IIOT
  environments it is also necessary to adhere to environmental
  health and safety (EHS) requirements.
- **Implement Zero Trust Principles (ZTP)
  following NIST SP 800-207**: Zero trust is not
  limited to traditional IT. Zero Trust Principles extend to the
  internet of things (IoT, operational technology (OT), and
  industrial IoT (IIoT). A zero-trust model can significantly
  improve an organization's security posture by alleviating the
  sole reliance on network or perimeter-based protection. This
  does not mean getting rid of network or perimeter security
  altogether. Where possible, use identity and network
  capabilities together to protect core assets and apply zero
  trust principles working backwards from specific use cases
  with a focus on extracting business value and achieving
  measurable business outcomes.
- **Establish secure connection with AWS
  through Site-to-Site VPN or AWS Direct Connect from the
  industrial edge:** For IIoT workloads, AWS offers
  multiple ways (For more information see
  [Network-to-Amazon VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md")) and design patterns to
  establish a secure connection to the AWS environment from the
  industrial edge. Establish a secure VPN connection to AWS over
  the public internet or set up a dedicated private connection
  via AWS Direct Connect. Use
  [AWS VPN with Direct Connect](https://aws.amazon.com/premiumsupport/knowledge-center/create-vpn-direct-connect/ "https://aws.amazon.com/premiumsupport/knowledge-center/create-vpn-direct-connect/") to encrypt traffic over Direct
  Connect.
- **Use VPC Endpoints whenever
  possible:** For IIoT workloads, once a secure
  connection to AWS has been established via VPN over public
  Internet or AWS Direct Connect, use
  [VPC
  Endpoints](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") whenever possible. VPC Endpoints enable
  customers to privately connect to supported regional AWS
  services without requiring or using the public IP address of
  those AWS service endpoints. Endpoints also support endpoint
  policies. Endpoint policies can be used to further limit
  access to AWS services through the network configuration for
  the solution.
- **Use secured and encrypted connections
  to AWS services over public internet paths:** Use
  HTTPS and MQTTS for devices to communicate with AWS services.
  If a VPC Endpoint for the required service is not available,
  establish a secure connection over the public Internet. If
  TLS-protected communications are not supported by the device
  itself, it is a best practice to route un-protected
  communications through a TLS proxy and a firewall. Using a
  proxy allows the cloud traffic to be inspected and monitored
  enabling threat and malware detection. This also allows the
  security policies to be applied at the network layer. Firewall
  rules can be established for HTTPS and MQTT traffic to
  securely connect to AWS IoT services over the public internet.
  **Note:** AWS IoT Core requires
  secure communications to API and Data endpoints. For more
  information, see
  [Device
  communication protocols](../../../iot/latest/developerguide/protocols.md "../../../iot/latest/developerguide/protocols.md").
- **Use secure protocols:** In
  most environments, prefer to use secure protocols which
  support end-to-end encryption. When using secure protocols is
  not an option, tighten the trust boundaries as described in
  the next point. For example, secure protocols such as HTTP
  over TLS (HTTPS) and MQTT over TLS using
  mutually-authenticated TLS (mTLS).
- **Use network segmentation and tighten
  trust boundaries:** Follow a micro segmentation
  approach. Build small islands of components within a single
  network that communicate only with each other and control the
  network traffic between segments. Select the newer version of
  industrial protocols which offer security features and
  configure the highest level of encryption available when using
  industrial control system (ICS) protocols such as CIP
  Security, Modbus Secure and OPC UA. When using secure
  industrial protocols is not an option, tighten the trust
  boundary using a protocol converter to translate the insecure
  protocol to a secure protocol as close to the data source as
  possible.
  - Alternatively, separate the plant network into smaller
    cell or area zones by grouping ICS devices into functional
    areas. This separation enables the limiting of scope and
    area of insecure communications. Consider using
    unidirectional gateways and data diodes for one-way data
    flow where appropriate. Consider using specialized
    firewall and inspection products that understand ICS
    protocols to inspect traffic entering and leaving cell or
    area zones and can detect anomalous behavior in the
    control network.

- **Securely manage and access edge
  computing resources:** Keeping computing resources at
  the industrial edge up to-date, securely accessing to them for
  configuration and management, and automatically deploying
  changes can be challenging. AWS provides options to securely
  manage edge compute resources
  ([AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md")), IoT resources

([IoT
Device management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/"),

[AWS IoT Greengrass](../../../greengrass/v2/developerguide/what-is-iot-greengrass.md "../../../greengrass/v2/developerguide/what-is-iot-greengrass.md")) and also provides fully managed
infrastructure services

([AWS Outposts](../../../outposts/latest/userguide/what-is-outposts.md "../../../outposts/latest/userguide/what-is-outposts.md"),

[Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/ "https://anywhere.eks.amazonaws.com/"), AWS Snowball) to make it straightforward to
consistently apply best practices to all resources.

- **Shared Responsibility
  Model:** Be aware of and follow the guidance provided
  in the
  [Shared
  Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"). Understand your responsibilities
  for the security of resources and data in the cloud as well as
  AWS's responsibility for security of the cloud. The shared
  responsibility model also extends into environments where
  devices are deployed. In the environments where devices are
  deployed, often called IoT edge locations, your
  responsibilities are much broader than the cloud environment.
  Security of edge environments is your responsibility and
  includes securing the edge network, edge network perimeter,
  devices in the edge network, securely connecting to the cloud,
  handling software updates of edge equipment and devices, and
  edge network logging, monitoring, and auditing, as examples.
  AWS is responsible for the AWS provided edge software such as
  AWS IoT Greengrass and AWS IoT SiteWise Edge and AWS edge
  infrastructure such as AWS Outposts and AWS Snowball.
