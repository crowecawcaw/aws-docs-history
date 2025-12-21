This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Edit a security group in AWS Wickr

You can edit the details of your Wickr security group.

Complete the following procedure to edit a security group.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose **Security
   groups**.
4. Select the name of the security group that you want to edit.

The security group details page displays the settings for the security
group in different tabs. 5. The following tabs and corresponding settings are available:

    * **Security group details** — Choose
     **Edit** in the **Security group
     details** section to edit the name.
    * **Messaging** — Manage messaging features
     for members of the group.




    	+ **Burn-on-read** — Controls the
    	 maximum value that users can set for their burn-on-read
    	 timers in their Wickr clients. For more information, see
    	  [Set
    	 message expiration and burn timers in the Wickr
    	 client](../userguide/message-timers.md "../userguide/message-timers.md").
    	+ **Expiration timer** — Controls
    	 the maximum value that users can set for their message
    	 expiration timer in their Wickr clients. For more
    	 information, see  [Set
    	 message expiration and burn timers in the Wickr
    	 client](../userguide/message-timers.md "../userguide/message-timers.md").
    	+ **Message forwarding** — Controls
    	 whether users can forward messages in their Wickr clients.
    	 For more information, see [Forward messages in the Wickr client](../userguide/message-forwarding.md "../userguide/message-forwarding.md").
    	+ **Quick responses** — Set a list
    	 of quick responses for users to respond to messages.
    	+ **Secure shredder intensity** —
    	 Configure how frequently the secure shredder control runs
    	 for users. For more information, see [Messaging](../enterpriseadminguide/messaging.md "../enterpriseadminguide/messaging.md").
    * **Calling** — Manage calling features for
     members of the group.




    	+ **Enable audio calling** — Users
    	 can initiate audio calls.
    	+ **Enable video calling and screen
    	 sharing** — Users can start video calls
    	 or share screen during call.
    	+ **TCP calling** — Enabling (or
    	 forcing) TCP calling is typically used when standard VoIP
    	 UDP ports are disallowed by an organization's IT or security
    	 department. If TCP calling is disabled, and UDP ports are
    	 not available for use, Wickr clients will try UDP first
    	 and fallback to TCP.
    * **Media and links** — Manage settings
     related to media and links for members of the group.


    **File download size** — Select
     **Best quality transfer** to allow users to
     transfer files and attachments in their original encrypted form. If
     you select **Low bandwidth transfer**, file
     attachments sent by users in Wickr will be compressed by the
     Wickr file transfer service.
    * **Location** — Manage location sharing
     settings for members of the group.


    **Location sharing** — Users can share
     their locations using GPS-enabled devices. This feature displays a
     visual map based on the device's operating system defaults. Users
     have the option to disable the map view and share a link containing
     their GPS coordinates instead.
    * **Security** — Configure additional
     security features for the group.




    	+ **Enable account takeover protection**
    	 — Enforce a two-factor authentication when a user
    	 adds a new device to their account. To verify a new device,
    	 user can generate a Wickr code from their old device, or
    	 perform an email verification. This is an additional layer
    	 of security to prevent unauthorized access to AWS Wickr
    	 accounts.
    	+ **Enable always re-authenticate**
    	 — Force users to always re-authenticate when
    	 re-entering the application.
    	+ **Master recovery key** — Creates
    	 a Master recovery key when an account is created. Users can
    	 approve the addition of a new device to their account if no
    	 other devices are available.
    * **Notification and visibility** —
     Configure notification and visibility settings such as message
     previews in notifications for members of the group.
    * **Wickr open access** — Configure
     Wickr open access settings for members of the group.




    	+ **Enable Wickr open access** —
    	 Enabling Wickr open access will disguise traffic to
    	 protect data on restricted and monitored networks. Based on
    	 geographic location, Wickr open access will connect to
    	 various global proxy servers that provide the best path and
    	 protocols for traffic obfuscation.
    	+ **Force Wickr open access** —
    	 Automatically enables and enforces Wickr open access on
    	 all devices.
    * **Federation** — Control your users
     ability to communicate with other Wickr networks.




    	+ **Local federation** — The ability
    	 to federate with AWS users in other networks within the
    	 same region. For example, if there are two networks in AWS
    	 Canada (Central) Region with local federation enabled, they will
    	 be able to communicate with each other.
    	+ **Global federation** — The
    	 ability to federate with either Wickr Enterprise users or
    	 AWS users in a different network who belong to other
    	 regions. For example, a user on a Wickr network in AWS
    	 Canada (Central) Region, and a user in a network in AWS
    	 Europe (London) Region will be able to communicate with each other
    	 when global federation is turned **ON** for
    	 both networks.
    	+ **Restricted federation** — Allow
    	 list specific AWS Wickr or Wickr Enterprise networks
    	 that users can federate with. When configured, users can
    	 only communicate with external users in allow listed
    	 networks. Both networks must allow list each other to use
    	 restricted federation.


    	For information on guest federation, see  [Enable or disable guest users in AWS Wickr
    	 network](guest-users-enable-disable.md "guest-users-enable-disable.md").
    * **ATAK plugin configuration** — For more
     information on enabling ATAK, see  [What is
     ATAK?](what-is-atak.md "what-is-atak.md").

6. Choose **Save** to save edits you make to the security
   group details.
