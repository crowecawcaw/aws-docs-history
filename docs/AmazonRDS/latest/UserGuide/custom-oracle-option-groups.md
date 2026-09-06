

# Working with option groups in RDS Custom for Oracle
<a name="custom-oracle-option-groups"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

RDS Custom uses option groups to enable and configure additional features. An *option group* specifies features, called options, that are available for an RDS Custom for Oracle DB instance. Options can have settings that specify how the option works. When you associate an RDS Custom for Oracle DB instance with an option group, the specified options and option settings are enabled for this instance. For general information about option groups in Amazon RDS, see [Working with option groups](USER_WorkingWithOptionGroups.md).

**Topics**
+ [Overview of option groups in RDS Custom for Oracle](#custom-oracle-option-groups.overview)
+ [Oracle time zone](custom-managing.timezone.md)

## Overview of option groups in RDS Custom for Oracle
<a name="custom-oracle-option-groups.overview"></a>

To enable options for your Oracle database, add them to an option group, and then associate the option group with your DB instance. For more information, see [Working with option groups](USER_WorkingWithOptionGroups.md).

**Topics**
+ [Summary of RDS Custom for Oracle options](#custom-oracle-option-groups.summary)
+ [Basic steps for adding an option to an RDS Custom for Oracle DB instance](#custom-oracle-timezone.overview.steps)
+ [Creating an option group for in RDS Custom for Oracle](#custom-oracle-timezone.creating)
+ [Associating an option group with an RDS Custom for Oracle DB instance](#custom-oracle-timezone.associating)

### Summary of RDS Custom for Oracle options
<a name="custom-oracle-option-groups.summary"></a>

RDS Custom for Oracle supports the following options for a DB instance.



| Option | Option ID | Description | 
| --- | --- | --- | 
| Oracle time zone | `Timezone` | The time zone used by your RDS Custom for Oracle DB instance.  | 

### Basic steps for adding an option to an RDS Custom for Oracle DB instance
<a name="custom-oracle-timezone.overview.steps"></a>

The general procedure for adding an option to your RDS Custom for Oracle DB instance is the following:

1. Create a new option group, or copy or modify an existing option group.

1. Add the option to the option group.

1. Associate the option group with your DB instance when you create or modify it.

### Creating an option group for in RDS Custom for Oracle
<a name="custom-oracle-timezone.creating"></a>

You can create a new option group that derives its settings from the default option group. You then add one or more options to the new option group. Or, if you already have an existing option group, you can copy that option group with all of its options to a new option group. To learn how to copy an option group, see [Copying an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy).

The default option groups for RDS Custom for Oracle are the following:
+ `default:custom-oracle-ee`
+ `default:custom-oracle-se2`
+ `default:custom-oracle-ee-cdb`
+ `default:custom-oracle-se2-cdb`

When you create an option group, the settings are derived from the default option group. After you have added the `TIME_ZONE` option, you can then associate the option group with your DB instance. 

#### Console
<a name="custom-oracle-timezone.Create.Console"></a>

 One way of creating an option group is by using the AWS Management Console. 

**To create a new option group by using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose **Create group**.

1. In the **Create option group** window, do the following:

   1. For **Name**, type a name for the option group that is unique within your AWS account. The name can contain only letters, digits, and hyphens. 

   1. For **Description**, type a brief description of the option group. The description is used for display purposes. 

   1. For **Engine**, choose any of the following RDS Custom for Oracle DB engines:
      + **custom-oracle-ee**
      + **custom-oracle-se2**
      + **custom-oracle-ee-cdb**
      + **custom-oracle-se2-cdb**

   1. For **Major engine version**, choose a major engine version supported by RDS Custom for Oracle. For more information, see [Supported Regions and DB engines for RDS Custom for Oracle](Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.ora).

1. To continue, choose **Create**. To cancel the operation instead, choose **Cancel**. 

#### AWS CLI
<a name="custom-oracle-timezone.Create.CLI"></a>

To create an option group, use the AWS CLI [`create-option-group`](https://docs.aws.amazon.com/cli/latest/reference/rds/create-option-group.html) command with the following required parameters.
+ `--option-group-name`
+ `--engine-name`
+ `--major-engine-version`
+ `--option-group-description`

**Example**  
The following example creates an option group named `testoptiongroup`, which is associated with the Oracle Enterprise Edition DB engine. The description is enclosed in quotation marks.  
For Linux, macOS, or Unix:  

```
aws rds create-option-group \
    --option-group-name {{testoptiongroup}} \
    --engine-name {{custom-oracle-ee-cdb}} \
    --major-engine-version {{19}} \
    --option-group-description "{{Test option group for a Custom Oracle CDB}}"
```
For Windows:  

```
aws rds create-option-group ^
    --option-group-name {{testoptiongroup}} ^
    --engine-name {{custom-oracle-ee-cdb}} ^
    --major-engine-version {{19}} ^
    --option-group-description "{{Test option group for a Custom Oracle CDB}}"
```

#### RDS API
<a name="custom-oracle-timezone.Create.API"></a>

To create an option group, call the Amazon RDS API [`CreateOptionGroup`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateOptionGroup.html) operation.

### Associating an option group with an RDS Custom for Oracle DB instance
<a name="custom-oracle-timezone.associating"></a>

You can associate your option group with a new or existing DB instance:
+ For a new DB instance, apply the option group when you create the instance. For more information, see [Creating an RDS Custom for Oracle DB instance](custom-creating.md#custom-creating.create).
+ For an existing DB instance, apply the option group by modifying the instance and attaching the new option group. For more information, see [Modifying your RDS Custom for Oracle DB instance](custom-managing.modifying.md).