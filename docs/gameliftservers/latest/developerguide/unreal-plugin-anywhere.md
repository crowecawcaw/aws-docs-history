# Plugin for Unreal: Host your game locally with

Amazon GameLift Servers Anywhere

Use this workflow to set up your local workstation as a game server host using an
Anywhere fleet. You can use it to test your game server integration before deploying to
a cloud-based managed fleet. It can also be useful for local testing during iterative
game development.

###### To start the Amazon GameLift Servers Anywhere workflow:

- In the Unreal editor main toolbar, choose the Amazon GameLift Servers menu, and select **Host
  with Anywhere**. This action opens the plugin page **Deploy
  Anywhere**, which presents a six-step process to integrate, build,
  and launch your game components.

## Step 1: Set your profile

Choose the profile you want to use when following this workflow. The profile you
select impacts all steps in the workflow. All resources you create are associated
with the profile's AWS account and are placed in the profile's default AWS Region.
The profile user's permissions determine your access to AWS resources and
actions.

###### To set a user profile

1. Select a profile from the dropdown list of available profiles. If you
   don't have a profile yet or want to create a new one, go to the
   **Amazon GameLift** menu and choose **Set AWS
   User Profiles**.
2. If bootstrap status is not "Active", choose **Bootstrap
   profile** and wait for the status to change to "Active".

## Step 2: Set up your game code

In this step, prepare your game server and game client builds to work with Amazon GameLift Servers.
If you haven't yet integrated your game code, see [Plugin for Unreal: Integrate your game code](unreal-plugin-integrate.md "unreal-plugin-integrate.md").
Enter the paths to your game executables on your local workstation.

- Game server: Integrate your game server with the server SDK for Amazon GameLift Servers and package your game
  server build. For instructions, see [Plugin for Unreal: Integrate your game code](unreal-plugin-integrate.md "unreal-plugin-integrate.md"). The game server must be
  integrated with the server SDK in order to establish communication with
  the Amazon GameLift Servers service and respond to prompts to start new game sessions and
  accept game client connections.
- Game client: At minimum, you need a game client that can connect to your game server using IP
  address and port information. If you don't yet have your game client
  components set up for Amazon GameLift Servers, you can use the AWS CLI tool to manually
  request new game sessions, get connection information, and use that
  information to connect the game client.

At some point, you'll need to have a backend service to send new game
sessions requests to the Amazon GameLift Servers service and relay connection information
back to a game client. You can use the test maps included with the
plugin to add client Amazon GameLift Servers functionality to your game project. For help
with building a custom solution, see [Integrate Amazon GameLift Servers game client functionality](gamelift-sdk-client-api.md "gamelift-sdk-client-api.md").

## Step 3: Connect to an Anywhere fleet

In this step, you designate an Anywhere fleet to use. An Anywhere fleet defines a collection of compute resources, which can be located anywhere, for game server hosting.

- If the AWS account you're currently using has existing Anywhere fleets, open the Fleet name dropdown field and choose a fleet. This dropdown only shows the Anywhere fleets in the AWS Region for the currently active user profile.
- If there are no existing fleets—or you want to create a new one, choose Create new Anywhere fleet and provide a fleet name.

After you've chosen an Anywhere fleet for your project, Amazon GameLift Servers verifies that fleet status is active and displays the fleet ID. You can track progress of this request in the Unreal editor's output log.

## Step 4: Register your workstation

In this step, you register your local workstation as a compute resource in the new Anywhere fleet.

###### To register your workstation as an Anywhere compute

1. Enter a compute name for your local machine. If you add more than one compute in the fleet, the names must be unique.
2. Provide an IP address for your local machine. This field defaults to your machine's public IP address. You can also use localhost (127.0.0.1) as long as you're running your game client and server on the same machine.
3. Choose Register compute. You can track progress of this request in the Unreal editor's output log.

In response to this action, Amazon GameLift Servers verifies that it can connect to the compute and returns information about the newly registered compute. It also creates the console arguments that your game executables need when initializing communication with the Amazon GameLift Servers service.

## Step 5: Generate auth token

Game server processes that are running on your Anywhere compute need an authentication token to make calls
to the Amazon GameLift Servers service. The plugin automatically generates and stores an auth token for the Anywhere fleet
whenever you launch the game server from the plugin. The auth token value is stored as a command line argument,
which your server code can retrieve at runtime.

The code examples given above also allow you to use [AWS Signature Version 4 (SigV4) for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md"). SigV4
is the AWS signing protocol for adding authentication information to API requests.

You do not have to take any action in this step.

## Step 6: Launch game

At this point, you've completed all of the tasks needed to launch and play your multiplayer game on a local workstation using Amazon GameLift Servers.

###### To play your hosted game

1. Launch your game server. The game server will notify Amazon GameLift Servers when it is ready to host game sessions.
2. Launch your game client and use the new functionality to start a new game session. This
   request is sent to Amazon GameLift Servers via the new backend service. In
   response, Amazon GameLift Servers, calls the game server, running on your local
   machine, to start a new game session. When the game session is ready to
   accept players, Amazon GameLift Servers provides connection information for the
   game client to join the game session.
