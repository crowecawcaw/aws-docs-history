# Create a WorkSpaces Pool

Set up and create a pool from which user applications are launched and streamed.

###### Note

You should create a directory before you create a WorkSpaces Pool. For more information, see
[Configure SAML 2.0 and create a WorkSpaces Pools
directory](create-directory-pools.md "create-directory-pools.md").

###### To set up and create a pool

1.  Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2.  In the navigation pane, choose **WorkSpaces**,
    **Pool**.
3.  Choose **Create WorkSpaces Pools**.
4.  Under **Onboarding** (optional), you can choose
    **Recommend options to me based on my use case** to get
    recommendations on the type of WorkSpace you want to use. You can skip this step if
    you know that you want to use WorkSpaces Pools.
5.  Under **Configure WorkSpaces**, enter the following details:
    - For **Name**, enter a unique name identifier for the
      pool. Special characters aren't allowed.
    - For **Description**, enter a description for the pool
      (maximum of 256 characters).
    - For **Bundle**, choose from the following the bundle type
      that you want to use for your WorkSpaces.
      - **Use a base WorkSpaces bundle** - Choose one of the
        bundles from the drop down. For more information about the bundle
        type you selected, choose **Bundle details**. To
        compare bundles offered for pools, choose **Compare all
        bundles**.
      - **Use your own custom bundle** - Choose a bundle
        that you previously created. To create a custom bundle, see [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md "create-custom-bundle.md").

    - For **Running mode**, choose from the following to
      configure the pool’s immediate availability and how you pay for it:
      - **AutoStop** — Pools instances are billed an
        hourly usage fee, based on the bundle chosen, only for the instances
        that are connected to users. Instances within the pool that are not
        connected to users are billed a low stopped-instance hourly fee.
        When users initiate their session, they start streaming after a 1-2
        minute wait.
      - **AlwaysOn** — All pools instances that are
        running are billed the applicable hourly usage fee, even when users
        aren't connected. This mode is best for users who don’t want to wait
        for their streaming to start.

    - For **Maximum session duration in minutes**, choose the
      maximum amount of time that a streaming session can remain active. If users
      are still connected to a streaming instance five minutes before this limit
      is reached, they are prompted to save any open documents before being
      disconnected. After this time elapses, the instance is terminated and
      replaced by a new instance. The maximum session duration that you can set in
      the WorkSpaces Pools console is 5760 minutes (96 hours). The maximum session
      duration that you can set using the WorkSpaces Pools API and CLI is 432000 seconds
      (120 hours).
    - For **Disconnect timeout in minutes**, choose the amount
      of time that a streaming session remains active after users disconnect. If
      users try to reconnect to the streaming session after a disconnection or
      network interruption within this time interval, they are connected to their
      previous session. Otherwise, they are connected to a new session with a new
      streaming instance.
    - If a user ends the session by choosing **End Session** or
      **Logout** on the pools toolbar, the disconnect timeout
      doesn’t apply. Instead, the user is prompted to save any open documents, and
      then immediately disconnected from the streaming instance. The instance the
      user was using is then terminated.
    - For **Idle disconnect timeout in minutes**, choose the
      amount of time that users can be idle (inactive) before they are
      disconnected from their streaming session and the **Disconnect
      timeout in minutes** time interval begins. Users are notified
      before they are disconnected due to inactivity. If they try to reconnect to
      the streaming session before the time interval specified in
      **Disconnect timeout in minutes** has elapsed, they are
      connected to their previous session. Otherwise, they are connected to a new
      session with a new streaming instance. Setting this value to 0 disables it.
      When this value is disabled, users are not disconnected due to
      inactivity.

    ###### Note

    Users are considered idle when they stop providing keyboard or mouse
    input during their streaming session. For domain-joined pools, the
    countdown for the idle disconnect timeout doesn't begin until users log
    in with their Active Directory domain password or with a smart card.
    File uploads and downloads, audio in, audio out, and pixels changing do
    not qualify as user activity. If users continue to be idle after the
    time interval in **Idle disconnect timeout in minutes**
    elapses, they are disconnected.
    - For **Scheduled capacity policies** (optional), choose
      **Add new schedule capacity**. Indicate the start and
      end date and time for when to provision the minimum and maximum number of
      instances for your pool based on the minimum number of expected concurrent
      users.
    - For **Manual scaling policies** (optional), specify the
      scaling policies for pools to use to increase and decrease the capacity of
      your pool. Expand **Manual scaling policies** to add new scaling policies.

    ###### Note

    The size of your pool is limited by the minimum and maximum capacity
    that you specified.

        + Choose **Add new scale out policies**
         and enter the values for adding specified instances if the
         specified capacity utilization is less or more than the specified threshold value.
        + Choose **Add new scale in policies**
         and enter the values for removing specified instances if the
         specified capacity utilization is less or more than the specified threshold value.

    - For **Tags**, specify the key pair value that you want to
      use. A key can be a general category, such as "project," "owner," or
      "environment," with specific associated values.

6.  On the **Select directory page**, choose the directory that you
    created. To create a directory, choose **Create directory**. For
    more information, see [Manage directories for WorkSpaces Pools](manage-workspaces-pools-directory.md "manage-workspaces-pools-directory.md").
7.  Choose **Create WorkSpace Pool**.
