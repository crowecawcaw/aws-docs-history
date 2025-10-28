This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Wickr IO clients troubleshooting

###### Topics

- [Setting up Wickr IO Docker container](#troubleshooting-docker-container "#troubleshooting-docker-container")
- [Provisioning Wickr IO client](#troubleshooting-provisioning "#troubleshooting-provisioning")
- [Start bot client failures](#troubleshooting-failures "#troubleshooting-failures")
- [Wickr IO command line
  interface](#troubleshooting-command-line-interface "#troubleshooting-command-line-interface")
- [Client and Integration compatibility
  issues](#troubleshooting-compatibility-issues "#troubleshooting-compatibility-issues")
- [Deploying custom Integrations](#troubleshooting-deploying-integrations "#troubleshooting-deploying-integrations")
- [Other issues](#troubleshooting-other-issues "#troubleshooting-other-issues")
- [Upgrading bots](#upgrading-bots "#upgrading-bots")
  These are troubleshooting suggestions associated with running the Wickr IO gateway,
  clients, and integrations. You may also run into some issues when developing your own custom
  Wickr IO integrations.

This section will describe some possible issues you may run into while using the Wickr IO
client and the associated services

## Setting up Wickr IO Docker container

**Cannot load Docker image**

If you receive the following error then you may have to make sure you have permissions to
access the unix socket to communicate with the Docker engine:

`docker: Got permission denied while trying to connect to the Docker daemon socket at
 unix:...`

**Solution**:

For help setting the appropriate permissions for you Docker account, see [Linux post-installation steps
for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/ "https://docs.docker.com/engine/install/linux-postinstall/")

**Wickr IO Fails startup due to directory permissions**

When running the Docker container on a Mac system, you may encounter a failure when starting
the Wickr IO Docker container if you have not changed the write permissions for the
`/opt` directory. This issue typically arises after the `./start.sh`
command. You will see the following errors:

```

  "QIODevice::write (QFile, "/opt/WickrIO/logs/WickrIOSvr.output"): device not open
terminate called after throwing an instance of 'zmq::error_t'
what(): No such file or directory
./start.sh: line 3: 7 Aborted WickrIOSvr"

```

This issue has only been seen on Mac systems. It occurs when a user creates the
`/opt` directory as the root, and then runs the container as a user.

**Solution**:

This is caused by a permission issue in the `/opt` directory. To resolve the
issue, change the permissions of the `/opt/WickrIO` directory (or the name of the
directory you created for your installation) to make it writeable. The following command will fix
this problem:

```
chmod 777 /opt/WickrIO

```

**Host system running out of disk space**

Your system is low on storage, preventing you from downloading and running a new Docker
container. This issue may arise if you have not removed old Docker containers from your
system.

**Solution**:

- Run `docker ps` to see all running containers.
- Run `docker kill container_id` on a container you would like to stop
  using.
- Run `docker rm container_id` to remove it from your system completely.

###### Note

Your integrations will not be affected and will stay on your system in your
`/opt/WickrIO` directory for future use.

**Docker Mounts denied Error**

You're getting the following error: `docker: Error response from daemon: Mounts denied:
 The path /opt/WickrIO is not shared from OS X and is not known to Docker.`

**Solution**:

Restart Docker.

**Wickr IO Not working on Mac M1 hosts**

The Wickr IO Docker images are not built to run on the Mac M1 hosts. During our testing of
the Mac M1 hardware, we discovered an issue related to the interaction exec() commands, which led
to failures when trying to start a bot from the command line interface (CLI).

**Solution**:

If you want to run the Wickr IO Docker images on Mac M1 hardware, follow these
steps:

- Make sure you have a version of Docker that supports the Linux/amd64 platform. The version
  we recommend for Mac is 20.10.14.
- When using the docker run command, make sure to include the —platform=linux/amd64
  option

## Provisioning Wickr IO client

**Bot client provisioning failures**

When adding a bot client to a Docker image, you may encounter issues during the provisioning
step. This can occur for both new and existing clients. Below are some common problems you might
face:

**_Username does not exist:_**

![The username is does not exist.](images/wickr-username.png)

**Solution**

Make sure the bot username is correct and exists in the Wickr Admin Console.

**_Incorrect password:_**

![The password is incorrect.](images/wickr-incorrect-password.png)

**Solution**

Make sure the password entered is correct. It should match the one used when creating the
bot user in the Wickr Admin Console.

###### Note

If your issue is different from the scenarios defined above, you can also identify the
issue by looking at the provisioning logs found in the following file:
`/opt/WickrIO/WickrIOProvisionLog.output`

For further assistance, [Wickr
support](https://mailto:wickr-support@amazon.com "https://mailto:wickr-support@amazon.com") is always available to assist you with any issues that are not addressed
here.

## Start bot client failures

**_Incorrect password_**

When trying to start a bot client, if you enter an incorrect password, you will get a “Bus
Error” and see the Docker container has exited.

![The password is incorrect.](images/wickr-wrong-password.png)

**Solution**

- Remove the stopped container using `docker rm -f (container-name).`
- Set up the docker container again by sharing a different host volume.

**_Wickr IO client does not start_**

If your Wickr IO client isn't starting and the previous solutions haven't resolved the
issue, try the following steps. First, check if the client is running by using the
`ps` command. Enter the following command in the terminal:

`ps -aef | grep wickrio_bot`

This command should return an entry for each Wickr IO client that is currently running.
Additionally, the command line interface of the Wickr IO Docker container includes various
commands that can help you diagnose any client issues.

- Enter the `list` command to see the list of Wickr IO clients.
- If the client state is `Paused` then use the `start` command to
  start the client.
- If the client state is `Running` and there are still no associated process
  running, then check the `WickrIOSvr.output` file for the background services to see
  if there is any issue starting the client. For more information on logging details, see [Wickr IO clients
  logging](../wickrioguide/logging.md "../wickrioguide/logging.md").

## Wickr IO command line

interface

**_Wickr IO client is not running._**

Once the client has started, it should remain in the `Running` state unless it is
manually paused or deleted. If, at any point, your client enters a `Down` or `Not
 Running` state unexpectedly, follow the solution below.

**Solution:**

Try restarting the Wickr IO client using the `restart` command. If the issue
continues, check the provisioning and client logs for more information, and then contact Wickr
Support.

**_Turn on debugging in Wickr IO CLI_**

If you are facing issues with performing any operation using the Wickr IO command line
interface like adding or deploying a custom bot , this procedure will help you view more detailed
debugging information on the command line interface.

**Solution**

To enable debugging, enter `debug` in the CLI.

###### Note

This action will output a lot of debug information with this option enabled.

![Turn debug on.](images/wickr-debug.png)

## Client and Integration compatibility

issues

With the release of new Wickr IO Docker images containing changes to the Wickr IO Add-on
APIs, when you upgrade your container to use the new version, it is possible there will be
compatibility issues that will cause Integrations to not work.

**Solution**

If you are running an officially Wickr supported integration, you will see the
**Needs Upgrade** text on your Wickr IO client.

To upgrade your integration to avoid any compatibility issues, complete the following
steps.

1. Pause the running client using `pause (index)` command.
2. Upgrade the client using `upgrade (index)` command.
3. Start the client again.

If you are using a custom integration, make sure to update your integration to ensure
compatibility with the updated Wickr IO container.

If you need to contact Wickr support it's helpful to have the version number of the Docker
container ready. You can find the version number by using the `version` command in the
Wickr IO command line interface. Additionally, new versions of the Wickr IO Docker image will
display the version numbers of the integrations when you run the `list` command. When
addressing integration issues, having the version numbers for the integrations will also be
beneficial.

## Deploying custom Integrations

**_Cannot import a custom integration_**

If the necessary files are missing from the software.tar.gz imported into the Docker
container, you will receive an "install shell file does not exist" error when starting a Wickr
IO client using your custom integration.

![The custom integration command.](images/wickr-custom-integration.png)

**Solution**

Make sure all the required files are present in the zipped integration software imported in
the docker container. You can use any sample integrations as reference.

## Other issues

**_Exited Docker container_**

Once the Wickr IO container is set up, it is designed to run indefinitely unless stopped
manually. However, unexpected events may occur that could cause your running Docker container to
exit.

**Solution**

- Run docker restart (container-name) to get your container back up.
- Look at Wickr IO client logs to identify the reason for crash. For more information, see
  [Wickr IO clients
  logging](../wickrioguide/logging.md "../wickrioguide/logging.md").
- Check your host’s disk space usage to ensure your host machine has enough disk space to
  support the clients running within the Wickr IO Docker container.

**_Exited Docker container_**

Once you have a running bot client, you should be able to interact(depends on the
integration type) with it on Wickr client application. If the bot is not responding as expected
see the solution below to debug the issue.

**Solution**

- Ensure the Wickr IO client is in `Running` state on the Wickr IO docker
  CLI. You can list all clients and their state using the `list` command.
- If the client is running, then see the integration logs for any errors. For more
  information, see [Wickr IO clients logging](../wickrioguide/logging.md "../wickrioguide/logging.md").

**_Too many bot devices_**

Bot clients do not automatically remove old devices upon start-up. If you frequently move a
bot between different machines, you may reach the limit of 50 devices. Each time you move the bot
to a new device or recreate it, a new device entry is created. Once you reach this limit of 50
devices, the bot may stop functioning properly.

**Solution**

Starting from version 5.81, there are multiple ways to clear out old bot devices. To do
this, you need to modify the bot's `.ini` file. This is a one-time setting that the bot client will
use to eliminate old devices. The setting will specify the number of seconds a bot device has
remained logged in. If a device's last login exceeds this specified duration, it will be
suspended. For example:

```
[oneshot]
suspenddeviceafterseconds=120
```

In the example, you can set the value to 120 seconds (or two minutes). This setting will NOT
affect the current device but will suspend all devices that have not logged in within the
specified time frame. The `.ini` file can be found in the client directory associated with the bot
client. For example:

`/opt/WickrIO/clients/[botname]/WickrIO[botname].ini`

Restart the bot after you have added this to the `.ini` file.

**_Wickr files are not received or
transmitted_**

If the Wickr IO integration you are using requires sending or receiving files but you're
experiencing issues with either, it may be due to an inaccurate date and/or time setting on your
system. Wickr's system relies on the host date and time to transfer encrypted files
successfully. If these setting are incorrect, file transfers will fail.

**Solution**

For accuracy, it's recommended to install and run an NTP (Network Time Protocol) service on
your host system.

**_Network timeouts_**

If your bot is failing to interact with the backend servers and the logs indicate time
errors, there is a way to increase the timeout for network requests. While this may not resolve
the underlying problem, it can help rule out timeout as a cause of connection issues.

**Solution**

To adjust the network timeouts, you'll need to modify the `.ini` file for the bot client. The
`/opt/WickrIO/clients/WickrIO.ini` is the appropriate file.

Add the following below to the `.ini` file:

```
[networksetup]
requesttimeout=[some value in seconds]
userrequesttimeout=[some value in seconds]
```

The `.ini` file is located in the client directory associated with the bot client, for example:

`/opt/WickrIO/clients/[botname]/WickrIO[botname].ini`

Restart the bot after you have added this to the `.ini` file.

## Upgrading bots

The WickrIO bots do not automatically upgrade, like a Wickr client does. You will need to periodically and manually upgrade the bots to make sure you have the latest software.

**Solution**

The following are the steps you will perform to upgrade a WickrIO docker image and the associated bots:

1. Pause the bots that are running on the WickrIO docker container. This is a safety precaution to make sure there are no database corruption problems when you upgrade the container. You will log into the WickrIO CLI and perform the 'pause' command for each bot you have running. After pausing the bots, exit out of the WickrIO CLI (using the <ctrl>p <ctrl>q keyboard sequence).
2. Next, you will kill the current docker container. The following commands will kill the running container and remove it. Notice we named our bot 'MyBotName', you may have named it differently. If you ran the docker container with the appropriate "-v" option your bot data will be safe. The following is an example command:

```
docker kill MyBotName
docker rm -f MyBotName
```

3. Next, you will start the docker container with the new version and use the same options you used to start the old version. The following is an example command:

```
docker run -v /opt/MyBotName:/opt/WickrIO -p 4001:4001 -d --restart=always --name="MyBotName" -ti wickr/bot-cloud:latest
```

4. Next, you will upgrade the bots running on this container. You will need to do that for each of the bots on this container. Log onto the WickrIO CLI, and perform the 'list' command, which will show you the list of bots and identify which ones need to be upgraded. Depending on how old your version is, it is likely all of your bots will require upgrading.
5. Next, for each bot perform the "upgrade" command. It is possible that the configuration tokens associated with the bot integration has changed, if so you will be prompted for the new values.
6. After ensuring all the bots have been upgraded, start each bot. When done starting you can perform the "list" command to verify each bot is running. Once verified, you can exit out of the WickrIO CLI.

The following is sample output from upgrading an old WickrIO bot running version v4.64.9.3, with a wickrio_web_interface bot. The version being upgraded to is the 5.116.18.01 version/tag.

```
Enter command:list
Current list of clients:
 client[0] old-test-bot, State=Running, Integration=wickrio_web_interface
Enter command:version
version: v4.64.9.3
Enter command:pause 0
Do you really want to pause the client with the name old-test-bot (default: yes):yes
Enter command:list
Current list of clients:
 client[0] old-test-bot, State=Paused, Integration=wickrio_web_interface
Enter command:read escape sequence
ubuntu@mybothost:~$
docker kill VeryOldBot
ubuntu@mybothost:~$
docker rm -f VeryOldBot
ubuntu@mybothost:~$
docker run -v /opt/VeryOldBot/WickrIO:/opt/WickrIO -p 4444:4444 -d --restart=always --name="VeryOldBot" -ti wickr/bot-cloud:latest
Unable to find image 'wickr/bot-cloud:latest' locally
5.116.18.01: Pulling from wickr/bot-cloud
4bbfd2c87b75: Already exists
d2e110be24e1: Already exists
889a7173dcfe: Already exists
20ca454721b1: Already exists
02c4b05cb492: Already exists
1c731f8c023d: Already exists
fcd34fc70cfe: Already exists
b1fceb668295: Already exists
68307b81514b: Pull complete
b9f674e60307: Pull complete
e4fd99322c5a: Pull complete
3fdf8c473cd1: Pull complete
9dd71d5d554c: Pull complete
225a5f4a7590: Pull complete
Digest: sha256:05f7d0df8a488f7e325845423d13ebda95b1967b7b00203fe2425ae35e43480f
Status: Downloaded newer image for wickr/bot-cloud:latest
71bb0c85bc4c4c92db604136ad9f64e62d9769debcfccb656794037b4dc06d44
ubuntu@mybothost:~$ docker attach VeryOldBot

Updating integration software version numbers
Updating integration software version numbers
Searching NPM registry
Searching NPM registry

Welcome to the WickrIO Console program (v5.116.18.01)

Current list of clients:
#  Name          Status  Integration            Version  Events  Misc
======================================================================
0  old-test-bot  Paused  wickrio_web_interface  1.1.2    2       Needs Upgrade!
Enter command:
Enter command:upgrade 0
Upgrading from version 1.1.2 to version 5.82.2
Okay to proceed? (default: yes):yes
Copying wickrio_web_interface software

Upgrading wickrio_web_interface software
Installing wickrio_web_interface software
Installing
Installing
Begin configuration of wickrio_web_interface software for old-test-bot
Now using node v12.20.2 (npm v6.14.11)
adminsOptional=false
adminsOptional=false
Finished Configuring package!
Finished Configuring forever!
Finished Configuring!
Enter command:list
Current list of clients:
#  Name          Status  Integration            Version  Events  Misc
======================================================================
0  old-test-bot  Paused  wickrio_web_interface  5.82.2   2
Enter command:start 0
Preparing to start the client with the name old-test-bot
Do you really want to start the client with the name old-test-bot:yes
Enter command:list
Current list of clients:
#  Name          Status   Integration            Version  Events  Misc
=======================================================================
0  old-test-bot  Running  wickrio_web_interface  5.82.2   3
Enter command:
```
