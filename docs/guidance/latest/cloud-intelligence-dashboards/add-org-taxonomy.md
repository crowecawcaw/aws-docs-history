

# Add organizational taxonomy
<a name="add-org-taxonomy"></a>

## Introduction
<a name="introduction"></a>

Most organizations need to answer a simple question: *which team, business unit, or cost center is responsible for this AWS spend?* Attributing costs to the parts of your business is called **cost allocation**, and the set of labels you use to group that spend — such as team, environment, or business unit — is your organizational [taxonomy](https://en.wikipedia.org/wiki/Taxonomy). Taxonomies range from a single level of business units to complex, multi-dimensional structures.

This guide shows you how to add your organization’s taxonomy to Cloud Intelligence Dashboards (CID) so you can filter and group costs by the dimensions that matter to your business. By the end, you will be able to break down costs by account, organizational unit (OU), tag, or cost category — and, optionally, restrict what each user can see.

The following video introduces the concept of taxonomy in the context of AWS resource management. It will guide you through the main concepts using the example of Unicorn Rental Corporation.

[![AWS Videos](http://img.youtube.com/vi/8-OMF9sca2E?rel=0/0.jpg)](http://www.youtube.com/watch?v=8-OMF9sca2E?rel=0)


### Before you begin
<a name="add-org-taxonomy-prerequisites"></a>

The tools and versions you need depend on which taxonomy sources you use. Confirm the relevant rows below before you start:


| If you want to use…​ | You need…​ | 
| --- | --- | 
| Any taxonomy method |  `cid-cmd` version 4.4.17 or later (`pip3 install -U cid-cmd`) | 
| Account Tags as Cost Allocation Tags (from CUR 2.0), IAM Principal Tags, IAM Principal ARN, or User Attributes |  [Data export stack](data-exports.md) `v0.11.0` or later (includes the **Tags** and `line_item_iam_principal` columns) | 
| OU names, OU tags, or hierarchical tag inheritance |  [CID Data Collection](data-collection.md) deployed | 

## Choosing an allocation approach
<a name="choosing-an-allocation-approach"></a>

Cost allocation in AWS typically follows two primary patterns. Use the quick guide below to find the one that fits your needs, then read the details that follow.


| If you need to…​ | Use…​ | 
| --- | --- | 
| Allocate costs by whole account (team owns the account), and adapt easily to frequent reorganizations |  **Account-Level Allocation** — start with [OU or Account Tags](#add-org-taxonomy-account-level-cost-allocation)  | 
| Split costs *within* a shared account across teams, applications, or environments |  **Resource-Level Allocation** — use [Cost Allocation Tags or Cost Categories](#add-org-taxonomy-resource-level-cost-allocation)  | 

Here is what each pattern covers in more detail:

1.  [Account-Level Allocation](#add-org-taxonomy-account-level-cost-allocation) - Uses information at the AWS account level, such as:

   1. AWS Account Names

   1. Organizational Unit (OU) hierarchical structure

   1. Account-level or OU level tagging in AWS Organizations

   1. External sources (e.g. CMDB) as a source of truth to allocate account ownership based on organizational policies

1.  [Resource-Level Allocation](#add-org-taxonomy-resource-level-cost-allocation) - Enables more granular allocation through:

   1. AWS Cost Allocation Tags (user-defined and AWS-generated)

      1.  [Account Tags as Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/account-tags-cost-allocation.html) (available in CUR2)

      1.  [IAM Principal Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/iam-principal-cost-allocation.html) (available in CUR2)

      1.  [User Attributes](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/user-attributes-cost-allocation.html) (available in CUR2)

   1. AWS Cost Categories

Cloud Intelligence Dashboards provide a comprehensive way to integrate organizational taxonomy into your dashboards, enabling precise filtering and cost allocation tracking. You can define a set of taxonomy fields to be used as Filters and GroupBy dimensions within the CID dashboards. Additionally, you can configure Row-Level Security (RLS) to restrict access based on one of these taxonomy fields, ensuring that users see only the data relevant to their scope of responsibility.

### Choose your taxonomy sources
<a name="choose-your-taxonomy-sources"></a>

It is essential to establish reporting that accurately reflects the current structure of your organization while also accounting for potential future changes. Once your taxonomy is clear, the next step is to map it to the appropriate technical data source. The table below lists the available sources, where each one comes from, and what it requires.

![taxonomy](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/taxonomy-pipe.svg)



| Name | Level | Source | Prerequisite | Comment | 
| --- | --- | --- | --- | --- | 
| Account Tag | Account Level | AWS Organizations or CUR2 | CID Data Collection or CUR2 | A simple way to achieve account level taxonomy and cost allocation from CUR2 or AWS Organizations | 
| OU Name | Account Level | AWS Organizations | CID Data Collection |  | 
| OU Tag | Account Level | AWS Organizations | CID Data Collection | [RECOMMENDED] More flexible than Account Tag. CID Data Collection allows collecting Hierarchical Tags where lower-level Tags can override higher-level ones. This can create a flexible system that does not require setting tags on the individual account level | 
| Account Name | Account Level | AWS Organizations or CUR2 | CID Data Collection or CUR2 | Some organizations can have an established naming convention for AWS Accounts. A part of this name can be used for a business unit taxonomy. | 
| AWS Cost Allocation Tags | Resource Level | CUR | AWS Data Exports |  | 
| IAM Principal Tags | Resource Level | CUR2 `tags` column | AWS Data Exports with Tags column | Tags attached to IAM principals (roles/users) making API calls. Useful for attributing costs to specific teams or applications based on who performed the action. | 
| User Attributes | Resource Level | CUR2 `tags` column | AWS Data Exports with Tags column | Workforce user attributes (cost center, division, department) from IAM Identity Center. Supported for Amazon Q Business, Amazon Q Developer, and Amazon Quick. | 
| IAM Principal (ARN) | Resource Level | CUR2 `line_item_iam_principal` column | AWS Data Exports | The full IAM principal ARN that made the API call. Currently supported for Amazon Bedrock. | 
| AWS Cost Categories | Resource Level or Account Level | CUR | AWS Data Exports |  | 

Additional recommendations:

1.  **Anticipate Organizational Change**. Using AWS Account Tags or OU (Organizational Unit) Tags can be a flexible and maintainable approach, especially in environments where organizational changes are frequent. Account-level tagging allows you to adapt to these changes with minimal operational overhead. However, if an account contains shared resources used across multiple teams or business units, Resource-Level Attribution becomes necessary to accurately reflect usage and costs at a more granular level.

1.  **Balance Granularity and Effort**. Resource-Level Attribution, such as Tags and Cost Categories, provides detailed visibility into per resource usage and cost and is essential when shared resources exist within a single account. It requires consistent and disciplined tagging practices across teams and services, along with ongoing governance to ensure tags remain accurate and meaningful over time. In contrast, Account-Level Attribution is easier to implement and maintain but offers less granularity.

## Account Level Cost Allocation
<a name="add-org-taxonomy-account-level-cost-allocation"></a>

### Using Account Tags as Cost Allocation Tags in CUR2
<a name="using-account-tags-as-cost-allocation-tags-in-cur2"></a>

AWS supports enabling Account Tags from AWS Organizations as Cost Allocation Tags (available since December 2025).

The main benefit of Account Tags as Cost Allocation Tags is simplicity: all required information comes directly from CUR2, eliminating the need for additional data sources or collection mechanisms.

 **Implementation Steps:** 

1. In AWS Organizations, add tags to your AWS accounts (e.g., `Owner`, `BusinessUnit`, `CostCenter`)

1. In the AWS Billing Console, activate these account tags as Cost Allocation Tags

1. Upgrade your [data export stack](data-exports.md) on payer account(s) to `v0.11.0` or later if you are running an older version

1. Wait 24 hours for the tags to appear in your Cost and Usage Report

1. Run `cid-cmd update --force --recursive` to discover and configure the tags

1. Select the account-level tags you want to use as taxonomy dimensions when prompted

 **When to Use CID Data Collection Method for organizational data Instead:** 

While Account Tags as Cost Allocation Tags in CUR2 are recommended for simple account level taxonomy use cases, you should use the [Advanced account map](#add-org-taxonomy-account-map-based-on-org-example) method if:
+ You need to use OU Tags as part of your taxonomy (OU Tags as Cost Allocation Tags are not yet supported)
+ You require hierarchical tag inheritance from OUs to accounts
+ You need more complex organizational hierarchy mapping

### Using Account Map View
<a name="using-account-map-view"></a>

To implement account level mapping, CID uses a special View in Amazon Athena called `account_map`. This Athena view is specifically designed to be customizable by customers. It can be generated using `cid-cmd map` (recommended) or created manually using any of the following data sources:

1. Cost and Usage Report (CUR) data. CUR2 data contains Account Names.

1. AWS Organizations metadata collected via [CID Data Collection](data-collection.md).

1. External sources such as external [CMDB](https://en.wikipedia.org/wiki/Configuration_management_database) systems or just a spreadsheet or csv file on Amazon S3.

![Architecture](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/ou-integration-architecture.png)


The following sections describe different ways to use the `account_map` view to build dynamic or static account mapping to organizational taxonomy dimensions.

### Account map based on AWS Organizations data (Recommended)
<a name="add-org-taxonomy-account-map-based-on-org-example"></a>

The `cid-cmd map` command provides an interactive workflow for creating enriched `account_map` views with custom taxonomy dimensions. It supports multiple data sources and can be used with or without an `organization_data` table in Athena.

The `cid-cmd map` command automatically generates an `account_map` Athena view with your organizational taxonomy columns. It supports three data source modes:


| Mode | Description | 
| --- | --- | 
|  **organization\_data table**  | Uses AWS Organizations data collected via [CID Data Collection](data-collection.md). Supports OU hierarchy levels, hierarchical tags, and account name splitting. | 
|  **CSV file only**  | Creates the account map entirely from a CSV file. No Athena source table required. | 
|  **Both**  | Combines organization\_data as the base account list with a CSV file for additional taxonomy columns (e.g. from an external CMDB). | 

 **Prerequisites:** 
+ For organization\_data mode: [CID Data Collection](data-collection.md) must be deployed
+ For CSV mode: A CSV file with at minimum an `account_id` column
+  `cid-cmd` version 4.4.17 or later

 **Basic usage:** 

```
# Interactive mode — prompts for data source selection
cid-cmd map

# (Optional) With a CSV file for additional static mapping taxonomy
cid-cmd map --file accounts_mapping.csv
```

 **Available taxonomy dimension sources (organization\_data mode):** 


| Source | Description | 
| --- | --- | 
|  **Tags from source table**  | Extract values from OU-level or Account-level tags in AWS Organizations (hierarchical inheritance supported) | 
|  **OU hierarchy level**  | Use the name of the OU at a specific level (e.g., level 2 = Business Unit) | 
|  **Additional file (CSV)**  | Join columns from a CSV file by account\_id | 
|  **Split account name**  | Extract a portion of the account name using a delimiter (e.g., `prod-team1-app` → `team1`) | 

 **Example workflow:** 

```
$ cid-cmd map --file accounts_mapping.csv

? Select account data source for taxonomy:
❯ organization_data table (collected with CID Data Collection)
  CSV file only
  Both (organization_data table + CSV file for additional taxonomy)

? Select data sources for taxonomy dimensions:
  ☑ Tags from source table
  ☑ OU hierarchy level
  ☑ Additional file (CSV)
  ☐ Split account name column
```

The command will guide you through selecting specific tags, OU levels, and file columns to include as taxonomy dimensions, then preview the resulting SQL before creating the view.

#### See the demo: `cid-cmd map` walkthrough
<a name="collapsible-section-id-add-org-taxonomy-map-demo"></a>

The following recording walks through a full `cid-cmd map --file accounts.csv` session in *Both* mode — combining `organization_data` with a CSV file, selecting OU tags and hierarchy levels, splitting the account name, and creating the `account_map` view.

![cid-cmd map walkthrough](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/account-mapper-full-demo.gif)


#### Example of generated SQL (organization\_data mode)
<a name="collapsible-section-id-add-org-taxonomy-2"></a>

```
CREATE OR REPLACE VIEW "cid_cur"."account_map" AS
SELECT
    -- Mandatory
      id AS account_id
    , name AS account_name
    , managementaccountid AS parent_account_id

    -- Friendly name for management account(s)
    , CASE managementaccountid
        WHEN '111111111111' THEN 'My Management Org'
        WHEN '222222222222' THEN 'My Test Org'
        ELSE managementaccountid
    END AS parent_account_name

    -- OU hierarchy levels
    , TRY(hierarchy[1].name) AS o_u_level1
    , TRY(hierarchy[2].name) AS business_unit

    -- Hierarchical Tags (set on OU level, override on lower OU or Account level)
    , element_at(filter(hierarchytags, x - x.key = 'environment'), 1).value AS environment
    , element_at(filter(hierarchytags, x - x.key = 'cost_center'), 1).value AS cost_center

    -- Part of Account Name (when naming convention allows)
    , TRY(split_part(name, '-', 1)) AS account_prefix

    -- Additional columns from CSV file (joined by account_id)
    , file.team AS team
FROM
    "optimization_data"."organization_data" org
LEFT JOIN "cid_cur"."account_map_file_source" file ON org.id = file.account_id
```

You can also create a similar view manually if you want to tailor it to your specific needs not supported by `cid-cmd map` capabilities. Please note that you do not need to use all the fields from this example — adjust it to your specific business and organizational requirements.

### Static Account Map from CSV
<a name="static-account-map-from-csv"></a>

As an alternative to the dynamic account map based on AWS Organizations data, you can create a static account map only from a CSV file. This approach is useful when you have a custom mapping maintained in a CMDB or spreadsheet and you want to bring it into the account map.

 **Using `cid-cmd map` with CSV file:** 

```
cid-cmd map --file my_accounts.csv
# Select "CSV file only" when prompted
```

The CSV file should contain at minimum an `account_id` column. All other columns can be selected as taxonomy dimensions during the interactive workflow.

#### Example of resulting static account map generated with cid-cmd or created manually
<a name="collapsible-section-id-add-org-taxonomy-3"></a>

```
CREATE OR REPLACE VIEW account_map AS
SELECT *
FROM
  (
 VALUES
     ROW ('111111111111', 'Account1', 'Company 1', 'Business Unit 11')
   , ROW ('222222222222', 'Account2', 'Company 1', 'Business Unit 11')
   , ROW ('333333333333', 'Account3', 'Company 2', 'Business Unit 21')
   , ROW ('444444444444', 'Account4', 'Company 2', 'Business Unit 22')
)  ignored_table_name (
    account_id,   --mandatory
    account_name, --mandatory
    company,      --custom
    business_unit --custom
)
```

## Resource Level Cost Allocation (Tags and Cost Categories)
<a name="add-org-taxonomy-resource-level-cost-allocation"></a>

Resource-level cost allocation uses tags and cost categories embedded in the Cost and Usage Report (CUR) to attribute costs to specific resources, teams, or applications. The `cid-cmd` tool automatically discovers available tags and allows you to select which ones to include in your dashboards.

### Cost Allocation Tags
<a name="cost-allocation-tags"></a>

Cost Allocation Tags are the most common resource-level taxonomy source. They come from the `resource_tags` column in CUR and include both user-defined tags and AWS-generated tags.

### IAM Principal Tags, IAM Principal ARN, and User Attributes
<a name="iam-principal-tags-iam-principal-arn-and-user-attributes"></a>

CUR2 introduces additional tag types in the `tags` MAP column that enable attribution based on **who** performed an action rather than just **what** resource was used:


| Tag Type | CUR2 Column | Supported Services | Use Case | 
| --- | --- | --- | --- | 
|  [**IAM Principal Tags**](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/iam-principal-cost-allocation.html)  |  `tags` (prefix: `iamPrincipal/`) | Amazon Bedrock | Tags attached to the IAM role or user that made the API call. Useful for attributing costs to teams when multiple teams share an account but use different IAM roles. | 
|  **IAM Principal ARN**  |  `line_item_iam_principal`  | Amazon Bedrock | The full ARN of the principal that made the API call. Useful for seeing which role or user is driving model invocations. | 
|  [**User Attributes**](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/user-attributes-cost-allocation.html)  |  `tags` (prefix: `userAttribute/`) | Amazon Q Business, Amazon Q Developer, Amazon Quick | Workforce user attributes (cost center, division, department) from IAM Identity Center. Enables automatic cost allocation based on organizational structure for per-user services. | 

 **Prerequisites:** 
+  [Data export stack](data-exports.md) version `v0.11.0` or above. This will ensure:
  + CUR2 data export includes the **Tags** column (for IAM Principal Tags and User Attributes)
  + CUR2 data export includes `line_item_iam_principal` column

### Cost Categories
<a name="cost-categories"></a>

AWS Cost Categories allow you to define rules that categorize costs into meaningful groups. They appear in CUR as the `cost_category` column and are automatically discovered by `cid-cmd`.

### How cid-cmd discovers tags and cost categories
<a name="how-cid-cmd-discovers-tags-and-cost-categories"></a>

When you run `cid-cmd update --force --recursive`, the tool scans the CUR2 `tags` column for each prefix separately:

```
Scanning resource_tags in cur2_data.
 resource_tags   | Distinct Values (Top 20)
 Environment     | 3
 Project         | 18
 Owner           | 42

Scanning cost_category in cur2_data.
 cost_category   | Distinct Values (Top 20)
 Team            | 6
 Department      | 4

Scanning Account Tags (tags column) in cur2_data.
 Account Tags    | Distinct Values (Top 20)
 BusinessUnit    | 5
 Environment     | 3

Scanning User Attributes (tags column) in cur2_data.
 User Attributes         | Distinct Values (Top 20)
 PipelineName            | 12
 DeveloperAlias          | 45

Scanning IAM Principal Tags (tags column) in cur2_data.
 IAM Principal Tags      | Distinct Values (Top 20)
 Team                    | 8
 ServiceName             | 15

Scanning line_item_iam_principal in cur2_data.
 line_item_iam_principal | 234 distinct values
```

You can then select which of these to include as taxonomy dimensions in your dashboards. During selection the choices are grouped by their source (resource tags, IAM principal tags, account tags, user attributes, cost categories), so it is easy to see where each field comes from.

If the same business dimension (such as `application` or `team`) appears under more than one source, you can combine them into a single dashboard field — see [Merging multiple sources into a single dimension](#add-org-taxonomy-merging-dimensions).

### Performance Considerations
<a name="performance-considerations"></a>

Please note that introducing tags with many unique values can significantly expand the dataset. For example, using tag\_a with 10 unique values and tag\_b with 100 independent values could result in up to a 1,000-fold increase in dataset size due to combinatorial growth. Avoid using high-cardinality tags, such as `Name`, especially when working with large datasets based on the Cost and Usage Report (CUR).

**Warning**  
Each tag added to the dashboard increases the cardinality of data and increases the size of aggregated SPICE datasets in Amazon Quick. This architectural decision directly impacts SPICE caching size and performance. We recommend selecting only the minimum necessary tags to satisfy business requirements.

If your Amazon Quick datasets take too long to refresh after configuring the tags, remove all tags (`cid-cmd update --force --recursive -y`) and try re-adding them one by one.

## Merging multiple sources into a single dimension
<a name="add-org-taxonomy-merging-dimensions"></a>

The same business dimension often arrives from more than one source. For example, an `application` value might be set as a resource tag on some resources, as an IAM principal tag on others, and be captured only at the account level for the rest. Filtering and grouping by three separate `application`-like columns is confusing and splits your costs across controls.

Starting with `cid-cmd` version `4.4.17`, you can merge several taxonomy fields into a single dashboard dimension. The merged column takes the **first non-empty value** from your ordered list of sources, giving you one clean field to filter and group by.

The same capability is also a simple way to normalize inconsistent tag keys. When one concept was tagged under different spellings — for example `application` on some resources and `app` on others — merging those keys into one column lets a single filter and Group By cover every resource, regardless of which key was used.

![Merging one business dimension from several sources into a single column](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/taxonomy-merge-concept.svg)


**Note**  
Merging is applied as an Amazon Quick calculated field at the dataset level. It does **not** modify any Athena view, and it does not change the underlying tag or account map columns — they remain available individually. This also means merging adds no data-cardinality cost of its own.

Alternatively, an [AWS Cost Categories](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-cost-categories.html) rule can group several tags into one category upstream of CID; that cost category can then be added to the dashboard like any other taxonomy dimension.

### How the priority works
<a name="how-the-priority-works"></a>

You choose the source fields in priority order: the first field that has a value "wins". Put the most specific or most trusted source first (typically resource tags), then fall back to broader sources (account tags or account map columns).

For example, merging `tag_application`, `iam_principal_tag_Application`, and `account_tag_application` (in that order) produces one column resolved as:

```
application_merged = first non-empty of:
  1. resource tag        tag_application
  2. IAM principal tag   iam_principal_tag_Application
  3. account tag         account_tag_application
```

Both resource-level tag fields and [Account Map](#add-org-taxonomy-account-level-cost-allocation) columns (such as `business_unit` or `cost_center`) can be combined in the same merged column.

### Configure interactively during update
<a name="configure-interactively-during-update"></a>

Merging is offered automatically while you run `cid-cmd update --force --recursive`, right after you select Cost Allocation Tags and Cost Categories:

1. When asked **"Merge some of these columns into single dashboard dimensions?"**, answer **yes**.

1. Select the source fields for one merged column. Choices are grouped by source, and the **selection order sets the priority**.

1. Accept the suggested column name (derived from the common part of the field names, for example `application_merged`) or enter your own.

1. Optionally add more merged columns, then finish.

The merged columns then appear — pre-selected — at the top of the **"Select taxonomy fields to add as dashboard filters and group by fields"** prompt, so they are added to the dashboard when you confirm.

Your merge configuration is remembered between runs (stored alongside the other dashboard parameters), so later `cid-cmd update` runs reuse it and simply ask you to confirm rather than reconfigure from scratch.

#### See the demo: merging taxonomy fields during update
<a name="collapsible-section-id-add-org-taxonomy-merge-demo"></a>

The following recording walks through `cid-cmd update --force --recursive` — selecting cost allocation tags, merging `tag_application`, `iam_principal_tag_Application`, and `account_tag_application` into a single `application_merged` dimension, and adding it to the dashboard as a filter and Group By field.

![Merging taxonomy fields during update](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/cid-update-taxonomy-merge-demo.gif)


## Adding Taxonomy to the Dashboards
<a name="add-account-level-resource-level-taxonomy-dimension"></a>

The CID framework allows you to seamlessly add taxonomy fields to the dashboards including attributes from the [Account Map](#add-org-taxonomy-account-level-cost-allocation) as well as resource-level tags.

Once configured, taxonomy fields are added as Filter Controls across all sheets in the respective dashboard. They can also be used in Calculated Fields and Parameter Controls to support "Group By" aggregations.

To modify the taxonomy fields or update the set of Cost Allocation Tags, run the following commands:

1. Install the tool

   ```
   pip3 install -U cid-cmd
   ```

1. Update a dashboard and all dependency datasets

   ```
   cid-cmd update --force --recursive
   ```

After the update, Amazon Quick datasets are refreshed automatically. During the refresh process you may see a `Dataset changed too much` error, which should disappear once the datasets are fully refreshed.

See more in [update](update-dashboards.md) documentation.

### You can also specify in the command line
<a name="collapsible-section-id-add-org-taxonomy-5"></a>

Following command can be used for deployment if the taxonomy fields are known. Parameters `--taxonomy` and `--resource-tags` are optional. If not provided the tool will discover and propose operator to choose them.

```
cid-cmd update --force --recursive  --resource-tags 'tag_environment' --taxonomy 'company,business_unit,tag_environment'
```

Once dashboard is installed AND all datasets are updated, you can use filters and Group By elements in dashboards.

![Screenshot](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/images/taxonomy-screen.png)


See more details on the live [interactive dashboard demo](https://cid.workshops.aws.dev/demo/?dashboard=cudos&sheet=Taxonomy%20Explorer).
+ You can use top level filters (for Company or Business units from Account Map or Environment Tag).
+ You can use the same taxonomy dimensions as GroupBy fields.

## FAQ
<a name="add-org-taxonomy-faq"></a>

### Do all dashboards support taxonomy?
<a name="do-all-dashboards-support-taxonomy"></a>

The following dashboards support adding organizational taxonomy with `cid-cmd` tool: CID, KPI, CUDOS, FOCUS, Extended Support Cost Projection Dashboard, and Graviton Savings Dashboard. We plan to support this in all CID dashboards in the future.

### I need to append a taxonomy from AWS Organization Tags
<a name="i-need-to-append-a-taxonomy-from-aws-organization-tags"></a>

1. Make sure [CID Data Collection](data-collection.md) is installed.

1. Run `cid-cmd map` and select "organization\_data table" as the data source, then choose "Tags from source table" as a taxonomy dimension source.

1. Run [update](#add-account-level-resource-level-taxonomy-dimension) via command line.

### I just need to add a taxonomy based on AWS Cost Allocation Tag
<a name="i-just-need-to-add-a-taxonomy-based-on-aws-cost-allocation-tag"></a>

Run [update](#add-account-level-resource-level-taxonomy-dimension) via command line. No other actions needed.

### I want to use IAM Principal Tags or User Attributes for cost allocation
<a name="i-want-to-use-iam-principal-tags-or-user-attributes"></a>

1. Ensure your CUR2 data export includes the **Tags** column (update the CID stack on payer account(s) if needed).

1. Run `cid-cmd update --force --recursive`.

1. When prompted to select Cost Allocation Tags, choose the `iam_principal_tag_*` or `user_attribute_tag_*` entries.

### The same dimension (e.g. application) comes from several tags or columns. How do I combine them?
<a name="i-have-the-same-dimension-in-several-tags-or-columns"></a>

Use taxonomy merging to fold them into one dashboard field. When you run `cid-cmd update --force --recursive`, answer **yes** to **"Merge some of these columns into single dashboard dimensions?"** and pick the sources in priority order, or pass `--taxonomy-merges` on the command line. See [Merging multiple sources into a single dimension](#add-org-taxonomy-merging-dimensions).

### After updating and adding tags, the refresh of SPICE datasets times out or shows an error about a resource limitation
<a name="after-update-and-adding-tags-the-refresh-of-spice-datasets-times-out"></a>

Try to [re-update](#add-account-level-resource-level-taxonomy-dimension) using tags with less cardinality (less unique values).

### How to restore the default Account Map?
<a name="how-to-restore-default-account-map"></a>

The default account map view is based on CUR 2.0 data. You can use this query to restore the view to its default state:

#### Default account map query (CUR 2.0)
<a name="collapsible-section-id-add-org-taxonomy-1"></a>

```
CREATE OR REPLACE VIEW account_map AS
SELECT DISTINCT
    line_item_usage_account_id                                        account_id,
    MAX_BY(line_item_usage_account_name, line_item_usage_start_date)  account_name,
    MAX_BY(bill_payer_account_id,        line_item_usage_start_date)  parent_account_id,
    MAX_BY(bill_payer_account_name,      line_item_usage_start_date)  parent_account_name
FROM
    "${cur_database}"."${cur_table_name}"
GROUP BY
    line_item_usage_account_id
```

### How to update Account Map manually?
<a name="how-to-update-account-map-manually"></a>

1. Navigate to Amazon Athena and the cur database (default: `cid_cur`).

1. Locate the `account_map` and click on the vertical ellipses (`⋮`) next to the view and select *Show/edit query* from the context menu.

1. First, make a copy of the view as backup, naming the new view something like *account\_map\_original*.

1. Select the entire view and replace it with this query adjusted to your needs.

1. Click `Run` to execute the query and create/update the view.

1. Run `cid-cmd update --force --recursive` in CloudShell.

### Can I change taxonomy?
<a name="can-i-change-taxonomy"></a>

Yes. Just [re-update](#add-account-level-resource-level-taxonomy-dimension).

### Can CloudFormation Template manage this?
<a name="can-cloudformation-template-manage-this"></a>

As of now you can only use the CID-CMD command line tool to manage taxonomy as it allows choosing values from existing configuration in interactive way.

## Authors
<a name="authors"></a>
+ Yuriy Prykhodko, Principal Technical Account Manager
+ Martin Trost, Senior Technical Account Manager