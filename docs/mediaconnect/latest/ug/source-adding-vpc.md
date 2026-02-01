# Adding a VPC source to an existing MediaConnect

flow

You can add a second source to an existing transport stream flow for failover.
Both sources on the flow must be binary identical (come from the same encoder) and
they must use the same protocol. (However, you can have one source that uses RTP and
the other that uses RTP-FEC.) For more information about source failover, see [Source failover](source-failover.md "source-failover.md").

###### Important

Before you start this procedure, make sure that you completed the following
steps:

- In Amazon VPC, set up your VPC and associated security groups. For more
  information about VPCs, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md"). For information about
  configuring security groups to work with your VPC interface, see [Security group
  considerations](vpc-interface-security-groups.md "vpc-interface-security-groups.md").
- In IAM, [set up
  MediaConnect as a trusted service](security-iam-trusted-entity.md "security-iam-trusted-entity.md").
- If the source of your flow requires encryption, [set up
  encryption](encryption-static-key-set-up.md "encryption-static-key-set-up.md").
- [Stop your flow](flows-stop.md "flows-stop.md")
  or make sure that it's in a standby state. You can't add VPC interfaces
  to an active flow.
  MediaConnect doesn't support two sources on CDI flows. For redundancy with ST
  2110 JPEG XS sources, you can specify two inbound VPC interfaces on an individual
  media stream. For redundancy with CDI sources, create a second flow.

###### To add a VPC source to an existing flow (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the flow that
   you want to update.
3. Choose the **Source** tab.
4. In the **Source failover configuration** section, choose
   **Edit**.
5. In the **Edit source failover configuration** window,
   make sure that **Failover** is set to
   **Enabled**.

###### Note

If you enable failover on a flow that is running, you might encounter
a brief interruption in the flow output. 6. For **Recovery window**, specify the size of the buffer
(delay) that you want the service to maintain. A larger buffer means a
longer delay in transmitting the stream, but more room for error correction.
A smaller buffer means a shorter delay, but less room for error correction.
You can choose a value from 100–15000 ms. If you keep this field blank,
MediaConnect uses the default value of 200 ms. 7. Choose **Update**. 8. In the **Sources** section, choose **Add
source**. 9. For **Name**, specify a name for your source. This value
is an identifier that is visible only on the MediaConnect console. 10. For **Source type**, choose **VPC
source**. 11. Determine which protocol your source uses.

###### Note

All sources on a flow must use the same protocol. However, you can
have one source that uses RTP and the other that uses RTP-FEC. 12. For specific instructions based on your protocol, choose one of the
following tabs:

RIST

    1. For **Protocol**,
     **RIST** will automatically be
     selected.
    2. For **Inbound port**, specify the
     port that the flow listens on for incoming content.


    ###### Note

    The RIST protocol requires one additional port for
     error correction. To accommodate this requirement,
     MediaConnect reserves the port that is +1 from the
     port that you specify. For example, if you specify
     port 4000 for the output, the service assigns ports
     4000 and 4001.
    3. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    4. For **Maximum bitrate**, specify the
     maximum expected bitrate (in bits per second) for the
     flow. We recommend that you specify a value that is
     twice the actual bitrate. The lowest value that you can
     enter in this field is 100 Kbps.
    5. For **Maximum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value from 1–15,000 ms. If you keep this field blank,
     MediaConnect uses the default value of 2,000 ms.

RTP or RTP-FEC

    1. For **Protocol**, choose
     **RTP** or
     **RTP-FEC**.
    2. For **Inbound port**, specify the
     port that the flow listens on for incoming
     content.


    ###### Note

    The RTP-FEC protocol requires two additional ports
     for error correction. To accommodate this
     requirement, MediaConnect reserves the ports that
     are +2 and +4 from the port that you specify. For
     example, if you specify port 4000 for the output,
     the service assigns ports 4000, 4002, and 4004.
    3. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    4. For **Maximum bitrate**, specify the
     maximum expected bitrate (in bits per second) for the
     flow. We recommend that you specify a value that is
     twice the actual bitrate. The lowest value that you can
     enter in this field is 100 Kbps.

SRT listener

    1. For **Protocol**, **SRT
     listener** will automatically be selected.
    2. For **Source description**, enter a
     description that will remind you later where this source
     is from. This might be the company name or notes about
     the setup.
    3. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    4. For **Inbound port**, specify the
     port that the flow listens on for incoming
     content.
    5. For **Maximum bitrate**, specify the
     maximum expected bitrate (in bits per second) for the
     flow. We recommend that you specify a value that is
     twice the actual bitrate. The lowest value that you can
     enter in this field is 100 Kbps.
    6. For **Minimum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value from 10 -15,000 ms. If you keep this field blank,
     the service uses the default value of 2,000 ms.


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
    7. If the source is encrypted, choose
     **Enable** in the
     **Decryption** section and do the
     following:




    	1. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	2. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").

SRT caller

    1. For **Protocol**, **SRT
     caller** will automatically be selected.
    2. For **Source description**, enter a
     description that will remind you later where this source
     is from. This might be the company name or notes about
     the setup.
    3. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    4. For **Source listener
     port**, enter the port MediaConnect will
     use for the SRT connection.
    5. For **Source listener
     address**, enter the address MediaConnect
     will use for the SRT connection. The address can be an
     IP address or a domain name.
    6. For **Maximum bitrate**, specify the
     maximum expected bitrate (in bits per second) for the
     flow. We recommend that you specify a value that is
     twice the actual bitrate. The lowest value that you can
     enter in this field is 100 Kbps.
    7. For **Minimum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value from 10 -15,000 ms. If you keep this field blank,
     the service uses the default value of 2,000 ms.


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
    8. For **Stream ID**
     (optional), enter an identifier for the stream. This
     identifier can be used to communicate information about
     the stream.
    9. If the source is encrypted, choose
     **Enable** in the
     **Decryption** section and do the
     following:




    	1. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	2. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").

Zixi push

    1. For **Protocol**, **Zixi
     push** will automatically be selected.


    AWS Elemental MediaConnect populates the value of the inbound
     port.
    2. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    3. For **Stream ID**, specify the stream
     ID set in the Zixi feeder.


    ###### Important

    The stream ID must match the value set in the Zixi
     feeder. If you leave this field blank, MediaConnect uses
     the source name as the stream ID. If the stream ID
     is not exactly the same as the source name, you must
     manually enter the stream ID.
    4. For **Maximum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value from 0–60,000 ms. If you keep this field blank,
     the service uses the default value of 6,000 ms.
    5. If the source is encrypted, choose
     **Enable** in the
     **Decryption** section and do the
     following:




    	1. For **Decryption type**,
    	 choose **Static key**.
    	2. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	3. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").
    	4. For **Decryption algorithm**,
    	 choose the type of encryption that was used to
    	 encrypt the source.

13. Choose **Save**.
