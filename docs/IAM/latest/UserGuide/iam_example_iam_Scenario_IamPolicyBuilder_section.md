# Work with the IAM Policy Builder API using an AWS SDK

The following code example shows how to:

- Create IAM policies by using the object-oriented API.
- Use the IAM Policy Builder API with the IAM service.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iam#code-examples").

The examples use the following imports.

```

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.policybuilder.iam.IamConditionOperator;
import software.amazon.awssdk.policybuilder.iam.IamEffect;
import software.amazon.awssdk.policybuilder.iam.IamPolicy;
import software.amazon.awssdk.policybuilder.iam.IamPolicyWriter;
import software.amazon.awssdk.policybuilder.iam.IamPrincipal;
import software.amazon.awssdk.policybuilder.iam.IamPrincipalType;
import software.amazon.awssdk.policybuilder.iam.IamResource;
import software.amazon.awssdk.policybuilder.iam.IamStatement;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.iam.IamClient;
import software.amazon.awssdk.services.iam.model.GetPolicyResponse;
import software.amazon.awssdk.services.iam.model.GetPolicyVersionResponse;
import software.amazon.awssdk.services.sts.StsClient;

import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.List;


```

Create a time-based policy.

```
        public String timeBasedPolicyExample() {
                IamPolicy policy = IamPolicy.builder()
                                .addStatement(b -> b
                                                .effect(IamEffect.ALLOW)
                                                .addAction("dynamodb:GetItem")
                                                .addResource(IamResource.ALL)
                                                .addCondition(b1 -> b1
                                                                .operator(IamConditionOperator.DATE_GREATER_THAN)
                                                                .key("aws:CurrentTime")
                                                                .value("2020-04-01T00:00:00Z"))
                                                .addCondition(b1 -> b1
                                                                .operator(IamConditionOperator.DATE_LESS_THAN)
                                                                .key("aws:CurrentTime")
                                                                .value("2020-06-30T23:59:59Z")))
                                .build();

                // Use an IamPolicyWriter to write out the JSON string to a more readable
                // format.
                return policy.toJson(IamPolicyWriter.builder()
                                .prettyPrint(true)
                                .build());
        }


```

Create a policy with multiple conditions.

```
        public String multipleConditionsExample() {
                IamPolicy policy = IamPolicy.builder()
                                .addStatement(b -> b
                                                .effect(IamEffect.ALLOW)
                                                .addAction("dynamodb:GetItem")
                                                .addAction("dynamodb:BatchGetItem")
                                                .addAction("dynamodb:Query")
                                                .addAction("dynamodb:PutItem")
                                                .addAction("dynamodb:UpdateItem")
                                                .addAction("dynamodb:DeleteItem")
                                                .addAction("dynamodb:BatchWriteItem")
                                                .addResource("arn:aws:dynamodb:*:*:table/table-name")
                                                .addConditions(IamConditionOperator.STRING_EQUALS
                                                                .addPrefix("ForAllValues:"),
                                                                "dynamodb:Attributes",
                                                                List.of("column-name1", "column-name2", "column-name3"))
                                                .addCondition(b1 -> b1
                                                                .operator(IamConditionOperator.STRING_EQUALS
                                                                                .addSuffix("IfExists"))
                                                                .key("dynamodb:Select")
                                                                .value("SPECIFIC_ATTRIBUTES")))
                                .build();

                return policy.toJson(IamPolicyWriter.builder()
                                .prettyPrint(true).build());
        }


```

Use principals in a policy.

```
        public String specifyPrincipalsExample() {
                IamPolicy policy = IamPolicy.builder()
                                .addStatement(b -> b
                                                .effect(IamEffect.DENY)
                                                .addAction("s3:*")
                                                .addPrincipal(IamPrincipal.ALL)
                                                .addResource("arn:aws:s3:::amzn-s3-demo-bucket/*")
                                                .addResource("arn:aws:s3:::amzn-s3-demo-bucket")
                                                .addCondition(b1 -> b1
                                                                .operator(IamConditionOperator.ARN_NOT_EQUALS)
                                                                .key("aws:PrincipalArn")
                                                                .value("arn:aws:iam::444455556666:user/user-name")))
                                .build();
                return policy.toJson(IamPolicyWriter.builder()
                                .prettyPrint(true).build());
        }


```

Allow cross-account access.

```
        public String allowCrossAccountAccessExample() {
                IamPolicy policy = IamPolicy.builder()
                                .addStatement(b -> b
                                                .effect(IamEffect.ALLOW)
                                                .addPrincipal(IamPrincipalType.AWS, "111122223333")
                                                .addAction("s3:PutObject")
                                                .addResource("arn:aws:s3:::amzn-s3-demo-bucket/*")
                                                .addCondition(b1 -> b1
                                                                .operator(IamConditionOperator.STRING_EQUALS)
                                                                .key("s3:x-amz-acl")
                                                                .value("bucket-owner-full-control")))
                                .build();
                return policy.toJson(IamPolicyWriter.builder()
                                .prettyPrint(true).build());
        }


```

Build and upload an `IamPolicy`.

```
        public String createAndUploadPolicyExample(IamClient iam, String accountID, String policyName) {
                // Build the policy.
                IamPolicy policy = IamPolicy.builder() // 'version' defaults to "2012-10-17".
                                .addStatement(IamStatement.builder()
                                                .effect(IamEffect.ALLOW)
                                                .addAction("dynamodb:PutItem")
                                                .addResource("arn:aws:dynamodb:us-east-1:" + accountID
                                                                + ":table/exampleTableName")
                                                .build())
                                .build();
                // Upload the policy.
                iam.createPolicy(r -> r.policyName(policyName).policyDocument(policy.toJson()));
                return policy.toJson(IamPolicyWriter.builder().prettyPrint(true).build());
        }


```

Download and work with an `IamPolicy`.

```
        public String createNewBasedOnExistingPolicyExample(IamClient iam, String accountID, String policyName,
                        String newPolicyName) {

                String policyArn = "arn:aws:iam::" + accountID + ":policy/" + policyName;
                GetPolicyResponse getPolicyResponse = iam.getPolicy(r -> r.policyArn(policyArn));

                String policyVersion = getPolicyResponse.policy().defaultVersionId();
                GetPolicyVersionResponse getPolicyVersionResponse = iam
                                .getPolicyVersion(r -> r.policyArn(policyArn).versionId(policyVersion));

                // Create an IamPolicy instance from the JSON string returned from IAM.
                String decodedPolicy = URLDecoder.decode(getPolicyVersionResponse.policyVersion().document(),
                                StandardCharsets.UTF_8);
                IamPolicy policy = IamPolicy.fromJson(decodedPolicy);

                /*
                 * All IamPolicy components are immutable, so use the copy method that creates a
                 * new instance that
                 * can be altered in the same method call.
                 *
                 * Add the ability to get an item from DynamoDB as an additional action.
                 */
                IamStatement newStatement = policy.statements().get(0).copy(s -> s.addAction("dynamodb:GetItem"));

                // Create a new statement that replaces the original statement.
                IamPolicy newPolicy = policy.copy(p -> p.statements(Arrays.asList(newStatement)));

                // Upload the new policy. IAM now has both policies.
                iam.createPolicy(r -> r.policyName(newPolicyName)
                                .policyDocument(newPolicy.toJson()));

                return newPolicy.toJson(IamPolicyWriter.builder().prettyPrint(true).build());
        }


```

- For more information, see [AWS SDK for Java 2.x Developer Guide](../../../sdk-for-java/latest/developer-guide/feature-iam-policy-builder.md "../../../sdk-for-java/latest/developer-guide/feature-iam-policy-builder.md").
- For API details, see the following topics in _AWS SDK for Java 2.x API Reference_.
  - [CreatePolicy](../../../goto/SdkForJavaV2/iam-2010-05-08/CreatePolicy.md "../../../goto/SdkForJavaV2/iam-2010-05-08/CreatePolicy.md")
  - [GetPolicy](../../../goto/SdkForJavaV2/iam-2010-05-08/GetPolicy.md "../../../goto/SdkForJavaV2/iam-2010-05-08/GetPolicy.md")
  - [GetPolicyVersion](../../../goto/SdkForJavaV2/iam-2010-05-08/GetPolicyVersion.md "../../../goto/SdkForJavaV2/iam-2010-05-08/GetPolicyVersion.md")

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
