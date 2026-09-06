

# Amazon Detective Integration with Amazon Security Lake
<a name="securitylake-integration"></a>

Amazon Security Lake is a fully managed security data lake service. You can use Security Lake to automatically centralize security data from AWS environments, SaaS providers, on-premises sources, cloud sources, and third-party sources into a purpose-built data lake that's stored in your AWS account. Security Lake helps you analyze security data, so you can get a more complete understanding of your security posture across your entire organization. With Security Lake, you can also improve the protection of your workloads, applications, and data.

Amazon Detective integrates with Amazon Security Lake, which means that you can query and retrieve the raw log data stored by Security Lake. 

Using this integration, you can collect logs and events from the following sources which Security Lake natively supports. Detective supports up to source version 2 (OCSF 1.1.0).
+ AWS CloudTrail management events version 1.0 and after
+ Amazon Virtual Private Cloud (Amazon VPC) Flow Logs version 1.0 and after
+ Amazon Elastic Kubernetes Service (Amazon EKS) Audit Log version 2.0. — To use Amazon EKS audit logs as a source you must add `ram:ListResources` to the IAM permissions. For more details, see [Add the required IAM permissions to your account](https://docs.aws.amazon.com/detective/latest/userguide/securitylake-integration.html#iam-permissions).

 For details on how Security Lake automatically converts logs and events that come from natively-supported AWS services to the OCSF schema, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/open-cybersecurity-schema-framework.html).

After you integrate Detective with Security Lake, Detective begins pulling raw logs from Security Lake related to AWS CloudTrail management events and Amazon VPC Flow Logs. For more details, see [Querying raw logs](https://docs.aws.amazon.com/detective/latest/userguide/profile-panel-drilldown-overall-api-volume.html#drilldown-api-volume-time-range).