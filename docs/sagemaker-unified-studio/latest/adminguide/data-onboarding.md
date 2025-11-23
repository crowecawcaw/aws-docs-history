# Onboarding data in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio supports the following key capabilities for Amazon SageMaker Lakehouse data
management and governance.

- Automated onboarding of Amazon SageMaker Lakehouse: you can automatically ingest the
  metadata of all datasets in your Amazon SageMaker Lakehouse into the catalog. This removes
  the need for manually granting permissions, creating metadata ingestion jobs, or configuring
  scripts. By onboarding assets in a single step, administrators can immediately make this
  data discoverable and ready for governance, analysis, and collaboration within
  Amazon SageMaker Unified Studio.
- Continuous real-time metadata ingestion: After onboarding existing Amazon SageMaker
  datasets, the catalog continuously keeps metadata current via real-time streaming. Any
  changes, such as new tables or schema updates, are automatically reflected in the catalog.
  This eliminates the need for periodic ingestion jobs, reduces stale metadata risk, and
  lowers your operational costs while ensuring your teams have access to the freshest
  metadata.
- Continuous Real-time data quality sync: After onboarding existing Amazon SageMaker datasets,
  the catalog continuously keeps data quality results current via real-time streaming. Metrics
  such as completeness, timeliness, and accuracy are
  automatically synchronized, enabling data consumers to visualize quality scores and track changes
  over time. This eliminates manual dataSourceRuns and ensures immediate visibility into data health
  status.
- Direct sharing: data owners can now proactively grant access to their assets without
  waiting for data access requests. This enables smoother cross-team collaboration, helping
  accelerate projects and reduce handoffs while maintaining strong governance.
  You can onboard your Amazon SageMaker Lakehouse data as part of creating a new Amazon
  SageMaker unified domain or for an existing domain.

- If you create your new domain using the quick set up option, data onboarding is
  supported as part of domain creation. For more information, see [Create a Amazon SageMaker Unified Studio domain -
  quick setup](create-domain-sagemaker-unified-studio-quick.md "create-domain-sagemaker-unified-studio-quick.md").
- If you create your new domain using the manual setup option, once the domain is created
  you must first enable the Tooling blueprint before you can onboard your data. To do this,
  complete the steps in [Enable or disable blueprints](enable-disable-blueprints.md "enable-disable-blueprints.md") (choose the Tooling blueprint in the
  **Blueprints** tab). You can also get to the **Enable
  Tooling** blueprint page by first navigating to the **Onboarded
  data** tab, then attempting to onboard your data by choosing **Onboard
  data**. This displays the **Tooling blueprint not enabled**
  notification and the **Enable Tooling** button opens the **Enable
  Tooling** page where you can complete this task.
  To onboard your data in an existing Amazon SageMaker unified domain, complete the following
  procedure.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector in the top
   navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the list. The
   name is a hyperlink.
3. On the domain's details page, navigate to the **Onboarded data** tab
   and choose **Onboard data**.
4. On the **Onboard your data** page, do the following and then choose
   **Onboard data**.
   - Check the AWS Glue (SageMaker Lakehouse) checkbox.
   - Optional - check the **Make your data discoverable** checkbox -
     other users in the domain will be able to find your data in the catalog. This setting
     can only be reverted later in Amazon SageMaker Unified Studio by un-publishing each dataset
     individually.
   - Under **Permissions and resources**, specify the provisioning role.
     Amazon SageMaker Unified Studio uses this role to provision and manage resources required to onboard the account data.
   - Under **Owning project** specify the owning project. Your data will
     be accessible in this project that is auto-created in Amazon SageMaker Unified Studio. Once created, you
     cannot rename the project.
   - Under **Add project owner**, add the project owner for the owning
     project.
