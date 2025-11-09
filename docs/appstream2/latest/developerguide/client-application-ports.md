# IP Address and Port Requirements for WorkSpaces Applications User Devices

WorkSpaces Applications users' devices require outbound access on port 443 (TCP) and port 8433
(UDP) when using the internet endpoints, and if you are using DNS servers for domain
name resolution, port 53 (UDP).

- Port 443 is used for HTTPS communication between WorkSpaces Applications users' devices and
  streaming instances when using the internet endpoints. Typically, when end
  users browse the web during streaming sessions, the web browser randomly
  selects a source port in the high range for streaming traffic. You must
  ensure that return traffic to this port is allowed.

###### Note

WorkSpaces Applications uses WebSockets on port 443.

- Port 8433 is used for UDP HTTPS communication between WorkSpaces Applications users'
  devices and streaming instances when using the internet endpoints. This is
  currently only supported in the Windows native client. UDP is not supported
  if you are using VPC endpoints.

###### Note

Streaming through interface VPC endpoints requires additional ports.
For more information, see [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md "creating-streaming-from-interface-vpc-endpoints.md").

- Port 53 is used for communication between WorkSpaces Applications users' devices and your
  DNS servers. The port must be open to the IP addresses for your DNS servers
  so that public domain names can be resolved. This port is optional if you
  are not using DNS servers for domain name resolution.
