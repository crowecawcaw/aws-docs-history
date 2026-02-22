# Resource identifiers for APIs and controls

Each control in AWS Control Tower has unique Amazon Resource Names (ARNs) for use with the [AWS Control Tower](../APIReference/Welcome.md "../APIReference/Welcome.md") and [Control Catalog](../../../controlcatalog/latest/APIReference/Welcome.md "../../../controlcatalog/latest/APIReference/Welcome.md") APIs. You can call an API using a global ARN or a regional ARN.

- We recommend that you use the global ARNs for all use cases.
- The regional ARNs have been available longer but are considered as legacy ARNs.

## Understand control ARNs

AWS Control Tower supports two types of control ARNs.

**Global ARNs (recommended)**

A global ARN is available for all controls that are part of [Control Catalog](../../../controlcatalog/latest/userguide/what-is-controlcatalog.md "../../../controlcatalog/latest/userguide/what-is-controlcatalog.md"). Global ARNs use the following format.

```
arn:{PARTITION}:controlcatalog:::control/{GLOBAL_CONTROL_ID}
```

For example, `arn:aws:controlcatalog:::control/k4izcjxhukijhajp6ks5mjxk`. Global ARNs are independent of any AWS Region. We recommend that you use global ARNs for all use cases.

**Regional ARNs (legacy)**

Older Control Catalog controls also have regional ARNs. A regional ARN is a unique identifier for each Region in which AWS Control Tower operates. Regional ARNs use the following format.

```
arn:{PARTITION}:controltower:{REGION}::control/{REGIONAL_CONTROL_ID}
```

For example, `arn:aws:controltower:us-east-1::control/YEHYWYAUIQHZ`. Regional ARNs for the same control can be different in different Regions.

**Benefits of using global ARNs**

Global ARNs provide several advantages over Regional ARNs.

- **Region independence** – The same ARN works across all AWS Regions within the same partition.
- **Simplified management** – You don't need to maintain Region-specific identifiers. This simplifies multi-Region management and deployments.
- **Future-proof** – New controls are assigned global ARNs only.

## Find global ARNs

You can retrieve global ARNs for Control Catalog controls in the following ways.

**AWS Control Tower console**

To view the global ARNs and other details about Control Catalog controls in the console, navigate to the **Control details** page in the AWS Control Tower console. You can find the identifier in the **API identifier** field.

**ListControls API**

You can use the [ListControls API](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md") to retrieve all controls with their global ARNs.

## Migrate from regional ARNs to global ARNs

Regional ARNs are no longer displayed in the console or the documentation, in favor of global ARNs. If you're using existing regional ARNs in your automation, you can continue to use them with the [AWS Control Tower](../APIReference/Welcome.md "../APIReference/Welcome.md") and [Control Catalog](../../../controlcatalog/latest/APIReference/Welcome.md "../../../controlcatalog/latest/APIReference/Welcome.md") APIs. However, we recommend that you migrate to global ARNs.

**Retrieve global ARNs by using regional control ARNs**

You can use regional ARNs with the [GetControl API](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md") to retrieve control metadata and global ARNs. For example:

```
aws controlcatalog get-control --control-arn arn:aws:controltower:us-east-1::control/YEHYWYAUIQHZ --region us-east-1
```

The response includes the corresponding global ARN, but not the Regional ARN.

## Find identifiers for OUs

For more information about how to find the resource identifier for an OU and its
resources, see [Resource types defined by AWS Organizations](../../../service-authorization/latest/reference/list_awsorganizations.md#awsorganizations-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsorganizations.md#awsorganizations-resources-for-iam-policies").

To learn more about how to get information from an OU, see [the
AWS Organizations API Reference](../../../organizations/latest/APIReference/API_DescribeOrganizationalUnit.md "../../../organizations/latest/APIReference/API_DescribeOrganizationalUnit.md").
