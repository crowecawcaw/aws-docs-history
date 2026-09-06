

# Product details
<a name="product-columns"></a>

The **product** columns provide metadata about the product that incurred the expense, and the line item. The product columns are dynamic, and their visibility in Cost and Usage Reports depends on the usage of product in the billing period. The pricing columns are based off of the AWS Price List Service API. AWS Price List Service API doesn't include Spot Instances, products in AWS Marketplace, upfront annual subscription fees (`Fee`), and monthly recurring fees (`RIFee`).

 [A](#A) \| B \| [C](#C) \| [D](#D) \| [E](#E) \| [F](#F) \| [G](#G) \| H \| [I](#I) \| J \| K \| [L](#L) \| [M](#M) \| [N](#N) \| [O](#O) \| [P](#P) \| Q \| [R](#R) \| [S](#S) \| [T](#T) \| [U](#U) \| [V](#V) \| [W](#W) \| XYZ 

## A
<a name="product-details-A"></a>

### product/APICalls
<a name="product-details-A-apicalls"></a>
+ **Description:** Describes the number of APIs the DevOps Guru service uses to enable the DevOps Guru service.
+ **Sample values:** `100`, `500`, `10000`
+ **Services:**
  + Amazon DevOps Guru

### product/attachmentType
<a name="product-details-A-attachmenttype"></a>
+ **Description:** Describes the type of attachment to Transit Gateway or Cloud WAN service.
+ **Sample values:** `VPC`, `AWS Site-to-Site VPN`, `AWS DirectConnect`, `Connect`, `Transit Gateway`
+ **Services:**
  + Amazon Virtual Private Cloud
  + AWS Cloud WAN

### product/availability
<a name="product-details-A-availability"></a>
+ **Description:** Describes the availability of your various AWS storage options. 
+ **Sample values:** `99.99%`, `99.5%`
+ **Services:**
  + Amazon Glacier
  + Amazon S3
  + AWS Elemental MediaStore
  + AWS RoboMaker

## C
<a name="product-details-C"></a>

### product/cacheType
<a name="product-details-C-cachetype"></a>
+ **Description:** Describes the provision opted by the customer on HDD-based file systems for a read-only SSD cache to improve performance for the frequently read data.

  For example, RC20 indicates the presence of a read-only SSD cache that is automatically sized to 20 percent of the file system's HDD storage capacity.
+ **Sample values:** `RC20`, `N/A`
+ **Services:**
  + Amazon FSx

### product/capacitystatus
<a name="product-details-C-capacity"></a>
+ **Description:** Describes the status of your capacity reservations. 
+ **Sample values:** `UnusedCapacityReservation`, `AllocatedCapacityReservation`, `Used`
+ **Services:**
  + Amazon EC2

### product/clockspeed
<a name="product-details-C-clock"></a>
+ **Description:** Describes the operating speed of your AWS instances. 
+ **Sample values:** `2.4 GHz`, `2.6 GHz`
+ **Services:**
  + Amazon DocumentDB
  + Amazon EC2
  + Amazon MQ
  + Amazon Neptune
  + Amazon RDS
  + AWS Database Migration Service

### product/component
<a name="product-details-C-component"></a>
+ **Description:** Maps to features in SageMaker AI.

  For example, if a user is running a SageMaker AI notebook, the product will have a component attribute of Notebook. If the user has deployed and hosted their model for inference, they will see product with component attribute of Hosting.
+ **Sample values:** `Notebook`, `Hosting`
+ **Services:**
  + Amazon SageMaker AI

## D
<a name="product-details-D"></a>

### product/databaseedition
<a name="product-details-D-databaseedition"></a>
+ **Description:** Describes the database software suitable for different development, deployment scenarios, and specific application purposes.
+ **Services:**
  + Amazon RDS

### product/dataTransfer
<a name="product-details-D-dataTransfer"></a>
+ **Description:** An AWS data transfer occurs whenever data is moved to from AWS to the internet, or moved between AWS instances across their respective Regions or Availability Zones. Interregional and inter availability zone data transfers incur costs, metered per Gigabyte.
+ **Services:**
  + AWS Systems Manager

### product/dedicatedEbsThroughput
<a name="product-details-D-dedicated"></a>
+ **Description:** Describes the dedicated throughput between your instances (for example, Amazon EC2 instances and Amazon EBS volumes), with options between 500 and 10,000 megabits per second (Mbps) depending on the instance type used. The dedicated throughput minimizes contention between Amazon EBS I/O and other traffic from your EC2 instance, providing the best performance for your Amazon EBS volumes.
+ ** Sample values: ** `200 Mbps`, `Upto 5000 Mbps`
+ **Services:**
  + Amazon EC2
  + Amazon Neptune
  + Amazon RDS

### product/deploymentoption
<a name="product-details-D-deploymentoption"></a>
+ **Description:** Describes where the infrastructure for the environment is located. The deployment models for AWS cloud are `public`, `on-premise`, and `hybrid`.
+ ** Sample values: ** `Multi-AZ`, `Single-AZ`
+ **Services:**
  + Amazon MQ
  + Amazon Neptune
  + Amazon RDS

### product/description
<a name="product-details-D-description"></a>
+ **Description:** The description of the specific AWS service.
+ **Services:**
  + AWS CodePipeline
  + AWS Device Farm
  + AWS Elemental MediaConvert
  + AWS Elemental MediaStore

### product/destinationCountryISOCode
<a name="product-details-D-destinationcountryisocode"></a>
+ **Description:** Describes the destination Country ISO 3166-1 alpha-2 code to which the SMS was sent to.

  For reference, visit [https://en.wikipedia.org/wiki/ISO\_3166-1\_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
+ ** Sample values:** `FR`, `CO`, `MA`, `KN`, `PL`, `LV`, `LA`, `GB`, `ID`, `KR`, `MY`, `BR`, `MM`, `CA`, `VN`, `BD`, `BJ`, `AU`, `HK`, `AM`, `CZ`, `UA`, `PH`, `TW`, `ES`, `DE`, `NG`, `FI`, `SG`, `TH`, `IL`, `TR`, `JP`, `IT`, `PR`, `RU`, `EE`
+ **Services:**
  + Amazon Simple Notification Service

### product/directconnectlocation
<a name="product-details-D-directconnectlocation"></a>
+ **Description:** Specifies the location where a private dedicated network connection from the customer to AWS exists.
+ ** Sample values: ** `Equinix DC1 - DC6`, `Equinix DC10 - DC11`, `Global Switch Singapore`
+ **Services:**
  + Direct Connect

### product/directorysize
<a name="product-details-D-directorysize"></a>
+ **Description:** The space on the disk that is used to store the meta information for the directory or folder.
+ **Services:**
  + Direct Connect

### product/directorytype
<a name="product-details-D-directorytype"></a>
+ **Description:** Specifies if the directory is a file or another directory.
+ **Services:**
  + Direct Connect

### product/directorytypedescription
<a name="product-details-D-directorytypedescription"></a>
+ **Description:** The meaningful name given to the directory.
+ **Services:**
  + Direct Connect

### product/disableactivationconfirmationemail
<a name="product-details-D-disableactivationconfirmationemail"></a>
+ **Description:** Active or deactivate the ability to send an email to confirm the activation of a service.

### product/durability
<a name="product-details-D-durability"></a>
+ **Description:** Describes the durability of objects over a given year. 
+ **Sample values:** `99.999999999%`, `N/A`, `99.99%`
+ **Services:**
  + Amazon Glacier
  + Amazon S3
  + AWS Elemental MediaStore

## E
<a name="product-details-E"></a>

### product/ebsOptimized
<a name="product-details-E-ebs"></a>
+ **Description:** Describes whether your Amazon EC2 instances are Amazon EBS–optimized. 
+ **Sample values:** `Yes`, `No`
+ **Services:**
  + Amazon EC2

### product/ecu
<a name="product-details-E-ecu"></a>
+ **Description:** Describes the EC2 Compute Unit (ECU) that provides the relative measure of the integer processing power of an Amazon EC2 instance. 
+ **Sample values:** `9`, `100`, `variable`
+ **Services:**
  + Amazon EC2
  + OpenSearch Service
  + Amazon GameLift Servers
  + Amazon Redshift

### product/endpointtype
<a name="product-details-E-endpointtype"></a>
+ **Description:** Describes the characteristics of the remote connection that a device connects to.

  For example, `REST` (representational state transfer) endpoints. A `REST` API (or `RESTful` API) is an application programming interface that conforms to the constraints of `REST` architectural style and you can interact with `RESTful` web services.
+ **Sample values:** `Ipsec`, `Amazon SQS`, `AWS Lambda`
+ **Services:**
  + Amazon SNS
  + Amazon VPC
  + Storage Gateway
  + Amazon Glacier

### product/enhancedNetworkingSupported
<a name="product-details-E-enhanced"></a>
+ **Description:** Describes whether your instance supports enhanced networking. Enhanced networking uses single root I/O virtualization (SR-IOV) to provide high-performance networking capabilities on supported instance types. 
+ **Sample values:** `Yes`, `No`
+ **Services:**
  + Amazon DocumentDB
  + Amazon EC2
  + Amazon Neptune
  + Amazon RDS
  + AWS Database Migration Service

## F
<a name="product-details-F"></a>

### product/filesystemtype
<a name="product-details-F-filesystemtype"></a>
+ **Description:** Describes the details of the local or remote storage device, and specifications of the operating system.

### product/findingGroup
<a name="product-details-F-findingGroup"></a>
+ **Description:** Specifies whether a finding stored in Security Hub is paid or free. If free, the reason may also be specified.
+ **Sample values:** `FreeFindingsIngestion-CrossRegion`, `FreeFindingsIngestion-FreeTier`, `FreeFindingsIngestion-FreeTrial`, `PaidFindingsIngestion`
+ **Services:**
  + AWS Security Hub

### product/findingSource
<a name="product-details-F-findingSource"></a>
+ **Description:** Specifies whether a finding was generated by a Security Hub control or by other partner security product.
+ **Sample values:** `SecurityHubProduct`, `OtherProduct`
+ **Services:**
  + AWS Security Hub

### product/freeUsageIncluded
<a name="product-details-F-freeUsageIncluded"></a>
+ **Description:** Free usage under AWS Free Tier is calculated each month across all Regions, and automatically applied to your bill. For example, you receive 750 Amazon EC2 Linux Micro Instance hours for free across all of the Regions you use. Not 750 hours per Region.
+ **Services:**
  + Amazon Inspector

### product/fromLocation
<a name="product-details-F-fromLoc"></a>
+ **Description:** Describes the location where the usage originated from.
+ **Sample values:** `External`, `US East (N. Virginia)`, `Global`
+ **Services:**
  + Amazon CloudFront
  + AWS DataTransfer

### product/fromRegionCode
<a name="product-details-F-fromRegionCode"></a>
+ **Description:** Describes the source Region code for the AWS service. For more information, see [product/regioncode](#product-details-R-regioncode).
+ **Sample values:** `ap-northeast-1`
+ **Services:**
  + Amazon RDS
  + Amazon EC2
  + Amazon VPC
  + Direct Connect

### product/fromLocationType
<a name="product-details-F-fromloctype"></a>
+ **Description:** Describes the location type where the usage originated from.
+ **Sample values:** `AWS Region`, `AWS Edge Location`
+ **Services:**
  + Direct Connect
  + AWS Elemental MediaConnect
  + Amazon CloudFront
  + Amazon Lightsail
  + AWS Shield

## G
<a name="product-details-G"></a>

### product/gpu
<a name="product-details-G-gpu"></a>
+ **Description:** Describes the number of GPUs. 
+ **Sample values:** `16`, `32` 
+ **Services:**
  + Amazon SageMaker AI
  + Amazon EC2

### product/gpuMemory
<a name="prodcut-details-G-gpuMem"></a>
+ **Description:** Describes your GPU memory details. 
+ **Sample values:** `16`, `32`
+ **Services:**
  + Amazon SageMaker AI
  + Amazon EC2

### product/group
<a name="prodcut-details-G-group"></a>
+ **Description:** A construct of several products that are similar by definition, or grouped together. For example, the Amazon EC2 team can categorize their products into shared instances, dedicated host, and dedicated usage.
+ **Services:**
  + AWS Certificate Manager
  + AWS CodeCommit
  + AWS Glue
  + AWS IoT Analytics
  + AWS Lambda

### product/groupdescription
<a name="prodcut-details-G-groupdescription"></a>
+ **Description:** A simplified name given to a product group.
+ **Services:**
  + AWS Budgets
  + AWS Certificate Manager
  + AWS Lambda
  + Amazon SQS

## I
<a name="product-details-I"></a>

### product/insightsType
<a name="product-details-I-insightstype"></a>
+ **Description:** Indicates the type of Insight event generated.
+ **Sample values:** `APICallVolume` 
+ **Services:**
  + CloudTrail

### product/instance
<a name="product-details-I-instance"></a>
+ **Description:** An Amazon EC2 instance is a virtual server in Amazon Elastic Compute Cloud (Amazon EC2) for running applications on the AWS infrastructure. You can choose an AMI provided by AWS, the user community, or through the AWS Marketplace.
+ **Sample values:** `T3` 
+ **Services:**
  + Amazon EC2

### product/instanceFamily
<a name="product-details-I-instanceFamily"></a>
+ **Description:** Describes your Amazon EC2 instance family. Amazon EC2 provides you with a large number of options across 10 different instance types, each with one or more size options, organized into distinct instance families optimized for different types of applications. 
+ **Sample values:** `General Purpose`, `Memory Optimized`, `Accelerated Computing` 
+ **Services:**
  + Amazon EC2
  + Amazon RDS
  + OpenSearch Service
  + Amazon ElastiCache
  + Amazon EMR

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/instanceSize
<a name="product-details-I-instancesize"></a>
+ **Description:** Indicates the instance size of a resource.
+ **Sample values:** `2vCPU`, `4vCPU`, `8vCPU`, `16vCPU` 
+ **Services:**
  + Amazon CodeCatalyst

### product/instanceType
<a name="prodcut-details-I-instancetype"></a>
+ **Description:** Describes the instance type, size, and family, which define the CPU, networking, and storage capacity of your instance. 
+ **Sample values:** `t2.small`, `m4.xlarge`, `t2.micro`, `m4.large`, `t2.large`
+ **Services:**
  + Amazon EC2
  + Amazon RDS
  + OpenSearch Service
  + Amazon ElastiCache
  + Amazon EMR

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/instanceTypeFamily
<a name="product-details-I-instancetypefamily"></a>
+ **Description:** The instance family that is associated with the given usage. 
+ **Sample values:** `t2`, `m4`, `m3`
+ **Services:**
  + Amazon DocumentDB
  + Amazon RDS

### product/integratingApi
<a name="product-details-I-integratingApi"></a>
+ **Description:** Application integration on AWS using service like Amazon API Gateway or no-code integration using Amazon AppFlow.

### product/integratingService
<a name="product-details-I-integratingService"></a>
+ **Description:** Application integration on AWS is a suite of services used to communicate between decoupled components within micro services, distributed systems, and serverless applications. You don’t need to refactor your entire architecture. Decoupling applications at any scale can reduce the impact of changes, making it easier to update, and faster to release new features.

### product/intelAvxAvailable
<a name="product-details-I-intelAvx"></a>
+ **Description:** Describes whether your process has the Intel Advanced Vector Extension instruction set. 
+ **Sample values:** `Yes`, `No`.
+ **Services:**
  + Amazon EC2

### product/intelAvx2Available
<a name="product-details-I-intelAvx2"></a>
+ **Description:** Describes whether your process has the Intel Advanced Vector Extension instruction set two. 
+ **Sample values:** `Yes`, `No`
+ **Services:**
  + Amazon EC2

### product/intelTurboAvailable
<a name="product-details-I-intelturbo"></a>
+ **Description:** Describes whether your core is allowed to use Intel Turbo Technology to increase frequency. 
+ **Sample values:** `Yes`, `No`
+ **Services:**
  + Amazon EC2

### product/invocation
<a name="product-details-I-invocation"></a>
+ **Description:** Describes the invocations that EventBridge Scheduler makes to an API or service.
+ **Sample values:** `Scheduled Invocation`
+ **Services:**
  + Amazon CloudWatch Events

## L
<a name="product-details-L"></a>

### product/licenseModel
<a name="product-details-L-license"></a>
+ **Description:** Describes the license model for your instance. 
+ **Sample value:** `license-included`, `bring-your-own-license`, `general-public-license`
+ **Services:**
  + Amazon AppStream
  + Amazon EC2
  + Amazon MQ
  + Amazon Neptune
  + Amazon RDS

### product/location
<a name="product-details-L-location"></a>
+ **Description:** Describes the Region that your Amazon S3 bucket resides in.
+ **Sample values:** `Asia Pacific (Mumbai)`, `Asia Pacific (Seoul)`, `Canada (Central)`, `EU (London)`, `US West (Oregon)`
+ **Services:**
  + Amazon EC2
  + AWS Certificate Manager
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/locationType
<a name="product-details-L-location"></a>
+ **Description:** Describes the endpoint of your task. 
+ **Sample values:** `AWS Region`, `AWS Edge Location`, `Other` 
+ **Services:**
  + Amazon EC2
  + AWS Certificate Manager
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/logsDestination
<a name="product-details-L-logsDestination"></a>
+ **Description:** The `AWS::Logs::Destination` resource specifies a CloudWatch logs destination. A destination includes a physical resource (for example, Amazon Kinesis data stream) and you can subscribe the resource to a stream of log events.
+ **Sample values:** `AWS Region`, `AWS Edge Location`, `Other` 
+ **Services:**
  + Amazon EC2
  + AWS Certificate Manager
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

## M
<a name="product-details-M"></a>

### product/maxIopsBurstPerformance
<a name="product-details-M-maxiops"></a>
+ **Description:** Describes the max IOPS burst performance of your Amazon EBS volume. 
+ **Sample value:** `3000 IOPS for volumes <= 1TB`
+ **Services:**
  + Amazon EC2

### product/maxIopsvolume
<a name="product-details-M-maxiopsvolume"></a>
+ **Description:** Describes maximum input/output per second of your Amazon EBS volume. 
+ **Sample value:** `16,000 (maxiops for a General Purpose SSD (gp2))`
+ **Services:**
  + Amazon EC2

### product/maxThroughputvolume
<a name="product-details-M-maxthroughput"></a>
+ **Description:** Describes the max network throughput volume of your Amazon EBS volume. 
+ **Sample values:** `500 MiB/s`, `250 MiB/s`, `1000 MiB/s`, `40 - 90 MB/sec`
+ **Services:**
  + Amazon EC2
  + Amazon SageMaker AI

### product/memory
<a name="product-details-M-memory"></a>
+ **Description:** The placeholder electronics for instructions and data a computer needs to respond quickly. Computer bytes indicate the storage units.
+ **Services:**
  + AWS Database Migration Service
  + DynamoDB Accelerator
  + Amazon DocumentDB
  + Amazon EC2

### product/messageCountfee
<a name="product-details-M-messagecountfee"></a>
+ **Description:** Describes the type of metering usage, denoting whether the usage represents the number of messages or fees charged.
+ **Sample values:** `CarrierFeeCount`, `MessageFees`, `MessageCount`, `CarrierFees`
+ **Services:**
  + Amazon Simple Notification Service

### product/messageType
<a name="product-details-M-messagetype"></a>
+ **Description:** Describes the type of SMS message. Note that SNS supports only Outbound SMS.
+ **Sample values:** `OutboundSMS`
+ **Services:**
  + Amazon Simple Notification Service

## N
<a name="product-details-N"></a>

### product/networkPerformance
<a name="product-details-N-network"></a>
+ **Description:** Describes the network throughput of your Amazon EC2 instances. 
+ **Sample values:** `moderate`, `high`, `up to 10 GB`
+ **Services:**
  + Amazon EC2
  + Amazon RDS
  + Amazon ElastiCache
  + Amazon SageMaker AI
  + AWS Database Migration Service

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/normalizationSizeFactor
<a name="product-details-N-normalization"></a>
+ **Description:** Describes the normalization factor of the instance size. 
+ **Sample values:** `nano - 0.25`, `micro - 0.5`, `medium - 2`, `xlarge - 8`, `16xlarge - 128`
+ **Services:**
  + Amazon DocumentDB
  + Amazon EC2
  + Amazon MQ
  + Amazon Neptune
  + Amazon RDS

## O
<a name="product-details-O"></a>

### product/operatingSystem
<a name="product-details-O-os"></a>
+ **Description:** Describes the operating system of your Amazon EC2 instance. 
+ **Sample values:** `Amazon Linux`, `Ubuntu`, `Windows Server`, `Oracle Linux`, `FreeBSD`
+ **Services:**
  + Amazon AppStream
  + Amazon EC2
  + Amazon GameLift Servers
  + Amazon Lightsail
  + Amazon WorkSpaces
  + AWS CodeBuild

### product/operation
<a name="product-details-O-ops"></a>
+ **Description:** Describes the specific AWS operation that this line item covers. 
+ **Sample values:** `RunInstances` (indicates the operation of an Amazon EC2 instance)
+ **Services:**
  + Amazon EC2
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB
  + Amazon CloudWatch
  + Amazon Redshift

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/originationIdType
<a name="product-details-O-originationidtype"></a>
+ **Description:** Describes the type of origination ID used when sending SMS messages.
+ **Sample values:** `Sharedroute`
+ **Services:**
  + Amazon Simple Notification Service

### product/osType
<a name="product-details-O-ostype"></a>
+ **Description:** Describes the operating system of the resource.
+ **Sample values:** `Dev Environment`, `Linux`, `Linux ARM64`, `Windows`
+ **Services:**
  + Amazon CodeCatalyst

## P
<a name="product-details-P"></a>

### product/parameterType
<a name="product-details-P-parameterType"></a>
+ **Description:** Use parameters in CloudFormation to enter custom values to your template when you create or update a stack. For Example, `InstanceTypeParameter`. You can use this parameter to specify the Amazon EC2 instance type when you create or update the stack.

### product/physicalCores
<a name="product-details-P-physical"></a>
+ **Description:** Describes the number of physical cores an instance provides. 
+ **Sample values:** `4`, `8`
+ **Services:**
  + Amazon EC2

### product/physicalProcessor
<a name="product-details-P-processor"></a>
+ **Description:** Describes the processor on your Amazon EC2 instance. 
+ **Sample values: **`High Frequency Intel Xeon E7-8880 v3 (Haswell)`, `Intel Xeon E5-2670`, `AMD EPYC 7571`
+ **Services:**
  + Amazon DocumentDB
  + Amazon EC2
  + Amazon Neptune
  + Amazon RDS
  + AWS Database Migration Service

### product/platoClassificationType
<a name="product-details-P-platoclassificationtype"></a>
+ **Description:** Tiered per object pricing for data annotation workflow routing.
+ **Sample values: **`LabeledObject`, `3DLabeledObjectMultiFrame`, `3DLabeledObject`, `Processing:VolumeUsage`
+ **Services:**
  + Amazon SageMaker AI

### product/pricingUnit
<a name="product-details-P-pricingUnit"></a>
+ **Description:** The smallest billing unit for an AWS service. For example, 0.01c per API call.
+ **Services:**
  + Directory Service

### product/primaryplaceofuse
<a name="product-details-P-primaryplaceofuse"></a>
+ **Description:** The primary business or residential street address location where a customer's use of the service primarily occurs.

### product/processorArchitecture
<a name="product-details-P-processorarch"></a>
+ **Description:** Describes your processor architecture. 
+ **Sample values:** `32-bit`, `64-bit`
+ **Services:**
  + Amazon DocumentDB
  + Amazon EC2
  + Amazon Neptune
  + Amazon RDS
  + AWS Database Migration Service

### product/processorFeatures
<a name="product-details-P-processorfeature"></a>
+ **Description:** Describes the processor features of your instances. 
+ **Sample values:** `Intel AVX`, `Intel AVX2`, `Intel AVX512`, `Intel Turbo`
+ **Services:**
  + AWS Database Migration Service
  + Amazon DocumentDB
  + Amazon EC2
  + Amazon Neptune
  + Amazon RDS

### product/ProductFamily
<a name="product-details-P-productfamily"></a>
+ **Description:** The category for the type of product. 
+ **Sample values:** `Alarm`, `AWS Budgets`, `Stopped Instance`, `Storage Snapshot`, `Compute`
+ **Services:**
  + Amazon EC2
  + AWS Certificate Manager
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/ProductName
<a name="product-details-P-productname"></a>
+ **Description:** The full name of the AWS service. Use this column to filter AWS usage by AWS service. 
+ **Sample values:** `AWS Backup`, `AWS Config`, `Amazon Registrar`, `Amazon Elastic File System`, `Amazon Elastic Compute Cloud`

### product/productSchemaDescription
<a name="product-details-P-productSchemaDescription"></a>
+ **Description:** A blueprint of how your product is constructed. This contains the various attributes that make up your product.

### product/provisioned
<a name="product-details-P-provisioned"></a>
+ **Description:** Indicates whether Amazon EBS usage was related to provisioned Amazon EBS storage. 
+ **Sample values:** `Yes`, `No`
+ **Services:**
  + Amazon EC2
  + Amazon MQ

### product/provisioningType
<a name="product-details-P-provisioningtype"></a>
+ **Description:** Describes whether the resources were deployed on-demand or pre-provisioned.
+ **Sample values:** `On-Demand`, `Pre-Provisioned`
+ **Services:**
  + Amazon CodeCatalyst

### product/PurchaseOption
<a name="product-details-P-PurchaseOption"></a>
+ **Description:** Describes the available purchasing models for an AWS service. For example, AWS provides four main Amazon EC2 instance purchasing options: `On-Demand`, `Reserved Instances`, `Spot Instances`, with the added option of `Dedicated Hosts`.

### product/purchaseterm
<a name="product-details-P-purchaseterm"></a>
+ **Description:** In Amazon EC2, this specifies a commitment to a consistent instance configuration. This includes instance type and Region for a period of 1 to 3 years.

## R
<a name="product-details-R"></a>

### product/region
<a name="product-details-R-region"></a>
+ **Description:** The geographical area that hosts your AWS services. Use this field to analyze spend across a particular Region. 
+ **Sample values:** `eu-west-3`, `us-west-1`, `us-east-1`, `ap-northeast-2`, `sa-east-1`
+ **Services:**
  + Amazon EC2
  + AWS Certificate Manager
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/regioncode
<a name="product-details-R-regioncode"></a>
+ **Description:** A Region is a physical location around the world where data centers are clustered. AWS calls each group of logical data centers an Availability Zone (AZ). Each AWS Region consists of multiple, isolates, and physically separate AZs within a geographical area. The Region code attribute has the same name as an AWS Region, and specifies where the AWS service is available.
+ **Sample values:** `us-west-2`, `us-east-1`, `ap-southeast-2`
+ **Services:**
  + Amazon SageMaker AI

### product/replicationType
<a name="product-details-R-replicationType"></a>
+ **Description:** Specifies that the service is free to use. For example, AWS Server Migration Service is free to use, and you only pay for the storage resources used during the migration process.
+ **Sample values:** `Free`
+ **Services:**
  + AWS Application Migration Service

### product/resourceAssessment
<a name="product-details-R-resourceAssessment"></a>
+ **Description:** A process that collects, stores, and manages evidence. You can use this to assess risk and compliance with industry standards and regulations.
+ **Sample values:** `All assessment`
+ **Services:**
  + AWS Audit Manager

### product/resourcePriceGroup
<a name="product-details-R-resourcepricegroup"></a>
+ **Description:** Describes the resource type, the resource, and the price group (the price we charge for monitoring; there are currently two price classes: A and B). Therefore, as an example, if we were monitoring an RDS resource, the resource type would be RDS (the "product"), the resource would be instance, and the price group would be B.
+ **Sample values:** `RDS-DBInstance-GroupB`
+ **Services:**
  + Amazon DevOps Guru

### product/routeType
<a name="product-details-R-routetype"></a>
+ **Description:** Describes the type of SMS route used. Only Standard applies for now.
+ **Sample values:** `Standard`
+ **Services:**
  + Amazon Simple Notification Service

## S
<a name="product-details-S"></a>

### product/servicecode
<a name="product-details-S-servicecode"></a>
+ **Description:** This identifies the specific AWS service to the customer as a unique short abbreviation.
+ **Sample values:** `Amazon EC2`, `AWS KMS`
+ **Services:**
  + AWS Budgets
  + AWS Backup
  + AWS Certificate Manager
  + AWS Cloud Map
  + AWS CloudTrail

### product/servicename
<a name="product-details-S-servicename"></a>
+ **Description:** A simplified description about the AWS service.
+ **Services:**
  + Amazon EC2 Budgets
  + Amazon ECR
  + Amazon ECS
  + Amazon EFS
  + Amazon Elastic Inference
  + Amazon EKS

### product/singleOrDualPass
<a name="product-details-S-singleOrDualPass"></a>
+ **Description:** Terms used to decide the type of encoding that happens for videos. In one-pass encoding, the encoding is done in the first pass itself. For 2-pass encoding, the file is analyzed thoroughly in the first pass, and a intermediate file is created. In the second pass the encoder finds the intermediate file and allocates bits. The actual encoding takes place in the second pass.
+ **Services:**
  + AWS Elemental MediaConvert

### product/sizeFlex
<a name="product-details-S-sizeflex"></a>
+ **Description:** Describes whether a normalized benefit of the RI can be applied to other instance sizes within the Region and instance family.
+ **Sample values:** `true`, `false`
+ **Services:**
  + Amazon Elastic Compute Cloud

### product/sku
<a name="product-details-S-sku"></a>
+ **Description:** A unique code for a product. The SKU is created by combining the `ProductCode`, `UsageType`, and `Operation`. For size-flexible RIs, the SKU uses the instance that was used. For example, if you used a `t2.micro` instance and AWS applied a `t2.small` RI discount to the usage, the line item SKU is created with the `t2.micro`.
+ **Sample values:** `FFNT87MQSCR328W6`, `VBYCEU494XUAHCA7`
+ **Services:**
  + Amazon EC2
  + AWS Certificate Manager
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/storage
<a name="product-details-S-storage"></a>
+ **Description:** Describes the disk storage attached to your instance. 
+ **Sample values:** `60GB`, `True`, `EBS Only`, `1 x 900 NVMe SSD`, `1 x 150 NVMe SSD`
+ **Services:**
  + Amazon EC2
  + Amazon RDS
  + Amazon Redshift
  + OpenSearch Service
  + Amazon WorkSpaces

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/storageclass
<a name="product-details-S-storageclass"></a>
+ **Description:** Describes the storage class of your Amazon S3 bucket. 
+ **Sample values:** `Archive`, `General Purpose`, `Infrequent Access`, `Intelligent-Tiering`, `Non-Critical Data`
+ **Services:**
  + AWS Elemental MediaStore
  + AWS Storage Gateway
  + Amazon Cloud Directory
  + Amazon EFS
  + Amazon MQ
  + Amazon S3

### product/storagemedia
<a name="product-details-S-storagemedia"></a>
+ **Description:** A storage medium is any technology, including device and material used to place, keep, and retrieve electronic data.
+ **Services:**
  + AWS Database Migration Service
  + Amazon CloudWatch
  + Amazon DocumentDB
  + Amazon EC2
  + Amazon ES

### product/storagetype
<a name="product-details-S-storagetype"></a>
+ **Description:** Describes how and where the information is stored by a computer. This might be internal or external to a computer, server, or computing device.
+ **Sample values:** `Amazon S3`, `SSD`, `SSD-backed`
+ **Services:**
  + AWS Backup
  + Amazon ECR

## T
<a name="product-details-T"></a>

### product/tenancy
<a name="product-details-T-tenancy"></a>
+ **Description:** The type of tenancy allowed on the Amazon EC2 instance. 
+ **Sample values:** `Dedicated`, `Reserved`, `Shared`, `NA`, `Host`
+ **Services:**
  + Amazon EC2
  + Amazon ECS

### product/throughputCapacity
<a name="product-details-T-throughputcapacity"></a>
+ **Description:** Describes the Speed at which the file server hosting the file system can serve file data. For Amazon FileCache, the value will be 1000 only.
+ **Sample values:** `12`, `40`, `50`, `100`, `125`, `250`, `500`, `1000`
+ **Services:**
  + Amazon FileCache
  + Amazon FSx

### product/tier
<a name="product-details-T-tier"></a>
+ **Description:** With AWS, you can get volume based discounts and savings as your usage increases. For services like Amazon S3, pricing is tiered. This means the more you use, the less you pay per GB. AWS provides options to acquire services that assist your business needs.
+ **Services:**
  + AWS Elemental MediaConvert

### product/toLocation
<a name="product-details-T-toloc"></a>
+ **Description:** Describes the location usage destination.
+ **Sample values:** `External`, `US East (N. Virginia)`
+ **Services:**
  + Amazon CloudFront
  + AWS Data Transfer

### product/toLocationType
<a name="product-details-T-toloctype"></a>
+ **Description:** Describes the destination location of the service usage.
+ **Sample values:** `AWS Region`, `AWS Edge Location`
+ **Services:**
  + Direct Connect
  + AWS Elemental MediaConnect
  + AWS Shield
  + Amazon CloudFront
  + Amazon Lightsail

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip).

### product/toRegionCode
<a name="product-details-T-toRegionCode"></a>
+ **Description:** Describes the source Region code for the AWS service. For more information, see [product/regioncode](#product-details-R-regioncode).
+ **Sample values:** `eu-west-1`
+ **Services:**
  + Amazon RDS
  + Amazon EC2
  + Amazon VPC
  + Direct Connect

### product/transcodingResult
<a name="product-details-T-transcodingResult"></a>
+ **Description:** The output of decoding an encoded video source to an intermediate uncompressed format, and re-encoding it into the target format.
+ **Services:**
  + AWS Elemental MediaConvert

### product/trialProduct
<a name="product-details-T-trialProduct"></a>
+ **Description:** Describes if AWS CloudHSM allows free hours.
+ **Services:**
  + AWS CloudHSM

## U
<a name="product-details-U"></a>

### product/upfrontCommitment
<a name="product-details-U-upfrontCommitment"></a>
+ **Description:** Describes if any usage commitment is required for AWS CloudHSM. You will be charged an hourly fee for each hour (or partial hour) that an HSM is provisioned to a AWS CloudHSM cluster. A cluster with no HSMs is not billed, and you aren't billed for automatic storage of encrypted backups. For more information, see [AWS CloudHSM Pricing](https://aws.amazon.com/cloudhsm/pricing/).

  Network data transfers to and from your HSMs are charged separately. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/).
+ **Services:**
  + AWS CloudHSM

### product/usagetype
<a name="product-details-U-usage"></a>
+ **Description:** Describes the usage details of the line item. 
+ **Sample values:** `EU-BoxUsage:c5d.9xlarge`, `EU-BoxUsage:m4.16xlarge`, `SAE1-InstanceUsage:db.t2.medium`, `USW2-AW-SW-19`, `SAE1-BoxUsage:c4.large`, 
+ **Services:**
  + Amazon EC2
  + AWS Certificate Manager
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

## V
<a name="product-details-V"></a>

### product/vcpu
<a name="product-details-V-vcpu"></a>
+ **Description:** Describes the number of threads concurrently running on a single CPU core. Amazon EC2 instances support multithreading, which enables multiple threads to run concurrently on a single CPU core. Each thread is represented as a virtual CPU (vCPU) on the instance.
+ **Sample values:** `8`, `16`, `36`, `72`, `128`
+ **Services:**
  + Amazon EC2
  + Amazon RDS
  + Amazon Redshift
  + OpenSearch Service
  + Amazon ElastiCache

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

### product/videoCodec
<a name="product-details-V-videoCodec"></a>
+ **Description:** A software or hardware that compresses and decompresses digital video. In the context of video compression, codec is a blending of encoder and decoder. A device that only compresses is typically called an encoder, and one that only decompresses is a decoder.
+ **Services:**
  + AWS Elemental MediaConvert;

### product/videoFrameRate
<a name="product-details-V-videoFrameRate"></a>
+ **Description:** A video frame rate (shown as frames per second (FPS)) is the frequency rate which consecutive images (frames) are captured or displayed by video cameras, computer graphics, and motion capture systems.
+ **Services:**
  + AWS Elemental MediaConvert;

### product/videoQualitySetting
<a name="product-details-V-videoqualitysetting"></a>
+ **Description:** Describes the quality setting used for the encode, which impacts the compression efficiency and, therefore, the video quality at a given bitrate.
+ **Sample values:** `Multi-pass`, `Multi-pass HQ`, `NA`, `Single-pass`, `Single-pass HQ`, 
+ **Services:**
  + AWS Elemental MediaConvert

### product/volumeType
<a name="product-details-V-volumetype"></a>
+ **Description:** Describes your Amazon EBS volume types. 
+ **Sample values:** `Standard`, `General Purpose`, `General Purpose-Aurora`, `Amazon Glacier`, `Amazon SimpleDB – Standard`, 
+ **Services:**
  + Amazon EC2
  + Amazon S3
  + Amazon RDS
  + Amazon DynamoDB
  + Amazon Glacier

    and more. For the full service list, download [Column\_Attribute\_Service.zip](samples/Column_Attribute_Service.zip). 

## W
<a name="product-details-W"></a>

### product/workforceType
<a name="product-details-W-workforceType"></a>
+ **Description:** The segmentation of the employed or unemployed labour pool. For example, `Full Time Employees` (FTE), or `Temporary`.
+ **Services:**
  + Amazon SageMaker AI