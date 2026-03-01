# Dynamic Application Framework Thrift Definitions and Named Pipe Name

Thrift enables you to use simple definition files provided by WorkSpaces Applications to
compile RPC clients. The RPC clients let you communicate with the WorkSpaces Applications agent
software running on a streaming instance. For information about how to compile
the RPC client for your language, see the [Apache Thrift documentation](https://thrift.apache.org/docs/ "https://thrift.apache.org/docs/").
After you compile the Thrift libraries for the language of your choice, build a
Thrift client by using the Named Pipe transport. Use
D56C0258-2173-48D5-B0E6-1EC85AC67893 as the pipe name.

## AppStreamServer.thrift

```
namespace netstd AppStream.ApplicationCatalogService.Model

const string ServiceEndpoint = "D56C0258-2173-48D5-B0E6-1EC85AC67893";


struct AddApplicationsRequest
{
    1: required string userSid;
    2: required list<Application> applications;
}

struct AddApplicationsResponse
{
}

struct RemoveApplicationsRequest
{
    1: required string userSid;
    2: required list<string> applicationIds;
}

struct RemoveApplicationsResponse
{
}

struct ClearApplicationsRequest
{
    1: required string userSid;
}

struct ClearApplicationsResponse
{
}

struct Application
{
    1: required string id;
    2: required string displayName;
    3: required string launchPath;
    4: required string iconData;
    5: string launchParams;
    6: string workingDirectory;
}

exception AppStreamClientException
{
    1: string errorMessage,
    2: ErrorCode errorCode
}

exception AppStreamServerException
{
    1: string errorMessage,
    2: ErrorCode errorCode
}

enum ErrorCode
{
}

service ApplicationCatalogService
{
    AddApplicationsResponse AddApplications(1:AddApplicationsRequest request)
    throws (1: AppStreamClientException ce, 2: AppStreamServerException se),

    RemoveApplicationsResponse RemoveApplications(1:RemoveApplicationsRequest request)
    throws (1: AppStreamClientException ce, 2: AppStreamServerException se),

    ClearApplicationsResponse ClearApplications(1:ClearApplicationsRequest request)
    throws (1: AppStreamClientException ce, 2: AppStreamServerException se),
}
```
