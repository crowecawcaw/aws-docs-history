AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Step 5: Use Strategy Recommendations in the Migration Hub

console to get recommendations

This section describes how to use Strategy Recommendations in the Migration Hub console to get migration
recommendations for the first time.

###### To get recommendations

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md "setting-up.md"), sign in to the AWS Management Console and open the Migration Hub
   console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the Migration Hub console navigation pane, choose **Strategy**.
3. On the **Migration Hub Strategy Recommendations** page, choose
   **Get recommendations**.
4. Choose **Agree** if you agree to allow Migration Hub to create a
   service-linked role (SLR) in your account. For more information about the SLR, see
   [Using service-linked roles for
   Strategy Recommendations](using-service-linked-roles.md "using-service-linked-roles.md").
5. **Configure data sources**
   1. On the **Configure data sources** page, you must choose
      the source of your servers to analyze from the following options:
      1. **Strategy Recommendations application data collector**
         – You can use the Strategy Recommendations collector to retrieve information
         about VMs hosted in VMware vCenter automatically. Using this option,
         you don't need to perform additional setup.
      2. **Manual import** – If you
         want to bring in data about your servers and applications
         independently, you can use the Strategy Recommendations import template. The import
         template is a JSON file in which you can fill out the available
         information for your VMs.
      3. **Application Discovery Service** – You can use
         Application Discovery Service to gather information about your on-premises applications
         and servers. In the Migration Hub console, under the
         **Tools** section, you can choose from multiple
         options under **Discovery tools**. For example,
         you can choose **Application Discovery Service Agentless Collector**,
         **AWS Discovery Agent**, or
         **Import** (for CSV files).

   2. The **Servers** table lists all of the available servers
      based on your selection in the data source section.
   3. Under Registered application data collectors, the application data
      collectors that you've set up are listed. If you haven't set up any data
      collectors, you can download the data collector and then deploy it. For more
      information, see [Step 1: Download the Strategy Recommendations
      collector](getting-started-dowmload-collector.md "getting-started-dowmload-collector.md") and [Step 2: Deploy the Strategy Recommendations collector](getting-started-deploy.md "getting-started-deploy.md").

   ###### Note

   To get strategy recommendations, you must set up at least one
   application data collector or perform an application data import. If you
   want to add your application-level data without setting up a collector,
   you can use the application data import template. You can add additional
   data sources later. 4. If you selected **Manual import**, under **Import
   details**, choose **Add new import**. 5. For **Import name**, enter a name for your import. 6. For **S3 bucket URI**, enter the S3 bucket URI for your
   import JSON file to upload to.

   ###### Important

   The S3 bucket name must start with a prefix of
   `migrationhub-strategy`. 7. Choose **Next**.

6. **Specify preferences**
   1. On the **Specify preferences** page, set up your business
      goals and migration preferences. Strategy Recommendations recommends the optimal strategy
      for migrating and modernizing your applications and databases based on the
      preferences that you specify. You can change these preferences at a later
      time.
   2. Choose **Next**.

7. **Review and submit**.
   1. Review your configured data sources and migration preferences.
   2. If everything looks correct, choose **Start data
      analysis**. This will perform an analysis of your server
      inventory and runtime environment and the application binaries for your
      Microsoft IIS and Java applications.

   ###### Note

   The status of the binary analysis is not displayed in the console.
   When the analysis completes, you will either see a link to the
   anti-pattern report or a message indicating that the analysis was not
   successful.

## Next

[Viewing strategy recommendations in
Strategy Recommendations](viewing-recommendations.md "viewing-recommendations.md")
