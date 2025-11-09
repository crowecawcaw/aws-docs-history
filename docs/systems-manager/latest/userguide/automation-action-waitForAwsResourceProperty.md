AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# `aws:waitForAwsResourceProperty` – Wait on an AWS resource

property

The `aws:waitForAwsResourceProperty` action allows your automation to wait
for a specific resource state or event state before continuing the automation. For more
examples of how to use this action, see [Additional runbook
examples](automation-document-examples.md "automation-document-examples.md").

###### Note

The default timeout value for this action is 3600 seconds (one hour). You can
limit or extend the timeout by specifying the `timeoutSeconds` parameter
for an `aws:waitForAwsResourceProperty` step. For more information and
examples of how to use this action, see [Handling timeouts in runbooks](automation-handling-timeouts.md "automation-handling-timeouts.md").

###### Note

The `aws:waitForAwsResourceProperty` action supports automatic
throttling retry. For more information, see [Configuring automatic retry for
throttled operations](automation-throttling-retry.md "automation-throttling-retry.md").

###### Input

Inputs are defined by the API operation that you choose.

YAML

```
action: aws:waitForAwsResourceProperty
inputs:
  Service: `The official namespace of the service`
  Api: `The API operation or method name`
  `API operation inputs or parameters`: `A value`
  PropertySelector: `Response object`
  DesiredValues:
  - `Desired property value`
```

JSON

```
{
  "action": "aws:waitForAwsResourceProperty",
  "inputs": {
    "Service":"`The official namespace of the service`",
    "Api":"`The API operation or method name`",
    "`API operation inputs or parameters`":"`A value`",
    "PropertySelector": "`Response object`",
    "DesiredValues": [
      "`Desired property value`"
    ]
  }
}
```

Service

The AWS service namespace that contains the API operation that you want
to run. For example, the namespace for AWS Systems Manager is `ssm`. The
namespace for Amazon Elastic Compute Cloud (Amazon EC2) is `ec2`. You can view a list of
supported AWS service namespaces in the [Available Services](../../../cli/latest/reference.md#available-services "../../../cli/latest/reference.md#available-services")
section of the _AWS CLI Command Reference_.

Type: String

Required: Yes

Api

The name of the API operation that you want to run. You can view the API
operations (also called methods) by choosing a service in the left
navigation on the following [Services Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html") page. Choose a method in the
**Client** section for the service that you want to
invoke. For example, all API operations (methods) for Amazon Relational Database Service (Amazon RDS) are
listed on the following page: [Amazon RDS methods](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html").

Type: String

Required: Yes

API operation inputs

One or more API operation inputs. You can view the available inputs (also
called parameters) by choosing a service in the left navigation on the
following [Services
Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html") page. Choose a method in the
**Client** section for the service that you want to
invoke. For example, all methods for Amazon RDS are listed on the following page:
[Amazon RDS methods](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html"). Choose the [describe_db_instances](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instances "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instances") method and scroll down to see the
available parameters, such as **DBInstanceIdentifier**,
**Name**, and **Values**.

YAML

```
inputs:
  Service: `The official namespace of the service`
  Api: `The API operation name`
  `API input 1`: `A value`
  `API Input 2`: `A value`
  `API Input 3`: `A value`
```

JSON

```
"inputs":{
      "Service":"`The official namespace of the service`",
      "Api":"`The API operation name`",
      "`API input 1`":"`A value`",
      "`API Input 2`":"`A value`",
      "`API Input 3`":"`A value`"
}
```

Type: Determined by chosen API operation

Required: Yes

PropertySelector

The JSONPath to a specific attribute in the response object. You can view
the response objects by choosing a service in the left navigation on the
following [Services
Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html") page. Choose a method in the
**Client** section for the service that you want to
invoke. For example, all methods for Amazon RDS are listed on the following page:
[Amazon RDS methods](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html"). Choose the [describe_db_instances](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instances "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instances") method and scroll down to the
**Response Structure** section.
**DBInstances** is listed as a response object.

Type: String

Required: Yes

DesiredValues

The expected status or state on which to continue the automation.

Type: MapList, StringList

Required: Yes
