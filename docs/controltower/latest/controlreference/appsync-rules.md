# AWS AppSync controls

###### Topics

- [[CT.APPSYNC.PR.1] Require an AWS AppSync GraphQL API to have logging enabled](#ct-appsync-pr-1-description "#ct-appsync-pr-1-description")
- [[CT.APPSYNC.PR.2] Require an AWS AppSync GraphQL API to be configured with private visibility](#ct-appsync-pr-2-description "#ct-appsync-pr-2-description")
- [[CT.APPSYNC.PR.3] Require that an AWS AppSync GraphQL API is not authenticated with API keys](#ct-appsync-pr-3-description "#ct-appsync-pr-3-description")
- [[CT.APPSYNC.PR.4] Require an AWS AppSync GraphQL API cache to have encryption in transit enabled.](#ct-appsync-pr-4-description "#ct-appsync-pr-4-description")
- [[CT.APPSYNC.PR.5] Require an AWS AppSync GraphQL API cache to have encryption at rest enabled.](#ct-appsync-pr-5-description "#ct-appsync-pr-5-description")

## [CT.APPSYNC.PR.1] Require an AWS AppSync GraphQL API to have logging enabled

This control checks whether an AWS AppSync GraphQL API has been configured to send request-level and field-level logs to Amazon CloudWatch Logs.

- **Control objective:** Establish logging and monitoring
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AppSync::GraphQLApi`
- **CloudFormation guard rule:**
  [CT.APPSYNC.PR.1 rule specification](#ct-appsync-pr-1-rule "#ct-appsync-pr-1-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.APPSYNC.PR.1 rule specification](#ct-appsync-pr-1-rule "#ct-appsync-pr-1-rule")
- For examples of PASS and FAIL CloudFormation templates related to
  this control, see:
  [CT.APPSYNC.PR.1 example templates](#ct-appsync-pr-1-templates "#ct-appsync-pr-1-templates")

**Explanation**

AppSync logs are useful for debugging issues related to requests.

### Remediation for rule failure

Within `LogConfig`, set `FieldLogLevel` to `ERROR`, `INFO`, `DEBUG`, or `ALL` and set `CloudWatchLogsRoleArn` to the ARN of an AWS IAM role configured to allow AWS AppSync to send logs to Amazon CloudWatch Logs.

The examples that follow show how to implement this remediation.

#### AWS AppSync GraphQL API - Example

An AWS AppSync GraphQL API configured to send GraphQL operations and tracing to Amazon CloudWatch Logs. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "GraphQLApi": {
        "Type": "AWS::AppSync::GraphQLApi",
        "Properties": {
            "Name": "SampleApi",
            "AuthenticationType": "AWS_IAM",
            "LogConfig": {
                "FieldLogLevel": "ALL",
                "CloudWatchLogsRoleArn": {
                    "Fn::GetAtt": [
                        "AppSyncLoggingRole",
                        "Arn"
                    ]
                }
            }
        }
    }
}

```

**YAML example**

```

GraphQLApi:
  Type: AWS::AppSync::GraphQLApi
  Properties:
    Name: SampleApi
    AuthenticationType: AWS_IAM
    LogConfig:
      FieldLogLevel: ALL
      CloudWatchLogsRoleArn: !GetAtt 'AppSyncLoggingRole.Arn'


```

### CT.APPSYNC.PR.1 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   appsync_logging_enabled_check
#
# Description:
#   This control checks whether an AWS AppSync GraphQL API has been configured to send request-level and field-level logs to Amazon CloudWatch Logs.
#
# Reports on:
#   AWS::AppSync::GraphQLApi
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any AppSync GraphQL API resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AppSync GraphQL API resource
#       And: 'LogConfig' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AppSync GraphQL API resource
#       And: 'LogConfig' has been provided
#       And: 'FieldLogLevel' in 'LogConfig' has not been provided or provided and set to a value other
#            than 'ERROR', 'INFO', 'DEBUG', or 'ALL'
#       And: 'CloudWatchLogsRoleArn' in 'LogConfig' has not been provided or provided and set to an empty
#            string or invalid local reference
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AppSync GraphQL API resource
#       And: 'LogConfig' has been provided
#       And: 'FieldLogLevel' in 'LogConfig' has been provided and set to 'ERROR', 'INFO', 'DEBUG' or 'ALL'
#       And: 'CloudWatchLogsRoleArn' in 'LogConfig' has not been provided or provided and set to an empty
#            string or invalid local reference
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AppSync GraphQL API resource
#       And: 'LogConfig' has been provided
#       And: 'FieldLogLevel' in 'LogConfig' has not been provided or provided and set to a value other
#            than 'ERROR', 'INFO', 'DEBUG', or 'ALL'
#       And: 'CloudWatchLogsRoleArn' in 'LogConfig' has been provided and set to a non-empty string or valid
#            local reference
#      Then: FAIL
#   Scenario: 6
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AppSync GraphQL API resource
#       And: 'LogConfig' has been provided
#       And: 'FieldLogLevel' in 'LogConfig' has been provided and set to 'ERROR', 'INFO', 'DEBUG', or 'ALL'
#       And: 'CloudWatchLogsRoleArn' in 'LogConfig' has been provided and set to a non-empty string or valid
#            local reference
#      Then: PASS

#
# Constants
#
let APPSYNC_GRAPHQL_API_TYPE = "AWS::AppSync::GraphQLApi"
let ALLOWED_APPSYNC_LOG_LEVELS = [ "ERROR",  'INFO', 'DEBUG', "ALL" ]
let INPUT_DOCUMENT = this

#
# Assignments
#
let appsync_graphql_apis = Resources.*[ Type == %APPSYNC_GRAPHQL_API_TYPE ]

#
# Primary Rules
#
rule appsync_logging_enabled_check when is_cfn_template(%INPUT_DOCUMENT)
                                        %appsync_graphql_apis not empty {
    check(%appsync_graphql_apis.Properties)
        <<
        [CT.APPSYNC.PR.1]: Require an AWS AppSync GraphQL API to have logging enabled
        [FIX]: Within 'LogConfig', set 'FieldLogLevel' to 'ALL', 'INFO', 'DEBUG', or 'ERROR' and set 'CloudWatchLogsRoleArn' to the ARN of an AWS IAM role configured to allow AWS AppSync to send logs to Amazon CloudWatch Logs.
        >>
}

rule appsync_logging_enabled_check when is_cfn_hook(%INPUT_DOCUMENT, %APPSYNC_GRAPHQL_API_TYPE) {
    check(%INPUT_DOCUMENT.%APPSYNC_GRAPHQL_API_TYPE.resourceProperties)
        <<
        [CT.APPSYNC.PR.1]: Require an AWS AppSync GraphQL API to have logging enabled
        [FIX]: Within 'LogConfig', set 'FieldLogLevel' to 'ALL', 'INFO', 'DEBUG', or 'ERROR' and set 'CloudWatchLogsRoleArn' to the ARN of an AWS IAM role configured to allow AWS AppSync to send logs to Amazon CloudWatch Logs.
        >>
}

#
# Parameterized Rules
#
rule check(appsync_graphql_api) {
    %appsync_graphql_api {
        # Scenario 2
        LogConfig exists
        LogConfig is_struct

        LogConfig {
            # Scenarios 3, 4, 5 and 6
            FieldLogLevel exists
            FieldLogLevel in %ALLOWED_APPSYNC_LOG_LEVELS

            CloudWatchLogsRoleArn exists
            check_is_string_and_not_empty(CloudWatchLogsRoleArn) or
            check_local_references(%INPUT_DOCUMENT, CloudWatchLogsRoleArn, "AWS::IAM::Role")
        }
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}

rule check_is_string_and_not_empty(value) {
    %value {
        this is_string
        this != /\A\s*\z/
    }
}

rule check_local_references(doc, reference_properties, referenced_resource_type) {
    %reference_properties {
        'Fn::GetAtt' {
            query_for_resource(%doc, this[0], %referenced_resource_type)
                <<Local Stack reference was invalid>>
        } or Ref {
            query_for_resource(%doc, this, %referenced_resource_type)
                <<Local Stack reference was invalid>>
        }
    }
}

rule query_for_resource(doc, resource_key, referenced_resource_type) {
    let referenced_resource = %doc.Resources[ keys == %resource_key ]
    %referenced_resource not empty
    %referenced_resource {
        Type == %referenced_resource_type
    }
}


```

### CT.APPSYNC.PR.1 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
      LogConfig:
        FieldLogLevel: ALL
        CloudWatchLogsRoleArn:
          Fn::GetAtt:
          - AppSyncLoggingRole
          - Arn
  AppSyncLoggingRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - appsync.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: AppSyncLoggingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
      LogConfig:
        FieldLogLevel: NONE
        CloudWatchLogsRoleArn:
          Fn::GetAtt:
          - AppSyncLoggingRole
          - Arn
  AppSyncLoggingRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - appsync.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: /
      Policies:
      - PolicyName: AppSyncLoggingPolicy
        PolicyDocument:
          Version: '2012-10-17		 	 	 '
          Statement:
          - Effect: Allow
            Action:
            - logs:CreateLogGroup
            - logs:CreateLogStream
            - logs:PutLogEvents
            Resource: '*'


```

## [CT.APPSYNC.PR.2] Require an AWS AppSync GraphQL API to be configured with private visibility

This control checks whether an AWS AppSync GraphQL API has been configured with private visibility.

- **Control objective:** Limit network access
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AppSync::GraphQLApi`
- **CloudFormation guard rule:**
  [CT.APPSYNC.PR.2 rule specification](#ct-appsync-pr-2-rule "#ct-appsync-pr-2-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.APPSYNC.PR.2 rule specification](#ct-appsync-pr-2-rule "#ct-appsync-pr-2-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.APPSYNC.PR.2 example templates](#ct-appsync-pr-2-templates "#ct-appsync-pr-2-templates")

**Explanation**

If you use Amazon Virtual Private Cloud (Amazon VPC), you can create AWS AppSync Private APIs, which are APIs that are accessible only from a Amazon VPC.
With a Private API, you can restrict API access to your internal applications and connect to your GraphQL and Realtime endpoints without
exposing data publicly.

###### Usage considerations

- This control requires AWS AppSync GraphQL APIs to be configured with private API features, so that they are accessible
  only from a Amazon VPC. If you require your AWS AppSync GraphQL APIs to be accessible from an AWS AppSync public endpoint,
  do not enable this control.

### Remediation for rule failure

Set the Visibility property to PRIVATE.

The examples that follow show how to implement this remediation.

#### AWS AppSync Private API - Example

An AWS AppSync GraphQL API configured with private visibility. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "GraphQLApi": {
        "Type": "AWS::AppSync::GraphQLApi",
        "Properties": {
            "Name": "SampleApi",
            "AuthenticationType": "AWS_IAM",
            "Visibility": "PRIVATE"
        }
    }
}

```

**YAML example**

```

GraphQLApi:
  Type: AWS::AppSync::GraphQLApi
  Properties:
    Name: SampleApi
    AuthenticationType: AWS_IAM
    Visibility: PRIVATE


```

### CT.APPSYNC.PR.2 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   appsync_api_private_visibility_check
#
# Description:
#   This control checks whether an AWS AppSync GraphQL API has been configured with private visibility.
#
# Reports on:
#   AWS::AppSync::GraphQLApi
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any AWS AppSync GraphQL API resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'Visibility' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'Visibility' has been provided and set to a value other than 'PRIVATE'
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'Visibility' has been provided and set to 'PRIVATE'
#      Then: PASS

#
# Constants
#
let APPSYNC_GRAPHQL_API_TYPE = "AWS::AppSync::GraphQLApi"
let ALLOWED_VISIBILITY_LEVELS = [ "PRIVATE" ]
let INPUT_DOCUMENT = this

#
# Assignments
#
let appsync_graphql_apis = Resources.*[ Type == %APPSYNC_GRAPHQL_API_TYPE ]

#
# Primary Rules
#
rule appsync_api_private_visibility_check when is_cfn_template(%INPUT_DOCUMENT)
                                               %appsync_graphql_apis not empty {
    check(%appsync_graphql_apis.Properties)
        <<
        [CT.APPSYNC.PR.2]: Require an AWS AppSync GraphQL API to be configured with private visibility
        [FIX]: Set the Visibility property to PRIVATE.
        >>
}

rule appsync_api_private_visibility_check when is_cfn_hook(%INPUT_DOCUMENT, %APPSYNC_GRAPHQL_API_TYPE) {
    check(%INPUT_DOCUMENT.%APPSYNC_GRAPHQL_API_TYPE.resourceProperties)
        <<
        [CT.APPSYNC.PR.2]: Require an AWS AppSync GraphQL API to be configured with private visibility
        [FIX]: Set the Visibility property to PRIVATE.
        >>
}

#
# Parameterized Rules
#
rule check(appsync_graphql_api) {
    %appsync_graphql_api {
        # Scenario 2
        Visibility exists
        # Scenarios 3 and 4
        Visibility in %ALLOWED_VISIBILITY_LEVELS
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.APPSYNC.PR.2 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
      Visibility: PRIVATE


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
      Visibility: GLOBAL


```

## [CT.APPSYNC.PR.3] Require that an AWS AppSync GraphQL API is not authenticated with API keys

This control checks that an AWS AppSync GraphQL API has been configured with an authentication type other than API_KEY authentication.

- **Control objective:** Enforce least privilege
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AppSync::GraphQLApi`
- **CloudFormation guard rule:**
  [CT.APPSYNC.PR.3 rule specification](#ct-appsync-pr-3-rule "#ct-appsync-pr-3-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.APPSYNC.PR.3 rule specification](#ct-appsync-pr-3-rule "#ct-appsync-pr-3-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.APPSYNC.PR.3 example templates](#ct-appsync-pr-3-templates "#ct-appsync-pr-3-templates")

**Explanation**

One way to control throttling for unauthenticated GraphQL endpoints is through the use of API keys.
API keys are recommended only for development purposes, or in scenarios where it is safe to expose a public API.
If static API keys are stolen, an API can become vulnerable to replay attacks.

### Remediation for rule failure

Set the AuthenticationType property to a value other than API_KEY, and ensure no entry in the AdditionalAuthenticationProviders property has an AuthenticationType value of API_KEY.

The examples that follow show how to implement this remediation.

#### AWS AppSync GraphQL API - Example

An AWS AppSync GraphQL API configured with IAM authorization. The example is shown in JSON and
in YAML.

**JSON example**

```

{
    "GraphQLApi": {
        "Type": "AWS::AppSync::GraphQLApi",
        "Properties": {
            "Name": "SampleApi",
            "AuthenticationType": "AWS_IAM"
        }
    }
}

```

**YAML example**

```

GraphQLApi:
  Type: AWS::AppSync::GraphQLApi
  Properties:
    Name: SampleApi
    AuthenticationType: AWS_IAM


```

### CT.APPSYNC.PR.3 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   appsync_authorization_check
#
# Description:
#   This control checks that an AWS AppSync GraphQL API has been configured with an authentication type other than API_KEY authentication.
#
# Reports on:
#   AWS::AppSync::GraphQLApi
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any AWS AppSync GraphQL API resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'AuthenticationType' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'AuthenticationType' has been provided and is equal to 'API_KEY'
#       And: 'AdditionalAuthenticationProviders' has not been provided or provided as an empty list
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'AuthenticationType' has been provided and is equal to a value other than 'API_KEY'
#       And: 'AdditionalAuthenticationProviders' has been provided as a non-empty list
#       And: An entry in 'AdditionalAuthenticationProviders' has 'AuthenticationType' equal to 'API_KEY'
#      Then: FAIL
#   Scenario: 5
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'AuthenticationType' has been provided and is equal to a value other than 'API_KEY'
#       And: 'AdditionalAuthenticationProviders' has not been provided or provided as an empty list
#      Then: PASS
#   Scenario: 6
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API resource
#       And: 'AuthenticationType' has been provided and is equal to a value other than 'API_KEY'
#       And: 'AdditionalAuthenticationProviders' has been provided as a non-empty list
#       And: No entries in 'AdditionalAuthenticationProviders' have 'AuthenticationType' equal to 'API_KEY'
#      Then: PASS

#
# Constants
#
let APPSYNC_GRAPHQL_API_TYPE = "AWS::AppSync::GraphQLApi"
let DISALLOWED_AUTHORIZATION_TYPES = [ "API_KEY" ]
let INPUT_DOCUMENT = this

#
# Assignments
#
let appsync_graphql_apis = Resources.*[ Type == %APPSYNC_GRAPHQL_API_TYPE ]

#
# Primary Rules
#
rule appsync_authorization_check when is_cfn_template(%INPUT_DOCUMENT)
                                      %appsync_graphql_apis not empty {
    check(%appsync_graphql_apis.Properties)
        <<
        [CT.APPSYNC.PR.3]: Require that an AWS AppSync GraphQL API is not authenticated with API keys
        [FIX]: Set the AuthenticationType property to a value other than API_KEY, and ensure no entry in the AdditionalAuthenticationProviders property has an AuthenticationType value of API_KEY.
        >>
}

rule appsync_authorization_check when is_cfn_hook(%INPUT_DOCUMENT, %APPSYNC_GRAPHQL_API_TYPE) {
    check(%INPUT_DOCUMENT.%APPSYNC_GRAPHQL_API_TYPE.resourceProperties)
        <<
        [CT.APPSYNC.PR.3]: Require that an AWS AppSync GraphQL API is not authenticated with API keys
        [FIX]: Set the AuthenticationType property to a value other than API_KEY, and ensure no entry in the AdditionalAuthenticationProviders property has an AuthenticationType value of API_KEY.
        >>
}

#
# Parameterized Rules
#
rule check(appsync_graphql_api) {
    %appsync_graphql_api {
        # Scenarios 2, 3 and 5
        check_authentication_type(this)
    }

    %appsync_graphql_api [
        AdditionalAuthenticationProviders exists
        AdditionalAuthenticationProviders is_list
        AdditionalAuthenticationProviders not empty
    ] {
        AdditionalAuthenticationProviders[*] {
            # Scenarios 4 and 6
            check_authentication_type(this)
        }
    }
}

rule check_authentication_type(appsync_configuration) {
    %appsync_configuration {
        AuthenticationType exists
        AuthenticationType not in %DISALLOWED_AUTHORIZATION_TYPES
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.APPSYNC.PR.3 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM


```

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
      AdditionalAuthenticationProviders:
      - AuthenticationType: OPENID_CONNECT
        OpenIDConnectConfig:
          Issuer: https://example.com/


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: API_KEY


```

## [CT.APPSYNC.PR.4] Require an AWS AppSync GraphQL API cache to have encryption in transit enabled.

This control checks whether an AWS AppSync API cache has encryption in transit enabled.

- **Control objective:** Encrypt data in transit
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AppSync::ApiCache`
- **CloudFormation guard rule:**
  [CT.APPSYNC.PR.4 rule specification](#ct-appsync-pr-4-rule "#ct-appsync-pr-4-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.APPSYNC.PR.4 rule specification](#ct-appsync-pr-4-rule "#ct-appsync-pr-4-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.APPSYNC.PR.4 example templates](#ct-appsync-pr-4-templates "#ct-appsync-pr-4-templates")

**Explanation**

Enabling this feature ensures that requests between AWS AppSync, the cache, and the data sources (except insecure HTTP data sources)
are encrypted at the network level. Because some processing is needed to encrypt and decrypt the data at the endpoints,
in-transit encryption can affect performance.

### Remediation for rule failure

Set the value of the TransitEncryptionEnabled property to true.

The examples that follow show how to implement this remediation.

#### AWS AppSync GraphQL API Cache - Example

An AWS AppSync GraphQL API cache configured with encryption in transit enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "GraphQLApiCache": {
        "Type": "AWS::AppSync::ApiCache",
        "Properties": {
            "ApiId": {
                "Fn::GetAtt": "GraphQLApi.ApiId"
            },
            "Type": "SMALL",
            "ApiCachingBehavior": "FULL_REQUEST_CACHING",
            "Ttl": 1200,
            "TransitEncryptionEnabled": true
        }
    }
}

```

**YAML example**

```

GraphQLApiCache:
  Type: AWS::AppSync::ApiCache
  Properties:
    ApiId: !GetAtt 'GraphQLApi.ApiId'
    Type: SMALL
    ApiCachingBehavior: FULL_REQUEST_CACHING
    Ttl: 1200
    TransitEncryptionEnabled: true


```

### CT.APPSYNC.PR.4 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   appsync_cache_encryption_in_transit_check
#
# Description:
#   This control checks whether an AWS AppSync API cache has encryption in transit enabled.
#
# Reports on:
#   AWS::AppSync::ApiCache
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any AWS AppSync GraphQL API cache resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API cache resource
#       And: 'TransitEncryptionEnabled' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API cache resource
#       And: 'TransitEncryptionEnabled' been provided and is equal to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API cache resource
#       And: 'TransitEncryptionEnabled' been provided and is equal to bool(true)
#      Then: PASS

#
# Constants
#
let APPSYNC_GRAPHQL_API_CACHE_TYPE = "AWS::AppSync::ApiCache"
let INPUT_DOCUMENT = this

#
# Assignments
#
let appsync_graphql_api_caches = Resources.*[ Type == %APPSYNC_GRAPHQL_API_CACHE_TYPE ]

#
# Primary Rules
#
rule appsync_cache_encryption_in_transit_check when is_cfn_template(%INPUT_DOCUMENT)
                                                    %appsync_graphql_api_caches not empty {
    check(%appsync_graphql_api_caches.Properties)
        <<
        [CT.APPSYNC.PR.4]: Require an AWS AppSync GraphQL API cache to have encryption in transit enabled.
        [FIX]: Set the value of the TransitEncryptionEnabled property to true.
        >>
}

rule appsync_cache_encryption_in_transit_check when is_cfn_hook(%INPUT_DOCUMENT, %APPSYNC_GRAPHQL_API_CACHE_TYPE) {
    check(%INPUT_DOCUMENT.%APPSYNC_GRAPHQL_API_CACHE_TYPE.resourceProperties)
        <<
        [CT.APPSYNC.PR.4]: Require an AWS AppSync GraphQL API cache to have encryption in transit enabled.
        [FIX]: Set the value of the TransitEncryptionEnabled property to true.
        >>
}

#
# Parameterized Rules
#
rule check(appsync_graphql_api_cache) {
    %appsync_graphql_api_cache {
        # Scenario 2
        TransitEncryptionEnabled exists
        # Scenarios 3 and 4
        TransitEncryptionEnabled == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.APPSYNC.PR.4 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
  GraphQLApiCache:
    Type: AWS::AppSync::ApiCache
    Properties:
      ApiId:
        Fn::GetAtt: GraphQLApi.ApiId
      Type: SMALL
      ApiCachingBehavior: FULL_REQUEST_CACHING
      Ttl: 1200
      TransitEncryptionEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
  GraphQLApiCache:
    Type: AWS::AppSync::ApiCache
    Properties:
      ApiId:
        Fn::GetAtt: GraphQLApi.ApiId
      Type: SMALL
      ApiCachingBehavior: FULL_REQUEST_CACHING
      Ttl: 1200
      TransitEncryptionEnabled: false


```

## [CT.APPSYNC.PR.5] Require an AWS AppSync GraphQL API cache to have encryption at rest enabled.

This control checks whether an AWS AppSync API cache has encryption at rest enabled.

- **Control objective:** Encrypt data at rest
- **Implementation:** CloudFormation guard rule
- **Control behavior:** Proactive
- **Resource types:** `AWS::AppSync::ApiCache`
- **CloudFormation guard rule:**
  [CT.APPSYNC.PR.5 rule specification](#ct-appsync-pr-5-rule "#ct-appsync-pr-5-rule")

**Details and examples**

- For details about the PASS, FAIL, and SKIP behaviors associated with
  this control, see the:
  [CT.APPSYNC.PR.5 rule specification](#ct-appsync-pr-5-rule "#ct-appsync-pr-5-rule")
- For examples of PASS and FAIL CloudFormation Templates related to
  this control, see:
  [CT.APPSYNC.PR.5 example templates](#ct-appsync-pr-5-templates "#ct-appsync-pr-5-templates")

**Explanation**

Data saved to disk from memory during swap operations is encrypted at the cache instance. Protecting data at rest is an important
security best practice. It can mitigate the risk associated with unintended data exposure.

### Remediation for rule failure

Set the value of the AtRestEncryptionEnabled property to true.

The examples that follow show how to implement this remediation.

#### AWS AppSync GraphQL API Cache - Example

An AWS AppSync GraphQL API cache configured with encryption at rest enabled. The example is shown in JSON and in YAML.

**JSON example**

```

{
    "GraphQLApiCache": {
        "Type": "AWS::AppSync::ApiCache",
        "Properties": {
            "ApiId": {
                "Fn::GetAtt": "GraphQLApi.ApiId"
            },
            "Type": "SMALL",
            "ApiCachingBehavior": "FULL_REQUEST_CACHING",
            "Ttl": 1200,
            "AtRestEncryptionEnabled": true
        }
    }
}

```

**YAML example**

```

GraphQLApiCache:
  Type: AWS::AppSync::ApiCache
  Properties:
    ApiId: !GetAtt 'GraphQLApi.ApiId'
    Type: SMALL
    ApiCachingBehavior: FULL_REQUEST_CACHING
    Ttl: 1200
    AtRestEncryptionEnabled: true


```

### CT.APPSYNC.PR.5 rule specification

```

# ###################################
##       Rule Specification        ##
#####################################
#
# Rule Identifier:
#   appsync_cache_encryption_at_rest_check
#
# Description:
#   This control checks whether an AWS AppSync API cache has encryption at rest enabled.
#
# Reports on:
#   AWS::AppSync::ApiCache
#
# Evaluates:
#   CloudFormation, CloudFormation hook
#
# Rule Parameters:
#   None
#
# Scenarios:
#   Scenario: 1
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document does not contain any AWS AppSync GraphQL API cache resources
#      Then: SKIP
#   Scenario: 2
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API cache resource
#       And: 'AtRestEncryptionEnabled' has not been provided
#      Then: FAIL
#   Scenario: 3
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API cache resource
#       And: 'AtRestEncryptionEnabled' been provided and is equal to a value other than bool(true)
#      Then: FAIL
#   Scenario: 4
#     Given: The input document is an CloudFormation or CloudFormation hook document
#       And: The input document contains an AWS AppSync GraphQL API cache resource
#       And: 'AtRestEncryptionEnabled' been provided and is equal to bool(true)
#      Then: PASS

#
# Constants
#
let APPSYNC_GRAPHQL_API_CACHE_TYPE = "AWS::AppSync::ApiCache"
let INPUT_DOCUMENT = this

#
# Assignments
#
let appsync_graphql_api_caches = Resources.*[ Type == %APPSYNC_GRAPHQL_API_CACHE_TYPE ]

#
# Primary Rules
#
rule appsync_cache_encryption_at_rest_check when is_cfn_template(%INPUT_DOCUMENT)
                                                 %appsync_graphql_api_caches not empty {
    check(%appsync_graphql_api_caches.Properties)
        <<
        [CT.APPSYNC.PR.5]: Require an AWS AppSync GraphQL API cache to have encryption at rest enabled.
        [FIX]: Set the value of the AtRestEncryptionEnabled property to true.
        >>
}

rule appsync_cache_encryption_at_rest_check when is_cfn_hook(%INPUT_DOCUMENT, %APPSYNC_GRAPHQL_API_CACHE_TYPE) {
    check(%INPUT_DOCUMENT.%APPSYNC_GRAPHQL_API_CACHE_TYPE.resourceProperties)
        <<
        [CT.APPSYNC.PR.5]: Require an AWS AppSync GraphQL API cache to have encryption at rest enabled.
        [FIX]: Set the value of the AtRestEncryptionEnabled property to true.
        >>
}

#
# Parameterized Rules
#
rule check(appsync_graphql_api_cache) {
    %appsync_graphql_api_cache {
        # Scenario 2
        AtRestEncryptionEnabled exists
        # Scenarios 3 and 4
        AtRestEncryptionEnabled == true
    }
}

#
# Utility Rules
#
rule is_cfn_template(doc) {
    %doc {
        AWSTemplateFormatVersion exists  or
        Resources exists
    }
}

rule is_cfn_hook(doc, RESOURCE_TYPE) {
    %doc.%RESOURCE_TYPE.resourceProperties exists
}


```

### CT.APPSYNC.PR.5 example templates

You can view examples of the PASS and FAIL test artifacts for the AWS Control Tower proactive controls.

PASS Example - Use this template to verify a compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
  GraphQLApiCache:
    Type: AWS::AppSync::ApiCache
    Properties:
      ApiId:
        Fn::GetAtt: GraphQLApi.ApiId
      Type: SMALL
      ApiCachingBehavior: FULL_REQUEST_CACHING
      Ttl: 1200
      AtRestEncryptionEnabled: true


```

FAIL Example - Use this template to verify that the control prevents non-compliant resource creation.

```

Resources:
  GraphQLApi:
    Type: AWS::AppSync::GraphQLApi
    Properties:
      Name:
        Fn::Sub: ${AWS::StackName}-example
      AuthenticationType: AWS_IAM
  GraphQLApiCache:
    Type: AWS::AppSync::ApiCache
    Properties:
      ApiId:
        Fn::GetAtt: GraphQLApi.ApiId
      Type: SMALL
      ApiCachingBehavior: FULL_REQUEST_CACHING
      Ttl: 1200
      AtRestEncryptionEnabled: false


```
