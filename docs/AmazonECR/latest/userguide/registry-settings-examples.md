# Private image replication examples for

Amazon ECR

The following examples show common use cases for private image replication. If you
configure replication by using the AWS CLI, you can use the JSON examples as a starting
point when you create your JSON file. If you configure replication by using the
AWS Management Console, you will see similar JSON when you review your replication rule on the
**Review and submit** page.

## Example: Configuring

cross-Region replication to a single destination Region

The following shows an example for configuring cross-Region replication within a
single registry. This example assumes that your account ID is
`111122223333` and that you're specifying this replication
configuration in a Region other than `us-west-2`.

```
{
    "rules": [
        {
            "destinations": [
                {
                    "region": "`us-west-2`",
                    "registryId": "`111122223333`"
                }
            ]
        }
    ]
}
```

## Example: Configuring

cross-Region replication using a repository filter

The following shows an example for configuring cross-Region replication for
repositories that match a prefix name value. This example assumes your account ID is
`111122223333` and that you're specifying this replication
configuration in a Region other than `us-west-1` and have repositories
with a prefix of `prod`.

```
{
	"rules": [{
		"destinations": [{
			"region": "`us-west-1`",
			"registryId": "`111122223333`"
		}],
		"repositoryFilters": [{
			"filter": "`prod`",
			"filterType": "PREFIX_MATCH"
		}]
	}]
}
```

## Example:

Configuring cross-Region replication to multiple destination Regions

The following shows an example for configuring cross-Region replication within a
single registry. This example assumes your account ID is
`111122223333` and that you're specifying this replication
configuration in a Region other than `us-west-1` or
`us-west-2`.

```
{
    "rules": [
        {
            "destinations": [
                {
                    "region": "`us-west-1`",
                    "registryId": "`111122223333`"
                },
                {
                    "region": "`us-west-2`",
                    "registryId": "`111122223333`"
                }
            ]
        }
    ]
}
```

## Example: Configuring

cross-account replication

The following shows an example for configuring cross-account replication for your
registry. This example configures replication to the
`444455556666` account and to the `us-west-2`
Region.

###### Important

For cross-account replication to occur, the destination account must configure
a registry permissions policy to allow replication to occur. For more
information, see [Private registry permissions in Amazon ECR](registry-permissions.md "registry-permissions.md").

```
{
    "rules": [
        {
            "destinations": [
                {
                    "region": "`us-west-2`",
                    "registryId": "`444455556666`"
                }
            ]
        }
    ]
}
```

## Example: Specifying

multiple rules in a configuration

The following shows an example for configuring multiple replication rules for your
registry. This example configures replication for the
`111122223333` account with one rule that
replicates repositories with a prefix of `prod` to the
`us-west-2` Region and repositories with a prefix of
`test` to the `us-east-2` Region. A replication
configuration may contain up to 10 rules, with each rule specifying up to 25
destinations.

```
{
	"rules": [{
			"destinations": [{
				"region": "`us-west-2`",
				"registryId": "`111122223333`"
			}],
			"repositoryFilters": [{
				"filter": "`prod`",
				"filterType": "PREFIX_MATCH"
			}]
		},
		{
			"destinations": [{
				"region": "`us-east-2`",
				"registryId": "`111122223333`"
			}],
			"repositoryFilters": [{
				"filter": "`test`",
				"filterType": "PREFIX_MATCH"
			}]
		}
	]
}
```

## Example: Removing all

replication settings

The following shows an example for removing all replication settings from your
registry. To remove replication settings, you must configure an empty rules
array.

```
{
    "rules": []
}
```

###### Important

Removing replication settings does not delete any previously replicated
repositories or images. You must manually delete replicated content if it is no
longer needed.
