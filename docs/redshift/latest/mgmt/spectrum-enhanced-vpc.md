

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Querying data lake tables with enhanced VPC routing
<a name="spectrum-enhanced-vpc"></a>

When enhanced VPC routing is turned on, Amazon Redshift routes traffic through your VPC. Data lake tables store their data in Amazon S3 and their metadata in the AWS Glue Data Catalog, both of which are outside your VPC. For data lake queries to succeed, your cluster or workgroup must be able to reach Amazon S3 and AWS Glue. If your data lake tables are managed by AWS Lake Formation, it must also be able to reach Lake Formation. Enhanced VPC routing affects the way that Amazon Redshift accesses these external resources, so queries might fail unless you configure your VPC correctly.

Create the following VPC endpoints in the VPC and subnets where your cluster or workgroup runs, associating them with the appropriate route tables. These endpoints are required for both the integrated data lake query engine and Amazon Redshift Spectrum:
+ **Amazon S3 gateway endpoint** – Gives your cluster or workgroup a route through the AWS network to Amazon S3 to read data lake data files. For steps, see [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) in the *Amazon VPC User Guide*.
+ **AWS Glue interface endpoint** – Gives your cluster or workgroup a route to the AWS Glue Data Catalog to resolve data lake schemas and tables. For steps, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.
+ **AWS Lake Formation interface endpoint** – Required only if your data lake tables are managed by AWS Lake Formation. Gives your cluster or workgroup a route to Lake Formation. For steps, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.

The endpoint configuration is the same regardless of how you query external tables, but the way traffic is routed differs depending on the query engine. The following sections describe the behavior for the integrated data lake query engine on RG provisioned clusters and Amazon Redshift Serverless, and for Redshift Spectrum on RA3 and DC2 provisioned clusters.

## Integrated data lake query engine for RG provisioned clusters and Amazon Redshift Serverless
<a name="spectrum-enhanced-vpc-integrated-engine"></a>

RG provisioned clusters and Amazon Redshift Serverless include an integrated data lake query engine. This engine runs on the cluster's or workgroup's own compute resources, within your VPC. When enhanced VPC routing is turned on and the required VPC endpoints are in place, access to Amazon S3 and AWS Glue originates from your in-VPC compute and flows through those VPC endpoints. This traffic stays within your VPC boundary and on the AWS network. This access is authorized based on the IAM role that is attached to your cluster or workgroup. To further manage this traffic, you can modify the IAM role and the policy attached to the Amazon S3 bucket.

## Amazon Redshift Spectrum for RA3 and DC2 provisioned clusters
<a name="spectrum-enhanced-vpc-spectrum"></a>

Redshift Spectrum runs on AWS managed resources that are owned by Amazon Redshift but are outside your VPC. As a result, even when enhanced VPC routing is turned on, the traffic that Redshift Spectrum sends to Amazon S3 does not pass through your VPC, but the cluster still requires the Amazon S3 and AWS Glue VPC endpoints described earlier to run data lake queries.

Traffic between Redshift Spectrum and Amazon S3 is securely routed through the AWS private network, outside of your VPC. In-flight traffic is signed using Amazon Signature Version 4 protocol (SIGv4) and encrypted using HTTPS. This traffic is authorized based on the IAM role that is attached to your Amazon Redshift cluster. To further manage Redshift Spectrum traffic, you can modify your cluster's IAM role and your policy attached to the Amazon S3 bucket.

## Permissions policy configuration for data lake queries
<a name="spectrum-enhanced-vpc-considerations"></a>

Consider the following when querying data lake tables in Amazon S3: 
+ [Amazon S3 bucket access policies and IAM roles](#spectrum-enhanced-vpc-considerations-policies)
+ [Permissions for assuming the IAM role](#spectrum-enhanced-vpc-considerations-cluster-role)
+ [Logging and auditing Amazon S3 access](#spectrum-enhanced-vpc-considerations-logging-s3)
+ [Access to AWS Glue or Amazon Athena](#spectrum-enhanced-vpc-considerations-glue-access)

### Amazon S3 bucket access policies and IAM roles
<a name="spectrum-enhanced-vpc-considerations-policies"></a>

You can control access to data in your Amazon S3 buckets by using a bucket policy attached to the bucket and by using an IAM role attached to a provisioned cluster. 

Redshift Spectrum on provisioned clusters can't access data stored in Amazon S3 buckets that use a bucket policy that restricts access to only specified VPC endpoints. Instead, use a bucket policy that restricts access to only specific principals, such as a specific AWS account or specific users. The integrated data lake query engine on RG provisioned clusters and Amazon Redshift Serverless can access such buckets when enhanced VPC routing is turned on, because its Amazon S3 access flows through your VPC endpoints. 

For the IAM role that is granted access to the bucket, use a trust relationship that allows the role to be assumed only by the Amazon Redshift service principal. When attached to your cluster, the role can be used only in the context of Amazon Redshift and can't be shared outside of the cluster. For more information, see [Restricting access to IAM roles](authorizing-redshift-service-database-users.md). A service control policy (SCP) can also be used to further restrict the role, see [Prevent IAM users and roles from making specified changes, with an exception for a specified admin role](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-restricts-with-exception) in the *AWS Organizations User Guide*.

**Note**  
To use Redshift Spectrum, no IAM policies blocking the use of Amazon S3 presigned URLs can be in place. The presigned URLs generated by Amazon Redshift Spectrum are valid for 1 hour so that Amazon Redshift has enough time to load all the files from the Amazon S3 bucket. A unique presigned URL is generated for each file scanned by Redshift Spectrum. For bucket policies that include an `s3:signatureAge` action, make sure to set the value to at least 3,600,000 milliseconds.

The following example bucket policy permits access to the specified bucket owned by AWS account `123456789012`. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "BucketPolicyForSpectrum",
            "Effect": "Allow",
            "Principal": {
                "AWS": ["arn:aws:iam::123456789012:role/redshift"]
            },
            "Action": [
                "s3:GetObject",
                "s3:ListBucketVersions",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ]
        }
    ]
}
```

------

### Permissions for assuming the IAM role
<a name="spectrum-enhanced-vpc-considerations-cluster-role"></a>

The role attached to your cluster should have a trust relationship that permits it to be assumed only by the Amazon Redshift service, as shown following.

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
        "Service": "redshift.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

For more information, see [IAM Policies for Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-iam-policies.html) in the *Amazon Redshift Database Developer Guide*.

### Logging and auditing Amazon S3 access
<a name="spectrum-enhanced-vpc-considerations-logging-s3"></a>

One benefit of using Amazon Redshift enhanced VPC routing is that all COPY and UNLOAD traffic is logged in the VPC flow logs. Traffic originating from Redshift Spectrum to Amazon S3 doesn't pass through your VPC, so it isn't logged in the VPC flow logs. When Redshift Spectrum accesses data in Amazon S3, it performs these operations in the context of the AWS account and respective role privileges. You can log and audit Amazon S3 access using server access logging in AWS CloudTrail and Amazon S3. 

Ensure that the S3 IP ranges are added to your allow list. To learn more about the required S3 IP ranges, see [Network isolation](https://docs.aws.amazon.com/redshift/latest/mgmt/security-network-isolation.html#network-isolation).

**AWS CloudTrail Logs** 

To trace all access to objects in Amazon S3, including Redshift Spectrum access, enable CloudTrail logging for Amazon S3 objects. 

You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. For more information, see [Getting Started with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-getting-started.html). 

By default, CloudTrail tracks only bucket-level actions. To track object-level actions (such as `GetObject`), enable data and management events for each logged bucket. 

**Amazon S3 Server Access Logging** 

Server access logging provides detailed records for the requests that are made to a bucket. Access log information can be useful in security and access audits. For more information, see [How to Enable Server Access Logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html#server-access-logging-overview) in the *Amazon Simple Storage Service User Guide.*

For more information, see the AWS Security blog post [How to Use Bucket Policies and Apply Defense-in-Depth to Help Secure Your Amazon S3 Data](https://aws.amazon.com/blogs/security/how-to-use-bucket-policies-and-apply-defense-in-depth-to-help-secure-your-amazon-s3-data/). 

### Access to AWS Glue or Amazon Athena
<a name="spectrum-enhanced-vpc-considerations-glue-access"></a>

Both Redshift Spectrum and the integrated data lake query engine access your data catalog in AWS Glue or Athena. Another option is to use a dedicated Hive metastore for your data catalog. 

The recommended way to reach the AWS Glue Data Catalog is to create an interface VPC endpoint (AWS PrivateLink) for AWS Glue. When you use a VPC interface endpoint, communication between your VPC and AWS Glue is routed within the AWS network. For more information, see [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint).

Alternatively, to reach the public endpoints for AWS Glue and Athena, configure your VPC with an internet gateway or NAT gateway, and configure your VPC security groups to allow outbound traffic to those public endpoints. You can configure the following pathways in your VPC: 
+ **Internet gateway** –To connect to AWS services outside your VPC, you can attach an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) to your VPC subnet, as described in the *Amazon VPC User Guide.* To use an internet gateway, a provisioned cluster must have a public IP address to allow other services to communicate with it. 
+ **NAT gateway **–To connect to an Amazon S3 bucket in another AWS Region or to another service within the AWS network, configure a [network address translation (NAT) gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html), as described in the *Amazon VPC User Guide.* Use this configuration also to access a host instance outside the AWS network.