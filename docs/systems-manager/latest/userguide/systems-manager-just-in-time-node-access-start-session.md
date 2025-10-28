# Start a

just-in-time node access session

After enabling and setting up just-in-time node access, and configuring session and
notification preferences, users are ready to start just-in-time node access sessions.
You can start sessions using just-in-time node access from the Systems Manager console or from the
AWS Command Line Interface using the Session Manager plugin. Just-in-time node access sessions can be started on nodes
in the same account and Region. The following procedures describe how to start sessions
with just-in-time node access.

###### Note

If your users previously used Session Manager to connect to nodes, you must remove the
Session Manager permissions, for example `ssm:StartSession`, from their IAM
policies to start sessions using just-in-time node access. Otherwise, when
connecting to nodes they'll continue to use Session Manager.

###### To start a session with just-in-time node access using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Explore nodes** in the navigation pane.
3. Select the node you want to connect to.
4. In the **Actions** dropdown, select
   **Connect**.
   If your organization's approval policies don't allow you to automatically connect to
   the node, you're prompted to submit an access request. After you fill out the
   information requested and submit the acccess request, you'll be able to start sessions
   to the node once all of the required approvals are received.

###### To start a session with just-in-time node access using the AWS CLI

1. Run the following command to start the access request workflow, making sure to
   replace the `placeholder values` with your own
   information.

```
aws ssm start-access-request \
    --targets  Key=InstanceIds,Values=`i-02573cafcfEXAMPLE`
    --reason "`Troubleshooting networking performance issue`"
```

Depending on your organization's approval policies, you'll either be
automatically connected to the node or the manual approval process is started.
For requests that require manual approvals, note the ID of the access request
that is returned in the response. 2. Wait for all of the required approvals to be provided. 3. After all required approvals have been provided, run the following command to
get an access token containing temporary credentials. Replace the
`placeholder values` with your own
information.

```
aws ssm get-access-token \
    --access-request-id `oi-12345abcdef`
```

Note the access token returned in the response. 4. Run the following command to use the temporary credential in the AWS CLI, making
sure to replace the `placeholder values` with your own
information.

```
export AWS_SESSION_TOKEN=`AQoDYXdzEJr...<remainder of session token>`
```

5. Run the following command to start a session to the node, making sure to
   replace the `placeholder values` with your own
   information.

```
aws ssm start-session \
    --target i-02573cafcfEXAMPLE
```
