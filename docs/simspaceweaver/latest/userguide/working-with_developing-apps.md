End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Developing apps

SimSpace Weaver development requires an Amazon Linux 2 (AL2) environment to build apps
because your simulations run on Amazon Linux in the AWS Cloud. If you're using Windows, you
can use scripts in the SimSpace Weaver app SDK to create and launch a Docker container that
runs AL2 with the dependencies that you need to build SimSpace Weaver apps. You can also
launch an AL2 environment using Windows Subsystem for Linux (WSL), or use a native AL2 system.
For more information, see [Set up your local environment for SimSpace Weaver](setting-up_local.md "setting-up_local.md").

###### Note

Regardless of how you configure your local development environment, your apps run in
Docker containers when you upload them to run in the AWS Cloud. **Your
apps don't have direct access to the host operating system**.

###### General flow of a SimSpace Weaver app

1. Create an application.
2. Loop:
   1. Begin the update by creating a `Transaction`.
      1. Exit the loop if the simulation is shutting down.

   2. Process subscription and ownership entity events.
   3. Update the simulation.
   4. Commit the `Transaction` to end the update.

3. Destroy the application.

## Spatial apps

Each spatial app has an ownership area that is a spatial region of the simulation world.
Entities located in a spatial app's ownership area are stored in the app's assigned
partition. The single spatial app has full ownership (read and write permissions) over all
entities within its assigned partition. No other apps can write to those entities. The
spatial app advances the state of its entities. Each spatial app owns only 1 partition.
SimSpace Weaver uses the spatial location of an entity to index and assign it to a spatial
app partition.

The SimSpace Weaver app SDK provides a sample application. You can find the
source code for the spatial app of the sample application in the following folder (use the correct path separator for your operating system):

```
`sdk-folder`\Samples\PathfindingSample\src\SpatialApp
```

## Custom apps

You create and use custom apps to interact with the simulation.

###### Custom apps can

- Create entities
- Subscribe to other partitions
- Commit changes

###### General flow of a custom app

1. Create an application.
2. Subscribe to a specific region in the simulation:
   1. Create a `Transaction` to begin the first update.
   2. Create a subscription for the specific region.
   3. Commit the `Transaction` to end the first update.

3. Loop:
   1. Create a `Transaction` to begin the update.
      1. Exit the loop if the simulation is shutting down.

   2. Process state changes.
   3. Commit the `Transaction` to end the update.

4. Destroy the application.

After a custom app creates an entity, it must transfer the entity to a spatial domain in
order for the entity to exist spatially within the simulation. SimSpace Weaver uses the
entity's spatial location to place the entity in the appropriate spatial app partition. The
custom app that created the entity can't update or delete the entity after transferring it
to a spatial domain.

The SimSpace Weaver app SDK provides a sample application. You can use the custom apps
included in the sample application as models for your own custom apps. You can find the
source code for the view app (a custom app) of the sample application in the following
folder (use the correct path separator for your operating system):

```
`sdk-folder`\Samples\PathfindingSample\src\ViewApp
```
