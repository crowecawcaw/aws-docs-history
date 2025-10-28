# Creating AWS Config Custom Lambda

Rules

You can develop custom rules and add them to AWS Config with AWS Lambda functions.

You associate
each custom rule with an Lambda function, which contains the logic that evaluates whether
your AWS resources comply with the rule. You associate this function with your rule, and
the rule invokes the function either in response to configuration changes or periodically.
The function then evaluates whether your resources comply with your rule, and sends its
evaluation results to AWS Config.

The AWS Rule Development Kit (RDK) is designed to support a "Compliance-as-Code" workflow that is intuitive and productive. It abstracts away much of the undifferentiated heavy lifting associated with
deploying AWS Config rules backed by custom Lambda functions, and provides a streamlined develop-deploy-monitor iterative process.

For step-by-step instruction, see the [AWS Rule Development Kit (RDK) Documentation](https://aws-config-rdk.readthedocs.io/en/master "https://aws-config-rdk.readthedocs.io/en/master").

AWS Lambda executes functions in response to events that are published by AWS services.
The function for an AWS Config Custom Lambda rule receives an event that is published by AWS Config, and
the function then uses data that it receives from the event and that it retrieves from the
AWS Config API to evaluate the compliance of the rule. The operations in a function for a Config
rule differ depending on whether it performs an evaluation that is triggered by
configuration changes or triggered periodically.

For information about common patterns within AWS Lambda functions, see [Programming Model](../../../lambda/latest/dg/programming-model-v2.md "../../../lambda/latest/dg/programming-model-v2.md") in the
_AWS Lambda Developer Guide_.

Example Function for Evaluations Triggered by
Configuration Changes AWS Config will invoke a function like the following example when it detects a configuration
change for a resource that is within a custom rule's scope.

If you use the AWS Config console to create a rule that is associated with a function like
this example, choose **Configuration changes** as the trigger type. If
you use the AWS Config API or AWS CLI to create the rule, set the `MessageType`
attribute to `ConfigurationItemChangeNotification` and
`OversizedConfigurationItemChangeNotification`. These settings enable
your rule to be triggered whenever AWS Config generates a configuration item or an oversized
configuration item as a result of a resource change.

This example evaluates your resources and checks whether the instances match the
resource type, `AWS::EC2::Instance`. The rule is triggered when AWS Config
generates a configuration item or an oversized configuration item notification.

```
'use strict';

import { ConfigServiceClient, GetResourceConfigHistoryCommand, PutEvaluationsCommand } from "@aws-sdk/client-config-service";

const configClient = new ConfigServiceClient({});

// Helper function used to validate input
function checkDefined(reference, referenceName) {
    if (!reference) {
        throw new Error(`Error: ${referenceName} is not defined`);
    }
    return reference;
}

// Check whether the message type is OversizedConfigurationItemChangeNotification,
function isOverSizedChangeNotification(messageType) {
    checkDefined(messageType, 'messageType');
    return messageType === 'OversizedConfigurationItemChangeNotification';
}

// Get the configurationItem for the resource using the getResourceConfigHistory API.
async function getConfiguration(resourceType, resourceId, configurationCaptureTime, callback) {
    const input = { resourceType, resourceId, laterTime: new Date(configurationCaptureTime), limit: 1 };
    const command = new GetResourceConfigHistoryCommand(input);
    await configClient.send(command).then(
        (data) => {
            callback(null, data.configurationItems[0]);
        },
        (error) => {
            callback(error, null);
        }
    );

}

// Convert the oversized configuration item from the API model to the original invocation model.
function convertApiConfiguration(apiConfiguration) {
    apiConfiguration.awsAccountId = apiConfiguration.accountId;
    apiConfiguration.ARN = apiConfiguration.arn;
    apiConfiguration.configurationStateMd5Hash = apiConfiguration.configurationItemMD5Hash;
    apiConfiguration.configurationItemVersion = apiConfiguration.version;
    apiConfiguration.configuration = JSON.parse(apiConfiguration.configuration);
    if ({}.hasOwnProperty.call(apiConfiguration, 'relationships')) {
        for (let i = 0; i < apiConfiguration.relationships.length; i++) {
            apiConfiguration.relationships[i].name = apiConfiguration.relationships[i].relationshipName;
        }
    }
    return apiConfiguration;
}

// Based on the message type, get the configuration item either from the configurationItem object in the invoking event or with the getResourceConfigHistory API in the getConfiguration function.
async function getConfigurationItem(invokingEvent, callback) {
    checkDefined(invokingEvent, 'invokingEvent');
    if (isOverSizedChangeNotification(invokingEvent.messageType)) {
        const configurationItemSummary = checkDefined(invokingEvent.configurationItemSummary, 'configurationItemSummary');
        await getConfiguration(configurationItemSummary.resourceType, configurationItemSummary.resourceId, configurationItemSummary.configurationItemCaptureTime, (err, apiConfigurationItem) => {
            if (err) {
                callback(err);
            }
            const configurationItem = convertApiConfiguration(apiConfigurationItem);
            callback(null, configurationItem);
        });
    } else {
        checkDefined(invokingEvent.configurationItem, 'configurationItem');
        callback(null, invokingEvent.configurationItem);
    }
}

// Check whether the resource has been deleted. If the resource was deleted, then the evaluation returns not applicable.
function isApplicable(configurationItem, event) {
    checkDefined(configurationItem, 'configurationItem');
    checkDefined(event, 'event');
    const status = configurationItem.configurationItemStatus;
    const eventLeftScope = event.eventLeftScope;
    return (status === 'OK' || status === 'ResourceDiscovered') && eventLeftScope === false;
}

// In this example, the resource is compliant if it is an instance and its type matches the type specified as the desired type.
// If the resource is not an instance, then this resource is not applicable.
function evaluateChangeNotificationCompliance(configurationItem, ruleParameters) {
    checkDefined(configurationItem, 'configurationItem');
    checkDefined(configurationItem.configuration, 'configurationItem.configuration');
    checkDefined(ruleParameters, 'ruleParameters');

    if (configurationItem.resourceType !== 'AWS::EC2::Instance') {
        return 'NOT_APPLICABLE';
    } else if (ruleParameters.desiredInstanceType === configurationItem.configuration.instanceType) {
        return 'COMPLIANT';
    }
    return 'NON_COMPLIANT';
}

// Receives the event and context from AWS Lambda.
export const handler = async (event, context) => {
    checkDefined(event, 'event');
    const invokingEvent = JSON.parse(event.invokingEvent);
    const ruleParameters = JSON.parse(event.ruleParameters);
    await getConfigurationItem(invokingEvent, async (err, configurationItem) => {

        let compliance = 'NOT_APPLICABLE';
        let annotation = '';
        const putEvaluationsRequest = {};
        if (isApplicable(configurationItem, event)) {
            // Invoke the compliance checking function.
            compliance = evaluateChangeNotificationCompliance(configurationItem, ruleParameters);
            if (compliance === "NON_COMPLIANT") {
                annotation = "This is an annotation describing why the resource is not compliant.";
            }
        }
        // Initializes the request that contains the evaluation results.
        if (annotation) {
            putEvaluationsRequest.Evaluations = [
                {
                    ComplianceResourceType: configurationItem.resourceType,
                    ComplianceResourceId: configurationItem.resourceId,
                    ComplianceType: compliance,
                    OrderingTimestamp: new Date(configurationItem.configurationItemCaptureTime),
                    Annotation: annotation
                },
            ];
        } else {
            putEvaluationsRequest.Evaluations = [
                {
                    ComplianceResourceType: configurationItem.resourceType,
                    ComplianceResourceId: configurationItem.resourceId,
                    ComplianceType: compliance,
                    OrderingTimestamp: new Date(configurationItem.configurationItemCaptureTime),
                },
            ];
        }
        putEvaluationsRequest.ResultToken = event.resultToken;

        // Sends the evaluation results to AWS Config.
        await configClient.send(new PutEvaluationsCommand(putEvaluationsRequest));
    });
};
```

###### Function Operations

The function performs the following operations at runtime:

1. The function runs when AWS Lambda passes the `event` object to the
   `handler` function. In this example, the function accepts the
   optional `callback` parameter, which it uses to return information to
   the caller. AWS Lambda also passes a `context` object, which contains
   information and methods that the function can use while it runs. Note that in
   newer versions of Lambda, context is no longer used.
2. The function checks whether the `messageType` for the event is a
   configuration item or an oversized configuration item, and then returns the
   configuration item.
3. The handler calls the `isApplicable` function to determine whether
   the resource was deleted.

###### Note

Rules reporting on deleted resources should return the evaluation result of `NOT_APPLICABLE` in order to avoid unnecessary rule evaluations. 4. The handler calls the `evaluateChangeNotificationCompliance`
function and passes the `configurationItem` and
`ruleParameters` objects that AWS Config published in the event.

The function first evaluates whether the resource is an EC2 instance. If the
resource is not an EC2 instance, the function returns a compliance value of
`NOT_APPLICABLE`.

The function then evaluates whether the `instanceType` attribute in
the configuration item is equal to the `desiredInstanceType`
parameter value. If the values are equal, the function returns
`COMPLIANT`. If the values are not equal, the function returns
`NON_COMPLIANT`. 5. The handler prepares to send the evaluation results to AWS Config by initializing
the `putEvaluationsRequest` object. This object includes the
`Evaluations` parameter, which identifies the compliance result,
the resource type, and the ID of the resource that was evaluated. The
`putEvaluationsRequest` object also includes the result token
from the event, which identifies the rule and the event for AWS Config. 6. The handler sends the evaluation results to AWS Config by passing the object to the
`putEvaluations` method of the `config` client.

Example Function for Periodic
Evaluations AWS Config will invoke a function like the following example for periodic evaluations.
Periodic evaluations occur at the frequency that you specify when you define the rule in
AWS Config.

If you use the AWS Config console to create a rule that is associated with a function like
this example, choose **Periodic** as the trigger type. If you use the
AWS Config API or AWS CLI to create the rule, set the `MessageType` attribute to
`ScheduledNotification`.

This example checks whether the total number of a specified resource
exceeds a specified maximum.

```
'use strict';
import { ConfigServiceClient, ListDiscoveredResourcesCommand, PutEvaluationsCommand } from "@aws-sdk/client-config-service";

const configClient = new ConfigServiceClient({});

// Receives the event and context from AWS Lambda.
export const handler = async (event, context, callback) => {
    // Parses the invokingEvent and ruleParameters values, which contain JSON objects passed as strings.
    var invokingEvent = JSON.parse(event.invokingEvent),
        ruleParameters = JSON.parse(event.ruleParameters),
        numberOfResources = 0;

    if (isScheduledNotification(invokingEvent) && hasValidRuleParameters(ruleParameters, callback)) {
        await countResourceTypes(ruleParameters.applicableResourceType, "", numberOfResources, async function (err, count) {
            if (err === null) {
                var putEvaluationsRequest;
                const compliance = evaluateCompliance(ruleParameters.maxCount, count);
                var annotation = '';
                if (compliance === "NON_COMPLIANT") {
                    annotation = "Description of why the resource is not compliant.";
                }
                // Initializes the request that contains the evaluation results.
                if (annotation) {
                    putEvaluationsRequest = {
                        Evaluations: [{
                            // Applies the evaluation result to the AWS account published in the event.
                            ComplianceResourceType: 'AWS::::Account',
                            ComplianceResourceId: event.accountId,
                            ComplianceType: compliance,
                            OrderingTimestamp: new Date(),
                            Annotation: annotation
                        }],
                        ResultToken: event.resultToken
                    };
                } else {
                    putEvaluationsRequest = {
                        Evaluations: [{
                            // Applies the evaluation result to the AWS account published in the event.
                            ComplianceResourceType: 'AWS::::Account',
                            ComplianceResourceId: event.accountId,
                            ComplianceType: compliance,
                            OrderingTimestamp: new Date()
                        }],
                        ResultToken: event.resultToken
                    };
                }

                // Sends the evaluation results to AWS Config.
                try {
                    await configClient.send(new PutEvaluationsCommand(putEvaluationsRequest));
                }
                catch (e) {
                    callback(e, null);
                }
            } else {
                callback(err, null);
            }
        });
    } else {
        console.log("Invoked for a notification other than Scheduled Notification... Ignoring.");
    }
};

// Checks whether the invoking event is ScheduledNotification.
function isScheduledNotification(invokingEvent) {
    return (invokingEvent.messageType === 'ScheduledNotification');
}

// Checks the rule parameters to see if they are valid
function hasValidRuleParameters(ruleParameters, callback) {
    // Regular express to verify that applicable resource given is a resource type
    const awsResourcePattern = /^AWS::(\w*)::(\w*)$/;
    const isApplicableResourceType = awsResourcePattern.test(ruleParameters.applicableResourceType);
    // Check to make sure the maxCount in the parameters is an integer
    const maxCountIsInt = !isNaN(ruleParameters.maxCount) && parseInt(Number(ruleParameters.maxCount)) == ruleParameters.maxCount && !isNaN(parseInt(ruleParameters.maxCount, 10));
    if (!isApplicableResourceType) {
        callback("The applicableResourceType parameter is not a valid resource type.", null);
    }
    if (!maxCountIsInt) {
        callback("The maxCount parameter is not a valid integer.", null);
    }
    return isApplicableResourceType && maxCountIsInt;
}

// Checks whether the compliance conditions for the rule are violated.
function evaluateCompliance(maxCount, actualCount) {
    if (actualCount > maxCount) {
        return "NON_COMPLIANT";
    } else {
        return "COMPLIANT";
    }
}

// Counts the applicable resources that belong to the AWS account.
async function countResourceTypes(applicableResourceType, nextToken, count, callback) {
    const input = { resourceType: applicableResourceType, nextToken: nextToken };
    const command = new ListDiscoveredResourcesCommand(input);
    try {
        const response = await configClient.send(command);
        count = count + response.resourceIdentifiers.length;
        if (response.nextToken !== undefined && response.nextToken != null) {
            countResourceTypes(applicableResourceType, response.nextToken, count, callback);
        }
        callback(null, count);
    } catch (e) {
        callback(e, null);
    }
    return count;
}
```

###### Function Operations

The function performs the following operations at runtime:

1. The function runs when AWS Lambda passes the `event` object to the
   `handler` function. In this example, the function accepts the
   optional `callback` parameter, which it uses to return information to
   the caller. AWS Lambda also passes a `context` object, which contains
   information and methods that the function can use while it runs. Note that in
   newer versions of Lambda, context is no longer used.
2. To count the resources of the specified type, the handler calls the
   `countResourceTypes` function, and it passes the
   `applicableResourceType` parameter that it received from the
   event. The `countResourceTypes` function calls the
   `listDiscoveredResources` method of the `config`
   client, which returns a list of identifiers for the applicable resources. The
   function uses the length of this list to determine the number of applicable
   resources, and it returns this count to the handler.
3. The handler prepares to send the evaluation results to AWS Config by initializing
   the `putEvaluationsRequest` object. This object includes the
   `Evaluations` parameter, which identifies the compliance result
   and the AWS account that was published in the event. You can use the
   `Evaluations` parameter to apply the result to any resource type
   that is supported by AWS Config. The `putEvaluationsRequest` object also
   includes the result token from the event, which identifies the rule and the
   event for AWS Config.
4. Within the `putEvaluationsRequest` object, the handler calls the
   `evaluateCompliance` function. This function tests whether the
   number of applicable resources exceeds the maximum assigned to the
   `maxCount` parameter, which was provided by the event. If the
   number of resources exceeds the maximum, the function returns
   `NON_COMPLIANT`. If the number of resources does not exceed the
   maximum, the function returns `COMPLIANT`.
5. The handler sends the evaluation results to AWS Config by passing the object to the
   `putEvaluations` method of the `config` client.

AWS Lambda executes functions in response to events that are published by AWS services.
The function for an AWS Config Custom Lambda rule receives an event that is published by AWS Config, and
the function then uses data that it receives from the event and that it retrieves from the
AWS Config API to evaluate the compliance of the rule. The operations in a function for a Config
rule differ depending on whether it performs an evaluation that is triggered by
configuration changes or triggered periodically.

For information about common patterns within AWS Lambda functions, see [Programming Model](../../../lambda/latest/dg/programming-model-v2.md "../../../lambda/latest/dg/programming-model-v2.md") in the
_AWS Lambda Developer Guide_.

Example Function for Evaluations Triggered by
Configuration Changes AWS Config will invoke a function like the following example when it detects a configuration
change for a resource that is within a custom rule's scope.

If you use the AWS Config console to create a rule that is associated with a function like
this example, choose **Configuration changes** as the trigger type. If
you use the AWS Config API or AWS CLI to create the rule, set the `MessageType`
attribute to `ConfigurationItemChangeNotification` and
`OversizedConfigurationItemChangeNotification`. These settings enable
your rule to be triggered whenever AWS Config generates a configuration item or an oversized
configuration item as a result of a resource change.

```
import botocore
import boto3
import json
import datetime

# Set to True to get the lambda to assume the Role attached on the Config Service (useful for cross-account).
ASSUME_ROLE_MODE = False

# This gets the client after assuming the Config service role
# either in the same AWS account or cross-account.
def get_client(service, event):
    """Return the service boto client. It should be used instead of directly calling the client.
    Keyword arguments:
    service -- the service name used for calling the boto.client()
    event -- the event variable given in the lambda handler
    """
    if not ASSUME_ROLE_MODE:
        return boto3.client(service)
    credentials = get_assume_role_credentials(event["executionRoleArn"])
    return boto3.client(service, aws_access_key_id=credentials['AccessKeyId'],
                        aws_secret_access_key=credentials['SecretAccessKey'],
                        aws_session_token=credentials['SessionToken']
                       )

# Helper function used to validate input
def check_defined(reference, reference_name):
    if not reference:
        raise Exception('Error: ', reference_name, 'is not defined')
    return reference

# Check whether the message is OversizedConfigurationItemChangeNotification or not
def is_oversized_changed_notification(message_type):
    check_defined(message_type, 'messageType')
    return message_type == 'OversizedConfigurationItemChangeNotification'

# Get configurationItem using getResourceConfigHistory API
# in case of OversizedConfigurationItemChangeNotification
def get_configuration(resource_type, resource_id, configuration_capture_time):
    result = AWS_CONFIG_CLIENT.get_resource_config_history(
        resourceType=resource_type,
        resourceId=resource_id,
        laterTime=configuration_capture_time,
        limit=1)
    configurationItem = result['configurationItems'][0]
    return convert_api_configuration(configurationItem)

# Convert from the API model to the original invocation model
def convert_api_configuration(configurationItem):
    for k, v in configurationItem.items():
        if isinstance(v, datetime.datetime):
            configurationItem[k] = str(v)
    configurationItem['awsAccountId'] = configurationItem['accountId']
    configurationItem['ARN'] = configurationItem['arn']
    configurationItem['configurationStateMd5Hash'] = configurationItem['configurationItemMD5Hash']
    configurationItem['configurationItemVersion'] = configurationItem['version']
    configurationItem['configuration'] = json.loads(configurationItem['configuration'])
    if 'relationships' in configurationItem:
        for i in range(len(configurationItem['relationships'])):
            configurationItem['relationships'][i]['name'] = configurationItem['relationships'][i]['relationshipName']
    return configurationItem

# Based on the type of message get the configuration item
# either from configurationItem in the invoking event
# or using the getResourceConfigHistory API in getConfiguration function.
def get_configuration_item(invokingEvent):
    check_defined(invokingEvent, 'invokingEvent')
    if is_oversized_changed_notification(invokingEvent['messageType']):
        configurationItemSummary = check_defined(invokingEvent['configurationItemSummary'], 'configurationItemSummary')
        return get_configuration(configurationItemSummary['resourceType'], configurationItemSummary['resourceId'], configurationItemSummary['configurationItemCaptureTime'])
    return check_defined(invokingEvent['configurationItem'], 'configurationItem')

# Check whether the resource has been deleted. If it has, then the evaluation is unnecessary.
def is_applicable(configurationItem, event):
    try:
        check_defined(configurationItem, 'configurationItem')
        check_defined(event, 'event')
    except:
        return True
    status = configurationItem['configurationItemStatus']
    eventLeftScope = event['eventLeftScope']
    if status == 'ResourceDeleted':
        print("Resource Deleted, setting Compliance Status to NOT_APPLICABLE.")
    return (status == 'OK' or status == 'ResourceDiscovered') and not eventLeftScope

def get_assume_role_credentials(role_arn):
    sts_client = boto3.client('sts')
    try:
        assume_role_response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName="configLambdaExecution")
        return assume_role_response['Credentials']
    except botocore.exceptions.ClientError as ex:
        # Scrub error message for any internal account info leaks
        if 'AccessDenied' in ex.response['Error']['Code']:
            ex.response['Error']['Message'] = "AWS Config does not have permission to assume the IAM role."
        else:
            ex.response['Error']['Message'] = "InternalError"
            ex.response['Error']['Code'] = "InternalError"
        raise ex

def evaluate_change_notification_compliance(configuration_item, rule_parameters):
    check_defined(configuration_item, 'configuration_item')
    check_defined(configuration_item['configuration'], 'configuration_item[\'configuration\']')
    if rule_parameters:
        check_defined(rule_parameters, 'rule_parameters')

    if (configuration_item['resourceType'] != 'AWS::EC2::Instance'):
        return 'NOT_APPLICABLE'

    elif rule_parameters.get('desiredInstanceType'):
        if (configuration_item['configuration']['instanceType'] in rule_parameters['desiredInstanceType']):
            return 'COMPLIANT'
    return 'NON_COMPLIANT'

def lambda_handler(event, context):

    global AWS_CONFIG_CLIENT

    check_defined(event, 'event')
    invoking_event = json.loads(event['invokingEvent'])
    rule_parameters = {}
    if 'ruleParameters' in event:
        rule_parameters = json.loads(event['ruleParameters'])

    compliance_value = 'NOT_APPLICABLE'

    AWS_CONFIG_CLIENT = get_client('config', event)
    configuration_item = get_configuration_item(invoking_event)
    if is_applicable(configuration_item, event):
        compliance_value = evaluate_change_notification_compliance(
                configuration_item, rule_parameters)

    response = AWS_CONFIG_CLIENT.put_evaluations(
       Evaluations=[
           {
               'ComplianceResourceType': invoking_event['configurationItem']['resourceType'],
               'ComplianceResourceId': invoking_event['configurationItem']['resourceId'],
               'ComplianceType': compliance_value,
               'OrderingTimestamp': invoking_event['configurationItem']['configurationItemCaptureTime']
           },
       ],
       ResultToken=event['resultToken'])
```

###### Function Operations

The function performs the following operations at runtime:

1. The function runs when AWS Lambda passes the `event` object to the
   `handler` function. In this example, the function accepts the
   optional `callback` parameter, which it uses to return information to
   the caller. AWS Lambda also passes a `context` object, which contains
   information and methods that the function can use while it runs. Note that in
   newer versions of Lambda, context is no longer used.
2. The function checks whether the `messageType` for the event is a
   configuration item or an oversized configuration item, and then returns the
   configuration item.
3. The handler calls the `isApplicable` function to determine whether
   the resource was deleted.

###### Note

Rules reporting on deleted resources should return the evaluation result of `NOT_APPLICABLE` in order to avoid unnecessary rule evaluations. 4. The handler calls the `evaluateChangeNotificationCompliance`
function and passes the `configurationItem` and
`ruleParameters` objects that AWS Config published in the event.

The function first evaluates whether the resource is an EC2 instance. If the
resource is not an EC2 instance, the function returns a compliance value of
`NOT_APPLICABLE`.

The function then evaluates whether the `instanceType` attribute in
the configuration item is equal to the `desiredInstanceType`
parameter value. If the values are equal, the function returns
`COMPLIANT`. If the values are not equal, the function returns
`NON_COMPLIANT`. 5. The handler prepares to send the evaluation results to AWS Config by initializing
the `putEvaluationsRequest` object. This object includes the
`Evaluations` parameter, which identifies the compliance result,
the resource type, and the ID of the resource that was evaluated. The
`putEvaluationsRequest` object also includes the result token
from the event, which identifies the rule and the event for AWS Config. 6. The handler sends the evaluation results to AWS Config by passing the object to the
`putEvaluations` method of the `config` client.

Example Function for Periodic
Evaluations AWS Config will invoke a function like the following example for periodic evaluations.
Periodic evaluations occur at the frequency that you specify when you define the rule in
AWS Config.

If you use the AWS Config console to create a rule that is associated with a function like
this example, choose **Periodic** as the trigger type. If you use the
AWS Config API or AWS CLI to create the rule, set the `MessageType` attribute to
`ScheduledNotification`.

```
import botocore
import boto3
import json
import datetime

# Set to True to get the lambda to assume the Role attached on the Config Service (useful for cross-account).
ASSUME_ROLE_MODE = False
DEFAULT_RESOURCE_TYPE = 'AWS::::Account'

# This gets the client after assuming the Config service role
# either in the same AWS account or cross-account.
def get_client(service, event):
    """Return the service boto client. It should be used instead of directly calling the client.
    Keyword arguments:
    service -- the service name used for calling the boto.client()
    event -- the event variable given in the lambda handler
    """
    if not ASSUME_ROLE_MODE:
        return boto3.client(service)
    credentials = get_assume_role_credentials(event["executionRoleArn"])
    return boto3.client(service, aws_access_key_id=credentials['AccessKeyId'],
                        aws_secret_access_key=credentials['SecretAccessKey'],
                        aws_session_token=credentials['SessionToken']
                       )

def get_assume_role_credentials(role_arn):
    sts_client = boto3.client('sts')
    try:
        assume_role_response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName="configLambdaExecution")
        return assume_role_response['Credentials']
    except botocore.exceptions.ClientError as ex:
        # Scrub error message for any internal account info leaks
        if 'AccessDenied' in ex.response['Error']['Code']:
            ex.response['Error']['Message'] = "AWS Config does not have permission to assume the IAM role."
        else:
            ex.response['Error']['Message'] = "InternalError"
            ex.response['Error']['Code'] = "InternalError"
        raise ex

# Check whether the message is a ScheduledNotification or not.
def is_scheduled_notification(message_type):
    return message_type == 'ScheduledNotification'

def count_resource_types(applicable_resource_type, next_token, count):
    resource_identifier = AWS_CONFIG_CLIENT.list_discovered_resources(resourceType=applicable_resource_type, nextToken=next_token)
    updated = count + len(resource_identifier['resourceIdentifiers']);
    return updated

# Evaluates the configuration items in the snapshot and returns the compliance value to the handler.
def evaluate_compliance(max_count, actual_count):
    return 'NON_COMPLIANT' if int(actual_count) > int(max_count) else 'COMPLIANT'

def evaluate_parameters(rule_parameters):
    if 'applicableResourceType' not in rule_parameters:
        raise ValueError('The parameter with "applicableResourceType" as key must be defined.')
    if not rule_parameters['applicableResourceType']:
        raise ValueError('The parameter "applicableResourceType" must have a defined value.')
    return rule_parameters

# This generate an evaluation for config
def build_evaluation(resource_id, compliance_type, event, resource_type=DEFAULT_RESOURCE_TYPE, annotation=None):
    """Form an evaluation as a dictionary. Usually suited to report on scheduled rules.
    Keyword arguments:
    resource_id -- the unique id of the resource to report
    compliance_type -- either COMPLIANT, NON_COMPLIANT or NOT_APPLICABLE
    event -- the event variable given in the lambda handler
    resource_type -- the CloudFormation resource type (or AWS::::Account) to report on the rule (default DEFAULT_RESOURCE_TYPE)
    annotation -- an annotation to be added to the evaluation (default None)
    """
    eval_cc = {}
    if annotation:
        eval_cc['Annotation'] = annotation
    eval_cc['ComplianceResourceType'] = resource_type
    eval_cc['ComplianceResourceId'] = resource_id
    eval_cc['ComplianceType'] = compliance_type
    eval_cc['OrderingTimestamp'] = str(json.loads(event['invokingEvent'])['notificationCreationTime'])
    return eval_cc

def lambda_handler(event, context):

    global AWS_CONFIG_CLIENT

    evaluations = []
    rule_parameters = {}
    resource_count = 0
    max_count = 0

    invoking_event = json.loads(event['invokingEvent'])
    if 'ruleParameters' in event:
        rule_parameters = json.loads(event['ruleParameters'])
        valid_rule_parameters = evaluate_parameters(rule_parameters)

    compliance_value = 'NOT_APPLICABLE'

    AWS_CONFIG_CLIENT = get_client('config', event)
    if is_scheduled_notification(invoking_event['messageType']):
        result_resource_count = count_resource_types(valid_rule_parameters['applicableResourceType'], '', resource_count)

    if valid_rule_parameters.get('maxCount'):
        max_count = valid_rule_parameters['maxCount']

    compliance_value = evaluate_compliance(max_count, result_resource_count)
    evaluations.append(build_evaluation(event['accountId'], compliance_value, event, resource_type=DEFAULT_RESOURCE_TYPE))
    response = AWS_CONFIG_CLIENT.put_evaluations(Evaluations=evaluations, ResultToken=event['resultToken'])
```

###### Function Operations

The function performs the following operations at runtime:

1. The function runs when AWS Lambda passes the `event` object to the
   `handler` function. In this example, the function accepts the
   optional `callback` parameter, which it uses to return information to
   the caller. AWS Lambda also passes a `context` object, which contains
   information and methods that the function can use while it runs. Note that in
   newer versions of Lambda, context is no longer used.
2. To count the resources of the specified type, the handler calls the
   `countResourceTypes` function, and it passes the
   `applicableResourceType` parameter that it received from the
   event. The `countResourceTypes` function calls the
   `listDiscoveredResources` method of the `config`
   client, which returns a list of identifiers for the applicable resources. The
   function uses the length of this list to determine the number of applicable
   resources, and it returns this count to the handler.
3. The handler prepares to send the evaluation results to AWS Config by initializing
   the `putEvaluationsRequest` object. This object includes the
   `Evaluations` parameter, which identifies the compliance result
   and the AWS account that was published in the event. You can use the
   `Evaluations` parameter to apply the result to any resource type
   that is supported by AWS Config. The `putEvaluationsRequest` object also
   includes the result token from the event, which identifies the rule and the
   event for AWS Config.
4. Within the `putEvaluationsRequest` object, the handler calls the
   `evaluateCompliance` function. This function tests whether the
   number of applicable resources exceeds the maximum assigned to the
   `maxCount` parameter, which was provided by the event. If the
   number of resources exceeds the maximum, the function returns
   `NON_COMPLIANT`. If the number of resources does not exceed the
   maximum, the function returns `COMPLIANT`.
5. The handler sends the evaluation results to AWS Config by passing the object to the
   `putEvaluations` method of the `config` client.

When the trigger for a rule occurs, AWS Config invokes the rule's AWS Lambda function by
publishing an event. Then AWS Lambda executes the function by passing the event to the
function's handler.

Example Event for Evaluations Triggered by
Configuration Changes
AWS Config publishes an event when it detects a configuration change for a resource that is
within a rule's scope. The following example event shows that the rule was triggered by
a configuration change for an EC2 instance.

```
{
    "invokingEvent": "`{\"configurationItem\":{\"configurationItemCaptureTime\":\"2016-02-17T01:36:34.043Z\",\"awsAccountId\":\"123456789012\",\"configurationItemStatus\":\"OK\",\"resourceId\":\"i-00000000\",\"ARN\":\"arn:aws:ec2:us-east-2:123456789012:instance/i-00000000\",\"awsRegion\":\"us-east-2\",\"availabilityZone\":\"us-east-2a\",\"resourceType\":\"AWS::EC2::Instance\",\"tags\":{\"Foo\":\"Bar\"},\"relationships\":[{\"resourceId\":\"eipalloc-00000000\",\"resourceType\":\"AWS::EC2::EIP\",\"name\":\"Is attached to ElasticIp\"}],\"configuration\":{\"foo\":\"bar\"}},\"messageType\":\"ConfigurationItemChangeNotification\"}`",
    "ruleParameters": "`{\"myParameterKey\":\"myParameterValue\"}`",
    "resultToken": "`myResultToken`",
    "eventLeftScope": `false`,
    "executionRoleArn": "`arn:aws:iam::123456789012:role/config-role`",
    "configRuleArn": "`arn:aws:config:us-east-2:123456789012:config-rule/config-rule-0123456`",
    "configRuleName": "`change-triggered-config-rule`",
    "configRuleId": "`config-rule-0123456`",
    "accountId": "`123456789012`",
    "version": "1.0"
}

```

Example
Event for Evaluations Triggered by Oversized Configuration Changes Some resource changes generate oversized configuration items. The following example
event shows that the rule was triggered by an oversized configuration change for an EC2
instance.

```
{
        "invokingEvent": "`{\"configurationItemSummary\": {\"changeType\": \"UPDATE\",\"configurationItemVersion\": \"1.2\",\"configurationItemCaptureTime\":\"2016-10-06T16:46:16.261Z\",\"configurationStateId\": 0,\"awsAccountId\":\"123456789012\",\"configurationItemStatus\": \"OK\",\"resourceType\": \"AWS::EC2::Instance\",\"resourceId\":\"i-00000000\",\"resourceName\":null,\"ARN\":\"arn:aws:ec2:us-west-2:123456789012:instance/i-00000000\",\"awsRegion\": \"us-west-2\",\"availabilityZone\":\"us-west-2a\",\"configurationStateMd5Hash\":\"8f1ee69b287895a0f8bc5753eca68e96\",\"resourceCreationTime\":\"2016-10-06T16:46:10.489Z\"},\"messageType\":\"OversizedConfigurationItemChangeNotification\"}`",
        "ruleParameters": "`{\"myParameterKey\":\"myParameterValue\"}`",
        "resultToken": "`myResultToken`",
        "eventLeftScope": `false`,
        "executionRoleArn": "`arn:aws:iam::123456789012:role/config-role`",
        "configRuleArn": "`arn:aws:config:us-east-2:123456789012:config-rule/config-rule-ec2-managed-instance-inventory`",
        "configRuleName": "`change-triggered-config-rule`",
        "configRuleId": "`config-rule-0123456`",
        "accountId": "`123456789012`",
        "version": "1.0"
    }

```

Example Event for Evaluations Triggered by
Periodic Frequency AWS Config publishes an event when it evaluates your resources at a frequency that you
specify (such as every 24 hours). The following example event shows that the rule was
triggered by a periodic frequency.

```
{
    "invokingEvent": "`{\"awsAccountId\":\"123456789012\",\"notificationCreationTime\":\"2016-07-13T21:50:00.373Z\",\"messageType\":\"ScheduledNotification\",\"recordVersion\":\"1.0\"}`",
    "ruleParameters": "`{\"myParameterKey\":\"myParameterValue\"}`",
    "resultToken": "`myResultToken`",
    "eventLeftScope": `false`,
    "executionRoleArn": "`arn:aws:iam::123456789012:role/config-role`",
    "configRuleArn": "`arn:aws:config:us-east-2:123456789012:config-rule/config-rule-0123456`",
    "configRuleName": "`periodic-config-rule`",
    "configRuleId": "`config-rule-6543210`",
    "accountId": "`123456789012`",
    "version": "1.0"
}
```

### Event Attributes

The JSON object for an AWS Config event contains the following attributes:

`invokingEvent`

The event that triggers the evaluation for a rule. If the event is
published in response to a resource configuration change, the value for this
attribute is a string that contains a JSON `configurationItem` or
a `configurationItemSummary` (for oversized configuration items).
The configuration item represents the state of the resource at the moment
that AWS Config detected the change. For an example of a configuration item, see
the output produced by the `get-resource-config-history` AWS CLI
command in [Viewing Configuration History](view-manage-resource-console.md#get-config-history-cli "view-manage-resource-console.md#get-config-history-cli").

If the event is published for a periodic evaluation, the value is a string
that contains a JSON object. The object includes information about the
evaluation that was triggered.

For each type of event, a function must parse the string with a JSON
parser to be able to evaluate its contents, as shown in the following
Node.js example:

```
`var invokingEvent = JSON.parse(event.invokingEvent);`
```

`ruleParameters`

Key/value pairs that the function processes as part of its evaluation
logic. You define parameters when you use the AWS Config console to create a
Custom Lambda rule. You can also define parameters with the
`InputParameters` attribute in the `PutConfigRule`
AWS Config API request or the `put-config-rule` AWS CLI command.

The JSON code for the parameters is contained within a string, so a
function must parse the string with a JSON parser to be able to evaluate its
contents, as shown in the following Node.js example:

```
`var ruleParameters = JSON.parse(event.ruleParameters);`
```

`resultToken`

A token that the function must pass to AWS Config with the
`PutEvaluations` call.

`eventLeftScope`

A Boolean value that indicates whether the AWS resource to be evaluated
has been removed from the rule's scope. If the value is `true`,
the function indicates that the evaluation can be ignored by passing
`NOT_APPLICABLE` as the value for the
`ComplianceType` attribute in the `PutEvaluations`
call.

`executionRoleArn`

The ARN of the IAM role that is assigned to AWS Config.

`configRuleArn`

The ARN that AWS Config assigned to the rule.

`configRuleName`

The name that you assigned to the rule that caused AWS Config to publish the
event and invoke the function.

`configRuleId`

The ID that AWS Config assigned to the rule.

`accountId`

The ID of the AWS account that owns the rule.

`version`

A version number assigned by AWS. The version will increment if AWS
adds attributes to AWS Config events. If a function requires an attribute that is
only in events that match or exceed a specific version, then that function
can check the value of this attribute.

The current version for AWS Config events is 1.0.
