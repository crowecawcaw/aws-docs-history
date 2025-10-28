# Creating a CDI flow

A CDI flow transports high-quality uncompressed or lightly compressed content into and
out of the AWS Cloud. You can configure a CDI flow to use JPEG XS to transport lightly
compressed content. The content is demuxed into separate media streams for audio, video,
or ancillary data. Each CDI flow can use multiple media streams for the source and
multiple media streams for each output. MediaConnect uses AWS Cloud Digital Interface (AWS CDI) network
technology to transport content that adheres to the SMPTE 2110, part 22 transport
standard.

CDI flows only support sources from a virtual private cloud (VPC) that you set up
using Amazon VPC. You set up your VPC and then create a flow that has an interface to that
VPC.

MediaConnect doesn't support two sources on CDI flows. For redundancy with ST 2110
JPEG XS sources, you can specify two inbound VPC interfaces on an individual media
stream. For redundancy with CDI sources, create a second flow.

## Prerequisites

Before you begin this procedure, make sure that the following steps have been
completed:

- Review the suggested workflow shown in [Contribution for CDI flows](use-cases-cdi.md "use-cases-cdi.md").
- In Amazon VPC, set up your VPC and associated security groups. For more
  information about VPCs, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md"). For information about
  configuring security groups to work with your VPC interface, see [Security group
  considerations](vpc-interface-security-groups.md "vpc-interface-security-groups.md").
- In IAM, [set up MediaConnect as a
  trusted service](security-iam-trusted-entity.md "security-iam-trusted-entity.md").

## Procedure

### Create an AWS CDI flow (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose **Create
   flow**.
3. In the **Details** section, for **Name**,
   specify a name for your flow. This name will become part of the ARN for this
   flow.

###### Note

MediaConnect allows you to create multiple flows with the same name.
However, we encourage you to use unique flow names within an AWS Region to
help with organization. After you create a flow, you can't change the
name. 4. For **Availability Zone**, choose the Availability Zone where
your VPC subnet resides. 5. For **Flow size**, select **Large 4x**. 6. In the **Source** section, for **Source
type**, choose **VPC source**. 7. For **Name**, specify a name for your source. This value is
an identifier that is visible only on the MediaConnect console. 8. Skip to the **VPC interface** section. 9. For each VPC that you want to connect to the flow, do the following:

    1. Choose **Add VPC interface**.
    2. For **Name**, specify a name for your VPC interface.
     The name of the VPC interface must be unique within the flow.
    3. For **Type**, choose the type of network adapter that
     you want MediaConnect to use on this interface. If you want to use this
     interface for a CDI source or output, you must choose
     **EFA** as the type.
    4. For **Role ARN**, specify the Amazon Resource Name
     (ARN) of the role that you created when you set up MediaConnect as a
     trusted service.
    5. For **VPC**, choose the ID of the VPC that you want
     to use.


    ###### Note

    If you don't see the VPC that you want in the list, verify that
     the VPC has been set up in Amazon Virtual Private Cloud and that you have IAM
     permissions to view the VPC.
    6. For **Subnet**, choose the VPC subnet that you want
     MediaConnect to use to set up your VPC configuration. You must choose
     at least one and can choose as many as you want.
    7. For **Security groups**, specify the VPC security
     groups that you want MediaConnect to use to set up your VPC
     configuration. You must choose at least one security group.

10. For each media stream that you want to add to the flow, do the
    following:
    1.  In the **Media streams** section, choose
        **Add media stream**.
    2.  In the **Name** field, specify a descriptive name
        that will help you distinguish this media stream from others in the
        flow.
    3.  For **Description**, specify a description that will
        help you remember the use of this media stream.
    4.  For **Stream ID**, specify a unique identifier for
        the media stream.

    If the source or any of the outputs uses the CDI protocol, specify the
    value that is expected by the production and playout systems.

    If the source and all outputs use the ST 2110 JPEG XS protocol,
    specify a value that is unique to that of other media streams within the
    flow. 5. Choose **Advanced options** to display the additional
    options based on your stream type. 6. For specific instructions on the advanced options based on your stream
    type, choose one of the following tabs:

    Audio

        1. For **Stream type**, choose
         **Audio**.
        2. For **Media clock rate**, specify
         the sample rate for the stream. This value is
         measured in Hz.
        3. For **Language**, specify the
         language of the audio. This value should be in a
         format that the receiver recognizes.
        4. For **Channel order**, specify
         the format of the audio channel.
        5. Choose **Add media stream**.

    Video

        1. For **Stream type**, choose
         **Video**.


        For many fields, MediaConnect provides a default
         value that represents the recommended setting.
         Change the default value if needed.
        2. **Media clock rate** is the
         sample rate for the stream, and is set to 90000.
         This value is measured in Hz.
        3. For **Video format**, specify the
         resolution of the video.
        4. For **Exact framerate**, specify
         the frame rate of the video. This value should be
         represented in frames per second.
        5. For **Colorimetry**, specify the
         format that was used for the representation of color
         in the video.
        6. For **Scan mode**, specify the
         method that was used to scan the incoming video.




        	* Choose **Interlace** if the
        	 incoming video is interlaced (for example, 480i or
        	 1080i).
        	* Choose **Progressive** if
        	 the incoming video is progressive (for example,
        	 720p or 1080p).
        	* Choose **Progressive segmented
        	 frame** if the incoming video is PSF (for
        	 example, 1080psf).
        7. For **TCS**, specify the transfer
         characteristic system (TCS) that was used in the
         video.
        8. For **Range**, specify the
         encoding range of the video.
        9. For **PAR**, specify the pixel
         access ratio (PAR) of the video.
        10. Choose **Add media stream**.

    Ancillary data

        1. For **Stream type**, choose
         **Ancillary data**.
        2. **Media clock rate** is the
         sample rate for the stream, and is set to 90000.
         This value is measured in Hz.
        3. Choose **Add media stream**.

11. Scroll back up to the **Sources** section.
12. Determine which protocol your source uses.
13. For specific instructions based on your protocol, choose one of the following
    tabs:

CDI

    1. For **Protocol**, choose
     **CDI**.
    2. For **Description**, enter a description
     that will remind you later where this source is from. This
     might be the company name or notes about the setup.
    3. For **Inbound port**, specify the port
     that the flow will listen on for incoming content. This
     value can be anything from 1024 to 65535, with the exception
     of 2077 and 2088 (those ports are reserved for other
     protocols).
    4. For **VPC interface**, choose the name of
     the VPC interface that you want to use as the source.
    5. For each media stream that you want to use as part of the
     source, do the following.




    	1. For **Media stream name**, choose
    	 the name of the media stream.
    	2. For **Encoding name**, accept the
    	 default value.




    		* For ancillary data streams, the encoding
    		 name is `smpte291`.
    		* For audio streams, the encoding name is
    		 `pcm`.
    		* For video, the encoding name is
    		 `raw`.

ST 2110 JPEG XS

    1. For **Protocol**, choose **ST
     2110 JPEG XS**.
    2. For **Description**, enter a description
     that will remind you later where this source is from. This
     might be the company name or notes about the setup.
    3. For **Max sync buffer**, specify the size
     of the buffer that you want MediaConnect to use to sync
     incoming source data. This value is measured in milliseconds
     (ms).
    4. For **VPC interface name 1**, choose one
     of the VPC interfaces that you want to use as a
     source.
    5. For **VPC interface name 2**, choose a
     second VPC interface that you want to use as a source. There
     is no priority between VPC interfaces 1 and 2.
    6. For each media stream that you want to use as part of the
     source, do the following.




    	1. For **Media stream name**, choose
    	 the name of the media stream.
    	2. For **Encoding name**, accept the
    	 default value.




    		* For ancillary data streams, the encoding
    		 name is `smpte291`.
    		* For audio streams, the encoding name is
    		 `pcm`.
    		* For video, the encoding name is
    		 `jxsv`.
    	3. For **Inbound port**, specify the
    	 port that the flow will listen on for incoming
    	 content. This value can be anything from 1024 to
    	 65535, with the exception of 2077 and 2088 (those
    	 ports are reserved for other protocols).

14. At the bottom of the page, choose **Create flow**.

###### Note

The flow doesn't start automatically. You must [start the flow](flows-start.md "flows-start.md") manually. 15. [Add outputs](outputs-add-vpc.md "outputs-add-vpc.md") to specify where you want
MediaConnect to send the content.

### Create an AWS CDI flow (AWS CLI)

To use the AWS CLI to create a flow, you must use the `create-flow`
command. To simplify the flow creation, we suggest you use the
`create-flow` command with the `--cli-input-json` option.
The `--cli-input-json` option requires you to create a JSON file with the
necessary settings for your new flow. Step 1 of this procedure provides an example
of one possible way configure this JSON file. For more information about the
`create-flow` command and the `--cli-input-json` option,
see: [AWS CLI Command Reference create-flow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-flow.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-flow.html")

1. Create a JSON file that contains the details of the flow that you want to
   create.

The following example shows the structure for the contents of the file.
This example uses a JPEG XS source to create a AWS CDI output with the
following attributes:

    * 2 Amazon VPC interfaces, 1 EFA (Elastic Fabric Adapter) and 1 ENA
     (Elastic Network Adapter)
    * 1 video stream, 1 audio stream, and 1 ancillary data stream

```
{
    "Name": "`AwardsShow`",

    "MediaStreams": [
        {
            "Attributes": {
                "Fmtp": {
                    "Colorimetry": "`BT709`",
                    "ExactFramerate": "`60000/1001`",
                    "Par": "`1:1`",
                    "Range": "`NARROW`",
                    "ScanMode": "`progressive`",
                    "Tcs": "`SDR`"
                }
            },
            "ClockRate": `90000`,
            "MediaStreamId": `0`,
            "MediaStreamName": "`video-stream`",
            "MediaStreamType": "`video`",
            "VideoFormat": "`1080p`"
        },
        {
            "Attributes": {
                "Fmtp": {
                    "ChannelOrder": "`SMPTE2110.(ST)`"
                }
            },
            "ClockRate": `48000`,
            "MediaStreamId": `1`,
            "MediaStreamName": "`audio-stream`",
            "MediaStreamType": "`audio`"
        },
        {
            "ClockRate": `90000`,
            "MediaStreamId": `2`,
            "MediaStreamName": "`anc-stream`",
            "MediaStreamType": "`ancillary-data`"
        }
    ],

    "Outputs": [
        {
            "Name": "`cdi-output`",
            "Protocol": "`cdi`",
            "Description": "`cdi-output to medialive`",
            "Destination": "`198.51.100.5`",
            "MediaStreamOutputConfigurations": [
                {
                    "EncodingName": "`raw`",
                    "MediaStreamName": "`video-stream`"
                },
                {
                    "EncodingName": "`pcm`",
                    "MediaStreamName": "`audio-stream`"
                }
            ],
            "Port": `5000`,
            "VpcInterfaceAttachment": {
                "VpcInterfaceName": "`efa-name`"
            }
        }
    ],

    "Source": {
        "Name": "`jxs-input`",
        "Protocol": "`st2110-jpegxs`",
        "Description": "`jxs-input to cdi-output`",
        "MaxSyncBuffer": `100`,
        "MediaStreamSourceConfigurations": [
            {
                "EncodingName": "`jxsv`",
                "InputConfigurations": [
                    {
                        "InputPort": `5011`,
                        "Interface": {
                            "Name": "`efa-name`"
                        }
                    },
                    {
                        "InputPort": `5011`,
                        "Interface": {
                            "Name": "`ena-name`"
                        }
                    }
                ],
                "MediaStreamName": "`video-stream`"
            },
            {
                "EncodingName": "`pcm`",
                "InputConfigurations": [
                    {
                        "InputPort": `5001`,
                        "Interface": {
                            "Name": "`efa-name`"
                        }
                    },
                    {
                        "InputPort": `5001`,
                        "Interface": {
                            "Name": "`ena-name`"
                        }
                    }
                ],
                "MediaStreamName": "`audio-stream`"
            }
        ]
    },

    "VpcInterfaces": [
        {
            "Name": "`efa-name`",
            "NetworkInterfaceType": "`efa`",
            "RoleArn": "`arn:aws:iam::111122223333:role/MediaConnectAccessRole`",
            "SecurityGroupIds": [
                "`sg-1234567890abcdef0`"
            ],
            "SubnetId": "`subnet-abcdef01234567890`"
        },
        {
            "Name": "`ena-name`",
            "NetworkInterfaceType": "`ena`",
            "RoleArn": "`arn:aws:iam::111122223333:role/MediaConnectAccessRole`",
            "SecurityGroupIds": [
                "`sg-1234567890abcdef0`"
            ],
            "SubnetId": "`subnet-abcdef01234567890`"
        }
    ]
}
```

2. In the AWS CLI, use the `create-flow` command.

```
aws mediaconnect create-flow --cli-input-json file://`filename`.json --profile `YourProfile`
```

The following example shows the return value:

```
{
    "Flow": {
        "AvailabilityZone": "us-west-2a",
        "Description": "jxs-input to cdi-output",
        "EgressIp": "203.0.113.0",
        "Entitlements": [],
        "FlowArn": "arn:aws:mediaconnect:us-west-2:111122223333:flow:1-DwtfUlYOUVABAQNR-c94d84ce4215:AwardsShow",
        "MediaStreams": [
            {
                "Attributes": {
                    "Fmtp": {
                        "Colorimetry": "BT709",
                        "ExactFramerate": "60000/1001",
                        "Par": "1:1",
                        "Range": "NARROW",
                        "ScanMode": "progressive",
                        "Tcs": "SDR"
                    }
                },
                "ClockRate": 90000,
                "Fmt": 96,
                "MediaStreamId": 0,
                "MediaStreamName": "video-stream",
                "MediaStreamType": "video",
                "VideoFormat": "1080p"
            },
            {
                "Attributes": {
                    "Fmtp": {
                        "ChannelOrder": "SMPTE2110.(ST)"
                    }
                },
                "ClockRate": 48000,
                "Fmt": 97,
                "MediaStreamId": 1,
                "MediaStreamName": "audio-stream",
                "MediaStreamType": "audio"
            },
            {
                "ClockRate": 90000,
                "Fmt": 98,
                "MediaStreamId": 2,
                "MediaStreamName": "anc-stream",
                "MediaStreamType": "ancillary-data"
            }
        ],
        "Name": "AwardsShow",
        "Outputs": [
            {
                "Description": "cdi-output to medialive",
                "Destination": "198.51.100.5",
                "MediaStreamOutputConfigurations": [
                    {
                        "EncodingName": "raw",
                        "MediaStreamName": "video-stream"
                    },
                    {
                        "EncodingName": "pcm",
                        "MediaStreamName": "audio-stream"
                    }
                ],
                "Name": "cdi-output",
                "OutputArn": "arn:aws:mediaconnect:us-west-2:111122223333:output:1-DwtfUlYOUVABAQNR-c94d84ce4215:cdi-output",
                "Port": 5000,
                "Transport": {
                    "Protocol": "cdi"
                },
                "VpcInterfaceAttachment": {
                    "VpcInterfaceName": "efa-name"
                }
            }
        ],
        "Source": {
            "Description": "jxs-input to cdi-output",
            "MediaStreamSourceConfigurations": [
                {
                    "EncodingName": "jxs-input",
                    "InputConfigurations": [
                        {
                            "InputIp": "203.0.113.1",
                            "InputPort": 5011,
                            "Interface": {
                                "Name": "efa-name"
                            }
                        },
                        {
                            "InputIp": "203.0.113.2",
                            "InputPort": 5011,
                            "Interface": {
                                "Name": "ena-name"
                            }
                        }
                    ],
                    "MediaStreamName": "video-stream"
                },
                {
                    "EncodingName": "pcm",
                    "InputConfigurations": [
                        {
                            "InputIp": "203.0.113.3",
                            "InputPort": 5001,
                            "Interface": {
                                "Name": "efa-name"
                            }
                        },
                        {
                            "InputIp": "203.0.113.4",
                            "InputPort": 5001,
                            "Interface": {
                                "Name": "ena-name"
                            }
                        }
                    ],
                    "MediaStreamName": "audio-stream"
                }
            ],
            "Name": "jxs-input",
            "SourceArn": "arn:aws:mediaconnect:us-west-2:111122223333:source:1-DwtfUlYOUVABAQNR-c94d84ce4215:jxs-input",
            "Transport": {
                "MaxSyncBuffer": 100,
                "Protocol": "st2110-jpegxs"
            }
        },
        "Sources": [
            {
                "Description": "jxs-input to cdi-output",
                "MediaStreamSourceConfigurations": [
                    {
                        "EncodingName": "jxsv",
                        "InputConfigurations": [
                            {
                                "InputIp": "203.0.113.173",
                                "InputPort": 5011,
                                "Interface": {
                                    "Name": "efa-name"
                                }
                            },
                            {
                                "InputIp": "203.0.113.114",
                                "InputPort": 5011,
                                "Interface": {
                                    "Name": "ena-name"
                                }
                            }
                        ],
                        "MediaStreamName": "video-stream"
                    },
                    {
                        "EncodingName": "pcm",
                        "InputConfigurations": [
                            {
                                "InputIp": "203.0.113.173",
                                "InputPort": 5001,
                                "Interface": {
                                    "Name": "efa-name"
                                }
                            },
                            {
                                "InputIp": "203.0.113.114",
                                "InputPort": 5001,
                                "Interface": {
                                    "Name": "ena-name"
                                }
                            }
                        ],
                        "MediaStreamName": "audio-stream"
                    }
                ],
                "Name": "jxs-input",
                "SourceArn": "arn:aws:mediaconnect:us-west-2:111122223333:source:1-DwtfUlYOUVABAQNR-c94d84ce4215:jxs-input",
                "Transport": {
                    "MaxSyncBuffer": 100,
                    "Protocol": "st2110-jpegxs"
                }
            }
        ],
        "Status": "STANDBY",
        "VpcInterfaces": [
            {
                "Name": "efa-name",
                "NetworkInterfaceIds": [
                    "eni-0ae6ca9ea6673a2a7"
                ],
                "NetworkInterfaceType": "efa",
                "RoleArn": "arn:aws:iam::111122223333:role/MediaConnectAccessRole",
                "SecurityGroupIds": [
                    "sg-1234567890abcdef0"
                ],
                "SubnetId": "subnet-abcdef01234567890"
            },
            {
                "Name": "ena-name",
                "NetworkInterfaceIds": [
                    "eni-0cbabcf978eeb00a2"
                ],
                "NetworkInterfaceType": "ena",
                "RoleArn": "arn:aws:iam::111122223333:role/MediaConnectAccessRole",
                "SecurityGroupIds": [
                    "sg-1234567890abcdef0"
                ],
                "SubnetId": "subnet-abcdef01234567890"
            }
        ]
    }
}
```

## Next steps

Now that you've created a flow, complete these steps to start delivering your content:

- [Add outputs](outputs-add.md "outputs-add.md") to specify where you want
  MediaConnect flow to send your content
- [Grant entitlements](entitlements-grant.md "entitlements-grant.md") to allow
  users of other AWS accounts to subscribe to your content
- [Start your flow](flows-start.md "flows-start.md") to begin content
  delivery
