# Supported SQL schemas for event data stores

The following sections provide the supported SQL schema for each event data store type.

###### Topics

* [Supported schema for CloudTrail event
 record ﬁelds](#query-supported-event-schema "#query-supported-event-schema")
* [Supported schema for CloudTrail Insights event record fields](#query-supported-insights-schema "#query-supported-insights-schema")
* [Supported schema for
 AWS Config configuration item record ﬁelds](#query-supported-config-items-schema "#query-supported-config-items-schema")
* [Supported schema for AWS Audit Manager evidence record
 ﬁelds](#query-supported-event-schema-audit-manager "#query-supported-event-schema-audit-manager")
* [Supported schema for non-AWS event ﬁelds](#query-supported-event-schema-integration "#query-supported-event-schema-integration")

## Supported schema for CloudTrail event
 record ﬁelds


The following is the valid SQL schema for CloudTrail management, data, and network activity event record fields. For more information about CloudTrail event record fields, see [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").



```
[
    {
        "Name": "eventversion",
        "Type": "string"
    },
    {
        "Name": "useridentity",
        "Type": "struct<type:string,principalid:string,arn:string,accountid:string,accesskeyid:string,
                 username:string,sessioncontext:struct<attributes:struct<creationdate:timestamp,
                 mfaauthenticated:string>,sessionissuer:struct<type:string,principalid:string,arn:string,
                 accountid:string,username:string>,webidfederationdata:struct<federatedprovider:string,
                 attributes:map<string,string>>,sourceidentity:string,ec2roledelivery:string,
                 ec2issuedinvpc:string>,onbehalfof:struct<userid:string,identitystorearn:string>,
                 inscopeof:struct<sourcearn:string,sourceaccount:string,issuertype:string,
                 credentiaisissuedto:string>,invokedby:string,identityprovider:string>"
    },
    {
        "Name": "eventtime",
        "Type": "timestamp"
    },
    {
        "Name": "eventsource",
        "Type": "string"
    },
    {
        "Name": "eventname",
        "Type": "string"
    },
    {
        "Name": "awsregion",
        "Type": "string"
    },
    {
        "Name": "sourceipaddress",
        "Type": "string"
    },
    {
        "Name": "useragent",
        "Type": "string"
    },
    {
        "Name": "errorcode",
        "Type": "string"
    },
    {
        "Name": "errormessage",
        "Type": "string"
    },
    {
        "Name": "requestparameters",
        "Type": "map<string,string>"
    },
    {
        "Name": "responseelements",
        "Type": "map<string,string>"
    },
    {
        "Name": "additionaleventdata",
        "Type": "map<string,string>"
    },
    {
        "Name": "requestid",
        "Type": "string"
    },
    {
        "Name": "eventid",
        "Type": "string"
    },
    {
        "Name": "readonly",
        "Type": "boolean"
    },
    {
        "Name": "resources",
        "Type": "array<struct<accountid:string,type:string,arn:string,arnprefix:string>>"
    },
    {
        "Name": "eventtype",
        "Type": "string"
    },
    {
        "Name": "apiversion",
        "Type": "string"
    },
    {
        "Name": "managementevent",
        "Type": "boolean"
    },
    {
        "Name": "recipientaccountid",
        "Type": "string"
    },
    {
        "Name": "sharedeventid",
        "Type": "string"
    },
    {
        "Name": "annotation",
        "Type": "string"
    },
    {
        "Name": "vpcendpointid",
        "Type": "string"
    },
    {
        "Name": "vpcendpointaccountid",
        "Type": "string"
    },
    {
        "Name": "serviceeventdetails",
        "Type": "map<string,string>"
    },
    {
        "Name": "addendum",
        "Type": "map<string,string>"
    },
    {
        "Name": "edgedevicedetails",
        "Type": "map<string,string>"
    },
    {
        "Name": "insightdetails",
        "Type": "map<string,string>"
    },
    {
        "Name": "eventcategory",
        "Type": "string"
    },
    {
        "Name": "tlsdetails",
        "Type": "struct<tlsversion:string,ciphersuite:string,clientprovidedhostheader:string>"
    },
    {
        "Name": "sessioncredentialfromconsole",
        "Type": "string"
    },
    {
        "Name": "eventjson",
        "Type": "string"
    }
    {
        "Name": "eventjsonchecksum",
        "Type": "string"
    }
]
```

## Supported schema for CloudTrail Insights event record fields


The following is the valid SQL schema for Insights event record fields. For
 Insights events, the value of `eventcategory` is
 `Insight`, and the value of `eventtype` is
 `AwsCloudTrailInsight`. For descriptions of these fields, see [CloudTrail record contents for Insights events for event data stores](cloudtrail-insights-fields-lake.md "cloudtrail-insights-fields-lake.md").


###### Note

The `insightvalue`, `insightaverage`, `baselinevalue`, and `baselineaverage` fields 
 within the `attributions` field of `insightContext` will begin to be deprecated on June 23, 2025.



```
[
    {
        "Name": "eventversion",
        "Type": "string"
    },
    {
        "Name": "eventcategory",
        "Type": "string"
    },
    {
        "Name": "eventtype",
        "Type": "string"
    },
        "Name": "eventid",
        "Type": "string"
    },
    {
        "Name": "eventtime",
        "Type": "timestamp"
    },
    {
        "Name": "awsregion",
        "Type": "string"
    },
    {
        "Name": "recipientaccountid",
        "Type": "string"
    },
    {
        "Name": "sharedeventid",
        "Type": "string"
    },
    {
        "Name": "addendum",
        "Type": "map<string,string>"
    },
    {
        "Name": "insightsource",
        "Type": "string"
    },
    {
        "Name": "insightstate",
        "Type": "string"
    },
    {
        "Name": "insighteventsource",
        "Type": "string"
    },
    {
        "Name": "insighteventname",
        "Type": "string"
    },
    {
        "Name": "insighterrorcode",
        "Type": "string"
    },
    {
        "Name": "insighttype",
        "Type": "string"
    },
    {
        "Name": "insightContext",
        "Type": "struct<baselineaverage:double,insightaverage:double,
                 baselineduration:integer,insightduration:integer,
                 attributions:struct<attribute:string,insightvalue:string,
                 insightaverage:double,baselinevalue:string,baselineaverage:double,
                 insight:struct<value:string,average:double>,
                 baseline:struct<value:string,average:double>>>"
    }
]
```

## Supported schema for
 AWS Config configuration item record ﬁelds


The following is the valid SQL schema for configuration item record fields. For
 configuration items, the value of `eventcategory` is
 `ConfigurationItem`, and the value of `eventtype` is
 `AwsConfigurationItem`.



```
[
    {
        "Name": "eventversion",
        "Type": "string"
    },
    {
        "Name": "eventcategory",
        "Type": "string"
    },
    {
        "Name": "eventtype",
        "Type": "string"
    },
        "Name": "eventid",
        "Type": "string"
    },
    {
        "Name": "eventtime",
        "Type": "timestamp"
    },
    {
        "Name": "awsregion",
        "Type": "string"
    },
    {
        "Name": "recipientaccountid",
        "Type": "string"
    },
    {
        "Name": "addendum",
        "Type": "map<string,string>"
    },
    {
        "Name": "eventdata",
        "Type": "struct<configurationitemversion:string,configurationitemcapturetime:
                 string,configurationitemstatus:string,configurationitemstateid:string,accountid:string,
                 resourcetype:string,resourceid:string,resourcename:string,arn:string,awsregion:string,
                 availabilityzone:string,resourcecreationtime:string,configuration:map<string,string>,
                 supplementaryconfiguration:map<string,string>,relatedevents:string,
                 relationships:struct<name:string,resourcetype:string,resourceid:string,
                 resourcename:string>,tags:map<string,string>>"
    }
]
```

## Supported schema for AWS Audit Manager evidence record
 ﬁelds


The following is the valid SQL schema for Audit Manager evidence record fields. For Audit Manager
 evidence record fields, the value of `eventcategory` is
 `Evidence`, and the value of `eventtype` is
 `AwsAuditManagerEvidence`. For more information about aggregating evidence in CloudTrail Lake using Audit Manager, see [Evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder.html "https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder.html") in
 the *AWS Audit Manager User Guide*.



```
[
    {
        "Name": "eventversion",
        "Type": "string"
    },
    {
        "Name": "eventcategory",
        "Type": "string"
    },
    {
        "Name": "eventtype",
        "Type": "string"
    },
        "Name": "eventid",
        "Type": "string"
    },
    {
        "Name": "eventtime",
        "Type": "timestamp"
    },
    {
        "Name": "awsregion",
        "Type": "string"
    },
    {
        "Name": "recipientaccountid",
        "Type": "string"
    },
    {
        "Name": "addendum",
        "Type": "map<string,string>"
    },
    {
        "Name": "eventdata",
        "Type": "struct<attributes:map<string,string>,awsaccountid:string,awsorganization:string,
                 compliancecheck:string,datasource:string,eventname:string,eventsource:string,
                 evidenceawsaccountid:string,evidencebytype:string,iamid:string,evidenceid:string,
                 time:timestamp,assessmentid:string,controlsetid:string,controlid:string,
                 controlname:string,controldomainname:string,frameworkname:string,frameworkid:string,
                 service:string,servicecategory:string,resourcearn:string,resourcetype:string,
                 evidencefolderid:string,description:string,manualevidences3resourcepath:string,
                 evidencefoldername:string,resourcecompliancecheck:string>"
    }
]
```

## Supported schema for non-AWS event ﬁelds


The following is the valid SQL schema for non-AWS events. For non-AWS events, the value of `eventcategory` is
 `ActivityAuditLog`, and the value of `eventtype` is
 `ActivityLog`.



```
[
    {
        "Name": "eventversion",
        "Type": "string"
    },
    {
        "Name": "eventcategory",
        "Type": "string"
    },
    {
        "Name": "eventtype",
        "Type": "string"
    },
        "Name": "eventid",
        "Type": "string"
    },
    {
        "Name": "eventtime",
        "Type": "timestamp"
    },
    {
        "Name": "awsregion",
        "Type": "string"
    },
    {
        "Name": "recipientaccountid",
        "Type": "string"
    },
    {
        "Name": "addendum",
        "Type": "struct<reason:string,updatedfields:string,originalUID:string,originaleventid:string>"
    },
    {
        "Name": "metadata",
        "Type": "struct<ingestiontime:string,channelarn:string>"
    },
    {
        "Name": "eventdata",
        "Type": "struct<version:string,useridentity:struct<type:string,
                 principalid:string,details:map<string,string>>,useragent:string,eventsource:string,
                 eventname:string,eventtime:string,uid:string,requestparameters:map<string,string>>,
                 responseelements":map<string,string>>,errorcode:string,errormssage:string,sourceipaddress:string,
                 recipientaccountid:string,additionaleventdata":map<string,string>>"
    }
]
```
