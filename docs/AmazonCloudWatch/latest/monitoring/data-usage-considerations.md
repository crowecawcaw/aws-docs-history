# How CloudWatch investigations finds data for suggestions

CloudWatch investigations uses a wide range of data sources to determine dependency relationships and plan
analysis paths, including telemetry data configurations, service configurations, and
observed relationships. These dependency relationships are found more easily if you use
CloudWatch Application Signals and AWS X-Ray. When Application Signals and X-Ray aren't
available, CloudWatch investigations will attempt to infer dependency relationships through co-occurring
telemetry anomalies.

While CloudWatch investigations will continue to analyze telemetry data and provide suggestions without
these features enabled, we strongly recommend that you enable the services and features
listed in [(Recommended) Best practices to enhance investigations](Investigations-RecommendedServices.md "Investigations-RecommendedServices.md") for optimal quality and
performance for CloudWatch investigations.

###### Important

To help CloudWatch investigations provide the most relevant information, we might use certain content
from CloudWatch investigations, including but not limited to, questions that you ask CloudWatch investigations and its
response, insights, user interactions, telemetry, and metadata for service
improvements. Your trust and privacy, as well as the security of your content, is
our highest priority. For more information, see [**AWS Service
Terms**](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") and [**AWS responsible AI
policy**](https://aws.amazon.com/ai/responsible-ai/policy/ "https://aws.amazon.com/ai/responsible-ai/policy/").

You can opt out of having your content collected to develop or improve the quality
of CloudWatch investigations by creating an AI service opt-out policy for CloudWatch or AI Operations (aiops).
For more information, see [AI
services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the AWS Organizations User Guide.
