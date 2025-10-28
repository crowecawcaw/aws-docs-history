End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Snapshots

You can create a _snapshot_ to back up your simulation entity data
at any point in time.
SimSpace Weaver creates a .zip file in an Amazon S3 bucket.
You can create a new simulation with the snapshot. SimSpace Weaver initializes
the State Fabric of your new simulation with the entity data stored in the snapshot,
starts the spatial and service apps that were running when the snapshot was created,
and sets the clock to the appropriate tick. SimSpace Weaver gets the configuration of
your simulation from the snapshot instead of from a schema file. Your app .zip files
must be in the same location in Amazon S3 as they were in the original simulation.
You must start any custom apps separately.

###### Topics

- [Use cases for snapshots](#working-with_snapshots_use-cases "#working-with_snapshots_use-cases")
- [Use the SimSpace Weaver console to work with snapshots](working-with_snapshots_console.md "working-with_snapshots_console.md")
- [Use the AWS CLI to work with snapshots](working-with_snapshots_cli.md "working-with_snapshots_cli.md")
- [Using snapshots with AWS CloudFormation](working-with_cloudformation_snapshots.md "working-with_cloudformation_snapshots.md")
- [Frequently asked questions about snapshots](working-with_snapshots_faq.md "working-with_snapshots_faq.md")

## Use cases for snapshots

### Return to a previous state and explore branching scenarios

You can create a snapshot of your simulation to save it at a specific
state. You can then create multiple new simulations from that snapshot and
explore different scenarios that could branch from that state.

### Disaster recovery and security best practices

We recommend that you regularly backup your simulation, especially for simulations
that run for more than 1 hour or use multiple workers.
Backups can help you recover from disasters and security incidents. Snapshots provide
a way for you to backup your simulation. Snapshots require your app .zip files to exist
in the same location in Amazon S3 as they were before. If you need to be able to
move your app .zip files to another location, you must use a custom backup solution.

For more information about other best practices, see [Best practices when working with SimSpace Weaver](best-practices.md "best-practices.md") and [Security best practices for SimSpace Weaver](security_best-practices.md "security_best-practices.md").

### Extend the duration of your simulation

Your _simulation resource_ is the representation of
your simulation in SimSpace Weaver. All simulation resources have a
`MaximumDuration` setting. A simulation resource automatically stops
when it reaches its `MaximumDuration`. The maximum value of
`MaximumDuration` is `14D`
(14 days).

If you need your simulation to persist longer than the `MaximumDuration`
of its simulation resource, you can create a snapshot before the simulation resource
reaches its `MaximumDuration`.
You can start a new simulation (create a new simulation resource) with your snapshot.
SimSpace Weaver initializes your entity data from the snapshot, starts the same
spatial and service apps that ran before, and restores the clock. You can start
your custom apps and perform any additional custom initialization. You can set
the `MaximumDuration` of the new simulation resource to a different value
when you start it.
