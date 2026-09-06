

# AWS Regions for your projects
<a name="project-regions"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

When you create your project, AWS assigns it to a Region—US East (Ohio) (`us-east-2`), Europe (Stockholm) (`eu-north-1`), or Asia Pacific (Sydney) (`ap-southeast-2`)—based on the country in your contact address—either the United States, Europe, or Asia Pacific. Any Regional resources that you create will be hosted in that Region.

The following are considerations for the selected AWS Region for your account:
+ If you change your contact information in AWS Settings, your selected Region will not change. If you need to access a specific Region, use Sign up for AWS (advanced). You can also activate advanced features for your account to select different Regions.
+ AWS may introduce additional supported Regions, but those will only be available for new sign-ups. To see the latest supported Regions as of August 18, 2026, see the tables below. If you already have a project, you can find your selected Region in [AWS Settings](#project-regions-find).
+ Global services are available with your project. These services are accessed via a single region that may differ from your home region. For more information, see [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html). In addition, there are some services which are available in specific Regions. In the AWS Management Console, you can view these services in certain Regions, but you'll return to your selected Region when you navigate to a different service.
+ If you use Amazon Bedrock, you can use APIs that do not create resources in all commercial AWS Regions that are enabled by default.
+ If you use CloudFront, certain features that would create resources outside of your selected Region aren't available. This includes using AWS WAF with CloudFront.
+ Some CloudTrail events involving the global services are recorded in the Region where the global service operates. You have access to these events.
+ Amazon Simple Storage Service, Amazon Kinesis, AWS WAF, Amazon CloudWatch Logs, and Amazon CloudWatch metrics are available in US East (N. Virginia) (`us-east-1`).

You can find what is the selected Region for all projects in your account by using AWS Settings. In the AWS Management Console, most service consoles are hosted in the Region you are in, including Bedrock and SageMaker. If you ever look at a service console from a global service, the console automatically routes all your API calls to the appropriate Region for the global service.

## Find the selected AWS Region for your projects
<a name="project-regions-find"></a>

As a best practice, we recommend that you always confirm the AWS Region for your project before you create any AWS resources.

**To find the selected AWS Region for your projects**

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Project**.

1. In the **Overview** section, choose **Additional Info**.

   In this view, you can also find the AWS account ID associated with your project.

1. For **Region**, you'll see the AWS Region your project has been provisioned in.

When you create Regional AWS resources in any of your projects, the Amazon Resource Names of these resources will include this AWS Region.

## Countries where Regional resources are provisioned in US East (Ohio) (`us-east-2`)
<a name="project-regions-amer"></a>


| Country name | Country code | 
| --- | --- | 
| Antigua and Barbuda | AG | 
| Argentina | AR | 
| Bahamas | BS | 
| Barbados | BB | 
| Belize | BZ | 
| Bolivia | BO | 
| Brazil | BR | 
| Canada | CA | 
| Chile | CL | 
| Colombia | CO | 
| Costa Rica | CR | 
| Dominica | DM | 
| Dominican Republic | DO | 
| Ecuador | EC | 
| El Salvador | SV | 
| Grenada | GD | 
| Guatemala | GT | 
| Guyana | GY | 
| Haiti | HT | 
| Honduras | HN | 
| Jamaica | JM | 
| Mexico | MX | 
| Nicaragua | NI | 
| Panama | PA | 
| Paraguay | PY | 
| Peru | PE | 
| Saint Kitts and Nevis | KN | 
| Saint Lucia | LC | 
| Saint Vincent and the Grenadines | VC | 
| Suriname | SR | 
| Trinidad and Tobago | TT | 
| United States | US | 
| Uruguay | UY | 
| Venezuela | VE | 
| Anguilla | AI | 
| Aruba | AW | 
| Bermuda | BM | 
| Bonaire, Sint Eustatius and Saba | BQ | 
| British Virgin Islands | VG | 
| Cayman Islands | KY | 
| Curaçao | CW | 
| Falkland Islands | FK | 
| French Guiana | GF | 
| Guadeloupe | GP | 
| Martinique | MQ | 
| Montserrat | MS | 
| Puerto Rico | PR | 
| Saint Barthélemy | BL | 
| Saint Martin | MF | 
| Saint Pierre and Miquelon | PM | 
| Sint Maarten | SX | 
| Turks and Caicos Islands | TC | 
| U.S. Virgin Islands | VI | 

## Countries where Regional resources are provisioned in Asia Pacific (Sydney) (`ap-southeast-2`)
<a name="project-regions-apac"></a>


| Country name | Country code | 
| --- | --- | 
| Afghanistan | AF | 
| Australia | AU | 
| Bangladesh | BD | 
| Bhutan | BT | 
| Brunei | BN | 
| Cambodia | KH | 
| China | CN | 
| East Timor (Timor-Leste) | TL | 
| Fiji | FJ | 
| Hong Kong | HK | 
| India | IN | 
| Indonesia | ID | 
| Japan | JP | 
| Kazakhstan | KZ | 
| Kiribati | KI | 
| Kyrgyzstan | KG | 
| Laos | LA | 
| Macau | MO | 
| Malaysia | MY | 
| Maldives | MV | 
| Marshall Islands | MH | 
| Micronesia | FM | 
| Mongolia | MN | 
| Myanmar | MM | 
| Nauru | NR | 
| Nepal | NP | 
| New Zealand | NZ | 
| Pakistan | PK | 
| Palau | PW | 
| Papua New Guinea | PG | 
| Philippines | PH | 
| Samoa | WS | 
| Singapore | SG | 
| Solomon Islands | SB | 
| South Korea | KR | 
| Sri Lanka | LK | 
| Taiwan | TW | 
| Tajikistan | TJ | 
| Thailand | TH | 
| Tonga | TO | 
| Turkmenistan | TM | 
| Tuvalu | TV | 
| Uzbekistan | UZ | 
| Vanuatu | VU | 
| Vietnam | VN | 
| American Samoa | AS | 
| Christmas Island | CX | 
| Cocos (Keeling) Islands | CC | 
| Cook Islands | CK | 
| French Polynesia | PF | 
| Guam | GU | 
| Heard Island and McDonald Islands | HM | 
| New Caledonia | NC | 
| Niue | NU | 
| Norfolk Island | NF | 
| Northern Mariana Islands | MP | 
| Pitcairn Islands | PN | 
| Tokelau | TK | 
| U.S. Minor Outlying Islands | UM | 
| Wallis and Futuna | WF | 

## Countries where Regional resources are provisioned in Europe (Stockholm) (`eu-north-1`)
<a name="project-regions-emea"></a>


| Country name | Country code | 
| --- | --- | 
| Albania | AL | 
| Algeria | DZ | 
| Andorra | AD | 
| Angola | AO | 
| Armenia | AM | 
| Austria | AT | 
| Azerbaijan | AZ | 
| Bahrain | BH | 
| Belarus | BY | 
| Belgium | BE | 
| Benin | BJ | 
| Bosnia and Herzegovina | BA | 
| Botswana | BW | 
| Bulgaria | BG | 
| Burkina Faso | BF | 
| Burundi | BI | 
| Cabo Verde | CV | 
| Cameroon | CM | 
| Central African Republic | CF | 
| Chad | TD | 
| Comoros | KM | 
| Congo (Brazzaville) | CG | 
| Congo (DRC) | CD | 
| Côte d'Ivoire | CI | 
| Croatia | HR | 
| Cyprus | CY | 
| Czech Republic | CZ | 
| Denmark | DK | 
| Djibouti | DJ | 
| Egypt | EG | 
| Equatorial Guinea | GQ | 
| Eritrea | ER | 
| Estonia | EE | 
| Eswatini | SZ | 
| Ethiopia | ET | 
| Finland | FI | 
| France | FR | 
| Gabon | GA | 
| Gambia | GM | 
| Georgia | GE | 
| Germany | DE | 
| Ghana | GH | 
| Greece | GR | 
| Guinea | GN | 
| Guinea-Bissau | GW | 
| Hungary | HU | 
| Iceland | IS | 
| Iraq | IQ | 
| Ireland | IE | 
| Israel | IL | 
| Italy | IT | 
| Jordan | JO | 
| Kenya | KE | 
| Kosovo | XK | 
| Kuwait | KW | 
| Latvia | LV | 
| Lebanon | LB | 
| Lesotho | LS | 
| Liberia | LR | 
| Libya | LY | 
| Liechtenstein | LI | 
| Lithuania | LT | 
| Luxembourg | LU | 
| Madagascar | MG | 
| Malawi | MW | 
| Mali | ML | 
| Malta | MT | 
| Mauritania | MR | 
| Mauritius | MU | 
| Moldova | MD | 
| Monaco | MC | 
| Montenegro | ME | 
| Morocco | MA | 
| Mozambique | MZ | 
| Namibia | NA | 
| Netherlands | NL | 
| Niger | NE | 
| Nigeria | NG | 
| North Macedonia | MK | 
| Norway | NO | 
| Oman | OM | 
| Palestine | PS | 
| Poland | PL | 
| Portugal | PT | 
| Qatar | QA | 
| Romania | RO | 
| Russia | RU | 
| Rwanda | RW | 
| San Marino | SM | 
| São Tomé and Príncipe | ST | 
| Saudi Arabia | SA | 
| Senegal | SN | 
| Serbia | RS | 
| Seychelles | SC | 
| Sierra Leone | SL | 
| Slovakia | SK | 
| Slovenia | SI | 
| Somalia | SO | 
| South Africa | ZA | 
| South Sudan | SS | 
| Spain | ES | 
| Sweden | SE | 
| Switzerland | CH | 
| Tanzania | TZ | 
| Togo | TG | 
| Tunisia | TN | 
| Turkey | TR | 
| Uganda | UG | 
| Ukraine | UA | 
| United Arab Emirates | AE | 
| United Kingdom | GB | 
| Vatican City | VA | 
| Yemen | YE | 
| Zambia | ZM | 
| Zimbabwe | ZW | 
| Åland Islands | AX | 
| Antarctica | AQ | 
| Bouvet Island | BV | 
| British Indian Ocean Territory | IO | 
| Faroe Islands | FO | 
| French Southern Territories | TF | 
| Gibraltar | GI | 
| Greenland | GL | 
| Guernsey | GG | 
| Isle of Man | IM | 
| Jersey | JE | 
| Mayotte | YT | 
| Réunion | RE | 
| Saint Helena | SH | 
| South Georgia and the South Sandwich Islands | GS | 
| Svalbard and Jan Mayen | SJ | 
| Western Sahara | EH | 