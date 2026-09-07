

# MIDACOST02-BP03 Automate production-aware resource decommissioning
<a name="midacost02-bp03"></a>

 Implement automated identification and removal of unused resources synchronized with production schedules, product lifecycles, and manufacturing compliance requirements. This automation includes safety checks, rollback procedures, and consideration of maintenance windows to help prevent disruption to manufacturing operations. 

 **Desired outcome:** Automated identification and removal of unused resources synchronized with production schedules, product lifecycles, and manufacturing compliance requirements. 

 **Common anti-patterns:** 
+  Implementing automated removal without considering production schedules 
+  Using the same automation rules for both IT and OT resources 
+  Not incorporating manufacturing compliance checks in automation 
+  Failing to account for interdependencies with MES, SCADA, or other manufacturing systems 
+  Automated decommissioning during production hours 
+  Not maintaining audit trails for regulated manufacturing processes 
+  Bypassing quality management system validations 

 **Benefits of establishing this best practice:** 
+  Reduced manual intervention 
+  Consistent application of decommissioning policies 
+  Immediate cost savings from unused resource removal 
+  Reduced human error 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-59"></a>

 Create automated systems that can safely identify, tag, notify relevant stakeholders, and finally remove resources that are no longer needed, with appropriate safeguards to help prevent disruption to manufacturing operations. 

### Implementation steps
<a name="implementation-steps-39"></a>

1.  Define automation rules for resource identification. 

1.  Create automated workflows for: 
   +  Resource tagging 
   +  Notification of stakeholders 
   +  Backup creation 
   +  Resource termination 

1.  Implement safety checks and rollback procedures. 

1.  Monitor automation effectiveness. 

1.  Include manufacturing-specific automation rules: 
   +  Production schedule-aware decommissioning 
   +  Product lifecycle milestones 
   +  Equipment maintenance windows 
   +  Shift pattern considerations 

## Key AWS services
<a name="key-aws-services-21"></a>
+  AWS Lambda 
+  Amazon EventBridge 
+  AWS Config Rules 
+  AWS Systems Manager Automation 
+  AWS Step Functions 
+  Amazon SNS 

## Resources
<a name="resources-60"></a>

 **Related documents:** 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduler.html) 
+  [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) 
+  [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) 