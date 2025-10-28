# App Block Builder Actions

You can perform the following actions on an app block builder, depending on the
current state (status) of the app block builder instance.

**Delete**

Permanently delete an app block builder.

The instance must be in a **Stopped** state.

**Connect**

Connect to a running app block builder. This action starts a desktop
streaming session with the app block builder to install and add
applications, and create an app block.

The instance must be in a **Running** state.

**Start**

Start a stopped app block builder. A running instance is billed to your
account.

The instance must be in a **Stopped** state, and
associated with an app block.

**Stop**

Stop a running app block builder. A stopped instance is not billed to your
account.

The instance must be in a **Running** state.

**Update**

Update any of the app block builder properties, except the name.

The instance must be in a **Stopped** state.

None of these actions can be performed on an instance in any of the following
intermediate states:

- **Pending**
- **Stopping**
- **Starting**
- **Deleting**
