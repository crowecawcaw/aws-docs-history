# Generate a test set for Test Workbench

You can create a test set to evaluate the performance of your bot. Generate a test set
by uploading a test set that is in a CSV file format or by generating a test set from
[conversation logs](conversation-logs.md "conversation-logs.md"). The test set can contain audio or text input.

![Create a test set with the Test Workbench.](images/testworkbench/test-workbench-create.png)
If a test set creates validation errors, remove the test set and replace it with
another list of test set data, or edit the data in the CSV file by using a spreadsheet
editing program.

###### To create a test set:

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. Choose **Test workbench** from the left side panel.
3. Select **Test sets** from the options under Test workbench.
4. Select the **Create test set** button on the console.
5. In the **Details**, enter a test set name and an optional
   description.
6. Select **Generate a baseline test set**.
7. Select **Generate from conversation logs**.
8. Select **Bot name**, **Bot Alias**, and
   **Language** from the drop down menus.
9. If you are generating a baseline test from a conversation log, choose
   **Time range** and **IAM role**, if
   required. You can create a role with the basic Amazon Lex V2 permissions or use an
   existing role.
10. Choose a modality of **Audio** or **Text**
    for the test set you are creating. NOTE: The Test Workbench can import text
    files up to 50k, and up to 5 hours of audio.
11. Select an Amazon S3 location to store your test results, and add an optional KMS
    key to encrypt output transcripts.
12. Select **Create**.

###### To upload an existing test set in a CSV file format, or to update the test

set:

1. Choose **Test workbench** from the left side panel.
2. Select **Test sets** from the options under Test workbench.
3. Select **Upload a file to this test set** on the console.
4. Choose **Upload from Amazon Amazon S3 bucket** or **Upload
   from your computer**. NOTE: You can upload a CSV file created from
   a template. Click **CSV template** to download a zip file that
   contains the templates.
5. Choose **Create a role with basic Amazon Lex permissions** or
   **Use an existing role for Role ARN**.
6. Choose a modality of **Audio** or **Text**
   for the test set you are creating. NOTE: The Test Workbench can import text
   files up to 50k, and up to 5 hours of audio.
7. Select an Amazon S3 location to store your test results, and add an optional KMS
   key to encrypt output transcripts.
8. Select **Create**.
   If the operation is successful, the confirmation message will indicate that the test
   set is ready to test, and the status will display **Ready for
   testing**.
