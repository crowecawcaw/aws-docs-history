

# Add a training job (Studio)
<a name="model-registry-details-studio-training"></a>

**Important**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md).

You can add one training job, created externally or with SageMaker AI, to your model. If you add a SageMaker training job, SageMaker AI prepopulates the fields for all of the subpages in the **Train** tab. If you add an externally created training job, you need to add details related to your training job manually. 

**To add a training job to your model package, complete the following steps.**

1. Choose the **Train** tab.

1. Choose **Add**. If you do not see this option, you may already have a training job attached. If you want to remove this training job, complete the following instructions to remove a training job. 

1. You can add a training job you created in SageMaker AI or a training job you created externally.

   1. To add a training job you created in SageMaker AI, complete the following steps.

      1. Choose **SageMaker AI**.

      1. Select the radio box next to the training job you want to add.

      1. Choose **Add**.

   1. To add a training job you created externally, complete the following steps.

      1. Choose **Custom**.

      1. In the **Name** field, insert the name of your custom training job.

      1. Choose **Add**.