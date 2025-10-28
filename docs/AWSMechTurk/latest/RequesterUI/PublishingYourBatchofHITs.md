# Publish a batch of HITs

Publishing your HITs on the [Amazon
Mechanical Turk web page](https://www.mturk.com/mturk/findhits "https://www.mturk.com/mturk/findhits") provides Workers with the opportunity to work on them.
If your project template contains variables, you must upload the `.csv` data file
that supplies the values for the variables in each HIT before you can publish your batch of
HITs.

The following procedure describes how to publish an Amazon Mechanical Turk batch using an existing
project.

###### To publish a batch

1. Sign in to the Amazon Mechanical Turk Requester website at [https://requester.mturk.com/](https://requester.mturk.com/ "https://requester.mturk.com/").
2. Choose the **Create** tab and then choose **New Batch
   with an Existing Project**.
3. Under **Start a New Batch with an Existing Project**, choose
   **Publish Batch** to publish the batch for your project. If you
   want to make edits to your project before publishing a new batch, click
   **Edit** to make changes to the HIT properties or design
   layout.
4. If your project template contains variables, choose a `.csv` file to
   upload. In **Publish Batch**, choose **Choose
   File** to locate the `.csv` data file and then choose
   **Upload**.
5. After you upload your file, choose **Next** to preview your HITs
   to see how they'll appear to Workers.
6. On the **Preview HITs** page, carefully review your HITs and
   correct mistakes before publishing. For example, make sure that any variables in the
   HIT are correctly replaced by your input data. Choose **Next HIT**
   to preview the next HIT. You can preview up to 200 HITs in your data file.
7. After you finish reviewing your HITs, choose **Next**.
8. Review the information on the **Confirm and Publish Batch** page,
   which shows the total amount you will pay Workers and Mechanical Turk Mechanical Turk
   if you approve all of the assignments. The following table explains the sections of
   the **Confirm and Publish Batch** page.

| Section          | Description                                                                                                                                                                                                                                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Batch Properties | Contains the values that you set on the **Design** tab for the batch properties, including the number of days the batch can exist before expiring, and the number of days you have to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.                                                        |
| Tasks            | Calculates the number of assignments per batch.                                                                                                                                                                                                                                                                                                        |
| Cost Summary     | Calculates the cost of the batch assuming you approve all assignments. The total cost is the number of assignments multiplied by the price per assignment plus the Mechanical Turk fee. You must have enough money in your account to cover the total cost before you can publish the HIT. If you don't, you'll be asked to add money to your account. | 9. If you haven't already entered a payment method, enter it in **Payment Method**. 10. Choose **Purchase & Publish** to publish the batch of HITs. After your batch has been published, you can track its progress in the **Manage** section of the Mechanical Turk Requester console. For more information about managing batches, see [Manage batches](ManagingYourHITs.md "ManagingYourHITs.md"). |
