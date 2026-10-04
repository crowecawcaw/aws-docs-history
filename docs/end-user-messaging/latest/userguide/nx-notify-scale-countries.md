

# Supported countries
<a name="nx-notify-scale-countries"></a>

The countries available for Notify messaging depend on your configuration's tier. The Basic tier supports a curated set of 30 pre-approved countries optimized for reliability and quality. The Advanced tier supports an expanded list that includes all countries available in AWS End User Messaging; some Advanced-tier countries require you to associate your own phone pool with customer-owned origination identities. Country availability may change over time, so use the `ListNotifyCountries` API or the console to check the current list.

In the console, navigate to a Notify configuration and choose the **Countries** tab to see countries grouped by region, with an indicator on countries that require the Advanced tier. From the AWS CLI, use the `list-notify-countries` command, optionally filtered by channel, tier, or use case:

```
$ aws pinpoint-sms-voice-v2 list-notify-countries \
    --channels SMS \
    --tier BASIC
```

For each country, the response includes the ISO country code, country name, supported channels, supported use cases, supported tiers, and whether a customer-owned origination identity is required. If a country requires a customer-owned identity, associate your own phone pool as described in the get-set-up topic. To change the countries enabled on a configuration, edit the configuration. Countries that require the Advanced tier are visible on a Basic-tier configuration but cannot be selected until you upgrade.


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