# Actions, resources, and condition keys for AWS IoT Device Tester

AWS IoT Device Tester (service prefix: `iot-device-tester`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../freertos/latest/userguide/device-tester-for-freertos-ug.md "../../../freertos/latest/userguide/device-tester-for-freertos-ug.md").
- View a list of the [API operations available for
  this service](../../../freertos/latest/userguide/dev-tester-prereqs.md "../../../freertos/latest/userguide/dev-tester-prereqs.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../freertos/latest/userguide/dev-tester-prereqs.md "../../../freertos/latest/userguide/dev-tester-prereqs.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/iot-device-tester/iot-device-tester.json "https://servicereference.us-east-1.amazonaws.com/v1/iot-device-tester/iot-device-tester.json") for this service.

###### Topics

- [Actions defined by AWS IoT Device Tester](#list_iot-device-tester-actions-as-permissions "#list_iot-device-tester-actions-as-permissions")
- [Resource types defined by AWS IoT Device Tester](#list_iot-device-tester-resources-for-iam-policies "#list_iot-device-tester-resources-for-iam-policies")
- [Condition keys for AWS IoT Device Tester](#list_iot-device-tester-policy-keys "#list_iot-device-tester-policy-keys")

## Actions defined by AWS IoT Device Tester

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                  | Description                                                                                                                    | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | -------------- | ------------ |
| [CheckVersion](../../../freertos/latest/userguide/dev-tester-prereqs.md "../../../freertos/latest/userguide/dev-tester-prereqs.md")      | Grants permission to IoT Device Tester to check if a given set of product, test suite and device tester version are compatible |                             |                | Read         |
| [DownloadTestSuite](../../../freertos/latest/userguide/dev-tester-prereqs.md "../../../freertos/latest/userguide/dev-tester-prereqs.md") | Grants permission to IoT Device Tester to download compatible test suite versions                                              |                             |                | Read         |
| [LatestIdt](../../../freertos/latest/userguide/dev-tester-prereqs.md "../../../freertos/latest/userguide/dev-tester-prereqs.md")         | Grants permission to IoT Device Tester to get information on latest version of device tester available                         |                             |                | Read         |
| [SendMetrics](../../../freertos/latest/userguide/dev-tester-prereqs.md "../../../freertos/latest/userguide/dev-tester-prereqs.md")       | Grants permission to IoT Device Tester to send usage metrics on your behalf                                                    |                             |                | Write        |
| [SupportedVersion](../../../freertos/latest/userguide/dev-tester-prereqs.md "../../../freertos/latest/userguide/dev-tester-prereqs.md")  | Grants permission to IoT Device Tester to get list of supported products and test suite versions                               |                             |                | Read         |

## Resource types defined by AWS IoT Device Tester

AWS IoT Device Tester does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS IoT Device Tester

AWS IoT Device Tester has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
