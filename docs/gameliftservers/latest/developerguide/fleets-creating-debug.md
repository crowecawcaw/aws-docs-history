# Debug Amazon GameLift Servers fleet issues

This topic provides guidance on how to resolve issues with your Amazon GameLift Servers managed EC2 fleets.

## Fleet creation issues

When you create a managed EC2 fleet, the Amazon GameLift Servers service initiates a workflow that
creates the fleet, deploys EC2 instances with your game server build installed, and
starts game server processes on each instance. For a detailed description, see [How Amazon GameLift Servers fleet creation works](fleets-intro.md#fleets-creation-workflow "fleets-intro.md#fleets-creation-workflow"). A
fleet cannot host game sessions and players until it reaches **Active** status.

You can debug issues that prevent fleets from becoming active by identifying the fleet
creation phase where the issue occurred and reviewing fleet creation events and logs. If
the logs do not offer useful information, it's possible that the problem is due to an
internal service error. In this situation, try to create the fleet again. If the problem
persists, try re-uploading the game build to resolve possible file corruption). You can
also contact Amazon GameLift Servers support or post a question on the forum.

**Downloading and validating the build**
During this phase, Amazon GameLift Servers gets your uploaded game server build, extracts the files,
and runs any install scripts. If fleet creation fails during these phases,
look at fleet events and logs to pinpoint the issue. Possible causes
include:

- Amazon GameLift Servers can't get the compressed build file (event
  `FLEET_BINARY_DOWNLOAD_FAILED`). Verify that the
  build's storage location can be accessed, that you're creating a
  fleet in the same AWS Region as the build, and that Amazon GameLift Servers has the
  correct permissions to access it.
- Amazon GameLift Servers can't extract the build files (event
  `FLEET_CREATION_EXTRACTING_BUILD`).
- An install script in the build files failed to complete
  successfully (event `FLEET_CREATION_FAILED_INSTALLER`).

**Building fleet resources**
Issues during this phase usually involve the allocation and deployment of fleet
resources. Possible causes include:

- The requested instance type isn't available.
- The requested fleet type (Spot or On-Demand) isn't
  available.

**Activating game server processes**
During this phase, Amazon GameLift Servers is attempting a number of tasks and testing key elements,
including the game server's viability, runtime configuration settings, and
the game server's ability to connect with the Amazon GameLift Servers service using the Server
SDK.

###### Note

In this phase, you can remotely access a fleet instance to further
investigate issues. See [Remotely connect to Amazon GameLift Servers fleet instances](fleets-remote-access.md "fleets-remote-access.md").

Possible issues include:

- Server processes don't start running. This suggests an issue with the fleet's runtime
  configuration settings (events
  `FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND` or
  `FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE`. Verify
  that you've correctly set the launch path and optional launch
  parameters.
- Server processes start running, but the fleet fails to activate. If server
  processes start and run successfully, but the fleet does not move to
  **Active** status, a likely cause
  is that the server process is failing to communicate with the Amazon GameLift Servers
  service. Verify that your game server is making these correct server
  SDK calls (see [Initialize the server process](gamelift-sdk-server-api.md#gamelift-sdk-server-initialize "gamelift-sdk-server-api.md#gamelift-sdk-server-initialize")):
  - Server process fails to initialize (event
    `SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT`).
    The server process is not successfully calling
    `InitSdk()`.
  - Server process fails to notify Amazon GameLift Servers when it's ready to
    host a game session (event
    `SERVER_PROCESS_PROCESS_READY_TIMEOUT`). The
    server process initialized but didn't call
    `ProcessReady()` in time.

- A VPC peering connection request failed. For fleets that are created with
  a VPC peering connection (see [To set up VPC peering with a new
  fleet](vpc-peering.md#fleets-creating-aws-cli-vpc "vpc-peering.md#fleets-creating-aws-cli-vpc")), VPC peering is
  done during this **Activating** phases.
  If a VPC peering fails for any reason, the new fleet will fail to
  move to **Active** status. You can
  track the success or failure of the peering request by calling
  [describe-vpc-peering-connections](../../../cli/latest/reference/gamelift/describe-vpc-peering-connections.md "../../../cli/latest/reference/gamelift/describe-vpc-peering-connections.md"). Be sure to check that
  a valid VPC peering authorization exists ([describe-vpc-peering-authorizations](../../../cli/latest/reference/gamelift/describe-vpc-peering-authorizations.md "../../../cli/latest/reference/gamelift/describe-vpc-peering-authorizations.md"), since
  authorizations are only valid for 24 hours.

## Server process issues

**Server processes start but fail quickly or report poor health.**

Other than issues with your game build, this outcome can happen when
trying to run too many server processes simultaneously on the instance. The
optimum number of concurrent processes depends on both the instance type and
your game server's resource requirements. Try reducing the number of
concurrent processes, which is set in the fleet's runtime configuration, to
see if performance improves. You can change a fleet's runtime configuration
using either the Amazon GameLift Servers console (edit the fleet's capacity allocation
settings) or by calling the AWS CLI command [update-runtime-configuration](../../../cli/latest/reference/gamelift/update-runtime-configuration.md "../../../cli/latest/reference/gamelift/update-runtime-configuration.md").

## Fleet deletion issues

**Fleet can't be terminated due to max instance count.**

The error message indicates that the fleet being deleted still has active
instances, which is not allowed. You must first scale a fleet down to zero
active instances. This is done by manually setting the fleet's desired
instance count to "0" and then waiting for the scale-down to take effect. Be
sure to turn off auto-scaling, which will counteract manual settings.

**VPC actions are not authorized.**

This issue only applies to fleets that you have specifically created VPC
peering connections for (see [VPC peering for Amazon GameLift Servers](vpc-peering.md "vpc-peering.md"). This scenario occurs because the process
of deleting a fleet also includes deleting the fleet's VPC and any VPC
peering connections. You must first get an authorization by calling the
service API for Amazon GameLift Servers [CreateVpcPeeringAuthorization()](../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md "../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md") or use the AWS CLI command
`create-vpc-peering-authorization`. Once you have the
authorization, you can delete the fleet.

## Amazon GameLift Servers Realtime fleet issues

**Zombie game sessions: They start and run a game, but they never end.**

You might observe this issues as any of the following scenarios:

- Script updates are not picked up by the fleet's Realtime
  servers.
- The fleet quickly reaches maximum capacity and does not scale down
  when player activity (such as new game session requests) decreases.

This is almost certainly a result of failing to successfully call
`processEnding` in your Realtime script. Although the fleet
goes active and game sessions are started, there is no method for stopping
them. As a result, the Realtime server that is running the game session is
never freed up to start a new one, and new game sessions can only start when
new Realtime servers are spun up. In addition, updates to the Realtime
script do not impact already- running game sessions, only ones.

To prevent this from happening, scripts need to provide a mechanism to
trigger a `processEnding` call. As illustrated in the [Amazon GameLift Servers Realtime script example](realtime-script.md#realtime-script-examples "realtime-script.md#realtime-script-examples"), one way is to program an
idle session timeout where, if no player is connected for a certain amount
of time, the script will end the current game session.

However, if you do fall into this scenario, there are a couple workarounds
to get your Realtime servers unstuck. The trick is to trigger the
Realtime server processes—or the underlying fleet
instances—to restart. In this event, Amazon GameLift Servers automatically closes
the game sessions for you. Once Realtime servers are freed up, they can
start new game sessions using the latest version of the Realtime script.

There are a couple of methods to achieve this, depending on how pervasive
the problem is:

- Scale the entire fleet down. This method is the simplest to do but
  has a widespread effect. Scale the fleet down to zero instances,
  wait for the fleet to fully scale down, and then scale it back up.
  This will wipe out all existing game sessions, and let you start
  fresh with the most recently updated Realtime script.
- Remotely access the instance and restart the process. This is a
  good option if you have only a few processes to fix. If you are
  already logged onto the instance, such as to tail logs or debug,
  then this may be the quickest method. See [Remotely connect to Amazon GameLift Servers fleet instances](fleets-remote-access.md "fleets-remote-access.md").

If you opt not to include way to call `processEnding` in your Realtime
script, there are a couple of tricky situations that might occur even when the fleet
goes active and game sessions are started. First, a running game session does not end.
As a result, the server process that is running that game session is never free to start
a new game session. Second, the Realtime server does not pick up any script updates.
