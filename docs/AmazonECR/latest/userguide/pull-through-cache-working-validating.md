

# Validating pull through cache rules in Amazon ECR
<a name="pull-through-cache-working-validating"></a>

After you create a pull through cache rule, for upstream registries that require authentication you can validate that the rule works properly. When validating a pull through cache rule, Amazon ECR makes a network connection with the upstream registry, verifies that it can access the Secrets Manager secret containing the credentials for the upstream registry, and verifies that authentication was successful.

Before you start working with your pull through cache rules, verify that you have the proper IAM permissions. For more information, see [IAM permissions required to sync an upstream registry with an Amazon ECR private registry](pull-through-cache-iam.md).

## To validate a pull through cache rule (AWS Management Console)
<a name="pull-through-cache-working-verifying-console"></a>

The following steps show how to validate a pull through cache rule using the Amazon ECR console.

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region containing the pull through cache rule to validate.

1. In the navigation pane, choose **Private registry**, **Pull through cache**.

1. On the **Pull through cache configuration** page, select the pull through cache rule to validate. Then, use the **Actions** drop down menu and choose **View details**.

1. On the pull through cache rule detail page, use the **Actions** drop down menu and choose **Verify authentication**. Amazon ECR will display a banner with the result.

1. Repeat these steps for each pull through cache rule you want to validate.

## To validate a pull through cache rule (AWS CLI)
<a name="pull-through-cache-working-verifying-cli"></a>

The [validate-pull-through-cache-rule](https://docs.aws.amazon.com/cli/latest/reference/ecr/validate-pull-through-cache-rule.html) AWS CLI command is used to validate a pull through cache rule for an Amazon ECR private registry. The following example uses the `ecr-public` namespace prefix. Replace that value with the prefix value for the pull through cache rule to validate.

```
aws ecr validate-pull-through-cache-rule \
     --ecr-repository-prefix {{ecr-public}} \
     --region {{us-east-2}}
```

In the response, the `isValid` parameter indicates whether the validation was successful or not. If `true`, Amazon ECR was able to reach the upstream registry and authentication was successful. If `false`, there was an issue and validation failed. The `failure` parameter indicates the cause.