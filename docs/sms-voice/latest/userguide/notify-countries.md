

# Notify supported countries
<a name="notify-countries"></a>

The countries available for Notify messaging depend on your Notify configuration's tier:
+ **Basic tier** – A curated set of countries optimized for reliability and quality.
+ **Advanced tier** – An expanded list with additional countries. Some Advanced-tier countries may require you to associate your own phone pool with customer-owned origination identities.

Country availability may change over time. Use the `ListNotifyCountries` API or the console to check the current list of supported countries.

## Basic tier countries
<a name="notify-countries-basic-list"></a>

Basic tier supports 30 pre-approved countries. Use the `ListNotifyCountries` API for the most current list.


**Basic tier supported countries**  

| Country | ISO code | 
| --- | --- | 
| American Samoa | AS | 
| Australia | AU | 
| Belgium | BE | 
| Brazil | BR | 
| Canada | CA | 
| Colombia | CO | 
| Denmark | DK | 
| Finland | FI | 
| France | FR | 
| Germany | DE | 
| Guam | GU | 
| Hong Kong | HK | 
| India | IN | 
| Ireland | IE | 
| Italy | IT | 
| Japan | JP | 
| Mexico | MX | 
| Netherlands | NL | 
| New Zealand | NZ | 
| Northern Mariana Islands | MP | 
| Portugal | PT | 
| Puerto Rico | PR | 
| Singapore | SG | 
| South Korea | KR | 
| Spain | ES | 
| Sweden | SE | 
| Switzerland | CH | 
| United Kingdom | GB | 
| United States | US | 
| US Virgin Islands | VI | 

## Advanced tier countries
<a name="notify-countries-advanced-list"></a>

Advanced tier supports all countries available in AWS End User Messaging SMS. Use the `ListNotifyCountries` API with `--tier ADVANCED` to see the full list.

## Checking supported countries
<a name="notify-countries-check"></a>

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to a Notify configuration and choose the **Countries** tab.

1. The table shows countries grouped by region. Countries that require the Advanced tier are marked with an indicator. Use the property filter to search by country name or region.

------
#### [ AWS CLI ]

List all supported countries:

```
aws pinpoint-sms-voice-v2 list-notify-countries
```

Filter by channel:

```
aws pinpoint-sms-voice-v2 list-notify-countries \
  --channels SMS
```

Filter by tier:

```
aws pinpoint-sms-voice-v2 list-notify-countries \
  --tier BASIC
```

Filter by use case:

```
aws pinpoint-sms-voice-v2 list-notify-countries \
  --use-cases CODE_VERIFICATION
```

------

## Country information fields
<a name="notify-countries-response"></a>

The `ListNotifyCountries` response includes the following information for each country:

IsoCountryCode  
The two-character ISO 3166-1 alpha-2 country code.

CountryName  
The name of the country.

SupportedChannels  
The channels available for this country (`SMS`, `VOICE`).

SupportedUseCases  
The use cases available for this country.

SupportedTiers  
The tiers that can send to this country (`BASIC`, `ADVANCED`, or both).

CustomerOwnedIdentityRequired  
Whether you must associate your own phone pool with customer-owned origination identities to send to this country. If `true`, see [Using dedicated numbers with Notify](notify-dedicated-numbers.md).

## Enabling countries on a configuration
<a name="notify-countries-enable"></a>

To update the countries enabled on a Notify configuration, see [Managing Notify configurations](notify-configurations.md).

**Note**  
If your configuration is on the Basic tier, countries that require the Advanced tier are visible but cannot be selected. Upgrade to the Advanced tier to access these countries.