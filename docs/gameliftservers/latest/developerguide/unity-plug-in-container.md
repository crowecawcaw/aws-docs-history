# Plugin for Unity: Deploy your game to a

managed container fleet

Use this guided plugin workflow to create a container image for your game server and
deploy it to a container-based hosting solution. When you’ve successfully completed this
workflow, your containerized game server is running in the cloud, and you can use the
plugin to start a game client, connect to a game session, and play the game.

## Before you start

This workflow assumes that you’ve completed the following tasks.

- **Integrate your game server code with Amazon GameLift Servers
  server SDK.** our hosted game server must be able to
  communicate with the Amazon GameLift Servers service so that it can respond to
  requests to start new game sessions and report game session status. If you
  haven’t completed this task, we recommend that you follow the plugin
  workflow Host with Anywhere first. For guidance on preparing your game
  server code, see [Integrate your server code](unity-plug-in-anywhere.md#unity-plug-in-anywhere-integrate-server "unity-plug-in-anywhere.md#unity-plug-in-anywhere-integrate-server"). For a managed container fleet,
  you must integrate your game with server SDK version 5.2 or higher.

###### Note

If you're using the startup game map, this task is already
done for you.

- **Package your game server executable to run on
  Linux.**
- **Gather files to deploy with your game server
  build.** On your local machine, create a working directory to
  organize the files, which will be built into your game server container
  image. These might include game dependencies, a script to launch game
  servers and other processes when starting a container, etc.
- **Integrate your game client code with
  Amazon GameLift Servers.** One way to complete this task is to add a sample asset
  (included with the plugin) that’s already integrated. For guidance on
  preparing your game client code, see [Integrate your client code](unity-plug-in-anywhere.md#unity-plug-in-anywhere-integrate-client "unity-plug-in-anywhere.md#unity-plug-in-anywhere-integrate-client").
- **Install Docker on your local
  machine.**
  You need this tool installed if you want the plugin to create
  container images for you and push them to an ECR repository.
  Alternatively you can do these tasks manually and instruct the plugin to
  use an existing container image. For more information about building
  your image manually, see [Build a container image for Amazon GameLift Servers](containers-prepare-images.md "containers-prepare-images.md").

###### To start the Amazon GameLift Servers managed containers workflow:

- In the Unity editor main toolbar, choose the Amazon GameLift Servers menu, and select **Managed Containers**.
  This action opens the plugin page **Host with Managed Containers**, which presents a step-by-step process
  to create a container image with your game server build, deploy it to a container fleet, and launch your game.

## Step 0: Set your profile

This section displays your currently selected user profile. Verify that the
current user profile is the one you want to use for this workflow. All the resources
that you create in this workflow are associated with the profile's AWS account and
are placed in the profile's default AWS Region. The profile user's permissions
determine your access to AWS resources and actions.

You might need to modify the selected user profile if:

- No profile is currently selected.
- You want to select a different profile or create a new profile.
- You need to bootstrap the selected profile (if bootstrap status is
  inactive).

###### To set or change the selected user profile

- In the Amazon GameLift Servers menu, choose **Open AWS Access
  Credentials**.

## Step 1: Assess container readiness

Before deploying your game server to a container fleet, you must package it into a
container image and store in an Amazon ECR repository. The plugin can complete these tasks
for you or you can do these tasks manually. In this step, provide information about
the status of your container image and the ECR repository.

Use the assessment questions to tell the plugin what steps it needs to take:

- **Create a new container image.** If you
  choose this option, the next step will prompt you for the location of your
  game server build directory and the build executable. The plugin uses a
  Dockerfile template (supplied by Amazon GameLift Servers) and automatically configures it for
  your game. You can view the template at [Build a container image for Amazon GameLift Servers](containers-prepare-images.md "containers-prepare-images.md"). After choosing this option,
  indicate where you want the plugin to store the new image:
  - Create a new Amazon ECR repository and push the container image to
    it. The plugin creates a private ECR repo
    using the AWS account and default AWS Region in your selected user
    profile.
  - Push the container image to a previously created Amazon ECR repository. If
    you choose this option, the next step will prompt you to select an
    existing Amazon ECR repository from a list. The list includes all Amazon ECR
    repositories for the AWS account and default AWS Region in your
    selected user profile. You can select a public or private
    repository.

- **Use an existing container image.** If
  you've manually built an image, we recommend that you use the Dockerfile
  template supplied by Amazon GameLift Servers, which is available at [Build a container image for Amazon GameLift Servers](containers-prepare-images.md "containers-prepare-images.md"). After choosing this option,
  indicate where the image is located.
  - A locally stored Docker-generated image. If you choose this option, the plugin
    creates a new Amazon ECR private repository and pushes the local image file to it.
    The next step will prompt you for an image ID, which the
    plugin uses to locate the image file.
  - A container image that's already stored in an Amazon ECR repository. If you choose this option, the
    next step will prompt you to select an existing Amazon ECR repository and
    image from a list. The list includes all Amazon ECR repositories for the
    AWS account and default AWS Region in your selected user
    profile. You can select a public or private repository.

## Step 2: Configure image deployment

In this step, provide information that the plugin needs to deploy your container
image to a container fleet. This step requests the following information:

- The location of your game server build, container image, or Amazon ECR repository,
  based on your selections in Step 1.
- The scenario to use for your managed containers deployment.
- Optional deployment settings. This section has configuration settings that the plugin
  uses by default. You can modify these or keep the default values
  - Game name is set to the name of your game project by default. All
    AWS resources that the plugin creates references the game name value.
  - Port range, memory limit, and vCPU limit are configuration settings for
    the container fleet. For more information about customizing these values, see
    [Configure network connections](containers-design-fleet.md#containers-custom-network "containers-design-fleet.md#containers-custom-network")
    for connection port range, and
    [Set resource limits](containers-design-fleet.md#containers-design-fleet-limits "containers-design-fleet.md#containers-design-fleet-limits")
    for resource limits.
  - Container image tag is used to categorize your container images in Amazon ECR. The default value is
    `unity-gamelift-plugin`.

### Deployment scenario options

This scenario deploys your game server to a single container fleet.
It's a good starting point for testing your server integration with
AWS and your container configuration. It deploys the following
resources.

- Amazon GameLift Servers container group definition describes
  how to deploy and run your container images on a container
  fleet.
- Amazon GameLift Servers container fleet (On-Demand) with your game
  server container installed and running, with alias.
- Amazon Cognito user pool and client to enable players to
  authenticate and start a game.
- API Gateway authorizer that links the user pool with
  APIs.
- Web access control list (ACL) for throttling excessive player calls to API Gateway.
- Backend service to make requests to the Amazon GameLift Servers service on behalf of
  game clients, such as to request game sessions and join games:

      + API Gateway + Lambda function for players to request a game
       session slot. This function calls
       `CreateGameSession()` if no open slots
       are available.
      + API Gateway + Lambda function for players to get
       connection info for their game request.

  This scenario deploys your game server to a container fleet,
  configures game session placement, and sets up FlexMatch matchmaking. This
  scenario is useful when you're ready to start designing a custom
  matchmaker for your hosting solution. Use this scenario to create the
  basic resources for this solution, which you can customize later as
  needed. It deploys the following resources:

- Amazon GameLift Servers container group definition that describes how to
  deploy and run your container images on a container fleet.
- Amazon GameLift Servers container fleet (On-Demand) with your game server
  container installed and running, with alias.
- FlexMatch matchmaking configuration and matchmaking rule set
  to accept player requests and form matches.
- Amazon GameLift Servers game session queue that fulfills requests for
  proposed matches by finding the best possible hosting
  resource (based on viability, cost, player latency, etc.)
  and starting a game session.
- Amazon Cognito user pool and client to enable players to
  authenticate and start a game.
- API Gateway authorizer that links the user pool with APIs.
- Web access control list (ACL) for throttling excessive player
  calls to API Gateway.
- Backend service to make requests to the Amazon GameLift Servers service on
  behalf of game clients, such as to request game sessions and
  join games:
  - API Gateway + Lambda function for players to request a game
    session slot. This function calls
    `StartMatchmaking()` if no open slots are
    available.
  - API Gateway + Lambda function for players to get connection
    info for their game request.

- DynamoDB tables to store matchmaking tickets for
  players and game session information.
- Amazon SNS topic + Lambda function to handle GameSessionQueue
  events.

## Deploy container fleet

When your fleet configuration is complete, choose the **Deploy
container fleet** button to start deployment. This process can take
several minutes while the plugin creates a container image and pushes it to ECR,
provisions hosting resources for the container fleet, deploys the fleet and other
AWS resources for the selected hosting solution scenario.

When you start a deployment, you can track the progress of each step. Depending
on your configuration, the steps might include the following:

- Configuring container image
- Creating an Amazon ECR repository
- Building an image and pushing to Amazon ECR
- Creating container group definition
- Creating container fleet

For more detailed deployment information, choose **View in AWS
Management Console**. When the container fleet reaches active status,
the fleet is actively running containers with server processes that are ready to
host game sessions.

When deployment is complete, you have a working container fleet that’s ready to
host game sessions and accept player connections.

You can’t stop a deployment in progress. If the deployment enters a bad state or
fails, you can start over by using the **Reset deployment**
option.

## Launch client

At this point, you've completed all the tasks to launch and play your multiplayer
game hosted with Amazon GameLift Servers. To play your game, choose **Start Client**
to launch a local instance of your game client.

- If you deployed the single fleet scenario, open one instance of your game
  client with one player and enter the server map to move around. You can open
  a second instance of the game client to add a second player to the same
  server game map.
- If you deployed the FlexMatch scenario, the hosting solution waits for at
  least two game clients to make matchmaking requests. Open at least two
  instances of your game client with one player. The two players will be
  matched and prompted to join a game session for the match.

## Update a container fleet

If you've successfully deployed a managed containers hosting solution, you can use the
**Update deployment**feature. This option lets you update configuration
settings for a deployed container fleet, without having to create a new fleet.

When updating a deployment, you can deploy a container image with a different game server
build, change the Amazon ECR repository, choose a different deployment scenario, and customize
optional configuration settings.

When you're ready to deploy your changes, choose Update. The time required for a deployment
update is similar to a full deployment. For detailed deployment information, choose
**View in AWS Management Console**.

## Clean up deployed resources

As a best practice, clean up the AWS resources for your managed containers
solution as soon as you no longer need them. You might continue to incur costs for these resources
if you don't remove them.

Delete the following resources:

- Managed container resource stack. The resources in this stack depends on the deployment
  scenario you selected. To delete the entire stack, use the AWS CloudFormation console.
  Stacks that are generated from the Amazon GameLift Servers plugin use the following naming
  convention: `GameLiftPluginForUnity-{GameName}-Containers`. Wait
  for the stack deletion process to complete before you initiate a new managed
  containers deployment in the plugin. For more information, see [Delete a stack from the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md").
- Amazon ECR repository. If you used the plugin to create a repository for your container image, you
  might want to delete any repositories that are no longer needed. You don't
  need to delete a repository before resetting a managed containers
  deployment. If you update or reset a deployment, the plugin will
  automatically use the same repository unless directed to use another one.
  For more information, see
  [Deleting a private repository in Amazon ECR](../../../AmazonECR/latest/userguide/repository-delete.md "../../../AmazonECR/latest/userguide/repository-delete.md").
