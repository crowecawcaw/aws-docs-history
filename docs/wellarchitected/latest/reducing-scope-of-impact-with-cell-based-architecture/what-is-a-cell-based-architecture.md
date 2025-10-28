# What is a cell-based architecture?

A cell-based architecture comes from the concept of a [bulkhead in a ship](https://en.wikipedia.org/wiki/Bulkhead_%28partition%29 "https://en.wikipedia.org/wiki/Bulkhead_%28partition%29"), where
vertical partition walls subdivide the ship's interior into self-contained, watertight compartments. Bulkheads
reduce the extent of seawater flooding in case of damage and provide additional stiffness to the
hull girder.

![Diagram of a ship showing how a bulkhead isolates a failure.](images/failure-isolation-using-bulkheads.jpg)
_Isolating failures using bulkheads_

On a ship, bulkheads ensure that a hull breach is contained within one section of the
ship. In complex systems, this pattern is often replicated to allow fault isolation.
_Fault isolated boundaries_ restrict the effect of a failure within a
workload to a limited number of components. Components outside of the boundary are unaffected by
the failure.

Using multiple fault isolated boundaries, you can limit the impact on your workload. When
provisioning a new customer or tenant, or applying a workload change, you can do this gradually,
compartment by compartment, or in other words, isolation boundary by isolation boundary. This
way, when a failure occurs, a smaller number of customers or resources will be impacted. On
AWS, customers can use multiple Availability Zones and AWS Regions to provide fault
isolation, but the concept of fault isolation can be extended to your workload's architecture as
well.

The overall workload is partitioned by a partition key. This key
needs to align with the _grain_ of the service,
or the natural way that a service's workload can be subdivided
with minimal cross-cell interactions. Examples of partition keys
are customer ID, resource ID, or any other parameter easily
accessible in most API calls. A cell routing layer distributes
requests to individual cells based on the partition key and
presents a single endpoint to clients.

A cell-based architecture uses multiple isolated instances of a workload, where each
instance is known as a _cell_. Each cell is independent, does not share state
with other cells, and handles a subset of the overall workload requests. This reduces the
potential impact of a failure, such as a bad software update, to an individual cell and the
requests that it's processing. If a workload uses 10 cells to service 100 requests, when a
failure occurs in one cell, 90% of the overall requests would be unaffected by the failure.

With cell-based architectures, many common types of failure are
contained within the cell itself, providing additional fault
isolation. These fault boundaries can provide resilience against
failure types that otherwise are hard to contain, such as
unsuccessful code deployments or requests that are corrupted or
invoke a specific failure mode (also known as _poison
pill requests_).

## A typical workload

To make it clearer, in the following diagram, we have a typical application divided
into three layers. In this context, this application would be serving requests from 100% of
clients. In the event of a failure, or a change in the application, 100% of customers would be
impacted.

![A reference architecture diagram showing a typical workload.](images/typical-workload.jpg)

_A typical workload_

## A workload with cell-based architecture

Rather than build out services as single-image systems, we propose a different
approach: break your services down internally into cells and build thin layers to route
traffic to the right cells. This type of architecture can be zonal, regional, or global.

![Reference architecture diagram showing a cell-based architecture.](images/cell-based-architecture.jpg)

_A cell-based architecture_

The cell-based architecture has the following components, which will be further
explored later in this guidance:

- **Cell router** — We also refer to this layer as the
  _thinnest possible layer_, with the responsibility of routing
  requests to the right cell, and only that.
- **Cell** — A complete workload, with everything needed to
  operate independently.
- **Control plane** — Responsible for administration tasks,
  such as provisioning cells, de-provisioning cells, and migrating cell customers.

Building a cell-based architecture doesn't necessarily mean having to double, triple,
or more your application's infrastructure. It might be that your application has 30 hosts, and
in a cell-based architecture it has the same 30 hosts, but with a cell router and with tasks
that are distributed or grouped between cells.
