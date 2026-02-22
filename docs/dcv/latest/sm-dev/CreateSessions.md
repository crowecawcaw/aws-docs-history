# CreateSessions

Creates a new Amazon DCV session with the specified details.

###### API actions

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Example](#example "#example")

## Request parameters

**`Name`**

The name for the session.

Type: String

Required: Yes

**`Owner`**

The name of the session owner. This must be the name of an existing user on the target Amazon DCV server.

Type: String

Required: Yes

**`Type`**

The session type. For more information about the types of sessions, see [Introduction to Amazon DCV Sessions](../adminguide/managing-sessions.md "../adminguide/managing-sessions.md") in the
_Amazon DCV Administrator Guide_.

Valid values: CONSOLE | VIRTUAL

Type: String

Required: Yes

**`InitFile`**

Supported with virtual sessions on Linux Amazon DCV servers. It is not supported with console
sessions on Windows and Linux Amazon DCV servers. The path to custom script on the Amazon DCV server to run
for initializing the session when it is created. The file path is relative to the init directory
specified for the `agent.init_folder` Agent configuration parameter. If the file is in
the specified init directory, specify the file name only. If the file is not in the specified init
directory, specify the relative path. For more information, see [Agent configuration file](../sm-admin/agent-file.md "../sm-admin/agent-file.md") in the _Amazon DCV Session Manager
Administrator Guide_.

Type: String

Required: No

**`MaxConcurrents`**

The maximum number of concurrent Amazon DCV clients.

Type: Integer

Required: No

**`DcvGlEnabled`**

Indicates whether the virtual session is configured to use hardware-based OpenGL.
Supported with virtual sessions only. This parameter is not supported with Windows
Amazon DCV servers.

Valid values: true | false

Type: Boolean

Required: No

**`PermissionsFile`**

The Base64-encoded contents of the permissions file. Defaults to the server defaults if omitted.
For more information, see [Configuring Amazon DCV
Authorization](../adminguide/security-authorization.md "../adminguide/security-authorization.md") in the _Amazon DCV Administrator Guide_.

Type: String

Required: No

**`EnqueueRequest`**

Indicates whether to queue the request if it can't be immediately fulfilled.

Type: Boolean

Default: false

Required: No

**`AutorunFile`**

Supported with console sessions on Windows Amazon DCV servers and virtual sessions
on Linux Amazon DCV servers. It is not supported with console sessions on Linux Amazon DCV
servers.

The path to a file on the host server that is to be run inside the
session. The file path is relative to the autorun directory specified for the
`agent.autorun_folder` Agent configuration parameter. If the file is
in the specified autorun directory, specify the file name only. If the file is not
in the specified autorun directory, specify the relative path. For more information,
see [Agent
configuration file](../sm-admin/agent-file.md "../sm-admin/agent-file.md") in the _Amazon DCV Session Manager Administrator
Guide_.

The file is run on behalf of the specified **Owner**.
The specified owner must have permission to run the file on the server. On Windows
Amazon DCV servers, the file is run when the owner logs into the session. On Linux Amazon DCV
servers, the file is run when the session is created.

Type: String

Required: No

**`AutorunFileArguments`**

Supported with virtual sessions on Linux Amazon DCV servers. It is not supported in console
sessions on Windows and Linux Amazon DCV servers. Command-line arguments passed to **AutorunFile** upon its execution inside the session. Arguments are passed in
the order they appear into the given array. Maximum allowed number of arguments and maximum allowed
length of each argument can be configured. For more information, see [Broker configuration file](../sm-admin/broker-file.md "../sm-admin/broker-file.md") in the _Amazon DCV Session Manager
Administrator Guide_.

Type: Array of strings

Required: No

**`DisableRetryOnFailure`**

Indicates whether to not retry the create session request after it fails on a Amazon DCV host
for any reason. For more information about create session retry mechanism, see [Broker configuration file](../sm-admin/broker-file.md "../sm-admin/broker-file.md") in
the _Amazon DCV Session Manager Administrator Guide_.

Type: Boolean

Default: false

Required: No

**`Requirements`**

The requirements that the server must satisfy in order to place the session. The requirements
can include server tags and/or server properties, both server tags and server properties are
retrieved by calling the **DescribeServers** API.

Requirements condition expressions:

- `a` **!=** `b` true if `a` is not equal to `b`
- `a` **=** `b` true if `a` is equal to `b`
- `a` **>** `b` true if `a` is greater than `b`
- `a` **>=** `b` true if `a` is greater than or equal to `b`
- `a` **<** `b` true if `a` is less than `b`
- `a` **<=** `b` true if `a` is less than or equal to `b`
- `a` **=** `b` true if `a` contains the string `b`

Requirements boolean operators:

- `a` **and**
  `b` true if `a` and `b`
  are true
- `a` **or**
  `b` true if `a` or `b`
  are true
- **not** `a` true if
  `a` is false

The tag keys must be prefixed by `tag:`, the server properties must be prefixed by
`server:`.The requirements expressions supports parenthesis `()`.

Requirements examples:

- `tag:color = 'pink' and (server:Host.Os.Family = 'windows' or tag:color := 'red')`
- `"server:Host.Aws.Ec2InstanceType := 't2' and server:Host.CpuInfo.NumberOfCpus >= 2"`

Numerical values can be specified using the exponential notation, for example:
`"server:Host.Memory.TotalBytes > 1024E6"`.

The supported server properties are:

- `Id`
- `Hostname`
- `Version`
- `SessionManagerAgentVersion`
- `Host.Os.BuildNumber`
- `Host.Os.Family`
- `Host.Os.KernelVersion`
- `Host.Os.Name`
- `Host.Os.Version`
- `Host.Memory.TotalBytes`
- `Host.Memory.UsedBytes`
- `Host.Swap.TotalBytes`
- `Host.Swap.UsedBytes`
- `Host.CpuLoadAverage.OneMinute`
- `Host.CpuLoadAverage.FiveMinutes`
- `Host.CpuLoadAverage.FifteenMinutes`
- `Host.Aws.Ec2InstanceId`
- `Host.Aws.Ec2InstanceType`
- `Host.Aws.Region`
- `Host.Aws.Ec2ImageId`
- `Host.CpuInfo.Architecture`
- `Host.CpuInfo.ModelName`
- `Host.CpuInfo.NumberOfCpus`
- `Host.CpuInfo.PhysicalCoresPerCpu`
- `Host.CpuInfo.Vendor`

Type: String

Required: No

**`StorageRoot`**

Specifies the path to the folder used for session storage. For more information about the
Amazon DCV session storage, see [Enabling Session Storage](../adminguide/manage-storage.md "../adminguide/manage-storage.md") in the
_Amazon DCV Administrator Guide_.

Type: String

Required: No

## Response parameters

**`Id`**

The unique ID of the session.

**`Name`**

The session name.

**`Owner`**

The session owner.

**`Type`**

The type of session.

**`State`**

The state of the session. If the request completes successfully, the session enters the
`CREATING` state.

**`Substate`**

The substate of the session. If the request completes successfully, the substate enters the
`SESSION_PLACING` substate.

## Example

Python

###### Request

The following example creates three sessions.

```

from swagger_client.models.create_session_request_data import CreateSessionRequestData

def get_sessions_api():
    api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

def create_sessions(sessions_to_create):
    create_sessions_request = list()
    for name, owner, session_type, init_file_path, autorun_file, autorun_file_arguments, max_concurrent_clients,\
            dcv_gl_enabled, permissions_file, requirements, storage_root in sessions_to_create:
        a_request = CreateSessionRequestData(
            name=name, owner=owner, type=session_type,
            init_file_path=init_file_path, autorun_file=autorun_file, autorun_file_arguments=autorun_file_arguments, max_concurrent_clients=max_concurrent_clients,
            dcv_gl_enabled=dcv_gl_enabled, permissions_file=permissions_file, requirements=requirements, storage_root=storage_root)
        create_sessions_request.append(a_request)

    api_instance = get_sessions_api()
    print('Create Sessions Request:', create_sessions_request)
    api_response = api_instance.create_sessions(body=create_sessions_request)
    print('Create Sessions Response:', api_response)

def main():
    create_sessions([
    ('session1', 'user1', 'CONSOLE', None, None, None, 1, None, '/dcv/permissions.file', "tag:os = 'windows' and server:Host.Memory.TotalBytes > 1024", "/storage/root"),
    ('session2', 'user1', 'VIRTUAL', None, 'myapp.sh', None, 1, False, None, "tag:os = 'linux'", None),
    ('session3', 'user1', 'VIRTUAL', '/dcv/script.sh', 'myapp.sh', ['argument1', 'argument2'], 1, False, None, "tag:os = 'linux'", None),
])
```

###### Response

The following is the sample output.

```
{
              "RequestId": "e32d0b83-25f7-41e7-8c8b-e89326ecc87f",
    "SuccessfulList": [
    {
            "Id": "78b45deb-1163-46b1-879b-7d8fcbe9d9d6",
            "Name": "session1",
            "Owner": "user1",
            "Type": "CONSOLE",
            "State": "CREATING"
    },
    {
            "Id": " a0c743c4-9ff7-43ce-b13f-0c4d55a268dd",
            "Name": "session2",
            "Owner": "user1",
            "Type": "VIRTUAL",
            "State": "CREATING"
    },
    {
            "Id": " 10311636-df90-4cd1-bcf7-474e9675b7cd",
            "Name": "session3",
            "Owner": "user1",
            "Type": "VIRTUAL",
            "State": "CREATING"
    }
    ],
    "UnsuccessfulList": [
    ]
}
```
