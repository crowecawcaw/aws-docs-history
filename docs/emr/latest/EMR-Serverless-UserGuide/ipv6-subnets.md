

# Configure IPv6 subnets for EMR Serverless applications
<a name="ipv6-subnets"></a>

With Amazon EMR Serverless, you can run your Apache Spark and Apache Hive jobs over IPv6 in your Amazon Virtual Private Cloud (Amazon VPC). If you supply dual-stack (IPv4 and IPv6) or IPv6-only subnets, EMR Serverless runs your jobs using the addressing mode of those subnets. Your jobs can then reach IPv6 endpoints in your VPC and external IPv6 endpoints. IPv6-only subnets run over IPv6 automatically. For dual-stack subnets, you enable IPv6 with a configuration property, as described in [Configuring IPv6 properties](#ipv6-properties).

## Understanding key benefits
<a name="ipv6-key-benefits"></a>

Running EMR Serverless applications over IPv6 provides the following benefits.
+ **Larger address space** – IPv6 provides a much larger address space than IPv4, which helps you avoid IPv4 address exhaustion in VPCs and subnets that run many workers.
+ **Dual-stack and IPv6-only networking** – Run jobs on dual-stack subnets that use both IPv4 and IPv6, or on IPv6-only subnets, to meet networking standards and compliance requirements that call for IPv6.
+ **Connectivity to IPv6 endpoints** – Your Spark and Hive jobs can reach IPv6 endpoints and services in your VPC and external IPv6 endpoints.
+ **Flexible enablement** – IPv6-only subnets run over IPv6 automatically. For dual-stack subnets, you enable IPv6 with a single configuration property, so you control when IPv6 applies.

## How EMR Serverless determines the addressing mode
<a name="ipv6-addressing-mode"></a>

EMR Serverless determines your application's addressing mode from the subnets that you supply.
+ **IPv4-only subnets** – The application runs IPv4-only, exactly as before. There is no behavior change for existing applications.
+ **Dual-stack subnets** – The application runs IPv4-only unless you enable IPv6 with the configuration property described in [Configuring IPv6 properties](#ipv6-properties). When you enable IPv6, the application can use both IPv4 and IPv6.
+ **IPv6-only subnets** – The application runs IPv6-only. This is available on all release versions.

When you supply more than one subnet, EMR Serverless runs the whole application in the one addressing mode that every subnet in the set supports. If the subnets share no common mode, EMR Serverless rejects the request. The following cases describe the kinds of subnets a set can contain, in any number and in any combination.
+ **IPv4-only and IPv6-only** – EMR Serverless rejects the set with a validation error.
+ **IPv6-only and dual-stack** – The set runs IPv6-only, including any dual-stack subnets in the set. Make sure every subnet in the set, including any dual-stack subnets, meets the prerequisites in [Meeting VPC and subnet prerequisites](#ipv6-prerequisites).
+ **IPv4-only and dual-stack** – The set runs IPv4-only, including any dual-stack subnets in the set.

EMR Serverless evaluates the addressing mode from the current subnets and configuration each time the application starts. A running application keeps the mode it started with, so a change does not take effect until the next start.

For the definitions of IPv4-only, dual-stack, and IPv6-only subnets, see [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon Virtual Private Cloud User Guide*.

## Meeting VPC and subnet prerequisites
<a name="ipv6-prerequisites"></a>

You are responsible for configuring your VPC and subnets so that IPv6 traffic can reach your data stores and the AWS services that your jobs use. Configure the following in your own VPC before you run IPv6 jobs.

Use the *Amazon Virtual Private Cloud User Guide* for the step-by-step instructions.
+ **Associate an IPv6 Classless Inter-Domain Routing (CIDR) block with the subnet.** Each dual-stack or IPv6-only subnet must have an IPv6 CIDR block. See [Add or remove an IPv6 CIDR block from your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-associate-ipv6-cidr.html) and [IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html) in the *Amazon Virtual Private Cloud User Guide*.
+ **Turn on auto-assign IPv6 address for the subnet.** The subnet must automatically assign IPv6 addresses so that your application receives IPv6 connectivity. See [Modify the IP addressing attributes of your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-public-ip.html) in the *Amazon Virtual Private Cloud User Guide*.
+ **Enable DNS64 (DNS-based IPv6-to-IPv4 translation) on the subnet and provide an outbound NAT64 (network address translation from IPv6 to IPv4) path (IPv6-only).** An IPv6-only application needs this to reach IPv4-only endpoints (for example, services that do not yet publish an IPv6 address). Enable DNS64 on the subnet and route the synthesized `64:ff9b::/96` traffic through a NAT gateway, which performs NAT64. A dual-stack application can reach IPv4-only endpoints over IPv4 and does not require this. See [DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html) and [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon Virtual Private Cloud User Guide*.
+ **Provide an egress-only internet gateway for private outbound IPv6 traffic.** To allow a private subnet to initiate outbound IPv6 connections without accepting inbound connections from the internet, add an egress-only internet gateway and a `::/0` route to it. See [Enable outbound IPv6 traffic using an egress-only internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html) in the *Amazon Virtual Private Cloud User Guide*.
+ **Allow the outbound IPv6 traffic your jobs need in your security groups.** The existing EMR Serverless security group rules apply. For general VPC and security group setup, see [Configuring VPC access for EMR Serverless applications to connect to data](vpc-access.md).

## Configuring IPv6 for your application
<a name="ipv6-configure"></a>

You configure IPv6 when you create an application, or change it later by updating an existing application. In both cases, EMR Serverless derives the addressing mode from the subnets in `--network-configuration`, as described in [How EMR Serverless determines the addressing mode](#ipv6-addressing-mode). For dual-stack subnets, you also enable IPv6 with the property described in [Configuring IPv6 properties](#ipv6-properties); for IPv6-only subnets, no property is required.

### To create an application
<a name="ipv6-create-app"></a>

The following procedure creates a Spark application that uses dual-stack subnets and enables IPv6. Before you begin, make sure that each subnet you plan to use meets the requirements in [Meeting VPC and subnet prerequisites](#ipv6-prerequisites).

The following AWS CLI command creates a Spark application with dual-stack subnets and enables IPv6:

```
aws emr-serverless create-application \
--type SPARK \
--name {{my-application-name}} \
--release-label emr-7.14.0 \
--network-configuration '{
    "subnetIds": ["{{subnet-id-1}}", "{{subnet-id-2}}"],
    "securityGroupIds": ["{{security-group-id}}"]
}' \
--runtime-configuration '[
    {
        "classification": "spark-defaults",
        "properties": {
            "spark.emr-serverless.networking.ipv6.enabled": "true"
        }
    }
]' \
--region {{AWS_REGION}}
```

Replace the following values:
+ **`my-application-name`** – The name that you want to give your application.
+ **`subnet-id-1`, `subnet-id-2`** – The IDs of the dual-stack subnets that you want to use.
+ **`security-group-id`** – The ID of the security group that you want to attach.
+ **`AWS_REGION`** – The AWS Region where you want to create the application.

On dual-stack subnets, the job uses IPv4 by default. To have Spark prefer IPv6, set the engine-preference properties described in [Configuring IPv6 properties](#ipv6-properties). For a Hive application, use `--type HIVE`, the `hive-site` classification, and the `hive.emr-serverless.networking.ipv6.enabled` property.

**Note**  
For IPv6-only subnets, omit `--runtime-configuration`. The application runs over IPv6 automatically, and you do not set the enablement or engine-preference properties.

### To update an existing application
<a name="ipv6-update-app"></a>

1. Stop the application if it is running.

1. Update the application while it is in the `CREATED` or `STOPPED` state. Supply the subnets you want in `--network-configuration`, and for dual-stack subnets include the enablement property in `--runtime-configuration`. Parameters that you do not include keep their current values.

   The following AWS CLI command updates the application with the new subnets and the enablement property:

   ```
   aws emr-serverless update-application \
   --application-id {{application-id}} \
   --network-configuration '{
       "subnetIds": ["{{subnet-id-1}}", "{{subnet-id-2}}"],
       "securityGroupIds": ["{{security-group-id}}"]
   }' \
   --runtime-configuration '[
       {
           "classification": "spark-defaults",
           "properties": {
               "spark.emr-serverless.networking.ipv6.enabled": "true"
           }
       }
   ]' \
   --region {{AWS_REGION}}
   ```

   Replace the following values:
   + **`application-id`** – The ID of the application that you want to update.
   + **`subnet-id-1`, `subnet-id-2`** – The IDs of the subnets that you want to use.
   + **`security-group-id`** – The ID of the security group that you want to attach.
   + **`AWS_REGION`** – The AWS Region of the application.

1. Start the application. EMR Serverless applies the addressing mode at start.

## Configuring IPv6 properties
<a name="ipv6-properties"></a>

The following properties control IPv6 for your application and jobs. Set the enablement property at the application level in `runtimeConfiguration`. Set the engine-preference properties at the job level, in `sparkSubmitParameters` for Spark or with `--hiveconf` for Hive.



| Engine | Property | Where you set it | Default | Applies to | Notes | 
| --- | --- | --- | --- | --- | --- | 
| Spark | spark.emr-serverless.networking.ipv6.enabled | spark-defaults (application runtimeConfiguration) | false | Dual-stack | Enables IPv6 on dual-stack subnets. | 
| Spark | spark.emr-serverless.driverEnv.SPARK\_PREFER\_IPV6 | sparkSubmitParameters (job) | false | Dual-stack (optional) | Makes the Spark driver prefer IPv6. Set automatically on IPv6-only subnets. Do not set on IPv4-only subnets. | 
| Spark | spark.executorEnv.SPARK\_PREFER\_IPV6 | sparkSubmitParameters (job) | false | Dual-stack (optional) | Makes Spark executors prefer IPv6. Set automatically on IPv6-only subnets. Do not set on IPv4-only subnets. | 
| Hive | hive.emr-serverless.networking.ipv6.enabled | hive-site (application runtimeConfiguration) | false | Dual-stack | Same as the Spark enablement property, for Hive applications. | 
| Hive | JAVA\_TOOL\_OPTIONS=-Djava.net.preferIPv6Addresses=true | --hiveconf (job) | Not set | Dual-stack (optional) | Makes Hive prefer IPv6. Set automatically on IPv6-only subnets. Do not set on IPv4-only subnets. | 

On dual-stack subnets, both IPv4 and IPv6 are available and the engine uses IPv4 by default. To have the engine prefer IPv6, set the engine-preference properties for your engine. On IPv6-only subnets, EMR Serverless sets the IPv6 preference for you, so you do not set these properties. On IPv4-only subnets, do not set the engine-preference properties; there is no IPv6 available, so preferring IPv6 causes the job to fail.

The following example sets the Spark engine to prefer IPv6 in a job's `sparkSubmitParameters`.

```
--conf spark.emr-serverless.driverEnv.SPARK_PREFER_IPV6=true
--conf spark.executorEnv.SPARK_PREFER_IPV6=true
```

**Important**  
Do not force the IPv4 stack in the JVM (for example, by setting `-Djava.net.preferIPv4Stack=true` in `spark.driver.extraJavaOptions` or `spark.executor.extraJavaOptions`) on any addressing mode.

For more information about declaring `runtimeConfiguration` at the application level, see [Default application configuration for EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/default-configs.html). For more information about passing engine configurations, see [Using Spark configurations when you run EMR Serverless jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark.html) and [Using Hive configurations when you run EMR Serverless jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-hive.html).

## Considerations and limitations
<a name="ipv6-considerations"></a>
+ The addressing mode cannot be set through the API. To change it, change your subnets (or the `spark.emr-serverless.networking.ipv6.enabled` opt-in property for dual-stack subnets) and restart the application.
+ IPv4-only and IPv6-only subnets cannot be mixed in one application.
+ Your job code and any SDKs, drivers, or endpoints it uses must support IPv6 when the application runs IPv6-only. With EMR Serverless, you get IPv6 connectivity; it does not modify your application code or third-party endpoints.

## Troubleshooting
<a name="ipv6-troubleshooting"></a>

This topic helps you diagnose and resolve common IPv6 networking issues with EMR Serverless applications, including DNS resolution failures, missing auto-assigned IPv6 addresses, unexpected IPv4 usage, and subnet validation errors. The following are symptoms you might see when running IPv6 jobs, and what to do about each.

### DNS resolution error (UnknownHostException)
<a name="ipv6-ts-dns"></a>

This can happen on an IPv6-only application when the subnet is missing DNS64 or a NAT64 outbound path, so jobs cannot reach the endpoints they need. Enable DNS64 and provide a NAT gateway for NAT64 on every subnet in the application, as described earlier in this topic under [Meeting VPC and subnet prerequisites](#ipv6-prerequisites).

### Dual-stack subnet does not auto-assign IPv6 addresses
<a name="ipv6-ts-no-autoassign"></a>

This can happen when a subnet has an associated IPv6 CIDR block but does not automatically assign IPv6 addresses, so the application does not receive the IPv6 connectivity it expects. Turn on auto-assign IPv6 address for the subnet, as described earlier in this topic, and then start a new job. The setting applies only to resources created after you change it.

### Job runs over IPv4 on a dual-stack application
<a name="ipv6-ts-ran-ipv4"></a>

On dual-stack subnets, this can happen for either of two reasons. First, you did not enable IPv6 with the configuration property, so the application runs IPv4-only. Second, you enabled IPv6 but did not set the engine to prefer it, so the engine used IPv4. Confirm both the enablement property and the engine-preference properties in [Configuring IPv6 properties](#ipv6-properties).

### Job fails with UnresolvedAddressException
<a name="ipv6-ts-unresolved"></a>

This can happen when the job forces the IPv4 stack in the JVM. Remove `-Djava.net.preferIPv4Stack=true` (and any equivalent setting) from your job configuration, and resubmit the job. See [Configuring IPv6 properties](#ipv6-properties).

### Request fails with an incompatible-subnets validation error
<a name="ipv6-ts-validation"></a>

This can happen when you supply subnets that cannot run together, such as IPv4-only subnets mixed with IPv6-only subnets, or the `spark.emr-serverless.networking.ipv6.enabled` opt-in property set to `true` while the application includes an IPv4-only subnet. Review your subnets against [How EMR Serverless determines the addressing mode](#ipv6-addressing-mode), adjust them or the opt-in property, and retry the request.