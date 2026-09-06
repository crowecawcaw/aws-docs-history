

# Identify your landing zone
<a name="lz-api-list"></a>

Calling `ListLandingZones` can help you determine if your account is already set up with AWS Control Tower. This API returns one landing zone identifier (ARN) across any **commercial** region, regardless of the landing zone's home region. Landing zone ARNs are regionally unique. 

```
aws controltower list-landing-zones --region us-east-1
```

For [opt-in regions](https://docs.aws.amazon.com/controltower/latest/userguide/opt-in-region-considerations.html), the `ListLandingZones` API only returns the landing zone identifier *if you call the API in the same region as the API's home region*. For example, if your landing zone is set up in af-south-1 and you call `ListLandingZones` *in af-south-1*, the API returns the landing zone identifier. If your landing zone is set up in af-south-1 and you call `ListLandingZones` *in ap-east-1*, the API **does not** return the landing zone identifier. 

**Output**: 

```
{
   "landingZones" [
        "arn": "arn:aws:controltower:us-west-2:123456789123:landingzone/1A2B3C4D5E6F7G8H"
   ]
}
```