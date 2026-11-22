

# Upgrading a domain (CLI)

You can use the following operations to identify the correct version of OpenSearch or Elasticsearch for your domain, start an in-place or clone-based upgrade, perform the pre-upgrade check, and view progress:
+ `get-compatible-versions` (`GetCompatibleVersions`)
+ `upgrade-domain` (`UpgradeDomain`)
+ `get-upgrade-status` (`GetUpgradeStatus`)
+ `get-upgrade-history` (`GetUpgradeHistory`)
+ `describe-domain-change-progress` (`DescribeDomainChangeProgress`) – Monitors a clone-based upgrade.
+ `update-clone` (`UpdateClone`) – Shifts read traffic to the cloned cluster, cuts over, cancels, and manages the retention period for a clone-based upgrade.

## In-place upgrade
<a name="cli-in-place"></a>

To check whether your domain is eligible without starting an upgrade, use the `--perform-check-only` option:

```sh
aws opensearch upgrade-domain \
  --domain-name my-domain \
  --target-version OpenSearch_2.19 \
  --perform-check-only
```

To start the upgrade, run the same command without `--perform-check-only`:

```sh
aws opensearch upgrade-domain \
  --domain-name my-domain \
  --target-version OpenSearch_2.19
```

To view progress, use `get-upgrade-status`:

```sh
aws opensearch get-upgrade-status --domain-name my-domain
```

## Clone-based upgrade
<a name="cli-clone-based"></a>

A clone-based upgrade has more steps than an in-place upgrade. For information about each step, see [Validating, cutting over, and rolling back during a clone-based upgrade](clone-based-upgrade.md).

### Start the upgrade
<a name="cli-clone-start"></a>

To start a clone-based upgrade, run `upgrade-domain` with `DeploymentStrategy` set to `ClonedBlueGreen` in `--deployment-strategy-options`. The retention period is optional. The maximum is 336 hours (14 days). To request a longer period, contact [AWS Support](https://aws.amazon.com/premiumsupport/).

```sh
aws opensearch upgrade-domain \
  --domain-name my-domain \
  --target-version OpenSearch_3.1 \
  --deployment-strategy-options 'DeploymentStrategy=ClonedBlueGreen,ClonedBlueGreenOptions={RetentionOptions={RetentionInHours=48}}'
```

The response includes a `ChangeId`. Use it to monitor the upgrade:

```sh
aws opensearch describe-domain-change-progress \
  --domain-name my-domain \
  --change-id 9f1c2b7a-4d3e-4e21-9a5f-0c8b7d6e5f40
```

When the `ConfigChangeStatus` is `PendingUserInput`, the cloned cluster is ready for you to validate.

### Shift read traffic to the cloned cluster
<a name="cli-clone-traffic"></a>

`CloneReadTrafficPercent` is the share of read requests that go to the cloned cluster, from 0 to 100. Writes always go to the primary cluster.

```sh
aws opensearch update-clone \
  --domain-name my-domain \
  --traffic-split-options Strategy=ShiftReadTrafficPercent,CloneReadTrafficPercent=10
```

### Cut over to the cloned cluster
<a name="cli-clone-cutover"></a>

Set `Target` to `ClonedCluster`.

```sh
aws opensearch update-clone \
  --domain-name my-domain \
  --cutover-options Target=ClonedCluster
```

### Cancel the upgrade before cutover
<a name="cli-clone-cancel"></a>

Set `Target` to `PrimaryCluster`. OpenSearch Service deletes the cloned cluster, and your domain stays as it was.

```sh
aws opensearch update-clone \
  --domain-name my-domain \
  --cutover-options Target=PrimaryCluster
```

### Set or change the retention period
<a name="cli-clone-retention"></a>

You can set or change the retention period before or after cutover.

```sh
aws opensearch update-clone \
  --domain-name my-domain \
  --retention-options RetentionInHours=24
```

### End the retention period early
<a name="cli-clone-end-retention"></a>

After cutover, you can roll back to the primary cluster, or delete the primary cluster now.

```sh
aws opensearch update-clone \
  --domain-name my-domain \
  --retention-options '{"RetentionAction":"RollbackToPrimaryCluster"}'
```

```sh
aws opensearch update-clone \
  --domain-name my-domain \
  --retention-options '{"RetentionAction":"DeletePrimaryCluster"}'
```

For more information, see the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html) and [Amazon OpenSearch Service API Reference](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html).