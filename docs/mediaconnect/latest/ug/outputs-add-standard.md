# Adding standard outputs to a MediaConnect flow

For transport stream flows, you can add up to 50 outputs. However, for optimal
performance, follow the guidance offered in [Best practices](best-practices.md "best-practices.md"). A standard output goes to any
destination that is not part of a virtual private cloud (VPC) that you created using
Amazon Virtual Private Cloud.

###### Note

CDI flows don't support standard outputs.

###### To add a standard output to a flow (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the flow that
   you want to add an output to.

The details page for that flow appears. 3. Choose the **Outputs** tab. 4. Choose **Add output**. 5. For **Name**, specify a name for your output. This value
is an identifier that is visible only on the AWS Elemental MediaConnect console and
is not visible to the end user. 6. For **Output type**, choose **Standard
output**. 7. For **Description**, enter a description that will remind
you later where this output is going. This might be the company name or
notes about the setup. 8. Determine which protocol you want to use for the output. 9. For specific instructions based on the protocol that you want to use,
choose one of the following tabs:

RIST

    1. For **Protocol**, choose
     **RIST**.
    2. For **IP address**, choose the IP
     address where you want to send the output.
    3. For **Port**, choose the port that
     you want to use when the content is distributed to this
     output. For more information about ports, see [Output destinations](destinations.md "destinations.md").


    ###### Note

    The RIST protocol requires one additional port for
     error correction. To accommodate this requirement,
     AWS Elemental MediaConnect reserves the port that is +1 from
     the port that you specify. For example, if you
     specify port 4000 for the output, the service
     assigns ports 4000 and 4001.
    4. For **Smoothing latency**, specify
     the additional delay that you want to use with output
     smoothing. We recommend that you specify a value of 0 ms
     to disable smoothing. However, if the receiver can't
     process the stream properly, specify a value between 100
     and 1,000 ms. This way, AWS Elemental MediaConnect attempts to
     correct jitter from the flow source. If you keep this
     field blank, the service uses the default value of 0
     ms.

RTP or RTP-FEC

    1. For **Protocol**, choose
     **RTP** or
     **RTP-FEC**.
    2. For **IP address**, choose the IP
     address where you want to send the output.
    3. For **Port**, choose the port that
     you want to use when the content is distributed to this
     output. For more information about ports, see [Output destinations](destinations.md "destinations.md").


    ###### Note

    The RTP-FEC protocol requires two additional ports
     for error correction. To accommodate this
     requirement, AWS Elemental MediaConnect reserves the ports
     that are +2 and +4 from the port that you specify.
     For example, if you specify port 4000 for the
     output, the service assigns ports 4000, 4002, and
     4004.
    4. For **Smoothing latency**, specify
     the additional delay that you want to use with output
     smoothing. We recommend that you specify a value of 0 ms
     to disable smoothing. However, if the receiver can't
     process the stream properly, specify a value between 100
     and 1,000 ms. This way, AWS Elemental MediaConnect attempts to
     correct jitter from the flow source. If you keep this
     field blank, the service uses the default value of 0
     ms.

SRT listener

    1. For **Name**, specify a name for your
     source. This value is an identifier that is visible only
     on the MediaConnect console. It is not visible to
     anyone outside of the current AWS account.
    2. For **Protocol**, choose
     **SRT listener**.
    3. For **Minimum latency**, specify the
     minimum size of the buffer (delay) that you want the
     service to maintain. A higher latency value means a
     longer delay in transmitting the stream, but more room
     for error correction. A lower latency value means a
     shorter delay, but less room for error correction. You
     can choose a value from 10–15,000 ms. If you keep this
     field blank, MediaConnect uses the default value of 2,000
     ms.


    The SRT protocol uses a **minimum
     latency** configuration on each side of the
     connection. The larger of these two values is used as
     the *recovery latency*. If the
     transmitted bitrate, multiplied by the recovery latency,
     is higher than the *receiver
     buffer*, the buffer will overflow and the
     stream can fail with a `Buffer Overflow
     Error`. On the SRT receiver side, the receiver
     buffer is configured by the SRTO\_RCVBUF value. The size
     of the receiver buffer is limited by the *flow control window
     size* (SRTO\_FC) value. On the MediaConnect side, the
     receiver buffer is calculated as the **maximum bitrate** value
     multiplied by the **minimum
     latency** value. For more information about
     the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
    4. For **CIDR allow list**, specify a
     range of IP addresses that are allowed to view content
     from your output. Format the IP addresses as a Classless
     Inter-Domain Routing (CIDR) block, for example,
     10.24.34.0/23. For more information about CIDR notation,
     see [RFC
     4632](https://tools.ietf.org/html/rfc4632 "https://tools.ietf.org/html/rfc4632").


    ###### Important

    Specify a CIDR block that is as precise as
     possible. Include only the IP addresses that you
     want to contribute content to your flow. If you
     specify a CIDR block that is too wide, it allows for
     the possibility of outside parties sending content
     to your flow.


    ###### Tip

    To specify an additional CIDR block, choose
     **Add**. You can specify up to
     three CIDR blocks.
    5. For **Port**, choose the port that
     you want to use when the content is distributed to this
     output. For more information about ports, see [Output destinations](destinations.md "destinations.md").
    6. If you want to encrypt the video as it is sent to this
     output, do the following:




    	1. In the **Encryption**
    	 section, choose
    	 **Enable**.
    	2. **Encryption type** will not
    	 be selectable. **srt-password**
    	 is the only available encryption for this
    	 protocol.
    	3. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	4. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the SRT
    	 password](encryption-srt-password-set-up.md#encryption-srt-password-set-up-password "encryption-srt-password-set-up.md#encryption-srt-password-set-up-password").

SRT caller

    1. For **Protocol**, choose
     **SRT-caller**.
    2. For **Minimum latency**, specify the
     minimum size of the buffer (delay) that you want the
     service to maintain. A higher latency value means a
     longer delay in transmitting the stream, but more room
     for error correction. A lower latency value means a
     shorter delay, but less room for error correction. You
     can choose a value from 10–15,000 ms. If you keep this
     field blank, MediaConnect uses the default value of 2,000 ms.


    The SRT protocol uses a **minimum
     latency** configuration on each side of the
     connection. The larger of these two values is used as
     the *recovery latency*. If the
     transmitted bitrate, multiplied by the recovery latency,
     is higher than the *receiver
     buffer*, the buffer will overflow and the
     stream can fail with a `Buffer Overflow
     Error`. On the SRT receiver side, the receiver
     buffer is configured by the SRTO\_RCVBUF value. The size
     of the receiver buffer is limited by the *flow control window
     size* (SRTO\_FC) value. On the MediaConnect side, the
     receiver buffer is calculated as the **maximum bitrate** value
     multiplied by the **minimum
     latency** value. For more information about
     the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
    3. For **Destination IP address**, enter
     the IP address or domain of the output's
     destination.
    4. For **Port**, choose the port that
     you want to use when the content is distributed to this
     output. For more information about ports, see [Output destinations](destinations.md "destinations.md").
    5. If you want to encrypt the video as it is sent to this
     output, do the following:




    	1. In the **Encryption**
    	 section, choose
    	 **Enable**.
    	2. **Encryption type** will not
    	 be selectable. **Srt-password**
    	 is the only available encryption for this
    	 protocol.
    	3. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	4. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager
    	 assigned when you [created the secret to store the SRT
    	 password](encryption-srt-password-set-up.md#encryption-srt-password-set-up-password "encryption-srt-password-set-up.md#encryption-srt-password-set-up-password").

Zixi pull

    1. For **Protocol**, choose
     **Zixi pull**.
    2. For **Stream ID**, enter the
     **Stream** value that was
     configured when you added the input on the Zixi
     receiver. In the Zixi receiver, this value is found in
     the **Stream parameters**
     section.


    ###### Important

    If you keep this field blank, the service uses the
     output name as the stream ID. Because the stream ID
     must match the value that is set in the Zixi
     receiver, you must specify the stream ID if it is
     not exactly the same as the output name.
    3. For **Remote ID**, enter the
     **ID** value that is assigned to
     the Zixi receiver. In the Zixi receiver, this value is
     located in the **General** settings
     menu and is labelled **ID**. The
     **ID** value can also be found on
     the Zixi receiver **Status**
     page.
    4. For **Maximum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value between 0 and 60,000 ms. If you keep this field
     blank, the service uses the latency that is set in the
     receiver.
    5. For **CIDR allow list**, specify a
     range of IP addresses that are allowed to retrieve
     content from your source. Format the IP addresses as a
     Classless Inter-Domain Routing (CIDR) block, for
     example, 10.24.34.0/23. For more information about CIDR
     notation, see [RFC
     4632](https://tools.ietf.org/html/rfc4632 "https://tools.ietf.org/html/rfc4632").


    ###### Tip

    To specify an additional CIDR block, choose
     **Add**. You can specify up to
     three CIDR blocks.
    6. If you want to encrypt the video as it is sent to this
     output, do the following:




    	1. In the **Encryption**
    	 section, choose
    	 **Enable**.
    	2. For **Encryption type**,
    	 choose **Static key**.
    	3. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	4. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").
    	5. For **Encryption algorithm**,
    	 choose the type of encryption that you want to use
    	 to encrypt the source.

Zixi push

    1. For **Protocol**, choose
     **Zixi push**.
    2. For **IP address**, choose the IP
     address where you want to send the output.
    3. For **Port**, choose the port that
     you want to use when the content is distributed to this
     output. For more information about ports, see [Output destinations](destinations.md "destinations.md").
    4. For **Stream ID**, enter the stream
     ID that is set in the Zixi receiver.


    ###### Important

    If you keep this field blank, the service uses the
     output name as the stream ID. Because the stream ID
     must match the value set in the Zixi receiver, you
     must specify the stream ID if it is not exactly the
     same as the output name.
    5. For **Maximum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value between 0 and 60,000 ms. If you keep this field
     blank, the service uses the default value of 6,000
     ms.
    6. If you want to encrypt the video as it is sent to this
     output, do the following:




    	1. In the **Encryption**
    	 section, choose
    	 **Enable**.
    	2. For **Encryption type**,
    	 choose **Static key**.
    	3. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	4. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").
    	5. For **Encryption algorithm**,
    	 choose the type of encryption that you want to use
    	 to encrypt the source.

10. Choose **Add output**.

###### To add an output to a flow (AWS CLI)

1. Create a JSON file that contains the details of the output that you want
   to add to the flow.

The following example shows the structure for the contents of the
file:

```
{
    "FlowArn": "`arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`",
    "Outputs": [
        {
            "Description": "`RTP-FEC Output`",
            "Destination": "`192.0.2.12`",
            "Name": "`RTPOutput`",
            "Port": `5020`,
            "Protocol": "`rtp-fec`",
            "SmoothingLatency": `100`
        }
    ]
}
```

2. In the AWS CLI, use the `add-flow-output` command:

```
aws mediaconnect add-flow-outputs --flow-arn "`arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`" --cli-input-json file://`addFlowOutput.txt` --region `us-west-2`

```

The following example shows the return value:

```
{
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
    "Outputs": [
        {
            "Name": "RTPOutput",
            "Port": 5020,
            "Transport": {
                "SmoothingLatency": 100,
                "Protocol": "rtp-fec"
            },
            "Destination": "192.0.2.12",
            "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:RTPOutput",
            "Description": "RTP-FEC Output"
        }
    ]
}

```
