

# Oracle time zone
<a name="custom-managing.timezone"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

To change the system time zone used by your RDS Custom for Oracle DB instance, use the time zone option. For example, you might change the time zone of a DB instance to be compatible with an on-premises environment, or a legacy application. The time zone option changes the time zone at the host level. Changing the time zone impacts all date columns and values, including `SYSDATE` and `SYSTIMESTAMP`.

**Topics**
+ [Time zone option settings in RDS Custom for Oracle](#custom-oracle-timezone.Options)
+ [Available time zones in RDS Custom for Oracle](#custom-oracle-timezone.Zones)
+ [Considerations for setting the time zone in RDS Custom for Oracle](#custom-oracle-timezone.PreReqs)
+ [Limitations for the time zone setting in RDS Custom for Oracle](#custom-oracle-timezone.overview.limitations)
+ [Adding the time zone option to an option group](#custom-oracle-timezone.Add)
+ [Removing the time zone option](#custom-oracle-timezone.remove)

## Time zone option settings in RDS Custom for Oracle
<a name="custom-oracle-timezone.Options"></a>

Amazon RDS supports the following settings for the time zone option. 



| Option setting | Valid values | Description | 
| --- | --- | --- | 
| `TIME_ZONE` | One of the available time zones. For the full list, see [Available time zones in RDS Custom for Oracle](#custom-oracle-timezone.Zones).  | The new time zone for your DB instance.  | 

## Available time zones in RDS Custom for Oracle
<a name="custom-oracle-timezone.Zones"></a>

You can use the following values for the time zone option. 



| Zone | Time zone | 
| --- | --- | 
| Africa | Africa/Cairo, Africa/Casablanca, Africa/Harare, Africa/Lagos, Africa/Luanda, Africa/Monrovia, Africa/Nairobi, Africa/Tripoli, Africa/Windhoek  | 
| America | America/Araguaina, America/Argentina/Buenos\_Aires, America/Asuncion, America/Bogota, America/Caracas, America/Chicago, America/Chihuahua, America/Cuiaba, America/Denver, America/Detroit, America/Fortaleza, America/Godthab, America/Guatemala, America/Halifax, America/Lima, America/Los\_Angeles, America/Manaus, America/Matamoros, America/Mexico\_City, America/Monterrey, America/Montevideo, America/New\_York, America/Phoenix, America/Santiago, America/Sao\_Paulo, America/Tijuana, America/Toronto  | 
| Asia | Asia/Amman, Asia/Ashgabat, Asia/Baghdad, Asia/Baku, Asia/Bangkok, Asia/Beirut, Asia/Calcutta, Asia/Damascus, Asia/Dhaka, Asia/Hong\_Kong, Asia/Irkutsk, Asia/Jakarta, Asia/Jerusalem, Asia/Kabul, Asia/Karachi, Asia/Kathmandu, Asia/Kolkata, Asia/Krasnoyarsk, Asia/Magadan, Asia/Manila, Asia/Muscat, Asia/Novosibirsk, Asia/Rangoon, Asia/Riyadh, Asia/Seoul, Asia/Shanghai, Asia/Singapore, Asia/Taipei, Asia/Tehran, Asia/Tokyo, Asia/Ulaanbaatar, Asia/Vladivostok, Asia/Yakutsk, Asia/Yerevan  | 
| Atlantic | Atlantic/Azores, Atlantic/Cape\_Verde  | 
| Australia | Australia/Adelaide, Australia/Brisbane, Australia/Darwin, Australia/Eucla, Australia/Hobart, Australia/Lord\_Howe, Australia/Perth, Australia/Sydney  | 
| Brazil | Brazil/DeNoronha, Brazil/East  | 
| Canada | Canada/Newfoundland, Canada/Saskatchewan  | 
| Etc | Etc/GMT-3 | 
| Europe | Europe/Amsterdam, Europe/Athens, Europe/Berlin, Europe/Dublin, Europe/Helsinki, Europe/Kaliningrad, Europe/London, Europe/Madrid, Europe/Moscow, Europe/Paris, Europe/Prague, Europe/Rome, Europe/Sarajevo  | 
| Pacific | Pacific/Apia, Pacific/Auckland, Pacific/Chatham, Pacific/Fiji, Pacific/Guam, Pacific/Honolulu, Pacific/Kiritimati, Pacific/Marquesas, Pacific/Samoa, Pacific/Tongatapu, Pacific/Wake  | 
| US | US/Alaska, US/Central, US/East-Indiana, US/Eastern, US/Pacific  | 
| UTC | UTC | 

## Considerations for setting the time zone in RDS Custom for Oracle
<a name="custom-oracle-timezone.PreReqs"></a>

If you choose to set the time zone for your DB instance, consider the following:
+ When you add the time zone option, a brief outage occurs while your DB instance is automatically restarted. 
+ If you accidentally set the time zone incorrectly, you must recover your DB instance to its previous time zone setting. For this reason, we strongly suggest that you to use one of the following strategies before you add the time zone option to your instance:
  + If your RDS Custom for Oracle DB instance uses the default option group, take a snapshot of your DB instance. For more information, see [Creating an RDS Custom for Oracle snapshot](custom-backup.creating.md).
  + If your DB instance currently uses a nondefault option group, take a snapshot of your DB instance, and then create a new option group with the time zone option.
+ We strongly recommend that you back up your DB instance manually after applying the `Timezone` option.
+ We strongly recommend that you to test the time zone option on a test DB instance before you add it to a production DB instance. Adding the time zone option can cause problems with tables that use system date to add dates or times. We recommend that you analyze your data and applications to assess the impact of changing the time zone. 

## Limitations for the time zone setting in RDS Custom for Oracle
<a name="custom-oracle-timezone.overview.limitations"></a>

Note the following limitations:
+ You can't change your timezone directly on your host without moving it outside the support perimeter. To change your database timezone, you must create an option group.
+ Because the time zone option is a persistent option (but not a permanent option), you can't do the following:
  + Remove the option from an option group after you add the option.
  + Modify the time zone setting of the option to a different time zone.
+ You can't associate multiple option groups with your RDS Custom for Oracle DB instance.
+ You can't set the time zone for individual PDBs within a CDB.

## Adding the time zone option to an option group
<a name="custom-oracle-timezone.Add"></a>

The default option groups for RDS Custom for Oracle are the following:
+ `default:custom-oracle-ee`
+ `default:custom-oracle-se2`
+ `default:custom-oracle-ee-cdb`
+ `default:custom-oracle-se2-cdb`

When you create an option group, the settings are derived from the default option group. For general information about option groups in Amazon RDS, see [Working with option groups](USER_WorkingWithOptionGroups.md).

### Console
<a name="custom-oracle-timezone.Console"></a>

**To add the time zone option to an option group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose the option group that you want to modify, and then choose **Add option**. 

1. In the **Add option** window, do the following: 

   1. Choose **Timezone**.

   1. In **Option settings**, choose a time zone.

   1. To enable the option on all associated RDS Custom for Oracle DB instances as soon as you add it, for **Apply Immediately**, choose **Yes**. If you choose **No** (the default), the option is enabled for each associated DB instances during its next maintenance window.

   1. 
**Important**  
If you add the time zone option to an existing option group that is already attached to one or more DB instances, a brief outage occurs while all the DB instances are automatically restarted.

1. When the settings are as you want them, choose **Add option**.

1. Back up the RDS Custom for Oracle DB instances whose time zones were updated. For more information, see [Creating an RDS Custom for Oracle snapshot](custom-backup.creating.md).

### AWS CLI
<a name="custom-oracle-timezone.CLI"></a>

The following example uses the AWS CLI [add-option-to-option-group](https://docs.aws.amazon.com/cli/latest/reference/rds/add-option-to-option-group.html) command to add the `Timezone` option and the `TIME_ZONE` option setting to an option group called `testoptiongroup`. The time zone is set to `America/Los_Angeles`. 

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name "{{testoptiongroup}}" \
    --options "{{OptionName=Timezone,OptionSettings=[{Name=TIME_ZONE,Value=America/Los_Angeles}]}}" \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name "{{testoptiongroup}}" ^
    --options "{{OptionName=Timezone,OptionSettings=[{Name=TIME_ZONE,Value=America/Los_Angeles}]}}" ^
    --apply-immediately
```

## Removing the time zone option
<a name="custom-oracle-timezone.remove"></a>

The time zone option is a persistent option, but not a permanent option. You can't remove the option from an option group after you add it. To disassociate the old option group from your DB instance:

1. Create a new option group with an updated `Timezone` option.

1. Associate the new option group with your DB instance when you modify the instance.