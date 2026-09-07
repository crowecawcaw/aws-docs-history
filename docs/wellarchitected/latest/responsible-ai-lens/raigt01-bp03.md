

# RAIGT01-BP03 Create a plan for publishing and updating documentation
<a name="raigt01-bp03"></a>

 Identify which documents require updates based on stakeholder feedback, new use-cases, new system releases, and industry best practice developments. Dedicate an owner to facilitate the change management process which supports plans for review cycles, document and system versioning and approval chains. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation considerations
<a name="implementation-considerations-88"></a>

1.  Establish documentation management infrastructure. Define the criteria for mandatory updates and create automated triggers (AWS EventBridge, Amazon SNS) based on system updates and stakeholder feedback. Assign ownership and responsibility for making the updates. Maintain document version history. 

1.  Establish and follow a review process. Set up an approval chain and create approval workflows. Check the contents for completeness, clarity, and technical accuracy. 

1.  Publish the updates and make them accessible to the stakeholders. Have a communication plan. Optionally set up an automated system to notify stakeholders of document updates. 

## Resources
<a name="resources-84"></a>

 **Related documents:** 
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.8.2 System documentation and information for users 

 **Related tools:** 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon Simple Notification Service](https://aws.amazon.com/sns/) 
+  [Serverless Computing - AWS Lambda](https://aws.amazon.com/pm/lambda/) 
+  [Cloud Object Storage - Amazon S3](https://aws.amazon.com/pm/serv-s3/) 