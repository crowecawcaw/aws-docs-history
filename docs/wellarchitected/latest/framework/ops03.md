

# Adopt change flow processes with quality gates

 Adopt approaches that improve the flow of changes into production and that help refactoring, fast feedback on quality, and bug fixing. These processes accelerate beneficial changes entering production, limit deployment issues, and enable the rapid identification and remediation of issues introduced through deployment activities. 

 With AWS, you can define and manage your entire workload (applications, infrastructure, policy, governance, and operations) as code. This means you can apply the same engineering discipline that you use for application code to every element of your stack. 


|  OPS03: How do you adopt change flow processes with quality gates?  | 
| --- | 
|  [OPS03-BP01 Adopt a configuration, build, and release pipeline](ops03-bp01.md)  | 
|  [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md)  | 
|  [OPS03-BP03 Implement practices to improve code quality](ops03-bp03.md)  | 
|  [OPS03-BP04 Fully automate integration and deployment](ops03-bp04.md)  | 
|  [OPS03-BP05 Design for efficient patch management](ops03-bp05.md)  | 

## Capability intent
<a name="ops03-intent"></a>
+  Every change flows through a governed pipeline that combines version control, configuration management, and automated build, test, and deployment, so changes are tracked, tested, and repeatable across environments. 
+  Changes of every kind (code, infrastructure, configuration, and security controls) are tested early, and any failure blocks promotion. 
+  Code quality is raised at the source through reviews, shared standards, and automated checks, so people focus on judgment rather than mechanical checks. 
+  The path from commit to validated deployment is fully automated, with environments defined as code and a consistent tagging strategy. 
+  Patching is a designed process that decides what to patch and when, favoring rebuilds from known good images over in-place changes. 

## Common issues to watch for
<a name="ops03-issues"></a>
+  Changes are deployed manually or on fixed release windows, which batches risk into large, infrequent events that are hard to diagnose and reverse. 
+  Testing is partial and promotion is not gated on results, so defects pass through to production unblocked. 
+  Code quality depends on review alone, without shared standards or automated checks to catch mechanical issues. 
+  Infrastructure and configuration changes bypass the discipline applied to application code, so environments drift apart. 
+  Patching is reactive and manual, so systems fall behind on security fixes until an update becomes an emergency. 