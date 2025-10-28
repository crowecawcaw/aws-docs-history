This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Edit a security group in AWS Wickr

You can edit the details of your Wickr security group.

Complete the following procedure to edit a security group.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, choose the **Admin** link,
   to navigate to Wickr Admin Console for that network.

You're redirected to the Wickr Admin Console for a specific network. 3. In the navigation pane of the Wickr Admin Console, choose
**Network Settings**, and then choose
**Security Group**. 4. Choose **Details** next to the name of the security group
that you want to edit.

The **Security Group Details** page displays the settings
for the security group in different tabs. 5. The following tabs and corresponding settings are available:

    * **Security group name** — Choose the
     pencil icon next to the name of the group to edit the name.
    * **General** — Edit the basic configuration
     of the group.
    * **Messaging** — Manage messaging features
     for members of the group.
    * **Calling** — Manage calling features for
     members of the group.
    * **Security** — Configure additional
     security features for the group.
    * **Federation** — The ability to
     communicate between networks. This can be configured in the Admin
     console for a network at the security group level. AWS Wickr has
     2 types of federation - Local and Global.




    	+ **Local Federation** — The ability
    	 to federate with AWS users in other networks within the same
    	 region. For example, if there are two networks in Canada
    	 with local federation enabled, they will be able to
    	 communicate with each other.
    	+ **Global Federation** — The
    	 ability to federate with either Enterprise users or AWS
    	 users in a different network who belong to other regions.
    	 For example, if there is a user in a network in Canada
    	 region and a user in a network in London region, and Global
    	 federation is turned ON for both networks, they will be able
    	 to communicate with each other.
    	+ **Restricted Federation** — The
    	 ability to federate with specific networks (Enterprise or
    	 AWS) belonging to different regions. Admins can allowlist
    	 specific networks their users can federate with. After the
    	 restriction, users can only communicate with users in the
    	 allowlisted networks. Both networks must allowlist each
    	 other from the security group settings in the federation tab
    	 to use restricted federation.

6. Choose **Save** to save edits that you make to the
   security group details.
