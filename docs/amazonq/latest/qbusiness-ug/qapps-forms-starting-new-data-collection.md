

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Starting a new data collection
<a name="qapps-forms-starting-new-data-collection"></a>

You can start a new data collection with the web experience or with the Q Apps APIs.

## Web experience
<a name="qapps-forms-data-collection-web-experience"></a>

To start a new data collection, you open an app with a data collection form, configure data collection settings, and then copy and share the link to start collecting responses.

1. Go to your Amazon Q Business web experience URL.

1. In the navigation pane, choose **Apps**.

1. Locate and open an existing Q App that has a data collection form.

1. Choose **Start data collection** at the top right.

1. Enter a name for the data collection. For example, John Doe's All-Hands Meeting. You use this name when you reference the data from the form in other cards. For example, outputting an AI-generated summary of responses to an output card in the app. 

1. In **Advanced settings**, configure the participant experience with the **Allow users to submit data** and **Allow users to see all collected data** check boxes. 

1. Choose **Create**.

1. Choose the options to enable/disable form submissions and whether users can see others' data.

1. Choose the **Copy** icon to obtain the shareable link.

1. Choose **Save**.

1. Share the link directly with your users. As users respond to questions, you can do the following from your app:
   + To see user data, on the form collection card, choose **All data**.
   + To delete collected data, choose **Data collection settings** and choose **Delete collected data**.
   + To stop or restart collecting data, toggle the **Allow users to submit data** check box.

## Q Apps APIs
<a name="qapps-forms-apis"></a>

Owners can start and manage data collections with the following APIs:
+ `StartQAppSession` - Start a new data collection.
+ `UpdateQAppSessionMetadata` - Update metadata for the data collection. For example, give the collection a name.
+ `UpdateQAppSession` - Optionally provide answers to your own data collection questions.
+ `ListQppSessionData` - List all submitted values for form cards.
+ `ExportQAppSessionData` - Export data in CSV format
+ `StopQAppSession` - Terminate the session

For participants, use the following APIs:
+ `StartQAppSession` - Associate the user with the data collection.
+ `GetQAppSession` - Get the latest state of the data collection. Use this API before and after submitting data into form cards.
+ `ListQAppSessionData` - Get all submitted values for form cards.
+ `UpdateQappSession` - Submit data into form cards.