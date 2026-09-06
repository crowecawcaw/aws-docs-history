

# Use `ListUserPolicies` with an AWS SDK or CLI
<a name="iam_example_iam_ListUserPolicies_section"></a>

The following code examples show how to use `ListUserPolicies`.

------
#### [ CLI ]

**AWS CLI**  
**To list policies for an IAM user**  
The following `list-user-policies` command lists the policies that are attached to the IAM user named `Bob`.  

```
aws iam list-user-policies \
    --user-name {{Bob}}
```
Output:  

```
{
    "PolicyNames": [
        "ExamplePolicy",
        "TestPolicy"
    ]
}
```
For more information, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in the *AWS IAM User Guide*.  
+  For API details, see [ListUserPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html) in *AWS CLI Command Reference*. 

------
#### [ Go ]

**SDK for Go V2**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/iam#code-examples). 

```
import (
	"context"
	"encoding/json"
	"errors"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/iam"
	"github.com/aws/aws-sdk-go-v2/service/iam/types"
	"github.com/aws/smithy-go"
)

// UserWrapper encapsulates user actions used in the examples.
// It contains an IAM service client that is used to perform user actions.
type UserWrapper struct {
	IamClient *iam.Client
}



// ListUserPolicies lists the inline policies for the specified user.
func (wrapper UserWrapper) ListUserPolicies(ctx context.Context, userName string) ([]string, error) {
	var policies []string
	result, err := wrapper.IamClient.ListUserPolicies(ctx, &iam.ListUserPoliciesInput{
		UserName: aws.String(userName),
	})
	if err != nil {
		log.Printf("Couldn't list policies for user %v. Here's why: %v\n", userName, err)
	} else {
		policies = result.PolicyNames
	}
	return policies, err
}
```
+  For API details, see [ListUserPolicies](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/iam#Client.ListUserPolicies) in *AWS SDK for Go API Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example retrieves the list of names of the inline policies that are embedded in the IAM user named `David`.**  

```
Get-IAMUserPolicyList -UserName David
```
**Output:**  

```
Davids_IAM_Admin_Policy
```
+  For API details, see [ListUserPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example retrieves the list of names of the inline policies that are embedded in the IAM user named `David`.**  

```
Get-IAMUserPolicyList -UserName David
```
**Output:**  

```
Davids_IAM_Admin_Policy
```
+  For API details, see [ListUserPolicies](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.