End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Key concepts for SimSpace Weaver

A simulation or game is limited by the computer that runs it. As you grow the size and
complexity of your virtual world, processing performance begins to degrade. Calculations
take longer, systems run out of memory, and client frame rates drop. For simulations that
don't need real-time performance, this might only be annoying. Or, it could be a
business-critical situation in which increased processing delays result in increased costs.
If your simulation or game needs real-time performance, then performance degradation is
definitely a problem.

A common solution for a simulation that reaches a performance limit is to simplify the
simulation. Online games with many users often address scaling problems by making copies of
their virtual world on different servers and spreading users across them.

SimSpace Weaver solves the scaling problem by dividing your virtual world spatially and
distributing the pieces across a cluster of compute instances that run in the AWS Cloud.
The compute instances work together to process the entire simulation world in parallel. Your
simulation world appears as a single integrated space to everything in it, and to all
clients that connect to it. You no longer have to simplify a simulation because of a
hardware performance limit. You can instead add more compute capacity in the cloud.

###### Topics

- [How SimSpace Weaver works](#what-is_key-concepts_how-it-works "#what-is_key-concepts_how-it-works")
- [How you use SimSpace Weaver](#what-is_key-concepts_how-you-use-it "#what-is_key-concepts_how-you-use-it")
- [Simulation schema](#what-is_key-concepts_schema "#what-is_key-concepts_schema")
- [Workers and resource units](#what-is_key-concepts_workers-and-resource-units "#what-is_key-concepts_workers-and-resource-units")
- [Simulation clock](#what-is_key-concepts_clock "#what-is_key-concepts_clock")
- [Partitions](#what-is_key-concepts_partitions "#what-is_key-concepts_partitions")
- [State Fabric](#what-is_key-concepts_state-fabric "#what-is_key-concepts_state-fabric")
- [Entities](#what-is_key-concepts_entities "#what-is_key-concepts_entities")
- [Apps](#what-is_key-concepts_apps "#what-is_key-concepts_apps")

## How SimSpace Weaver works

Your simulation consists of a world with objects in it. Some of the objects (such as
people and vehicles) move and do things. Other objects (such as trees and buildings) are
static. In SimSpace Weaver, an _entity_ is an object in your
simulation world.

You define the boundaries of your simulation world and divide it into a grid. Instead
of creating simulation logic that operates on the entire grid, you create simulation
logic that operates on one cell of the grid. In SimSpace Weaver, a _spatial app_ is a program that you write that implements the simulation
logic for a cell of your grid. This includes the logic for all entities in that cell. A
spatial app's _ownership area_ is the grid cell that
the spatial app controls.

###### Note

In SimSpace Weaver, the term "app" can refer to the code of an app or a running
instance of that code.

|                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The map of the simulation world divided into a 2-dimensional grid<br>Your simulation world divided into a grid<br>You divide your simulation world into a grid. Each spatial app implements<br>simulation logic for a single cell in that grid. |

SimSpace Weaver runs an instance of your spatial app code for each cell of your grid. All
of the spatial app instances run in parallel. Essentially, SimSpace Weaver divides your
overall simulation into multiple smaller simulations. Each of the smaller simulations
handles a part of the overall simulation world. SimSpace Weaver can distribute and run these
smaller simulations across multiple Amazon Elastic Compute Cloud (Amazon EC2) instances (called _workers_) in the AWS Cloud. A single worker can run
multiple spatial apps.

Entities can move through the simulation world. If an entity enters another spatial
app's ownership area (another cell in the grid), then the spatial app owner of the new
area takes over control of the entity. If your simulation runs on multiple workers, then
an entity could move from the control of a spatial app on one worker to a spatial app on
a different worker. When an entity moves to a different worker, SimSpace Weaver handles the
underlying network communication.

### Subscriptions

A spatial app's view of the world is its own ownership area. To find out what's
happening in another part of the simulation world, the spatial app creates a
_subscription_. The _subscription area_ is a subset of the overall simulation world area.
A subscription area can include parts of multiple ownership areas, including the
spatial app's own ownership area. SimSpace Weaver notifies the spatial app of all entity
events (for example, enter, exit, create, update, and delete) that occur within the
subscription area.

|                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The world grid with only one observable cell<br>A spatial app's view of the world<br>A spatial app's view of the world is its ownership<br>area, which is one cell in the world grid. | The world grid with one observable cell and an additional observable area that spans another cell and parts of surrounding cells<br>A spatial app's view with an added subscription<br>area<br>A spatial app uses a subscription to find out<br>what's happening in another part of the simulation<br>world. The subscription area can contain multiple<br>grid cells and parts of cells. |

For example, an app that simulates entities interacting physically might need to
know about entities just beyond the spatial boundaries of its ownership area. To
accomplish this, the app can subscribe to areas that border its ownership area.
After creating the subscription, the app receives notifications about entity events
in those areas and it can read the entities. Another example is an autonomous
vehicle that needs to see all entities 200 meters in front of it regardless of what
app owns the area. The app for the vehicle can create a subscription with a filter
as an axis-aligned bounding box (AABB) that covers the viewable area.

You can create simulation logic that isn't responsible for managing spatial
aspects of your simulation. A _custom app_ is an
executable program that runs on a single worker. You control the lifecycle (start
and stop) of a custom app. Simulation clients can connect to a custom app to view or
interact with the simulation. You can also create a _service
app_ that runs on every worker. SimSpace Weaver starts an instance of your
service app on every worker that runs your simulation.

Custom apps and service apps create subscriptions to learn about entity events and
read entities. These apps don't have ownership areas because they aren't spatial.
Using a subscription is the only way that they can find out what is happening in the
simulation world.

## How you use SimSpace Weaver

When you use SimSpace Weaver, these are the major steps that you follow:

1. Write and build C++ apps that integrate the SimSpace Weaver app SDK.
   1. Your apps make API calls to interact with the simulation state.

2. Write clients that view and interact with your simulation through some apps.
3. Configure your simulation in a text file.
4. Upload your app packages and simulation configuration to the service.
5. Start your simulation.
6. Start and stop your custom apps as needed.
7. Connect clients to your custom or service apps to view or interact with the simulation.
8. Check your simulation logs in Amazon CloudWatch Logs.
9. Stop your simulation.
10. Clean up your simulation.

## Simulation schema

The _simulation schema_ (or _schema_) is a YAML-formatted text file that contains configuration
information for your simulation. SimSpace Weaver uses your schema when it starts a
simulation. The SimSpace Weaver app SDK distributable package includes a schema for a sample
project. You can use this as a starting point for your own schema. For more information
about the simulation schema, see [SimSpace Weaver simulation schema reference](schema-reference.md "schema-reference.md").

## Workers and resource units

A _worker_ is an Amazon EC2 instance that runs your
simulation. You specify a worker type in your simulation schema. SimSpace Weaver maps your
worker type to a specific Amazon EC2 instance type that the service uses. SimSpace Weaver starts
and stops your workers for you, and manages network communication between the workers.
SimSpace Weaver starts a set of workers for each simulation. Different simulations use
different workers.

The available compute (processor and memory) capacity on a worker is divided into
logical units called _compute resource units_ (or
_resource units_). A resource unit represents a
fixed amount of processor and memory capacity.

###### Note

We previously referred to a compute resource unit as a _slot_. You might still see this previous term in our
documentation.

## Simulation clock

Each simulation has its own clock. You start and stop the clock using API calls or the
SimSpace Weaver console. The simulation updates only when the clock is running. All
operations in the simulation occur within time segments called _ticks_. The clock announces the start time of each tick to all
workers.

The _clock rate_ (or _tick
rate_) is the number of ticks per second (hertz, or Hz) that the clock
announces. The desired clock rate for a simulation is part of the simulation schema. All
operations for a tick must complete before the next tick starts. For this reason, the
effective clock rate can be lower than the desired clock rate. The effective clock rate
won't be higher than the desired clock rate.

## Partitions

A _partition_ is a segment of the shared memory on a
worker. Each partition holds part of the simulation state data.

A partition for a spatial app (also called a _spatial app
partition_ or _spatial partition_)
contains all the entities in a spatial app's ownership area. SimSpace Weaver puts entities in
spatial app partitions based on the spatial location of each entity. This means that
SimSpace Weaver tries to place entities that are spatially near each other on the same
worker. This minimizes the amount of knowledge that an app requires of entities that it
doesn't own to simulate the entities that it does own.

## State Fabric

The _State Fabric_ is the system of shared memory
(the collection of all partitions) on all workers. It holds all of the state data for
your simulation.

The State Fabric uses a custom binary format that describes an entity as a set of
initial data and an update log, for each data field of that entity. With this format,
you can access the state of an entity at a previous point in simulation time and map it
back to a point in real-world time. The buffer has a finite size, and it's not possible
to go back in time beyond what's in the buffer. SimSpace Weaver uses a pointer to the current
offset in the update log for each field, and it updates a pointer as part of a field
update. SimSpace Weaver maps these update logs into an app’s process space using shared
memory.

This object format results in low overhead and no serialization costs. SimSpace Weaver also
uses this object format to parse and identify index fields (such as entity
position).

## Entities

An _entity_ is the smallest building block of data in
your simulation. Examples of entities include actors (such as people and vehicles) and
static objects (such as buildings and obstacles). Entities have properties (such as
position and orientation) that you can store as persistent data in SimSpace Weaver. Entities
exist within partitions.

## Apps

A SimSpace Weaver _app_ is software that you write that
contains custom logic that runs each simulation tick. The purpose of most apps is to
update entities as the simulation runs. Your apps call APIs in the SimSpace Weaver app SDK to
perform actions (such as reading and updating) on entities in your simulation.

You package your apps and their required resources (such as libraries) as .zip files
and upload them to SimSpace Weaver. An app runs in a Docker container on a worker. SimSpace Weaver
allocates each app a fixed number of resource units on the worker.

SimSpace Weaver assigns ownership of one (and only one) partition to each app. An app and
its partition are located on the same worker. Each partition has only one app owner. An
app can create, read, update, and delete entities in its partition. An app owns all
entities in its partition.

There are three types of apps: _spatial apps_,
_custom apps_, and _service
apps_. They differ by use cases and lifecycles.

###### Note

In SimSpace Weaver, the term "app" can refer to the code for an app or a running
instance of that code.

### Spatial apps

_Spatial apps_ update the state of entities that
exist spatially in your simulation. For example, you might define a
`Physics` app that's responsible for moving and colliding entities
for every tick based on their velocity, shape, and size. In this case, SimSpace Weaver
runs multiple instances of the `Physics` app in parallel to handle the
size of the workload.

SimSpace Weaver manages the lifecycle of spatial apps. You specify an arrangement of
spatial app partitions in your simulation schema. When you launch your simulation,
SimSpace Weaver starts a spatial app for each spatial app partition. When you stop the
simulation, SimSpace Weaver shuts down your spatial apps.

Other types of apps can create entities, but only spatial apps can update
entities. Other types of apps must transfer entities that they create to a spatial
domain. SimSpace Weaver uses the spatial location of an entity to move the entity to the
partition of a spatial app. This transfers ownership of the entity to the spatial
app.

### Custom apps

You use _custom apps_ to interact with your
simulation. A custom app reads entity data using subscriptions. A custom app can
create entities. However, the app must transfer an entity to a spatial app to
include the entity in the simulation and update it. You can have SimSpace Weaver assign a
network endpoint to a custom app. Simulation clients can connect to the network
endpoint to interact with the simulation. You define your custom apps in your
simulation schema, but you are responsible to start and stop them (using SimSpace Weaver
API calls). After you start a custom app instance on a worker, SimSpace Weaver doesn't
transfer the instance to another worker.

### Service apps

You can use a _service app_ when you need a
read-only process running on every worker. For example, you can use a service app if
you have a large simulation and you need a viewing client that moves through the
simulation and displays only the visible entities to the user. In this case, a
single custom app instance can’t process all the entities in the simulation. You can
configure a service app to launch on every worker. Each of these service apps can
then filter the entities on its assigned worker and send only the relevant entities
to its connected clients. Your viewing client can then connect to different service
apps as it moves through the simulation space. You configure service apps in your
simulation schema. SimSpace Weaver starts and stops your service apps for you.

### App summary

The following table summarizes the characteristics of the different types of
SimSpace Weaver apps.

|                     | Spatial apps                                                                                        | Custom apps                  | Service apps                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Read entities       | Yes                                                                                                 | Yes                          | Yes                                                                                              |
| Update entities     | Yes                                                                                                 | No                           | No                                                                                               |
| Create entities     | Yes                                                                                                 | Yes\*                        | Yes\*                                                                                            |
| Lifecycle           | Managed (SimSpace Weaver controls it.)                                                              | Unmanaged (You control it.)  | Managed (SimSpace Weaver controls it.)                                                           |
| Start method        | SimSpace Weaver starts one app instance for each spatial partition,<br>as specified in your schema. | You start each app instance. | SimSpace Weaver starts one or more app instances on each worker, as<br>specified in your schema. |
| Clients can connect | No                                                                                                  | Yes                          | Yes                                                                                              |

\* When a custom app or service app creates an entity, the app must transfer
ownership of the entity to a spatial app so that the spatial app can update the
state of the entity.

### Domains

A SimSpace Weaver _domain_ is a collection of app
instances that run the same executable app code and have the same launch options and
commands. We refer to domains by the types of apps that they contain: spatial
domains, custom domains, and service domains. You configure your apps within
domains.

### Subscriptions and replication

An app creates a _subscription_ to a spatial
region to learn entity events (for example, enter, exit, create, update, and delete)
in that region. An app processes entity events from a subscription before it reads
data for entities in partitions that it doesn't own.

A partition can exist on the same worker as the app (this is called a _local partition_), but another app can own the
partition. A partition can also exist on a different worker (this is called a
_remote partition_). If the subscription is to
a remote partition, the worker creates a local copy of the remote partition through
a process called _replication_. The worker then
reads the local copy (replicated remote partition). If another app on the worker
needs to read from that partition on the same tick, then the worker reads the same
local copy.
