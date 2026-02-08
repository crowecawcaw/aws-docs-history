# Compute Optimizer Dashboard

## Introduction

AWS Compute Optimizer recommends optimal AWS resources for your
workloads to reduce costs and improve performance by using machine
learning to analyze historical utilization metrics. Compute Optimizer
Dashboard lets you view cost optimization and risk reduction
opportunities for all accounts in your AWS Organizations across all AWS
Regions. Out-of-the-box benefits of the COD include (but are not limited
to):

- Find over and underutilized resources (EC2, AutoScaling Groups, EBS,
  Lambda).
- Get right-sizing recommendations.
- Identify potential savings across all payer accounts and regions.
- Track optimization progress over time by AWS Account team or business
  unit.

## Architecture

![architecture](images/images/architecture/compute-optimizer-architecture.png)

1. AWS Compute Optimizer Collects the data about running instances and uses Machine Learning to generate recommendations
2. CID Data Collection has a Lambda functions that on schedule assume a role in Management account(s) to trigger an export of AWS Compute Optimizer in each region configured in data collection stack. By default it i scheduled for every 14 days, but it can be changed in the parameters of the Data Collection Stack.
3. The AWS Compute Optimizer exports data to regional buckets.
4. The replication mechanisms consolidates all data from regional buckets to one data bucket. All exports on regional bucket will be deleted after 1 day as per lifecycle policy.
5. Quick Sight Dataset refreshes daily to show the latest state on the dashboard.

## Learn more

- [3 New Features on the
  Compute Optimizer Dashboard](https://www.youtube.com/watch?v=IP_k2OXHPoo "https://www.youtube.com/watch?v=IP_k2OXHPoo")

See also:

- A basics of Compute Optimizer Right Sizing in a
  [lab
  200 Rightsizing with Compute Optimizer](https://wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/ "https://wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/")
- [AWS Compute Optimizer
  FAQ](https://aws.amazon.com/compute-optimizer/faqs/ "https://aws.amazon.com/compute-optimizer/faqs/")

## Demo Dashboard

Get more familiar with Dashboard using the live, interactive demo
dashboard following this
[link](https://cid.workshops.aws.dev/demo?dashboard=compute-optimizer-dashboard "https://cid.workshops.aws.dev/demo?dashboard=compute-optimizer-dashboard")

![Image of a compute optimizer dashboard in Quick Sight](images/co_demo.png)

## Prerequisites

1. To get right sizing recommendations you need to
   [Enroll
   all accounts to Compute Optimizer](../../../compute-optimizer/latest/ug/getting-started.md#account-opt-in "../../../compute-optimizer/latest/ug/getting-started.md#account-opt-in"). You can use free version that
   provides recommendations based on 14 days of look-back period.
2. Deploy or update [Data Collection Lab](data-collection.md "data-collection.md") and make
   sure AWS Compute Optimizer Data Collection Module is enabled.
3. Ensure you have [Compute Optimizer enabled at Organization level](../../../organizations/latest/userguide/services-that-can-integrate-compute-optimizer.md "../../../organizations/latest/userguide/services-that-can-integrate-compute-optimizer.md").

## Deployment

CloudFormation
If you already have CUDOS, Cost Intelligence Dashboard or KPI Dashboard
installed via CloudFormation as described
[here](deployment-in-global-regions.md "deployment-in-global-regions.md"), you can update
the Stack by setting DeployComputeOptimizerDashboard to "yes" and
updating the path of Data Collection S3 bucket (if different from
default).

If you do not have the stack installed, you can install using the
instructions [here](deployment-in-global-regions.md "deployment-in-global-regions.md")
(you can ignore the Cost and Usage report part as it is not required for
this dashboard).

Command Line
Alternative method to install dashboards is the
[cid-cmd](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd")
tool.

1. Log in to to your **Data Collection** Account.
2. Open up a command-line interface with permissions to run API requests
   in your AWS account. We recommend to use
   [CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell").
3. In your command-line interface run the following command to download
   and install the CID CLI tool:

```
pip3 install --upgrade cid-cmd
```

4. In your command-line interface run the following command to deploy the
   dashboard:

```
cid-cmd deploy --dashboard-id compute-optimizer-dashboard
```

Please follow the instructions from the deployment wizard. More info
about command line options are in the
[Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd")
or `cid-cmd --help`. 5. You can provide also additional tag names. This dashboard supports 2
tags: Primary and Secondary. Tags are the "key" part of the
Resource Tag. Please note that Tags here are case sensitive and they not
AWS Cost Allocation Tags.

Recommendation: You can use one Tag to define ownership of resource and
another tag to define if this particular resource is eligible for
RightSizing (default) or must be excluded for valid reason (DRP, Vendor
Compliance, Test, or any other reason for resource to be
over-provisioned).If your are not using tags, leave defaults.

Tags that are using a dash as separator (`-`) are not supported by
default. If you have this kind of tags you might need additional
customization of a dataset compute_optimizer_all_options. For example in
`primary_tag` field you can use
`parseJson(replace(tags, '-', '_'),'$.My_Tag')`

You can also define these tags later and apply to dashboard using
`cid-cmd update --force --recursive`

## Update

Please note that dashboards are not updated with update of
CloudFormation Stack. When new version of the dashboard template is
released, you can update your dashboard by running the following command
in your command-line interface:

```
cid-cmd update --dashboard-id compute-optimizer-dashboard
```

## OPTIONAL STEPS

**Manage Business Units Map**

For managing Business Units please modify business_units_map view. You
can update view definition providing your values, or you can create an
csv file upload to s3, create a table and set business_units_map view to
select from this table.

```
CREATE OR REPLACE VIEW business_units_map AS
SELECT *
FROM
    (
    VALUES
        ROW ('`111111111`', '`account1`', '`Business Unit 1`')
        , ROW ('`222222222`','`account2`', '`Business Unit 2`')
    ) ignored_table_name (account_id, account_name, bu)
```

Also you can use business_units_map view as a
proxy to other data sources.

In case if you do not need Business Units functionality and you have
CUDOS dashboard installed with account_map, you can use this view to
SELECT from account_map.

```
CREATE OR REPLACE VIEW business_units_map AS
SELECT
    account_id as account_id,
    account_name as account_name,
    '`Undefined`' as bu
FROM account_map
```

## Authors

- Iakov Gan, Ex-Amazonian
- Yuriy Prykhodko, Principal Technical Account Manager
- Voicu Chirtes, Senior Technical Account Manager
- Timur Tulyaganov, Ex-Amazonian

## Feedback & Support

Follow [Feedback & Support](feedback-support.md "feedback-support.md") guide

###### Note

These dashboards and their content: (a) are for informational
purposes only, (b) represent current AWS product offerings and
practices, which are subject to change without notice, and (c) does not
create any commitments or assurances from AWS and its affiliates,
suppliers or licensors. AWS content, products or services are provided
"as is" without warranties, representations, or conditions of any
kind, whether express or implied. The responsibilities and liabilities
of AWS to its customers are controlled by AWS agreements, and this
document is not part of, nor does it modify, any agreement between AWS
and its customers.
