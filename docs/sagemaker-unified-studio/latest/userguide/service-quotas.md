# Quotas for Amazon SageMaker Unified Studio

Your AWS account has default quotas, formerly referred to as limits, for
each AWS service. Unless otherwise noted, each quota is account-specific and
Region-specific. If the default quotas don't fit your use case, you can request a quota increase. You can use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") from the AWS Management Console or contact [AWS Support](https://aws.amazon.com/startups/contact-us "https://aws.amazon.com/startups/contact-us") to submit
requests on your behalf. For more information about how to request a quota increase using
the Service Quota console, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User
Guide_.

The resource quota limits are applied at the account level, meaning the depletion of
resource quotas in one project can affect all other projects within the account.
Administrators can monitor resource usage by project and take necessary actions through the
Amazon SageMaker Unified Studio console. When approaching quota limits, administrators can delete unused resources
to free up quota allocation or request a quota increase.

Amazon SageMaker Unified Studio has the following default quotas and limits. These default quotas provide a
balance between resource availability and cost management.

| Resource                                                                                                                                                               | Default |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Maximum number of JupyterLab instances                                                                                                                                 | 4000    |
| Maximum number of project members for your Amazon SageMaker platform<br>domain. The total number of project members is the product of project<br>members and projects. | 6000    |
| Maximum number of spaces                                                                                                                                               | 6000    |
| Maximum number of projects                                                                                                                                             | 500     |
| Maximum number of Micro environments                                                                                                                                   | 200     |

For more information about other AWS service quotas, see [AWS
service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

For more quotas information, see the following:

- [Amazon SageMaker Supported Regions and Quotas](../../../sagemaker/latest/dg/regions-quotas.md "../../../sagemaker/latest/dg/regions-quotas.md")
- [Amazon
  Managed Workflows for Apache Airflow endpoints and quotas](../../../general/latest/gr/mwaa.md "../../../general/latest/gr/mwaa.md")
- [Amazon Redshift endpoints and quotas](../../../general/latest/gr/redshift-service.md "../../../general/latest/gr/redshift-service.md")
- [Amazon EMR
  endpoints and quotas](../../../general/latest/gr/emr.md "../../../general/latest/gr/emr.md")
- [Amazon
  DataZone endpoints and quotas](../../../general/latest/gr/datazone.md "../../../general/latest/gr/datazone.md")
- [Amazon Q
  Business endpoints and quotas](../../../general/latest/gr/amazonq.md "../../../general/latest/gr/amazonq.md")
- [Amazon
  Athena endpoints and quotas](../../../general/latest/gr/athena.md "../../../general/latest/gr/athena.md")
- [Amazon
  Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md")
- [AWS Glue
  endpoints and quotas](../../../general/latest/gr/glue.md "../../../general/latest/gr/glue.md")
