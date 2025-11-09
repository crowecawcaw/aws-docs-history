# Using TagOptions with AWS Organizations tag policies

This topic provides a brief overview of tag policies for AWS Organizations and
TagOptions for AWS Service Catalog. It also suggests how to prevent tagging conflicts
when using both features simultaneously.

TagOptions for AWS Service Catalog apply to provisioned products (CloudFormation
stacks), while tag policies for AWS Organizations apply to AWS accounts
and organizational units (OU) or an organizational root. For example, if you attach a
tag policy to an OU, the same tag policy applies to all accounts in that OU. If you use
both tagging features simultaneously, you should configure them so they won't conflict.

## Tag policies

Tag policies allow you to define rules on how to use tags on AWS
resources in your accounts in AWS Organizations. You can use tag policies to create
and maintain a consistent approach for tagging AWS resources at the
account level.

Tag policies provide an easy way to ensure users apply consistent tags, audit
tagged resources, and maintain proper resource categorization. You can also define
how tag keys should be capitalized, and the values you want to permit. For example,
you can require that all EC2 instances in an account must have a tag key set as
`CostCenter` and values for that tag to be `Data Insights` or `Marketing`.

Tag policies enable you to select options to enforce tagging rules, prevent
noncompliant operations for tags, and specify the resource types to which
enforcement applies. If you don’t choose an enforcement option, tag polices let you
create or mutate the noncompliant tags, but reports them as noncompliant in the AWS Organizations console.

For more information on how to set up account level tagging enforcement, see
[Tag policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") in _AWS Organizations_.

## TagOptions

TagOptions are a tagging feature that AWS Service Catalog applies to provisioned
products at the CloudFormation stack level if they’re applied to an associated
product. AWS Service Catalog provides a TagOptions library where you can define
the key-value pairs to associate with your AWS Service Catalog products. When you
launch a AWS Service Catalog product, you must choose TagOption values for the
existing TagOption keys associated to that portfolio or product to launch that
product. Because you set TagOptions at the portfolio or product levels, you can
enforce a consistent taxonomy for tagging with portfolios shared across accounts and
regions.

For more information on how to set up TagOptions in AWS Service Catalog, see [AWS Service Catalog TagOption Library](tagoptions.md "tagoptions.md").

## Avoiding conflicts between AWS Organizations tag policies and AWS Service Catalog TagOptions

If you configure AWS Organizations tag policies
for accounts
in your organization,
we recommend the following:

- Share the requirements
  for conformant tags
  with administrators
  who also manage TagOptions
  for AWS Service Catalog portfolios and products.
- Share the requirements
  for conformant tags
  with end users
  who might launch products
  in AWS Service Catalog and append optional end user tags
  to their product launches.

Suppose you want to launch a product in AWS Service Catalog that uses the TagOption key `city`,
and you have a tag policy that requires tag keys with `city` to have tag values of
**U.S cities**, such as `Atlanta`, `San Francisco`, or `Austin`.
AWS Service Catalog does not allow you to launch a product without having selected TagOption values for the required TagOption keys for a product.

In this case, if you have TagOption values for the TagOption key `city` that include
**South American cities**, such as `Rio de Janeiro` or `Buenos Aires`,
AWS Service Catalog will not launch the product. Instead, you must select a TagOption value that includes a U.S. city during launch
to comply with the tag policy.

The following table provides scenarios
that describe how
to resolve the tagging conflict issues
you might encounter
when using tag policies and TagOptions
at the same time.

| Scenario                                                                                                 | Reason                                                                                                                                                                                                          | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Product fails to launch because of noncompliant tags if tag<br>enforcement is checked in the tag policy. | Specifying TagOptions with keys and values that you have not<br>added to the allowed list of compliant tags in your tag policy.<br>Adding optional custom tags that are not conformant<br>with your tag policy. | If you configure a specific capitalization schema in your tag<br>policy tag key capitalization enforcement, ensure that your<br>TagOptions tag keys and optional custom tag keys are consistent with<br>what you've specified in your tag policy. Note when the<br>tag key capitalization enforcement box is unchecked in your tag<br>policy, it results in all lowercase tag keys being compliant,<br>and ensures your TagOptions tag keys and optional custom tag<br>keys are consistent (such as all lowercase) with what you've<br>required in your tag policy. |
| Product fails to launch due to nonconformant tag key<br>capitalization.                                  | Specifying capitalization in the TagOptions keys that is<br>inconsistent with your tag policy capitalization enforcement<br>rules.                                                                              | Correctly configure your tag policies. If you don’t specify tag<br>key capitalization compliance, the default tag key capitalization is<br>all lowercase. In addition, if you don’t specify tag<br>key capitalization compliance in your tag policy, make sure your<br>TagOptions tag keys in AWS Service Catalog are all lowercase to<br>comply to enforcement rules.If you use a tag policy<br>that doesn’t have capitalization compliance enabled, that tag<br>policy only considers all lower case tag keys to be<br>compliant.                                 |
| Product fails to launch because of incompatible tag<br>values.                                           | Selecting a TagOptions tag value for a product launch that is not<br>in your tag policy Tag Value Compliance allowed list.                                                                                      | Associate TagOptions to your products and portfolios that are<br>consistent with what you've required in the list tag policy Tag<br>Value Compliance allowed tag values.                                                                                                                                                                                                                                                                                                                                                                                            |
