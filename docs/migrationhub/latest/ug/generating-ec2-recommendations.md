AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Generating Amazon EC2 recommendations in

AWS Migration Hub

In the **Export Amazon EC2 instance recommendations** page of the Migration Hub
console, you'll choose your recommendation preferences. These preferences include
resource sizing, instance type preferences, and instance type exclusions. Use the
following procedure to generate your Amazon EC2 instance recommendations.

###### To generate Amazon EC2 instance recommendations

1. Open a browser and sign into the Migration Hub console at
   https://console.aws.amazon.com/migrationhub.
2. In the navigation pane, under **Assess**, choose
   **Amazon EC2 instance recommendations**.
3. Choose your Amazon EC2 instance sizing preference for your discovered servers. You
   can choose one of the following options.
   - **Maximum utilization** – This
     option sizes your instance recommendations based off of the maximum
     (peak) CPU and RAM utilization data that was collected by the discovery
     tools.
   - **Current server specification** –
     You have the two options of **Direct match** or
     **Custom match**.
     - **Custom match** – Scales
       the CPU and RAM specifications for your instances relative to
       the collected specification data. For example setting CPU to 50%
       and RAM to 60% will generate recommendations that assume 50%
       utilization of your discovered CPU usage and 60% utilization of
       your total RAM usage.
     - **Direct match** – Matches
       the recommendations based off of the exact CPU and RAM
       specification data collected by the discovery tools you used to
       get the data into Migration Hub.

   - **Average utilization** – This
     option sizes your instance recommendations based off of the average CPU
     and RAM utilization data that was imported or collected by the discovery
     tools.
   - **Percentile of utilization** – If
     you used an AWS Application Discovery Agent or an AWS Agentless Discovery Connector to collect your server data,
     you can generate your recommendations using percentiles of time-series
     utilization data. Percentile-based recommendations are only generated
     for servers with data collected by a Discovery Connector from March
     12th, 2019 onwards, or by a Discovery Agent.

   For all the data points collected for CPU and RAM utilization, a
   percentile is a value that exists below a given percentage of
   utilization since data has been discovered. For example, the 75th
   percentile represents the value under 75 percent of all the RAM and CPU
   utilization data that has been discovered.

4. Choose your Amazon EC2 instance type preferences, including AWS Region, tenancy,
   and pricing model.
   - **Region** – Your AWS Region
     selection affects Amazon EC2 instance availability and pricing.
   - **Tenancy** – This defines how EC2
     instances are distributed across physical hardware and affects
     pricing.
     - **Shared** – Multiple
       customers may share the same physical hardware.
     - **Dedicated** – Only your
       instances will run on the same physical hardware.

   - **Pricing Model** – This defines
     the kind of billing and commitment you intend to use for your
     instances.
     - **On-Demand** – Requires no
       long-term commitment.
     - **Reserved** – requires 1-3
       year commitment and provides discounts and additional confidence
       in your ability to launch instances when needed. For more
       information on reserved instance pricing model information, see
       [Reserved Instances](../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md "../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md") in the
       _Amazon EC2 User Guide_

5. Optionally, choose any Amazon EC2 instance type exclusions to prevent specific
   types of instances from appearing in your recommendations.
6. When you're done setting your preferences, choose **Export
   recommendations**. This will begin generating your recommendations.
   When the process is complete, your browser will automatically download a compressed
   archive (ZIP) file, containing the following two files.

| File name                                    | Description                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| EC2InstanceRecommendations-{type}-{date}.csv | Details of each server’s recommended Amazon EC2 instance type and cost. For more information, see [Understanding your Amazon EC2 recommendations in AWS Migration Hub](understanding-ec2-recommendations.md "understanding-ec2-recommendations.md").                                                                                         |
| MgnInventory-{type}-{date}.csv               | A list of server configurations that are compatible with AWS Application Migration Service and recommend Amazon EC2 instance configurations. For more information, see [Importing your data inventory](../../../mgn/latest/ug/import-main.md "../../../mgn/latest/ug/import-main.md") in the _AWS Application Migration Service User Guide_. | Large datasets can take a few minutes to generate recommendations. You can generate new recommendations at any time by repeating this procedure with a different set of preferences. |
