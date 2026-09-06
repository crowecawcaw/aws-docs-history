

# Adding a standard source to an existing MediaConnect flow
<a name="source-adding-standard"></a>

You can add a second source to an existing flow for failover. Both sources on the flow must use the same protocol. (However, you can have one source that uses RTP and the other that uses RTP-FEC.) For more information about source failover, see [Source failover](source-failover.md).

**To add a standard source to an existing flow (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that you want to update.

1. Choose the **Source** tab.

1. In the **Source failover configuration** section, choose **Edit**.

1. In the **Edit source failover configuration** window, make sure that **Failover** is set to **Active**.
**Note**  
If you activate failover on a flow that is running, you might encounter a brief interruption in the flow output. 

1. In the **Failover mode** drop-down menu, select the mode to use with your source protocol. For a list of the modes supported by each protocol, see [Failover support for source protocols in MediaConnect](source-failover.md#source-failover-table)

1. For **Recovery window**, specify the size of the buffer (delay) that you want the service to maintain. A larger buffer means a longer delay in transmitting the stream, but more room for error correction. A smaller buffer means a shorter delay, but less room for error correction. You can choose a value from 100–15000 ms. If you keep this field blank, MediaConnect uses the default value of 200 ms.

1. Choose **Update**.

1. In the **Sources** section, choose **Add**.

1. For **Name**, specify a name for your source. This value is an identifier that is visible only on the MediaConnect console. 

1. For **Source type**, choose **Standard source**.

1. Determine which protocol your source uses.
**Note**  
All sources on a flow must use the same protocol. However, you can have one source that uses RTP and the other that uses RTP-FEC.

1. For specific instructions based on your protocol, choose one of the following tabs:

------
#### [ RIST ]

   1. For **Protocol**, choose **RIST**. 

   1. For **Inbound port**, specify the port that the flow listens on for incoming content. 
**Note**  
The RIST protocol requires one additional port for error correction. To accommodate this requirement, MediaConnect reserves the port that is \+1 from the port that you specify. For example, if you specify port 4000 for the output, the service assigns ports 4000 and 4001.

   1. For **Allowlist CIDR**, specify a range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block, for example, 10.24.34.0/23. For more information about CIDR notation, see [RFC 4632](https://tools.ietf.org/html/rfc4632).
**Important**  
Specify a CIDR block that is as precise as possible. Include only the IP addresses that you want to contribute content to your flow. If you specify a CIDR block that is too wide, it allows for the possibility of outside parties sending content to your flow.

   1. For **Maximum bitrate**, specify the maximum expected bitrate (in bits per second) for the flow. We recommend that you specify a value that is twice the actual bitrate. The lowest value that you can enter in this field is 100 Kbps.

   1. For **Maximum latency**, specify the size of the buffer (delay) that you want the service to maintain. A higher latency value means a longer delay in transmitting the stream, but more room for error correction. A lower latency value means a shorter delay, but less room for error correction. You can choose a value from 1–15,000 ms. If you keep this field blank, MediaConnect uses the default value of 2,000 ms. 

------
#### [  RTP or RTP-FEC ]

   1. For **Protocol**, choose **RTP** or **RTP-FEC**. 

   1. For **Inbound port**, specify the port that the flow listens on for incoming content.
**Note**  
The RTP-FEC protocol requires two additional ports for error correction. To accommodate this requirement, MediaConnect reserves the ports that are \+2 and \+4 from the port that you specify. For example, if you specify port 4000 for the output, the service assigns ports 4000, 4002, and 4004. 

   1. For **Allowlist CIDR**, specify a range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block, for example, 10.24.34.0/23. For more information about CIDR notation, see [RFC 4632](https://tools.ietf.org/html/rfc4632).
**Important**  
Specify a CIDR block that is as precise as possible. Include only the IP addresses that you want to contribute content to your flow. If you specify a CIDR block that is too wide, it allows for the possibility of outside parties sending content to your flow.

   1. For **Maximum bitrate**, specify the maximum expected bitrate (in bits per second) for the flow. We recommend that you specify a value that is twice the actual bitrate. The lowest value that you can enter in this field is 100 Kbps.

------
#### [ SRT listener ]

   1. For **Protocol**, choose **SRT listener**. 

   1. For **Source description**, enter a description that will remind you later where this source is from. This might be the company name or notes about the setup.

   1. For **Allowlist CIDR block**, specify a range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block, for example, 10.24.34.0/23. For more information about CIDR notation, see [RFC 4632](https://tools.ietf.org/html/rfc4632).
**Important**  
Specify a CIDR block that is as precise as possible. Include only the IP addresses that you want to contribute content to your flow. If you specify a CIDR block that is too wide, it allows for the possibility of outside parties sending content to your flow.

   1. For **Inbound port**, specify the port that the flow listens on for incoming content. 

   1. For **Source listener address**, enter the address MediaConnect will use for the SRT connection. The address can be an IP address or a domain name.

   1. For **Maximum bitrate** (optional), specify the maximum expected bitrate (in bits per second) for the flow. We recommend that you specify a value that is twice the actual bitrate. The lowest value that you can enter in this field is 100 Kbps.

   1. For **Minimum latency**, specify the minimum size of the buffer (delay) that you want the service to maintain. A higher latency value means a longer delay in transmitting the stream, but more room for error correction. A lower latency value means a shorter delay, but less room for error correction. You can choose a value from 10–15,000 ms. If you keep this field blank, MediaConnect uses the default value of 2,000 ms. 

      The SRT protocol uses a **minimum latency** configuration on each side of the connection. The larger of these two values is used as the *recovery latency*. If the transmitted bitrate, multiplied by the recovery latency, is higher than the *receiver buffer*, the buffer will overflow and the stream can fail with a `Buffer Overflow Error`. On the SRT receiver side, the receiver buffer is configured by the SRTO\_RCVBUF value. The size of the receiver buffer is limited by the *flow control window size* (SRTO\_FC) value. On the MediaConnect side, the receiver buffer is calculated as the **maximum bitrate** value multiplied by the **minimum latency** value. For more information about the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md)

   1. If the source is encrypted, choose **Enable** in the **Decryption** section and do the following:

      1. For **Role ARN**, specify the ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role).

      1. For **Secret ARN**, specify the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key).

------
#### [ SRT caller ]

   1. For **Protocol**, choose **SRT caller**. 

   1. For **Source description**, enter a description that will remind you later where this source is from. This might be the company name or notes about the setup.

   1. For **Source listener address**, enter the address MediaConnect will use for the SRT connection. The address can be an IP address or a domain name.

   1. For **Source listener port**, enter the port MediaConnect will use for the SRT connection.

   1. For **Maximum bitrate** (optional), specify the maximum expected bitrate (in bits per second) for the flow. We recommend that you specify a value that is twice the actual bitrate. The lowest value that you can enter in this field is 100 Kbps.

   1. For **Minimum latency**, specify the minimum size of the buffer (delay) that you want the service to maintain. A higher latency value means a longer delay in transmitting the stream, but more room for error correction. A lower latency value means a shorter delay, but less room for error correction. You can choose a value from 10–15,000 ms. If you keep this field blank, MediaConnect uses the default value of 2,000 ms. 

      The SRT protocol uses a **minimum latency** configuration on each side of the connection. The larger of these two values is used as the *recovery latency*. If the transmitted bitrate, multiplied by the recovery latency, is higher than the *receiver buffer*, the buffer will overflow and the stream can fail with a `Buffer Overflow Error`. On the SRT receiver side, the receiver buffer is configured by the SRTO\_RCVBUF value. The size of the receiver buffer is limited by the *flow control window size* (SRTO\_FC) value. On the MediaConnect side, the receiver buffer is calculated as the **maximum bitrate** value multiplied by the **minimum latency** value. For more information about the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md)

   1. For **Stream ID** (optional), enter an identifier for the stream. This identifier can be used to communicate information about the stream.

   1. If the source is encrypted, choose **Enable** in the **Decryption** section and do the following:

      1. For **Role ARN**, specify the ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role).

      1. For **Secret ARN**, specify the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key).

------
#### [ Zixi push ]

   1. For **Protocol**, choose **Zixi push**. 

      AWS Elemental MediaConnect populates the value of the inbound port.

   1. For **Allowlist CIDR**, specify a range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block, for example, 10.24.34.0/23. For more information about CIDR notation, see [RFC 4632](https://tools.ietf.org/html/rfc4632).
**Important**  
Specify a CIDR block that is as precise as possible. Include only the IP addresses that you want to contribute content to your flow. If you specify a CIDR block that is too wide, it allows for the possibility of outside parties sending content to your flow.

   1. For **Stream ID**, specify the stream ID that the Zixi sender uses.
**Important**  
If you leave this field blank, MediaConnect uses the source name as the stream ID. The stream ID must match the value that the Zixi sender uses. If it differs from the source name, specify the stream ID explicitly.

   1. For **Maximum latency**, specify the size of the buffer (delay) that you want the service to maintain. A higher latency value means a longer delay in transmitting the stream, but more room for error correction. A lower latency value means a shorter delay, but less room for error correction. You can choose a value from 0–60,000 ms. If you keep this field blank, the service uses the default value of 6,000 ms. 

   1. If the source is encrypted, choose **Enable** in the **Decryption** section and do the following:

      1. For **Decryption type**, choose **Static key**.

      1. For **Role ARN**, specify the ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role).

      1. For **Secret ARN**, specify the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key).

      1. For **Decryption algorithm**, choose the type of encryption that was used to encrypt the source.

------
#### [ Zixi push for AWS Elemental Link UHD device ]

   After creating the additional Zixi push source, you must configure the AWS Elemental Link device using MediaLive. See the following MediaLive setup instructions to complete the process after you have created the source: [Using a device in a flow](https://docs.aws.amazon.com/medialive/latest/ug/device-use-flow.html) in the *MediaLive User Guide*. Ensure you have access to both MediaConnect and MediaLive to complete these steps.

**Note**  
Zixi push for AWS Elemental Link UHD devices only supports failover mode. Merge mode is not supported.

   1. For **Protocol**, choose **Zixi push**. 

      AWS Elemental MediaConnect populates the value of the inbound port.

   1. For **Allowlist CIDR**, specify a range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block, for example, 10.24.34.0/23. For more information about CIDR notation, see [RFC 4632](https://tools.ietf.org/html/rfc4632).
**Important**  
If you know the range of public IP addresses that your Link device uses to connect to the internet, enter that CIDR block. Note that this is not the same as the IP address of the AWS Elemental Link device. If you cannot obtain this information, it is possible to configure the CIDR block to be open to all possible IP addresses by using 0.0.0.0/0. Typically, it is not best practice to assign a CIDR block that is open to the entire internet (0.0.0.0/0). However, if this method must be used, the data being transferred is encrypted using AES-128 encryption.

   1. For **Maximum latency**, specify the size of the buffer (delay) that you want the service to maintain. A higher latency value means a longer delay in transmitting the stream, but more room for error correction. A lower latency value means a shorter delay, but less room for error correction. You can choose a value between 0 and 60,000 ms. If you keep this field blank, the service uses the default value of 6,000 ms. The **Maximum latency** value should match the **Latency** value configured on the AWS Elemental Link device. For information on configuring the Link device's latency, see: [Configuring the device](https://docs.aws.amazon.com/medialive/latest/ug/device-edit.html) in the *AWS Elemental MediaLive User Guide* 

   1. For **Decryption**, choose **Activate** and do the following:

      1. For **Decryption type**, choose **Static key**.

      1. For **Decryption algorithm**, choose **AES-128**. AWS Elemental Link requires AES-128, do not select another algorithm.

      1. For **Role ARN**, specify the ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role).

      1. For **Secret ARN**, specify the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key).

------

1. Choose **Save**.