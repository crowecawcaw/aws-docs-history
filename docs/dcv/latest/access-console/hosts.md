# Hosts

On the **Hosts** page, you can view a list of host
machines (either cloud or on-premises) you have installed Amazon DCV servers configured with
Amazon DCV Session Manager.

Before your users can connect to a Amazon DCV session, you must have hosts available for
users to create sessions on. You can't spin up hosts, install Amazon DCV servers on hosts, or
configure them with the Amazon DCV Session Manager from the console. For more information
about installing Amazon DCV servers, see [Installing the Amazon DCV server](../adminguide/setting-up-installing.md "../adminguide/setting-up-installing.md").

You can configure the visible fields in the top navigation bar by selecting the gear
icon. To view more details in a split panel view, select a session and then click the
caret (**^**) icon at the bottom-right corner of the page.

![Host management interface showing Windows and Linux servers with memory usage and availability status.](images/hosts.png)

## Host information

For more information about the requirements and details of the Amazon DCV servers, see
Amazon DCV Servers and DescribeServers.

### Host Details

![Host details showing Windows 10 OS information, memory usage, and swap space allocation.](images/hosts-operating-sys.png)

| Property                | Description                                                                                                                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Family                  | The host operating system family that the Amazon DCV server is<br>running on, such as Windows, Linux or macOS<br>(`Host.OS.Family` in the<br>[DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                        |
| Hostname                | The hostname of the host server that the Amazon DCV server is<br>running on (`Servers.Hostname` in the<br>[DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                                           |
| Name                    | The name of the host server operating system that the<br>Amazon DCV server is running on (`Host.OS.Name` in the<br>[DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                                  |
| Version                 | The version of the host server operating system that the<br>Amazon DCV server is running on (`Host.OS.Version` in<br>the [DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                            |
| Kernel version          | (Linux only) The kernel version of the host server<br>operating system that the Amazon DCV server is running on<br>(`Host.OS.KernelVersion` in the<br>[DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).               |
| Build number            | (Windows only) The build number of the host server<br>operating system that the Amazon DCV server is running on<br>(`Host.OS.BuildNumber` in the<br>[DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                 |
| LoggedInUsers           | The usernames of the users that are currently logged into<br>the host server (`Host.OS.LoggedInUsers` in the<br>[DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                                     |
| Memory                  | Information about the host server’s memory, in gigabytes. This information is<br>displayed as [Used GB/Total GB]<br>(`Memory.UsedBytes` /<br>`Memory/TotalBytes` in the [DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md")). |
| Memory<br>• Total bytes | The total memory, in bytes, on the host server that the<br>Amazon DCV server is running on (`Memory.TotalBytes`<br>in the [DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                           |
| Memory<br>• Used bytes  | The used memory, in bytes, on the host server that the<br>Amazon DCV server is running on (`Memory.UsedBytes` in<br>the [DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                             |
| Swap<br>• Total bytes   | The total swap file size, in bytes, on the host server<br>that the Amazon DCV server is running on<br>(`Swap.TotalBytes` in the<br>[DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                  |
| Swap<br>• Used bytes    | The used swap file size, in bytes, on the host server that<br>the Amazon DCV server is running on (`Swap.UsedBytes`<br>in the [DescribeServers API](../sm-dev/DescribeServers.md "../sm-dev/DescribeServers.md") API).                                       |

### AWS information

![AWS EC2 instance details showing region, instance type, ID, and image ID.](images/hosts-aws.png)

| Property          | Description                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Region            | The Region of the Amazon EC2. This parameter only applies for<br>customers hosting on AWS, and will not be shown to<br>customers hosting on-premise (`Host.Aws.Region`<br>in the `DescribeServers` API).                |
| EC2 Instance Type | The type of Amazon EC2 instance. This parameter only applies<br>for customers hosting on AWS, and will not be shown to<br>customers hosting on-premise<br>(`Host.Aws.Ec2InstanceType` in the<br>`DescribeServers` API). |
| EC2 Image ID      | The ID of the Amazon EC2 image. This parameter only applies for<br>customers hosting on AWS, and will not be shown to<br>customers hosting on-premise<br>(`Host.Aws.Ec2IMAGEId` in the<br>`DescribeServers` API).       |

### Amazon DCV server

![DCV server details showing name, ID, IP, version, and session information.](images/hosts-dcv-server.png)

| Property                      | Description                                                                                                                                                                                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                            | The unique ID of the Amazon DCV server (`Servers.Id` in the<br>`DescribeServers` API).                                                                                                                                                                                                              |
| Availability                  | The availability of the Amazon DCV server<br>(`Servers.Availability` in the<br>`DescribeServers` API). Possible values<br>include:<br>• AVAILABLE — The server is available and<br>ready for session placement.<br>• UNAVAILABLE — The server is unavailable and<br>can't accept session placement. |
| Version                       | The version of the Amazon DCV server<br>(`Servers.Version` in the<br>`DescribeServers` API).                                                                                                                                                                                                        |
| Session Manager agent version | The version Session Manager agent running on the Amazon DCV<br>server (`Servers.SessionManagerAgentVersion` in<br>the `DescribeServers` API).                                                                                                                                                       |
| Console session count         | The number of console sessions on the Amazon DCV server<br>(`Servers.ConsoleSessionCount` in the<br>`DescribeServers` API).                                                                                                                                                                         |
| Virtual session count         | The number of virtual sessions on the Amazon DCV server<br>(`Servers.ConsoleSessionCount` in the<br>`DescribeServers` API).                                                                                                                                                                         |

### CPU

![CPU info showing GenuineIntel Xeon E5-2686 v4 processor with 2 CPUs, 2 cores each, and 0% load.](images/hosts-cpu.png)

| Property                         | Description                                                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vendor                           | The vendor of the host server's CPU<br>(`Host.CpuInfo.Vendor` in the<br>`DescribeServers` API).                                                   |
| Model                            | The model name of the host server's CPU<br>(`Host.CpuInfo.ModelName` in the<br>`DescribeServers` API).                                            |
| Architecture                     | The architecture of the host server's CPU<br>(`Host.CpuInfo.Architecture` in the<br>`DescribeServers` API).                                       |
| Number of vCPUs                  | The number of virtual CPUs on the host server<br>(`Host.CpuInfo.NumberOfCpus` in the<br>`DescribeServers` API).                                   |
| Number of physical cores per CPU | The number of physical CPUs on the host server.                                                                                                   |
| One minute average               | The average CPU load over the last 1 minute period of the<br>host server (`Host.CpuLoadAverage.OneMinute` in<br>the `DescribeServers` API).       |
| Five minute average              | The average CPU load over the last 5 minute period of the<br>host server (`Host.CpuLoadAverage.FiveMinutes` in<br>the `DescribeServers` API).     |
| Fifteen minute average           | The average CPU load over the last 15 minute period of the<br>host server (`Host.CpuLoadAverage.FifteenMinutes`<br>in the `DescribeServers` API). |

### GPU

![Table showing GPU information with "No GPUs found" message displayed.](images/hosts-gpu.png)

| Property | Description                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------- |
| Vendor   | The vendor of the host server's GPU<br>(`Host.Gpus.Vendor` in the<br>`DescribeServers` API).        |
| Model    | The model name of the host server's GPU<br>(`Host.Gpus.ModelName` in the<br>`DescribeServers` API). |

### Server endpoints

![Server endpoints table showing IP, Protocol, Port, and Web URL Path for HTTP and QUIC connections.](images/hosts-server-endpoints.png)

| Property     | Description                                                                                                                                                                                                                                                                 |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IP           | The IP address of the Amazon DCV server endpoint<br>(`Servers.Endpoints.IpAddress` in the<br>`DescribeServers` API).                                                                                                                                                        |
| Protocol     | The protocol used by the Amazon DCV server endpoint<br>(`Servers.Endpoints.Protocol` in the<br>`DescribeServers` API). Possible values<br>include:<br>• HTTP — The endpoint uses the WebSocket<br>(TCP) protocol.<br>• QUIC — The endpoint uses the QUIC (UDP)<br>protocol. |
| Port         | The port of the Amazon DCV server endpoint<br>(`Servers.Endpoints.Port` in the<br>`DescribeServers` API).                                                                                                                                                                   |
| Web URL path | The web URL path of the Amazon DCV server endpoint. Available<br>for the HTTP protocol only<br>(`Servers.Endpoints.WebUrlPath` in the<br>`DescribeServers` API).                                                                                                            |
| Tags         | The tags assigned to the host server that the Amazon DCV server<br>is running on (`Host.Tags` in the<br>`DescribeServers` API).                                                                                                                                             |
