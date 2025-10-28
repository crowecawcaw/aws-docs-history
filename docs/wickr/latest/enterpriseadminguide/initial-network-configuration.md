This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Initial network configuration

Once the **bot-enterprise** container is running and have a working
deployment of Wickr Enterprise you can begin adding a bot user and completing the setup
process. Setup is comprised of four steps:

1. Adding additional administrators
2. Naming the network
3. Adding a compliance bot
4. Adding users

## Network dashboard setup

In this section, we show you how to setup your network dashboard.

Complete the following procedure to create a network administrator.

1. Once you login to Wickr Enterprise, you will see the **Admins**
   page.
2. On the **Admins** page, choose **Create Admin** to
   create a network admin account.
3. Once your network admin account has been created, choose **Sign Out**,
   and then sign in under the new account.

## Creating a compliance bot user

Once you sign into the Wickr Administrator Console, you can create a compliance bot
user.

**To create a compliance bot user**

1. In the navigation pane, choose **User** and then choose
   **Compliance Bot**.
2. Enter your **Username**. The username is unique for each bot. We
   recommend matching the network name in some fashion in the event you use multiple bots.
3. Enter your **Password**. The password is only used once during the bot
   setup process, so it’s safe to make this generic.
4. Choose **Submit**.

## Configuration file

After creating a bot user, it's time to create the configuration file it will use to
connect to your Wickr Enterprise deployment.

**To create a configuration file**

1. In the navigation pane, choose **User** and then choose
   **Compliance Bot**.
2. Choose **Create New Config**
3. On the **Create Configuration File** page, select the **Security
   Group**.
4. Select the **Expiration Period**. The expiration period should be no
   longer than one day to allow sufficient time to complete the compliance setup process.
5. Enter a **Password**. This password is solely for the configuration file
   and an expiration time.
6. Choose **Create**.
7. Choose **Download Configuration File** to download the
   `config.wickr` file.

## Server-side bot setup

Once you have the `config.wickr` file, you’ll need to upload it to the
compliance server to begin the server setup.

See the example setup below with annotations.

```
$ sudo mv conf.wickr /opt/WickrIO
$ docker attach wickr-compliance

Enter command: add
 Enter the user name: compliancebot  (`1` The username created from Creating a compliance bot user.)

Enter the password: ********  (`2` The password created from Creating a compliance bot user.)
Enter config file: /opt/WickrIO/conf.wickr
Enter the config file password: ********  (`3` The password created from Configuration file.)
Creating user: "compliancebot"

********************************************************************
**** GENERATED PASSWORD
**** DO NOT LOSE THIS PASSWORD, YOU WILL NEED TO ENTER IT EVERY TIME
**** TO START THE BOT
**** "Ft1MAC0FUaE1DiS67J8WN8nt" (`4` The password the bot will use going forward. **It's very important to save this password.**)
********************************************************************
Begin registration with password.

Successfully created user
****************************************************************
 **** USER SIGNING KEY
 **** You will need this to enter into the console for the Bot
 ****
"00040002f9abe40c27c8b29c14cfa014db29c02c53b72bcb11b5e6657414b89101574f531c772fae84966
0defc4dddb3115eb34acba654f8d5eda00edbcb75da08f398d901e4a2f95cdd9f519f236b3f541b6af282f
ac0d89f3524da0cb79d202f37212ec8b08ab319e84da6c0e6214205b95cbff43a7dc3a1ba5e30e434a117b
884f51354fc"  (`5` The password created from Configuration file.)
****************************************************************
 Successfully logged in as new user!
 Our work is done here, logging off!
 Return code from provision is: 0

The autologin capability allows you to start a bot without having to enter the
password, after the initial login.
NOTE: The bot client's password is NOT saved to disk.

Do you want to use autologin? (default: yes): yes (`6` The autologin will have your compliance bot user login automatically if disconnected.)

These integrations are local:
  - wickrio-calendar-bot
  - wickrio-example-app
  - wickrio-zendesk-bot
  - wickrio-file-bot
  - wickrio-compliance-bot  (`7` If this isn't the default option, please enter `wickrio-compliance-bot`.)
  - wickrio_web_interface
  - wickrio-broadcast-bot
  - core_bot
  - wickrio-monitor-bot
  - hubot
  - wickrio-user-engagement-bot
  - wickrio-hello-world-bot
These integrations are from the NPM registry:
  - wickrio-alias-bot

Please enter one of:
  - The full integration name from the list above
  - The word "search" to search the NPM registry for an integration
  - The word "import" to import an integration
  - The word "quit" to cancel adding the bot

Enter the bot integration to use:wickrio-compliance-bot
**********************************************************************
Begin setup of wickrio-compliance-bot software for compliance-bot
Copying wickrio-compliance-bot software

Installing wickrio-compliance-bot software
Installing
Installing



```

## Configuring the compliance integration

As of version 5.56, the Compliance integration has these extra options:

- Logs saved to alternate locations
- Output file prefix
- Size based log rotation
- Attachments saved to alternate location
- Automatic service restart

**Compliance Configuration Options**

See the example setup below with annotations.

```
Begin configuration of wickrio-compliance-bot software for compliance-bot
 Use new file save process [yes/no]: (no) :yes (`1` Entering **No** will use the previous settings and options.)
Please specify the directory to save message data: (/opt/WickrIO/clients/compliance-
bot/integration/wickrio-compliance-bot/messages) : (`2` The directory specified must be writable and in the current mount point.)
Please add a prefix for message data files: (receivedMessages) : (`3` This sets a prefix on log files that are rotated.)
Please enter the maximum size in bytes for each messages file [1GB = 1073741824]:
(1073741824) : (`4` This sets the size limit on log files.)
Please specify the directory to save attachment data:
(/opt/WickrIO/clients/compliance-bot/integration/wickrio-compliance-bot/attachments)
: (`5` The directory specified here must be writable and in the current mount point.)
Memory can reach 100% if the bot isn't restarted periodically. Please enter a time in
 minutes to restart the service [24hrs = 1440]: (1440) : (`6` The integration will restart at a regular interval set here.)
Finished Configuring!

Integration files written to:
/opt/WickrIO/clients/compliance-bot/integration/wickrio-compliance-bot (`7` This directory will house all configuration and necessary files for the compliance service.)

End of setup of wickrio-compliance-bot software for compliance-bot
**********************************************************************
Successfully added record to the database!
Enter command:



```

## Starting the compliance bot

The last step is starting the bot you just configured. Use the `start` command
as described here:

```
Enter command: start
 Do you really want to start the client with the name compliancebot: y
Enter password for this client: ************** (`1` The generated password created from Server-side bot setup.)



```

## Other commands

The following table describes the other commands besides **add** and
**start**.

| Command              | Description                                                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| list                 | The list command will show all active or inactive bots.                                                                                                 |
| delete (bot number)  | Delete removes a bot from your system. If you have more than one, use the number shown from the list command to specify which bot you’d like to delete. |
| pause (bot number)   | Pause temporarily stops a running bot.                                                                                                                  |
| restart (bot number) | Restart will restart a bot.                                                                                                                             |
