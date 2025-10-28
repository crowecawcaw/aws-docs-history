# MediaTailor domain variables for multiple content

sources

AWS Elemental MediaTailor dynamic domain variables allow you to use multiple domains, such as the
**my-ads-server.com** part of the URL
http://my-ads-server.com, with the player parameters in your configuration. This makes
it possible for you to use more than one content source or ad decision server (ADS) in a
single configuration.

You can use domain variables with any parameter that contains a URI:

- `AdDecisionServerUrl`
- `AdSegmentUrlPrefix`
- `ContentSegmentUrlPrefix`
- `LivePreroll.AdDecisionServerUrl`
- `VideoContentSourceUrl`
  Domain variables are used alongside _configuration aliases_ to
  perform dynamic variable replacement. Configuration aliases map a set of aliases and
  values to the player parameters that are used for dynamic domain configuration. For
  setup procedures, see [Creating and using configuration
  aliases with MediaTailor](creating-configuration-aliases.md "creating-configuration-aliases.md"). For detailed reference
  information, see [MediaTailor configuration aliases
  overview](configuration-aliases-overview.md "configuration-aliases-overview.md").
