# Request routing optimization for CDN and MediaTailor

integrations

Implement these routing optimizations for all AWS Elemental MediaTailor CDN integrations:

- Create separate cache behaviors for manifest and segment requests
- Configure origin request policies to control header forwarding
- Set up proper error handling and failover mechanisms
- Implement origin shields if available in your CDN to reduce origin load
- Implement request collapsing at the CDN level to efficiently handle concurrent
  requests
