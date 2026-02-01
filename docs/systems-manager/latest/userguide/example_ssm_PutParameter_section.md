• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `PutParameter` with an AWS SDK or CLI

The following code examples show how to use `PutParameter`.

CLI

**AWS CLI**

**Example 1: To change a parameter value**

The following `put-parameter` example changes the value of the specified parameter.

```
`aws ssm put-parameter \
 --name `"MyStringParameter"` \
 --type `"String"` \
 --value `"Vici"` \
 --overwrite`

```

Output:

```
{
    "Version": 2,
    "Tier": "Standard"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](param-create-cli.md "param-create-cli.md"), [Managing parameter tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md"), and [Working with parameter policies](parameter-store-policies.md "parameter-store-policies.md") in the _AWS Systems Manager User Guide_.

**Example 2: To create an advanced parameter**

The following `put-parameter` example creates an advanced parameter.

```
`aws ssm put-parameter \
 --name `"MyAdvancedParameter"` \
 --description `"This is an advanced parameter"` \
 --value `"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat [truncated]"` \
 --type `"String"` \
 --tier `Advanced``

```

Output:

```
{
    "Version": 1,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](param-create-cli.md "param-create-cli.md"), [Managing parameter tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md"), and [Working with parameter policies](parameter-store-policies.md "parameter-store-policies.md") in the _AWS Systems Manager User Guide_.

**Example 3: To convert a standard parameter to an advanced parameter**

The following `put-parameter` example converts an existing standard parameter into an advanced parameter.

```
`aws ssm put-parameter \
 --name `"MyConvertedParameter"` \
 --value `"abc123"` \
 --type `"String"` \
 --tier `Advanced` \
 --overwrite`

```

Output:

```
{
    "Version": 2,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](param-create-cli.md "param-create-cli.md"), [Managing parameter tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md"), and [Working with parameter policies](parameter-store-policies.md "parameter-store-policies.md") in the _AWS Systems Manager User Guide_.

**Example 4: To create a parameter with a policy attached**

The following `put-parameter` example creates an advanced parameter with a parameter policy attached.

```
`aws ssm put-parameter \
 --name `"/Finance/Payroll/q2accesskey"` \
 --value `"P@sSwW)rd"` \
 --type `"SecureString"` \
 --tier `Advanced` \
 --policies "[{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-06-30T00:00:00.000Z\"}},{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"5\",\"Unit\":\"Days\"}},{\"Type\":\"NoChangeNotification\",\"Version\":\"1.0\",\"Attributes\":{\"After\":\"60\",\"Unit\":\"Days\"}}]"`

```

Output:

```
{
    "Version": 1,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](param-create-cli.md "param-create-cli.md"), [Managing parameter tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md"), and [Working with parameter policies](parameter-store-policies.md "parameter-store-policies.md") in the _AWS Systems Manager User Guide_.

**Example 5: To add a policy to an existing parameter**

The following `put-parameter` example attaches a policy to an existing advanced parameter.

```
`aws ssm put-parameter \
 --name `"/Finance/Payroll/q2accesskey"` \
 --value `"N3wP@sSwW)rd"` \
 --type `"SecureString"` \
 --tier `Advanced` \
 --policies "[{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-06-30T00:00:00.000Z\"}},{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"5\",\"Unit\":\"Days\"}},{\"Type\":\"NoChangeNotification\",\"Version\":\"1.0\",\"Attributes\":{\"After\":\"60\",\"Unit\":\"Days\"}}]"
 --overwrite`

```

Output:

```
{
    "Version": 2,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](param-create-cli.md "param-create-cli.md"), [Managing parameter tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md"), and [Working with parameter policies](parameter-store-policies.md "parameter-store-policies.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [PutParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.ParameterType;
import software.amazon.awssdk.services.ssm.model.PutParameterRequest;
import software.amazon.awssdk.services.ssm.model.SsmException;

public class PutParameter {

    public static void main(String[] args) {
        final String usage = """

                Usage:
                    <paraName>

                Where:
                    paraName - The name of the parameter.
                    paraValue - The value of the parameter.
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String paraName = args[0];
        String paraValue = args[1];
        Region region = Region.US_EAST_1;
        SsmClient ssmClient = SsmClient.builder()
                .region(region)
                .build();

        putParaValue(ssmClient, paraName, paraValue);
        ssmClient.close();
    }

    public static void putParaValue(SsmClient ssmClient, String paraName, String value) {
        try {
            PutParameterRequest parameterRequest = PutParameterRequest.builder()
                    .name(paraName)
                    .type(ParameterType.STRING)
                    .value(value)
                    .build();

            ssmClient.putParameter(parameterRequest);
            System.out.println("The parameter was successfully added.");

        } catch (SsmException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [PutParameter](../../../goto/SdkForJavaV2/ssm-2014-11-06/PutParameter.md "../../../goto/SdkForJavaV2/ssm-2014-11-06/PutParameter.md")
  in _AWS SDK for Java 2.x API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a parameter. There is no output if the command succeeds.**

```
Write-SSMParameter -Name "Welcome" -Type "String" -Value "helloWorld"

```

**Example 2: This example changes a parameter. There is no output if the command succeeds.**

```
Write-SSMParameter -Name "Welcome" -Type "String" -Value "Good day, Sunshine!" -Overwrite $true

```

- For API details, see
  [PutParameter](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a parameter. There is no output if the command succeeds.**

```
Write-SSMParameter -Name "Welcome" -Type "String" -Value "helloWorld"

```

**Example 2: This example changes a parameter. There is no output if the command succeeds.**

```
Write-SSMParameter -Name "Welcome" -Type "String" -Value "Good day, Sunshine!" -Overwrite $true

```

- For API details, see
  [PutParameter](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ssm#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ssm#code-examples").

```
async fn make_parameter(
    client: &Client,
    name: &str,
    value: &str,
    description: &str,
) -> Result<(), Error> {
    let resp = client
        .put_parameter()
        .overwrite(true)
        .r#type(ParameterType::String)
        .name(name)
        .value(value)
        .description(description)
        .send()
        .await?;

    println!("Success! Parameter now has version: {}", resp.version());

    Ok(())
}


```

- For API details, see
  [PutParameter](https://docs.rs/aws-sdk-ssm/latest/aws_sdk_ssm/client/struct.Client.html#method.put_parameter "https://docs.rs/aws-sdk-ssm/latest/aws_sdk_ssm/client/struct.Client.html#method.put_parameter")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
