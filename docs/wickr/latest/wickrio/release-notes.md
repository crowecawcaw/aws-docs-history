This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Release Notes

AWS Wickr bots and integrations are regularly updated with new features, improvements, and
bug fixes. This chapter provides information about the changes in each release.

## Version 6.60.05.78 - Release Date: 01/20/2026

The 6.60.05.78 release is a bug fix release and focused on the following major
changes:

### Bug Fix: Enhanced authorization

validation in bot's admin command handling

Admin command handling was found to have limited authorization validation. Changes were
made to prevent unauthorized privilege escalation.

## Version 6.60 - Release Date: 12/08/2025

AWS Wickr Bots 6.60 is a maintenance release focused on platform modernization, security
compliance, and infrastructure improvements. This release includes critical updates to support
Ubuntu 24, Qt 6, and FIPS compliance standards.

## Critical Changes

**Platform Modernization**

- Ubuntu 24 & Qt 6 Upgrade: Major platform modernization for better performance
  - Upgraded to Ubuntu 24 LTS base operating system
  - Migrated to Qt 6 framework
  - Enhanced stability and long-term support

**Security & Compliance**

- FIPS Compliance Support: Added federal security standards compliance
  - Support for Federal Information Processing Standards (FIPS) 140-2/140-3
  - Enables deployment in federal and regulated environments requiring FIPS
    compliance
  - Cryptographic operations can be configured for FIPS mode

- Security Vulnerability Remediation:
  - Fixed known CVEs (Common Vulnerabilities and Exposures)
  - Updated dependencies to address security issues

**Data Standards**

- JSON Data Compliance: Fixed compliance issues with required timestamps and sender/receiver
  information
  - Ensures all message payloads include required timestamp fields
  - Corrected sender and receiver information formatting
  - Improved data consistency across JSON outputs

**Network Connectivity**

- SOCKS5 Proxy Support: Enhanced network connectivity options
  - Added support for SOCKS5 proxy protocol
  - Improved connectivity in restricted or enterprise network environments
  - Enables deployment behind corporate proxies

## Infrastructure Improvements

**Docker Architecture**

- Reorganized container structure for improved maintainability
- Unified FIPS dependency management across containers

**Build System**

- Modernized build processes for improved reliability
- Updated Python dependencies to current versions

**Performance Optimizations**

- Optimized memory usage during bot operations
- Improved database query performance

## Version 6.48 - Release Date: 04/14/2025

The 6.48.04.11 release of the bot-cloud and bot-dataretention-govcloud images are focused on
the changes described below. The 6.48.04.01 bot-compliance-cloud and bot-dataretention-govcloud
images include the CloudWatch metrics bug fix described below.

### Upgrade to Node 20

The bot-cloud and bot-dataretention-govcloud docker images have been upgraded from Node 16
to Node 20. Prior to installing version 6.48 (and above), complete the steps in [Version 6.48 announcement](version-6-48-announcement.md "version-6-48-announcement.md") to update your integrations and avoid disruption.

### Deprecate old integrations

Some of the older and non-supported integrations have been removed from the docker images.
For more information, see [Version 6.48 announcement](version-6-48-announcement.md "version-6-48-announcement.md").

### WickrIO Addon to use ZeroMq

The WickrIO Addon is changed to use ZeroMq for all interactions between integrations and
WickrIO client. This change will make the bot APIs asynchronous. For more information, see [Version 6.48 announcement](version-6-48-announcement.md "version-6-48-announcement.md").

### Bug Fix: Data Retention Bot failing to publish

CloudWatch metrics

Fixed issue where the Data Retention Bot was not publishing metrics to CloudWatch due to a
missing parameter. This fix will ensure that all the required metrics are published successfully
to CloudWatch - if users have CloudWatch configured.

## Version 6.36.20.02 - Hotfix

The 6.36.20.02 hotfix release of the bot-enterprise image and the 6.36.09.01 hotfix release
of Data Retention bot images are focused on the fix described below.

### Bug Fix: The Edit message, delete message and

reactions are not being captured

The Compliance bot and Data Retention are not processing a few types of control
messages:

- Edit Messages: 9000
- Edit Reaction message: 9100
- Delete message: 4011

This hotfix will allow the compliance bot and Data Retention bot to process the above
mentioned control messages and capture them in the receivedMessages files.

## Version 6.36.13.01

The 6.36.13.01 release of the bot-cloud and bot-enterprise images are focused on the changes
described below.

### Add ability to suspend bot devices

Currently there is no way to suspend old bot devices. These changes will by default only
allot 10 devices for each bot. There are two environment variables that allow you to remove
devices older than a specific number of minutes, or change the limit on the number of
devices.

### Better logging for clientConfig.json bad

JSON

Using the clientConfig.json file to automate the start of bots does not generate logs when
there is a failure to parse the JSON. This fix will output errors when failure to parse the JSON
occurs.

### Bug Fix: Sending messages to invalid users could

hang bot

There have been situations where trying to send messages to invalid users will hang a bot.
This has been easily reproducible using the broadcast bot when sending to a list of users in a
file. This fix addresses this issue.

## Version 6.34.05.01

The 6.34.05.01 release of the bot-cloud and bot-enterprise images are focused on the changes
described below. The 6.34.02.01 bot-compliance-cloud images include the File Management and SDK
changes described below.

### Support File Management feature message

formats

The AWS Wickr control message formats were changed to support the AWS Wickr File
Management feature. The 6.34 versions of the WickrIO and WickrIO Compliance releases support
this new message format. The Data Retention / Compliance bots will also download files that are
referred to in these modified control messages. Details of these updated control messages will
be detailed in the appropriate WickrIO documentation.

### Bug Fix: Broadcast Bot security group selection

failed

Some AWS Wickr clients have added spaces padding the security group selection which broke
the broadcast bot processing of that string. Added coding in the broadcast bot to trim the
padding off of the response string.

### Bug Fix: Bug fixes inherited from lower layer

SDK

Several bug fixes were made to the SDK that bots use to interact with the AWS Wickr
servers for login and messaging services. Changes made to improve room membership for room
conversations. Changes made to improve the AWS Wickr client record information more reliable.
Removed some code associated with legacy message sends, which is not used any more.

## Version 6.32.04.02

The 6.32.04.02 release is a bug fix release and focused on the following major
changes:

### Bug Fix: Airgap version contacting NPM Registry

Some code was found to still have references to the default NPM registry
(registry.npmjs.org). Changes were made so the Airgap version does not reference any NPM
registry.

### Bug Fix: Read receipts not working for

Broadcast Bot

Software was found to not be decoding read receipt API call responses correctly. Changes
were made to fix this.

### Bug Fix: Registration failures

A race condition was found which caused initial registrations to fail.

### Bug Fix: Read receipts never time out

Changes were made to stop sending requests for read receipt status after one week for
broadcasts.

## Version 6.24.06.02

The 6.24.06.02 release is focused on the following major changes:

### Bug Fix: Conversations not restored when

creating new instance of bot

Found issue where AWS Wickr conversations were not being restored correctly for new
instances of a bot. This issue would present itself if you created a new instance of a bot and
then tried to send a message from the bot to a secure room or group conversation. The bot would
not have restored the connection list and would not have a record of the conversation.

### Bug Fix: Downloading files in multi-domain

environments

Found issue where the downloading of files from clients in different domains was not
working for bots. This change will make sure files are downloaded when a bot downloads a file
from a AWS Wickr client from another federated domain.

### Bug Fix: Handle files with long file names

When a bot receives a file with a long file name, approximately 255 characters, it adds
some information to the filename which may make the file name larger than 255 characters. The
bot would end up dropping the file in this case, due to operating system limitations. This fix
will remove any characters at the end of the file name to keep the length under 255
characters.

### Feature to send events to AWS Amazon SNS Topic

To improve the health capabilities of AWS Wickr bots we added the ability to send events
generated on a bot to an AWS Amazon SNS Topic. This topic can be used to send events to an email
address or any other endpoint that can subscribe to events pushed to the defined Amazon SNS Topic. To
use this feature there are environment variables (to be defined in the WickrIO documentation)
that identify the AWS Amazon SNS Topic.

### Created new API to set avatar for the bot client

This new bot API allows bot developers to set the avatar associated with the bot client.
Details of this API will be defined in the WickrIO documentation.

## Version 6.18.19.02

The 6.18.19.02 release is focused on the following major changes:

### Continue using AWS Amazon ECR to host Docker images

We are starting to transition hosting our AWS Wickr bot docker images on AWS Amazon ECR.
These are the AWS Amazon ECR repositories used to host the AWS Wickr bot docker images:

public.ecr.aws/x3s2s6k3/wickrio/bot-cloud

public.ecr.aws/x3s2s6k3/wickrio/bot-enterprise

public.ecr.aws/x3s2s6k3/wickrio/bot-compliance-cloud

We will continue to host production docker images on DockerHub for the next couple of
releases.

### Two-way data retention support

The AWS Wickr bot clients will support running with federated networks that are running
data retention. When sending messages to clients in federated data retention active the bot
client will also send the message to the appropriate data retention bot(s).

### Data retention bots support additional user

information

The SAAS data retention bot (bot-compliance-cloud) will output additional information about
the users associated with a message. This new information includes the network ID as well as
room membership.

###### Note

Some of this information is not immediately available to the data retention bot. For the
network ID the data retention bot will need to interact with the server to get the information.
The network ID for a user may not be known by the data retention bot until the server responds
with that information. For the room membership information the data retention bot must capture
room membership control messages that contain the current room membership. The data retention
bot cannot show a valid list of room conversation members unless it sees this information. In
this case an indication of the membership validity will be included with the message
information.

## Version 6.16.19.01

The 6.16.19.01 release is focused on the following major changes:

### Continue using AWS Amazon ECR to host Docker

images

We are starting to transition hosting our AWS Wickr bot docker images on AWS Amazon ECR.
These are the AWS Amazon ECR repositories used to host the AWS Wickr bot docker images:

```
public.ecr.aws/x3s2s6k3/wickrio/bot-cloud
public.ecr.aws/x3s2s6k3/wickrio/bot-enterprise
```

We will continue to host production docker images on DockerHub for the next couple of
releases.

### Update image from Ubuntu 18.04 to Ubuntu 20.04

The Ubuntu operating system version was upgraded to Ubuntu 20.04 in all AWS Wickr bot
docker images.

### Fix message send error issues

If the bot attempted to send a message to a user and that message failed to send the
indication to the bot software was not indicated. The bot software would get into a frozen state
and not able to proceed. This was seen with broadcasts to groups of users where a user account
may be in a bad state where the bot would fail to send to it. The bot would be stuck and not
able to function. This fix handles the error cases appropriately, and in the case of the
broadcast bot the /report command will show the failed users.

### Support for AWS Wickr Multi-Region

All AWS Wickr bot images will support bot clients created in other AWS Regions, for
example ca-central-1.

### Fix Broadcast bot not receiving messages from

users

If the bot sends a message to a user, before the user has sent a message to the bot, the
bot software will not process the message. The creation of the user record in the database was
not attaching to get message indications if the user record was created by the bot sending the
initial message for that user. This can happen, for example, when setting up a broadcast bot
with administrators. The broadcast bot would start by sending a welcome message to all of the
administrators. The user record was not created to receive the incoming message indications, so
the broadcast bot would not respond. In those cases restarting the broadcast bot would fix the
indication for those users. There may be other situations where this happens.

### More user-friendly bot startup failure

indications

If a bot fails to startup the logs indicate this using an error code. To help indicate the
actual reason for the failure a failure string will also be output to the logs.

### Fix issue where bot startups more than 5 attempts

will stop trying to start

If a bot fails to start more than 5 times, normally the bot will not attempt to start again
without some user intervention. In some cases, the bot service will keep trying to start the bot
which could lead to the bot client being suspended or the bot docker image CPU usage elevating
too high. The change will keep the bot service from retrying to start the bot. The bot CLI will
also indicate that there was an error in the Misc column. The CLI will also prompt the user to
make sure they want to start the bot, if it was stopped due to it not starting more than 5
times.

### Update control message to indicate rooms with

saved links and files

Certain control messages did not indicate the filevault information associated with saved
links and files, specifically when new users were added to rooms.

## Version 6.11.05.01

This version is an update for all bots with the move from the forever process manager to the
WPM2 process manager as well as more specific updates to the broadcast bot, compliance bot, bot
client, and wickrio-docs. The 6.11.05.01 release is focused on the following major
changes:

### Using AWS Amazon ECR to host Docker images

We are starting to transition hosting our AWS Wickr bot docker images on AWS Amazon ECR.
These are the AWS Amazon ECR repositories used to host the AWS Wickr bot docker images:

```
public.ecr.aws/x3s2s6k3/wickrio/bot-cloud
public.ecr.aws/x3s2s6k3/wickrio/bot-enterprise
```

We will continue to host production docker images on DockerHub for the next couple of
releases.

### Move from Forever process manager to WPM2

This change affects all bots as they were all using the forever process manager. WPM2 is an
internal project that can be found on NPM at: https://www.npmjs.com/package/wpm2

With WPM2 we rely on the use of PID files to keep track of the running process and the
ability to kill the running process based on the PID (process ID) and WPM2 handles keeping the
bot running and ending the process gracefully when we go to pause or restart the bot. Here is an
example of what the new package.json scripts look like:

```
"restart": "kill $(cat $(cat pidLocation.json)) && nohup wpm2 start --no-metrics ./wpm.json >>wpm2.output 2>&1 & echo $! > $(cat pidLocation.json)",
"start": "nohup wpm2 start --no-metrics ./wpm.json >>wpm2.output 2>&1 & echo $! > $(cat pidLocation.json)",
"stop": "kill $(cat $(cat pidLocation.json))"
```

### Performance improvement for large

broadcast

Performance has been improved for large broadcasts in the broadcast bot. The pre-send
preparation of the broadcast bot will see an obvious increase in performance for large
broadcasts.

### Updating the Support email in all the bots

In any bots and documentation that made reference to AWS Wickr support we were using the
old support@wickr.com email. All these instances have been updated to the new support email:
wickr-support@amazon.com.

### Updated JSON timestamp

An ISO format timestamp has been added for message JSON. This was done in the compliance
bot and all messages passed to bots and integrations.

### Mutex Lock Enhancements

Mutex lock enhancements have been made to reduce the possibilities of database
lockups.

## Version 5.116.19.02

This version is a bug fix release.

### Fix for Enterprise updated password not

showing

This version of the enterprise docker image(s) will fix an issue where the changed password
was not being shown if you run the "debug on" command and then the "debug off" command on the
CLI. The debug state was not being set correctly to off when the "debug off" command was
performed, which caused a problem processing the messages from the provisioning software. The
debugging output was stopped but the internal state was not updated appropriately.

## Version 5.116.18.01

This version is an update for the wickr/bot-enterprise and the wickr/bot-cloud Docker
images. The 5.116.18.01 release is a patch release. Please see the Version 5.116.13.01 Release
notes for details of the 5.116 version. This version includes the following changes:

### Fix for Missing Rooms

A bug was detected when upgrading to the 5.112 or 5.112.13.01 releases of the WickrIO Bots,
which made secure room and group conversations not visible to bots/integrations. These
conversations were not deleted they were not being made visible to the bot APIs. This release
fixes these issues.

### Fix for upgrades from old bot versions

This issue was seen when an upgrade was performed from an old version of the WickrIO docker
image, specifically 5.62.05.02. The issue was caused by a new database field not being added
during the migration from the old version to the recent version (i.e. 5.112 or 5.116).

To identify if your bot is experiencing this issue, the log files will contain a failure
message when ever the bot receives a message. The failure message will contain the following
text and can be seen in the WickrIO<botname>.output file:

```
BULK INSERT MESSAGE: Failed, can't prepare insertQuery
```

### Fix to address high CPU

Several customers have reported WickrIO bots randomly running at high CPU rates, and
staying at that rate. We have reproduced the problem. This patch release contains a change that
has shown to eliminate this problem. If you have seen this issue and want to confirm it is the
same CPU issue please do the following:

- run the following command which will start a bash shell inside the docker image.

```
docker exec -ti <dockerimagename/id> bash
```

- run the "top" command which will show you the processes running inside the docker image.
  The process at the top of the list will have the highest CPU value.
- The process at the top of the list should be the "wickrio_bot" process, if it is the
  problem we are trying to solve.

###### Note

If you continue to have the CPU issue after installing this patch, please contact
support.

### Fix for SAAS Data Retention Network Transmit

Failures

The 5.116.13.01 wickr/bot-cloud image would have transmit failure when operating in a SAAS
Data Retention network. This version will fix that problem.

## Version 5.116.13.01

This version is an update for the wickr/bot-enterprise and the wickr/bot-cloud Docker
images. The 5.116.13.01 release is focused on the following two major changes:

### Support for Mac M1 Host

Changes made to support running on Mac M1 machines. Older versions of the WickrIO Docker
images will not run on the Mac M1 systems.

If you want to run the WickrIO Docker image(s) on a Mac M1 machine, you will have to start
the Docker images with the —platform=linux/amd64 option.

We do not recommend running production bots on Mac M1 hardware at this point. Using Mac M1
systems to do development should be fine.

### Support for Node 16

As of the 5.116.13.01 version, all of the Docker images and software are updated to use
node version 16. Node 12 is not supported anymore and will NOT be part of the 5.116.13.01 Docker
images. All of the bots and integrations shipped with the 5.116.13.01 Docker images have been
updated to use Node 16. When you update your WickrIO Docker images to the 5.116.13.01 version,
you will need to upgrade all bots and integrations to use the latest versions. Any bots that use
Node 12 will not work when the 5.116.13.01 version is installed. The bot client will operate and
show that it is running, but the bot/integration software will not be able to start up since
they will be looking for Node 12. The 5.116.13.01 WickrIO Docker images contain upgrades for all
of the supplied bots.

#### Custom Bots/Integrations

This section applies to you if you have or are developing custom Node-js bots. This does
not apply to anyone using the REST APIs of the wickrio_web_interface bot.

If you are creating custom bots/integrations you will need to use the latest 5.113 version
of the wickrio-bot-api or the the latest 5.113 version of the wickrio_addon (which ever is
appropriate for your custom bot).

### Installation Process

We recommend that before you install the new 5.116.13.01 version of the appropriate Docker
image that you pause all of the bots running on each Docker instance. Using the WickrIO CLI you
should see your bot(s) in the "Paused" state.

```
Enter command:read escape sequence
ubuntu@ip-172-31-25-75:~$ docker attach bot_test_prod
Enter command:
Enter command:list
Current list of clients:
# Name Status Integration Version Events Misc
0 dev-test-bot Paused wickrio-compliance-bot 5.112.1 53
Enter command:
```

After you start the Docker image with the 5.116.13.01 version the CLI will show that your
bot has a needed upgrade available:

```
Welcome to the WickrIO Console program (v5.116.13.01)

Current list of clients:
# Name Status Integration Version Events Misc
0 dev-test-bot Paused wickrio-compliance-bot 5.112.1 43 Needs Upgrade!
```

Please make sure you upgrade each of your bots to the latest version. The following is a
sample of what upgrading a compliance bot would look like. The software will be upgraded and you
will be prompted to enter the configuration information for the bot (previously configured
values are shown in the parenthesis).

### FAQ

**Question:** Will my bots be running if I don't want to
upgrade?

**Answer:** Your bots will continue to run if you do not
upgrade to the 5.116.13.01 version. However, we recommend upgrading to receive the latest
security updates.

**Question:** If I run into problems with the 5.116.13.01
version can I downgrade my installation?

**Answer:** Yes you can. The process is very similar to how
you upgraded to the 5.116.13.01 version. Instead you will do the following:

- pause the bots running on the Docker instance
- start the older Docker image
- use the CLI's 'upgrade' command to install the version of the bot software on the older
  Docker instance.
- start the bots
