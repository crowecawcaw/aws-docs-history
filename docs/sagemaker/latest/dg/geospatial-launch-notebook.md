# Create an Amazon SageMaker Studio Classic notebook using the

geospatial image

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

###### Note

Currently, SageMaker geospatial is only supported in the US West (Oregon) Region.

If you don't see SageMaker geospatial available in your current domain or notebook instance, make sure that you're currently in the US West (Oregon) Region.

Use the following procedure to create Studio Classic notebook with the SageMaker geospatial image. If your default studio experience is Studio, see [Accessing SageMaker geospatial](access-studio-classic-geospatial.md "access-studio-classic-geospatial.md") to learn about starting a Studio Classic application.

###### To create a Studio Classic notebook with the SageMaker geospatial image

1. Launch Studio Classic
2. Choose **Home** in the menu bar.
3. Under **Quick actions**, choose **Open Launcher**.
4. When the **Launcher** dialog box opens. Choose **Change environment** under **Notebooks and compute resources**.
5. When, the **Change environment** dialog box opens. Choose the **Image** dropdown and choose or type **Geospatial 1.0**.

![A dialogue boxing showing the correct geospatial image and instance type selected.](images/geospatial-environment-dialogue.png) 6. Next, choose an **Instance type** from the dropdown.

SageMaker geospatial supports two types of notebook instances: CPU and GPU. The supported CPU
instance is called **ml.geospatial.interactive**. Any of the G5-family of GPU instances can be used with the Geospatial 1.0 image.

###### Note

If you receive a **`ResourceLimitExceeded`** error when
attempting to start a GPU based instance, you need to request a quota
increase. To get started on a Service Quotas quota increase request, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_ 7. Choose **Select**. 8. Choose **Create notebook**.
After creating a notebook, to learn more about SageMaker geospatial, try the [SageMaker geospatial tutorial](geospatial-demo.md "geospatial-demo.md"). It shows you how to process
Sentinel-2 image data and perform land segmentation on it using the earth observation
jobs API.
