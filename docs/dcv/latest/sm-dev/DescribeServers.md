# DescribeServers

Describes one or more Amazon DCV servers.

###### Topics

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Example](#example "#example")

## Request parameters

**`ServerIds`**

The IDs of the Amazon DCV servers to describe. If no IDs are specified, all servers are
returned in paginated output.

Type: Array of strings

Required: No

**`NextToken`**

The token to use to retrieve the next page of results.

Type: String

Required: No

**`MaxResults`**

The maximum number of results to be returned by the request in paginated output. When
this parameter is used, the request returns only the specified number of
results in a single page along with a `NextToken` response
element. The remaining results of the initial request can be seen by
sending another request with the returned `NextToken`
value.

Valid range: 1 - 1000

Default: 1000

Type: Integer

Required: No

## Response parameters

**`RequestId`**

The unique ID of the request.

**`Servers`**

Information about the Amazon DCV servers. This data structure includes the following
nested response parameters:

**`Id`**

The unique ID of the Amazon DCV server.

**`Ip`**

The IP address of the Amazon DCV server.

**`Hostname`**

The hostname of the Amazon DCV server.

**`Endpoints`**

Information about the Amazon DCV server endpoints. This data structure includes
the following nested response parameters:

**`IpAddress`**

The IP address of the server endpoint.

**`Port`**

The port of the server endpoint.

**`Protocol`**

The protocol used by the server endpoint. Possible values include:

- `HTTP` — The endpoint uses the WebSocket (TCP) protocol.
- `QUIC` — The endpoint uses the QUIC (UDP) protocol.

**`WebUrlPath`**

The web URL path of the server endpoint. Available for the HTTP protocol only.

**`Version`**

The version of the Amazon DCV server.

**`SessionManagerAgentVersion`**

The version Session Manager Agent running on the Amazon DCV server.

**`Availability`**

The availability of the Amazon DCV server. Possible values include:

- `AVAILABLE` — The server is available and ready for session
  placement.
- `UNAVAILABLE` — The server is unavailable and can't accept
  session placement.

**`UnavailabilityReason`**

The reason for the Amazon DCV server's unavailability. Possible values include:

- `SERVER_FULL` — The Amazon DCV server has reached the maximum number of
  concurrent sessions that it can run.
- `SERVER_CLOSED` — The Amazon DCV server has been made unavailable using the
  **CloseServer** API.
- `UNREACHABLE_AGENT` — The Session Manager Broker can't communicate with the
  Session Manager Agent on the Amazon DCV server.
- `UNHEALTHY_DCV_SERVER` — The Session Manager Agent can't communicate with
  the Amazon DCV server.
- `EXISTING_LOGGED_IN_USER` — (Windows Amazon DCV servers only) A user
  is currently logged in to the Amazon DCV server using RDP.
- `UNKNOWN` — The Session Manager Broker is unable to determine the reason.

**`ConsoleSessionCount`**

The number of console sessions on the Amazon DCV server.

**`VirtualSessionCount`**

The number of virtual sessions on the Amazon DCV server.

**`Host`**

Information about the host server on which the Amazon DCV server is running. This data structure
includes the following nested response parameters:

**`Os`**

Information about host server's operating system. This data structure includes
the following nested response parameters:

**`Family`**

The operating system family. Possible values include:

- `windows` — The host server is running a
  Windows operating system.
- `linux` — The host server is running a
  Linux operating system.

**`Name`**

The name of the operating system.

**`Version`**

The version of the operating system.

**`KernelVersion`**

(Linux only) The kernel version of the operating system.

**`BuildNumber`**

(Windows only) The build number of the operating system.

**`Memory`**

Information about the host server's memory. This data structure includes the
following nested response parameters:

**`TotalBytes`**

The total memory, in bytes, on the host server.

**`UsedBytes`**

The used memory, in bytes, on the host server.

**`Swap`**

Information about the host server's swap file. This data structure includes the
following nested response parameters:

**`TotalBytes`**

The total swap file size, in bytes, on the host server.

**`UsedBytes`**

The used swap file size, in bytes, on the host server.

**`Aws`**

Only for Amazon DCV servers running on an Amazon EC2 instance. AWS-specific information.
This data structure includes the following nested response parameters:

**`Region`**

The AWS Region of the Amazon EC2 instance.

**`Ec2InstanceType`**

The type of Amazon EC2 instance.

**`Ec2InstanceId`**

The ID of the Amazon EC2 instance.

**`Ec2ImageId`**

The ID of the Amazon EC2 image.

**`CpuInfo`**

Information about the host server's CPUs. This data structure includes the following
nested response parameters:

**`Vendor`**

The vendor of the host server's CPU.

**`ModelName`**

The model name of the host server's CPU.

**`Architecture`**

The architecture of the host server's CPU.

**`NumberOfCpus`**

The number of CPUs on the host server.

**`PhysicalCorePerCpu`**

The number of CPU cores per CPU.

**`CpuLoadAverage`**

Information about the host server's CPU load. This data structure includes the
following nested response parameters:

**`OneMinute`**

The average CPU load over the last 1-minute period.

**`FiveMinutes`**

The average CPU load over the last 5-minute period.

**`FifteenMinutes`**

The average CPU load over the last 15-minute period.

**`Gpus`**

Information about the host server's GPUs. This data structure includes the following
nested response parameters:

**`Vendor`**

The vendor of the host server's GPU.

**`ModelName`**

The model name of the host server's GPU.

**`LoggedInUsers`**

The users that are currently logged in to the host server. This data structure includes the
following nested response parameter:

**`Username`**

The user name of the logged in user.

**`Tags`**

The tags assigned to the server. This data structure includes the following nested response parameters:

**`Key`**

The tag key.

**`Value`**

The tag value.

## Example

Python

###### Request

The following example describes all available Amazon DCV servers. The results are paginated
to show two results per page.

```
from swagger_client.models.describe_servers_request_data import DescribeServersRequestData

def get_servers_api():
    api_instance = swagger_client.ServersApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

def describe_servers(server_ids=None, next_token=None, max_results=None):
    request = DescribeServersRequestData(server_ids=server_ids, next_token=next_token, max_results=max_results)
    print('Describe Servers Request:', request)
    api_instance = get_servers_api()
    api_response = api_instance.describe_servers(body=request)
    print('Describe Servers Response', api_response)

def main():
    describe_servers(max_results=2)
```

###### Response

The following is the sample output.

```
{
    "RequestId": "request-id-123",
    "Servers": [
        {
            "Id": "ServerId123",
            "Ip": "1.1.1.123",
            "Hostname": "node001",
            "DefaultDnsName": "node001",
            "Endpoints": [
                {
                    "IpAddress": "x.x.x.x",
                    "Port": 8443,
                    "WebUrlPath": "/",
                    "Protocol": "HTTP"
                }
            ],
            "Version": "2021.0.10000",
            "SessionManagerAgentVersion": "2021.0.300",
            "Availability": "UNAVAILABLE",
            "UnavailabilityReason": "SERVER_FULL",
            "ConsoleSessionCount": 1,
            "VirtualSessionCount": 0,
            "Host": {
                "Os": {
                    "Family": "windows",
                    "Name": "Windows Server 2016 Datacenter",
                    "Version": "10.0.14393",
                    "BuildNumber": "14393"
                },
                "Memory": {
                    "TotalBytes": 8795672576,
                    "UsedBytes": 1743886336
                },
                "Swap": {
                    "TotalBytes": 0,
                    "UsedBytes": 0
                },
                "Aws": {
                    "Region": "us-west-2b",
                    "EC2InstanceType": "t2.large",
                    "EC2InstanceId": "i-123456789",
                    "EC2ImageId": "ami-12345678987654321"
                },
                "CpuInfo": {
                    "Vendor": "GenuineIntel",
                    "ModelName": "Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz",
                    "Architecture": "x86_64",
                    "NumberOfCpus": 2,
                    "PhysicalCoresPerCpu": 3
                },
                "CpuLoadAverage": {
                    "OneMinute": 0.04853546,
                    "FiveMinutes": 0.21060601,
                    "FifteenMinutes": 0.18792416
                },
                "Gpus": [],
                "LoggedInUsers": [
                    {
                        "Username": "Administrator"
                    }
                ]
            },
            "Tags": [
                {
                    "Key": "color",
                    "Value": "pink"
                },
                {
                    "Key": "dcv:os-family",
                    "Value": "windows"
                },
                {
                    "Key": "size",
                    "Value": "small"
                },
                {
                    "Key": "dcv:max-virtual-sessions",
                    "Value": "0"
                }
            ]
        },
        {
            "Id": "server-id-12456897",
            "Ip": "1.1.1.145",
            "Hostname": "node002",
            "DefaultDnsName": "node002",
            "Endpoints": [
                {
                    "IpAddress": "x.x.x.x",
                    "Port": 8443,
                    "WebUrlPath": "/",
                    "Protocol": "HTTP"
                },
                {
                    "IpAddress": "x.x.x.x",
                    "Port": 8443,
                    "Protocol": "QUIC"
                }
            ],
            "Version": "2021.0.10000",
            "SessionManagerAgentVersion": "2021.0.0",
            "Availability": "AVAILABLE",
            "ConsoleSessionCount": 0,
            "VirtualSessionCount": 5,
            "Host": {
                "Os": {
                    "Family": "linux",
                    "Name": "Amazon Linux",
                    "Version": "2",
                    "KernelVersion": "4.14.203-156.332.amzn2.x86_64"
                },
                "Memory": {
                    "TotalBytes": 32144048128,
                    "UsedBytes": 2184925184
                },
                "Swap": {
                    "TotalBytes": 0,
                    "UsedBytes": 0
                },
                "Aws": {
                    "Region": "us-west-2a",
                    "EC2InstanceType": "g3s.xlarge",
                    "EC2InstanceId": "i-123456789",
                    "EC2ImageId": "ami-12345678987654321"
                },
                "CpuInfo": {
                    "Vendor": "GenuineIntel",
                    "ModelName": "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz",
                    "Architecture": "x86_64",
                    "NumberOfCpus": 4,
                    "PhysicalCoresPerCpu": 2
                },
                "CpuLoadAverage": {
                    "OneMinute": 2.24,
                    "FiveMinutes": 0.97,
                    "FifteenMinutes": 0.74
                },
                "Gpus": [
                    {
                        "Vendor": "NVIDIA Corporation",
                        "ModelName": "GM204GL [Tesla M60]"
                    }
                ],
                "LoggedInUsers": [
                    {
                        "Username" : "user45687"
                    },
                    {
                        "Username" : "user789"
                    }
                ]
            },
            "Tags": [
                {
                    "Key": "size",
                    "Value": "big"
                },
                {
                    "Key": "dcv:os-family",
                    "Value": "linux"
                },
                {
                    "Key": "dcv:max-virtual-sessions",
                    "Value": "10"
                },
                {
                    "Key": "color",
                    "Value": "blue"
                }
            ]
        }
    ]
}
```
