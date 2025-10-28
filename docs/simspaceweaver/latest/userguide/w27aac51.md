End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Glossary

This glossary defines terms that are specific to AWS SimSpace Weaver.

For the latest AWS terminology, see the [AWS glossary](../../../general/latest/gr/glos-chap.md "../../../general/latest/gr/glos-chap.md") in the
_AWS General Reference_.

### A

app
Executable code (also called _binaries_) that you
create. The term _app_ can refer to the code
or a running instance of that code. An app encapsulates
simulation behavior. Apps create, delete, read,
and update [entities](#glossary_entity "#glossary_entity").

app SDK
A software development kit (SDK) that you use to integrate an app with
SimSpace Weaver. The SDK provides APIs for reading and writing
[entity](#glossary_entity "#glossary_entity") data
and tracking simulation time. For more information, see
[SimSpace Weaver app SDK](working-with_app-sdk.md "working-with_app-sdk.md").

### C

client
Processes (or their definitions) that exist outside of SimSpace Weaver and
interact with the simulation through a
[custom app](#glossary_custom-app "#glossary_custom-app") or
[service app](#glossary_service-app "#glossary_service-app").
You can use a client to view or change the
simulation state.

clock
An abstraction of SimSpace Weaver's internal scheduling processes. The
clock publishes [ticks](#glossary_tick "#glossary_tick") to
[apps](#glossary_app "#glossary_app") to maintain time
synchronization. Each simulation has its own clock.

clock rate
The number of [ticks](#glossary_tick "#glossary_tick") per second
that the [clock](#glossary_clock "#glossary_clock") publishes to
[apps](#glossary_app "#glossary_app"). For more information about
supported clock rates, see [SimSpace Weaver endpoints and quotas](service-quotas.md "service-quotas.md").

clock tick rate
See [clock rate](#glossary_clock-rate "#glossary_clock-rate").

compute resource unit
A unit of compute resources (processor and memory) on a
[worker](#glossary_worker "#glossary_worker"). A single
instance of an [app](#glossary_app "#glossary_app") is normally allocated
1 compute resource unit. You can
allocate more than 1 compute resource unit for each app.

custom app
A type of [app](#glossary_app "#glossary_app") that you use to read and
interact with the state of the
simulation. Custom apps can create entities in the simulation but don't own
them. When a custom app creates an entity, it must transfer the
entity to the [spatial domain](#glossary_spatial-domain "#glossary_spatial-domain").
You control the lifecycle of a custom app using the app APIs. For more
information about the SimSpace Weaver APIs, see [SimSpace Weaver API references](api-reference.md "api-reference.md").

custom domain
A [domain](#glossary_domain "#glossary_domain") that contains
[custom apps](#glossary_custom-app "#glossary_custom-app").

custom partition
The [partition](#glossary_partition "#glossary_partition") of a
[custom app](#glossary_custom-app "#glossary_custom-app").

### D

deadline
An [actual time](#glossary_time-actual "#glossary_time-actual") by
which an operation (such as processing for a
[tick](#glossary_tick "#glossary_tick")) should be complete.

domain
A group of [app](#glossary_app "#glossary_app") instances that
run the same executable code (app binary) and
have the same launch options.

### E

endpoint (service)
A fully-qualified domain name (FQDN) that programs (such as the
AWS Command Line Interface) use to connect to the SimSpace Weaver service.

endpoint (simulation)
An IP address and port number that clients use to connect to connect to
a simulation. You can configure endpoints on
[custom apps](#glossary_custom-app "#glossary_custom-app") and
[service apps](#glossary_service-app "#glossary_service-app").

entity
Customer data objects (or their definitions). Entities can be static (remain
in one location) or dynamic (move through the simulation space). For example,
people and buildings in a simulation.

### I

index (simulation)
A description of the spatial properties of a simulation, including its spatial
boundaries and coordinate system.

### L

lifecycle (of an app)
A description of the expected logical steps that an
[app](#glossary_app "#glossary_app") goes through during a
simulation. Lifecycles are either _managed_
(SimSpace Weaver starts and stops the app) or _unmanaged_ (you start and stop the app).

load (entity field data)
Read [entity](#glossary_entity "#glossary_entity") field data
from the [State Fabric](#glossary_state-fabric "#glossary_state-fabric").

### P

partition
A segment of shared memory on a [worker](#glossary_worker "#glossary_worker").
Each partition contains a discrete subset of
[entities](#glossary_entity "#glossary_entity") within a
[domain](#glossary_domain "#glossary_domain"). Each
[app](#glossary_app "#glossary_app") has an assigned partition.
An app owns all of the entities in its partition. When
an app creates an entity, it creates it in its partition.
When entities move from one partition to
another partition, ownership transfers from the source partition's app
to the destination partition's app.

### R

resource unit
See .

### S

schema
A YAML or JSON document that describes the configuration of a simulation.
SimSpace Weaver uses a schema to create a
[simulation resource](#glossary_simulation "#glossary_simulation").

service app
A type of [app](#glossary_app "#glossary_app") that you use to
read and interact with the state of the simulation.
Service apps can create entities in the simulation but must transfer
them to the spatial [domain](#glossary_domain "#glossary_domain").
SimSpace Weaver manages the [lifecycle](#glossary_lifecycle-app "#glossary_lifecycle-app")
of a service app, and starts 1 (or more, as specified in your
simulation [schema](#glossary_schema "#glossary_schema")) on each
[worker](#glossary_worker "#glossary_worker") in your simulation.

service domain
A [domain](#glossary_domain "#glossary_domain") that contains
[service apps](#glossary_service-app "#glossary_service-app").

service partition
The [partition](#glossary_partition "#glossary_partition") of a
[service app](#glossary_service-app "#glossary_service-app").

simulation (resource)
An abstraction of a compute cluster that runs a simulated virtual space. You
can have multiple simulations. You configure a simulation using a
[schema](#glossary_schema "#glossary_schema").

spatial app
A type of [app](#glossary_app "#glossary_app") that encapsulates
the core simulation logic. Each spatial app
owns 1 (and only 1) [partition](#glossary_partition "#glossary_partition").

spatial domain
A [domain](#glossary_domain "#glossary_domain") that contains
[spatial apps](#glossary_spatial-app "#glossary_spatial-app").

spatial partition
The [partition](#glossary_partition "#glossary_partition") of a
[spatial app](#glossary_spatial-app "#glossary_spatial-app").

State Fabric
SimSpace Weaver's in-memory database. The State Fabric stores the state of
simulations, including entities and internal SimSpace Weaver data.

store (entity field data)
Write entity field data to the
[State Fabric](#glossary_state-fabric "#glossary_state-fabric").

subscription
A long-running request for a specific [app](#glossary_app "#glossary_app")
instance to receive data from a
[subscription area](#glossary_subscription-area "#glossary_subscription-area"). The
subscribing app uses a subscription to discover changes to
[entities](#glossary_entity "#glossary_entity") inside the subscription area.

subscription area
A 2-dimensional region of the simulation space. A [subscription](#glossary_subscription "#glossary_subscription") refers to a subscription
area. A subscription area can span more than 1 [partition](#glossary_partition "#glossary_partition"), and also include parts of
partitions. A subscription area is continuous within its defined bounds.

### T

tick
A discrete value for time (either wall-clock time or simulation time).
[Apps](#glossary_app "#glossary_app") can
iterate faster than the tick duration, but are expected to write specified
ticks within specific deadlines. All operations for all apps for a given
tick must complete before the next tick can start.

tick rate
See clock rate.

time (actual)
The current time from the perspective of reality. SimSpace Weaver uses a 64-bit POSIX
timestamp which is the number of nanoseconds since the Unix epoch (January 1,
1970, 00:00:00 UTC).

time (simulation)
The current time from the perspective of the simulation. SimSpace Weaver uses a 64-bit
integer logical tick counter, which might not directly correspond to the actual
time.

### W

worker
An Amazon Elastic Compute Cloud (Amazon EC2) instance that runs simulation
code.
