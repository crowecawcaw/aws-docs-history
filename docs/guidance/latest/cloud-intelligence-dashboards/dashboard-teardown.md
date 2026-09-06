

# Teardown
<a name="dashboard-teardown"></a>

## Teardown of CloudFormation deployment (Automated)
<a name="teardown-of-cloudformation-deployment-automated"></a>

**Note**  
 **Deleting the CloudFormation template means that CUR data will not flow to your destination (data collection) account anymore. However, historical data will be retained in your destination account. To delete the CURs, go to the ${resource-prefix}-${payer-account-id}-shared S3 Bucket and manually delete the account data. Note that if you deployed following best practices with a separate Destination account hosting the dashboards, you should also delete the CID-DataExports-Source Stack in your Management/Payer/Source account.** 

### Click here to use the same CFN templates you used to deploy the dashboards to tear down the environment
<a name="collapsible-section-id-dashboard-teardown-1"></a>

1. Login to the Account(s) where you deployed CloudFormation templates as part of this lab

1. Find your existing CID-related templates and choose Delete.

![Cloudformation stack detail CID-Multipayeraccount with the delete button highlighted](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/teardown.png)


## Manual Teardown
<a name="manual-teardown"></a>

### To perform a teardown manually for this lab, perform the following steps:
<a name="collapsible-section-id-dashboard-teardown-2"></a>

Please follow instructions [here](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/blob/main/CID-CMD.md) to install cid-cmd tool.

You can run the **delete** command and follow instructions in an interactive mode to delete the relevant Dashboard.

```
cid-cmd delete
```