# Find your Amazon Managed Service for Prometheus workspace details,

including ARN

You can find the details of your Amazon Managed Service for Prometheus workspace by using either the AWS
console or the AWS CLI.

Console

###### To find your workspace details using the Amazon Managed Service for Prometheus console

1.  Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2.  In the upper left corner of the page, choose the menu icon and then choose
    **All workspaces**.
3.  Choose the **Workspace ID** of the workspace. This will
    display details about your workspace, including:

        * **Current status** – The status
         of your workspace, for example **Active**, is displayed
         under **Status**.
        * **ARN** – The workspace ARN is
         displayed under **ARN**.
        * **ID** – The workspace ID is
         displayed under **Workspace ID**.
        * **URLs** – The console displays
         multiple URLs for the workspace, including the URLs for writing to or
         querying data from the workspace.


        ###### Note

        By default, the URLs given are the IPv4 URLs. You can also use
         dualstack (IPv4 and IPv6 supported) URLs. These are the same, but
         are in the domain `api.aws` rather than the default
         `amazonaws.com`. For example, if you were to see the
         following (an IPv4 URL):


        ```
        https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-abcd1234-ef56-7890-ab12-example/api/v1/remote_write
        ```
        You could create a dualstack (including support for IPv6), URL
         as follows:


        ```
        https://aps-workspaces.us-east-1.api.aws/workspaces/ws-abcd1234-ef56-7890-ab12-example/api/v1/remote_write
        ```

    Below this section are tabs with information about rules, alert manager, logs, configuration, and tags.

AWS CLI
**To find your workspace details using the AWS CLI**

The following command returns the details of the workspace. You must replace
`my-workspace-id` with the workspace ID of the workspace for
which you want the details.

```
aws amp describe-workspace --workspace-id `my-workspace-id`
```

This returns details about your workspace, including:

- **Current status** – The status
  of your workspace, for example `ACTIVE`, is returned
  in the `statusCode` property.
- **ARN** – The workspace ARN is
  returned in the `arn` property.
- **URLs** – The AWS CLI returns the
  base URL for the workspace in the `prometheusEndpoint`
  property.

###### Note

By default, the URL returned is the IPv4 URL. You can also use a
dualstack (IPv4 and IPv6 supported) URL in the domain `api.aws`
rather than the default `amazonaws.com`. For example, if you
were to see the following (an IPv4 URL):

```
https://aps-workspaces.us-east-1.amazonaws.com/workspaces/ws-abcd1234-ef56-7890-ab12-example/
```

You could create a dualstack (including support for IPv6), URL
as follows:

```
https://aps-workspaces.us-east-1.api.aws/workspaces/ws-abcd1234-ef56-7890-ab12-example/
```

You can also create the remote write and query URLs for the
workspace, by adding `/api/v1/remote_write` or
`/api/v1/query`, respectively.
