# Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications

To stream your applications, Amazon WorkSpaces Applications requires an environment that includes a fleet that is associated with a stack, and at least one application image. This tutorial describes how to configure a
sample WorkSpaces Applications environment for application streaming and give users access to that stream.

###### Note

For additional guidance in learning how to get started with WorkSpaces Applications, see the [Amazon WorkSpaces Applications Getting
Started Guide](https://aws.amazon.com/appstream2/stream-desktop-applications/ "https://aws.amazon.com/appstream2/stream-desktop-applications/"). This guide describes how to install and configure two
applications, perform foundational administrative tasks using the WorkSpaces Applications console, and provision
an Amazon Virtual Private Cloud by using a provided AWS CloudFormation template.

###### Tasks

- [Step 1: Set Up a Sample Stack, Choose an Image, and Configure a Fleet](#getting-started-stack "#getting-started-stack")
- [Step 2: Provide Access to Users](#getting-started-access "#getting-started-access")
- [Resources](#getting-started-next "#getting-started-next")

## Step 1: Set Up a Sample Stack, Choose an Image, and Configure a Fleet

Before you can stream your applications, you need to set up a stack, choose an image that has applications installed, and configure a fleet. In this step, you use a template to help simplify these tasks.

###### To set up a sample stack, choose an image, and configure a fleet

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. Choose **Get Started** if you are new to the console, or
   **Quick Links** from the left navigation menu. Choose
   **Set up with sample apps**.
3. For **Step 1: Stack Details**, keep the default stack name or
   enter your own. Optionally, you can do the following:
   - **Display name** — Enter a name to display for
     the stack (maximum of 100 characters).
   - **Description**— Keep the default description
     or enter your own (maximum of 256 characters).
   - **Redirect URL** — Specify a URL to which users
     are redirected after their streaming sessions end.
   - **Feedback URL** — Specify a URL to which users
     are redirected after they click the **Send Feedback**
     link to submit feedback about their application streaming experience. If
     you do not specify a URL, this link is not displayed.
   - **Streaming Protocol Preference** — Specify the
     streaming protocol you’d like your stack to prefer, UDP or TCP. UDP is
     currently only supported in the Windows native client. For more
     information, see [System Requirements and Feature Support (WorkSpaces Applications Client)](client-system-requirements-feature-support.md "client-system-requirements-feature-support.md").
   - **Tags** — Choose **Add Tag**,
     and type the key and value for the tag. To add more tags, repeat this
     step as needed. For more information, see [Tagging Your Amazon WorkSpaces Applications Resources](tagging-basic.md "tagging-basic.md").
   - **VPC Endpoints (Advanced)** — You can create a
     private link, which is an [interface VPC endpoint](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") (interface endpoint), in your
     virtual private cloud (VPC). To start creating the interface endpoint,
     select **Create VPC Endpoint**. Selecting this link
     opens the VPC console. To finish creating the endpoint, follow steps 3
     through 6 in _To create an interface endpoint_, in
     [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md "creating-streaming-from-interface-vpc-endpoints.md").

   After you create the interface endpoint, you can use it to keep
   streaming traffic within your VPC.
   - **Embed WorkSpaces Applications (Optional)** — To embed an
     WorkSpaces Applications streaming session in a webpage, specify the domain to host the
     embedded streaming session. Embedded streaming sessions are only
     supported over HTTPS [TCP port 443].

   ###### Note

   You must meet prerequisites and perform additional steps to
   configure embedded WorkSpaces Applications streaming sessions. For more information,
   see [Embed Amazon WorkSpaces Applications Streaming Sessions](embed-streaming-sessions.md "embed-streaming-sessions.md").

4. Choose **Next**.
5. For **Step 2: Choose Image**, a sample image is already selected. The image contains pre-installed open-source applications for evaluation purposes. Choose **Next**.
6. For **Step 3: Configure Fleet**, we recommend that you keep
   any default values that are provided. You can change most of these values after
   fleet creation.
   - **Choose instance type** — Choose the instance type
     that matches the performance requirements of your applications. All streaming
     instances in your fleet launch with the instance type that you select. For
     more information, see [WorkSpaces Applications Instance Families](instance-types.md "instance-types.md").
   - **Fleet type** — Choose the fleet type that suits
     your use case. The fleet type determines its immediate availability and
     how you pay for it.
   - **Maximum session duration in minutes** — Choose the maximum amount of time that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
   - **Disconnect timeout in minutes** — Choose the amount of time that a streaming session should remain active after users disconnect. If users try to reconnect to the streaming instance after a disconnection or network interruption within this time interval, they are connected to the previous session. Otherwise, they are connected to a new session with a new instance. If you associate a stack with a fleet for which a redirect URL is specified, after users’ streaming sessions end, the users are redirected to that URL.

   If a user ends the session by choosing **End Session** on the streaming session toolbar, the disconnect timeout does not apply. Instead, the user is prompted to save any open documents, and then immediately disconnected from the streaming instance.
   - **Idle disconnect timeout in minutes** — Choose the amount of time that
     users can be idle (inactive) before they are disconnected from their
     streaming session and the **Disconnect timeout in
     minutes** time interval begins. Users are notified before they are
     disconnected due to inactivity. If they try to reconnect to the
     streaming session before the time interval specified in **Disconnect
     timeout in minutes** has elapsed, they are connected to
     their previous session. Otherwise, they are connected to a new session
     with a new streaming instance. Setting this value to 0 disables it. When
     this value is disabled, users are not disconnected due to
     inactivity.

   ###### Note

   Users are considered idle when they stop providing keyboard or mouse input during their
   streaming session. File uploads and downloads, audio in, audio out,
   and pixels changing do not qualify as user activity. If users
   continue to be idle after the time interval in **Idle
   disconnect timeout in minutes** elapses, they are
   disconnected.
   - **Multiple user sessions** — Choose this option
     if you want to provision multiple user sessions on a single instance. By
     default, every unique user session is served by an instance
     (single-session).

   ###### Note

   Multi-session is available only on Always-on and On-demand fleets
   powered by a Windows operating system. Multi-session is not
   available on Elastic fleets or the Linux operating system.

   Make sure you are using latest WorkSpaces Applications images for multi-session
   fleets. To keep your images are up-to-date, see [Keep Your Amazon WorkSpaces Applications Image Up-to-Date](keep-image-updated.md "keep-image-updated.md"). For details on supported images
   and WorkSpaces Applications agent versions for multi-session, see [WorkSpaces Applications Base Image and Managed Image Update
   Release Notes](base-image-version-history.md "base-image-version-history.md").
   - **Maximum sessions per instance** — Maximum
     number of user sessions on an instance. You must choose this value based
     on your end users' application performance needs. You can also adjust
     the maximum sessions per instance for a fleet after it is provisioned.
     In that case, the existing user sessions and instances will not be
     impacted, but the fleet will become consistent with the new value of
     maximum sessions per instance. The value must be between 2 and 50.
     Before setting this value for your fleet, see [Multi-Session Recommendations](multi-session-recs.md "multi-session-recs.md").
   - **Minimum capacity** — Choose a minimum number of instances
     for your fleet based on the minimum number of expected concurrent users. Every
     unique user session is served by an instance. For example, to have your stack support
     100 concurrent users during low demand, specify a minimum capacity of 100. This
     ensures that 100 instances are running even if there are fewer than 100 users.
   - **Maximum capacity** — Choose a maximum number of instances
     for your fleet based on the maximum number of expected concurrent users. Every unique
     user session is served by an instance. For example, to have your stack support
     500 concurrent users during high demand, specify a maximum capacity of 500. This
     ensures that up to 500 instances can be created on demand.
   - **Minimum user sessions for fleet** — Choose a
     minimum number of user sessions for your fleet based on the minimum
     number of expected concurrent users. For example, to have your stack
     support 100 concurrent users during low demand, specify a minimum
     capacity of 100. This ensures that 100 user sessions are available even
     if there are fewer than 100 users.
   - **Maximum user sessions for fleet** — Choose a
     maximum number of user sessions for your fleet based on the maximum
     number of expected concurrent users. For example, to have your stack
     support 500 concurrent users during high demand, specify a maximum
     capacity of 500. This ensures that up to 500 user sessions can be
     provisioned on demand.

   ###### Note

   For a single-session fleet, one instance will be launched of every
   user session. However, for multi-session, the number of running
   instances depends on the maximum sessions per instance. You must
   provide the capacity in terms of user sessions. The service will
   decide how many instances are required based on your fleet type
   (multi-session or single-session) and maximum sessions per
   instance.
   - **Scaling details** — Specify the scaling policies that WorkSpaces Applications uses to
     increase and decrease the capacity of your fleet. Note that the size of
     your fleet is limited by the minimum and maximum capacity that you
     specified. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md "autoscaling.md").
   - **IAM role (Advanced)** — When you apply an IAM role from your account
     to an WorkSpaces Applications fleet instance, you can make AWS API requests from the
     fleet instance without manually managing AWS credentials. To apply an
     IAM role, do either of the following:
     - To use an existing IAM role in your Amazon Web Services account, choose the role that you want to use from the **IAM role** list. The role must must be accessible from the fleet instance. For more information, see [Configuring an Existing IAM Role to Use With WorkSpaces Applications Streaming Instances](configuring-existing-iam-role-to-use-with-streaming-instances.md "configuring-existing-iam-role-to-use-with-streaming-instances.md").
     - To create a new IAM role, choose **Create new IAM role** and follow the steps in [How to Create an IAM Role to Use With WorkSpaces Applications Streaming Instances](how-to-create-iam-role-to-use-with-streaming-instances.md "how-to-create-iam-role-to-use-with-streaming-instances.md").

7. Choose **Next**.
8. For **Step 4: Configure Network**, a default VPC is provided. This VPC includes a default public subnet in each Availability Zone and an internet gateway that is attached to your VPC. The VPC also includes a default security group. To use the default VPC configuration, do the following:
   - Keep the **Default Internet Access** check box selected.

   When **Default Internet Access** is enabled, a maximum of 100 fleet instances is supported. If your deployment must support more than 100 concurrent users, use the [NAT gateway configuration](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md") instead.
   - For **VPC**, keep the default VPC selected for your AWS Region.

   The default VPC name uses the following format: `vpc-``vpc-id``(No_default_value_Name)`.
   - For **Subnet 1** and **Subnet 2**, keep the default public subnets selected.

   The default subnet names use the following format: `subnet-``subnet-id` `|
 (``IPv4 CIDR block``) |
 Default in` `availability-zone`.
   - For **Security groups**, keep the default security group selected.

   The default security group name uses the following format: `sg-``security-group-id``-default`.

9. For **Step 5: Enable Storage**, choose one or more of the
   following, then choose **Next**.

###### Note

Google Drive and OneDrive options are currently not available for
multi-session fleets.

    * **Enable Home Folders** — By default, this setting is enabled. Keep the default setting. For information about requirements for enabling home
     folders, see [Enable Home Folders for Your WorkSpaces Applications
     Users](enable-home-folders.md "enable-home-folders.md").
    * **Enable Google Drive** — Optionally, you can enable users to link
     their Google Drive for G Suite account to WorkSpaces Applications. You can enable Google
     Drive for accounts in G Suite domains only, not for personal Gmail
     accounts. For information about requirements for enabling Google Drive,
     see [Enable Google Drive for Your WorkSpaces Applications
     Users](enable-google-drive.md "enable-google-drive.md").
    * **Enable OneDrive** — Optionally, you can
     enable users to link their OneDrive for Business account to WorkSpaces Applications. You
     can enable OneDrive for accounts in OneDrive domains only, not for
     personal accounts. For information about requirements for enabling
     OneDrive, see [Enable OneDrive for Your WorkSpaces Applications Users](enable-onedrive.md "enable-onedrive.md").

10. For **Step 6: User Settings**, configure the following settings. When you're done,
    choose **Review**:

**Clipboard, file transfer, print to local device, and authentication permissions options**:

###### Note

**Print to local device** and **Smart card sign
in for Active Directory** are currently not available for
multi-session fleets.

    * **Clipboard** — By default, users can copy and
     paste data between their local device and streaming applications. You
     can limit Clipboard options so that users can paste data to their remote
     streaming session only or copy data to their local device only. You can
     also disable Clipboard options entirely. Users can still copy and paste
     between applications in their streaming session. You can choose
     **Copy to local device character limit** or
     **Paste to remote session character limit** or both
     to limit the amount of data that users can copy or paste when using the
     clipboard, either in or out of their WorkSpaces Applications streaming session. The value
     can be between 1 and 20,971,520 (20 MB), and defaults to the maximum
     value when unspecified.
    * **File transfer** — By default, users can
     upload and download files between their local device and streaming
     session. You can limit file transfer options so that users can upload
     files to their streaming session only or download files to their local
     device only. You can also disable file transfer entirely.


    ###### Important

    If your users require WorkSpaces Applications file system redirection to access local drives and folders during their streaming sessions, you must enable both file upload and download. To use file system redirection, your users must have WorkSpaces Applications client version 1.0.480 or later installed. For more information, see [Enable File System Redirection for
     Your WorkSpaces Applications Users](enable-file-system-redirection.md "enable-file-system-redirection.md").
    * **Print to local device** — By default, users can print to their local device from within a streaming application. When they choose **Print** in the application, they can download a .pdf file that they can print to a local printer. You can disable this option to prevent users from printing to a local device.
    * **Password sign in for Active Directory** —
     Users can enter their Active Directory domain password to sign in to an WorkSpaces Applications streaming instance that is joined to an Active Directory domain.



    You can also enable **Smart card sign in for Active Directory**. At least one authentication method must be enabled.
    * **Smart card sign in for Active Directory** —
     Users can use a smart card reader and smart card connected to their
     local computer to sign in to an WorkSpaces Applications streaming instance that is joined
     to an Active Directory domain.


    You can also enable **Password sign in for Active Directory**. At least one authentication method must be enabled.

###### Note

**Clipboard, file transfer, and print to local device settings** — These settings control only whether users can use WorkSpaces Applications data transfer features. If your image
provides access to a browser, network printer, or other remote resource,
your users might be able to transfer data to or from their streaming session
in other ways.

**Authentication settings** — These settings control only the authentication method that can be used for Windows sign in to an WorkSpaces Applications streaming instance (fleet or image builder). They do not
control the authentication method that can be used for in-session authentication, after a user signs in to a streaming instance. For information about configuration requirements for using smart cards for Windows sign in and in-session authentication, see [Smart Cards](feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards "feature-support-USB-devices-qualified.md#feature-support-USB-devices-qualified-smart-cards").

**Application settings persistence options**:

    * **Enable Application Settings Persistence**
     — Users' application customizations and Windows settings are
     automatically saved after each streaming session and applied during the
     next session. These settings are saved to an Amazon Simple Storage Service (Amazon S3) bucket in your account, within the AWS Region in
     which application settings persistence is enabled.
    * **Settings Group** — The settings group determines which saved application settings are used for a streaming session from this stack. If the same settings group is applied to another stack, both stacks use the same application settings. By default, the settings group value is the name of the stack.

###### Note

For information about requirements for enabling and administering application settings
persistence, see [Enable Application Settings Persistence for Your
WorkSpaces Applications Users](app-settings-persistence.md "app-settings-persistence.md"). 11. For **Step 7: Review**, confirm the details for the stack. To change the
configuration for any section, choose **Edit** and make the
needed changes. After you finish reviewing the configuration details, choose
**Create**. 12. In the pricing acknowledgement dialog box, select the acknowledgement check box, and choose **Create**. 13. After the service sets up resources, the **Stacks** page
appears. The status of your new stack appears as **Active** when it is ready to use.

## Step 2: Provide Access to Users

After you create a stack with an associated fleet, you can provide access to users
through the WorkSpaces Applications user pool, SAML 2.0 [single sign-on (SSO)], or the WorkSpaces Applications API. For
more information, see [User Pool Administration in Amazon WorkSpaces Applications](user-pool-admin.md "user-pool-admin.md")
and [Amazon WorkSpaces Applications Integration with SAML 2.0](external-identity-providers.md "external-identity-providers.md").

###### Note

Users in the WorkSpaces Applications user pool can't be assigned to stacks with fleets that are joined to an Active Directory domain.

For this getting started exercise, you can use the WorkSpaces Applications user
pool. This access method enables you to create and manage users by using a permanent login portal URL.
To quickly test application streaming without setting up users, complete the following steps to create a temporary URL, also known as a streaming URL.

###### To provide access to users with a temporary URL

1. In the navigation pane, choose **Fleets**.
2. In the list of fleets, choose the fleet that is associated with the stack for which you want to create a streaming URL. Verify that the status of the fleet is **Running**.
3. In the navigation pane, choose **Stacks**.
   Select the stack, and then choose
   **Actions**, **Create Streaming URL**.
4. For **User id**, type the user ID. Choose an expiration
   time, which determines how long the generated URL is valid.
5. To view the user ID and URL, choose **Get URL**.
6. To copy the link to the clipboard, choose **Copy Link**.

After you provide your users with access to WorkSpaces Applications, they can start WorkSpaces Applications streaming sessions. If you provide access through the WorkSpaces Applications user pool, they must use a web browser for streaming sessions.

If you plan to use SAML 2.0 [single sign-on (SSO)] or the WorkSpaces Applications API to provide access
to your users, you can make the WorkSpaces Applications client available to them. The WorkSpaces Applications client is a
native application that is designed for users who require additional functionality
during their WorkSpaces Applications streaming sessions. For more information, see [Provide Access Through the WorkSpaces Applications Client](client-application.md "client-application.md").

## Resources

For more information, see the following:

- Learn how to use the WorkSpaces Applications image builder to add your own applications and create
  images that you can stream to your users. For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the
  WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").
- Provide persistent storage for your session users by using WorkSpaces Applications home
  folders, Google Drive, and OneDrive. For more information, see [Enable and Administer Persistent Storage for Your
  WorkSpaces Applications Users](persistent-storage.md "persistent-storage.md").
- Integrate your WorkSpaces Applications streaming resources with your Microsoft Active
  Directory environment. For more information, see [Using Active Directory with WorkSpaces Applications](active-directory.md "active-directory.md").
- Control who has access to your WorkSpaces Applications streaming instances. For more
  information, see [Identity and Access Management for Amazon WorkSpaces Applications](controlling-access.md "controlling-access.md"),
  [Amazon WorkSpaces Applications User Pools](user-pool.md "user-pool.md") and
  [Amazon WorkSpaces Applications Integration with SAML 2.0](external-identity-providers.md "external-identity-providers.md").
- Monitor your WorkSpaces Applications resources by using Amazon CloudWatch. For more information, see
  [WorkSpaces Applications Metrics and Dimensions](monitoring-with-cloudwatch.md "monitoring-with-cloudwatch.md") .
- Troubleshoot your WorkSpaces Applications streaming experience. For more information, see
  [Troubleshooting](troubleshooting.md "troubleshooting.md").
