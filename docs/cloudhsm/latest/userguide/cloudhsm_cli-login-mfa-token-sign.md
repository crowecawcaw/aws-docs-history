

# Log in with MFA to an HSM using CloudHSM CLI
<a name="cloudhsm_cli-login-mfa-token-sign"></a>

Use the **login mfa-token-sign** command in AWS CloudHSM CloudHSM CLI to log in to a hardware security module (HSM) using multi-factor authentication (MFA). To use this command, you must first set up [MFA for CloudHSM CLI](login-mfa-token-sign.md).

## User type
<a name="cloudhsm_cli-login-mfa-token-userType"></a>

The following users can run these commands.
+ Admin
+ Crypto user (CU)

## Syntax
<a name="cloudhsm_cli-login-mfa-token-syntax"></a>

```
aws-cloudhsm > help login mfa-token-sign
Login with token-sign mfa

USAGE:
    login --username {{<username>}} --role {{<role>}} mfa-token-sign --token {{<token>}}

OPTIONS:
      --cluster-id {{<CLUSTER_ID>}}  Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
      --token {{<TOKEN>}}            Filepath where the unsigned token file will be written
  -h, --help                     Print help
```

## Example
<a name="cloudhsm_cli-login-mfa-token-example"></a>

**Example**  

```
aws-cloudhsm > login --username test_user --role admin mfa-token-sign --token /home/valid.token
Enter password:
Enter signed token file path (press enter if same as the unsigned token file):
{
  "error_code": 0,
  "data": {
    "username": "test_user",
    "role": "admin"
  }
}
```

## Arguments
<a name="cloudhsm_cli-login-mfa-token-arguments"></a>

**{{<CLUSTER\_ID>}}**  
The ID of the cluster to run this operation on.  
Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md)

**{{<TOKEN>}}**  
Filepath where the unsigned token file will be written.  
Required: Yes

## Related topics
<a name="cloudhsm_cli-login-mfa-token-seeAlso"></a>
+ [Getting Started with CloudHSM CLI](cloudhsm_cli-getting-started.md)
+ [Activate the Cluster](activate-cluster.md)
+ [Using CloudHSM CLI to manage MFA](login-mfa-token-sign.md)