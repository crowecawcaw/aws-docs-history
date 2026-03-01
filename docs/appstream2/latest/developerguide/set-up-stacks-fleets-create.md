# Create a Fleet in Amazon WorkSpaces Applications

Set up and create a fleet from which user applications are launched and
streamed.

###### Note

To create an Always-On or On-Demand fleet, you must have an image that has
applications installed to create an Always-On or On-Demand fleet that your users can
stream from. To create an image, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md"). To
create an Elastic fleet, you must have applications associated to app blocks. To
create applications and app blocks for an Elastic fleet, see [Applications Manager](app-blocks-applications.md "app-blocks-applications.md").

###### To set up and create a fleet

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. Choose **Get Started** if you are new to the console, or
   **Fleets** from the left navigation pane. Choose
   **Create Fleet**.
3. For **Step 1: Select fleet type**, review the details of the
   fleet types, choose the type of fleet to create based on your use case, and
   select **Next**.

###### Note

The fleet type determines its immediate availability and how you pay for
it. For more information, see [WorkSpaces Applications Fleet Types](fleet-type.md "fleet-type.md"). 4. If you chose to create an Always-On or On-Demand fleet, for **Step 2: Choose an Image**, choose an image that meets your needs and then choose **Next**. 5. If you chose to create an Elastic fleet, for **Step 2: Assign applications**, choose the applications that users can launch from this fleet. 6. For **Step 3: Configure fleet**, enter the following
**details**:

    * For **Name**, enter a unique name identifier for the
     fleet. Special characters aren't allowed.
    * For **Display Name**, enter a name to display for the
     fleet (maximum of 100 characters). Special characters aren't
     allowed.
    * For **Description**, enter a description for the
     fleet (maximum of 256 characters).
    * For **Choose instance type**, choose the instance
     type that meets the performance requirements of your applications. All
     streaming instances in your fleet launch with the instance type that you
     select. For more information, see [WorkSpaces Applications Instance Families](instance-types.md "instance-types.md").




    	+ You can use stream.\* instance types for images with `type = "native"`. To use any of the following instance type you must [Import Image](import-image.md "import-image.md") and create an image with `type = "custom"`.




    		- GeneralPurpose.\*
    		- MemoryOptimized.\*
    		- ComputeOptimized.\*
    		- Accelerated.\*
    * Configure **storage** volumes for Always-On or On-Demand fleet instances. By default, the storage volume matches your image volume size, with a service default of 200 GB included in the hourly instance rate. You can customize your storage capacity from 200 GB up to 500 GB based on your requirements.


    ###### Note

    Note: Storage volume size cannot be set below the image volume size. Storage capacity can be increased up to 500 GB, with additional charges applying to any storage beyond the included 200 GB. These charges apply to fleet instances regardless of their running state (both running and stopped instances).
    * For Elastic fleets, for **Choose platform type**,
     choose the operating system that matches the requirements of your users’
     applications.
    * For **Maximum session duration in minutes**, choose
     the maximum amount of time that a streaming session can remain active.
     If users are still connected to a streaming instance five minutes before
     this limit is reached, they are prompted to save any open documents
     before being disconnected. After this time elapses, the instance is
     terminated and replaced by a new instance. The maximum session duration
     that you can set in the WorkSpaces Applications console is 5760 minutes (96 hours). The
     maximum session duration that you can set using the WorkSpaces Applications API and CLI
     is 432000 seconds (120 hours).
    * For **Disconnect timeout in minutes**, choose the
     amount of time that a streaming session remains active after users
     disconnect. If users try to reconnect to the streaming session after a
     disconnection or network interruption within this time interval, they
     are connected to their previous session. Otherwise, they are connected
     to a new session with a new streaming instance. If you associate a stack
     with a fleet for which a redirect URL is specified, after users’
     streaming sessions end, the users are redirected to that URL.


    If a user ends the session by choosing **End
     Session** or **Logout** on the WorkSpaces Applications
     toolbar, the disconnect timeout does not apply. Instead, the user is
     prompted to save any open documents, and then immediately disconnected
     from the streaming instance. The instance the user was using is then
     terminated.
    * For **Idle disconnect timeout in minutes**, choose
     the amount of time that users can be idle (inactive) before they are
     disconnected from their streaming session and the **Disconnect
     timeout in minutes** time interval begins. Users are
     notified before they are disconnected due to inactivity. If they try to
     reconnect to the streaming session before the time interval specified in
     **Disconnect timeout in minutes** has elapsed, they
     are connected to their previous session. Otherwise, they are connected
     to a new session with a new streaming instance. Setting this value to 0
     disables it. When this value is disabled, users are not disconnected due
     to inactivity.


    ###### Note

    Users are considered idle when they stop providing keyboard or
     mouse input during their streaming session. For domain-joined
     fleets, the countdown for the idle disconnect timeout doesn't begin
     until users log in with their Active Directory domain password or
     with a smart card. File uploads and downloads, audio in, audio out,
     and pixels changing do not qualify as user activity. If users
     continue to be idle after the time interval in **Idle
     disconnect timeout in minutes** elapses, they are
     disconnected.
    * For Elastic fleets, for **Max concurrent sessions**,
     specify the maximum number of concurrent sessions this fleet should
     have.


    ###### Note

    If you get an error message that says “The maximum number of
     concurrent sessions for your account was exceeded," you can submit a
     limit increase, through the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For more
     information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
     *Service Quotas User Guide*.
    * **Multiple user sessions** — Choose this option
     if you want to provision multiple user sessions on a single instance. By
     default, every unique user session is served by an instance
     (single-session).


    ###### Note

    Multi-session is available only on Always-on and On-demand fleets
     powered by a Windows operating system. Multi-session is not
     available on Elastic fleets or the Linux operating system.

    Only base images and managed image updates released on or after
     May 15, 2023 support multi-session fleets. For more details, see
     [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md "base-image-version-history.md").
    * **Maximum sessions per instance** — Maximum
     number of user sessions on an instance. You must choose this value based
     on your end users' application performance needs. You can also adjust
     the maximum sessions per instance for a fleet after it is provisioned.
     In that case, the existing user sessions and instances will not be
     impacted, but the fleet will become consistent with the new value of
     maximum sessions per instance. The value must be between 2 and 50.
     Before setting this value for your fleet, see [Multi-Session Recommendations](multi-session-recs.md "multi-session-recs.md").
    * For Always-On and On-Demand fleets, for **Minimum
     capacity**, choose a minimum number of instances (for
     single-session fleets) or user sessions (for multi-session fleets) for
     your fleet based on the minimum number of expected concurrent users.
    * For Always-On and On-Demand fleets, for **Maximum
     capacity**, choose a maximum number of instances (for
     single-session fleets) or user sessions (for multi-session fleets) for
     your fleet based on the maximum number of expected concurrent users.


    ###### Note

    For multi-session, you must specify the capacity based on the
     number of user sessions. The service will calculate the required
     number of instances to be launched, based on your fleet
     configuration and the value of maximum sessions per instance.
    * For **Stream view**, choose the WorkSpaces Applications view that is
     displayed to your users during their streaming sessions. Choose
     **Application** to display only the windows of
     applications opened by users. Choose **Desktop** to
     display the standard desktop that is provided by the operating system.


    ###### Note

    By default, WorkSpaces Applications displays only the windows of applications
     opened by users during their streaming sessions. To enable
     **Desktop** view for your users, configure your
     fleet to use an WorkSpaces Applications image that uses a version of the WorkSpaces Applications agent
     released on or after February 19, 2020.
    * For **Scaling details (Advanced)**, specify the
     scaling policies that WorkSpaces Applications uses to increase and decrease the capacity
     of your fleet. Note that the size of your fleet is limited by the
     minimum and maximum capacity that you specified. For more information,
     see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md "autoscaling.md").
    * For **IAM role (Advanced)**, when you apply an
     IAM role from your account to an WorkSpaces Applications fleet instance, you can make
     AWS API requests from the fleet instance without manually managing
     AWS credentials. To apply an IAM role, do either of the
     following:




    	+ To use an existing IAM role in your AWS account, choose
    	 the role that you want to use from the **IAM
    	 role** list. The role must be accessible from the
    	 fleet instance. For more information, see [Configuring an Existing IAM Role to Use With WorkSpaces Applications Streaming Instances](configuring-existing-iam-role-to-use-with-streaming-instances.md "configuring-existing-iam-role-to-use-with-streaming-instances.md").
    	+ To create a new IAM role, choose **Create new IAM
    	 role** and follow the steps in [How to Create an IAM Role to Use With WorkSpaces Applications Streaming Instances](how-to-create-iam-role-to-use-with-streaming-instances.md "how-to-create-iam-role-to-use-with-streaming-instances.md").


    * For Elastic fleets, for **USB Redirection
     (advanced)**, you can specify up to 10 strings that specify
     what types of USB devices that are attached to the local device can be
     redirected into the streaming session when using the Windows native
     client. For more information, see [Qualify USB Devices for Use with Streaming Applications](qualify-usb-devices.md "qualify-usb-devices.md").

7. Choose **Next**.
8. If you chose to create an Always-On or On-Demand fleet, for **Step 3:
   Choose an Image**, choose an image that meets your needs and then
   choose **Next**.
9. If you chose to create an Elastic fleet, for **Step 3: Assign
   applications**, choose the applications that users can launch from
   this fleet.
10. For **Step 4: Configure Network**, do the following:
    - To add internet access for fleet instances in a VPC with a public
      subnet, choose **Default Internet Access**. If you are
      providing internet access by using a NAT gateway, leave
      **Default Internet Access** unselected. For more
      information, see [Internet Access](internet-access.md "internet-access.md").

    ###### Note

    Your VPC must provide access to Amazon Simple Storage Service (S3)
    if you enable features that rely on saving to an S3 bucket. For more
    information, see [Using Amazon S3 VPC Endpoints for WorkSpaces Applications Features](managing-network-vpce-iam-policy.md "managing-network-vpce-iam-policy.md").
    - For **VPC** and **Subnet 1**, choose
      a VPC and at least one subnet that has access to the network resources
      that your application needs. For increased fault tolerance, we recommend
      that you choose two subnets in different Availability Zones. For more
      information, see [Configure a VPC with Private Subnets and a NAT Gateway](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md").

    ###### Note

    Elastic fleets require that you specify at least two subnets that
    are in different availability zones.

    If you don't have your own VPC and subnet, you can use the [default VPC](default-vpc-with-public-subnet.md "default-vpc-with-public-subnet.md") or
    create your own. To create your own, choose the **Create a new
    VPC** and **Create new subnet** links to
    create them. Choosing these links opens the Amazon VPC console. After you
    create your VPC and subnets, return to the WorkSpaces Applications console and choose the
    refresh icon to the left of the **Create a new VPC**
    and **Create new subnet** links to display them in the
    list. For more information, see [Configure a VPC for WorkSpaces Applications](appstream-vpc.md "appstream-vpc.md").
    - For **Security group(s)**, choose up to five security
      groups to associate with this fleet. If you don't have your own security
      group and you don't want to use the default security group, choose the
      **Create new security group** link to create one.
      After you create your subnets in the Amazon VPC console, return to the WorkSpaces Applications
      console and choose the refresh icon to the left of the **Create
      new security group** link to display them in the list. For
      more information, see [Security Groups in Amazon WorkSpaces Applications](managing-network-security-groups.md "managing-network-security-groups.md").
    - For Always-On and On-Demand fleets, for **Active Directory
      Domain (Optional)**, choose the Active Directory and
      organizational unit (OU) for your streaming instance computer objects.
      Ensure that the network access settings you selected enable DNS
      resolvability and communication with your directory. For more
      information, see [Using Active Directory with WorkSpaces Applications](active-directory.md "active-directory.md").

11. Choose **Next**.
12. For **Step 5: Review**, confirm the details for the fleet. To
    change the configuration for any section, choose **Edit** and
    make the needed changes. After you finish reviewing the configuration details,
    choose **Create**.
13. In the pricing acknowledgement dialog box, select the acknowledgement check
    box, and choose **Create**.

###### Note

If an error message notifies you that you don't have sufficient limits
(quotas) to create the fleet, submit a limit increase request through the
Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For more information, see
[Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_. 14. While your fleet is being created, the status of your fleets displays as
**Starting** in the **Fleets** list.
Choose the **Refresh** icon periodically to update the fleet
status until the status is **Running**. You cannot associate
the fleet with a stack and use it for streaming sessions until the status of the
fleet is **Running**.
