# What is a stream?

In AWS IoT, a _stream_ is a publicly addressable resource that is an abstraction for a list of
files that can be transferred to an IoT device. A typical stream contains the following information:

- **An Amazon Resource Name (ARN)** that uniquely identifies a stream at a
  given time. This ARN has the pattern
  `arn:`partition`:iot:`region`:`account-ID`:stream/`stream ID``.
- **A stream ID** that identifies your stream and is used (and usually
  required) in AWS Command Line Interface (AWS CLI) or SDK commands.
- **A stream description** that provides a description of the stream resource.
- **A stream version** that identifies a particular version of the stream.
  Because stream data can be modified immediately before devices start the data transfer, the stream version
  can be used by the devices to enforce a consistency check.
- **A list of files** that can be transferred to
  devices. For each file in the list, the stream records a file ID, the file size,
  and the address information of the file, which consists of, for example, the
  Amazon S3 bucket name, object key, and object version.
- **An AWS Identity and Access Management (IAM) role** that grants AWS IoT
  MQTT-based file delivery the permission to read stream files stored in data storage.
  AWS IoT MQTT-based file delivery provides the following functionality so that devices can transfer data from the AWS
  Cloud:

- Data transfer using the MQTT protocol.
- Support for JSON or CBOR formats.
- The ability to describe a stream ([`DescribeStream`](mqtt-based-file-delivery-in-devices.md#mqtt-based-file-delivery-describe-stream "mqtt-based-file-delivery-in-devices.md#mqtt-based-file-delivery-describe-stream")
  API) to get a stream file list, stream version, and related information.
- The ability to send data in small blocks ([`GetStream`](mqtt-based-file-delivery-in-devices.md#mqtt-based-file-delivery-get-getstream "mqtt-based-file-delivery-in-devices.md#mqtt-based-file-delivery-get-getstream")
  API) so that devices with hardware constraints can receive the blocks.
- Support for a dynamic block size per request, to support devices that have different memory
  capacities.
- Optimization for concurrent streaming requests when multiple devices request data blocks from the
  same stream file.
- Amazon S3 as data storage for stream files.
- Support for data transfer log publishing from AWS IoT MQTT-based file delivery to CloudWatch.
  For MQTT-based file delivery quotas, see [AWS IoT Core Service Quotas](../../../general/latest/gr/iot-core.md#limits_iot "../../../general/latest/gr/iot-core.md#limits_iot") in the _AWS General Reference_.
