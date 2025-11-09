AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Grouping servers in the AWS Migration Hub console

Some of your discovered servers might need to be migrated together to remain
functional. In this case, you can logically define and group discovered servers into
applications.

As part of the grouping process, you can search, filter, and add tags.

###### To group servers into a new or existing application

1. Using your AWS account, sign in to the AWS Management Console and open the Migration Hub console
   at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane under **Discover**,
   choose **Servers**.
3. In the servers list, select each server that you want to group into a new or
   existing application.

To help choose servers for your group, you can search and filter on any
criteria that you specify in the server list. Click inside the search bar and
choose an item from the list, choose an operator from the next list, and then
type in your criteria. 4. Optional: For each selected server, choose **Add tag**, type
a value for **Key**, and then optionally type a value for
**Value**. 5. Choose **Group as application** to create your application,
or add to an existing one. 6. In the **Group as application** dialog box, choose
**Group as a new application** or **Add to an
existing application**.

    1. If you chose **Group as a new application**, type a
     name for **Application name**. Optionally, you can type
     a description for **Application description**.
    2. If you chose **Add to an existing application**,
     select the name of the application to add to in the list.

7. Choose **Save**.
