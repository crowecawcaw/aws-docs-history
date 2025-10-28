**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# ATP example: Simple

configuration

The following JSON listing shows an example protection pack (web ACL) with an AWS WAF Fraud Control account takeover prevention (ATP) managed rule
group. Note the additional sign-in page configuration, which gives the rule group
the information it needs to monitor and manage your login requests. This JSON
includes the protection pack (web ACL)'s automatically generated settings, like the label namespace
and the protection pack (web ACL)'s application integration URL.

```

{
    "WebACL": {
        "LabelNamespace": "awswaf:111122223333:webacl:ATPModuleACL:",
        "Capacity": 50,
        "Description": "This is a test protection pack (web ACL) for ATP.",
        "Rules": [
            {
                "Priority": 1,
                "OverrideAction": {
                    "None": {}
                },
                "VisibilityConfig": {
                    "SampledRequestsEnabled": true,
                    "CloudWatchMetricsEnabled": true,
                    "MetricName": "AccountTakeOverValidationRule"
                },
                "Name": "DetectCompromisedUserCredentials",
                "Statement": {
                    **"ManagedRuleGroupStatement": {
 "VendorName": "AWS",
 "Name": "`AWSManagedRulesATPRuleSet`",
 "ManagedRuleGroupConfigs": [
 {
 "AWSManagedRulesATPRuleSet": {
 "LoginPath": "/web/login",
 "RequestInspection": {
 "PayloadType": "JSON",
 "UsernameField": {
 "Identifier": "/form/username"
 },
 "PasswordField": {
 "Identifier": "/form/password"
 }
 },
 "EnableRegexInPath": false
 }
 }
 ]
 }**
                }
            }
        ],
        "VisibilityConfig": {
            "SampledRequestsEnabled": true,
            "CloudWatchMetricsEnabled": true,
            "MetricName": "ATPValidationAcl"
        },
        "DefaultAction": {
            "Allow": {}
        },
        "ManagedByFirewallManager": false,
        "RetrofittedByFirewallManager": false,
        "Id": "32q10987-65rs-4tuv-3210-98765wxyz432",
        "ARN": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/ATPModuleACL/32q10987-65rs-4tuv-3210-98765wxyz432",
        "Name": "ATPModuleACL"
    },
    "ApplicationIntegrationURL": "https://9z87abce34ea.us-east-1.sdk.awswaf.com/9z87abce34ea/1234567a1b10/",
    "LockToken": "6d0e6966-95c9-48b6-b51d-8e82e523b847"
}
```
