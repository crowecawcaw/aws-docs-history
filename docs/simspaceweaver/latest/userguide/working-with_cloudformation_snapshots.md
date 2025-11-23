End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Using snapshots with AWS CloudFormation

A [snapshot](working-with_snapshots.md "working-with_snapshots.md") is a backup
of a simulation. The following example
starts a new simulation from a snapshot instead of from a schema. The
snapshot in this example was created from a SimSpace Weaver app SDK
project simulation. CloudFormation creates the new simulation resource
and initializes it with data from the snapshot. The new simulation
can have a different `MaximumDuration` than the
original simulation.

We recommend that you make and use a copy of your original
simulation's app role. The original simulation's app role could
be deleted if you delete that simulation's CloudFormation
stack.

```

Description: "Example - Start a simulation from a snapshot"
Resources:
  MyTestSimulation:
    Type: "AWS::SimSpaceWeaver::Simulation"
    Properties:
      MaximumDuration: "2D"
      Name: "MyTestSimulation_from_snapshot"
      RoleArn: "arn:aws:iam::111122223333:role/weaver-MyTestSimulation-app-role-copy"
      SnapshotS3Location:
        BucketName: "weaver-mytestsimulation-111122223333-artifacts-us-west-2"
        ObjectKey: "snapshot/MyTestSimulation_22-12-15_12_00_00-230428-1207-13.zip"

```
