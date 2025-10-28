# Deleting an App Studio instance

Use the procedure in this topic to delete your App Studio instance. If you created resources in other services for use with App Studio, review and delete them
as necessary to avoid being charged.

You may want to delete an App Studio instance for the following reasons:

- You no longer want to use App Studio.
- You want to create an App Studio instance in a different AWS Region. Because App Studio only supports having an instance in one Region at a time,
  you must delete any existing instances to create another one.

###### Warning

Deleting an App Studio instance also deletes all App Studio resources, such as
applications and connectors. Deleting an instance cannot be undone.

###### To delete your App Studio instance

1. Open the App Studio console at [https://console.aws.amazon.com/appstudio/](https://console.aws.amazon.com/appstudio/ "https://console.aws.amazon.com/appstudio/").
2. Select the Region in which your App Studio instance exists.
3. In the navigation pane, choose **Instance**.
4. Choose **Actions** to open the dropdown with additional instance actions.
5. Choose **Delete App Studio instance**.
6. Enter `confirm` and choose **Delete**.
7. It may take a while for your instance deletion to process. Once it has been deleted, you will receive a confirmation email. Once
   you receive the email, you can create another instance if desired.
