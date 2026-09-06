

# AWS Transform MGN (MGN)
<a name="getting-started-step2-MGN"></a>

AWS Transform MGN (MGN) is a highly automated re-hosting solution that simplifies, expedites, and reduces the cost of migrating applications to AWS. It enables companies to re-host a large number of physical, virtual, or cloud servers without compatibility issues, performance disruption, or long cutover windows. AWS MGN continuously replicates source servers to your AWS account. When you’re ready, it automatically converts and launches your servers on AWS so you can quickly benefit from the cost savings, productivity, resilience, and agility of the Cloud. In addition, AWS MGN allows you to modernize launched applications by running custom or preconfigured actions.

MGN is MAP 2.0 aware and can automatically apply the required MAP 2.0 tags to your workloads migrated by MGN.



**To get started**

1. Set up MGN in any AWS account associated in the same AWS organization as the payer account listed in your MAP 2.0 term. For more information about setting up MGN, see [Getting started with AWS Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html) in the *Application Migration Service guide*.

1. During the MGN setup, choose **Settings**.

1. Choose the **Launch** template tab.

1. Choose **Edit**.

1. Choose **Add MAP tag to launched servers**.

1. Enter and replace your **MPE ID** with the tag value you want to apply to the migrated workloads.

   **Example**: 
   + If your MPE ID is {{12345}}, use the value {{mig12345}}.
   + If your MPE ID is {{ABCDE12345}}, use the value {{migABCDE12345}}.

1. Choose **Save template**.

1. Proceed migrating your workloads with MGN as detailed in Source Servers of the Application Migration Service guide. For more information about tagging in MGN, see [Tags](https://docs.aws.amazon.com/mgn/latest/ug/Cirrus_tags.html) in the *Application Migration Service guide*.

   

   The MAP 2.0 tags are automatically applied to all workloads migrated using MGN. Repeat Steps 2 - 7 if you are using MGN to migrate to multiple accounts or regions.

Depending on your migrated resource and MPE ID, the tag value can be any of the following:

## Short MPE IDs
<a name="mgn-short-ids"></a>
+ `mig{{5-digit MPE ID}}`
+ `sap{{5-digit MPE ID}}`
+ `oracle{{5-digit MPE ID}}`

## Long MPE IDs
<a name="mgn-long-ids"></a>
+ `mig{{10 alphanumeric MPE ID characters}}`
+ `sap{{10 alphanumeric MPE ID characters}}`
+ `oracle{{10 alphanumeric MPE ID characters}}`

**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your MPE ID, see [MPE ID length](mpe-length.md).