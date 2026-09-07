

# MASEC 2: What security tools (AWS or third-party) do you use?
<a name="masec-2"></a>

 Security is a shared responsibility. It is important to understand if the seller is using AWS services to find and remediate vulnerabilities, misconfigurations, and resources. Are they using third party tools to do this? 

## MASEC02-BP01 Use an AWS-defined process to report vulnerabilities
<a name="masec02-bp01"></a>

 AWS takes security very seriously and investigates all reported vulnerabilities (for more detail, see [AWS Cloud Security](https://aws.amazon.com/security/)). 

## MASEC02-BP02 Use AWS services with self-service within the existing management console
<a name="masec02-bp02"></a>

 On AWS, you can automate manual security tasks so you can shift your focus to scaling and innovating your business. 

## MASEC02-BP03 Use third-party security tools when necessary due to integration with on-premises resources
<a name="masec02-bp03"></a>

 Amazon Security Lake is a fully-managed security data lake service. You can use Security Lake to automatically centralize security data from AWS and third-party sources into a data lake that's stored in your AWS account. Security Lake helps you analyze security data, so you can get a more complete understanding of your security posture across the entire organization. You can also use Security Lake to improve the protection of your workloads, applications, and data. 

## MASEC02-BP04 Migrate to a common set of tools, including partner tools from marketplace
<a name="masec02-bp04"></a>

The AWS Shared Responsibility Model (SRM) makes it easy to understand various choices for protecting unique AWS environment, and [access partner resources](https://aws.amazon.com/partners/featured/security/) that can help you implement end-to-end security quickly and easily.

## MASEC02-BP05 Create a common policy for auditing and rotating credentials
<a name="masec02-bp05"></a>

 For human identities, you should require users to change their passwords periodically and retire access keys in favor of temporary credentials. For machine identities, rely on temporary credentials using IAM roles. For situations where this is not possible, frequent auditing and rotating access keys is necessary. 