

# ADVREL06-BP08 Decouple innovative format rendering from core ad delivery pipeline
<a name="advrel06-bp08"></a>

 Innovative format rendering logic adds complexity that does not belong in the critical path of standard ad delivery. A squeeze-back rendering failure must not affect standard pre-roll ad serving. 

 **Desired outcome:** 
+  Format-specific rendering services operate as independent microservices with their own scaling, health checks, and deployment pipelines. 
+  The core ADS is unaffected by format service failures, standard VAST delivery continues normally. 
+  Failed format rendering requests are captured in dead-letter queues for analysis without blocking the main ad delivery pipeline. 

 **Common anti-patterns:** 
+  Coupling innovative format logic into the core ADS code base, format bugs can crash the entire ad server 
+  Shared deployment pipeline for core ADS and format services, format service deployment failures trigger full rollback 
+  No circuit breakers between core ADS and format services, format service overload cascades upstream 
+  Format rendering failures blocking the standard ad response path 

 **Benefits of establishing this best practice:** 
+  Decoupled format services help contain innovative ad format failures to their specific service. 
+  Core ad delivery (standard VAST/VPAID) remains unaffected, protecting baseline publisher revenue even during format service outages. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Innovative formats change constantly. Standard VAST and VPAID delivery, by contrast, stays stable and generates most publisher revenue. Shared code paths spread format volatility into that stable core. 

 This practice limits the scope of impact when a format breaks. A format bug must stay inside format logic, but coupled designs remove that boundary. A squeeze-back crash can halt standard pre-roll, a shared deployment can force a full rollback over one format defect, and overload in one service can cascade into the core. 

 The sidecar pattern implements a boundary where the core response includes standard video elements plus an optional format extension. A player reads the standard elements independently, and the extension only adds the innovative enhancement. An unavailable format sidecar costs only the enhancement. The ad still delivers as a standard spot, so a format outage does not create a blank slot. 

 Independent services and pipelines multiply operational overhead across deployments, alarms, and health checks. This overhead yields a bounded failure domain. The shoppable commerce gateway can fail alone while overlay ads and the core VAST path keep serving. Experiment teams own the format services and the delivery team owns the stable core, so that split needs a clear boundary. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy format services as independent ECS microservices:** Create separate ECS services per format type with independent Auto Scaling policies, task definitions, and CloudWatch alarms. Configure service-level health checks that validate format rendering functionality specifically. 

1.  **Implement sidecar extension pattern in VAST responses:** Structure the core ADS VAST response to include standard video ad elements plus an optional extension containing innovative format instructions. Player SDK processes standard elements regardless of sidecar availability. As a result, a sidecar service failure produces standard ad delivery rather than blank slots. 

1.  **Configure SQS dead-letter queues for failed rendering requests:** Add DLQ on all SQS queues serving format rendering services. Set maxReceiveCount to 3 for transient failures. Configure CloudWatch alarms on DLQ depth. Process DLQ messages on a 15-minute schedule to handle transient failures without losing impression opportunities. 

1.  **Implement independent deployment pipelines per format service:** Create separate CodePipeline pipelines for each format service. Deploy format service changes without affecting the core ADS pipeline. Include format-specific integration tests in each pipeline that validate rendering output quality. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures](advrel01-bp01.md) 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 

 **Related documents:** 
+  [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html) 

 **Related services:** 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 