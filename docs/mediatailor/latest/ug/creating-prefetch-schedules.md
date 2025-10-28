# Creating prefetch schedules

The following procedure explains how to create a prefetch schedule by using the MediaTailor
console. For information about creating and managing prefetch schedules programmatically using
the MediaTailor API, see [PrefetchSchedules](../apireference/API_PrefetchSchedule.md "../apireference/API_PrefetchSchedule.md") in the
_AWS Elemental MediaTailor API Reference_.

###### Note

When configuring prefetch schedules in MediaTailor, it's important to understand how different
types of variables are handled.

**Avail matching criteria**

If you want to use avail matching criteria in a schedule, make sure that you first
configure your playback configuration's ADS URL template with [dynamic session variables](variables-session.md "variables-session.md"), otherwise the avail matching
criteria won't have an effect. For information about working with dynamic session variables,
see [Step 3: Configure
ADS request URL and query parameters](getting-started-ad-insertion.md#getting-started-configure-request "getting-started-ad-insertion.md#getting-started-configure-request") in the Getting started with MediaTailor
ad insertion topic.

**Player variables in prefetch schedules**

When you create a prefetch schedule, don't define player variables as dynamic variables
in your prefetch configuration. Instead, pass the player variables as you normally would at
session start. MediaTailor automatically includes these variables in prefetch ad requests if the
variables are mapped in the ADS template URL.

###### To create a new prefetch schedule using the console

1.  Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2.  In the navigation pane, choose **Configurations**. Select the playback
    configuration that you want to create a prefetch schedule for.
3.  On the **Prefetch schedules** tab, choose **Add prefetch
    schedule**.
4.  Under the **Prefetch schedule details** pane, do the following:
    - For **Name**, enter an identifier for your prefetch schedule, such as
      **my-prefetch-schedule**.
    - For **Stream ID**, optionally enter a unique ID. If your origin
      contains multiple playback streams, you can use this ID to instruct MediaTailor to place ads in a
      specific stream. For example, if your playback configuration has a sports stream and a TV
      show stream, you can use the stream ID to create prefetch schedules to insert ads targeted
      for the sports stream. You pass the stream ID value to MediaTailor in your client's session
      initialization or manifest request. For more information see the following example.

          + For *server-side tracking*, include the
           `?aws.streamId` query parameter and value in your client's `GET
           HTTP` request to your MediaTailor endpoint. For general information about server-side
           tracking see [Server-side ad tracking](ad-reporting-server-side.md "ad-reporting-server-side.md"). A manifest request to an HLS endpoint that
           includes a stream ID looks like the following, where
           ``myStreamId`` is the name of your stream ID:



          ```
          GET <mediatailorURL>/v1/master/`<hashed-account-id>`/`<origin-id>`/`<asset-id>`?aws.streamId=`myStreamId`
          ```
          + For *client-side tracking*, include the
           `streamId` key and value in your client's `POST HTTP` session
           initialization request body to the **MediaTailor/v1/session**
           endpoint. For general information about client-side tracking see [Client-side ad tracking](ad-reporting-client-side.md "ad-reporting-client-side.md"). A session
           initialization request that includes a stream ID looks like the following, where
           ``myStreamId`` is the name of your stream ID:



          ```
          POST <mediatailorURL>/v1/session/`<hashed-account-id>`/`<origin-id>`/`<asset-id>`
          {
              'streamId': '`myStreamId`',
              'reportingMode': 'client'
          }
          ```

      [Show moreShow less](# "#")

5.  For **Prefetch type**, make your selection and choose the corresponding
    section for assistance with additional fields:

        * Choose **Single** if you're creating one prefetch schedule for one ad
         break in an event.
        * Choose **Recurring** if you're creating a schedule that automatically
         prefetches ads before each ad break in an event.

    To create a schedule that prefetches ads before one ad avail in an event.

6.  On the **Retrieval** pane, specify the retrieval settings you want to
    use. These settings determine when MediaTailor prefetches ads from the ADS. They also determine
    which dynamic session variables to include in the request to the ADS, if any.
    - For **Start time**, enter the time when MediaTailor can start prefetch
      retrievals for this ad break. MediaTailor will attempt to prefetch ads for manifest requests made
      by your client on or after this time. The default value is the current time. If you don't
      specify a value, the service starts prefetch retrieval as soon as possible.
    - For **End time**, enter the time when you want MediaTailor to stop
      prefetching ads for this ad break. MediaTailor will attempt to prefetch ads for manifest requests
      that occur at or before this time. The retrieval window can overlap with the consumption
      window.
    - Optionally, configure traffic shaping to limit the number of requests to the ADS at
      one time. Choose one of the following approaches:

    _Time-window approach_: For **Traffic shaping window
    duration**, enter the number of seconds that MediaTailor should distribute requests to
    the ADS. For more information, see [Single
    prefetch schedule retrieval explanation](understanding-prefetching.md#avail-matching-criteria-retr "understanding-prefetching.md#avail-matching-criteria-retr").

    _TPS-based approach_: Configure **Peak TPS** and
    **Peak concurrent users** to limit requests based on transactions per
    second and concurrent users. For more information, see [TPS-based traffic shaping](tps-traffic-shaping.md "tps-traffic-shaping.md").
    - In the [Dynamic variables](variables.md "variables.md")
      section, enter as many as 100 dynamic session variables. MediaTailor uses these variables for
      substitution in prefetch requests that it sends to the ADS. If you don't enter any dynamic
      session variables, MediaTailor makes a best effort attempt to interpolate the values for the
      dynamic variables contained in your [ADS](configurations-create.md#configurations-create-main "configurations-create.md#configurations-create-main")
      URL.
      - Select **Add dynamic variable**.
      - For **Key**, enter a dynamic session variable key, such as
        `scte.event_id`. You can use any dynamic variable that MediaTailor supports. For
        information about dynamic session variables, see [MediaTailor session variables for ADS requests](variables-session.md "variables-session.md").
      - For **Value**, enter a dynamic variable value, such as
        `my-event`.
      - To add another dynamic variable, choose Select **Add dynamic
        variable**.

7.  On the **Consumption** pane, specify the settings that you want to use
    for the consumption window. These settings determine when MediaTailor places the ads into the ad
    break. They also determine any avail matching criteria that you want to use.
    - For **Start time**, enter the time when you want MediaTailor to begin to
      place prefetched ads into the ad break. the default value is the current time. If you don't
      specify a time, the service starts prefetch consumption as soon as possible.
    - For **End time**, enter a time when you want MediaTailor to stop placing
      the prefetched ads into the ad break. MediaTailor will attempt to prefetch ads for your client's
      manifest requests that occur at or before this time. The end time must be after the start
      time, and less than one day from now. The consumption window can overlap with the retrieval
      window.
    - In the [Avail matching criteria](variables.md "variables.md")
      section, select **Add avail criteria** and add as many ad five avail
      matching criteria to your schedule. Then, under **Dynamic variable key**,
      add a dynamic variable key, such as `scte.event_id`. MediaTailor will place the
      prefetched ads into the ad break _only_ if it meets the
      criteria defined by the dynamic variable values that either your client passes to MediaTailor, or
      that MediaTailor infers from information such as session data. If an ad break doesn't meet the
      specified matching criteria, MediaTailor skips the prefetch for that break. For information, see
      the [Single prefetch schedule consumption
      explanation](understanding-prefetching.md#avail-matching-criteria "understanding-prefetching.md#avail-matching-criteria").

8.  Select **Add avail criteria**.
    Prefetch schedules automatically expire after the consumption window's end time. For
    diagnostic purposes, they remain visible for at least 7 days, after which MediaTailor automatically
    deletes them. Alternatively, you can manually delete a prefetch schedule at any time. For
    information about how to manually delete a prefetch schedule, see the following [Deleting prefetch schedules](deleting-prefetch-schedules.md "deleting-prefetch-schedules.md") section.

### Determining how often your client should call the

CreatePrefetchSchedule API

Your client can programmatically call the [CreatePrefetchSchedule](../apireference/API_CreatePrefetchSchedule.md "../apireference/API_CreatePrefetchSchedule.md") API once per day to set up retrieval and consumption if you
have knowledge of exactly when ad breaks will occur. Or, your client can call the API many
times over the course of the day to define retrieval and consumption. When choosing an API
call frequency, take into consideration the [maximum
number of active prefetch schedules](quotas.md#prefetch-schedules-limit "quotas.md#prefetch-schedules-limit"), and the likelihood of whether your ad break
schedule will change after you create your prefetch schedule(s). If it's likely that the ad
break schedule will change after you've created your prefetch schedule(s), you might want to
call the API more frequently.

To create a schedule that prefetches ads before each ad avail in an event.

1. On the **Recurring retrieval** pane, specify the retrieval settings you
   want to use. These settings determine when MediaTailor prefetches ads from the ADS. They also
   determine which dynamic session variables to include in the request to the ADS, if
   any.
   - For **Recurring prefetch window**, enter the time when MediaTailor can
     start prefetch retrievals for this ad break. MediaTailor will attempt to prefetch ads for
     manifest requests made by your client on or after this time. The default value is the
     current time. If you don't specify a value, the service starts prefetch retrieval as soon
     as possible.
   - For **Delay after avail end**, enter the number of seconds that MediaTailor
     should wait after an avail ends before prefetching ads for the next avail. If you don't
     specify a value, MediaTailor defaults to a no delay.
   - Optionally, configure traffic shaping to limit the number of requests to the ADS at
     one time. Choose one of the following approaches:

   _Time-window approach_: For **Traffic shaping window
   duration**, enter the number of seconds that MediaTailor should distribute requests to
   the ADS. For more information, see [Recurring prefetch schedule retrieval explanation](understanding-prefetching.md#avail-matching-criteria-recurring-retr "understanding-prefetching.md#avail-matching-criteria-recurring-retr")

   _TPS-based approach_: Configure **Peak TPS** and
   **Peak concurrent users** to limit requests based on transactions per
   second and concurrent users. For more information, see [TPS-based traffic shaping](tps-traffic-shaping.md "tps-traffic-shaping.md").
   - In the [Dynamic variables](variables.md "variables.md")
     section, enter as many as 100 dynamic session variables. MediaTailor uses these variables for
     substitution in prefetch requests that it sends to the ADS. If you don't enter any dynamic
     session variables, MediaTailor makes a best effort attempt to interpolate the values for the
     dynamic variables contained in your [ADS](configurations-create.md#configurations-create-main "configurations-create.md#configurations-create-main")
     URL.
     - Select **Add dynamic variable**.
     - For **Key**, enter a dynamic session variable key, such as
       `scte.event_id`. You can use any dynamic variable that MediaTailor supports. For
       information about dynamic session variables, see [MediaTailor session variables for ADS requests](variables-session.md "variables-session.md").
     - For **Value**, enter a dynamic variable value, such as
       `my-event`.
     - To add another dynamic variable, choose Select **Add dynamic
       variable**.

2. On the **Consumption** pane, specify the settings that you want to use
   for the consumption window. These settings determine when MediaTailor places the ads into the ad
   break. They also determine any avail matching criteria that you want to use.
   - For **Retrieved ad expiration**, indicate how long after retrieval
     ads are available for insertion.
   - In the [Avail matching criteria](variables.md "variables.md")
     section, select **Add avail criteria** and add as many ad five avail
     matching criteria to your schedule. Then, under **Dynamic variable key**,
     add a dynamic variable key, such as `scte.event_id`. MediaTailor will place the
     prefetched ads into the ad break _only_ if it meets the
     criteria defined by the dynamic variable values that either your client passes to MediaTailor, or
     that MediaTailor infers from information such as session data. If an ad break doesn't meet the
     specified matching criteria, MediaTailor skips the prefetch for that break. For information, see
     the [Recurring prefetch schedule consumption
     explanation](understanding-prefetching.md#avail-matching-criteria-recur "understanding-prefetching.md#avail-matching-criteria-recur").

3. Select **Add avail criteria**.
   Prefetch schedules automatically expire after the consumption window's end time. For
   diagnostic purposes, they remain visible for at least 7 days, after which MediaTailor automatically
   deletes them. Alternatively, you can manually delete a prefetch schedule at any time. For
   information about how to manually delete a prefetch schedule, see the following [Deleting prefetch schedules](deleting-prefetch-schedules.md "deleting-prefetch-schedules.md") section.
