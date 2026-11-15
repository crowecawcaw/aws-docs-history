

# Upgrading a domain (SDK)
<a name="starting-upgrades-sdk"></a>

This sample uses the [OpenSearchService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html) low-level Python client from the AWS SDK for Python (Boto) to check if a domain is eligible for upgrade to a specific version, upgrades it, and continuously checks the upgrade status.

The first sample upgrades a domain in place. The second sample runs a clone-based upgrade.

## In-place upgrade
<a name="sdk-in-place"></a>

```
import boto3
from botocore.config import Config
import time

# Build the client using the default credential configuration.
# You can use the CLI and run 'aws configure' to set access key, secret
# key, and default Region.

DOMAIN_NAME = ''  # The name of the domain to upgrade
TARGET_VERSION = ''  # The version you want to upgrade the domain to. For example, OpenSearch_1.1

my_config = Config(
    # Optionally lets you specify a Region other than your default.
    region_name='us-east-1'
)
client = boto3.client('opensearch', config=my_config)


def check_versions():
    """Determine whether domain is eligible for upgrade"""
    response = client.get_compatible_versions(
        DomainName=DOMAIN_NAME
    )
    compatible_versions = response['CompatibleVersions']
    for i in range(len(compatible_versions)):
        if TARGET_VERSION in compatible_versions[i]["TargetVersions"]:
            print('Domain is eligible for upgrade to ' + TARGET_VERSION)
            upgrade_domain()
            print(response)
        else:
            print('Domain not eligible for upgrade to ' + TARGET_VERSION)


def upgrade_domain():
    """Upgrades the domain"""
    response = client.upgrade_domain(
        DomainName=DOMAIN_NAME,
        TargetVersion=TARGET_VERSION
    )
    print('Upgrading domain to ' + TARGET_VERSION + '...' + response)
    time.sleep(5)
    wait_for_upgrade()


def wait_for_upgrade():
    """Get the status of the upgrade"""
    response = client.get_upgrade_status(
        DomainName=DOMAIN_NAME
    )
    if (response['UpgradeStep']) == 'UPGRADE' and (response['StepStatus']) == 'SUCCEEDED':
        print('Domain successfully upgraded to ' + TARGET_VERSION)
    elif (response['StepStatus']) == 'FAILED':
        print('Upgrade failed. Please try again.')
    elif (response['StepStatus']) == 'SUCCEEDED_WITH_ISSUES':
        print('Upgrade succeeded with issues')
    elif (response['StepStatus']) == 'IN_PROGRESS':
        time.sleep(30)
        wait_for_upgrade()


def main():
    check_versions()


if __name__ == "__main__":
    main()
```

## Clone-based upgrade
<a name="sdk-clone-based"></a>

This sample starts a clone-based upgrade, waits for the cloned cluster to be ready, sends 10 percent of read traffic to the cloned cluster, and then cuts over or cancels. For information about each step, see [Validating, cutting over, and rolling back during a clone-based upgrade](clone-based-upgrade.md).

```
import boto3
import time

DOMAIN_NAME = ''  # The name of the domain to upgrade
TARGET_VERSION = ''  # The version to upgrade to. For example, OpenSearch_3.1
RETENTION_HOURS = 48  # How long to keep the primary cluster after cutover (maximum 336). Optional.

client = boto3.client('opensearch', region_name='us-east-1')


def start_upgrade():
    """Starts a clone-based upgrade and returns the change ID"""
    response = client.upgrade_domain(
        DomainName=DOMAIN_NAME,
        TargetVersion=TARGET_VERSION,
        DeploymentStrategyOptions={
            'DeploymentStrategy': 'ClonedBlueGreen',
            'ClonedBlueGreenOptions': {
                'RetentionOptions': {'RetentionInHours': RETENTION_HOURS}
            }
        }
    )
    return response['ChangeProgressDetails']['ChangeId']


def wait_for_cloned_cluster(change_id):
    """Waits until the cloned cluster is ready for validation"""
    while True:
        progress = client.describe_domain_change_progress(
            DomainName=DOMAIN_NAME,
            ChangeId=change_id
        )['ChangeProgressStatus']
        if progress['ConfigChangeStatus'] == 'PendingUserInput':
            print('The cloned cluster is ready for validation')
            return
        if progress['Status'] in ('COMPLETED', 'FAILED'):
            raise RuntimeError('Upgrade ended with status ' + progress['Status'])
        time.sleep(60)


def shift_read_traffic(percent):
    """Sends a share of read requests to the cloned cluster"""
    client.update_clone(
        DomainName=DOMAIN_NAME,
        TrafficSplitOptions={
            'Strategy': 'ShiftReadTrafficPercent',
            'CloneReadTrafficPercent': percent
        }
    )


def cut_over():
    """Cuts over to the cloned cluster"""
    client.update_clone(
        DomainName=DOMAIN_NAME,
        CutoverOptions={'Target': 'ClonedCluster'}
    )


def cancel():
    """Cancels the upgrade before cutover and deletes the cloned cluster"""
    client.update_clone(
        DomainName=DOMAIN_NAME,
        CutoverOptions={'Target': 'PrimaryCluster'}
    )


def main():
    change_id = start_upgrade()
    wait_for_cloned_cluster(change_id)
    shift_read_traffic(10)
    if input('Validate the cloned cluster, then type "cutover" to continue: ') == 'cutover':
        cut_over()
    else:
        cancel()


if __name__ == "__main__":
    main()
```