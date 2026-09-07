

# MIDASEC02-BP04 Develop a mechanism for regular review of IAM roles and policies
<a name="midasec02-bp04"></a>

 Establish processes to regularly review IAM roles and permissions to help prevent privilege creep and maintain access integrity over time. 

 **Desired outcome:** Stale or over-permissive access is detected and remediated proactively. 

 **Benefits of establishing this best practice:** Improves compliance posture, reduces operational risk, and enforces clean access policies aligned to least privilege. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-13"></a>

 Use tools like IAM Access Analyzer, AWS Config, and custom automation to audit and report access configuration regularly. 

### Implementation steps
<a name="implementation-steps-14"></a>
+  Establish a schedule for IAM access reviews. 
+  Use AWS IAM Access Analyzer to identify unused or overly broad permissions. 
+  Log and track review outcomes for auditing purposes. 
+  Automate revocation or modification of unneeded permissions using AWS Lambda or AWS Systems Manager. 

## Resources
<a name="resources-14"></a>
+  [ Using IAM Access Analyzer ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html) 
+  [` iam-user-policy-check `](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-policy-check.html) 