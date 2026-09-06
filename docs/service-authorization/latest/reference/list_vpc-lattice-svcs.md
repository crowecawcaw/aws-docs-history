

# Actions, resources, and condition keys for Amazon VPC Lattice Services
<a name="list_vpc-lattice-svcs"></a>

Amazon VPC Lattice Services (service prefix: `vpc-lattice-svcs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/vpc-lattice-svcs/vpc-lattice-svcs.json) for this service.

**Topics**
+ [Actions defined by Amazon VPC Lattice Services](#list_vpc-lattice-svcs-actions-as-permissions)
+ [Resource types defined by Amazon VPC Lattice Services](#list_vpc-lattice-svcs-resources-for-iam-policies)
+ [Condition keys for Amazon VPC Lattice Services](#list_vpc-lattice-svcs-policy-keys)

## Actions defined by Amazon VPC Lattice Services
<a name="list_vpc-lattice-svcs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [Connect](https://docs.aws.amazon.com/vpc-lattice/latest/ug/sigv4-authenticated-requests.html)  **
  - **Description:** Grants permission to connect to a VPC Lattice service
  - **Resource types (\*required):** [TCP Service\*](#list_vpc-lattice-svcs-resource-TCPService)
  - **Condition keys:** [vpc-lattice-svcs:Port](#list_vpc-lattice-svcs-vpc-lattice-svcs_Port)<br />[vpc-lattice-svcs:ServiceArn](#list_vpc-lattice-svcs-vpc-lattice-svcs_ServiceArn)<br />[vpc-lattice-svcs:ServiceNetworkArn](#list_vpc-lattice-svcs-vpc-lattice-svcs_ServiceNetworkArn)<br />[vpc-lattice-svcs:SourceVpc](#list_vpc-lattice-svcs-vpc-lattice-svcs_SourceVpc)<br />[vpc-lattice-svcs:SourceVpcOwnerAccount](#list_vpc-lattice-svcs-vpc-lattice-svcs_SourceVpcOwnerAccount)
  - **Access level:** Write

- **   [Invoke](https://docs.aws.amazon.com/vpc-lattice/latest/ug/sigv4-authenticated-requests.html)  **
  - **Description:** Grants permission to invoke a VPC Lattice service
  - **Resource types (\*required):** [Service\*](#list_vpc-lattice-svcs-resource-Service)
  - **Condition keys:** [vpc-lattice-svcs:Port](#list_vpc-lattice-svcs-vpc-lattice-svcs_Port)<br />[vpc-lattice-svcs:RequestHeader/${HeaderName}](#list_vpc-lattice-svcs-vpc-lattice-svcs_RequestHeader___HeaderName_)<br />[vpc-lattice-svcs:RequestMethod](#list_vpc-lattice-svcs-vpc-lattice-svcs_RequestMethod)<br />[vpc-lattice-svcs:RequestPath](#list_vpc-lattice-svcs-vpc-lattice-svcs_RequestPath)<br />[vpc-lattice-svcs:RequestQueryString/${QueryStringKey}](#list_vpc-lattice-svcs-vpc-lattice-svcs_RequestQueryString___QueryStringKey_)<br />[vpc-lattice-svcs:ServiceArn](#list_vpc-lattice-svcs-vpc-lattice-svcs_ServiceArn)<br />[vpc-lattice-svcs:ServiceNetworkArn](#list_vpc-lattice-svcs-vpc-lattice-svcs_ServiceNetworkArn)<br />[vpc-lattice-svcs:SourceVpc](#list_vpc-lattice-svcs-vpc-lattice-svcs_SourceVpc)<br />[vpc-lattice-svcs:SourceVpcOwnerAccount](#list_vpc-lattice-svcs-vpc-lattice-svcs_SourceVpcOwnerAccount)
  - **Access level:** Write



## Resource types defined by Amazon VPC Lattice Services
<a name="list_vpc-lattice-svcs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:service/${ServiceId}/${RequestPath} |   | 
|  [TCP Service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)  | arn:${Partition}:vpc-lattice:${Region}:${Account}:service/${ServiceId} |   | 

## Condition keys for Amazon VPC Lattice Services
<a name="list_vpc-lattice-svcs-policy-keys"></a>

Amazon VPC Lattice Services defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [vpc-lattice-svcs:Port](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the destination port the request is made to | Numeric | 
|   [vpc-lattice-svcs:RequestHeader/${HeaderName}](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by a header name-value pair in the request headers | String | 
|   [vpc-lattice-svcs:RequestMethod](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the method of the request | String | 
|   [vpc-lattice-svcs:RequestPath](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the path portion of the request URL | String | 
|   [vpc-lattice-svcs:RequestQueryString/${QueryStringKey}](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the query string key-value pairs in the request URL | ArrayOfString | 
|   [vpc-lattice-svcs:ServiceArn](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the ARN of the service receiving the request | ARN | 
|   [vpc-lattice-svcs:ServiceNetworkArn](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the ARN of the service network receiving the request | ARN | 
|   [vpc-lattice-svcs:SourceVpc](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the VPC the request is made from | String | 
|   [vpc-lattice-svcs:SourceVpcOwnerAccount](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html#auth-policies-condition-keys)  | Filters access by the owning account of the VPC the request is made from | String | 