# View SageMaker AI resources in your

domain

## Use the SageMaker AI console to view

your domain resources

You can view Amazon SageMaker AI resources in your Amazon SageMaker AI domain using the SageMaker AI console. Use the
following instructions to learn how to view the resources tagged by the domain ARN.

The displayed SageMaker resources following this procedure are those that have the relevant
`sagemaker:domain-arn` tag associated to them. Untagged resources may have
been created outside the context of a domain or were created before 11/30/2022, when
resources were not automatically tagged with the domain ARN. You can add a tag to
untagged resources for better filtration by following the steps in [Backfill domain tags](domain-multiple-backfill.md "domain-multiple-backfill.md"). Resources
created in other domains are automatically filtered out.

###### Note

This is not a complete list of active resources on your domain. For all active
SageMaker resources, see [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/").

###### To view SageMaker AI resources in your domain using the console

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Expand the left navigation pane, if not already expanded.
3. Under **Admin configurations**, choose
   **Domains**.
4. From the list of domains, select the domain that you want to open the
   **Domain settings** page for.
5. On the **Domain details** page, choose the
   **Resources** tab.
6. On the **Domain resources** page, you can view the details of
   the resources tagged with the relative domain ARN. The running resources are
   displayed by default.
7. (Optional) You can filter the displayed resources for each resource type by
   using the search icon or **Filter status** at the top of each
   resource type.

## Use the AWS CLI to view the

SageMaker AI spaces in your domain

The following section provides instructions on how to view the spaces in your
domain using the AWS CLI.

You will need to know your `domain-id`. To obtain your
domain details, see [View domains](domain-view.md "domain-view.md").

```
aws sagemaker list-spaces \
    --region `region`
    --domain-id `domain-id`
```

## Use the AWS CLI to view the

SageMaker AI applications in your domain

The following section provides instructions on how to view the applications in your
domain using the AWS CLI.

You will need to know your `domain-id`. To obtain your
domain details, see [View domains](domain-view.md "domain-view.md").

```
aws sagemaker list-apps \
    --domain-id-equals `domain-id`
```

If you do not see the applications or your domain, you may need to change your
AWS Region. To do so, use `aws configure` to update your AWS credentials.
For more information, see [configure](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html").
