# Cell design

A cell is an instance of your complete workload, with everything needed to operate
independently. As an example, consider an application that is comprised by an Application Load Balancer, some EC2
instances, and an Amazon RDS database. In this case, all components are in your cell, for example,
`cell 1`. If you need another cell, `cell 2`, you will have to create
another deployment of these three components.

How you define your cell boundaries has a profound impact on the resiliency, cost, and
architecture of your workload. We are going to describe some ways to define your cell strategy
with its pros and cons.

In an ideal world, a cell is independent, is unaware of other cells, and does not share
its state with other cells. Cells should have no dependency on each other at all (that is, no
cross-cell API calls, no shared resources like databases or S3 buckets.) Even the use of
separate AWS accounts is encouraged. However, depending on your workload, it is not always
possible to maintain these characteristics. Cross-cell dependencies can quickly eliminate the
benefits of a cellular architecture, so try to do this as little as possible, or only at
specific transitory times.
