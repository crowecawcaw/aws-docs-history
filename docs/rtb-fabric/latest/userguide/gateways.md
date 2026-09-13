

# RTB Fabric gateways
<a name="gateways"></a>

RTB Fabric gateways are AWS managed network endpoints that operate colocated with your VPC to facilitate secure communication between RTB applications and RTB Fabric infrastructure. Gateways serve as connection points that route RTB traffic. There are two types of gateways: requester gateways that route outbound bid requests and receive responses, and responder gateways that route inbound bid requests and return responses.

A responder gateway can span more than one Availability Zone. Its client routing policy controls which of those Availability Zones RTB Fabric uses to reach it. You can prefer the requester gateway's own Availability Zone, or use any Availability Zone that the responder gateway spans. For more information about client routing policies, see [Configuring Availability Zone affinity](working-with-responder-gateways.md#configuring-availability-zone-affinity).