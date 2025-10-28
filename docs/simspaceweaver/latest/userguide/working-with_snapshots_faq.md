End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Frequently asked questions about snapshots

###### Does my simulation continue to run during a snapshot?

Your simulation resources continue to run during a snapshot and you continue
to receive billing charges for that time. The time counts towards your
simulation's maximum duration. Your apps don't receive ticks while
the snapshot is in progress. If your clock status was `STARTED` when
the snapshot creation started, your clock will still indicate
`STARTED` status. Your apps receive ticks again after the snapshot
finishes. If your clock status was `STOPPED` then your clock status
will remain `STOPPED`. Note that a simulation with a
`STARTED` status is running even if its clock status is
`STOPPED`.

###### What happens if a snapshot is in progress and my simulation reaches its maximum duration?

Your simulation will finish the snapshot and then stop as soon as the
snapshot process ends (either successfully or unsuccessfully). We recommend
that you test the snapshot process beforehand to find out how long it takes,
the size of the snapshot file you can expect, and if it should complete
successfully.

###### What happens if I stop a simulation that has a snapshot in progress?

A snapshot in progress stops immediately when you stop the simulation.
It won't create a snapshot file.

###### How can I stop a snapshot in progress?

The only way to stop a snapshot in progress is to the stop the
simulation. **You can't restart a simulation
after you stop it.**

###### How long will it take to complete my snapshot?

The time required to create a snapshot depends on your
simulation. We recommend that you test the snapshot
process beforehand to find out how long it will take for
your simulation.

###### How large will my snapshot file be?

The size of a snapshot file depends on your
simulation. We recommend that you test the snapshot
process beforehand to find out how large the file could be
for your simulation.
