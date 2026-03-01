# Lifecycle policy properties in Amazon ECR

Lifecycle policies have the following properties.

To see examples of lifecycle policies, see [Examples of lifecycle policies in Amazon ECR](lifecycle_policy_examples.md "lifecycle_policy_examples.md"). For instructions about creating a
lifecycle policy by using the AWS CLI, see [To create a lifecycle policy (AWS CLI)](lp_creation.md#lp-creation-cli "lp_creation.md#lp-creation-cli").

## Rule priority

`rulePriority`

Type: integer

Required: yes

Sets the order in which rules are applied, lowest to highest. A
lifecycle policy rule with a priority of `1` is applied
first, a rule with priority of `2` is next, and so on. When
you add rules to a lifecycle policy, you must give them each a unique
value for `rulePriority`. Values don't need to be sequential
across rules in a policy. A rule with a `tagStatus` value of
`any` must have the highest value for
`rulePriority` and be evaluated last.

## Description

`description`

Type: string

Required: no

(Optional) Describes the purpose of a rule within a lifecycle
policy.

## Tag status

`tagStatus`

Type: string

Required: yes

Determines whether the lifecycle policy rule that you are adding
specifies a tag for an image. Acceptable options are
`tagged`, `untagged`, or `any`. If you
specify `any`, then all images have the rule evaluated
against them. If you specify `tagged`, then you must also
specify a `tagPrefixList` value or a `tagPatternList` value. If you specify
`untagged`, then you must omit both
`tagPrefixList` and `tagPatternList`.

## Tag pattern list

`tagPatternList`

Type: list[string]

Required: yes, if `tagStatus` is set to tagged and
`tagPrefixList` isn't specified

When creating a lifecycle policy for tagged images, it's best practice
to use a `tagPatternList` to specify the tags to expire. You
specify a comma-separated list of image tag patterns that may contain
wildcards (`*`) on which to take action with your lifecycle
policy. For example, if your images are tagged as `prod`,
`prod1`, `prod2`, and so on, you would use the
tag pattern list `prod*` to specify all of them. If you
specify multiple tags, only the images with all specified tags are
selected.

###### Important

There is a maximum limit of four wildcards (`*`) per
string. For example, `["*test*1*2*3", "test*1*2*3*"]` is
valid but `["test*1*2*3*4*5*6"]` is invalid.

## Tag prefix list

`tagPrefixList`

Type: list[string]

Required: yes, if `tagStatus` is set to tagged and
`tagPatternList` isn't specified

Only used if you specified `"tagStatus": "tagged"` and you
aren't specifying a `tagPatternList`. You must specify a
comma-separated list of image tag prefixes on which to take action with
your lifecycle policy. For example, if your images are tagged as
`prod`, `prod1`, `prod2`, and so
on, you would use the tag prefix `prod` to specify all of
them. If you specify multiple tags, only the images with all specified
tags are selected.

## Storage class

`storageClass`

Type: string

Required: yes, if `countType` is `sinceImageTransitioned`

The rule will only select images of this storage class. When using a `countType` of `imageCountMoreThan`, `sinceImagePushed`, or `sinceImagePulled`, the only supported value is `standard`. When using a count type of `sinceImageTransitioned`, this is required, and the only supported value is `archive`. If you omit this, the value of `standard` will be used.

## Count type

`countType`

Type: string

Required: yes

Specify a count type to apply to the images.

If `countType` is set to `imageCountMoreThan`,
you also specify `countNumber` to create a rule that sets a
limit on the number of images that exist in your repository. If
`countType` is set to `sinceImagePushed`, `sinceImagePulled`, or `sinceImageTransitioned`, you
also specify `countUnit` and `countNumber` to
specify a time limit on the images that exist in your repository.

## Count unit

`countUnit`

Type: string

Required: yes, only if `countType` is set to
`sinceImagePushed`, `sinceImagePulled`, or `sinceImageTransitioned`

Specify a count unit of `days` to indicate that as the unit
of time, in addition to `countNumber`, which is the number of
days.

This should only be specified when `countType` is
`sinceImagePushed`, `sinceImagePulled`, or `sinceImageTransitioned`; an error will occur if you specify a
count unit when `countType` is any other value.

## Count number

`countNumber`

Type: integer

Required: yes

Specify a count number. Acceptable values are positive integers
(`0` is not an accepted value).

If the `countType` used is `imageCountMoreThan`,
then the value is the maximum number of images that you want to retain
in your repository. If the `countType` used is
`sinceImagePushed`, then the value is the maximum age
limit for your images. If the `countType` used is `sinceImagePulled`, then the value is the maximum number of days since the image was last pulled. If the `countType` used is `sinceImageTransitioned`, then the value is the maximum number of days since the image was archived.

## Action

`type`

Type: string

Required: yes

Specify an action type. The supported values are
`expire` (to delete images) and `transition` (to move images to archive storage).

`targetStorageClass`

Type: string

Required: yes, if `type` is `transition`

The storage class you want the lifecycle policy to transition the image to. `archive` is the only supported value.
