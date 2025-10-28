# Update deployment

information (Studio)

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

After you evaluate your model performance and determine that it is ready to
use for production workloads, you can change the approval status of the model to
initiate CI/CD deployment. For more about approval status definitions, see [Update the Approval Status of a
Model](model-registry-approve.md "model-registry-approve.md").

###### To view or update details related to the model package deployment,

complete the following steps.

1.  On the **Deploy** tab, view the model package
    approval status. Possible values can be the following:

        * **Pending Approval**: The model is registered
         but not yet approved or rejected for deployment.
        * **Approved**: The model is approved for CI/CD
         deployment. If there is an EventBridge rule in place that initiates
         model deployment upon a model approval event, as is the case for
         a model built from a SageMaker AI project template, SageMaker AI also deploys
         the model.
        * **Rejected**: The model is rejected for
         deployment.

    If you need to change the approval status, choose the dropdown menu
    next to the status and choose the updated status.

2.  To update the model package approval status, choose the dropdown next
    to the approval status and choose the updated approval status.
3.  In the **Containers** list, view the inference image
    containers.
4.  In the **Instances** list, view the instances which
    compose your deployment endpoint.
