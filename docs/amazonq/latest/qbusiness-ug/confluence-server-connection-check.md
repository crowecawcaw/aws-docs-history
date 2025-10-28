# Checking Confluence (Server/Data Center)

connectivity

Before you sync your Confluence (Server/Data Center) data source connector after [configuring it](confluence-server-console.md "confluence-server-console.md"), we recommend you check the connection
between Amazon Q Business and Confluence (Server/Data Center). The following are the cURL commands you need
to check Confluence (Server/Data Center) connectivity.

###### Topics

- [Checking basic
  authentication connectivity](#confluence-server-connection-check-basic "#confluence-server-connection-check-basic")
- [Checking personal access
  token connectivity](#confluence-server-connection-check-pat "#confluence-server-connection-check-pat")

## Checking basic

authentication connectivity

To check connectivity for a Confluence (Server/Data Center) data source connector using basic
authentication, use the following cURL command:

```
curl --location '`https://<confluence_host-url>/wiki/rest/api/user/current`'
--header 'Authorization: Basic <`Base64 encoded username and password`>'
```

If your data source is connected as expected, the JSON response should resemble
the following:

```
{
    "type": "known",
    "accountId": "`accountId`",
    "accountType": "atlassian",
    "email": "`email`",
    "publicName": "Administrator",
    "profilePicture": {
        "path": "`/wiki/aa-avatar/<accountId>`",
        "width": 48,
        "height": 48,
        "isDefault": false
    },
    "displayName": "Administrator",
    "isExternalCollaborator": false,
    "_expandable": {
        "operations": "",
        "personalSpace": ""
    },
    "_links": {
        "self": "`https://<host_url>/wiki/rest/api/user?accountId=<accountId>`",
        "base": "`https://<host_url>/wiki`",
        "context": "/wiki"
    }
}
```

If your Confluence (Server/Data Center) connector is not connected correctly, you will see the
following error:

- CNF-5123: The profile value is invalid. Try again after sometime.

To troubleshoot the issue, check your Confluence (Server/Data Center) URL and make sure it's
correct.

## Checking personal access

token connectivity

To check connectivity for a Confluence (Server/Data Center) data source connector using
personal access token authentication, use the following cURL command:

```
curl --location '`https://<confluence_server_host_url>/rest/api/user/current`'
--header 'Authorization: Bearer `<PAT_TOKEN>`'
```

If your data source is connected as expected, the JSON response should resemble
the following:

```
{
    "type": "known",
    "accountId": "`accountId`",
    "accountType": "atlassian",
    "email": "`email`",
    "publicName": "Administrator",
    "profilePicture": {
        "path": "`/wiki/aa-avatar/<accountId>`",
        "width": 48,
        "height": 48,
        "isDefault": false
    },
    "displayName": "Administrator",
    "isExternalCollaborator": false,
    "_expandable": {
        "operations": "",
        "personalSpace": ""
    },
    "_links": {
        "self": "`https://<host_url>/wiki/rest/api/user?accountId=<accountId>`",
        "base": "`https://<host_url>/wiki`",
        "context": "/wiki"
    }
}
```

If your Confluence (Server/Data Center) connector is not connected correctly, you will see the
following error:

- CNF-5123: The profile value is invalid. Try again after sometime.

To troubleshoot the issue, check your Confluence (Server/Data Center) URL and make sure it's
correct.
