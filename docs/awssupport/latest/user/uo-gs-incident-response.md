

# Unified Operations Getting started: How to request 5-minute incident response
<a name="uo-gs-incident-response"></a>

 AWS Unified Operations offers 5-minute incident response for your critical incidents. To request a 5-minute inbound response you can [create a support case from a support interaction](create-support-case-from-interaction.md) or use the [legacy support case creation method](case-management-legacy.md#creating-a-support-case-legacy). When you create your case, make sure that you enter the following information to ensure that your case receives a response within 5 minutes:

**Note**  
Use this method regardless of whether you use proactive monitoring or not, or when incidents occur before alarm setup is complete.

1. For **Case type**, choose **Technical**.

1. For **Service**, choose the affected AWS service.

1. For **Category**, choose the option that best matches your issue.

1. For **Severity**, choose **Business-critical system down**.

1. In the **Description**, include the following information

   1. Technical information
      + Workload name
      + Affected AWS Resource ARN(s)

   1. Business information
      + Description of impact to the business
      + (Optional) Customer bridge details

**Note**  
Resolution effectiveness depends on available context. Alarm onboarded workloads benefit from immediate access to comprehensive workload information, while non-onboarded workloads begin with service health data and customer-provided information.