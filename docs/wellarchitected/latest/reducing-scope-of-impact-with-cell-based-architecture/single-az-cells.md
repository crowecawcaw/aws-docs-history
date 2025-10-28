# Single-AZ cells

Another way to divide your workload into cells is to break the service down to follow
Availability Zone (AZ) boundaries. This approach is suitable for services that expose
Availability Zones directly as a failure unit. Like Amazon EC2, for example, asks to choose an AZ
for their instances, and encourages to build their systems to tolerate the failure of a
single Availability Zone.

![Diagram showing the use of Single-AZ cells](images/single-az-cells.jpg)

_Single-AZ cells_

Advantages of this approach:

- It is possible to accurately detect in which AZ a problem is occurring and take
  mitigation actions for it.
  Disadvantages of this approach:

- Requires three cell routers, and requires clients to chose the correct zonal
  endpoint.
- Require using services that have the AZ scope in its configuration
- It requires additional disaster recovery mechanisms such as active-passive or
  active-active to maintain cell resiliency. Cell state needs to be replicate to another,
  which in turn can break the cell concept.
