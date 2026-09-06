

# AWS Secrets and Configuration Provider code examples
<a name="ascp-examples"></a>

## ASCP authentication and access control examples
<a name="ascp-auth-access-examples"></a>

### Example: IAM policy allowing Amazon EKS Pod Identity service (pods.eks.amazonaws.com) to assume the role and tag the session:
<a name="w2aac21c17c18b5b3"></a>

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "pods.eks.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ]
    }
  ]
}
```

------

## SecretProviderClass
<a name="ascp-examples-secretproviderclass"></a>

You use YAML to describe which secrets to mount in Amazon EKS using the ASCP. For examples, see [SecretProviderClass usage](#ascp-scenarios-secretproviderclass).

### SecretProviderClass YAML structure
<a name="w2aac21c17c18c25b5"></a>

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
   name: {{name}}
spec:
  provider: aws
  parameters:
    region:
    failoverRegion:
    pathTranslation:
    usePodIdentity:
    preferredAddressType:
    objects:
```

The parameters field contains the details of the mount request:

**region**  
(Optional) The AWS Region of the secret. If you don't use this field, the ASCP looks up the Region from the annotation on the node. This lookup adds overhead to mount requests, so we recommend that you provide the Region for clusters that use large numbers of Pods.  
If you also specify `failoverRegion`, the ASCP tries to retrieve the secret from both Regions. If either Region returns a 4xx error, for example for an authentication issue, the ASCP does not mount either secret. If the secret is retrieved successfully from `region`, then the ASCP mounts that secret value. If the secret is not retrieved successfully from `region`, but it is retrieved successfully from `failoverRegion`, then the ASCP mounts that secret value.

**failoverRegion**  
(Optional) If you include this field, the ASCP tries to retrieve the secret from the Regions defined in `region` and this field. If either Region returns a 4xx error, for example for an authentication issue, the ASCP does not mount either secret. If the secret is retrieved successfully from `region`, then the ASCP mounts that secret value. If the secret is not retrieved successfully from `region`, but it is retrieved successfully from `failoverRegion`, then the ASCP mounts that secret value. For an example of how to use this field, see [Multi-Region secret failover](#multi-region-failover).

**pathTranslation**  
(Optional) A single substitution character to use if the file name in Amazon EKS will contain the path separator character, such as slash (/) on Linux. The ASCP can't create a mounted file that contains a path separator character. Instead, the ASCP replaces the path separator character with a different character. If you don't use this field, the replacement character is underscore (\_), so for example, `My/Path/Secret` mounts as `My_Path_Secret`.   
To prevent character substitution, enter the string `False`.

**usePodIdentity**  
(Optional) Determines the authentication approach. When not specified, it defaults to IAM Roles for Service Accounts (IRSA) (IRSA).  
+ To use EKS Pod Identity, use any of these values: `"true"`", `"True"`, `"TRUE"`, `"t"`, or `"T"`.
+ To explicitly use IRSA, set to any of these values: `"false"`, `"False"`, `"FALSE"`, `"f"`, or `"F"`"=.

**preferredAddressType**  
(Optional) Specifies the preferred IP address type for Pod Identity Agent endpoint communication. The field is only applicable when using EKS Pod Identity feature and will be ignored when using IAM Roles for Service Accounts.Values are case-insensitive. Valid values are:  
+ `"ipv4"`, `"IPv4"`", or `"IPV4"` – Force the use of Pod Identity Agent IPv4 endpoint
+ `"ipv6"`, `"IPv6"`, or `"IPV6"` – Force the use of Pod Identity Agent IPv6 endpoint
+ not specified – Use auto endpoint selection, trying IPv4 endpoint first and falling back to IPv6 endpoint if IPv4 fails

**objects**  
A string containing a YAML declaration of the secrets to be mounted. We recommend using a YAML multi-line string or pipe (\|) character.    
**objectName**  
Required. Specifies the name of the secret or parameter to be fetched. For Secrets Manager this is the [`SecretId`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html#API_GetSecretValue_RequestParameters) parameter and can be either the friendly name or full ARN of the secret. For SSM Parameter Store, this is the [`Name`](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html#API_GetParameter_RequestParameters) of the parameter and can be either the name or full ARN of the parameter.  
**objectType**  
Required if you don't use a Secrets Manager ARN for `objectName`. Can be either `secretsmanager` or `ssmparameter`.   
**objectAlias**  
(Optional) The file name of the secret in the Amazon EKS Pod. If you don't specify this field, the `objectName` appears as the file name.  
**filePermission**  
(Optional) The 4 digit octal string which specifies the file permission to mount secret with. If you don't specify this field it will default to `"0644"`.   
**objectVersion**  
(Optional) The version ID of the secret. Not recommended because you must update the version ID every time you update the secret. By default the most recent version is used. If you include a `failoverRegion`, this field represents the primary `objectVersion`.  
**objectVersionLabel**  
(Optional) The alias for the version. The default is the most recent version AWSCURRENT. For more information, see [Secret versions](whats-in-a-secret.md#term_version). If you include a `failoverRegion`, this field represents the primary `objectVersionLabel`.  
**jmesPath**  
(Optional) A map of the keys in the secret to the files to be mounted in Amazon EKS. To use this field, your secret value must be in JSON format. If you use this field, you must include the subfields `path` and `objectAlias`.    
**path**  
A key from a key-value pair in the JSON of the secret value. If the field contains a hyphen, use single quotes to escape it, for example: `path: '"hyphenated-path"'`  
**objectAlias**  
The file name to be mounted in the Amazon EKS Pod. If the field contains a hyphen, use single quotes to escape it, for example: `objectAlias: '"hyphenated-alias"'`  
**filePermission**  
(Optional) The 4 digit octal string which specifies the file permission to mount secret with. If you don't specify this field it will default to the parent object's file permission.   
**failoverObject**  
(Optional) If you specify this field, the ASCP tries to retrieve both the secret specified in the primary `objectName` and the secret specified in the `failoverObject` `objectName` sub-field. If either returns a 4xx error, for example for an authentication issue, the ASCP does not mount either secret. If the secret is retrieved successfully from the primary `objectName`, then the ASCP mounts that secret value. If the secret is not retrieved successfully from the primary `objectName`, but it is retrieved successfully from the failover `objectName`, then the ASCP mounts that secret value. If you include this field, you must include the field `objectAlias`. For an example of how to use this field, see [Failover to a different secret](#failover-secret).  
You typically use this field when the failover secret isn't a replica. For an example of how to specify a replica, see [Multi-Region secret failover](#multi-region-failover).    
**objectName**  
The name or full ARN of the failover secret. If you use an ARN, the Region in the ARN must match the field `failoverRegion`.  
**objectVersion**  
(Optional) The version ID of the secret. Must match the primary `objectVersion`. Not recommended because you must update the version ID every time you update the secret. By default the most recent version is used.   
**objectVersionLabel**  
(Optional) The alias for the version. The default is the most recent version AWSCURRENT. For more information, see [Secret versions](whats-in-a-secret.md#term_version). 

### Create a basic SecretProviderClass configuration to mount secrets in your Amazon EKS Pods.
<a name="w2aac21c17c18c25c11"></a>

------
#### [ Pod Identity ]

SecretProviderClass to use a secret in the same Amazon EKS cluster:

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: {{aws-secrets-manager}}
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "{{mySecret}}"
        objectType: "secretsmanager"
    usePodIdentity: "true"
```

------
#### [ IRSA ]

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: {{deployment-aws-secrets}}
spec:
  provider: aws
  parameters:
    objects: |
        - objectName: "{{MySecret}}"
          objectType: "secretsmanager"
```

------

### SecretProviderClass usage
<a name="ascp-scenarios-secretproviderclass"></a>

Use these examples to create SecretProviderClass configurations for different scenarios.

#### Example: Mount secrets by name or ARN
<a name="mount-by-name-arn"></a>

This example shows how to mount three different types of secrets:
+ A secret specified by full ARN
+ A secret specified by name
+ A specific version of a secret

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: {{aws-secrets}}
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "arn:aws:secretsmanager:us-east-2:{{777788889999}}:secret:MySecret2-d4e5f6"
      - objectName: "MySecret3"
        objectType: "secretsmanager"
      - objectName: "MySecret4"
        objectType: "secretsmanager"
        objectVersionLabel: "AWSCURRENT"
```

#### Example: Mount key-value pairs from a secret
<a name="mount-key-value-pairs"></a>

This example shows how to mount specific key-value pairs from a JSON-formatted secret:

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: {{aws-secrets}}
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "arn:aws:secretsmanager:us-east-2:{{777788889999}}:secret:MySecret-a1b2c3"
        jmesPath: 
            - path: username
              objectAlias: dbusername
            - path: password
              objectAlias: dbpassword
```

#### Example: Mount secrets by file permission
<a name="mount-by-permission"></a>

This example shows how to mount a secret with a specific file permission

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: {{aws-secrets}}
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "mySecret"
        objectType: "secretsmanager"
        filePermission: "0600"
        jmesPath: 
            - path: username
              objectAlias: dbusername
              filePermission: "0400"
```

#### Example: Failover configuration examples
<a name="failover-examples"></a>

These examples show how to configure failover for secrets.

##### Multi-Region secret failover
<a name="multi-region-failover"></a>

This example shows how to configure automatic failover for a secret replicated across multiple Regions:

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: {{aws-secrets}}
spec:
  provider: aws
  parameters:
    region: us-east-1
    failoverRegion: us-east-2
    objects: |
      - objectName: "MySecret"
```

##### Failover to a different secret
<a name="failover-secret"></a>

This example shows how to configure failover to a different secret (not a replica):

```
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: aws-secrets
spec:
  provider: aws
  parameters:
    region: us-east-1
    failoverRegion: us-east-2
    objects: |
      - objectName: "arn:aws:secretsmanager:us-east-1:{{777788889999}}:secret:MySecret-a1b2c3"
        objectAlias: "MyMountedSecret"
        failoverObject: 
          - objectName: "arn:aws:secretsmanager:us-east-2:{{777788889999}}:secret:MyFailoverSecret-d4e5f6"
```

## Additional resources
<a name="additional-resources"></a>

For more information about using ASCP with Amazon EKS, see the following resources:
+ [Using Pod Identity with Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)
+ [Using AWS Secrets and Configuration Provider](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_ascp_csi.html)
+ [AWS Secrets Store CSI Driver on GitHub](https://github.com/aws/secrets-store-csi-driver-provider-aws)