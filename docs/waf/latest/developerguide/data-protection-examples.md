**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Examples of data protection

This section provides log examples of data protection logging of protection pack (web ACL) traffic.

## DataProtection hashing

Webacl config

```
"data_protection_config": {
            "data_protections": [
                {
                    "field": {
                        "field_type": "SINGLE_QUERY_ARGUMENT",
                        "field_keys": [
                            "hoppy"
                        ]
                    },
                    "action": "HASH",
                    "exclude_rule_match_details": false,
                    "exclude_rate_based_details": false
                }
             ]
           }
```

Example DataProtection hashing: Log entry with the SingleQuery argument "hoppy" protected.

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionhashACL/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [{
        "ruleId": "ProtectedSQLIHeadersVisibleInSTM",
        "action": "COUNT",
        "ruleMatchDetails": [{
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "SINGLE_QUERY_ARG",
                "matchedData": [ "z6hpYAFaMYdtiTeHhxnN5ydgRE5E1WgyVIdgqH0D3iM=" ],
                "matchedFieldName": "hoppy"
        }]
    }],
"requestHeadersInserted": null,
"responseCodeSent": null,
"httpRequest": {
    "clientIp": "54.239.98.137",
    "country": "US",
    "headers": [{
        "name": "X-Forwarded-For",
        "value": "54.239.98.137"
    }, {
        "name": "X-Forwarded-Proto",
        "value": "https"
    }, {
        "name": "X-Forwarded-Port",
        "value": "443"
    }, {
        "name": "Host",
        "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
    }, {
        "name": "X-Amzn-Trace-Id",
        "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
    }, {
        "name": "Accept-Encoding",
        "value": "gzip"
    }, {
        "name": "User-Agent",
        "value": "okhttp/3.12.1"
    }],
    "uri": "/CanaryTest",
    "args": "hoppy=z6hpYAFaMYdtiTeHhxnN5ydgRE5E1WgyVIdgqH0D3iM=&yellow=hello&x-hoppy-extra=generic-%3Cwords%3E-in-angle-brackets",
    "httpVersion": "HTTP/1.1",
    "httpMethod": "GET",
    "requestId": "FepO0F8fIAMEqoQ="
},
"labels": [{
    "name": "awswaf:forwardedip:geo:country:US"
}, {
    "name": "awswaf:forwardedip:geo:region:US-VA"
}]
}
```

## DataProtection substitution

Webacl Config

```
"data_protection_config": {
            "data_protections": [
                {
                    "field": {
                        "field_type": "SINGLE_QUERY_ARGUMENT",
                        "field_keys": [
                            "hoppy"
                        ]
                    },
                    "action": "SUBSTITUTION",
                    "exclude_rule_match_details": false,
                    "exclude_rate_based_details": false
                }
             ]
           }
```

Example DataProtection substitution: Log entry with Single Query Argument “hoppy” protected

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionhashACL/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": []
"requestHeadersInserted": null,
"responseCodeSent": null,
"httpRequest": {
    "clientIp": "54.239.98.137",
    "country": "US",
    "headers": [{
        "name": "X-Forwarded-For",
        "value": "54.239.98.137"
    }, {
        "name": "X-Forwarded-Proto",
        "value": "https"
    }, {
        "name": "X-Forwarded-Port",
        "value": "443"
    }, {
        "name": "Host",
        "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
    }, {
        "name": "X-Amzn-Trace-Id",
        "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
    }, {
        "name": "Accept-Encoding",
        "value": "gzip"
    }, {
        "name": "User-Agent",
        "value": "okhttp/3.12.1"
    }],
    "uri": "/CanaryTest",
    "args": "hoppy=REDACTED&yellow=hello&x-hoppy-extra=generic-%3Cwords%3E-in-angle-brackets",
    "httpVersion": "HTTP/1.1",
    "httpMethod": "GET",
    "requestId": "FepO0F8fIAMEqoQ="
},
"labels": [{
    "name": "awswaf:forwardedip:geo:country:US"
}, {
    "name": "awswaf:forwardedip:geo:region:US-VA"
}]
}
```

## Retaining data in RuleMatchDetails

Webacl config

```
"data_protection_config": {
            "data_protections": [
                {
                    "field": {
                        "field_type": "SINGLE_HEADER",
                        "field_keys": [
                            "hoppy"
                        ]
                    },
                    "action": "HASH",
                    "exclude_rule_match_details": true,
                    "exclude_rate_based_details": false
                }
             ]
           }
```

Example of retaining data in RuleMatchDetails: Log entry with single `Header` “hoppy” protected but the value is retained only in `RuleMatchDetails`.

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionhashACL/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [{
        "ruleId": "ProtectedSQLIHeadersVisibleInSTM",
        "action": "COUNT",
        "ruleMatchDetails": [{
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "HEADER",
                "matchedData": [ "10", "AND", "1" ],
                "matchedFieldName": "hoppy"
        }]
    }],
"requestHeadersInserted": null,
"responseCodeSent": null,
"httpRequest": {
    "clientIp": "54.239.98.137",
    "country": "US",
    "headers": [{
        "name": "X-Forwarded-For",
        "value": "54.239.98.137"
    }, {
        "name": "X-Forwarded-Proto",
        "value": "https"
    }, {
        "name": "X-Forwarded-Port",
        "value": "443"
    }, {
        "name": "Host",
        "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
    }, {
        "name": "X-Amzn-Trace-Id",
        "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
    }, {
        "name": "hoppy",
        "value": "zuomr2mxQxofg6EI6f7hMNGaJhhPxt0rFVAXog6FLxE="
    }, {
        "name": "Accept-Encoding",
        "value": "gzip"
    }, {
        "name": "User-Agent",
        "value": "okhttp/3.12.1"
    }, {
        "name": "hoppy",
        "value": "z6hpYAFaMYdtiTeHhxnN5ydgRE5E1WgyVIdgqH0D3iM="
    }],
    "uri": "/CanaryTest",
    "args": "happy=true",
    "httpVersion": "HTTP/1.1",
    "httpMethod": "GET",
    "requestId": "FepO0F8fIAMEqoQ="
},
"labels": [{
    "name": "awswaf:forwardedip:geo:country:US"
}, {
    "name": "awswaf:forwardedip:geo:region:US-VA"
}]
}
```

## Retaining data in rateBasedRule

```
 "data_protection_config": {
            "data_protections": [
                {
                    "field": {
                        "field_type": "SINGLE_HEADER",
                        "field_keys": [
                            "hoppy"
                        ]
                    },
                    "action": "HASH",
                    "exclude_rule_match_details": false,
                    "exclude_rate_based_details": true
                }
             ]
           }
```

Example Retaining data in rateBasedRuleList: Log entry with the Single `Header` “hoppy” protected but the value is retained only in `rateBasedRuleList`

```
{
    "timestamp": 1683355579981,
    "formatVersion": 1,
    "webaclId": ...,
    "terminatingRuleId": "RateBasedRule",
    "terminatingRuleType": "RATE_BASED",
    "action": "BLOCK",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "EXAMPLE11:rjvegx5guh:CanaryTest",
    "ruleGroupList": [],
    "rateBasedRuleList": [{
        "rateBasedRuleId": ...,
        "rateBasedRuleName": "RateBasedRule",
        "limitKey": "CUSTOMKEYS",
        "maxRateAllowed": 100,
        "evaluationWindowSec": "120",
        "customValues": [{
            "key": "HEADER",
            "name": "hoppy",
            "value": "ella"
        }]
    }],
    "nonTerminatingMatchingRules": [],
    "requestHeadersInserted": null,
    "responseCodeSent": null,
    "httpRequest": {
        "clientIp": "52.46.82.45",
        "country": "FR",
        "headers": [{
            "name": "X-Forwarded-For",
            "value": "52.46.82.45"
        }, {
            "name": "X-Forwarded-Proto",
            "value": "https"
        }, {
            "name": "X-Forwarded-Port",
            "value": "443"
        }, {
            "name": "Host",
            "value": "rjvegx5guh.execute-api.eu-west-3.amazonaws.com"
        }, {
            "name": "X-Amzn-Trace-Id",
            "value": "Root=1-645566cf-7cb058b04d9bb3ee01dc4036"
        }, {
            "name": "hoppy",
            "value": "zuomr2mxQxofg6EI6f7hMNGaJhhPxt0rFVAXog6FLxE="
        }, {
            "name": "User-Agent",
            "value": "RateBasedRuleTestKoipOneKeyModulePV2"
        }, {
            "name": "Accept-Encoding",
            "value": "gzip,deflate"
        }],
        "uri": "/CanaryTest",
        "args": "",
        "httpVersion": "HTTP/1.1",
        "httpMethod": "GET",
        "requestId": "Ed0AiHF_CGYF-DA="
    }
}
```

## Data protection for Body

AWS WAF only log subsets of Body in `RuleMatchDetails`.

Webacl config

```
 "data_protection_config": {
            "data_protections": [
                {
                    "field": {
                        "field_type": "BODY"
                    },
                    "action": "SUBSTITUTE",
                    "exclude_rule_match_details": false,
                    "exclude_rate_based_details": false
                }
             ]
           }
```

Example DataProtection for Body: Log entry with Body Subsituted in `ruleMatchDetails`.

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionhashACL/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [{
        "ruleId": "ProtectedSQLIBody",
        "action": "COUNT",
        "ruleMatchDetails": [{
            "conditionType": "SQL_INJECTION",
            "sensitivityLevel": "HIGH",
            "location": "BODY",
            "matchedData": ["REDACTED"]
        }]
    }],
    "requestHeadersInserted": null,
    "responseCodeSent": null,
    "httpRequest": {
        "clientIp": "54.239.98.137",
        "country": "US",
        "headers": [{
            "name": "X-Forwarded-For",
            "value": "54.239.98.137"
        }, {
            "name": "X-Forwarded-Proto",
            "value": "https"
        }, {
            "name": "X-Forwarded-Port",
            "value": "443"
        }, {
            "name": "Host",
            "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
        }, {
            "name": "X-Amzn-Trace-Id",
            "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
        }, {
            "name": "Accept-Encoding",
            "value": "gzip"
        }, {
            "name": "User-Agent",
            "value": "okhttp/3.12.1"
        }, {
            "name": "cookie",
            "value": "hoppy=dog;"
        }],
        "uri": "/CanaryTest",
        "args": "baloo=abc&hoppy-query=xyz&x-hoppy-extra=generic-%3Cwords%3E-in-angle-brackets",
        "httpVersion": "HTTP/1.1",
        "httpMethod": "GET",
        "requestId": "FepO0F8fIAMEqoQ="
    },
    "labels": [{
        "name": "awswaf:forwardedip:geo:country:US"
    }, {
        "name": "awswaf:forwardedip:geo:region:US-VA"
    }]
}
```

## Data protection for `SINGLE_COOKIE`

Webacl config

```
 "data_protection_config": {
            "data_protections": [
                {
                    "field": {
                        "field_type": "SINGLE_COOKIE",
                        "field_keys": [
                            "MILO"
                        ]
                    },
                    "action": "HASH",
                    "exclude_rule_match_details": false,
                    "exclude_rate_based_details": false
                }
             ]
           }
```

Example DataProtection for `SINGLE_COOKIE`: Log entry with a `SINGLE_COOKIE` named "MILO" protected.

The full Log shows the Cookie named MILO is protected in `ruleMatchDetails` and the cookie header. Only cookie values are protected and key names are excluded.

###### Note

All protected fields (single header, cookie, query arg) are not case sensitive. So, for this example, "MILO" matches "milo".

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionhashACL/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [{
        "ruleId": "ProtectedSQLIHeadersVisibleInSTM",
        "action": "COUNT",
        "ruleMatchDetails": [{
            "conditionType": "SQL_INJECTION",
            "sensitivityLevel": "HIGH",
            "location": "COOKIE",
            "matchedData": ["zuomr2mxQxofg6EI6f7hMNGaJhhPxt0rFVAXog6FLxE="],
            "matchedFieldName": "milo"
        }]
    }],
    "requestHeadersInserted": null,
    "responseCodeSent": null,
    "httpRequest": {
        "clientIp": "54.239.98.137",
        "country": "US",
        "headers": [{
            "name": "X-Forwarded-For",
            "value": "54.239.98.137"
        }, {
            "name": "X-Forwarded-Proto",
            "value": "https"
        }, {
            "name": "X-Forwarded-Port",
            "value": "443"
        }, {
            "name": "Host",
            "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
        }, {
            "name": "X-Amzn-Trace-Id",
            "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
        }, {
            "name": "Accept-Encoding",
            "value": "gzip"
        }, {
            "name": "User-Agent",
            "value": "okhttp/3.12.1"
        }, {
            "name": "cookie",
            "value": "hoppy=dog;milo=zuomr2mxQxofg6EI6f7hMNGaJhhPxt0rFVAXog6FLxE=;aws-waf-token=51c71352-41f5-4f6d-b676-c24907bdf819:EQoAZ/J+AAQAAAAA:t9wvxbw042wva7E2Y6lgud/bS6YG0CJKVAJqaRqDZ140ythKW0Zj9wKB2O8lSkYDRqf1yONcVBFo5u0eYi0tvT4rtQCXsu+KanAardW8go4QSLw4yoED59lgV7oAhGyCalAzE7ra29j+RvvZPsQyoQuDCrtoY/TvQyMTXIXzGPDC/rKBbg=="
        }],
        "uri": "/CanaryTest",
        "args": "baloo=abc&hoppy-query=xyz&x-hoppy-extra=generic-%3Cwords%3E-in-angle-brackets",
        "httpVersion": "HTTP/1.1",
        "httpMethod": "GET",
        "requestId": "FepO0F8fIAMEqoQ="
    },
    "labels": [{
        "name": "awswaf:forwardedip:geo:country:US"
    }, {
        "name": "awswaf:forwardedip:geo:region:US-VA"
    }]
}
```

## Data protection for all cookies

You can configure data protection for cookies by using `SINGLE_HEADER`. Only cookie values are protected and key names are excluded.

```
"DataProtectionConfig": {
    "DataProtections": [
        {
            "Field": {
                "FieldType": "SINGLE_HEADER",
                "FieldKeys": ["cookie"]
            },
            "Action": "SUBSTITUTION",
            "ExcludeRuleMatchDetails": false,
            "ExcludeRateBasedDetails": false
        }
    ]
}
```

Example DataProtection for the `header` "COOKIE": Log entry with the cookie header protected.

###### Note

The cookie name `AWS-WAF-TOKEN` is out of scope for data protection.

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionhashACL/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [],
    "requestHeadersInserted": null,
    "responseCodeSent": null,
    "httpRequest": {
        "clientIp": "54.239.98.137",
        "country": "US",
        "headers": [{
            "name": "X-Forwarded-For",
            "value": "54.239.98.137"
        }, {
            "name": "X-Forwarded-Proto",
            "value": "https"
        }, {
            "name": "X-Forwarded-Port",
            "value": "443"
        }, {
            "name": "Host",
            "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
        }, {
            "name": "X-Amzn-Trace-Id",
            "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
        }, {
            "name": "Accept-Encoding",
            "value": "gzip"
        }, {
            "name": "User-Agent",
            "value": "okhttp/3.12.1"
        }, {
            "name": "cookie",
            "value": "hoppy=REDACTED;milo=REDACTED;aws-waf-token=51c71352-41f5-4f6d-b676-c24907bdf819:EQoAZ/J+AAQAAAAA:t9wvxbw042wva7E2Y6lgud/bS6YG0CJKVAJqaRqDZ140ythKW0Zj9wKB2O8lSkYDRqf1yONcVBFo5u0eYi0tvT4rtQCXsu+KanAardW8go4QSLw4yoED59lgV7oAhGyCalAzE7ra29j+RvvZPsQyoQuDCrtoY/TvQyMTXIXzGPDC/rKBbg=="
        }],
        "uri": "/CanaryTest",
        "args": "baloo=xyz=&hoppy-query=abc&x-hoppy-extra=abc",
        "httpVersion": "HTTP/1.1",
        "httpMethod": "GET",
        "requestId": "FepO0F8fIAMEqoQ="
    },
    "labels": [{
        "name": "awswaf:forwardedip:geo:country:US"
    }, {
        "name": "awswaf:forwardedip:geo:region:US-VA"
    }]
}
```

## Data protection for single query arguments

You can configure data protection for a query string by using `SINGLE_QUERY_ARGUMENT`. This affects the keys and values of all query args. For the following examples, the original query string was `baloo=10 AND 1=1&hoppy=10 AND 1=1&x-hoppy-extra=generic-%3Cwords`.

Webacl config

```
"DataProtectionConfig": {
   "DataProtections": [
        {
            "Field": {
                "FieldType": "SINGLE_QUERY_ARGUMENT",
                "FieldKeys": ["hoppy"]
            },
            "Action": "SUBSTITUTION",
            "ExcludeRuleMatchDetails": false,
            "ExcludeRateBasedDetails": false
        }
    ]
}
```

Example DataProtection for `SINGLE_QUERY_ARGUEMENT`: Log entry with "hoppy" query string protected with substitution.

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionSubstituteQueryString/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [
      {
        "ruleId": "ProtectedHoppyQueryArg",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "SINGLE_QUERY_ARG",
                "matchedData": ["REDACTED"],
                "matchedFieldName": "hoppy"
            }]
      },
      {
        "ruleId": "FullQueryStringInspectionWhichDetectsTheFirstFieldWithSQLi_Baloo_IsAlsoMaskedMasked",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "QUERY_ARGS",
                "matchedData": ["REDACTED"],
            }]
      },
      {
        "ruleId": "ProtectedBalooQueryArg",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "SINGLE_QUERY_ARG",
                "matchedData": [ "10", "AND", "1" ],
                "matchedFieldName": "baloo"
            }]
      }
    ],
    "requestHeadersInserted": null,
    "responseCodeSent": null,
    "httpRequest": {
        "clientIp": "54.239.98.137",
        "country": "US",
        "headers": [{
            "name": "X-Forwarded-For",
            "value": "54.239.98.137"
        }, {
            "name": "X-Forwarded-Proto",
            "value": "https"
        }, {
            "name": "X-Forwarded-Port",
            "value": "443"
        }, {
            "name": "Host",
            "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
        }, {
            "name": "X-Amzn-Trace-Id",
            "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
        }, {
            "name": "Accept-Encoding",
            "value": "gzip"
        }, {
            "name": "User-Agent",
            "value": "okhttp/3.12.1"
        }],
        "uri": "/CanaryTest",
        "args": "baloo=10 AND 1=1&hoppy=REDACTED&x-hoppy-extra=generic-%3Cwords",
        "httpVersion": "HTTP/1.1",
        "httpMethod": "GET",
        "requestId": "FepO0F8fIAMEqoQ="
    },
    "labels": [{
        "name": "awswaf:forwardedip:geo:country:US"
    }, {
        "name": "awswaf:forwardedip:geo:region:US-VA"
    }]
}
```

## Data protection for query strings

You can configure data protection for a query string by using `QUERY_STRING`. This affects the keys and values of all query args. For the following examples, the original query string was `baloo=10 AND 1=1&hoppy-query=10 AND 1=1&x-hoppy-extra=generic-%3Cwords`.

Webacl config

```
"DataProtectionConfig": {
 "DataProtections": [
 {
 "Field": {
 "FieldType": "QUERY_STRING"
 },
 "Action": "SUBSTITUTION",
 "ExcludeRuleMatchDetails": false,
 "ExcludeRateBasedDetails": false
 }
 ]
}
```

Example DataProtection for `QUERY_STRING`: Log entry with query string protected with substitution.

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionSubstituteQueryString/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [
      {
        "ruleId": "ProtectedHoppyQueryArg",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "QUERY_STRING",
                "matchedData": ["REDACTED"]
            }]
      },
      {
        "ruleId": "ProtectedBalooQueryArg",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "SINGLE_QUERY_ARG",
                "matchedData": [ "REDACTED" ],
                "matchedFieldName": "REDACTED"
            }]
      }
    ],
    "requestHeadersInserted": null,
    "responseCodeSent": null,
    "httpRequest": {
        "clientIp": "54.239.98.137",
        "country": "US",
        "headers": [{
            "name": "X-Forwarded-For",
            "value": "54.239.98.137"
        }, {
            "name": "X-Forwarded-Proto",
            "value": "https"
        }, {
            "name": "X-Forwarded-Port",
            "value": "443"
        }, {
            "name": "Host",
            "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
        }, {
            "name": "X-Amzn-Trace-Id",
            "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
        }, {
            "name": "Accept-Encoding",
            "value": "gzip"
        }, {
            "name": "User-Agent",
            "value": "okhttp/3.12.1"
        }],
        "uri": "/CanaryTest",
        "args": "REDACTED",
        "httpVersion": "HTTP/1.1",
        "httpMethod": "GET",
        "requestId": "FepO0F8fIAMEqoQ="
    },
    "labels": [{
        "name": "awswaf:forwardedip:geo:country:US"
    }, {
        "name": "awswaf:forwardedip:geo:region:US-VA"
    }]
}
```

## Data protection for multiple query arguments

You can configure data protection for individual query args by using `SINGLE_QUERY_ARGUMENT`. When reporting local information we use local protections. However, strings that matched in query string and cookie header have many protection configs that could apply. To simplify, the strictest protection for `RuleMatchDetails` is applied, even if it doesn't overlap with the specific data range that matched.

For the following examples, the original query string was `baloo=is_a_good_boy&hoppy=likes_to_sleep&x-hoppy-extra=10 AND 1=1`.

```
"DataProtectionConfig": {
    "DataProtections": [
        {
            "Field": {
                "FieldType": "SINGLE_QUERY_ARGUMENT",
                "FieldKeys": ["hoppy"]
            },
            "Action": "SUBSTITUTION",
            "ExcludeRuleMatchDetails": false,
            "ExcludeRateBasedDetails": false
        },
        {
            "Field": {
                "FieldType": "SINGLE_QUERY_ARGUMENT",
                "FieldKeys": ["baloo"]
            },
            "Action": "HASH",
            "ExcludeRuleMatchDetails": false,
            "ExcludeRateBasedDetails": false
        }
    ]
}
```

Example DataProtection for multiple query arguments.

```
{
    "timestamp": 1738705092889,
    "formatVersion": 1,
    "webaclId": "arn:aws:wafv2:us-east-1:111122223333:regional/webacl/DataProtectionSubstituteQueryString/4eede063-e611-44f5-b357-ffc9d7b7fed5",
    "terminatingRuleId": "Default_Action",
    "terminatingRuleType": "REGULAR",
    "action": "ALLOW",
    "terminatingRuleMatchDetails": [],
    "httpSourceName": "APIGW",
    "httpSourceId": "746533260405:xt7v59bhn7:ABC",
    "ruleGroupList": [],
    "rateBasedRuleList": [],
    "nonTerminatingMatchingRules": [
      {
        "ruleId": "ProtectedHoppyQueryArg",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "SINGLE_QUERY_ARG",
                "matchedData": ["REDACTED"],
                "matchedFieldName": "hoppy"
            }]
      },
      {
        "ruleId": "ProtectedBalooQueryArg",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "SINGLE_QUERY_ARG",
                "matchedData": ["zuomr2mxQxofg6EI6f7hMNGaJhhPxt0rFVAXog6FLxE="],
                "matchedFieldName": "baloo"
            }]
      },
      {
        "ruleId": "FullQueryStringDetects_x-hoppy-extra_IsSubstituted",
        "action": "COUNT",
        "ruleMatchDetails": [
            {
                "conditionType": "SQL_INJECTION",
                "sensitivityLevel": "HIGH",
                "location": "QUERY_ARGS",
                "matchedData": ["REDACTED"],  // Harshest of Protection Config
            }]
      }
    ],
    "requestHeadersInserted": null,
    "responseCodeSent": null,
    "httpRequest": {
        "clientIp": "54.239.98.137",
        "country": "US",
        "headers": [{
            "name": "X-Forwarded-For",
            "value": "54.239.98.137"
        }, {
            "name": "X-Forwarded-Proto",
            "value": "https"
        }, {
            "name": "X-Forwarded-Port",
            "value": "443"
        }, {
            "name": "Host",
            "value": "xt7xxx9bhn7.gamma.execute-api.us-east-1.amazonaws.com"
        }, {
            "name": "X-Amzn-Trace-Id",
            "value": "Root=1-67a288c4-27acb3cd5795dd8456b7e3c3"
        }, {
            "name": "Accept-Encoding",
            "value": "gzip"
        }, {
            "name": "User-Agent",
            "value": "okhttp/3.12.1"
        }],
        "uri": "/CanaryTest",
        "args": "baloo=zuomr2mxQxofg6EI6f7hMNGaJhhPxt0rFVAXog6FLxE=&hoppy=REDACTED&x-hoppy-extra=10 AND 1=1",
        "httpVersion": "HTTP/1.1",
        "httpMethod": "GET",
        "requestId": "FepO0F8fIAMEqoQ="
    },
    "labels": [{
        "name": "awswaf:forwardedip:geo:country:US"
    }, {
        "name": "awswaf:forwardedip:geo:region:US-VA"
    }]
}
```

###### Note

You cannot specify both **QueryString Masking** and **Single Query Arg Masking** in the same webACL.
