# Control plane and data plane

AWS separates most services into the concepts of _control plane_ and
_data plane_. These terms come from the world of networking, specifically
routers. The router's data plane, which is its main function, is moving packets around based
on rules. But the routing policies have to be created and distributed from somewhere, and
that's where the control plane comes in.

Control planes for your cell-based architecture provide the administrative APIs used to
provision, move, migrate, update, remove, deploy, and monitor cells, among others. The data
plane is what provides the primary function of the service together with cell router.

To understand the relationship between the control plane and data plane in a cell-based
architecture, imagine that you have five cells and the number of users starts growing. Your
control plane is responsible for provisioning a new cell and letting the router to know where
traffic needs to be sent to. After that, both the router and the cell will be just performing
the work they're supposed to (data plane).

Another important aspect to consider here is the static stability as recommended in the
Well-Architected Framework, [REL11-BP04 Rely on the data plane and not the control plane during recovery](../framework/rel_withstand_component_failures_avoid_control_plane.md "../framework/rel_withstand_component_failures_avoid_control_plane.md"). In a
statically stable design, the overall system keeps working even when a dependency becomes
impaired. For the cell-based context, it would be the data plane to continue operating even if
the control plane is down, or even if some availability zone is also down.

Control planes are statistically more likely to fail than data planes. Although the data
plane typically depends on data that arrives from the control plane, the data plane maintains
its existing state and continues working even in the face of control plane impairment. Data
plane access to resources, once provisioned, has no dependency on the control plane, and
therefore is not affected by any control plane impairment. In other words, even if the ability
to create, modify, or delete resources is impaired, existing resources remain available. You
can implement different patterns to be statically stable against different types of dependency
failures depending on your cell design strategy.

In addition, we can say that control planes are designed to fail rather than corrupt or
provide incorrect information (CP in the [CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem "https://en.wikipedia.org/wiki/CAP_theorem")), while data planes
generally prefer AP in the [CAP
theorem](https://en.wikipedia.org/wiki/CAP_theorem "https://en.wikipedia.org/wiki/CAP_theorem") (Data planes try their best to remain available, even if they depend on
stale information for decisions.) An example would be [Using a compute layer like Amazon EC2, Amazon ECS or Amazon EKS and Amazon S3 for cell mapping as cell
router](using-a-compute-layer-like-ec2-ecs-or-eks-and-s3-for-cell-mapping-as-cell-router.md "using-a-compute-layer-like-ec2-ecs-or-eks-and-s3-for-cell-mapping-as-cell-router.md")
described later in this paper. Routes to cells are loaded into memory from an S3 bucket. Even
if the control plane, Amazon S3 or a zone is unavailable, the router is still able to direct
traffic to the cells.
