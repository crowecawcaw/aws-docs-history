# Exporting target recommendations

with AWS DMS Fleet Advisor

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

After you generate target recommendations, you can save a copy of the list of recommendations as
a comma-separated value (CSV) file.

###### To generate target recommendations

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/https://console.aws.amazon.com/dms/v2/").

Make sure that you choose the AWS Region where you use the DMS Fleet Advisor. 2. In the navigation pane, choose **Recommendations** under
**Assess**, and then select the recommendations to include in your CSV file. 3. Choose **Export to CSV**, enter the file name and choose the folder on your PC
where to save this file. 4. Open the CSV file.
The CSV file with recommendations contains the following information.

- **CreatedDate** – The date when DMS Fleet Advisor created the target engine
  recommendation.
- **DatabaseId** – The identifier of the source database for which
  DMS Fleet Advisor created this recommendation.
- **DeploymentOption** – The deployment option for the recommended Amazon RDS
  DB instance.
- **EngineEdition** – The recommended target Amazon RDS engine
  edition.
- **EngineName** – The name of the target engine.
- **InstanceMemory** – The amount of memory on the recommended Amazon RDS DB
  instance.
- **InstanceSizingType** – The size of your target instance.
- **InstanceType** – The recommended target Amazon RDS instance type.
- **InstanceVcpu** – The number of virtual CPUs on the recommended Amazon RDS
  DB instance.
- **Preferred** – A Boolean flag that indicates that this target option
  is recommended.
- **Status** – The status of the target engine recommendation.
- **StorageIops** – The number of I/O operations completed each second
  (IOPS) on the recommended Amazon RDS DB instance.
- **StorageSize** – The storage size of the recommended Amazon RDS DB
  instance.
- **StorageType** – The storage type of the recommended Amazon RDS DB
  instance.
- **WorkloadType** – The deployment option for your target engine such
  as Multi-AZ or Single-AZ deployment.
