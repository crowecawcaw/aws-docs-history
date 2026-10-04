

# Access to AWS Regions
<a name="remote_regions"></a>

From any Direct Connect location in a public Region or AWS GovCloud (US), you can access all public AWS Regions (except those in China (Beijing and Ningxia)), AWS GovCloud (US) Regions, and [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/). You can use Direct Connect to build multi-Region services. All networking traffic remains on the AWS global network backbone, regardless of whether you access public AWS services or a VPC.

You connect to Regions using one of the following virtual interface types:
+ **Public virtual interface** — Provides access to public resources. After you create a public virtual interface and establish a BGP session, your router learns routes for the public AWS Regions. For more information, see [Virtual interfaces and hosted virtual interfaces](WorkingWithVirtualInterfaces.md). For prefixes currently advertised by AWS, see [AWS IP Address Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the *Amazon Web Services General Reference*.
+ **Private virtual interface with a Direct Connect gateway** — Reaches VPCs in any AWS Region. For more information, see [Direct Connect gateways](direct-connect-gateways.md).
+ **Private virtual interface without a Direct Connect gateway** — Reaches a VPC in the associated Region only. The VPC must have a virtual private gateway in the same Region as the connection. For more information, see [Virtual private gateway associations](virtualgateways.md).
+ **Transit virtual interface with a Direct Connect gateway** — Reaches transit gateways in any AWS Region. For more information, see [Transit Gateway associations](direct-connect-transit-gateways.md).

Data transferred out is billed at the rate of the source Region or Local Zone where the resource resides. For more information about data transfer pricing, see the [Pricing](http://aws.amazon.com/directconnect/pricing/) section on the AWS Direct Connect detail page.

For information about routing policies and supported BGP communities, see [Routing policies and BGP communities](routing-and-bgp.md).

## Associated Region
<a name="associated-region"></a>

Each Direct Connect device is associated with a specific AWS Region. When you create a connection at a Direct Connect location, the connection inherits the associated Region of the device that it terminates on.

The associated Region determines where the connection is managed, not where your data flows. Traffic is routed based on the type of virtual interface and gateway that you create, not the associated Region. The associated Region controls:
+ **Management and configuration** — The connection and its virtual interfaces appear in the Direct Connect console and the AWS CLI in the associated Region, and you make all API operations for these resources against this Region.
+ **CloudWatch metrics** — Direct Connect publishes metrics for the connection and its virtual interfaces to Amazon CloudWatch in the associated Region.

The one exception is when you attach a private virtual interface directly to a virtual private gateway, described earlier under **Private virtual interface without a Direct Connect gateway**. In that case, the virtual private gateway must be in the same Region as the associated Region. This is the only case where the associated Region constrains which AWS resources you can reach.

**Note**  
In AWS terminology, the associated Region affects the *control plane* (management and monitoring) but not the *data plane* (the path that your traffic takes). For more information, see [Control planes and data planes](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html) in the *AWS Fault Isolation Boundaries* whitepaper.

## Locations and their associated Regions
<a name="locations-and-associated-regions"></a>

The following table lists each Direct Connect location and its associated Region.

A single Direct Connect location can host devices that are associated with different AWS Regions. In the following table, these locations list more than one associated Region, each with its own available port speeds and capabilities (**(M)** indicates MACsec encryption support at that port speed). Each device is associated with exactly one Region, and a location has separate devices for each Region that it lists.

For example, STT Hyderabad DC1 lists both Asia Pacific (Hyderabad) with 10G and 100G (MACsec) and Asia Pacific (Mumbai) with 1G and 10G. To connect at this location, you choose the associated Region whose port speed and capabilities you need. Your connection then terminates on a device for that Region and is managed in it.

**Note**  
Some associated Regions are [opt-in Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#opt-in-region) (Regions that are disabled by default). To create a connection that is associated with an opt-in Region, you must first enable the Region in your AWS account. Until you opt in, the Direct Connect location does not appear in the Direct Connect console or in API responses for that Region. For more information, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *AWS General Reference*.


**Direct Connect locations and their associated Regions ((M) indicates MACsec encryption support at that port speed)**  

| Direct Connect location | Associated Region | 
| --- | --- | 
| East Africa Data Centres NBO1, Nairobi, Kenya | Africa (Cape Town) | 
| Rack Centre LGS1, Lagos, Nigeria | Africa (Cape Town): 10G (M), 100G (M); Europe (London): 1G, 10G (M) | 
| Teraco CT1, Cape Town, South Africa | Africa (Cape Town): 10G (M), 100G (M); Europe (Ireland): 1G, 10G | 
| Equinix HK1, Tsuen Wan, N.T., Hong Kong | Asia Pacific (Hong Kong) | 
| STT Hyderabad DC1, Hyderabad, IND | Asia Pacific (Hyderabad): 10G (M), 100G (M); Asia Pacific (Mumbai): 1G, 10G | 
| DCI Indonesia, JK3 | Asia Pacific (Jakarta) | 
| NTT Jakarta 2 Data Center | Asia Pacific (Jakarta) | 
| CMC Tower, Hanoi, Vietnam | Asia Pacific (Malaysia) | 
| Menara AIMS, Kuala Lumpur, MYS | Asia Pacific (Malaysia): 10G (M), 100G (M); Asia Pacific (Singapore): 1G, 10G (M) | 
| Telcohub 1 (CX1) | Asia Pacific (Malaysia) | 
| ePLDT VM2, Makati City | Asia Pacific (Malaysia): 10G (M), 100G (M); Asia Pacific (Singapore): 1G, 10G (M) | 
| Equinix ME2, Melbourne Australia | Asia Pacific (Melbourne) | 
| Equinix MB1, Mumbai, India | Asia Pacific (Mumbai): 1G, 10G (M), 100G (M); Asia Pacific (Singapore): 1G, 10G | 
| Equinix MB2, Mumbai | Asia Pacific (Mumbai) | 
| NetMagic DC2, Bangalore, IND | Asia Pacific (Mumbai) | 
| STT Delhi DC2, Delhi, IND | Asia Pacific (Mumbai) | 
| STT GDC INDIA PVT. LTD. VSB, Chennai, IND | Asia Pacific (Mumbai) | 
| STT Kolkata, DC1 | Asia Pacific (Mumbai) | 
| Sify Rabale, Mumbai, IND | Asia Pacific (Mumbai) | 
| Spark MDR, Auckland, NZ | Asia Pacific (New Zealand) | 
| KDDI Telehouse Osaka 2 | Asia Pacific (Osaka) | 
| Digital Realty ICN10, Seoul, KOR | Asia Pacific (Seoul) | 
| KINX Gasen, Seoul, KOR | Asia Pacific (Seoul) | 
| LG U\+ Pyeong-Chon Mega Center, Seoul, KOR | Asia Pacific (Seoul) | 
| Equinix SG2, Singapore, SGP | Asia Pacific (Singapore) | 
| Global Switch, Singapore, SGP | Asia Pacific (Singapore) | 
| TCC, Bangkok | Asia Pacific (Singapore) | 
| iAdvantage MEGA-i, Hong Kong, HKG | Asia Pacific (Singapore) | 
| CDC Hume 2, Canberra | Asia Pacific (Sydney) | 
| Datacom DH6, Auckland | Asia Pacific (Sydney) | 
| Equinix SY1 - SY4, Sydney, AUS | Asia Pacific (Sydney) | 
| Global Switch SY6, Sydney, AUS | Asia Pacific (Sydney) | 
| NEXTDC B2, Brisbane | Asia Pacific (Sydney) | 
| NEXTDC C1, Canberra, AUS | Asia Pacific (Sydney) | 
| NEXTDC M1, Melbourne, AUS | Asia Pacific (Sydney) | 
| NEXTDC P1, Perth, AUS | Asia Pacific (Sydney) | 
| NEXTDC S2, Sydney, AUS | Asia Pacific (Sydney) | 
| Chief Telecom HD, Taipei, TWN | Asia Pacific (Taipei) | 
| Chunghwa Telecom, Taipei, TWN | Asia Pacific (Taipei): 10G (M), 100G (M); Asia Pacific (Tokyo): 1G, 10G (M) | 
| Telehouse Bangkok | Asia Pacific (Thailand) | 
| AT Tokyo Chuo Data Center, Tokyo, JPN | Asia Pacific (Tokyo) | 
| Chief Telecom LY, Taipei, TWN | Asia Pacific (Tokyo) | 
| Equinix OS1, Osaka, JPN | Asia Pacific (Tokyo) | 
| Equinix TY2, Tokyo, Japan | Asia Pacific (Tokyo) | 
| NEC Inzai, Japan | Asia Pacific (Tokyo) | 
| Cologix MTL3, Montreal, CAN | Canada (Central) | 
| Cologix VAN2, Vancouver, CAN | Canada (Central) | 
| Cologix VAN3, Vancouver, CAN | Canada (Central) | 
| Equinix TR2, Toronto | Canada (Central) | 
| Telehouse, Toronto, CAN | Canada (Central) | 
| eStruxture, Montreal, CAN | Canada (Central) | 
| Equinix CL1, Calgary | Canada West (Calgary) | 
| Equinix CL3, Calgary | Canada West (Calgary) | 
| CIDS Jiachuang IDC, Beijing, China | China (Beijing) | 
| GDS No. 3 DC, Shanghai, CHN | China (Beijing) | 
| Sinnet Jiuxianqiao IDC, Beijing, China | China (Beijing) | 
| Industrial Park IDC, Ningxia, CHN | China (Ningxia) | 
| Shapotou IDC, Ningxia, China | China (Ningxia) | 
| CDLAN srl Via Caldera 21, Milano | Europe (Frankfurt) | 
| CE Colo, Prague, CZE | Europe (Frankfurt) | 
| DigiPlex Ulven, Oslo, NOR | Europe (Frankfurt) | 
| Digital Realty AMS7, Amsterdam, Netherlands | Europe (Frankfurt) | 
| Digital Realty ATH3, Athens, Greece | Europe (Frankfurt) | 
| Digital Realty CPH2, Copenhagen, Denmark | Europe (Frankfurt) | 
| Digital Realty FRA6, Frankfurt, Germany | Europe (Frankfurt) | 
| Digital Realty MAD2, Madrid, Spain | Europe (Frankfurt) | 
| Digital Realty MAD3, Madrid, Spain | Europe (Frankfurt) | 
| Digital Realty STO1, Stockholm, Sweden | Europe (Frankfurt): 1G, 10G (M); Europe (Stockholm): 10G (M), 100G (M) | 
| Digital Realty VIE2, Vienna, Austria | Europe (Frankfurt) | 
| Digital Realty ZUR1, Zurich, Switzerland | Europe (Frankfurt) | 
| Equinix AM3, Amsterdam | Europe (Frankfurt) | 
| Equinix FR5, Frankfurt, DEU | Europe (Frankfurt) | 
| Equinix HE6, Helsinki, FIN | Europe (Frankfurt) | 
| Equinix IL4, Istanbul, Türkiye | Europe (Frankfurt) | 
| Equinix Itconic MD2, Madrid, ESP | Europe (Frankfurt) | 
| Equinix WA1, Warsaw, POL | Europe (Frankfurt) | 
| IPB GmbH, Berlin, DEU | Europe (Frankfurt) | 
| IPHH H3, Hamburg | Europe (Frankfurt) | 
| MedOne, Israel Haifa, ISR | Europe (Frankfurt): 1G, 10G; Israel (Tel Aviv): 10G (M), 100G (M) | 
| Telehouse Voltaire, Paris, FRA | Europe (Frankfurt): 1G, 10G (M); Europe (Paris): 1G, 10G (M), 100G (M) | 
| Digital Realty DUB2, Dublin, Ireland | Europe (Ireland) | 
| Digital Realty LHR20, London, GBR | Europe (Ireland): 1G, 10G (M); Europe (London): 1G, 10G (M) | 
| Digital Realty MRS1, Marseille, France | Europe (Ireland) | 
| Eircom Clonshaugh, Dublin, IRL | Europe (Ireland) | 
| Equinix DX1, Dubai UAE | Europe (Ireland) | 
| Equinix LD5, Slough, GBR | Europe (Ireland): 1G, 10G (M); Europe (London): 1G, 10G (M), 100G (M) | 
| Equinix LS1, Lisbon | Europe (Ireland) | 
| Etisalat Smart Hub Data Center, Fujairah, UAE | Europe (Ireland) | 
| Servecentric Unit 9, Blanchardstown, Dublin | Europe (Ireland) | 
| Teraco JB1, Johannesburg, South Africa | Europe (Ireland) | 
| Equinix MA3, Manchester, GBR | Europe (London) | 
| Telehouse West, London, GBR | Europe (London) | 
| Equinix ML2, Milano, Italy | Europe (Milan) | 
| Digital Realty PAR7, Paris, France | Europe (Paris) | 
| Equinix PA3, Paris, FRA | Europe (Paris) | 
| Equinix BA1, Barcelona, Spain | Europe (Spain) | 
| Equinix Sweden SK1 | Europe (Stockholm) | 
| Equinix ZH5, Zurich, CHE | Europe (Zurich) | 
| Edgeconnex, Herzliya, ISR | Israel (Tel Aviv) | 
| Equinix MX1, Queretaro | Mexico (Central) | 
| Cirion BNARAGMS, Buenos Aires | South America (São Paulo) | 
| Cirion LIMAPUCD, Lima | South America (São Paulo) | 
| Equinix BG1, Bogota | South America (São Paulo) | 
| Equinix RJ2, Rio de Janeiro, BRA | South America (São Paulo) | 
| Equinix SP4, Sao Paulo, BRA | South America (São Paulo) | 
| Sonda Quilicura, Santiago | South America (São Paulo) | 
| Tivit, Sao Paulo, BRA | South America (São Paulo) | 
| 165 Halsey Street, Newark, NJ | US East (N. Virginia) | 
| CoreSite NY1, New York, NY | US East (N. Virginia) | 
| CoreSite VA1, Reston, VA | US East (N. Virginia) | 
| Crown Castle, Philadelphia, PA | US East (N. Virginia) | 
| Digital Realty ATL13, Atlanta, GA | US East (N. Virginia) | 
| Digital Realty IAD38, Ashburn, VA | US East (N. Virginia) | 
| Equinix DA2, Dallas, TX | US East (N. Virginia) | 
| Equinix DC2/DC11, Ashburn, VA | US East (N. Virginia) | 
| Equinix MI1, Miami, FL | US East (N. Virginia) | 
| Equinix NY5, Secaucus, NJ | US East (N. Virginia) | 
| KIO Networks QRO 1, Queretaro | US East (N. Virginia) | 
| Markley, One Summer Street, Boston, MA | US East (N. Virginia) | 
| QTS ATL1, Atlanta, GA | US East (N. Virginia) | 
| Cologix COL2, Columbus, OH | US East (Ohio) | 
| Cologix MIN3, Minneapolis, MN | US East (Ohio) | 
| CoreSite CH1, Chicago, IL | US East (Ohio) | 
| CyrusOne Aurora A1 | US East (Ohio) | 
| DataBank HOU3, Houston, TX | US East (Ohio) | 
| Equinix CH2, Chicago, IL | US East (Ohio) | 
| Netrality Data Centers, Kansas City, MO | US East (Ohio) | 
| QTS, Chicago, IL | US East (Ohio) | 
| CoreSite LA1, Los Angeles, CA | US West (N. California) | 
| CoreSite SV4, Santa Clara, CA | US West (N. California) | 
| Coresite SV2, Milpitas, CA | US West (N. California) | 
| EdgeConnex PHX01, Phoenix, AZ | US West (N. California) | 
| Equinix LA3, El Segundo, CA | US West (N. California) | 
| Equinix SV5, San Jose, CA | US West (N. California) | 
| PhoenixNAP, Phoenix, AZ | US West (N. California) | 
| AlohaNap, Kapolei, HI | US West (Oregon) | 
| CoreSite DE1, Denver, CO | US West (Oregon) | 
| DataBank LAS1 | US West (Oregon) | 
| EdgeConnex, Hillsboro, OR | US West (Oregon) | 
| Pittock Block, Portland, OR | US West (Oregon) | 
| Serverfarm LAX1 El Segundo, CA | US West (Oregon) | 
| Switch SUPERNAP 8, Las Vegas, NV | US West (Oregon) | 
| TierPoint, Seattle, WA | US West (Oregon) | 
| Westin Building Exchange, Seattle, WA | US West (Oregon) | 
| Equinix SV5, San Jose, CA | AWS GovCloud (US-West) | 
| Atlas Edge BER001, Berlin, DEU | EU Sovereign Cloud (Germany) | 
| IPB GmbH, Berlin, DEU | EU Sovereign Cloud (Germany) | 