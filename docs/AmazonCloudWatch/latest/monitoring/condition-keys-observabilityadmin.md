

# Condition keys for CloudWatch Observability Admin
<a name="condition-keys-observabilityadmin"></a>

You can use IAM policies to control access to Amazon CloudWatch Observability Admin resources and actions by using condition keys.

Observability Admin has the following condition keys:


| Condition Key | Description | Type | 
| --- | --- | --- | 
| CentralizationSourceRegions | ArrayOfString | Filters access by the source Regions that are passed in the request | 
| CentralizationDestinationRegion | String | Filters access by the destination Region that is passed in the request | 
| CentralizationBackupRegion | String | Filters access by the backup Region that is passed in the request | 

## CentralizationSourceRegions
<a name="condition-keys-centralizationsourceregions"></a>

Filters access by the backup region specified for centralization rules.
+ *Availability* – This key is available for the following resource types: organization-centralization-rule
+ *Value type* – String

**Example JSON policy with observabilityadmin:CentralizationBackupRegion**    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
        "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

## CentralizationDestinationRegion
<a name="condition-keys-centralizationdestinationregion"></a>

Filters access by the destination region specified for centralization rules.
+ *Availability* – This key is available for the following resource types: organization-centralization-rule
+ *Value type* – String

**Example JSON policy with observabilityadmin:CentralizationDestinationRegion**    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
        "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

## CentralizationBackupRegion
<a name="condition-keys-centralizationbackupregion"></a>

Filters access by the source regions specified for centralization rules.
+ *Availability* – This key is available for the following resource types: organization-centralization-rule
+ *Value type* – List of strings

**Example JSON policy with observabilityadmin:CentralizationSourceRegions**    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
        "aws:RequestedRegion": ["us-east-1", "us-east-1"]
        }
      }
    }
  ]
}
```