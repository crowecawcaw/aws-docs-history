

# TELCOOPS05-BP02 Assign network interfaces in dependency order to prevent binding failures during instance lifecycle events
<a name="telcoops05-bp02"></a>

 When an EC2 instance hosting a container network function (CNF) launches or is replaced, its interfaces must be attached in the order the application's startup sequence requires. If the CNF binds to an interface that does not yet exist, it crashes or fails without raising an error. This best practice attaches interfaces in dependency order and holds the CNF until its interfaces are ready. 

 **Desired outcome:** 
+  Interface attachment automation assigns ENIs in the order the CNF expects: primary (control) first, then persistent interfaces (management, OAM), then ephemeral interfaces (data plane). 
+  CNF processes don't start until all required interfaces are attached, configured with IP addresses, and confirmed link-up. 
+  Instance-replacement events recreate interfaces in the same order and configuration as the original. 

 **Common anti-patterns:** 
+  Attaching all secondary interfaces in parallel without regard to the CNF's expected device ordering. 
+  Starting the CNF before confirming all secondary interfaces are attached and have IP connectivity. 
+  Not distinguishing persistent interfaces, which need a stable IP across replacements, from ephemeral interfaces, where a new IP is acceptable. 
+  Recreating interfaces in a different order after replacement, so device names no longer match what the CNF expects. 

 **Benefits of establishing this best practice:** 
+  Instance replacement is zero-touch because interfaces are recreated in the expected order and configuration. 
+  Device naming stays predictable, so DPDK and CNI bindings continue to work after a replacement. 
+  Holding the CNF until interfaces are link-up prevents silent bind failures and crashes at startup. 
+  Recovery from instance failure is faster and more reliable, which reduces mean time to repair. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A network function requires a specific device for control traffic, another for management or OAM traffic, and others for data-plane traffic, and binds to them by name or index at initialization. If automation attaches interfaces in a different order, or in parallel so the order is nondeterministic, the CNF binds to the wrong device or to one that is not yet present. A failure without an alarm means that the instance appears healthy while it serves traffic incorrectly. 

 Persistent interfaces (management, OAM, synchronization) must retain the same IP address across instance replacements, because peers and management systems reference those addresses. On the other hand, ephemeral interfaces (data plane) can take a new address on each instance. Attach persistent interfaces first and ephemeral ones last to satisfy the CNF's expected ordering and preserve the stable addresses. Misclassifying a persistent interface such as OAM as ephemeral breaks management connectivity on replacement, because the interface is recreated with a new address. 

 Enforcing order requires a control point in the lifecycle where the instance is paused until attachment completes. An Amazon EC2 Auto Scaling lifecycle hook provides this functionality, where the instance enters a wait state, an orchestrator attaches each interface in sequence and verifies link-up before proceeding, and only then does the hook complete and allow the CNF to start. Sequencing several dependent attachments with verification between them is a workflow rather than a single action, so AWS Step Functions driven from an Amazon EC2 Auto Scaling lifecycle hook, with AWS Lambda performing each attach-and-verify, expresses the ordering in a neat and repeatable way. 

### Implementation steps
<a name="implementation-steps"></a>
+  Classify interfaces as persistent or ephemeral: for each CNF, list its interfaces, mark each as persistent (stable IP required) or ephemeral (new IP acceptable), and record the order in which the CNF binds to them. 
+  Define the attachment sequence: order attachment as control interface first, then persistent management and OAM interfaces, then ephemeral data-plane interfaces, and store the sequence with the workload's configuration as code. 
+  Pause the instance with an Amazon EC2 Auto Scaling lifecycle hook that holds the instance in a wait state until interface attachment completes. 
+  Attach and verify each interface in order: drive the sequence with AWS Step Functions invoking AWS Lambda to attach each interface, assign its address, and confirm link-up before moving to the next, then complete the lifecycle action. 
+  Confirm identical recreation on replacement: test an instance replacement and verify that interfaces are recreated in the same order, that persistent interfaces retain their addresses, and that the CNF starts only after all interfaces are ready. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 