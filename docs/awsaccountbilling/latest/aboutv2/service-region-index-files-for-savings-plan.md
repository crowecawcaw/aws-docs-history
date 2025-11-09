# Service Region index

file for Savings Plan

|                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To provide feedback about AWS Price List, complete this [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA "https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA"). Your responses will be anonymous. \*_Note:_<br>• This survey is in English only. |

To understand the service Region index file for Savings Plan, see the following references:

###### Topics

- [Example: Service
  Region index file for Savings Plan](#service-region-index-file-for-savings-plans "#service-region-index-file-for-savings-plans")
- [Service Region index
  definitions](#service-region-index-file-definitions "#service-region-index-file-definitions")

## Example: Service

Region index file for Savings Plan

The service Region index file for Savings Plan looks like the following.

```
{
   "disclaimer":"The disclaimers for this service version index",
   "publicationDate":"The publication date of this service region index",
   "regions":[
      {
         "regionCode":"A unique identifier that identifies this region",
         "versionUrl":"The relative URL for the service regional price list file of this version"
      },
      {
         "regionCode": ...,
         "versionUrl": ...
      },
      ...
   ]
}
```

## Service Region index

definitions

The following list defines the terms in the service Region index file.

**disclaimer**

Any disclaimers that apply to the service Region index file.

**publicationDate**

The date and time in UTC format when a service Region index file was published. For
example, `2023-03-28T23:47:21Z`.

**regions**

The list of available AWS Region for the AWS service.

**regions:regionCode**

A unique code for the Region in which this AWS service is
offered. This is used as the lookup key in the Regions list. For
example, `us-east-2` is the (US East (Ohio) Region.

**regions:versionUrl**

The relative URL for the service Region index file of this version. For example,
`/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/20230407145705/us-east-2/index.json`.
