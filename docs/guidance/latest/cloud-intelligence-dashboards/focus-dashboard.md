# FOCUS Dashboard

[The FinOps Cost and Usage Specification](https://focus.finops.org/ "https://focus.finops.org/")
(FOCUS) is an open-source specification that defines clear requirements
for cloud vendors to produce consistent cost and usage datasets.

Supported by the FinOps Foundation, FOCUS aims to reduce complexity for
FinOps Practitioners so they can drive data-driven decision-making and
maximize the business value of cloud, while making their skills more
transferable across clouds, tools, and organizations.

The CID FOCUS Dashboard is an open-source and customizable dashboard that
provides pre-defined visuals to get actionable insights from FOCUS data
in Amazon QuickSight. It allows you to quickly get started with using
FOCUS in your organization. The FOCUS Dashboard provides the following
features:

- **Consolidated view** of FOCUS data from multiple dimensions across your entire organization
- Support for consolidation of **multiple FOCUS specification versions** from different cloud providers
- Month-over-month trends with the ability to drill down from high-level visibility into resource-level details in a few clicks
- Support of organizational taxonomy from tags
- Effective discount rate calculations

## High Level Architecture

![Architecture High Level](images/images/architecture/focus-high-level.png)

1. AWS Data Exports service provides FOCUS data (currently supporting FOCUS 1.2 for AWS). Use the CID [Data Exports](data-exports.md "data-exports.md") stack to activate it in your Management (Payer) Account and automatically configure the replication to a Data Collection Account.
2. Install [CID FOCUS Dashboard](#focus-dashboard-deployment "#focus-dashboard-deployment") that leverages FOCUS data and provides a dynamically generated consolidated view in Amazon Athena. This view can be extended once you add FOCUS data from other providers.
3. Install the FOCUS data collection stack(s) that collect data from other providers. Currently we provide integrations to collect FOCUS data from [Microsoft Azure](https://catalog.workshops.aws/cidforazure/en-US/03-setup "https://catalog.workshops.aws/cidforazure/en-US/03-setup"), [Google Cloud Platform](https://catalog.workshops.aws/cid-gcp-cost-dashboard/en-US/02-solution-design "https://catalog.workshops.aws/cid-gcp-cost-dashboard/en-US/02-solution-design"), and [Oracle Cloud Infrastructure](https://github.com/awslabs/cid-oci-cost-dashboard/ "https://github.com/awslabs/cid-oci-cost-dashboard/"). [Learn more](#focus-dashboard-add-focus-data-from-other-cloud-providers "#focus-dashboard-add-focus-data-from-other-cloud-providers") about integration of FOCUS data. Typically these stacks leverage scheduled AWS Lambda or AWS Glue Jobs and retrieve data via APIs using credentials stored in AWS Secrets Manager. The data is encrypted with custom KMS keys to protect sensitive billing information from unauthorized access.
4. Update the focus_consolidation_view in Athena to include tables with FOCUS data from other cloud providers.
5. You can also export cost data from on-premises datacenters or SaaS providers in the same format and integrate them in a similar way.

## Demo Dashboard

Get more familiar with the dashboard using the live, interactive demo
dashboard following this
[link](https://cid.workshops.aws.dev/demo?dashboard=focus-dashboard&sheet=default "https://cid.workshops.aws.dev/demo?dashboard=focus-dashboard&sheet=default").

Explore key FOCUS Dashboard capabilities in the [interactive presentation](https://app.storylane.io/share/zutqlizt5v45 "https://app.storylane.io/share/zutqlizt5v45").

![FOCUS Dashboard Screenshot](images/focus_dashboard.png)

## Prerequisites

Before installing the FOCUS Dashboard, you need to enable FOCUS Data
Export and consolidate it from your Management (Payer) Accounts in the Data
Collection Account.

![High Level Focus Export From AWS](images/images/architecture/focus-aws.png)

1. Create a FOCUS Data Export following the steps in the [Data Export](data-exports.md "data-exports.md") page and return to this page
   once completed.

The Data Export prerequisites support FOCUS 1.2 for AWS. If you are migrating from FOCUS 1.0, see [Migration to AWS FOCUS 1.2](migration-to-focus-1-2.md "migration-to-focus-1-2.md").

## Deployment

###### Example

CloudFormation

###### Note

**Prerequisite**: To install this dashboard using CloudFormation, you need to install Foundational Dashboards CFN with version v4.0.0 or above as described [here](deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard "deployment-in-global-regions.md#deployment-in-global-region-deploy-dashboard").

1. Log in to your **Data Collection** Account.
2. Click the Launch Stack button below to open the **pre-populated stack template** in your CloudFormation console.

[![Launch Stack button](images/LaunchStack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=FOCUS-Dashboard&param_DashboardId=focus-dashboard&param_RequiresDataExports=yes "https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/cid-plugin.yml&stackName=FOCUS-Dashboard¶m_DashboardId=focus-dashboard¶m_RequiresDataExports=yes") 3. You can change the **Stack name** if you wish. 4. Leave **Parameters** values as they are. 5. Review the configuration and click **Create stack**. 6. The stack will start in **CREATE_IN_PROGRESS**. Once complete, the stack will show **CREATE_COMPLETE**. 7. You can check the stack output for dashboard URLs.

###### Note

**Troubleshooting:** If you see the error "No export named cid-CidExecArn found" during stack deployment, make sure you have completed the prerequisite steps.

Command Line
An alternative method to install dashboards is the [cid-cmd](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd") tool.

1. Log in to your **Data Collection** Account.
2. Open a command-line interface with permissions to run API requests in your AWS account. We recommend using [CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell").
3. In your command-line interface, run the following command to download and install the CID CLI tool:

```
pip3 install --upgrade cid-cmd
```

If using [CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell"), install Python 3.11 first:

```
sudo yum install python3.11-pip -y
python3.11 -m pip install -U cid-cmd
```

4. Run the following command to deploy the dashboard:

```
cid-cmd deploy --dashboard-id focus-dashboard
```

Follow the instructions from the deployment wizard. More info about command-line options is available in the
[Readme](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd "https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md#command-line-tool-cid-cmd")
or via `cid-cmd --help`.

Data Exports can take up to 24-48 hours to deliver the first reports. If you just installed Data Exports, the dashboard will most likely be empty. Please allow up to 24 hours for data to arrive.

## Add FOCUS Data from Other Cloud Providers

The FOCUS Dashboard supports consolidation of FOCUS data from multiple FOCUS specification versions, allowing you to combine data from different cloud providers regardless of the FOCUS version they export.

After deploying each cloud provider integration, run the `cid-cmd update` command as described in [common update steps](#focus-dashboard-update-consolidation-view "#focus-dashboard-update-consolidation-view") to detect available FOCUS tables and select which ones to include in the consolidated view to be presented on FOCUS Dashboard.

### Microsoft Azure

![High Level Focus Export From Microsoft Azure](images/images/architecture/focus-azure.png)

1. Deploy the [FOCUS Dashboard](#focus-dashboard-deployment "#focus-dashboard-deployment").
2. Deploy the [Cloud
   Intelligence Dashboard for Azure workshop](https://catalog.workshops.aws/cidforazure/en-US/03-setup "https://catalog.workshops.aws/cidforazure/en-US/03-setup"), choosing FOCUS in
   [Export
   Type](https://catalog.workshops.aws/cidforazure/en-US/03_Setup/05_Parameters/#export-type "https://catalog.workshops.aws/cidforazure/en-US/03_Setup/05_Parameters/#export-type").
3. Follow the [common update steps](#focus-dashboard-update-consolidation-view "#focus-dashboard-update-consolidation-view") below.

### Google Cloud Platform (GCP)

![High Level Focus Export From GCP](images/images/architecture/focus-gcp.png)

1. Deploy the [FOCUS Dashboard](#focus-dashboard-deployment "#focus-dashboard-deployment").
2. Deploy the [GCP](https://catalog.workshops.aws/cid-gcp-cost-dashboard/en-US/02-solution-design "https://catalog.workshops.aws/cid-gcp-cost-dashboard/en-US/02-solution-design") workshop.
3. Follow the [common update steps](#focus-dashboard-update-consolidation-view "#focus-dashboard-update-consolidation-view") below.

### Oracle Cloud Infrastructure (OCI)

![High Level Focus Export From OCI](images/images/architecture/focus-oci.png)

1. Deploy the [FOCUS Dashboard](#focus-dashboard-deployment "#focus-dashboard-deployment").
2. Deploy the [OCI](https://catalog.workshops.aws/cidforoci/en-US/ "https://catalog.workshops.aws/cidforoci/en-US/") workshop.
3. Follow the [common update steps](#focus-dashboard-update-consolidation-view "#focus-dashboard-update-consolidation-view") below.

### Common Update Steps

After deploying any cloud provider integration above, update the FOCUS Dashboard and consolidation view:

1. Log in to your **Data Collection** Account.
2. Open a command-line interface with permissions to run API requests in your AWS account. We recommend using [CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell").
3. Run the following commands:

```
pip3 install --upgrade cid-cmd
cid-cmd update --recursive --force --dashboard-id focus-dashboard
```

If using [CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell"), replace the first line with:

```
sudo yum install python3.11-pip -y
python3.11 -m pip install -U cid-cmd
```

4. Select the FOCUS tables you would like to include in the consolidated view when prompted.

![Selecting FOCUS tables for consolidation](/images/guidance/latest/cloud-intelligence-dashboards/images/focus_update.gif)

## Update

Dashboards are not updated with an update of the CloudFormation stack. There are two update options depending on your needs:

### Dashboard Update

When a new version of the dashboard template is released, update your dashboard by running:

```
pip3 install --upgrade cid-cmd
cid-cmd update --dashboard-id focus-dashboard
```

If using [CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell"), replace the first line with:

```
sudo yum install python3.11-pip -y
python3.11 -m pip install -U cid-cmd
```

This updates the dashboard visuals to the latest template version.

### Dashboard and Data Schema Update

To add new FOCUS tables from other cloud providers, include new tags, or update the consolidation view schema, run:

```
pip3 install --upgrade cid-cmd
cid-cmd update --recursive --force --dashboard-id focus-dashboard
```

If using [CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell"), replace the first line with:

```
sudo yum install python3.11-pip -y
python3.11 -m pip install -U cid-cmd
```

This updates the dashboard, datasets and all dependent Athena views. You will be prompted to select which FOCUS tables to include in the consolidated view.

## Authors

- Yuriy Prykhodko, Principal Technical Account Manager
- Iakov Gan, Ex-Amazonian
- Zach Erdman, Senior Product Manager
- Mo Mohoboob, Senior Specialist SA
- Marco De Bianchi, Sr. Delivery Consultant
- Soham Majumder, Technical Account Manager

## Contributors

- Petro Kashlikov, Senior Solutions Architect

## Feedback & Support

Follow [Feedback & Support](feedback-support.md "feedback-support.md") guide

## FAQ

### Can we replace CUR/CUDOS dashboard with FOCUS?

The FOCUS format does not currently include important information like [lineItem/Operation](../../../cur/latest/userguide/Lineitem-columns.md#Lineitem-details-O "../../../cur/latest/userguide/Lineitem-columns.md#Lineitem-details-O") that is critical for FinOps use cases. Until the FOCUS specification is extended to support this, we cannot recommend FOCUS for Cost Optimization scenarios. Nevertheless, FOCUS can be useful for a wide range of high-level reporting use cases.

### How can we add another FOCUS provider?

Feel free to contribute data export mechanisms for other FOCUS providers. We will be happy to review and reference them.

### Does the dashboard support multiple FOCUS versions?

Yes. The FOCUS Dashboard supports consolidation of multiple FOCUS specification versions. You can combine data from providers exporting different FOCUS versions (for example, FOCUS 1.0 and FOCUS 1.2) in the same consolidated view.

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
