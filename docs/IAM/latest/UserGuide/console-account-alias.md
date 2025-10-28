# Using an alias for your AWS account ID

Your account ID is a 12-digit number that uniquely identifies your account. By default,
IAM users in the account sign in using a web URL that includes the account ID. If they
don't have the URL, they can provide the account ID on the AWS sign-in page when they
sign-in.

Your sign-in page URL has the following format, by default.

```
https://`Your_Account_ID`.signin.aws.amazon.com/console/
```

Many people find words to be easier to remember than numbers, so creating an alias for
your account ID can help your IAM users sign-in easier.

If you create an AWS account alias for your AWS account ID, your sign-in page URL
looks like the following example.

```
https://`Your_Account_Alias`.signin.aws.amazon.com/console/
```

###### Considerations before creating an account alias

- Your AWS account can have only one alias. If you create a new alias for
  your AWS account, the new alias overwrites the previous alias, and the URL
  containing the previous alias stops working.
- The account alias must contain only digits, lowercase letters, and
  hyphens. For more information on limitations on AWS account entities, see
  [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").
- The account alias must be unique across all Amazon Web Services products within a
  given network _partition_.

A _partition_ is a group of AWS
Regions. Each AWS account is scoped to one partition.

The following are the supported partitions:

    + `aws` - AWS Regions
    + `aws-cn` - China Regions
    + `aws-us-gov` - AWS GovCloud (US)
     Regions

###### Note

Account aliases are not secrets, and they will appear in your public-facing
sign-in page URL. Do not include any sensitive information in your account
alias.

The original URL containing your AWS account ID remains active and can be
used after you create your AWS account alias.
