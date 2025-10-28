**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# ATP example: Response inspection

configuration

The following JSON listing shows an example protection pack (web ACL) with an AWS WAF Fraud Control account takeover prevention (ATP) managed rule
group that is configured to inspect origin responses. Note the response inspection configuration, which specifies success and response status codes. You can also configure success and response settings based on header, body, and body JSON matches. This JSON
includes the protection pack (web ACL)'s automatically generated settings, like the label namespace
and the protection pack (web ACL)'s application integration URL.

###### Note

ATP response inspection is available only in protection packs (web ACLs) that protect CloudFront distributions.

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
 "ResponseInspection": {
 "StatusCode": {
 "SuccessCodes": [
 200
 ],
 "FailureCodes": [
 401
 ]
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
