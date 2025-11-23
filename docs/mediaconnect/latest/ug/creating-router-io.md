# Creating a router I/O in MediaConnect

When you create a router I/O, you'll configure its connection details and operating
parameters. Each router I/O connects to an external endpoint, which can be a public IP
address, or a private VPC IP address.

You can create two types of router I/Os:

- A **router input**, which receives content from a
  source endpoint (like a live video feed)
- A **router output**, which sends content to a
  destination endpoint (like a broadcast service)
  MediaConnect assigns each router I/O a permanent IP address. This ensures stable connections
  between your external endpoints and router I/Os, even when you change internal routing
  assignments. These connections persist until you either update the I/Os or delete
  them.

When creating a router I/O, you must specify both a tier and a maximum bitrate. The tier
you select determines the capacity limits, performance characteristics, and associated
costs. The maximum bitrate must fall within the limits of your selected tier. There are
separate tiers for inputs and outputs, each with different capacity limits.

You can configure router I/Os with either a Regional routing scope or a global routing
scope. By default, they use Regional scope, which restricts them to being assigned only to
other router I/Os within the same AWS Region. You can optionally set the routing scope to
global, which allows cross-Region routing (additional data transfer costs might apply).

###### Note

- AWS charges you for active router I/Os based on the tier you select. When a
  router I/O is active, it charges the hourly rate for that tier. Cross-Region routing
  and public internet egress for outputs incur additional hourly charges when data
  transfer is active. For more information, see [MediaConnect pricing](https://aws.amazon.com/mediaconnect/pricing/ "https://aws.amazon.com/mediaconnect/pricing/").
- For router inputs, MediaConnect manages incoming data transfers based on the
  tier's enforced bitrate limit. If content exceeds this limit, the source stream will
  be rejected. Router inputs have a fanout limit, determining the maximum number of
  outputs that can be simultaneously connected. This is set to 10.
- For router outputs, the maximum bitrate must be greater than or equal to the input
  it's assigned to.

## Prerequisites

- You have an AWS MediaConnect account.
- You know the AWS Region where you want to create the router I/O.
- You've identified the external endpoint that you want to connect to your router
  I/O.
- You have [created a network
  interface](creating-router-network-interfaces.md "creating-router-network-interfaces.md").
- If you want to connect your router I/O to a MediaConnect flow, your flow must be
  set up for router integration. For more information, see [Integrating router
  I/Os with MediaConnect
  flows](integrate-flow-with-router.md "integrate-flow-with-router.md").
- If you want to connect your router output to a MediaLive input, your MediaLive
  input must be set up for router integration. For more information, see [Integrating router
  outputs
  with MediaLive inputs](integrate-eml-with-router.md "integrate-eml-with-router.md").

## Procedure

Follow these procedures to create a router input or a router output.

1.  Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2.  In the navigation pane, choose **Router inputs**.
3.  Choose **Create router input**.
4.  Under **Router input details**, set up your input:
    1. **Name** - Give your input a descriptive name.

    ###### Tip

    Include details like the content type or source in the name (for
    example, `StudioA-Live` or
    `SatelliteFeed1`). This approach makes managing
    multiple inputs easier as your routing system grows. 2. **Tier** - Select a tier based on your performance requirements. 3. **Maximum bitrate** - Specify the highest bitrate that
    you expect (in bits per second).

    ###### Important

    This setting acts as a hard limit. If the incoming content exceeds
    this bitrate on a sustained basis, the source stream will be suspended
    and will automatically resume when the bitrate returns to an acceptable range. 4. **Region** - Select an AWS Region where you want to
    create this input.

    ###### Tip

    Choose a Region close to your upstream content source for optimal
    performance. 5. **Routing scope** - Select _regional_
    to restrict routing to outputs in the same AWS Region, or
    _global_ to enable cross-region routing.

5.  Under **Input type**, choose an option and complete its configuration:
    1.  **Standard** - To receive content from an external source endpoint, follow these steps:
        1. Under **Standard router input configuration**,
           select a network interface to use. For public network interfaces, select the availability
           zone where the router input will be placed in. For VPC network interfaces, the
           availability zone is inferred from the network interface subnet.
        2. Under **Protocol configuration**, select a protocol and set
           it up:

        RIST

            1. **Port** - Enter the listening port for incoming
             content.
            2. **Recovery latency** - Set your desired value in
             milliseconds.

        RTP

            1. **Port** - Enter the listening port for incoming
             content.
            2. **Forward error correction** - Choose whether to
             enable this feature.

        SRT Caller

            1. **Source address** - Enter the IP address or domain
             name for the SRT connection.
            2. **Router input source port** - Specify the SRT
             Listener source port.
            3. **Minimum latency** - Specify the smallest buffer
             latency that you want to maintain between the source and the router
             input.





            ###### Note

            The SRT protocol uses a **minimum latency**
             configuration on each side of the connection. The larger of these two
             values is used as the *recovery latency*. If the
             transmitted bitrate, multiplied by the recovery latency, is higher
             than the *receiver buffer*, the
             buffer will overflow and the stream can fail with a `Buffer
             Overflow Error`. On the SRT receiver side, the receiver buffer
             is configured by the SRTO\_RCVBUF value. The size of the receiver
             buffer is limited by the *flow control window
             size* (SRTO\_FC) value. On the MediaConnect side, the receiver
             buffer is calculated as the **maximum
             bitrate** value multiplied by the **minimum latency** value. For more information about the
             SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
            4. **Stream ID** - Enter the identifier for the
             stream.
            5. **SRT Caller decryption configuration**
             - If you want to enable decryption, follow these steps:




            	1. Select **Enable
            	 decryption**.
            	2. Under **Role ARN**, enter the ARN
            	 of the role that you created when you set up MediaConnect as a trusted
            	 entity.
            	3. Under **Secret ARN**, enter the ARN
            	 that AWS Secrets Manager assigned when you created the secret to store the
            	 encryption key.

        SRT Listener

            1. **Port** - Enter the listening port for incoming
             content.
            2. **Minimum latency** - Specify the smallest buffer
             latency that you want to maintain between the source and the router
             input.


            ###### Note

            The SRT protocol uses a **minimum latency**
             configuration on each side of the connection. The larger of these two
             values is used as the *recovery latency*. If the
             transmitted bitrate, multiplied by the recovery latency, is higher
             than the *receiver buffer*, the
             buffer will overflow and the stream can fail with a `Buffer
             Overflow Error`. On the SRT receiver side, the receiver buffer
             is configured by the SRTO\_RCVBUF value. The size of the receiver
             buffer is limited by the *flow control window
             size* (SRTO\_FC) value. On the MediaConnect side, the receiver
             buffer is calculated as the **maximum
             bitrate** value multiplied by the **minimum latency** value. For more information about the
             SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
            3. **SRT Listener decryption
             configuration** - If you want to enable decryption, follow
             these steps:




            	1. Select **Enable
            	 decryption**.
            	2. Under **Role ARN**, enter the ARN
            	 of the role that you created when you set up MediaConnect as a trusted
            	 entity.
            	3. Under **Secret ARN**, enter the ARN
            	 that AWS Secrets Manager assigned when you created the secret to store the
            	 encryption key.

    2.  **MediaConnect Flow** - To receive content from a flow,
        follow these steps.

    ###### Note

    This option requires a flow with an output that's been set up for router
    integration. For more information, see [Integrating router
    I/Os with MediaConnect
    flows](integrate-flow-with-router.md "integrate-flow-with-router.md").

    If you want to create the router input and connect the flow at a later time,
    select the **Do not connect to a MediaConnect flow** option
    and then select the availability zone where the router input will be placed in. Both the
    router input and the upstream flow must be placed in the same availability zone.

        1. Under **MediaConnect flow ARN**, specify the flow
         that you want to connect to.
        2. Under **MediaConnect flow output ARN**, specify the
         output of the flow.
        3. Under **Flow transit decryption key type**, choose
         how to decrypt the flow’s encrypted content as it moves from the flow to
         the router input.


        	1. **Automatic encryption key** - Choose this if you
        	 want automatic key management (recommended in most cases). With this
        	 option, MediaConnect will handle key creation and rotation for you.
        	2. **AWS Secrets Manager encryption key** - Choose this if
        	 your security requirements require you to use your own encryption
        	 keys. Then, do the following:


        		1. For **Role ARN**, enter the ARN of the IAM
        		 role that allows MediaConnect to access your encryption
        		 keys.
        		2. For **Secret ARN**, enter the ARN of the
        		 secret in Secrets Manager that contains your encryption
        		 key.



        		###### Important


        		 The content of the secret must be an AES-256 key in hexadecimal format.
        		 The key must have 64 digits.

    3.  **Failover** - For failover configuration, follow these steps:
        1. Under **Failover router input configuration**, select the network interface
           and the protocol. For public network interfaces, select the availability
           zone where the router input will be placed in. For VPC network interfaces, the
           availability zone is inferred from the network interface subnet.
        2. Under **First source protocol configuration**,
           define the protocol settings for the primary source.

        RIST

            1. **Port** - Enter the listening port for
             incoming content.
            2. **Recovery latency** - Set your desired
             value in milliseconds.

        RTP

            1. **Port** - Enter the listening port for
             incoming content.
            2. **Forward error correction** - Choose
             whether to enable this feature.

        SRT Caller

            1. **Source address** - Enter the IP address
             or domain name for the SRT connection.
            2. **Router input source port** - Specify the
             SRT Listener source port.
            3. **Minimum latency** - Specify the smallest
             buffer latency that you want to maintain between the source and
             the router input.





            ###### Note

            The SRT protocol uses a **minimum
             latency** configuration on each side of the
             connection. The larger of these two values is used as the
             *recovery latency*. If the transmitted
             bitrate, multiplied by the recovery latency, is higher than
             the *receiver buffer*, the
             buffer will overflow and the stream can fail with a
             `Buffer Overflow Error`. On the SRT receiver
             side, the receiver buffer is configured by the SRTO\_RCVBUF
             value. The size of the receiver buffer is limited by
             the *flow control window
             size* (SRTO\_FC) value. On the MediaConnect side, the
             receiver buffer is calculated as the **maximum bitrate** value multiplied by
             the **minimum latency** value.
             For more information about the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
            4. **Stream ID** - Enter the identifier for
             the stream.
            5. **Decryption** - If you want to
             enable decryption, follow these steps:




            	1. Select **Enable
            	 decryption**.
            	2. Under **Role ARN**, enter
            	 the ARN of the role that you created when you set up MediaConnect
            	 as a trusted entity.
            	3. Under **Secret ARN**, enter
            	 the ARN that AWS Secrets Manager assigned when you created the secret
            	 to store the encryption key.

        SRT Listener

            1. **Port** - Enter the listening port for
             incoming content.
            2. **Minimum latency** - Specify the smallest
             buffer latency that you want to maintain between the source and
             the router input.


            ###### Note

            The SRT protocol uses a **minimum
             latency** configuration on each side of the
             connection. The larger of these two values is used as the
             *recovery latency*. If the transmitted
             bitrate, multiplied by the recovery latency, is higher than
             the *receiver buffer*, the
             buffer will overflow and the stream can fail with a
             `Buffer Overflow Error`. On the SRT receiver
             side, the receiver buffer is configured by the SRTO\_RCVBUF
             value. The size of the receiver buffer is limited by
             the *flow control window
             size* (SRTO\_FC) value. On the MediaConnect side, the
             receiver buffer is calculated as the **maximum bitrate** value multiplied by
             the **minimum latency** value.
             For more information about the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
            3. **Decryption** - If you want to
             enable decryption, follow these steps:




            	1. Select **Enable
            	 decryption**.
            	2. Under **Role ARN**, enter
            	 the ARN of the role that you created when you set up MediaConnect
            	 as a trusted entity.
            	3. Under **Secret ARN**, enter
            	 the ARN that AWS Secrets Manager assigned when you created the secret
            	 to store the encryption key.

        3. Under **Second source protocol configuration**,
           repeat the previous step for the secondary source using a different port
           number.

        ###### Note

        When using RTP with FEC enabled for failover/merge on a router
        input, MediaConnect automatically reserves three ports: the port you
        specify, plus the ports that are +2 and +4 from that.

        For example, if you specify port 2000 for the input,
        MediaConnect will also reserve ports 2002 and 2004 for the FEC
        streams. 4. Under **Source priority configuration**,
        choose how sources are prioritized during failover scenarios.

            1. **No priority** - Choose this if you want
             MediaConnect to treat the sources with equal priority and switch between them as needed.
            2. **Primary/Secondary** - Choose this if you want
             to select one of the sources as a primary source. MediaConnect will switch to the secondary
             source if the primary source is not available, and will switch back to the primary
             source as soon as data returns.

    4.  **Merge** - For merge configuration, follow these steps:
        1. Under **Merge router input configuration**, select the network interface and
           the protocol, and define a recovery window in milliseconds.

        For public network interfaces, select the availability
        zone where the router input will be placed in. For VPC network interfaces, the
        availability zone is inferred from the network interface subnet.

        The recovery window is the size of the buffer (delay) that you want
        MediaConnect to maintain. A larger recovery window means a longer delay in
        transmitting the stream, but more room for error correction. A smaller
        recovery window means a shorter delay, but less room for error
        correction. 2. Under **First source protocol configuration**, define the protocol settings
        for the first source.

        RIST

            1. **Port** - Enter the listening port for incoming
             content.
            2. **Recovery latency** - Set your desired value in
             milliseconds.

        RTP

            1. **Port** - Enter the listening port for incoming
             content.
            2. **Forward error correction** - Choose whether to
             enable this feature.

        3. Under **Second source protocol configuration**,
           repeat the previous configuration step for the second source using a
           different port number.

        ###### Note

        When using RTP with FEC enabled for failover/merge on a router
        input, MediaConnect automatically reserves three ports: the port you
        specify, plus the ports that are +2 and +4 from that.

        For example, if you specify port 2000 for the input,
        MediaConnect will also reserve ports 2002 and 2004 for the FEC
        streams.

6.  Under **Transit encryption key configuration**, choose how to
    encrypt content as it moves through the router's internal network.

###### Note

This encryption applies only to content moving through the router matrix. It is separate from
any encryption you configure between your source and input, or between your
output and destination.

    1. **Automatic encryption key** - Choose this if you want automatic key management (recommended in most cases). With this option, MediaConnect will handle key creation and rotation for you.
    2. **AWS Secrets Manager encryption key** - Choose this if your security requirements require you to use your own encryption keys. Then, do the following:


    	1. For **Role ARN**, enter the ARN of the IAM role that
    	 allows MediaConnect to access your encryption keys.
    	2. For **Secret ARN**, enter the ARN of the secret in
    	 Secrets Manager that contains your encryption key.


    	###### Important


    	 The content of the secret must be an AES-256 key in hexadecimal format.
    	 The key must have 64 digits.

7.  Under **Maintenance configuration**, choose an option:
    1. **Default** - Choose this if you want MediaConnect to define the maintenance schedule for you.
    2. **Preferred day and time** - Choose this if you want to define your own maintenance schedule.

8.  Under **Tags**, define up to 50 tags to help you identify and
    organize this router input.
9.  Choose **Create router input**.

10. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
11. In the navigation pane, choose **Router outputs**.
12. Choose **Create router output**.
13. Under **Router output details**, set up your output:
    1. **Name** - Give your output a descriptive name.

    ###### Tip

    Include details like content type or destination in the name (such as
    `ControlRoom-Monitor` or
    `Affiliate1`). This can make managing multiple
    outputs easier as your routing system grows. 2. **Tier** - Select a tier based on your performance requirements. 3. **Maximum bitrate** - Enter the highest bitrate you
    expect (in bits per second).

    ###### Important

    This setting affects which inputs your output can take a route from.
    To ensure routing compatibility, the output's maximum bitrate must be at least as
    large as the input bitrate. 4. **Region** - Select an AWS Region where you want to
    create this output.

    ###### Tip

    Choose a Region close to your downstream content destination for optimal
    performance. 5. **Routing scope** - Select _regional_
    to restrict routing from inputs in the same AWS Region, or
    _global_ to enable cross-region routing.

14. Under **Output type**, choose one of these options and
    complete its configuration.
    1.  **Standard** - To send content to an external source
        endpoint, follow these steps:
        1. Under **Standard router output configuration**,
           select a network interface to use. For public network interfaces, select the availability
           zone where the router output will be placed in. For VPC network interfaces, the
           availability zone is inferred from the network interface subnet.
        2. Under **Protocol configuration**, select a protocol and set
           it up:

        RIST

            1. **Destination address** - Specify where you're
             sending the content.
            2. **Port** - Specify the port to use.

        RTP

            1. **Destination address** - Specify where you're
             sending the content.
            2. **Port** - Specify the port to use.
            3. **Forward error correction** - Choose whether to
             enable this feature.

        SRT Caller

            1. **Destination address** - Enter the IP address or
             domain where you're sending the content to.
            2. **Port** - Specify the port to use.
            3. **Minimum latency** - Specify the smallest buffer
             latency that you want to maintain between the router output and the
             destination.


            ###### Note

            The SRT protocol uses a minimum latency configuration on each side
             of the connection. The larger of these two values is used as the
             *recovery latency*. If the transmitted bitrate,
             multiplied by the recovery latency, is higher than the
             *receiver buffer*, the buffer might overflow,
             causing the stream to fail with a `Buffer Overflow Error`.
             On the SRT receiver side, the receiver buffer is configured by the
             SRTO\_RCVBUF value. The size of the receiver buffer is limited by the
             *flow control window size* (SRTO\_FC) value. On
             the MediaConnect side, the receiver buffer is calculated as the maximum
             bitrate value multiplied by the minimum latency value. For more
             information about the SRT buffer, see [the SRT Configuration Guidelines](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md").
            4. **Stream ID** (optional) - Enter an identifier for
             the stream.
            5. **SRT Caller encryption configuration**
             - If you want to enable encryption, follow these steps:




            	1. Select **Enable
            	 encryption**.
            	2. Under **Role ARN**, enter the ARN
            	 of the role that you created when you set up MediaConnect as a trusted
            	 entity.
            	3. Under **Secret ARN**, enter the ARN
            	 that AWS Secrets Manager assigned when you created the secret to store the
            	 encryption key.

        SRT Listener

            1. **Port** - Specify the port to use.
            2. **Minimum latency** - Specify the smallest buffer
             latency that you want to maintain between the router output and the
             destination.


            ###### Note

            The SRT protocol uses a minimum latency configuration on each side
             of the connection. The larger of these two values is used as the
             *recovery latency*. If the transmitted bitrate,
             multiplied by the recovery latency, is higher than the
             *receiver buffer*, the buffer might overflow,
             causing the stream to fail with a `Buffer Overflow Error`.
             On the SRT receiver side, the receiver buffer is configured by the
             SRTO\_RCVBUF value. The size of the receiver buffer is limited by the
             *flow control window size* (SRTO\_FC) value. On
             the MediaConnect side, the receiver buffer is calculated as the maximum
             bitrate value multiplied by the minimum latency value. For more
             information about the SRT buffer, see [the SRT Configuration Guidelines](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md").
            3. **SRT Listener encryption
             configuration** - If you want to enable encryption, follow
             these steps:




            	1. Select **Enable
            	 encryption**.
            	2. Under **Role ARN**, enter the ARN
            	 of the role that you created when you set up MediaConnect as a trusted
            	 entity.
            	3. Under **Secret ARN**, enter the ARN
            	 that AWS Secrets Manager assigned when you created the secret to store the
            	 encryption key.

    2.  **MediaConnect Flow** - To send content to a flow, follow
        these steps.

    ###### Note

    This option requires a flow with a source that's been set up for router
    integration. For more information, see [Integrating router
    I/Os with MediaConnect
    flows](integrate-flow-with-router.md "integrate-flow-with-router.md").

    If you want to create the router output and connect the flow at a later time,
    select the **Do not connect to a MediaConnect flow** option
    and then select the availability zone where the router output will be placed in. Both the
    router output and the downstream flow must be placed in the same availability zone.

        1. Under **MediaConnect flow ARN**, specify the flow
         that you want to connect to.
        2. Under **MediaConnect flow source ARN**, specify the
         source of the flow.
        3. Under **Transit encryption key type**, choose how to
         encrypt the content as it moves from the router output to the flow.


        	1. **Automatic encryption key** - Choose this if you
        	 want automatic key management (recommended in most cases). With this
        	 option, MediaConnect will handle key creation and rotation for you.
        	2. **AWS Secrets Manager encryption key** - Choose this if
        	 your security requirements require you to use your own encryption
        	 keys. Then, do the following:


        		1. For **Role ARN**, enter the ARN of the IAM
        		 role that allows MediaConnect to access your encryption
        		 keys.
        		2. For **Secret ARN**, enter the ARN of the
        		 secret in Secrets Manager that contains your encryption
        		 key.


        		###### Important


        		 The content of the secret must be an AES-256 key in hexadecimal format.
        		 The key must have 64 digits.

    3. **MediaLive input** - To send content to a MediaLive
       input, follow these steps.

    ###### Note

    This option requires a MediaLive input that's been set up for router
    integration. For more information, see [Integrating router
    outputs
    with MediaLive inputs](integrate-eml-with-router.md "integrate-eml-with-router.md").

    If you want to create the router output and connect the MediaLive input at a later time,
    select the **Do not connect to a MediaLive input** option
    and then select the availability zone where the router output will be placed in. Both the
    router output and the downstream MediaLive input must be placed in the same availability zone.

        1. Under **MediaLive input ARN**, specify the input that
         you want to connect to.
        2. Under **Pipeline**, specify the pipeline that you
         want to use.
        3. Under **Transit encryption key type**, choose how to
         encrypt the content as it moves from the router output to the MediaLive
         input.


        	1. **Automatic encryption key** - Choose this if you
        	 want automatic key management (recommended in most cases). With this
        	 option, MediaConnect will handle key creation and rotation for you.
        	2. **AWS Secrets Manager encryption key** - Choose this if
        	 your security requirements require you to use your own encryption
        	 keys. Then, do the following:


        		1. For **Role ARN**, enter the ARN of the IAM
        		 role that allows MediaConnect to access your encryption
        		 keys.
        		2. For **Secret ARN**, enter the ARN of the
        		 secret in Secrets Manager that contains your encryption
        		 key.


        		###### Important


        		 The content of the secret must be an AES-256 key in hexadecimal format.
        		 The key must have 64 digits.

15. Under **Maintenance configuration**, choose an option:
    1. **Default** - Choose this if you want MediaConnect to define the
       maintenance schedule for you.
    2. **Preferred day and time** - Choose this if you want to
       define your own maintenance schedule.

16. Under **Tags**, define up to 50 tags to help you identify and
    organize this router output.
17. Choose **Create router output**.

## Next steps

- To view the router I/Os you've created, see [Viewing router I/Os in MediaConnect](viewing-router-io.md "viewing-router-io.md").
- To start using your router I/O, see [Starting a router I/O in MediaConnect](starting-router-io.md "starting-router-io.md").
- To control how your media flows through the router, see [Managing routes in MediaConnect](assigning-route.md "assigning-route.md").

## Additional resources

To create router I/Os programmatically, see the following pages in the _MediaConnect API Reference_:

- [CreateRouterInput](../api/API_CreateRouterInput.md "../api/API_CreateRouterInput.md")
- [CreateRouterOutput](../api/API_CreateRouterOutput.md "../api/API_CreateRouterOutput.md")

This includes information about how to use the `CreateRouterInput` and
`CreateRouterOutput` operations and parameters in one of the
language-specific AWS SDKs.
