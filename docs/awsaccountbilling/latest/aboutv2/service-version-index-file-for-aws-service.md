# Service version index

file for an AWS service

|                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To provide feedback about AWS Price List, complete this [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA "https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA"). Your responses will be anonymous. \*_Note:_<br>• This survey is in English only. |

To understand the service version index file, see the following references:

###### Topics

- [Example: Service
  version index file for a service](#example-service-version-index-file-service "#example-service-version-index-file-service")
- [Service version index
  file definitions](#service-version-index-definitions-sps "#service-version-index-definitions-sps")

## Example: Service

version index file for a service

The service version index file looks like the following.

```
{
   "formatVersion":"The version number for the service version index format",
   "disclaimer":"The disclaimers for this service version index",
   "publicationDate":"The publication date of this service version index",
   "offerCode": "The service code/Savings Plan code",
   "currentVersion": "The latest version of the service"
   "versions":{
      "firstVersion":{
         "versionEffectiveBeginDate":"The date starting which this version is effective",
         "versionEffectiveEndDate":"The date until which this version is effective",
         "offerVersionUrl":"The relative URL for the service price list file of this version"
      },
      "secondVersion":{
         "versionEffectiveBeginDate": ...,
         "versionEffectiveEndDate": ...,
         "offerVersionUrl": ...
      },
      ...
   },
}
```

## Service version index

file definitions

The following list defines the terms in the service version index file.

**formatVersion**

An attribute that tracks which format version the service version
index file is in. The `formatVersion` of the file is
updated when the structure is changed. For example, the version will
change from `v1` to `v2`.

**disclaimer**

Any disclaimers that apply to the service version index file.

**publicationDate**

The date and time in UTC format when a service version index file was published. For
example, `2023-03-28T23:47:21Z`.

**offerCode**

A unique code for the product of an AWS service. For example,
`AmazonRDS` or `AmazonS3`.

**currentVersion**

The latest version number of the AWS service. For example,
`20230328234721`.

**versions**

The list of available versions for this AWS service.

**versions:version**

A unique code for the version of a price list for an
AWS service. This is used as the lookup key in the versions list.
For example, `20230328234721`,

**versions:version:versionEffectiveBeginDate**

The start date and time in UTC format, which this version is
effective. For example, `2023-03-28T23:47:21Z`.

**versions:version:versionEffectiveEndDate**

The end date and time in UTC format, which this version is
effective. For example, `2023-03-28T23:47:21Z`. If this
property isn't set, this means that this version is the currently
active version.

**versions:version:offerVersionUrl**

The relative URL for the service price list files of the version. For example,
`/offers/v1.0/aws/AmazonRDS/20230328234721/index.json`.
