

# Create a security configuration with the Amazon EMR console or with the AWS CLI
<a name="emr-create-security-configuration"></a>

This topic covers general procedures to create a security configuration with the Amazon EMR console and the AWS CLI, followed by a reference for the parameters that comprise encryption, authentication, and IAM roles for EMRFS. For more information about these features, see the following topics:
+ [Encrypt data at rest and in transit with Amazon EMR](emr-data-encryption.md)
+ [Use Kerberos for authentication with Amazon EMR](emr-kerberos.md)
+ [Configure IAM roles for EMRFS requests to Amazon S3](emr-emrfs-iam-roles.md)

**To create a security configuration using the console**

1. Open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr/).

1. In the navigation pane, choose **Security Configurations**, **Create security configuration**. 

1. Type a **Name** for the security configuration.

1. Choose options for **Encryption** and **Authentication** as described in the sections below and then choose **Create**.

**To create a security configuration using the AWS CLI**
+ Use the `create-security-configuration` command as shown in the following example.
  + For {{SecConfigName}}, specify the name of the security configuration. This is the name you specify when you create a cluster that uses this security configuration.
  + For `{{SecConfigDef}}`, specify an inline JSON structure or the path to a local JSON file, such as `{{file://MySecConfig.json}}`. The JSON parameters define options for **Encryption**, **IAM Roles for EMRFS access to Amazon S3**, and **Authentication** as described in the sections below.

  ```
  aws emr create-security-configuration --name "{{SecConfigName}}" --security-configuration {{SecConfigDef}}
  ```

## Configure data encryption
<a name="emr-security-configuration-encryption"></a>

Before you configure encryption in a security configuration, create the keys and certificates that are used for encryption. For more information, see [Providing keys for encrypting data at rest](emr-encryption-enable.md#emr-encryption-create-keys) and [Providing certificates for encrypting data in transit with Amazon EMR encryption](emr-encryption-enable.md#emr-encryption-certificates).

When you create a security configuration, you specify two sets of encryption options: at-rest data encryption and in-transit data encryption. Options for at-rest data encryption include both Amazon S3 with EMRFS and local-disk encryption. In-transit encryption options enable the open-source encryption features for certain applications that support Transport Layer Security (TLS). At-rest options and in-transit options can be enabled together or separately. For more information, see [Encrypt data at rest and in transit with Amazon EMR](emr-data-encryption.md).

**Note**  
When you use AWS KMS, charges apply for the storage and use of encryption keys. For more information, see [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/).

### Specifying encryption options using the console
<a name="emr-security-configuration-encryption-console"></a>

Choose options under **Encryption** according to the following guidelines.
+ Choose options under **At rest encryption** to encrypt data stored within the file system. 

  You can choose to encrypt data in Amazon S3, local disks, or both. 
+ Under **S3 data encryption**, for **Encryption mode**, choose a value to determine how Amazon EMR encrypts Amazon S3 data with EMRFS. 

  What you do next depends on the encryption mode you chose:
  + **SSE-S3**

    Specifies [Server-side encryption with Amazon S3-managed encryption keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html). You don't need to do anything more because Amazon S3 handles keys for you.
  + **SSE-KMS** or **CSE-KMS**

    Specifies [server-side encryption with AWS KMS-managed keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) or [client-side encryption with AWS KMS-managed keys (CSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html). For **AWS KMS key**, select a key. The key must exist in the same region as your EMR cluster. For key requirements, see [Using AWS KMS keys for encryption](emr-encryption-enable.md#emr-awskms-keys).
  + **CSE-Custom**

    Specifies [client-side encryption using a custom client-side root key (CSE-custom)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html#client-side-encryption-client-side-master-key-intro). For **S3 object**, enter the location in Amazon S3, or the Amazon S3 ARN, of your custom key-provider JAR file. Then, for **Key provider class**, enter the full class name of a class declared in your application that implements the EncryptionMaterialsProvider interface.
+ Under **Local disk encryption**, choose a value for **Key provider type**.
  + **AWS KMS key**

    Select this option to specify an AWS KMS key. For **AWS KMS key**, select a key. The key must exist in the same region as your EMR cluster. For more information about key requirements, see [Using AWS KMS keys for encryption](emr-encryption-enable.md#emr-awskms-keys).

    **EBS Encryption**

    When you specify AWS KMS as your key provider, you can enable EBS encryption to encrypt EBS root device and storage volumes. To enable such option, you must grant the Amazon EMR service role `EMR_DefaultRole` with permissions to use the AWS KMS key that you specify. For more information about key requirements, see [Enabling EBS encryption by providing additional permissions for KMS keys](emr-encryption-enable.md#emr-awskms-ebs-encryption).
  + **Custom**

    Select this option to specify a custom key provider. For **S3 object**, enter the location in Amazon S3, or the Amazon S3 ARN, of your custom key-provider JAR file. For **Key provider class**, enter the full class name of a class declared in your application that implements the EncryptionMaterialsProvider interface. The class name you provide here must be different from the class name provided for CSE-Custom.
+ Choose **In-transit encryption** to enable the open-source TLS encryption features for in-transit data. Choose a **Certificate provider type** according to the following guidelines: 
  + **EMR-managed**

    Select this option to have Amazon EMR create and store private certificates for you. When selecting this option, Amazon EMR will upload the PEM-encoded certificate of the created certificate authority to AWS Secrets Manager in your account for you to use in your trust stores. You may optionally configure the KMS key and tags used for this secret. You may also optionally specify a custom validity duration for the created certificates and a custom wildcard suffix for the certificate SAN in addition to the default private DNS wildcard (\*.ec2.internal in us-east-1 and \*.{{region}}.compute.internal in all other regions).
  + **PEM**

    Select this option to use PEM files that you provide within a zip file. Two artifacts are required within the zip file: privateKey.pem and certificateChain.pem. A third file, trustedCertificates.pem, is optional. See [Providing certificates for encrypting data in transit with Amazon EMR encryption](emr-encryption-enable.md#emr-encryption-certificates) for details. For **S3 object**, specify the location in Amazon S3, or the Amazon S3 ARN, of the zip file field. 
  + **Custom**

    Select this option to specify a custom certificate provider and then, for **S3 object**, enter the location in Amazon S3, or the Amazon S3 ARN, of your custom certificate-provider JAR file. For **Key provider class**, enter the full class name of a class declared in your application that implements the TLSArtifactsProvider interface. 

### Specifying encryption options using the AWS CLI
<a name="emr-security-configuration-encryption-cli"></a>

The sections that follow use sample scenarios to illustrate well-formed **--security-configuration** JSON for different configurations and key providers, followed by a reference for the JSON parameters and appropriate values.

#### Example in-transit data encryption options
<a name="emr-encryption-intransit-cli"></a>

The example below illustrates the following scenario:
+ In-transit data encryption is enabled and at-rest data encryption is disabled.
+ Amazon EMR will create and manage private certificates for you, with a wildcard trusting the EC2 private DNS suffix for the region. The ARN of the created secret is added to the CACertificateSecretARN field visible in the describe-security-configuration API response.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": true,
        "EnableAtRestEncryption": false,
        "InTransitEncryptionConfiguration": {
            "TLSCertificateConfiguration": {
                "CertificateProviderType": "EMR"
            }
        }
    }
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is enabled with Amazon EMR-managed certificates, specifying a customer KMS key and tags for secret creation and adding the EC2 public DNS suffix for the region to the SAN list of the created certificates. The generated CA certificate will expire in 30 days, at which point the security configuration will need to be deleted and re-created to continue being used.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": true,
        "EnableAtRestEncryption": false,
        "InTransitEncryptionConfiguration": {
            "TLSCertificateConfiguration": {
                "CertificateProviderType": "EMR",
                "AwsKmsKey": "arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012",
                "SecretTags": [{"Key": "cluster-type", "Value": "test"}],
                "WildcardDnsSuffix": "us-east-2.compute.amazonaws.com",
                "ValidityInDays": 30
            }
        }
    }
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is enabled and at-rest data encryption is disabled.
+ A zip file with certificates in Amazon S3 is used as the key provider (see [Providing certificates for encrypting data in transit with Amazon EMR encryption](emr-encryption-enable.md#emr-encryption-certificates) for certificate requirements.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
	"EncryptionConfiguration": {
		"EnableInTransitEncryption": true,
		"EnableAtRestEncryption": false,
		"InTransitEncryptionConfiguration": {
			"TLSCertificateConfiguration": {
				"CertificateProviderType": "PEM",
				"S3Object": "s3://MyConfigStore/artifacts/MyCerts.zip"
			}
		}
	}
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is enabled and at-rest data encryption is disabled.
+ A custom key provider is used (see [Providing certificates for encrypting data in transit with Amazon EMR encryption](emr-encryption-enable.md#emr-encryption-certificates) for certificate requirements).

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
	"EncryptionConfiguration": {
		"EnableInTransitEncryption": true,
		"EnableAtRestEncryption": false,
		"InTransitEncryptionConfiguration": {
			"TLSCertificateConfiguration": {
				"CertificateProviderType": "Custom",
				"S3Object": "s3://MyConfig/artifacts/MyCerts.jar",
				"CertificateProviderClass": "com.mycompany.MyCertProvider"
			}
		}
 	}
}'
```

#### Example at-rest data encryption options
<a name="emr-encryption-atrest-cli"></a>

The example below illustrates the following scenario:
+ In-transit data encryption is disabled and at-rest data encryption is enabled.
+ SSE-S3 is used for Amazon S3 encryption.
+ Local disk encryption uses AWS KMS as the key provider.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
	"EncryptionConfiguration": {
		"EnableInTransitEncryption": false,
		"EnableAtRestEncryption": true,
		"AtRestEncryptionConfiguration": {
			"S3EncryptionConfiguration": {
				"EncryptionMode": "SSE-S3"
			},
			"LocalDiskEncryptionConfiguration": {
				"EncryptionKeyProviderType": "AwsKms",
				"AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
			}
		}
 	}
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is enabled and references a zip file with PEM certificates in Amazon S3, using the ARN.
+ SSE-KMS is used for Amazon S3 encryption.
+ Local disk encryption uses AWS KMS as the key provider.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
	"EncryptionConfiguration": {
		"EnableInTransitEncryption": true,
		"EnableAtRestEncryption": true,
		"InTransitEncryptionConfiguration": {
			"TLSCertificateConfiguration": {
				"CertificateProviderType": "PEM",
				"S3Object": "arn:aws:s3:::MyConfigStore/artifacts/MyCerts.zip"
			}
		},
		"AtRestEncryptionConfiguration": {
			"S3EncryptionConfiguration": {
				"EncryptionMode": "SSE-KMS",
				"AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
			},
			"LocalDiskEncryptionConfiguration": {
				"EncryptionKeyProviderType": "AwsKms",
				"AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
			}
		}
	}
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is enabled with Amazon EMR-managed certificates, specifying a customer KMS key and tags for secret creation and adding `*.mydomain.com` to the SAN list of the created certificates.
+ CSE-KMS is used for Amazon S3 encryption.
+ Local disk encryption uses a custom key provider referenced by its ARN.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
	"EncryptionConfiguration": {
		"EnableInTransitEncryption": true,
		"EnableAtRestEncryption": true,
		"InTransitEncryptionConfiguration": {
			"TLSCertificateConfiguration": {
				"CertificateProviderType": "EMR",
				"AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
				"SecretTags": [{"Key": "cluster-type", "Value": "test"}],
				"WildcardDnsSuffix": "mydomain.com"
			}
		},
		"AtRestEncryptionConfiguration": {
			"S3EncryptionConfiguration": {
				"EncryptionMode": "CSE-KMS",
				"AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
			},
			"LocalDiskEncryptionConfiguration": {
				"EncryptionKeyProviderType": "Custom",
				"S3Object": "arn:aws:s3:::artifacts/MyKeyProvider.jar",
				"EncryptionKeyProviderClass": "com.mycompany.MyKeyProvider"
			}
		}
	}
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is enabled with a custom key provider.
+ CSE-Custom is used for Amazon S3 data.
+ Local disk encryption uses a custom key provider.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
	"EncryptionConfiguration": {
		"EnableInTransitEncryption": "true",
		"EnableAtRestEncryption": "true",
		"InTransitEncryptionConfiguration": {
			"TLSCertificateConfiguration": {
				"CertificateProviderType": "Custom",
				"S3Object": "s3://MyConfig/artifacts/MyCerts.jar", 
				"CertificateProviderClass": "com.mycompany.MyCertProvider"
			}
		},
		"AtRestEncryptionConfiguration": {
			"S3EncryptionConfiguration": {
				"EncryptionMode": "CSE-Custom",
				"S3Object": "s3://MyConfig/artifacts/MyCerts.jar", 
				"EncryptionKeyProviderClass": "com.mycompany.MyKeyProvider"
				},
			"LocalDiskEncryptionConfiguration": {
				"EncryptionKeyProviderType": "Custom",
				"S3Object": "s3://MyConfig/artifacts/MyCerts.jar",
				"EncryptionKeyProviderClass": "com.mycompany.MyKeyProvider"
			}
		}
	}
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is disabled and at-rest data encryption is enabled.
+ Amazon S3 encryption is enabled with SSE-KMS.
+ Multiple AWS KMS keys are used, one per each S3 bucket, and encryption exceptions are applied to these individual S3 buckets.
+ Local disk encryption is disabled.

```
aws emr create-security-configuration --name "MySecConfig" --security-configuration '{
  	"EncryptionConfiguration": {
   		"AtRestEncryptionConfiguration": {
      	     	"S3EncryptionConfiguration": {
        			"EncryptionMode": "SSE-KMS",
        			"AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
        			"Overrides": [
         				 {
           				 "BucketName": "amzn-s3-demo-bucket1",
            				"EncryptionMode": "SSE-S3"
          				},
          				{
            				"BucketName": "amzn-s3-demo-bucket2",
           				 "EncryptionMode": "CSE-KMS",
            				"AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
         				 },
         				 {
           				 "BucketName": "amzn-s3-demo-bucket3",
          				  "EncryptionMode": "SSE-KMS",
           				 "AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
          				}
        					]
      							}
   						 	},
   		"EnableInTransitEncryption": false,
    		"EnableAtRestEncryption": true
  }
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is disabled and at-rest data encryption is enabled.
+ Amazon S3 encryption is enabled with SSE-S3 and local disk encryption is disabled.

```
aws emr create-security-configuration --name "MyS3EncryptionConfig" --security-configuration '{
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": false,
        "EnableAtRestEncryption": true,
        "AtRestEncryptionConfiguration": {
            "S3EncryptionConfiguration": {
                "EncryptionMode": "SSE-S3"
            }
        }
     }
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is disabled and at-rest data encryption is enabled.
+ Local disk encryption is enabled with AWS KMS as the key provider and Amazon S3 encryption is disabled.

```
aws emr create-security-configuration --name "MyLocalDiskEncryptionConfig" --security-configuration '{
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": false,
        "EnableAtRestEncryption": true,
        "AtRestEncryptionConfiguration": {
            "LocalDiskEncryptionConfiguration": {
                "EncryptionKeyProviderType": "AwsKms",
                "AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
            }
        }
     }
}'
```

The example below illustrates the following scenario:
+ In-transit data encryption is disabled and at-rest data encryption is enabled.
+ Local disk encryption is enabled with AWS KMS as the key provider and Amazon S3 encryption is disabled.
+ EBS encryption is enabled. 

```
aws emr create-security-configuration --name "MyLocalDiskEncryptionConfig" --security-configuration '{
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": false,
        "EnableAtRestEncryption": true,
        "AtRestEncryptionConfiguration": {
            "LocalDiskEncryptionConfiguration": {
                "EnableEbsEncryption": true,
                "EncryptionKeyProviderType": "AwsKms",
                "AwsKmsKey": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
            }
        }
     }
}'
```

The example below illustrates the following scenario:

SSE-EMR-WAL is used for EMR WAL encryption

```
aws emr create-security-configuration --name "MySecConfig" \
    --security-configuration '{
        "EncryptionConfiguration": {
            "EMRWALEncryptionConfiguration":{ },
            "EnableInTransitEncryption":false, "EnableAtRestEncryption":false
        }
    }'
```

`EnableInTransitEncryption` and `EnableAtRestEncryption` still could be true, if want to enable related encryption.

The example below illustrates the following scenario:
+ SSE-KMS-WAL is used for EMR WAL encryption
+ Server side encryption uses AWS Key Management Service as the key provider

```
aws emr create-security-configuration --name "MySecConfig" \
    --security-configuration '{
        "EncryptionConfiguration": {
            "EMRWALEncryptionConfiguration":{
                "AwsKmsKey":"arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
                },
            "EnableInTransitEncryption":false, "EnableAtRestEncryption":false
        }
    }'
```

`EnableInTransitEncryption` and `EnableAtRestEncryption` still could be true, if want to enable related encryption.

#### JSON reference for encryption settings
<a name="emr-encryption-cli-parameters"></a>

The following table lists the JSON parameters for encryption settings and provides a description of acceptable values for each parameter.


| Parameter | Description | 
| --- |--- |
| "EnableInTransitEncryption" : true \| false | Specify true to enable in-transit encryption and false to disable it. If omitted, false is assumed, and in-transit encryption is disabled. | 
| "EnableAtRestEncryption": true \| false | Specify true to enable at-rest encryption and false to disable it. If omitted, false is assumed and at-rest encryption is disabled. | 
| **In-transit encryption parameters** | 
| --- |
| "InTransitEncryptionConfiguration" : | Specifies a collection of values used to configure in-transit encryption when EnableInTransitEncryption is true. | 
|  "CertificateProviderType": "EMR" \| "PEM" \| "Custom" | Specifies whether to use EMR-created and managed certificates, PEM certificates referenced with a zipped file, or a Custom certificate provider. If PEM is specified, S3Object must be a reference to the location in Amazon S3 of a zip file containing the certificates. If Custom is specified, S3Object must be a reference to the location in Amazon S3 of a JAR file, followed by a CertificateProviderClass entry. | 
|  "S3Object" : "{{ZipLocation}}" \| "{{JarLocation}}" | Provides the location in Amazon S3 to a zip file when PEM is specified, or to a JAR file when Custom is specified. The format can be a path (for example, s3://MyConfig/artifacts/CertFiles.zip) or an ARN (for example, arn:aws:s3:::Code/MyCertProvider.jar). If a zip file is specified, it must contain files named exactly privateKey.pem and certificateChain.pem. A file named trustedCertificates.pem is optional. | 
|  "CertificateProviderClass" : "{{MyClassID}}" | Required only if Custom is specified for CertificateProviderType. {{MyClassID}} specifies a full class name declared in the JAR file, which implements the TLSArtifactsProvider interface. For example, com.mycompany.MyCertProvider. | 
|  "AwsKmsKey" : "{{MyKeyARN}}" | Optional, only if EMR is specified for CertificateProviderType. A customer-managed key for uploading the created CA certificate to AWS Secrets Manager. {{MyKeyARN}} must be a fully specified ARN to a key (for example, arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-456789012123). | 
|  "SecretTags" : [{"Key":"mykey","Value":"myvalue"}] | Optional, only if EMR is specified for CertificateProviderType. Tags to add to the created CA certificate in AWS Secrets Manager. To include this field the caller must have secretsmanager:TagResource permissions. | 
|  "ValidityInDays" : {{number}} | Optional, only if EMR is specified for CertificateProviderType. How many days the created certificates will be valid for, starting from the date of security configuration creation. If not specified, defaults to 20 years. | 
|  "WildcardDnsSuffix" : "mydomain.com" | Optional, only if EMR is specified for CertificateProviderType. A domain to add with a wildcard prefix to the SAN list of the created certificates. Whether or not this is specified, the certificate will always include \*.ec2.internal in us-east-1 and \*.{{region}}.compute.internal in all other regions. | 
| **At-rest encryption parameters** | 
| --- |
| "AtRestEncryptionConfiguration" :  | Specifies a collection of values for at-rest encryption when EnableAtRestEncryption is true, including Amazon S3 encryption and local disk encryption. | 
| Amazon S3 encryption parameters | 
| "S3EncryptionConfiguration" : | Specifies a collection of values used for Amazon S3 encryption with the Amazon EMR File System (EMRFS). | 
| "EncryptionMode": "SSE-S3" \| "SSE-KMS" \| "CSE-KMS" \| "CSE-Custom" | Specifies the type of Amazon S3 encryption to use. If SSE-S3 is specified, no further Amazon S3 encryption values are required. If either SSE-KMS or CSE-KMS is specified, an AWS KMS key ARN must be specified as the AwsKmsKey value. If CSE-Custom is specified, S3Object and EncryptionKeyProviderClass values must be specified. | 
| "AwsKmsKey" : "{{MyKeyARN}}" | Required only when either SSE-KMS or CSE-KMS is specified for EncryptionMode. {{MyKeyARN}} must be a fully specified ARN to a key (for example, arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012). | 
|  "S3Object" : "{{JarLocation}}" | Required only when CSE-Custom is specified for CertificateProviderType. {{JarLocation}} provides the location in Amazon S3 to a JAR file. The format can be a path (for example, s3://MyConfig/artifacts/MyKeyProvider.jar) or an ARN (for example, arn:aws:s3:::Code/MyKeyProvider.jar). | 
| "EncryptionKeyProviderClass" : "{{MyS3KeyClassID}}" | Required only when CSE-Custom is specified for EncryptionMode. {{MyS3KeyClassID}} specifies a full class name of a class declared in the application that implements the EncryptionMaterialsProvider interface; for example, {{com.mycompany.MyS3KeyProvider}}. | 
| Local disk encryption parameters | 
| "LocalDiskEncryptionConfiguration" | Specifies the key provider and corresponding values to be used for local disk encryption. | 
| "EnableEbsEncryption": true \| false | Specify true to enable EBS encryption. EBS encryption encrypts the EBS root device volume and attached storage volumes. To use EBS encryption, you must specify AwsKms as your EncryptionKeyProviderType. | 
| "EncryptionKeyProviderType": "AwsKms" \| "Custom" | Specifies the key provider. If AwsKms is specified, an KMS key ARN must be specified as the AwsKmsKey value. If Custom is specified, S3Object and EncryptionKeyProviderClass values must be specified. | 
| "AwsKmsKey : "{{MyKeyARN}}" | Required only when AwsKms is specified for Type. {{MyKeyARN}} must be a fully specified ARN to a key (for example, arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-456789012123). | 
| "S3Object" : "{{JarLocation}}" | Required only when CSE-Custom is specified for CertificateProviderType. {{JarLocation}} provides the location in Amazon S3 to a JAR file. The format can be a path (for example, s3://MyConfig/artifacts/MyKeyProvider.jar) or an ARN (for example, arn:aws:s3:::Code/MyKeyProvider.jar). | 
| `"EncryptionKeyProviderClass" : "{{MyLocalDiskKeyClassID}}"` | Required only when Custom is specified for Type. {{MyLocalDiskKeyClassID}} specifies a full class name of a class declared in the application that implements the EncryptionMaterialsProvider interface; for example, {{com.mycompany.MyLocalDiskKeyProvider}}. | 
| **EMR WAL encryption parameters** | 
| --- |
| "EMRWALEncryptionConfiguration"  | Specifies the value for EMR WAL encryption. | 
| "AwsKmsKey"  | Specifies the CMK Key Id Arn. | 

## Configure Kerberos authentication
<a name="emr-security-configuration-kerberos"></a>

A security configuration with Kerberos settings can only be used by a cluster that is created with Kerberos attributes or an error occurs. For more information, see [Use Kerberos for authentication with Amazon EMR](emr-kerberos.md). Kerberos is only available in Amazon EMR release version 5.10.0 and later.

### Specifying Kerberos settings using the console
<a name="emr-security-configuration-console-kerberos"></a>

Choose options under **Kerberos authentication** according to the following guidelines.


<table>
<thead>
  <tr><th colspan="3">Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Kerberos</b></td><td>Specifies that Kerberos is enabled for clusters that use this security configuration. If a cluster uses this security configuration, the cluster must also have Kerberos settings specified or an error occurs.</td></tr>
  <tr><td rowspan="2"><b>Provider</b></td><td colspan="2"><b>Cluster-dedicated KDC</b></td><td>Specifies that Amazon EMR creates a KDC on the primary node of any cluster that uses this security configuration. You specify the realm name and KDC admin password when you create the cluster.<br />You can reference this KDC from other clusters, if required. Create those clusters using a different security configuration, specify an external KDC, and use the realm name and KDC admin password that you specify for the cluster-dedicated KDC.</td></tr>
  <tr><td colspan="2"><b>External KDC</b></td><td>Available only with Amazon EMR 5.20.0 and later. Specifies that clusters using this security configuration authenticate Kerberos principals using a KDC server outside the cluster. A KDC is not created on the cluster. When you create the cluster, you specify the realm name and KDC admin password for the external KDC.</td></tr>
  <tr><td colspan="3"> <b>Ticket Lifetime</b></td><td>Optional. Specifies the period for which a Kerberos ticket issued by the KDC is valid on clusters that use this security configuration.<br />Ticket lifetimes are limited for security reasons. Cluster applications and services auto-renew tickets after they expire. Users who connect to the cluster over SSH using Kerberos credentials need to run <code>kinit</code> from the primary node command line to renew after a ticket expires.</td></tr>
  <tr><td colspan="3"><b>Cross-realm trust</b></td><td>Specifies a cross-realm trust between a cluster-dedicated KDC on clusters that use this security configuration and a KDC in a different Kerberos realm.<br />Principals (typically users) from another realm are authenticated to clusters that use this configuration. Additional configuration in the other Kerberos realm is required. For more information, see <a href="emr-kerberos-cross-realm.md">Tutorial: Configure a cross-realm trust with an Active Directory domain</a>.</td></tr>
  <tr><td rowspan="4">Cross-realm trust properties</td><td colspan="2"> <b>Realm</b></td><td>Specifies the Kerberos realm name of the other realm in the trust relationship. By convention, Kerberos realm names are the same as the domain name but in all capital letters.</td></tr>
  <tr><td colspan="2"> <b>Domain</b></td><td>Specifies the domain name of the other realm in the trust relationship.</td></tr>
  <tr><td colspan="2"> <b>Admin server</b></td><td>Specifies the fully qualified domain name (FQDN) or IP address of the admin server in the other realm of the trust relationship. The admin server and KDC server typically run on the same machine with the same FQDN, but communicate on different ports.<br />If no port is specified, port 749 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:749</code>).</td></tr>
  <tr><td colspan="2"> <b>KDC server</b></td><td>Specifies the fully qualified domain name (FQDN) or IP address of the KDC server in the other realm of the trust relationship. The KDC server and admin server typically run on the same machine with the same FQDN, but use different ports.<br />If no port is specified, port 88 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:88</code>).</td></tr>
  <tr><td colspan="3"><b>External KDC</b></td><td>Specifies that clusters external KDC is used by the cluster. </td></tr>
  <tr><td rowspan="6">External KDC properties</td><td colspan="2"><b>Admin server</b></td><td>Specifies the fully qualified domain name (FQDN) or IP address of the external admin server. The admin server and KDC server typically run on the same machine with the same FQDN, but communicate on different ports.<br />If no port is specified, port 749 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:749</code>).</td></tr>
  <tr><td colspan="2"><b>KDC server</b></td><td>Specifies the fully qualified domain name (FQDN) of the external KDC server. The KDC server and admin server typically run on the same machine with the same FQDN, but use different ports.<br />If no port is specified, port 88 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:88</code>).</td></tr>
  <tr><td colspan="2"><b>Active Directory Integration</b></td><td>Specifies that Kerberos principal authentication is integrated with a Microsoft Active Directory domain.</td></tr>
  <tr><td rowspan="3">Active Directory integration properties</td><td><b>Active Directory realm</b></td><td>Specifies the Kerberos realm name of the Active Directory domain. By convention, Kerberos realm names are typically the same as the domain name but in all capital letters.</td></tr>
  <tr><td><b>Active Directory domain</b></td><td>Specifies the Active Directory domain name.</td></tr>
  <tr><td><b>Active Directory server</b></td><td>Specifies the fully qualified domain name (FQDN) of the Microsoft Active Directory domain controller.</td></tr>
</tbody>
</table>


### Specifying Kerberos settings using the AWS CLI
<a name="emr-kerberos-cli-parameters"></a>

The following reference table shows JSON parameters for Kerberos settings in a security configuration. For example configurations, see, [Configuration examples](emr-kerberos-config-examples.md).


<table>
<thead>
  <tr><th colspan="6">Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="6"><code>"AuthenticationConfiguration": {</code></td><td>Required for Kerberos. Specifies that an authentication configuration is part of this security configuration.</td></tr>
  <tr><td rowspan="22"> </td><td colspan="5"><code></code><code>"KerberosConfiguration": {</code></td><td>Required for Kerberos. Specifies Kerberos configuration properties.</td></tr>
  <tr><td rowspan="20"> </td><td colspan="4"><code></code><code>"Provider": "ClusterDedicatedKdc",</code><br /><code></code>—<i>or</i>—<br /><code></code><code>"Provider: "ExternalKdc",</code></td><td><code>ClusterDedicatedKdc</code> specifies that Amazon EMR creates a KDC on the primary node of any cluster that uses this security configuration. You specify the realm name and KDC admin password when you create the cluster. You can reference this KDC from other clusters, if required. Create those clusters using a different security configuration, specify an external KDC, and use the realm name and KDC admin password that you specified when you created the cluster with the cluster-dedicated KDC.<br /><code>ExternalKdc</code> specifies that the cluster uses an external KDC. Amazon EMR does not create a KDC on the primary node. A cluster that uses this security configuration must specify the realm name and KDC admin password of the external KDC. </td></tr>
  <tr><td colspan="4"><code>"ClusterDedicatedKdcConfiguration": {</code></td><td>Required when <code>ClusterDedicatedKdc</code> is specified.</td></tr>
  <tr><td rowspan="7"></td><td colspan="3"><code>"TicketLifetimeInHours": 24,</code></td><td>Optional. Specifies the period for which a Kerberos ticket issued by the KDC is valid on clusters that use this security configuration.<br />Ticket lifetimes are limited for security reasons. Cluster applications and services auto-renew tickets after they expire. Users who connect to the cluster over SSH using Kerberos credentials need to run <code>kinit</code> from the primary node command line to renew after a ticket expires.</td></tr>
  <tr><td colspan="3"><code>"CrossRealmTrustConfiguration": {</code></td><td>Specifies a cross-realm trust between a cluster-dedicated KDC on clusters that use this security configuration and a KDC in a different Kerberos realm.<br />Principals (typically users) from another realm are authenticated to clusters that use this configuration. Additional configuration in the other Kerberos realm is required. For more information, see <a href="emr-kerberos-cross-realm.md">Tutorial: Configure a cross-realm trust with an Active Directory domain</a>.</td></tr>
  <tr><td rowspan="4"></td><td colspan="2"><code>"Realm": "KDC2.COM",</code></td><td>Specifies the Kerberos realm name of the other realm in the trust relationship. By convention, Kerberos realm names are the same as the domain name but in all capital letters.</td></tr>
  <tr><td colspan="2"><code>"Domain": "kdc2.com",</code></td><td>Specifies the domain name of the other realm in the trust relationship.</td></tr>
  <tr><td colspan="2"><code>"AdminServer": "kdc.com:749",</code></td><td>Specifies the fully qualified domain name (FQDN) or IP address of the admin server in the other realm of the trust relationship. The admin server and KDC server typically run on the same machine with the same FQDN, but communicate on different ports.<br />If no port is specified, port 749 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:749</code>).</td></tr>
  <tr><td colspan="2"><code>"KdcServer": "kdc.com:88"</code></td><td>Specifies the fully qualified domain name (FQDN) or IP address of the KDC server in the other realm of the trust relationship. The KDC server and admin server typically run on the same machine with the same FQDN, but use different ports.<br />If no port is specified, port 88 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:88</code>).</td></tr>
  <tr><td colspan="4"><code>}</code></td></tr>
  <tr><td colspan="5"><code>}</code></td></tr>
  <tr><td colspan="4">"ExternalKdcConfiguration": {</td><td>Required when <code>ExternalKdc</code> is specified.</td></tr>
  <tr><td rowspan="8"></td><td colspan="3"><code>"TicketLifetimeInHours": 24,</code></td><td>Optional. Specifies the period for which a Kerberos ticket issued by the KDC is valid on clusters that use this security configuration.<br />Ticket lifetimes are limited for security reasons. Cluster applications and services auto-renew tickets after they expire. Users who connect to the cluster over SSH using Kerberos credentials need to run <code>kinit</code> from the primary node command line to renew after a ticket expires.</td></tr>
  <tr><td colspan="3"><code>"KdcServerType": "Single",</code></td><td>Specifies that a single KDC server is referenced. <code>Single</code> is currently the only supported value.</td></tr>
  <tr><td colspan="3">"AdminServer": "{{kdc.com:749}}",</td><td>Specifies the fully qualified domain name (FQDN) or IP address of the external admin server. The admin server and KDC server typically run on the same machine with the same FQDN, but communicate on different ports.<br />If no port is specified, port 749 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:749</code>).</td></tr>
  <tr><td colspan="3">"KdcServer": "{{kdc.com:88}}",</td><td>Specifies the fully qualified domain name (FQDN) of the external KDC server. The KDC server and admin server typically run on the same machine with the same FQDN, but use different ports.<br />If no port is specified, port 88 is used, which is the Kerberos default. Optionally, you can specify the port (for example, <code>domain.example.com:88</code>).</td></tr>
  <tr><td colspan="3"><code>"AdIntegrationConfiguration": {</code></td><td>Specifies that Kerberos principal authentication is integrated with a Microsoft Active Directory domain.</td></tr>
  <tr><td rowspan="3"> </td><td colspan="2"><code>"AdRealm": "AD.DOMAIN.COM",</code></td><td>Specifies the Kerberos realm name of the Active Directory domain. By convention, Kerberos realm names are typically the same as the domain name but in all capital letters.</td></tr>
  <tr><td colspan="2"><code>"AdDomain": "ad.domain.com"</code></td><td>Specifies the Active Directory domain name.</td></tr>
  <tr><td colspan="2"><code>"AdServer": "ad.domain.com"</code></td><td>Specifies the fully qualified domain name (FQDN) of the Microsoft Active Directory domain controller.</td></tr>
  <tr><td colspan="4"><code>}</code></td><td></td></tr>
  <tr><td colspan="5"><code>}</code></td><td></td></tr>
  <tr><td colspan="6"><code>}</code></td><td></td></tr>
  <tr><td colspan="7"><code>}</code></td></tr>
</tbody>
</table>


## Configure IAM roles for EMRFS requests to Amazon S3
<a name="emr-security-configuration-emrfs"></a>

IAM roles for EMRFS allow you to provide different permissions to EMRFS data in Amazon S3. You create mappings that specify an IAM role that is used for permissions when an access request contains an identifier that you specify. The identifier can be a Hadoop user or role, or an Amazon S3 prefix. 

For more information, see [Configure IAM roles for EMRFS requests to Amazon S3](emr-emrfs-iam-roles.md).

### Specifying IAM roles for EMRFS using the AWS CLI
<a name="w2aac32c17b9c15b7"></a>

The following is an example JSON snippet for specifying custom IAM roles for EMRFS within a security configuration. It demonstrates role mappings for the three different identifier types, followed by a parameter reference. 

```
{
  "AuthorizationConfiguration": {
    "EmrFsConfiguration": {
      "RoleMappings": [{
        "Role": "{{arn:aws:iam::123456789101:role/allow_EMRFS_access_for_user1}}",
        "IdentifierType": "User",
        "Identifiers": [ "{{user1}}" ]
      },{
        "Role": "{{arn:aws:iam::123456789101:role/allow_EMRFS_access_to_demo_s3_buckets}}",
        "IdentifierType": "Prefix",
        "Identifiers": [ "{{s3://amzn-s3-demo-bucket1/","s3://amzn-s3-demo-bucket2/}}" ]
      },{
        "Role": "{{arn:aws:iam::123456789101:role/allow_EMRFS_access_for_AdminGroup}}",
        "IdentifierType": "Group",
        "Identifiers": [ "{{AdminGroup}}" ]
      }]
    }
  }
}
```


| Parameter | Description | 
| --- | --- | 
| `"AuthorizationConfiguration":` | Required. | 
|  `"EmrFsConfiguration":` | Required. Contains role mappings. | 
|   `"RoleMappings":` | Required. Contains one or more role mapping definitions. Role mappings are evaluated in the top-down order that they appear. If a role mapping evaluates as true for an EMRFS call for data in Amazon S3, no further role mappings are evaluated and EMRFS uses the specified IAM role for the request. Role mappings consist of the following required parameters: | 
|    `"Role":` | Specifies the ARN identifier of an IAM role in the format `arn:aws:iam::{{account-id}}:role/{{role-name}}`. This is the IAM role that Amazon EMR assumes if the EMRFS request to Amazon S3 matches any of the `Identifiers` specified. | 
|    `"IdentifierType":` | Can be one of the following:+ `"User"` specifies that the identifiers are one or more Hadoop users, which can be Linux account users or Kerberos principals. When the EMRFS request originates with the user or users specified, the IAM role is assumed. <br />+ `"Prefix"` specifies that the identifier is an Amazon S3 location. The IAM role is assumed for calls to the location or locations with the specified prefixes. For example, the prefix` s3://amzn-s3-demo-bucket/` matches` s3://amzn-s3-demo-bucket/mydir `and `s3://amzn-s3-demo-bucket/yetanotherdir`.<br />+ `"Group"` specifies that the identifiers are one or more [Hadoop groups](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/GroupsMapping.html). The IAM role is assumed if the request originates from a user in the specified group or groups.  | 
|    `"Identifiers":` | Specifies one or more identifiers of the appropriate identifier type. Separate multiple identifiers by commas with no spaces. | 

## Configure metadata service requests to Amazon EC2 instances
<a name="emr-security-configuration-imdsv2"></a>

Instance metadata is data about your instance that you can use to configure or manage the running instance. You can access instance metadata from a running instance using one of the following methods:
+ Instance Metadata Service Version 1 (IMDSv1) - a request/response method
+ Instance Metadata Service Version 2 (IMDSv2) - a session-oriented method

While Amazon EC2 supports both IMDSv1 and IMDSv2, Amazon EMR supports IMDSv2 in Amazon EMR 5.23.1, 5.27.1, 5.32 or later, and 6.2 or later. In these releases, Amazon EMR components use IMDSv2 for all IMDS calls. For IMDS calls in your application code, you can use both IMDSv1 and IMDSv2, or configure the IMDS to use only IMDSv2 for added security. When you specify that IMDSv2 must be used, IMDSv1 no longer works.

For more information, see [Configure the instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.

**Note**  
In earlier Amazon EMR 5.x or 6.x releases, turning off IMDSv1 causes cluster startup failure as Amazon EMR components use IMDSv1 for all IMDS calls. When turning off IMDSv1, please ensure that any custom software that utilizes IMDSv1 is updated to IMDSv2.

### Specifying instance metadata service configuration using the AWS CLI
<a name="w2aac32c17b9c17c13"></a>

The following is an example JSON snippet for specifying Amazon EC2 instance metadata service (IMDS) within a security configuration. Using a custom security configuration is optional.

```
{
  "InstanceMetadataServiceConfiguration" : {
      "MinimumInstanceMetadataServiceVersion": integer,
      "HttpPutResponseHopLimit": integer
   }
}
```


| Parameter | Description | 
| --- | --- | 
| `"InstanceMetadataServiceConfiguration":` | If you don't specify IMDS within a security configuration and use an Amazon EMR release that requires IMDSv1, Amazon EMR defaults to using IMDSv1 as the minimum instance metadata service version. If you want to use your own configuration, both of the following parameters are required. | 
|  `"MinimumInstanceMetadataServiceVersion":` | Required. Specify `1` or `2`. A value of `1` allows IMDSv1 and IMDSv2. A value of `2` allows only IMDSv2. | 
|  `"HttpPutResponseHopLimit":` | Required. The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel. Default: `1`. Specify an integer from `1` to `64`. | 

### Specifying instance metadata service configuration using the console
<a name="emr-security-configuration-imdsv2-console"></a>

You can configure the use of IMDS for a cluster when you launch it from the Amazon EMR console.

**To configure the use of IMDS using the console:**

1. When creating a new security configuration on the **Security configurations** page, select **Configure EC2 Instance metadata service** under the **EC2 Instance Metadata Service** setting. This configuration is supported only in Amazon EMR 5.23.1, 5.27.1, 5.32 or later, and 6.2 or later.

1. For the **Minimum Instance Metadata Service Version** option, select either:
   + **Turn off IMDSv1 and only allow IMDSv2**, if you want to allow only IMDSv2 on this cluster. See [Transition to using instance metadata service version 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#instance-metadata-transition-to-version-2) in the *Amazon EC2 User Guide*.
   + **Allow both IMDSv1 and IMDSv2 on cluster**, if you want to allow IMDSv1 and session-oriented IMDSv2 on this cluster.

1. For IMDSv2, you can also configure the allowable number of network hops for the metadata token by setting the **HTTP put response hop limit** to an integer between `1` and `64`.

For more information, see [Configure the instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.

See [Configure instance details](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html#configure_instance_details_step) and [Configure the instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.