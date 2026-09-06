

# Actions, resources, and condition keys for AWS Mainframe Modernization Application Testing
<a name="list_apptest"></a>

AWS Mainframe Modernization Application Testing (service prefix: `apptest`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/m2/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/apptest/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/m2/latest/userguide/apptest-security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/apptest/apptest.json) for this service.

**Topics**
+ [Actions defined by AWS Mainframe Modernization Application Testing](#list_apptest-actions-as-permissions)
+ [Resource types defined by AWS Mainframe Modernization Application Testing](#list_apptest-resources-for-iam-policies)
+ [Condition keys for AWS Mainframe Modernization Application Testing](#list_apptest-policy-keys)

## Actions defined by AWS Mainframe Modernization Application Testing
<a name="list_apptest-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateTestCase](https://docs.aws.amazon.com/apptest/latest/APIReference/API_CreateTestCase.html)  **
  - **Description:** Grants permission to create a test case
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTestConfiguration](https://docs.aws.amazon.com/apptest/latest/APIReference/API_CreateTestConfiguration.html)  **
  - **Description:** Grants permission to create a test configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTestSuite](https://docs.aws.amazon.com/apptest/latest/APIReference/API_CreateTestSuite.html)  **
  - **Description:** Grants permission to create a test suite
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteTestCase](https://docs.aws.amazon.com/apptest/latest/APIReference/API_DeleteTestCase.html)  **
  - **Description:** Grants permission to delete a test case
  - **Resource types (\*required):** [TestCase\*](#list_apptest-resource-TestCase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTestConfiguration](https://docs.aws.amazon.com/apptest/latest/APIReference/API_DeleteTestConfiguration.html)  **
  - **Description:** Grants permission to delete a test configuration
  - **Resource types (\*required):** [TestConfiguration\*](#list_apptest-resource-TestConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTestRun](https://docs.aws.amazon.com/apptest/latest/APIReference/API_DeleteTestRun.html)  **
  - **Description:** Grants permission to delete a test run
  - **Resource types (\*required):** [TestRun\*](#list_apptest-resource-TestRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTestSuite](https://docs.aws.amazon.com/apptest/latest/APIReference/API_DeleteTestSuite.html)  **
  - **Description:** Grants permission to delete a test suite
  - **Resource types (\*required):** [TestSuite\*](#list_apptest-resource-TestSuite)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetTestCase](https://docs.aws.amazon.com/apptest/latest/APIReference/API_GetTestCase.html)  **
  - **Description:** Grants permission to get a test case
  - **Resource types (\*required):** [TestCase\*](#list_apptest-resource-TestCase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTestConfiguration](https://docs.aws.amazon.com/apptest/latest/APIReference/API_GetTestConfiguration.html)  **
  - **Description:** Grants permission to get a test configuration
  - **Resource types (\*required):** [TestConfiguration\*](#list_apptest-resource-TestConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTestRunStep](https://docs.aws.amazon.com/apptest/latest/APIReference/API_GetTestRunStep.html)  **
  - **Description:** Grants permission to get test run step
  - **Resource types (\*required):** [TestRun\*](#list_apptest-resource-TestRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTestSuite](https://docs.aws.amazon.com/apptest/latest/APIReference/API_GetTestSuite.html)  **
  - **Description:** Grants permission to get a test suite
  - **Resource types (\*required):** [TestSuite\*](#list_apptest-resource-TestSuite)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/apptest/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTestCases](https://docs.aws.amazon.com/apptest/latest/APIReference/API_ListTestCases.html)  **
  - **Description:** Grants permission to list test cases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTestConfigurations](https://docs.aws.amazon.com/apptest/latest/APIReference/API_ListTestConfigurations.html)  **
  - **Description:** Grants permission to list test configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTestRunSteps](https://docs.aws.amazon.com/apptest/latest/APIReference/API_ListTestRunSteps.html)  **
  - **Description:** Grants permission to list steps for a test run
  - **Resource types (\*required):** [TestRun\*](#list_apptest-resource-TestRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestRunTestCases](https://docs.aws.amazon.com/apptest/latest/APIReference/API_ListTestRunTestCases.html)  **
  - **Description:** Grants permission to list test cases for a test run
  - **Resource types (\*required):** [TestRun\*](#list_apptest-resource-TestRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestRuns](https://docs.aws.amazon.com/apptest/latest/APIReference/API_ListTestRuns.html)  **
  - **Description:** Grants permission to list test runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTestSuites](https://docs.aws.amazon.com/apptest/latest/APIReference/API_ListTestSuites.html)  **
  - **Description:** Grants permission to list test suites
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartTestRun](https://docs.aws.amazon.com/apptest/latest/APIReference/API_StartTestRun.html)  **
  - **Description:** Grants permission to start a test run
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/apptest/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [TestCase](#list_apptest-resource-TestCase) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Resource types (\*required):** [TestConfiguration](#list_apptest-resource-TestConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Resource types (\*required):** [TestRun](#list_apptest-resource-TestRun) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Resource types (\*required):** [TestSuite](#list_apptest-resource-TestSuite) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apptest-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/apptest/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [TestCase](#list_apptest-resource-TestCase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Resource types (\*required):** [TestConfiguration](#list_apptest-resource-TestConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Resource types (\*required):** [TestRun](#list_apptest-resource-TestRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Resource types (\*required):** [TestSuite](#list_apptest-resource-TestSuite) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apptest-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateTestCase](https://docs.aws.amazon.com/apptest/latest/APIReference/API_UpdateTestCase.html)  **
  - **Description:** Grants permission to update a test case
  - **Resource types (\*required):** [TestCase\*](#list_apptest-resource-TestCase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTestConfiguration](https://docs.aws.amazon.com/apptest/latest/APIReference/API_UpdateTestConfiguration.html)  **
  - **Description:** Grants permission to update a test configuration
  - **Resource types (\*required):** [TestConfiguration\*](#list_apptest-resource-TestConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTestSuite](https://docs.aws.amazon.com/apptest/latest/APIReference/API_UpdateTestSuite.html)  **
  - **Description:** Grants permission to update a test suite
  - **Resource types (\*required):** [TestSuite\*](#list_apptest-resource-TestSuite)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Mainframe Modernization Application Testing
<a name="list_apptest-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [TestCase](https://docs.aws.amazon.com/m2/latest/userguide/concepts-apptest.html#TestCase-concept)  | arn:${Partition}:apptest:${Region}:${Account}:testcase/${TestCaseId} | [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_) | 
|  [TestConfiguration](https://docs.aws.amazon.com/m2/latest/userguide/concepts-apptest.html#TestConfiguration-concept)  | arn:${Partition}:apptest:${Region}:${Account}:testconfiguration/${TestConfigurationId} | [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_) | 
|  [TestRun](https://docs.aws.amazon.com/m2/latest/userguide/concepts-apptest.html#TestRun-concept)  | arn:${Partition}:apptest:${Region}:${Account}:testrun/${TestRunId} | [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_) | 
|  [TestSuite](https://docs.aws.amazon.com/m2/latest/userguide/concepts-apptest.html#TestSuite-concept)  | arn:${Partition}:apptest:${Region}:${Account}:testsuite/${TestSuiteId} | [aws:ResourceTag/${TagKey}](#list_apptest-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Mainframe Modernization Application Testing
<a name="list_apptest-policy-keys"></a>

AWS Mainframe Modernization Application Testing defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 