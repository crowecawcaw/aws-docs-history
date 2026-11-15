

# Multi-account enablement script
<a name="securityhub-enable-multiaccount-script"></a>

**Note**  
Instead of this script, we recommend integrating with AWS Organizations and using [declarative policies](accounts-orgs-policies.md) to enable and configure Security Hub CSPM across multiple accounts and Regions.

You can use the [Security Hub CSPM multi-account enablement script in GitHub](https://github.com/awslabs/aws-securityhub-multiaccount-scripts) to enable Security Hub CSPM across accounts and Regions. The script also automates the process of sending invitations to member accounts and enabling AWS Config.

The script automatically enables AWS Config resource recording for all resources, including global resources, in all Regions. It does not limit recording of global resources to a single Region. To conserve costs, we recommend recording global resources in a single Region only. If you use cross-Region aggregation, this Region should be your home Region. For more information, see [Recording resources in AWS Config](securityhub-setup-prereqs.md#config-resource-recording).

There is a corresponding script to disable Security Hub CSPM across accounts and Regions.