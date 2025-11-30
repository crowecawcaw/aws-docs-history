# Step 7: (Optional) Clean up

The walkthrough is complete. You can keep using the DataBrew and Amazon S3 resources that you
created, or delete them.

###### To clean up resources

1. Open the DataBrew console at [https://console.aws.amazon.com/databrew/](https://console.aws.amazon.com/databrew/ "https://console.aws.amazon.com/databrew/"), and on the navigation pane, choose
   **Projects**.
2. Choose your project (**Sample project**). For
   **Actions**, choose **Delete**.
3. On the **Delete Sample project** pane, choose
   **Delete attached recipe**. Then choose
   **Delete**. Your project, along with its recipe and jobs,
   will be deleted.
4. On the navigation pane, choose **Datasets**.
5. Choose your dataset (`chess-games`), and for
   **Actions**, choose **Delete**.
6. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"). Delete the `databrew-output`
   folder and its contents.

(Optional) If you're sure that you no longer need your Amazon S3 bucket, you can
delete it.
