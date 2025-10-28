# Checking Jira

connectivity

Before you sync your Jira data source connector after [configuring it](jira-console.md "jira-console.md"), we recommend you check the connection between
Amazon Q Business and Jira. The following are the cURL commands you need to
check Jira connectivity.

###### Topics

- [Checking basic
  authentication connectivity](#jira-connection-check-basic "#jira-connection-check-basic")

## Checking basic

authentication connectivity

To check connectivity for a Jira data source connector using
basic authentication, use the following cURL command:

```
curl --location '`https://<jira-url>/wiki/rest/api/user/current`'
--header 'Authorization: Basic <`base64(email:api_token)`>'
```

If your data source is connected as expected, the JSON response should
resemble the following:

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

If your Jira connector is not connected correctly, you will see
the following error:

- CNF-5123: The profile value is invalid. Try again after
  sometime.

To troubleshoot the issue, check your Jira URL and make sure
it's correct.
