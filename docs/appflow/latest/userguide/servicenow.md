# ServiceNow

The following are the requirements and connection instructions for using ServiceNow with
Amazon AppFlow.

###### Note

You can use ServiceNow as a source only.

###### Topics

- [Requirements](#servicenow-requirements "#servicenow-requirements")
- [Connection instructions](#servicenow-setup "#servicenow-setup")
- [Notes](#servicenow-notes "#servicenow-notes")
- [Supported destinations](#servicenow-destinations "#servicenow-destinations")
- [Related resources](#servicenow-resources "#servicenow-resources")

## Requirements

Before you can use Amazon AppFlow to import data from ServiceNow, you need the following:

- A ServiceNow account so that you can provide Amazon AppFlow with your user name, password, and
  instance name.
- Access to your ServiceNow instance through a role. This can be an admin role or one that
  allows the read operation for the following:

      + `sys_db_object`
      + `sys_db_object.*`
      + `sys_dictionary`
      + `sys_dictionary.*`
      + `sys_glide_object`
      + Any table that you want to access with Amazon AppFlow. For example, if you want to import
       data from a table named `incidents`, you need read access to
       `incidents` and `incidents.*`.

  For more information about ServiceNow roles, see [Roles](https://docs.servicenow.com/bundle/sandiego-platform-administration/page/administer/roles/reference/r_SecurityJumpStartACLRules.html "https://docs.servicenow.com/bundle/sandiego-platform-administration/page/administer/roles/reference/r_SecurityJumpStartACLRules.html") in the ServiceNow documentation.

## Connection instructions

###### To connect to ServiceNow while creating a flow

The ServiceNow connector for Amazon Appflow now has the option to create connections using
either Basic Auth or OAuth2 authentication. You make this choice in the console when you create
your connection. If you choose Basic Auth, you’ll need to provide your username, password, and
Instance URL. If you choose OAuth2, you’ll need to provide your Client ID, Client secret, and
Instance URL.

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. Choose **Create flow**.
3. For **Flow details**, enter a name and description for the flow.
4. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
   **Data encryption**, **Customize encryption settings** and
   then choose an existing CMK or create a new one.
5. (Optional) To add a tag, choose **Tags**, **Add tag**
   and then enter the key name and value.
6. Choose **Next**.
7. Choose **ServiceNow** from the **Source name** dropdown
   list.
8. Choose **Connect** to open the **Connect to ServiceNow**
   dialog box.
9. 1. Under **Connection name**, enter a name for your connection.
   2. In the **Select authentication mode** dropdown menu, select either **Basic Auth** or **OAuth2**.
   3. (For Basic Auth only) Under **User name**, enter your ServiceNow user name.
   4. (For Basic Auth only) Under **Password**, enter the password for that account.
   5. (For OAuth2 only) Under **Client ID**, enter the Client ID from your app.
   6. (For OAuth2 only) Under **Client secret**, specify the Client secret from your app.
   7. Under **Instance URL**, specify the instance of ServiceNow you want to
      connect to.
   8. Choose **Connect**.
10. Once connected, you can choose the ServiceNow object.

Now that you are connected to your ServiceNow account, you can continue with the flow
creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#servicenow-requirements "#servicenow-requirements")
section.

## Notes

- Once you are connected to your ServiceNow instance, you can select the relevant objects
  from ServiceNow by using the dropdown list. Given the amount of data being available via
  ServiceNow, the dropdown list may take some time to fully populate. Amazon AppFlow will list all
  tables available (including custom ones) and you can map the source fields to the destination
  fields during flow setup.
- You can run your flows either on demand, or on schedule, which enables you to integrate
  your ServiceNow data with AWS services.
- When you use ServiceNow as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per minute.
- When you use ServiceNow as a source for incremental flows that run on a schedule,
  Amazon AppFlow uses the `sys_updated_on` field to identify the updated record
  set.
- ServiceNow can process up to 100,000 records as part of a single flow run.

## Supported destinations

When you create a flow that uses ServiceNow as the data source, you can set the destination to any of the following connectors:

- Amazon Connect
- Amazon Honeycode
- Lookout for Metrics
- Amazon Redshift
- Amazon S3
- Marketo
- Salesforce
- Snowflake
- Upsolver
- Zendesk

You can also set the destination to any custom connectors that you
create with the Amazon AppFlow Custom Connector SDKs for [Python](https://github.com/awslabs/aws-appflow-custom-connector-python "https://github.com/awslabs/aws-appflow-custom-connector-python") or [Java](https://github.com/awslabs/aws-appflow-custom-connector-java "https://github.com/awslabs/aws-appflow-custom-connector-java") . You can download these SDKs from GitHub.

## Related resources

- [Roles](https://docs.servicenow.com/bundle/paris-platform-administration/page/administer/roles/concept/c_Roles.html "https://docs.servicenow.com/bundle/paris-platform-administration/page/administer/roles/concept/c_Roles.html") in the _ServiceNow_ documentation
