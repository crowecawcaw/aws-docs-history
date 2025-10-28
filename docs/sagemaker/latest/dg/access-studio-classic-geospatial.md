# Accessing SageMaker geospatial

###### Note

Currently, SageMaker geospatial capabilities are only supported in the US West (Oregon) Region and in Studio Classic.

If you don't see the SageMaker geospatial UI available in your current Studio Classic instance check to make sure you are currently in the US West (Oregon) Region.

A domain is required to access SageMaker geospatial. If you created a domain prior to November 30, 2023 the default experience is Studio Classic.

If you created a domain after November 30, 2023 or if you have migrated to
Studio, then you can use the following procedure to activate Studio Classic from within
Studio to use SageMaker geospatial features.

To learn more about creating a domain, see [Onboard to Amazon SageMaker AI domain](gs-studio-onboard.md "gs-studio-onboard.md").

###### To access Studio Classic from Studio

1. Launch Amazon SageMaker Studio.
2. Under **Applications**, choose **Studio Classic**.
3. Then, choose **Create Studio Classic space**.
4. On the **Create Studio Classic space** page, enter a **Name**.
5. Disable the **Share with my domain** option. SageMaker geospatial is not available in shared domains.
6. Then choose **Create space**.
   When successful the **Status** changes to **Updating**. When your Studio Classic application is ready to be used the status changes to **Stopped**.

To start your Studio Classic application, choose **Run**.
