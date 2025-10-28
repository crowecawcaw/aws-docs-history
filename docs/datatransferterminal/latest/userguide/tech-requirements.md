# Technical requirements for using Data Transfer Terminal

Before scheduling a reservation at a Data Transfer Terminal, you’ll need to ensure you have the equipment and configurations necessary to connect to the network. Refer to the following guidelines for optimal network connectivity and experience.

## Equipment

You must bring portable devices for connectivity including monitors, a keyboard, a mouse, and computer or laptop to the Data Transfer Terminal facility for your scheduled reservation.

Your hardware must be able to work with fiber optic (L4) connections

###### Note

As a data security best practice, ensure that your data is encrypted and secured on the storage devices you bring to the Data Transfer Terminal, and that you apply data encryption policies while using the Data Transfer Terminal facility. For more information, see [Security of AWS Data Transfer Terminal](security.md "security.md")

## Network requirements

Ensure your uploading device, server, or appliance (laptop) is prepared to connect to the network and that it supports DHCP. You should have the following for an optimal data upload experience:

- A 100G QSFP28 LR4 (100GBASE-LR4) optical QSFP transceiver, compatible with the NIC and LC connectors for the fiber cable connections provided in the Data Transfer Terminal facility.
- IP address auto-configuration DHCP enabled. DNS servers are automatically assigned by DHCP.
- Up-to-date software and NIC drivers.

## Performance optimization

To maximize the throughput while using the AWS Data Transfer Terminal consider the following recommendations.

- **Recommended hardware**:
  - 100 Gbps network interface card
  - 16-core CPU
  - 128 GB RAM
  - multiple NVME SSD drives in a RAID array

- Use the AWS Common Runtime (AWS CRT) library for uploads using the AWS Command Line Interface or AWS SDK.

Optimize Amazon S3 transfer settings by configuring the parameters below. Set these values under the top level `s3` key in the AWS config file, default location `~/.aws/config`.

```
[default]
s3 =
    preferred_transfer_client = crt
    target_bandwidth = 100Gb/s
    max_concurrent_requests = 20
    multipart_chunksize = 16MB
```

Note that all Amazon S3 configuration values are indented and nested under the top level `s3` key.

    + Optional: You can set the above values programmatically using the `aws configure set` command. For example, to set the above values for the default profile, you can run the following commands instead:



    ```
    aws configure set default.s3.preferred_transfer_client crt
    aws configure set default.s3.target_bandwidth 100Gb/s
    aws configure set default.s3.max_concurrent_requests 20
    aws configure set default.s3.multipart_chunksize 16MB
    ```

- To programmatically set these values for a profile other than default, provide the `--profile` flag. For example, to set configuration for a profile named `test-profile`, runa command like the example below.

```
aws configure set s3.max_concurrent_requests 20 --profile test-profile
```

- Enable BBR (Linux) on the device for better throughput.

```
sysctl -w net.core.default_qdisc=fq
sysctl -w net.ipv4.tcp_congestion_control=bbr
```

## More information

For more information about AWS command line Amazon S3 configurations to optimize your network connectivity and performance, refer to the following resources.

- [AWS CLI Amazon S3 Configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/topic/s3-config.html "https://awscli.amazonaws.com/v2/documentation/api/latest/topic/s3-config.html") in the **AWS CLI Command Reference**
- [Use a performant Amazon S3 client: AWS CRT-based client](../../../sdk-for-java/latest/developer-guide/crt-based-s3-client.md "../../../sdk-for-java/latest/developer-guide/crt-based-s3-client.md") in the **Amazon S3Amazon AppStream SDK for Java**
- [How do I optimize performance when I use AWS CLI to upload large files to Amazon S3?](https://repost.aws/knowledge-center/s3-upload-large-files "https://repost.aws/knowledge-center/s3-upload-large-files") in the **AWS Knowledge Center**
