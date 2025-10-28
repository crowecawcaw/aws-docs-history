This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Compliance container upgrades

If already running the compliance bot within a container, the upgrade process is very simple
and will not result in any downtime. Any messages received while the bot is offline will be
downloaded once the new version is up and running.

Follow the setup below to pause the compliance bot:

```
$ docker attach wickr-compliance
Continue to see welcome message on startup? (default: yes):
Current list of clients:
 client[0] compliancebot, State=Running, Integration=compliance_bot

pause 0



```

###### Note

To exit the foreground mode use the following key combination: **Ctrl** +
**P** and then **Ctrl** + **Q**.

Stop the current container:

```
$ docker stop wickr-compliance


```

You will now need to rename (or remove) the old container. Renaming is safest if you decide
you need to roll back, but removing the container will save on disk space in the long run.

```
$ docker rename wickr-compliance old-compliance-bot
```

**OR**

```
$ docker rm wickr-compliance
```

Once the old container is renamed, you can start the new container:

```
$ docker run `-v` /opt/WickrIO:/opt/WickrIO `-d —name` wickr-compliance `—restart`=always \
-ti public.ecr.aws/x3s2s6k3/wickrio/bot-enterprise:latest

```

Now you can **attach** to continue the upgrade.

```
$ docker attach wickr-compliance
```

```
Enter command:list
Current list of clients:
#  Name            Status  Integration             Version Misc
=======================================================================================
0  compliance_bot  Paused  wickrio-compliance-bot  6.18    Needs Upgrade!


```

Next upgrade the integration code:

```
Enter command:upgrade 0
Upgrading from version 0.1000.0 to version 5.44.9
Okay to proceed? (default: yes):yes
Searching NPM registry
Searching NPM registry
Searching NPM registry
Searching NPM registry
Searching NPM registry
Searching NPM registry
Copying wickrio-compliance-bot from the NPM registry
Upgrading wickrio-compliance-bot software
Installing wickrio-compliance-bot software
Installing
Begin configuration of wickrio-compliance-bot software



```

The bot is now ready to run. Use the **list** command to make sure the bot
is running. If it isn't running, you can start it with the following command:

```
Enter command:start 0
```

Now the log can be tailed to make sure new messages are captured.

```
$ cd/opt/WickrIO/clients/compliance/integration/wickrio-compliance-bot
$ tail receivedMessages.log
{`"id"`:`"d59ce4c0e16c11e98dd1cb32338ed079"`,`"message"`:`"test"`,`"msg_ts"`:`"1569619316.805649"`
,`"msgtype":1000`,`"receiver"`:`"user1"`,`"sender"`:`"user3"`,`"time"`:`"9/22/19 9:21 PM"`
,`"vgroupid"`:`"083983510e793950fabd97774979089ed550b02c00b63f8c52bc525c4afbb9a4"`}


```

If you see new messages, the upgrade is successful. If you’re not seeing new messages,
you’ll need to make sure your bot is in the **Running** state. You may need to
stop and start the bot again to provide the password. If you see any issues, please contact
[Wickr support](https://wickr.com/contact-us/ "https://wickr.com/contact-us/").

###### Note

If your bot is offline, it will store messages server-side and download them once back
online, ensuring no messages will be lost.
