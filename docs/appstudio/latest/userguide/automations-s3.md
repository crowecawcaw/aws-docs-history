# Interacting with Amazon Simple Storage Service with components and automations

You can invoke various Amazon S3 operations from an App Studio app. For example, you could create
a simple admin panel to manage your users and orders and display your media from Amazon S3. While you
can invoke any Amazon S3 operation using the **Invoke AWS** action,
there are four dedicated Amazon S3 actions that you can add to automations in your app to perform
common operations on Amazon S3 buckets and objects. The four actions and their operations are as
follows:

- **Put Object**: Uses the `Amazon S3 PutObject` operation to add an object an Amazon S3 bucket.
- **Get Object**: Uses the `Amazon S3 GetObject` operation to retrieve an object from an Amazon S3 bucket.
- **List Objects**: Uses the `Amazon S3 ListObjects` operation to list objects in an Amazon S3 bucket.
- **Delete Object**: Uses the `Amazon S3 DeleteObject` operation to delete an object from an Amazon S3 bucket.
  In addition to the actions, there is an **S3 upload** component
  that you can add to pages in applications. Users can use this component to choose a file to
  upload, and the component calls `Amazon S3 PutObject` to upload the file to the configured
  bucket and folder. This tutorial will use this component in place of the standalone **Put Object** automation action. (The standalone action should be used in
  more complex scenarios that involve additional logic or actions to be taken before or after
  uploading.)

## Prerequisites

This guide assumes you have completed the following prerequisite:

1. Created and configured an Amazon S3 bucket, IAM role and policy, and Amazon S3 connector in order
   to successfully integrate Amazon S3 with App Studio. To create a connector, you must have the
   Administrator role. For more information, see [Connect to Amazon Simple Storage Service (Amazon S3)](connectors-s3.md "connectors-s3.md").

## Create an empty application

Create an empty application to use throughout this guide by performing the following steps.

###### To create an empty application

1. In the navigation pane, choose **My applications**.
2. Choose **+ Create app**.
3. In the **Create app** dialog box, give your application a name, choose **Start from scratch**, and
   choose **Next**.
4. In the **Connect to existing data** dialog box, choose **Skip** to create the application.
5. Choose **Edit app** to be taken to the canvas of your new app, where you can use components, automations, and data to
   configure the look and function of your application.

## Create pages

Create three pages in your application to gather or show information.

###### To create pages

1. If necessary, choose the **Pages** tab at the top of the canvas.
2. In the left-hand navigation, there is a single page that was created with your app. Choose **+ Add** twice to create two more pages. The navigation
   pane should show three total pages.
3. Update the name of the **Page1** page by performing the following steps:
   1. Choose the ellipses icon and choose **Page properties**.
   2. In the right-hand **Properties** menu, choose the pencil icon to edit the
      name.
   3. Enter `FileList` and press **Enter**.

4. Repeat the previous steps to update the second and third pages as follows:
   - Rename **Page2** to `UploadFile`.
   - Rename **Page3** to `FailUpload`.

Now, your app should have three pages named **FileList**,
**UploadFile**, and **FailUpload**, which are shown in the
left-hand **Pages** panel.

Next, you will create and configure the automations that interact with Amazon S3.

## Create and configure automations

Create the automations of your application that interact with Amazon S3. Use the following procedures to create the following automations:

- A **getFiles** automation that lists the objects in your Amazon S3 bucket, which will be used to fill a table component.
- A **deleteFile** automation that deletes an object from your Amazon S3 bucket, which will be used to add a delete button to a table component.
- A **viewFile** automation that gets an object from your Amazon S3 bucket and displays it, which will be used to show more details about a
  single object selected from a table component.

### Create a `getFiles` automation

Create an automation that will list the files in a specified Amazon S3 bucket.

1. Choose the **Automations** tab at the top of the canvas.
2. Choose **+ Add automation**.
3. In the right-hand panel, choose **Properties**.
4. Update the automation name by choosing the pencil icon. Enter `getFiles`
   and press **Enter**.
5. Add a **List objects** action by performing the following steps:
   1. In the right-hand panel, choose **Actions**.
   2. Choose **List objects** to add an action. The action should be named `ListObjects1`.

6. Configure the action by performing the following steps:
   1. Choose the action from the canvas to open the right-hand **Properties** menu.
   2. For **Connector**, choose the Amazon S3 connector that you created from the
      prerequisites.
   3. For **Configuration**, enter the following text, replacing `bucket_name` with the bucket you created in
      the prerequisites:

   ```
   {
     "Bucket": "`bucket_name`",
     "Prefix": ""
   }
   ```

   ###### Note

   You can use the `Prefix` field to limit the response to objects that begin with the
   specified string.

7. The output of this automation will be used to populate a table component with objects from
   your Amazon S3 bucket. However, by default, automations don't create outputs. Configure the
   automation to create an automation output by performing the following steps:
   1. In the left-hand navigation, choose the **getFiles** automation.
   2. On the right-hand **Properties** menu, in **Automation
      output**, choose **+ Add output**.
   3. For **Output**, enter `{{results.ListObjects1.Contents}}`. This expression returns the contents of the action, and can now
      be used to populate a table component.

### Create a `deleteFile` automation

Create an automation that deletes an object from a specified Amazon S3 bucket.

1. In the left-hand **Automations** panel, choose **+ Add**.
2. Choose **+ Add automation**.
3. In the right-hand panel, choose **Properties**.
4. Update the automation name by choosing the pencil icon. Enter
   `deleteFile` and press **Enter**.
5. Add an automation parameter, used to pass data to an automation, by performing the following steps:
   1. On the right-hand **Properties** menu, in **Automation
      parameters**, choose **+ Add**.
   2. Choose the pencil icon to edit the automation parameter. Update the parameter name to
      `fileName` and press **Enter**.

6. Add a **Delete object** action by performing the following steps:
   1. In the right-hand panel, choose **Actions**.
   2. Choose **Delete object** to add an action. The action should be named `DeleteObject1`.

7. Configure the action by performing the following steps:
   1. Choose the action from the canvas to open the right-hand **Properties** menu.
   2. For **Connector**, choose the Amazon S3 connector that you created from the prerequisites.
   3. For **Configuration**, enter the following text, replacing `bucket_name` with the bucket you created in
      the prerequisites:

   ```
   {
     "Bucket": "`bucket_name`",
     "Key": params.fileName
   }
   ```

### Create a `viewFile` automation

Create an automation that retrieves a single object from a specified Amazon S3 bucket. Later, you will configure this automation with a file viewer component
to display the object.

1.  In the left-hand **Automations** panel, choose **+ Add**.
2.  Choose **+ Add automation**.
3.  In the right-hand panel, choose **Properties**.
4.  Update the automation name by choosing the pencil icon. Enter `viewFile`
    and press **Enter**.
5.  Add an automation parameter, used to pass data to an automation, by performing the following steps:
    1. On the right-hand **Properties** menu, in **Automation
       parameters**, choose **+ Add**.
    2. Choose the pencil icon to edit the automation parameter. Update the parameter name to
       `fileName` and press **Enter**.

6.  Add a **Get object** action by performing the following steps:
    1. In the right-hand panel, choose **Actions**.
    2. Choose **Get object** to add an action. The action should be named `GetObject1`.

7.  Configure the action by performing the following steps:
    1. Choose the action from the canvas to open the right-hand **Properties** menu.
    2. For **Connector**, choose the Amazon S3 connector that you created from the prerequisites.
    3. For **Configuration**, enter the following text, replacing `bucket_name` with the bucket you created in
       the prerequisites:

    ```
    {
      "Bucket": "`bucket_name`",
      "Key": params.fileName
    }
    ```

8.  By default, automations don't create outputs. Configure the automation to create an automation
    output by performing the following steps:
    1. In the left-hand navigation, choose the **viewFile** automation.
    2. On the right-hand **Properties** menu, in **Automation
       output**, choose **+ Add output**.
    3. For **Output**, enter `{{results.GetObject1.Body.transformToWebStream()}}`. This expression
       returns the contents of the action.

    ###### Note

    You can read the response of `S3 GetObject` in the following ways:

        * `transformToWebStream`: Returns a stream, which must be consumed to retrieve the
         data. If used as an automation output, the automation handles this, and the output can be
         used as a data source of an image or PDF viewer component. It can also be used as an
         input to another operation, such as `S3 PutObject`.
        * `transformToString`: Returns the raw data of the automation, and should be used in a JavaScript action if your files contain text content, such as JSON data. Must be
         awaited, for example: `await results.GetObject1.Body.transformToString();`
        * `transformToByteArray`: Returns an array of 8-bit unsigned integers. This response serves the purpose of a byte array, which allows storage and
         manipulation of binary data. Must be awaited, for example: `await results.GetObject1.Body.transformToByteArray();`

Next, you will add components to the pages you created earlier, and configure them with
your automations so that users can use your app to view and delete files.

## Add and configure page components

Now that you have created the automations that define the business logic and functionality of your app, you will create components and connect them both.

### Add components to the **FileList** page

The **FileList** page that you created earlier will be used to display a
list of files in the configured Amazon S3 bucket and more details about any file that is chosen from
the list. To do that, you will do the following:

1. Create a table component to display the list of files. You will configure the table's rows to be filled with the output of the
   **getFiles** automation you previously created.
2. Create a PDF viewer component to display a single PDF. You will configure the component to view a file selected from the table, using the
   **viewFile** automation you previously created to fetch the file from your bucket.

###### To add components to the **FileList** page

1.  Choose the **Pages** tab at the top of the canvas.
2.  In the left-hand **Pages** panel, choose the **FileList** page.
3.  On the right-hand **Components** page, find the **Table**
    component and drag it to the center of the canvas.
4.  Choose the table component that you just added to the page.
5.  On the right-hand **Properties** menu, choose the **Source**
    dropdown and select **Automation**.
6.  Choose the **Automation** dropdown and select the **getFiles** automation. The table will use the output
    of the **getFiles** automation as its content.
7.  Add a column to be filled with the name of the file.
    1. On the right-hand **Properties** menu, next to **Columns**,
       choose **+ Add**.
    2. Choose the arrow icon to the right of the **Column1** column that was just added.
    3. For **Column label**, rename the column to `Filename`.
    4. For **Value**, enter `{{currentRow.Key}}`.
    5. Choose the arrow icon at the top of the panel to return to the main **Properties** panel.

8.  Add a table action to delete the file in a row.
    1. On the right-hand **Properties** menu, next to **Actions**,
       choose **+ Add**.
    2. In **Actions**, rename **Button** to `Delete`.
    3. Choose the arrow icon to the right of the **Delete** action that was just renamed.
    4. In **On click**, choose **+ Add action** and choose **Invoke automation**.
    5. Choose the action that was added to configure it.
    6. For **Action name**, enter `DeleteRecord`.
    7. In **Invoke automation**, select `deleteFile`.
    8. In the parameter text box, enter `{{currentRow.Key}}`.
    9. For **Value**, enter `{{currentRow.Key}}`.

9.  In the right-hand panel, choose **Components** to view the components menu. There are two choices for showing files:

        * An **Image viewer** to view files with a
         `.png`, `.jpeg`, or `.jpg` extension.
        * A **PDF viewer** component to view PDF files.

    In this tutorial, you will add and configure the **PDF viewer** component.

10. Add the **PDF viewer** component.
    1. On the right-hand **Components** page, find the **PDF
       viewer** component and drag it to the canvas, below the table component.
    2. Choose the **PDF viewer** component that was just added.
    3. On the right-hand **Properties** menu, choose the **Source**
       dropdown and select **Automation**.
    4. Choose the **Automation** dropdown and select the **viewFile** automation. The table will use the output
       of the **viewFile** automation as its content.
    5. In the parameter text box, enter `{{ui.table1.selectedRow["Filename"]}}`.
    6. In the right-hand panel, there is also a **File name** field. The value of this field is used as the header for the
       PDF viewer component. Enter the same text as the previous step: `{{ui.table1.selectedRow["Filename"]}}`.

### Add components to the **UploadFile** page

The **UploadFile** page will contain a file selector that can be used to select and upload a file to the configured Amazon S3 bucket. You will
add the **S3 upload** component to the page, which users can use to select and upload a file.

1.  In the left-hand **Pages** panel, choose the **UploadFile** page.
2.  On the right-hand **Components** page, find the **S3
    upload** component and drag it to the center of the canvas.
3.  Choose the S3 upload component that you just added to the page.
4.  On the right-hand **Properties** menu, configure the component:
    1. In the **Connector** dropdown, select the Amazon S3 connector that was created in the
       prerequisites.
    2. For **Bucket**, enter the name of your Amazon S3 bucket.
    3. For **File name**,
       enter `{{ui.s3Upload1.files[0]?.nameWithExtension}}`.
    4. For **Max file size**, enter `5` in the text box, and
       ensure that `MB` is selected in the dropdown.
    5. In the **Triggers** section, add actions that run after successful or
       unsuccessful uploads by performing the following steps:

    To add an action that runs after successful uploads:

        1. In **On success**, choose **+ Add action** and select **Navigate**.
        2. Choose the action that was added to configure it.
        3. For **Navigation type**, choose **Page**.
        4. For **Navigate to**, choose `FileList`.
        5. Choose the arrow icon at the top of the panel to return to the main **Properties** panel.

    To add an action that runs after unsuccessful uploads:

        1. In **On failure**, choose **+ Add action** and select **Navigate**.
        2. Choose the action that was added to configure it.
        3. For **Navigation type**, choose **Page**.
        4. For **Navigate to**, choose `FailUpload`.
        5. Choose the arrow icon at the top of the panel to return to the main **Properties** panel.

### Add components to the **FailUpload** page

The **FailUpload** page is a simple page containing a text box that informs users that their upload failed.

1. In the left-hand **Pages** panel, choose the **FailUpload** page.
2. On the right-hand **Components** page, find the **Text**
   component and drag it to the center of the canvas.
3. Choose the text component that you just added to the page.
4. On the right-hand **Properties** menu, in **Value**, enter
   `Failed to upload, try again`.

## Update your app security settings

Every application in App Studio has content security settings that you can use to restrict external media or resources,
or which domains in Amazon S3 you can upload objects to. The default setting is to block all domains. To upload objects to Amazon S3 from your application, you must
update the setting to allow the domains you want to upload objects to.

###### To allow domains for uploading objects to Amazon S3

1. Choose the **App settings** tab.
2. Choose the **Content Security Settings** tab.
3. For **Connect source**, choose **Allow all connections**.
4. Choose **Save**.

## Next steps: Preview and publish the application for testing

The application is now ready for testing. For more information about previewing and publishing applications, see
[Previewing, publishing, and sharing applications](applications-preview-publish-share.md "applications-preview-publish-share.md").
