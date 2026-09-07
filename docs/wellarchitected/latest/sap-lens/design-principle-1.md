

# 1 - Design SAP workload to allow understanding and reaction to its state
<a name="design-principle-1"></a>

 **How do you design your SAP workload so that you can understand its state?** Design your SAP workload so that it provides the information necessary across all components for you to understand its internal and external state. Consider infrastructure, SAP technology/basis, front end, and network components. Design monitoring and logging approaches which capture metrics to allow real-time monitoring and also historical logging to allow remediation and post-event analysis. 


| ID | Priority | Best Practice | 
| --- | --- | --- | 
| ☐ BP 1.1 | Required | Implement prerequisites for monitoring SAP on AWS | 
| ☐ BP 1.2 | Required | Implement infrastructure monitoring for SAP | 
| ☐ BP 1.3 | Required | Implement application and database monitoring for SAP | 
| ☐ BP 1.4 | Highly Recommended | Implement workload configuration monitoring | 
| ☐ BP 1.5 | Highly Recommended | Implement user activity monitoring | 
| ☐ BP 1.6 | Highly Recommended | Implement dependency monitoring | 
| ☐ BP 1.7 | Recommended | Implement single pane of glass health monitoring across your SAP workloads | 
| ☐ BP 1.8 | Recommended | Use automated response and recovery techniques to react to monitoring alerts | 

 For more details, see the following links and information: 
+  AWS Documentation: [AWS Data Provider for SAP](https://docs.aws.amazon.com/sap/latest/general/aws-data-provider.html) 
+  AWS Service: [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/index.html) 
+  SAP on AWS Blog: [Set up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/) 
+  SAP on AWS Blog: [Serverless Monitoring for SAP](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/) 
+  AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2) 
+  SAP Note: [1656250 - SAP on AWS: Support Prerequisites](https://launchpad.support.sap.com/#/notes/1656250) [Requires SAP Portal Access] 
+  SAP Documentation: [SAP Solution Manager 7.2 - Application Operations](http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html) 