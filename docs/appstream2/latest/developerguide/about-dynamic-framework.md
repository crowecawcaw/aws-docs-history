# About the Dynamic Application

Framework

The dynamic application framework uses the [Apache Thrift software framework](https://thrift.apache.org/ "https://thrift.apache.org/")
for inter-process messaging. It is exposed through Named Pipes in Windows. Using
the Thrift framework allows you to build your dynamic app provider in your
software development language of choice. The dynamic application framework
consists of three API operations: `AddApplications`,
`RemoveApplications`, and `ClearApplications`.
