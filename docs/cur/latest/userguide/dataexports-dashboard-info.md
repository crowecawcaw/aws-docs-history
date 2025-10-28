# Understanding the Cost and Usage Dashboard

The Cost and Usage Dashboard is an easy to deploy, secure, and pre-built dashboard powered
by Amazon QuickSight, and inspired from the [Cloud Intelligence
Dashboards](https://www.wellarchitectedlabs.com/cloud-intelligence-dashboards/ "https://www.wellarchitectedlabs.com/cloud-intelligence-dashboards/") (CID) open source project. The Cost and Usage Dashboard includes a subset
of the summary visuals without the resource-level views from the [CUDOS dashboard](https://www.wellarchitectedlabs.com/cloud-intelligence-dashboards/#foundational-dashboards "https://www.wellarchitectedlabs.com/cloud-intelligence-dashboards/#foundational-dashboards"), which is one of the six Cloud Intelligence Dashboards. The Cost and
Usage Dashboard brings the benefits of the CUDOS solution into an AWS Billing and Cost Management console feature that
is easy to set up, and frees you from maintaining the underlying infrastructure, such as Amazon
Athena views or AWS Glue crawlers. You can deploy the Cost and Usage Dashboard from the
**Data Exports** page in the AWS Billing and Cost Management console within minutes. CID involves AWS
CloudFormation template-based deployment. For information on setting up the complete CID
solution, see [AWS well architected labs](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/ "https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/").

The following table summarizes the differences between a Cost and Usage Dashboard and Cloud
Intelligence Dashboards (CID):

| Feature                                       | Cost and Usage Dashboard                | Cloud Intelligence Dashboards                                                           |
| --------------------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------- |
| Deployment                                    | Seamless deployment from AWS console    | CloudFormation, Command Line, or Terraform                                              |
| Deployment options for AWS Organizations      | In management account only              | In management account or delegated linked account                                       |
| Multiple AWS Organizations aggregation        | No                                      | Yes                                                                                     |
| High-level cost and usage insights            | Yes                                     | Yes                                                                                     |
| Resource-level details                        | No                                      | Yes                                                                                     |
| Reserved Instances and Savings Plans insights | No                                      | Yes                                                                                     |
| Supported data sources                        | Cost and Usage Summary (dashboard view) | Cost and Usage Report (CUR), Compute Optimizer, Trusted Advisor, Cost Anomaly Detection |
