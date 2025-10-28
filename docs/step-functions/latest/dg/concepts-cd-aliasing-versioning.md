#

Manage continuous deployments with versions and aliases in Step Functions

You
can use
Step Functions
to manage continuous deployments of your workflows through state machine
_versions_ and _aliases_. A
_version_ is a numbered, immutable snapshot of a state machine
that
you can run. An
_alias_ is a pointer for up to two versions of a state
machine.

You can maintain multiple versions of your state machines and manage their deployment in your production workflow. With aliases, you can route traffic between
different workflow versions and gradually deploy those workflows to the production
environment.

Additionally, you can start state machine
executions
using a version or an alias. If you don't use a version or alias when you start a state
machine execution, Step Functions uses the latest revision of the state machine definition.

###### State machine revision

A state machine can have one or more revisions. When you update a state machine using the [UpdateStateMachine](../apireference/API_UpdateStateMachine.md "../apireference/API_UpdateStateMachine.md") API action, it creates a new state
machine revision. A _revision_ is an immutable, read-only snapshot of
a state machine’s definition and configuration. You can't start a state machine
execution from a revision, and revisions don't have an ARN. Revisions have a `revisionId`, which is a universally unique identifier (UUID).

###### Contents

- [Versions](concepts-state-machine-version.md "concepts-state-machine-version.md")
- [Aliases](concepts-state-machine-alias.md "concepts-state-machine-alias.md")
- [Versions and alias authorization](auth-version-alias.md "auth-version-alias.md")
- [Associating executions with a version or alias](execution-alias-version-associate.md "execution-alias-version-associate.md")
- [Deployment example](example-alias-version-deployment.md "example-alias-version-deployment.md")
- [Gradual deployment of versions](version-rolling-deployment.md "version-rolling-deployment.md")
