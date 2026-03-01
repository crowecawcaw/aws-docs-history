# Examples of lifecycle policies in Amazon ECR

The following are example lifecycle policies showing the syntax.

To see more information about policy properties, see [Lifecycle policy properties in Amazon ECR](lifecycle_policy_parameters.md "lifecycle_policy_parameters.md").
For instructions about creating a lifecycle policy by using the AWS CLI, see [To create a lifecycle policy (AWS CLI)](lp_creation.md#lp-creation-cli "lp_creation.md#lp-creation-cli").

## Lifecycle policy template

The contents of your lifecycle policy are evaluated before being associated with a
repository. The following is the JSON syntax template for the lifecycle
policy.

```
{
        "rules": [
            {
                "rulePriority": `integer`,
                "description": "`string`",
                "selection": {
                    "tagStatus": "`tagged`"|"`untagged`"|"`any`",
                    "tagPatternList": `list<string>`,
                    "tagPrefixList": `list<string>`,
                    "storageClass": "`standard`"|"`archive`",
                    "countType": "`imageCountMoreThan`"|"`sinceImagePushed`"|"`sinceImagePulled`"|"`sinceImageTransitioned`",
                    "countUnit": "`string`",
                    "countNumber": `integer`
                },
                "action": {
                    "type": "`expire`"|"`transition`",
                    "targetStorageClass": "`archive`"
                }
            }
        ]
    }
```

## Filtering on image age

The following example shows the lifecycle policy syntax for a policy that expires
images with a tag starting with `prod` by using a
`tagPatternList` of `prod*` that are also older than
`14` days.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Expire images older than 14 days",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 14
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

## Filtering on last pulled time

The following example shows the lifecycle policy syntax for a policy that
transitions images to archive storage that haven't been pulled in `90`
days.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive images not pulled in 90 days",
            "selection": {
                "tagStatus": "any",
                "countType": "sinceImagePulled",
                "countUnit": "days",
                "countNumber": 90
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        }
    ]
}
```

###### Important

The `sinceImagePulled` count type must be used with the
`transition` action. It cannot be used with the
`expire` action. To delete images based on pull activity, first
transition them to archive storage using `sinceImagePulled`, then
use `sinceImageTransitioned` with an `expire` action to
delete them. Images must be in archive storage for a minimum of 90 days before
deletion.

## Filtering on archive transition time

The following example shows the lifecycle policy syntax for a policy that expires
archived images that have been in archive storage for more than `365`
days.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Expire images archived for more than 365 days",
            "selection": {
                "tagStatus": "any",
                "storageClass": "archive",
                "countType": "sinceImageTransitioned",
                "countUnit": "days",
                "countNumber": 365
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

###### Important

The `sinceImageTransitioned` count type must be used with the
`expire` action and the `archive` storage class.
Images must be in archive storage for a minimum of 90 days before
deletion.

## Filtering on image count

The following example shows the lifecycle policy syntax for a policy that keeps
only one untagged image and expires all others.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Keep only one untagged image, expire all others",
            "selection": {
                "tagStatus": "untagged",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

## Filtering on multiple rules

The following examples use multiple rules in a lifecycle policy. An example
repository and lifecycle policy are given along with an explanation of the
outcome.

### Example A

Repository contents:

- Image A, Taglist: ["beta-1", "prod-1"], Pushed: 10 days ago
- Image B, Taglist: ["beta-2", "prod-2"], Pushed: 9 days ago
- Image C, Taglist: ["beta-3"], Pushed: 8 days ago

Lifecycle policy text:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 2,
            "description": "Rule 2",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["beta*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:

- Rule 1 identifies images tagged with prefix `prod`. It
  should mark images, starting with the oldest, until there is one or
  fewer images remaining that match. It marks Image A for
  expiration.
- Rule 2 identifies images tagged with prefix `beta`. It
  should mark images, starting with the oldest, until there is one or
  fewer images remaining that match. It marks both Image A and Image B for
  expiration. However, Image A has already been seen by Rule 1 and if
  Image B were expired it would violate Rule 1 and thus is skipped.
- Result: Image A is expired.

### Example B

This is the same repository as the previous example but the rule priority
order is changed to illustrate the outcome.

Repository contents:

- Image A, Taglist: ["beta-1", "prod-1"], Pushed: 10 days ago
- Image B, Taglist: ["beta-2", "prod-2"], Pushed: 9 days ago
- Image C, Taglist: ["beta-3"], Pushed: 8 days ago

Lifecycle policy text:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["beta*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 2,
            "description": "Rule 2",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:

- Rule 1 identifies images tagged with prefix `beta`. It
  should mark images, starting with the oldest, until there is one or
  fewer images remaining that match. It sees all three images and would
  mark Image A and Image B for expiration.
- Rule 2 identifies images tagged with prefix `prod`. It
  should mark images, starting with the oldest, until there is one or
  fewer images remaining that match. It would see no images because all
  available images were already seen by Rule 1 and thus would mark no
  additional images.
- Result: Images A and B are expired.

## Filtering on multiple tags in a single rule

The following examples specify the lifecycle policy syntax for multiple tag
patterns in a single rule. An example repository and lifecycle policy are given
along with an explanation of the outcome.

### Example A

When multiple tag patterns are specified on a single rule, images must match
all listed tag patterns.

Repository contents:

- Image A, Taglist: ["alpha-1"], Pushed: 12 days ago
- Image B, Taglist: ["beta-1"], Pushed: 11 days ago
- Image C, Taglist: ["alpha-2", "beta-2"], Pushed: 10 days ago
- Image D, Taglist: ["alpha-3"], Pushed: 4 days ago
- Image E, Taglist: ["beta-3"], Pushed: 3 days ago
- Image F, Taglist: ["alpha-4", "beta-4"], Pushed: 2 days ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["alpha*", "beta*"],
                "countType": "sinceImagePushed",
                "countNumber": 5,
                "countUnit": "days"
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:

- Rule 1 identifies images tagged with prefix `alpha` and
  `beta`. It sees images C and F. It should mark images
  that are older than five days, which would be Image C.
- Result: Image C is expired.

### Example B

The following example illustrates that tags are not exclusive.

Repository contents:

- Image A, Taglist: ["alpha-1", "beta-1", "gamma-1"], Pushed: 10 days
  ago
- Image B, Taglist: ["alpha-2", "beta-2"], Pushed: 9 days ago
- Image C, Taglist: ["alpha-3", "beta-3", "gamma-2"], Pushed: 8 days
  ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["alpha*", "beta*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:

- Rule 1 identifies images tagged with prefix `alpha` and
  `beta`. It sees all images. It should mark images,
  starting with the oldest, until there is one or fewer images remaining
  that match. It marks image A and B for expiration.
- Result: Images A and B are expired.

## Filtering on all images

The following lifecycle policy examples specify all images with different filters.
An example repository and lifecycle policy are given along with an explanation of
the outcome.

### Example A

The following shows the lifecycle policy syntax for a policy that applies to
all rules but keeps only one image and expires all others.

Repository contents:

- Image A, Taglist: ["alpha-1"], Pushed: 4 days ago
- Image B, Taglist: ["beta-1"], Pushed: 3 days ago
- Image C, Taglist: [], Pushed: 2 days ago
- Image D, Taglist: ["alpha-2"], Pushed: 1 day ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "any",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:

- Rule 1 identifies all images. It sees images A, B, C, and D. It should
  expire all images other than the newest one. It marks images A, B, and C
  for expiration.
- Result: Images A, B, and C are expired.

### Example B

The following example illustrates a lifecycle policy that combines all the
rule types in a single policy.

Repository contents:

- Image A, Taglist: ["alpha-1", "beta-1"], Pushed: 4 days ago
- Image B, Taglist: [], Pushed: 3 days ago
- Image C, Taglist: ["alpha-2"], Pushed: 2 days ago
- Image D, Taglist: ["git hash"], Pushed: 1 day ago
- Image E, Taglist: [], Pushed: 1 day ago

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Rule 1",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["alpha*"],
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 2,
            "description": "Rule 2",
            "selection": {
                "tagStatus": "untagged",
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        },
        {
            "rulePriority": 3,
            "description": "Rule 3",
            "selection": {
                "tagStatus": "any",
                "countType": "imageCountMoreThan",
                "countNumber": 1
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```

The logic of this lifecycle policy would be:

- Rule 1 identifies images tagged with prefix `alpha`. It
  identifies images A and C. It should keep the newest image and mark the
  rest for expiration. It marks image A for expiration.
- Rule 2 identifies untagged images. It identifies images B and E. It
  should mark all images older than one day for expiration. It marks image
  B for expiration.
- Rule 3 identifies all images. It identifies images A, B, C, D, and E.
  It should keep the newest image and mark the rest for expiration.
  However, it can't mark images A, B, C, or E because they were identified
  by higher priority rules. It marks image D for expiration.
- Result: Images A, B, and D are expired.

## Archive examples

The following examples show lifecycle policies that archive images instead of deleting them.

### Archiving images older than a specified number of days

The following example shows a lifecycle policy that archives images with tags starting with `prod` that are older than 30 days:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive production images older than 30 days",
            "selection": {
                "tagStatus": "tagged",
                "tagPatternList": ["prod*"],
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 30
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        }
    ]
}
```

### Archiving images not pulled in a specified number of days

The following example shows a lifecycle policy that archives images that haven't been pulled in 90 days:

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive images not pulled in 90 days",
            "selection": {
                "tagStatus": "any",
                "countType": "sinceImagePulled",
                "countUnit": "days",
                "countNumber": 90
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        }
    ]
}
```

### Combining archive and expire rules

The following example shows a lifecycle policy that archives images older than 30 days and then permanently expires images that have been archived for more than 365 days:

###### Note

Archived images have a minimum storage duration of 90 days. You cannot configure lifecycle policies that delete images that have been in archive for less than 90 days. If you must delete images that have been archived for less than 90 days, you need to use the **batch-delete-image** API, but you will be charged for the 90-day minimum storage duration.

```
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Archive images older than 30 days",
            "selection": {
                "tagStatus": "any",
                "countType": "sinceImagePushed",
                "countUnit": "days",
                "countNumber": 30
            },
            "action": {
                "type": "transition",
                "targetStorageClass": "archive"
            }
        },
        {
            "rulePriority": 2,
            "description": "Expire images archived for more than 365 days",
            "selection": {
                "tagStatus": "any",
                "storageClass": "archive",
                "countType": "sinceImageTransitioned",
                "countUnit": "days",
                "countNumber": 365
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
```
