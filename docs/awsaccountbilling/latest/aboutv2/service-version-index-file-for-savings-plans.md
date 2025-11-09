# Service version index

file for Savings Plan

|                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To provide feedback about AWS Price List, complete this [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA "https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA"). Your responses will be anonymous. \*_Note:_<br>• This survey is in English only. |

To understand the service version index file for Savings Plan, see the following references:

###### Contents

- [Example:
  Service version index file for Savings Plan](service-version-index-file-for-savings-plans.md#service-version-index-file-savings-plans-example "service-version-index-file-for-savings-plans.md#service-version-index-file-savings-plans-example")
- [Service version index
  definitions](service-version-index-file-for-savings-plans.md#service-version-index-definitions "service-version-index-file-for-savings-plans.md#service-version-index-definitions")

## Example:

Service version index file for Savings Plan

The service version index file for a Savings Plan looks like the following.

```
{
   "disclaimer":"The disclaimers for this service version index",
   "publicationDate":"The publication date of this service version index",
   "currentOfferVersionUrl" "The relative URL of region index file for latest version number of the service"
   "versions":[
      {
         "publicationDate":"The publication date of this version of service from which this version was effective",
         "offerVersionUrl":"The relative URL for the service region index file of this version"
      },
      {
         "publicationDate": ...,
         "offerVersionUrl": ...
      },
      ...
   ],
}
```

## Service version index

definitions

The following list defines the terms in the service version index file.

**disclaimer**

Any disclaimers that apply to the service version index file.

**publicationDate**

The date and time in UTC format when a service version index file was published. For
example, `2023-03-28T23:47:21Z`.

**currentOfferVersionUrl**

The relative URL of the regional index file for latest version
number of the service. For example,
`/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json`.

**versions**

The list of available version for this AWS service.

**versions:version:publicationDate**

The date and time in UTC format when an service version index file
was published. For example, `2023-04-07T14:57:05Z`

**versions:version:offerVersionUrl**

The relative URL for the service regional index file of this
version. For example,
`/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/20230407145705/region_index.json`.
