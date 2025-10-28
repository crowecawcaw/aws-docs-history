# Create an RTMP push input

After you have created the input security group, you can create the RTMP push input.

###### To create an RTMP push input

1. Make sure that you have the information from [step 1](setup-rtmp-push-obtain-info.md "setup-rtmp-push-obtain-info.md").
2. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
3. In the navigation pane, choose **Inputs**.
4. On the **Inputs** page, choose **Create
   input**.
5. Complete the **Input details** section:
   - **Input** name – enter a name.
   - **Input type** – choose **RTMP
     (push)**.

6. In the **Network mode** section, choose
   **Public**.
7. In the **Input security group** section, specify the group to
   attach to this push input. You can choose an existing group, or you can create a
   group. The security group must allow the public network IP addresses to push to
   MediaLive. Following from the example in step 1, it must allow these
   addresses:

   203.0.113.19, 203.0.113.58, 203.0.113.25, 198.51.100.19, 198.51.100.59, 198.51.100.21

For more information about security groups, see [Working with input security groups](working-with-input-security-groups.md "working-with-input-security-groups.md"). 8. In the **Channel and input class** section, choose the class
for this input:

    * STANDARD
    * SINGLE-PIPELINE

For more information, see [Implementing pipeline
redundancy](plan-redundancy-mode.md "plan-redundancy-mode.md"). 9. In the **Input destinations** section, in the
**Destination** section, enter the application names and
application instances you previously obtained:

    * If the input is a standard-class input, complete both fields, to
     specify two sources.
    * If the input is a single-class input, complete the first field with
     the information that you obtained and leave the second field
     empty.

For example:

**Application name:** `live`

**Application instance:**
`curling` 10. In the **Tags** section, create tags if you want to associate
tags with this input. For more information, see [Tagging resources](tagging.md "tagging.md"). 11. Choose **Create**.

MediaLive creates the input and automatically creates two endpoints on that input.
The endpoints include the application name, the application instance, and the
port 1935. For example:

`198.51.100.99:1935/live/curling`

`192.0.2.18:1935/live/curling`

Note that the IP addresses are addresses that MediaLive creates. They aren't the
public addresses that you used in the security group. For a diagram that shows
the role of all the IP addresses, see [Result of this procedure](setup-result-rtmp-push.md "setup-result-rtmp-push.md")
in the section about setting up an RTMP push source.

MediaLive always creates two endpoints:

    * If you will set up the channel as a standard channel, both endpoints
     will be used.
    * If you will set up the channel as a single-pipeline channel, only the
     first endpoint will be used. MediaLive won't expect to receive content at
     the second endpoint.
