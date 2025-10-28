# Add an evaluation job

(Studio)

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

After you register your model, you can test your model with one or more
datasets to assess its performance. You can add one or more evaluation jobs from
Amazon S3 or define your own evaluation job by manually entering all details. If you
add a job from Amazon S3, SageMaker AI prepopulates the fields for all of the subpages in the
**Evaluate** tab. If you define your own evaluation job,
you need to add details related to your evaluation job manually.

###### To add your first evaluation job to your model package, complete the

following steps.

1. Choose the **Evaluate** tab.
2. Choose **Add**.
3. You can add an evaluation job from Amazon S3 or a custom evaluation
   job.
   1. To add an evaluation job with collaterals from Amazon S3, complete
      the following steps.
      1. Choose **S3**.
      2. Enter a name for the evaluation job.
      3. Enter the Amazon S3 location to the output collaterals of
         your evaluation job.
      4. Choose **Add**.

   2. To add a custom evaluation job, complete the following
      step:
      1. Choose **Custom**.
      2. Enter a name for the evaluation job.
      3. Choose **Add**.

###### To add an additional evaluation job to your model package, complete the

following steps.

1. Choose the **Evaluate** tab.
2. Choose the **Gear** (
   ![Black square icon representing a placeholder or empty image.](images/icons/Settings_squid.png)
   ) icon under the **Train**
   tab.
3. In the dialog box, choose **Add**.
4. You can add an evaluation job from Amazon S3 or a custom evaluation
   job.
   1. To add an evaluation job with collaterals from Amazon S3, complete
      the following steps.
      1. Choose **S3**.
      2. Enter a name for the evaluation job.
      3. Enter the Amazon S3 location to the output collaterals of
         your evaluation job.
      4. Choose **Add**.

   2. To add a custom evaluation job, complete the following
      step:
      1. Choose **Custom**.
      2. Enter a name for the evaluation job.
      3. Choose **Add**.
