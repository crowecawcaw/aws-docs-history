# Integrate third-party applications (3p apps) in the Connect Customer agent workspace

Connect Customer agent workspace is a single, intuitive application that provides
your agents with the tools and step-by-step guidance they need to resolve issues
efficiently, improve customer experiences, and onboard faster. In addition to using
first-party applications in your agent workspace, such as Customer Profiles, Cases, and agent assist, you
can integrate third-party applications.

###### Note

This functionality is only supported in the default agent workspace; it is not
supported when using a custom CCP.

For example, you can integrate your proprietary reservation system or a
vendor-provided metrics dashboard, into the Connect Customer agent workspace.

If you are a developer interested in building a third-party application, see the
[Agent Workspace Developer
Guide](../../../agentworkspace/latest/devguide/getting-started.md "../../../agentworkspace/latest/devguide/getting-started.md").

###### Contents

- [Requirements](#onboard-3p-apps-requirements "#onboard-3p-apps-requirements")
- [How to add an integration](#onboard-3p-apps-how-to-integrate "#onboard-3p-apps-how-to-integrate")
- [Delete integrations](#delete-3p-apps "#delete-3p-apps")
- [Assign
  permissions](assign-security-profile-3p-apps.md "assign-security-profile-3p-apps.md")
- [Iframe permissions when
  granting third-party application access](3p-apps-iframe-permissions.md "3p-apps-iframe-permissions.md")
- [Integrate an MCP server](3p-apps-mcp-server.md "3p-apps-mcp-server.md")
- [Events and
  requests](3p-apps-events-requests.md "3p-apps-events-requests.md")
- [Access third-party
  applications in the agent workspace](3p-apps-agent-workspace.md "3p-apps-agent-workspace.md")
- [Access the Worklist app](worklist-app.md "worklist-app.md")
- [Third-party application SSO Federation
  setup](3p-apps-sso.md "3p-apps-sso.md")

- [Use screen pop functionality of third-party applications in the Connect Customer agent workspace](no-code-ui-builder-app-integration.md "no-code-ui-builder-app-integration.md")
- [Workshop for building a third-party app](https://catalog.workshops.aws/amazon-connect-agent-empowerment/en-US/third-party-applications/test "https://catalog.workshops.aws/amazon-connect-agent-empowerment/en-US/third-party-applications/test")

## Requirements

If you're using custom IAM policies to manage access to third-party applications,
your users need the following IAM permissions to integrate a third-party application
using the AWS Management Console. In addition to `AmazonConnect_FullAccess`, users
need:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "app-integrations:CreateApplication",
 "app-integrations:GetApplication",
 "iam:GetRolePolicy",
 "iam:PutRolePolicy",
 "iam:DeleteRolePolicy"
 ],
 "Resource": "arn:aws:app-integrations:`us-east-1`:`111122223333`:application/*",
 "Effect": "Allow"
 }
 ]
}`

```

## Integrations

###### Note

To add an integration to your instances, ensure that your
instance is using a Service-Linked Role (SLR). If your instance currently does
not use an SLR but you wish to add an integration, you will need
to migrate to an SLR. Integration can only be add to instances that are using an SLR. For more information, see [For instances created before October 2018](connect-slr.md#migrate-slr "connect-slr.md#migrate-slr").

1. Open the Connect Customer
   [console](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/")
   (https://console.aws.amazon.com/connect/).
2. On the left navigation pane, choose **Integrations**. If you do not see this menu, it's because it is
   not available in your region. To check the regions where this feature is
   available, see [Availability of Connect Customer features by Region](regions.md "regions.md").
3. On the **Integrations** page, choose
   **Add integration**.

![The properties page of the Set contact attributes block.](images/integrations-list.png) 4. On the **Add integration** page, enter:

    1. **Basic information**


    	1. **Display name**: A friendly
    	 name for the integration. This name is displayed on security
    	 profiles and to your agents on the tab in the agent
    	 workspace. You can come back and change this name.
    	2. **Description (optional)**:
    	 You may optionally provide any description for this
    	 integration. This description is not displayed to
    	 agents.
    	3. **Integration type**:
    	 Indicates whether the integration is a standard web
    	 application, service, or MCP server. This determines how the
    	 integration will be accessed within the
    	 system.
    	4. **Integration identifier**:
    	 The official name that is unique for integrations of type standard application or service. If
    	 you have only one application per access URL, we recommend
    	 that you use the origin of the access URL. You cannot
    	 change this name.
    	5. **Initialization timeout**:
    	 The maximum time allowed to establish a connection with the
    	 workspace. The time allowed is in milliseconds. This setting
    	 helps manage connection issues and ensures timely
    	 application startup.
    2. **Application details**


    	1. **Contact Scope**: Indicates
    	 whether the web application refreshes for each contact or
    	 refreshes only with each new browser session. This setting
    	 affects how frequently the application updates its
    	 data.
    	2. **Initialization timeout**:
    	 The maximum time allowed to establish a connection with the
    	 workspace. The time allowed is in milliseconds. This setting
    	 helps manage connection issues and ensures timely
    	 application startup.
    3. **Access**


    	1. **Access URL**: This is the
    	 URL where your application is hosted. The URL must be
    	 secure, starting with https, unless it's a local
    	 host.


    	###### Note

    	Not all URLs can be iframed. Here are two ways to
    	 check if the URL can be iframed:


    		1. There is a third-party tool available to help
    		 check if a URL can be iframed that is called
    		 [Iframe
    		 Tester](http://iframetester.com/ "http://iframetester.com/").


    			1. If a URL can be iframed, it will render in a
    			 preview on this page.
    			2. If a URL cannot be iframed, it will display
    			 an error in the preview on this page.




    				* It is possible that this website displays
    				 an error, and the app can still be iframed in the
    				 agent workspace. This is because the app developer
    				 can lock down their app to only be embeddable into
    				 the workspace and nowhere else. If you received
    				 this app from an app developer, we recommend that
    				 you still try integrating this app into the agent
    				 workspace.
    		2. For technical users: Check the security policy
    		 content of the application you are trying to
    		 integrate.


    			1. Firefox: Hamburger menu > More tools > Web
    			 developer tools > Network
    			2. Chrome: 3 dots menu > More tools > Developer
    			 tools > Network
    			3. Other browsers: Locate the network settings
    			 in the developer tools.
    			4. The Content-Security-Policy frame-ancestors
    			 directive should be
    			 `https://`your-instance`.my.connect.aws`.


    				1. If the directive is `same origin`
    				 or `deny`, then this URL cannot be
    				 iframed by AWS/Amazon Connect
    	Here's what you can do if the app cannot be
    	 iframed:




    		* If you control the app/URL, you can update the
    		 app's content security policy. Follow the best
    		 practices for app developers/ Ensuring that apps
    		 can only be embedded in the Connect Customer agent workspace
    		 section [here](../../../agentworkspace/latest/devguide/recommendations-and-best-practices.md "../../../agentworkspace/latest/devguide/recommendations-and-best-practices.md").
    		* If you do not control the app/URL, you can try
    		 reaching out to the app developer and asking them
    		 to update the app's content security
    		 policy.
    	2. **Approved origins
    	 (optional)**: Allowlist URLs that should be
    	 permitted, if different than the access URL. The URL must be
    	 secure, starting with https, unless it's a local
    	 host.
    4. Add permissions to [events
     and requests](3p-apps-events-requests.md "3p-apps-events-requests.md").


    The following is an example of how you can onboard a new
     application and assign permissions to it by using the AWS Management Console. In
     this example, six different permissions are assigned to the
     application.



    **Providing basic information and access
     details**
    5. **Instance association**


    	1. You may give any instance(s) within this account-region
    	 access to this application.
    	2. While associating the integration with an instance is
    	 optional, you will not be able to use this application until
    	 you associate it with instance(s).


    	###### Note

    	For MCP servers, you can only select the instance that is configured with the selected Gateway's Discovery URL.

![Providing basic information and access details.](images/integrations-add-basic-info.png)

**Granting permissions to the application for workspace
data integration**

![Granting permissions to the application for workspace data integration.](images/integrations-add-permissions.png)

**Iframe configuration**

![Iframe configuration.](images/integrations-add-iframe-config.png) 5. Choose **Add integration**. 6. If the integration was successfully created, you will be sent to the
**Integration details** page, and you will see a
success banner.

![Granting permissions to the application for workspace data integration.](images/integrations-view.png)

You can edit certain attributes of an existing app, such as its Display
Name, Access URL, and Permissions.

    1. If there was an error in either creating the application or
     associating the application to an instance, then you will see an
     error message, and you can take the corresponding action to correct
     the issue.

## Delete integrations

If you no longer want to use an integration in the foreseeable future,
you can delete it. If you temporarily want to stop using it, but you may want to use
it again in the foreseeable future, we recommend that you disassociate it from an
instance to avoid having to add it again. To delete integrations,
navigate to the AWS Management Console, select an integration, and choose
**Delete**.

**Troubleshooting**

- The operation will fail if the integration is associated with any
  instance. You will first have to disassociate the integration from any
  instance. Then you can come back and delete it.

###### Tip

If you created an integration before Dec 15, 2023, then you may encounter
issues when updating the association of the integration to instance(s). This is
because you need to make updates to your IAM policy.

![IAM error when trying to delete an integration due to insufficient permissions.](images/delete-3p-apps.png)

Your IAM policy will need to be updated to include the following
permissions:

- `app-integrations:CreateApplicationAssociation`
- `app-integrations:DeleteApplicationAssociation`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "app-integrations:CreateApplication",
 "app-integrations:GetApplication"
 ],
 "Resource": "arn:aws:app-integrations:`us-east-1`:`111122223333`:application/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "app-integrations:CreateApplicationAssociation",
 "app-integrations:DeleteApplicationAssociation"
 ],
 "Resource": "arn:aws:app-integrations:`us-east-1`:`111122223333`:application-association/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "iam:GetRolePolicy",
 "iam:PutRolePolicy",
 "iam:DeleteRolePolicy"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect_*",
 "Effect": "Allow"
 }
 ]
}`

```
