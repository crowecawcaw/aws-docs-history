# Destination containment

Destination containment is the application of filtering or routing within an environment to
prevent access to a targeted host or resource. In some cases, destination containment also
involves a form of resiliency to verify that legitimate resources are replicated for availability;
resources should be detached from these forms of resiliency for isolation and containment.
Examples of destination containment using AWS services include:

- **Network ACLs** – Network ACLs (network ACLs) that are
  configured on subnets that contain AWS resources can have deny rules added. These deny
  rules can be applied to prevent access to a particular AWS resource; however, applying
  network access control list (network ACL) will affect every resource on the subnet, not only the resources that are being
  accessed without authorization. Rules listed within an network ACL are processed in top-down
  order, so the first rule in an existing network ACL should be configured to deny unauthorized
  traffic to the targeted resource and subnet. Alternatively, a completely new network ACL can be
  created with a single deny rule for both inbound and outbound traffic and associated
  with the subnet containing the targeted resource to prevent access to the subnet using
  the new network ACL.
- **Shutdown** – Shutting down a resource completely can
  be effective at containing the effects of unauthorized use. Shutting down a resource
  will also prevent legitimate access for business needs and prevent volatile forensic
  data from being obtained, so this should be a purposeful decision and should be judged
  against an organization’s security policies.
- **Isolation VPCs** – Isolation VPCs can be used to
  provide effective containment of resources while providing access to legitimate traffic
  (such as anti-virus (AV) or EDR solutions that require access to the internet or an
  external management console). Isolation VPCs can be preconfigured in advance of a
  security event to permit valid IP addresses and ports, and targeted resources can
  immediately be moved into this isolation VPC during an active security event to contain
  the resource while allowing legitimate traffic to be sent and received by the targeted
  resource during subsequent phases of incident response. An important aspect of using an
  isolation VPC is that resources, such as EC2 instances, need to be shut down and
  relaunched in the new isolation VPC prior to use. Existing EC2 instances cannot be moved
  to another VPC or another Availability Zone. To do so, follow the steps outlined in
  [How do I move my Amazon EC2 instance to another subnet, Availability Zone, or VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/move-ec2-instance/ "https://aws.amazon.com/premiumsupport/knowledge-center/move-ec2-instance/")
- **Auto Scaling groups and load balancers** – AWS
  resources attached to Auto Scaling groups and load balancers should be detached and
  deregistered as part of destination containment procedures. Detachment and
  deregistration of AWS resources can be performed using the AWS Management Console, AWS CLI, and AWS SDK.

An example of destination containment is demonstrated in the following diagram with an
incident response analyst adding an network ACL to a subnet in order to block a network
connection request from an unauthorized host.

![Diagram showing an example of destination containment](images/destination-containment.png)
_Destination containment example_
