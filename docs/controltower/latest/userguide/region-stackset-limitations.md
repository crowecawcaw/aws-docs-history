

# Limitations based on underlying AWS services
<a name="region-stackset-limitations"></a>

This page describes limitations that you may encounter due to limitations in other AWS services, and how AWS Control Tower works with those services. 

**General guidelines**

As a general rule, we expect that the number of accounts supported when registering an OU diminishes as you increase the number of Regions governed, and the number of controls enabled, for that OU. These general guidelines assume that you have 15 optional controls enabled. If you have more or fewer controls enabled on your OU, the limits on accounts per OU will differ when registering.
+ With 15 governed Regions, OUs of up to 1000 accounts are supported.
+ With 16 to 21 governed Regions, the maximum supported OU size is in the range of 600-1000 accounts.
+ With 22 governed Regions, OUs of up to 680 accounts are supported.
+ With 23 or more governed Regions, the maximum supported OU size is less than 680 accounts.

**In case of error**

If registration fails, you can try to **Re-register** the OU. Also, you can make the OU smaller by using a nested OU or by moving acounts to another OU.

**Note**  
The mandatory controls that AWS Control Tower always enforces are not counted toward the number of controls you've enabled on an OU, for purposes of registration.

**CloudFormation stack set limitations**

If you plan to register a large number of accounts across multiple AWS Regions, you may encounter limits created by CloudFormation stack sets on the overall size of an organization. You can estimate the limitation with this formula:

*Number of managed accounts in the organization x Number of governed Regions <= 150,000*

This limitation becomes apparent during the OU registration process. For example, if 15 Regions are governed, and 15 optional controls are enabled, the limit for registering the OU is 1000 accounts. However, if you require to register OUs with more than 1000 accounts, or if you have a large number of optional controls enabled, you must reduce the number of governed Regions below 15. This reduction is due to stack set limitations. 

**AWS Config limitations**

If you plan to register OUs with a large number of accounts, you may encounter limits with [the maximum number of accounts that AWS Config allows to be created or deleted each week](https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html), across all aggregators. Enrolled accounts do not count toward this limit: You may enroll up to 1000 new accounts into AWS Control Tower each week.

**First-time limitations for accounts and opt-in Regions**

If you plan to register OUs with a large number of accounts across multiple opt-in Regions *for the first time*, you may encounter limitations due to [Account Management quotas](https://docs.aws.amazon.com/accounts/latest/reference/quotas.html), which can lead to prolonged latency. Errors may occur during OU registration due to latency.