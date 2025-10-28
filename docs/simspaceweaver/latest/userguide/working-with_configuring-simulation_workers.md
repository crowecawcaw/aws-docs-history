End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Workers

The `workers` section specifies the type and number of workers that you want for your
simulation. SimSpace Weaver uses its own worker types that map to Amazon EC2 instance types.

```

workers:
  MyComputeWorkers:
    type: "sim.c5.24xlarge"
    desired: 1

```

## Enabling multi-worker simulations

You can create a simulation that uses more than 1 worker. By default, simulations use 1 worker.
You must modify your simulation schema before you start the simulation.

###### Note

You can't change a simulation that has already started. If you want to enable multi-worker for
a running simulation, you must stop and delete the simulation first.

To use more than one worker, set the `desired` number of compute instances to
a value greater than 1. There is a maximum number of apps for each worker. For more
information, see [SimSpace Weaver endpoints and quotas](service-quotas.md "service-quotas.md").
SimSpace Weaver will only use more than 1 worker when the number of apps on a worker exceeds
this limit. SimSpace Weaver can place an app on any of the available workers. App placement on
a specific worker isn't guaranteed.

The following schema snippet demonstrates a configuration for a simulation that requests 2 workers.
SimSpace Weaver will attempt to allocate the second worker if the number of apps exceeds the maximum
number of apps for 1 worker.

```

workers:
  MyComputeWorkers:
    type: "sim.c5.24xlarge"
    desired: 2

```
