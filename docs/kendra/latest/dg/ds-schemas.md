# Data source template schemas

The following are template schemas for data sources where templates are supported.

###### Topics

- [Adobe Experience Manager template
  schema](#ds-aem-schema "#ds-aem-schema")
- [Amazon FSx (Windows) template schema](#ds-fsx-windows-schema "#ds-fsx-windows-schema")
- [Amazon FSx (NetApp ONTAP) template
  schema](#ds-fsx-ontap-schema "#ds-fsx-ontap-schema")
- [Alfresco template schema](#ds-alfresco-schema "#ds-alfresco-schema")
- [Aurora (MySQL) template schema](#ds-aurora-mysql-schema "#ds-aurora-mysql-schema")
- [Aurora (PostgreSQL) template
  schema](#ds-aurora-postgresql-schema "#ds-aurora-postgresql-schema")
- [Amazon RDS (Microsoft SQL Server)
  template schema](#ds-rds-ms-sql-server-schema "#ds-rds-ms-sql-server-schema")
- [Amazon RDS (MySQL) template schema](#ds-rds-mysql-schema "#ds-rds-mysql-schema")
- [Amazon RDS (Oracle) template schema](#ds-rds-oracle-schema "#ds-rds-oracle-schema")
- [Amazon RDS (PostgreSQL) template
  schema](#ds-rds-postgresql-schema "#ds-rds-postgresql-schema")
- [Amazon S3 template schema](#ds-s3-schema "#ds-s3-schema")
- [Amazon Kendra Web Crawler template schema](#ds-schema-web-crawler "#ds-schema-web-crawler")
- [Confluence template schema](#ds-confluence-schema "#ds-confluence-schema")
- [Dropbox template schema](#ds-dropbox-schema "#ds-dropbox-schema")
- [Drupal template schema](#ds-drupal-schema "#ds-drupal-schema")
- [GitHub template schema](#ds-github-schema "#ds-github-schema")
- [Gmail template schema](#ds-gmail-schema "#ds-gmail-schema")
- [Google Drive template schema](#ds-googledrive-schema "#ds-googledrive-schema")
- [IBM DB2 template schema](#ds-ibm-db2-schema "#ds-ibm-db2-schema")
- [Microsoft Exchange template schema](#ds-msexchange-schema "#ds-msexchange-schema")
- [Microsoft OneDrive template schema](#ds-onedrive-schema "#ds-onedrive-schema")
- [Microsoft SharePoint template schema](#ds-schema-sharepoint "#ds-schema-sharepoint")
- [Microsoft SQL Server template schema](#ds-ms-sql-server-schema "#ds-ms-sql-server-schema")
- [Microsoft Teams template schema](#ds-msteams-schema "#ds-msteams-schema")
- [Microsoft Yammer template schema](#ds-schema-yammer "#ds-schema-yammer")
- [MySQL template schema](#ds-mysql-schema "#ds-mysql-schema")
- [Oracle Database template schema](#ds-oracle-database-schema "#ds-oracle-database-schema")
- [PostgreSQL template schema](#ds-postgresql-schema "#ds-postgresql-schema")
- [Salesforce template schema](#ds-salesforce-schema "#ds-salesforce-schema")
- [ServiceNow template schema](#ds-servicenow-schema "#ds-servicenow-schema")
- [Slack template schema](#ds-schema-slack "#ds-schema-slack")
- [Zendesk template schema](#ds-schema-zendesk "#ds-schema-zendesk")

## Adobe Experience Manager template

schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") object. You provide the Adobe
Experience Manager host URL, the authentication type, and whether you use
Adobe Experience Manager (AEM) as a Cloud Service or AEM On-Premise as part
of the connection configuration or repository endpoint details. Also, specify the type of data
source as `AEM`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md").

You can use the template provided in this developer guide. For more information, see [Adobe Experience Manager JSON schema](#aem-json "#aem-json").

The following table describes the parameters of the AEM JSON schema.

| Configuration                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata                                                                                                                                 | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| aemUrl                                                                                                                                                     | The Adobe Experience Manager host URL. For example, if you use AEM<br>On-Premise, you include the hostname and port:<br>_https://hostname:port_. Or, if you use AEM as a<br>Cloud Service, you can use the author URL:<br>*https://author-xxxxxx-xxxxxxx.adobeaemcloud.com*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| authType                                                                                                                                                   | The type of authentication you use, whether `Basic` or<br>`OAuth2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| deploymentType                                                                                                                                             | The type of Adobe Experience Manager that you use, either<br>`CLOUD` or `ON_PREMISE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| repositoryConfigurations                                                                                                                                   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • page<br>• asset                                                                                                                                          | A list of objects that map the attributes or field names of your Adobe<br>Experience Manager pages and assets to Amazon Kendra index field names.<br>For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| additionalProperties                                                                                                                                       | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| timeZoneId                                                                                                                                                 | If you use AEM On-Premise and the time zone of your server is different than the<br>time zone of the Amazon Kendra AEM connector or index, you can specify the<br>server time zone to align with the AEM connector or index.<br>The default time zone for AEM On-Premise is the time zone of the Amazon Kendra AEM connector or index. The default time zone for AEM as a Cloud<br>Service is Greenwich Mean Time.                                                                                                                                                                                                                                                                                                                                                                      |
| • pageRootPaths<br>• assetRootPaths                                                                                                                        | A list of root paths for pages and assets. For example, the root path for a page<br>could be _/content/sub<br>• and the root path for an asset could be<br>_/content/sub/asset1\*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| crawlAssets                                                                                                                                                | `true` to crawl assets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| crawlPages                                                                                                                                                 | `true` to crawl pages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| • pagePathInclusionPatterns<br>• pageNameInclusionPatterns<br>• assetPathInclusionPatterns<br>• assetTypeInclusionPatterns<br>• assetNameInclusionPatterns | A list of regular expression patterns to include certain pages and assets in your<br>Adobe Experience Manager data source. Pages and assets that match the<br>patterns are included in the index. Pages and assets that don't match the patterns are<br>excluded from the index. If a page or asset matches both an inclusion and exclusion<br>pattern, the exclusion pattern takes precedence, and the content isn't included in the<br>index.                                                                                                                                                                                                                                                                                                                                         |
| • pagePathExclusionPatterns<br>• pageNameExclusionPatterns<br>• assetPathExclusionPatterns<br>• assetTypeInclusionPatterns<br>• assetNameInclusionPatterns | A list of regular expression patterns to exclude certain pages and assets in your<br>Adobe Experience Manager data source. Pages and assets that match the<br>patterns are excluded from the index. Pages and assets that don't match the patterns<br>are included in the index. If a page or asset matches both an inclusion and exclusion<br>pattern, the exclusion pattern takes precedence, and the content isn't included in the<br>index.                                                                                                                                                                                                                                                                                                                                         |
| pageComponents                                                                                                                                             | A list of names for the specific page components that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| contentFragmentVariations                                                                                                                                  | A list of names for the specific saved variations of Adobe Experience<br>Manager Content Fragments that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| type                                                                                                                                                       | The type of data source. Specify `AEM` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| syncMode                                                                                                                                                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                                                                                                                                                  | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Adobe Experience Manager. For<br>information on these key-value pairs, see [Connection<br>instructions for Adobe Experience Manager](data-source-aem.md#data-source-procedure-aem "data-source-aem.md#data-source-procedure-aem").                                                                                                                                                                                                                                                                                                                                                                                                                     |
| version                                                                                                                                                    | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties":
  {
    "connectionConfiguration": {
      "type": "object",
      "properties":
      {
        "repositoryEndpointMetadata":
        {
          "type": "object",
          "properties":
          {
            "aemUrl":
            {
              "type": "string",
              "pattern": "https:.*"
            },
            "authType": {
              "type": "string",
              "enum": ["Basic", "OAuth2"]
            },
            "deploymentType": {
              "type": "string",
              "enum": ["CLOUD","ON_PREMISE"]
            }
          },
          "required":
          [
            "aemUrl",
            "authType",
            "deploymentType"
          ]
        }
      },
      "required":
      [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties":
      {
        "page":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "asset":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties":
      {
        "timeZoneId": {
          "type": "string",
          "enum": [
            "Africa/Abidjan",
            "Africa/Accra",
            "Africa/Addis_Ababa",
            "Africa/Algiers",
            "Africa/Asmara",
            "Africa/Asmera",
            "Africa/Bamako",
            "Africa/Bangui",
            "Africa/Banjul",
            "Africa/Bissau",
            "Africa/Blantyre",
            "Africa/Brazzaville",
            "Africa/Bujumbura",
            "Africa/Cairo",
            "Africa/Casablanca",
            "Africa/Ceuta",
            "Africa/Conakry",
            "Africa/Dakar",
            "Africa/Dar_es_Salaam",
            "Africa/Djibouti",
            "Africa/Douala",
            "Africa/El_Aaiun",
            "Africa/Freetown",
            "Africa/Gaborone",
            "Africa/Harare",
            "Africa/Johannesburg",
            "Africa/Juba",
            "Africa/Kampala",
            "Africa/Khartoum",
            "Africa/Kigali",
            "Africa/Kinshasa",
            "Africa/Lagos",
            "Africa/Libreville",
            "Africa/Lome",
            "Africa/Luanda",
            "Africa/Lubumbashi",
            "Africa/Lusaka",
            "Africa/Malabo",
            "Africa/Maputo",
            "Africa/Maseru",
            "Africa/Mbabane",
            "Africa/Mogadishu",
            "Africa/Monrovia",
            "Africa/Nairobi",
            "Africa/Ndjamena",
            "Africa/Niamey",
            "Africa/Nouakchott",
            "Africa/Ouagadougou",
            "Africa/Porto-Novo",
            "Africa/Sao_Tome",
            "Africa/Timbuktu",
            "Africa/Tripoli",
            "Africa/Tunis",
            "Africa/Windhoek",
            "America/Adak",
            "America/Anchorage",
            "America/Anguilla",
            "America/Antigua",
            "America/Araguaina",
            "America/Argentina/Buenos_Aires",
            "America/Argentina/Catamarca",
            "America/Argentina/ComodRivadavia",
            "America/Argentina/Cordoba",
            "America/Argentina/Jujuy",
            "America/Argentina/La_Rioja",
            "America/Argentina/Mendoza",
            "America/Argentina/Rio_Gallegos",
            "America/Argentina/Salta",
            "America/Argentina/San_Juan",
            "America/Argentina/San_Luis",
            "America/Argentina/Tucuman",
            "America/Argentina/Ushuaia",
            "America/Aruba",
            "America/Asuncion",
            "America/Atikokan",
            "America/Atka",
            "America/Bahia",
            "America/Bahia_Banderas",
            "America/Barbados",
            "America/Belem",
            "America/Belize",
            "America/Blanc-Sablon",
            "America/Boa_Vista",
            "America/Bogota",
            "America/Boise",
            "America/Buenos_Aires",
            "America/Cambridge_Bay",
            "America/Campo_Grande",
            "America/Cancun",
            "America/Caracas",
            "America/Catamarca",
            "America/Cayenne",
            "America/Cayman",
            "America/Chicago",
            "America/Chihuahua",
            "America/Ciudad_Juarez",
            "America/Coral_Harbour",
            "America/Cordoba",
            "America/Costa_Rica",
            "America/Creston",
            "America/Cuiaba",
            "America/Curacao",
            "America/Danmarkshavn",
            "America/Dawson",
            "America/Dawson_Creek",
            "America/Denver",
            "America/Detroit",
            "America/Dominica",
            "America/Edmonton",
            "America/Eirunepe",
            "America/El_Salvador",
            "America/Ensenada",
            "America/Fort_Nelson",
            "America/Fort_Wayne",
            "America/Fortaleza",
            "America/Glace_Bay",
            "America/Godthab",
            "America/Goose_Bay",
            "America/Grand_Turk",
            "America/Grenada",
            "America/Guadeloupe",
            "America/Guatemala",
            "America/Guayaquil",
            "America/Guyana",
            "America/Halifax",
            "America/Havana",
            "America/Hermosillo",
            "America/Indiana/Indianapolis",
            "America/Indiana/Knox",
            "America/Indiana/Marengo",
            "America/Indiana/Petersburg",
            "America/Indiana/Tell_City",
            "America/Indiana/Vevay",
            "America/Indiana/Vincennes",
            "America/Indiana/Winamac",
            "America/Indianapolis",
            "America/Inuvik",
            "America/Iqaluit",
            "America/Jamaica",
            "America/Jujuy",
            "America/Juneau",
            "America/Kentucky/Louisville",
            "America/Kentucky/Monticello",
            "America/Knox_IN",
            "America/Kralendijk",
            "America/La_Paz",
            "America/Lima",
            "America/Los_Angeles",
            "America/Louisville",
            "America/Lower_Princes",
            "America/Maceio",
            "America/Managua",
            "America/Manaus",
            "America/Marigot",
            "America/Martinique",
            "America/Matamoros",
            "America/Mazatlan",
            "America/Mendoza",
            "America/Menominee",
            "America/Merida",
            "America/Metlakatla",
            "America/Mexico_City",
            "America/Miquelon",
            "America/Moncton",
            "America/Monterrey",
            "America/Montevideo",
            "America/Montreal",
            "America/Montserrat",
            "America/Nassau",
            "America/New_York",
            "America/Nipigon",
            "America/Nome",
            "America/Noronha",
            "America/North_Dakota/Beulah",
            "America/North_Dakota/Center",
            "America/North_Dakota/New_Salem",
            "America/Nuuk",
            "America/Ojinaga",
            "America/Panama",
            "America/Pangnirtung",
            "America/Paramaribo",
            "America/Phoenix",
            "America/Port-au-Prince",
            "America/Port_of_Spain",
            "America/Porto_Acre",
            "America/Porto_Velho",
            "America/Puerto_Rico",
            "America/Punta_Arenas",
            "America/Rainy_River",
            "America/Rankin_Inlet",
            "America/Recife",
            "America/Regina",
            "America/Resolute",
            "America/Rio_Branco",
            "America/Rosario",
            "America/Santa_Isabel",
            "America/Santarem",
            "America/Santiago",
            "America/Santo_Domingo",
            "America/Sao_Paulo",
            "America/Scoresbysund",
            "America/Shiprock",
            "America/Sitka",
            "America/St_Barthelemy",
            "America/St_Johns",
            "America/St_Kitts",
            "America/St_Lucia",
            "America/St_Thomas",
            "America/St_Vincent",
            "America/Swift_Current",
            "America/Tegucigalpa",
            "America/Thule",
            "America/Thunder_Bay",
            "America/Tijuana",
            "America/Toronto",
            "America/Tortola",
            "America/Vancouver",
            "America/Virgin",
            "America/Whitehorse",
            "America/Winnipeg",
            "America/Yakutat",
            "America/Yellowknife",
            "Antarctica/Casey",
            "Antarctica/Davis",
            "Antarctica/DumontDUrville",
            "Antarctica/Macquarie",
            "Antarctica/Mawson",
            "Antarctica/McMurdo",
            "Antarctica/Palmer",
            "Antarctica/Rothera",
            "Antarctica/South_Pole",
            "Antarctica/Syowa",
            "Antarctica/Troll",
            "Antarctica/Vostok",
            "Arctic/Longyearbyen",
            "Asia/Aden",
            "Asia/Almaty",
            "Asia/Amman",
            "Asia/Anadyr",
            "Asia/Aqtau",
            "Asia/Aqtobe",
            "Asia/Ashgabat",
            "Asia/Ashkhabad",
            "Asia/Atyrau",
            "Asia/Baghdad",
            "Asia/Bahrain",
            "Asia/Baku",
            "Asia/Bangkok",
            "Asia/Barnaul",
            "Asia/Beirut",
            "Asia/Bishkek",
            "Asia/Brunei",
            "Asia/Calcutta",
            "Asia/Chita",
            "Asia/Choibalsan",
            "Asia/Chongqing",
            "Asia/Chungking",
            "Asia/Colombo",
            "Asia/Dacca",
            "Asia/Damascus",
            "Asia/Dhaka",
            "Asia/Dili",
            "Asia/Dubai",
            "Asia/Dushanbe",
            "Asia/Famagusta",
            "Asia/Gaza",
            "Asia/Harbin",
            "Asia/Hebron",
            "Asia/Ho_Chi_Minh",
            "Asia/Hong_Kong",
            "Asia/Hovd",
            "Asia/Irkutsk",
            "Asia/Istanbul",
            "Asia/Jakarta",
            "Asia/Jayapura",
            "Asia/Jerusalem",
            "Asia/Kabul",
            "Asia/Kamchatka",
            "Asia/Karachi",
            "Asia/Kashgar",
            "Asia/Kathmandu",
            "Asia/Katmandu",
            "Asia/Khandyga",
            "Asia/Kolkata",
            "Asia/Krasnoyarsk",
            "Asia/Kuala_Lumpur",
            "Asia/Kuching",
            "Asia/Kuwait",
            "Asia/Macao",
            "Asia/Macau",
            "Asia/Magadan",
            "Asia/Makassar",
            "Asia/Manila",
            "Asia/Muscat",
            "Asia/Nicosia",
            "Asia/Novokuznetsk",
            "Asia/Novosibirsk",
            "Asia/Omsk",
            "Asia/Oral",
            "Asia/Phnom_Penh",
            "Asia/Pontianak",
            "Asia/Pyongyang",
            "Asia/Qatar",
            "Asia/Qostanay",
            "Asia/Qyzylorda",
            "Asia/Rangoon",
            "Asia/Riyadh",
            "Asia/Saigon",
            "Asia/Sakhalin",
            "Asia/Samarkand",
            "Asia/Seoul",
            "Asia/Shanghai",
            "Asia/Singapore",
            "Asia/Srednekolymsk",
            "Asia/Taipei",
            "Asia/Tashkent",
            "Asia/Tbilisi",
            "Asia/Tehran",
            "Asia/Tel_Aviv",
            "Asia/Thimbu",
            "Asia/Thimphu",
            "Asia/Tokyo",
            "Asia/Tomsk",
            "Asia/Ujung_Pandang",
            "Asia/Ulaanbaatar",
            "Asia/Ulan_Bator",
            "Asia/Urumqi",
            "Asia/Ust-Nera",
            "Asia/Vientiane",
            "Asia/Vladivostok",
            "Asia/Yakutsk",
            "Asia/Yangon",
            "Asia/Yekaterinburg",
            "Asia/Yerevan",
            "Atlantic/Azores",
            "Atlantic/Bermuda",
            "Atlantic/Canary",
            "Atlantic/Cape_Verde",
            "Atlantic/Faeroe",
            "Atlantic/Faroe",
            "Atlantic/Jan_Mayen",
            "Atlantic/Madeira",
            "Atlantic/Reykjavik",
            "Atlantic/South_Georgia",
            "Atlantic/St_Helena",
            "Atlantic/Stanley",
            "Australia/ACT",
            "Australia/Adelaide",
            "Australia/Brisbane",
            "Australia/Broken_Hill",
            "Australia/Canberra",
            "Australia/Currie",
            "Australia/Darwin",
            "Australia/Eucla",
            "Australia/Hobart",
            "Australia/LHI",
            "Australia/Lindeman",
            "Australia/Lord_Howe",
            "Australia/Melbourne",
            "Australia/NSW",
            "Australia/North",
            "Australia/Perth",
            "Australia/Queensland",
            "Australia/South",
            "Australia/Sydney",
            "Australia/Tasmania",
            "Australia/Victoria",
            "Australia/West",
            "Australia/Yancowinna",
            "Brazil/Acre",
            "Brazil/DeNoronha",
            "Brazil/East",
            "Brazil/West",
            "CET",
            "CST6CDT",
            "Canada/Atlantic",
            "Canada/Central",
            "Canada/Eastern",
            "Canada/Mountain",
            "Canada/Newfoundland",
            "Canada/Pacific",
            "Canada/Saskatchewan",
            "Canada/Yukon",
            "Chile/Continental",
            "Chile/EasterIsland",
            "Cuba",
            "EET",
            "EST5EDT",
            "Egypt",
            "Eire",
            "Etc/GMT",
            "Etc/GMT+0",
            "Etc/GMT+1",
            "Etc/GMT+10",
            "Etc/GMT+11",
            "Etc/GMT+12",
            "Etc/GMT+2",
            "Etc/GMT+3",
            "Etc/GMT+4",
            "Etc/GMT+5",
            "Etc/GMT+6",
            "Etc/GMT+7",
            "Etc/GMT+8",
            "Etc/GMT+9",
            "Etc/GMT-0",
            "Etc/GMT-1",
            "Etc/GMT-10",
            "Etc/GMT-11",
            "Etc/GMT-12",
            "Etc/GMT-13",
            "Etc/GMT-14",
            "Etc/GMT-2",
            "Etc/GMT-3",
            "Etc/GMT-4",
            "Etc/GMT-5",
            "Etc/GMT-6",
            "Etc/GMT-7",
            "Etc/GMT-8",
            "Etc/GMT-9",
            "Etc/GMT0",
            "Etc/Greenwich",
            "Etc/UCT",
            "Etc/UTC",
            "Etc/Universal",
            "Etc/Zulu",
            "Europe/Amsterdam",
            "Europe/Andorra",
            "Europe/Astrakhan",
            "Europe/Athens",
            "Europe/Belfast",
            "Europe/Belgrade",
            "Europe/Berlin",
            "Europe/Bratislava",
            "Europe/Brussels",
            "Europe/Bucharest",
            "Europe/Budapest",
            "Europe/Busingen",
            "Europe/Chisinau",
            "Europe/Copenhagen",
            "Europe/Dublin",
            "Europe/Gibraltar",
            "Europe/Guernsey",
            "Europe/Helsinki",
            "Europe/Isle_of_Man",
            "Europe/Istanbul",
            "Europe/Jersey",
            "Europe/Kaliningrad",
            "Europe/Kiev",
            "Europe/Kirov",
            "Europe/Kyiv",
            "Europe/Lisbon",
            "Europe/Ljubljana",
            "Europe/London",
            "Europe/Luxembourg",
            "Europe/Madrid",
            "Europe/Malta",
            "Europe/Mariehamn",
            "Europe/Minsk",
            "Europe/Monaco",
            "Europe/Moscow",
            "Europe/Nicosia",
            "Europe/Oslo",
            "Europe/Paris",
            "Europe/Podgorica",
            "Europe/Prague",
            "Europe/Riga",
            "Europe/Rome",
            "Europe/Samara",
            "Europe/San_Marino",
            "Europe/Sarajevo",
            "Europe/Saratov",
            "Europe/Simferopol",
            "Europe/Skopje",
            "Europe/Sofia",
            "Europe/Stockholm",
            "Europe/Tallinn",
            "Europe/Tirane",
            "Europe/Tiraspol",
            "Europe/Ulyanovsk",
            "Europe/Uzhgorod",
            "Europe/Vaduz",
            "Europe/Vatican",
            "Europe/Vienna",
            "Europe/Vilnius",
            "Europe/Volgograd",
            "Europe/Warsaw",
            "Europe/Zagreb",
            "Europe/Zaporozhye",
            "Europe/Zurich",
            "GB",
            "GB-Eire",
            "GMT",
            "GMT0",
            "Greenwich",
            "Hongkong",
            "Iceland",
            "Indian/Antananarivo",
            "Indian/Chagos",
            "Indian/Christmas",
            "Indian/Cocos",
            "Indian/Comoro",
            "Indian/Kerguelen",
            "Indian/Mahe",
            "Indian/Maldives",
            "Indian/Mauritius",
            "Indian/Mayotte",
            "Indian/Reunion",
            "Iran",
            "Israel",
            "Jamaica",
            "Japan",
            "Kwajalein",
            "Libya",
            "MET",
            "MST7MDT",
            "Mexico/BajaNorte",
            "Mexico/BajaSur",
            "Mexico/General",
            "NZ",
            "NZ-CHAT",
            "Navajo",
            "PRC",
            "PST8PDT",
            "Pacific/Apia",
            "Pacific/Auckland",
            "Pacific/Bougainville",
            "Pacific/Chatham",
            "Pacific/Chuuk",
            "Pacific/Easter",
            "Pacific/Efate",
            "Pacific/Enderbury",
            "Pacific/Fakaofo",
            "Pacific/Fiji",
            "Pacific/Funafuti",
            "Pacific/Galapagos",
            "Pacific/Gambier",
            "Pacific/Guadalcanal",
            "Pacific/Guam",
            "Pacific/Honolulu",
            "Pacific/Johnston",
            "Pacific/Kanton",
            "Pacific/Kiritimati",
            "Pacific/Kosrae",
            "Pacific/Kwajalein",
            "Pacific/Majuro",
            "Pacific/Marquesas",
            "Pacific/Midway",
            "Pacific/Nauru",
            "Pacific/Niue",
            "Pacific/Norfolk",
            "Pacific/Noumea",
            "Pacific/Pago_Pago",
            "Pacific/Palau",
            "Pacific/Pitcairn",
            "Pacific/Pohnpei",
            "Pacific/Ponape",
            "Pacific/Port_Moresby",
            "Pacific/Rarotonga",
            "Pacific/Saipan",
            "Pacific/Samoa",
            "Pacific/Tahiti",
            "Pacific/Tarawa",
            "Pacific/Tongatapu",
            "Pacific/Truk",
            "Pacific/Wake",
            "Pacific/Wallis",
            "Pacific/Yap",
            "Poland",
            "Portugal",
            "ROK",
            "Singapore",
            "SystemV/AST4",
            "SystemV/AST4ADT",
            "SystemV/CST6",
            "SystemV/CST6CDT",
            "SystemV/EST5",
            "SystemV/EST5EDT",
            "SystemV/HST10",
            "SystemV/MST7",
            "SystemV/MST7MDT",
            "SystemV/PST8",
            "SystemV/PST8PDT",
            "SystemV/YST9",
            "SystemV/YST9YDT",
            "Turkey",
            "UCT",
            "US/Alaska",
            "US/Aleutian",
            "US/Arizona",
            "US/Central",
            "US/East-Indiana",
            "US/Eastern",
            "US/Hawaii",
            "US/Indiana-Starke",
            "US/Michigan",
            "US/Mountain",
            "US/Pacific",
            "US/Samoa",
            "UTC",
            "Universal",
            "W-SU",
            "WET",
            "Zulu",
            "EST",
            "HST",
            "MST",
            "ACT",
            "AET",
            "AGT",
            "ART",
            "AST",
            "BET",
            "BST",
            "CAT",
            "CNT",
            "CST",
            "CTT",
            "EAT",
            "ECT",
            "IET",
            "IST",
            "JST",
            "MIT",
            "NET",
            "NST",
            "PLT",
            "PNT",
            "PRT",
            "PST",
            "SST",
            "VST"
          ]
        },
        "pageRootPaths":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "assetRootPaths":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "crawlAssets":
        {
          "type": "boolean"
        },
        "crawlPages":
        {
          "type": "boolean"
        },
        "pagePathInclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "pagePathExclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "pageNameInclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "pageNameExclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "assetPathInclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "assetPathExclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "assetTypeInclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "assetTypeExclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "assetNameInclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "assetNameExclusionPatterns":
        {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "pageComponents": {
          "type": "array",
          "items": {
            "type": "object"
            }
        },
        "contentFragmentVariations": {
          "type": "array",
          "items": {
            "type": "object"
          }
        },
        "cugExemptedPrincipals": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required":
      []
    },
    "type": {
      "type": "string",
      "pattern": "AEM"
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}
```

## Amazon FSx (Windows) template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the file system ID as
part of the connection configuration or repository endpoint details. You must also specify the
type of data source as `FSX`, a secret for your authentication
credentials, and other necessary configurations. You then specify
`TEMPLATE` as the `Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Amazon FSx (Windows) JSON schema](#fsx-windows-json "#fsx-windows-json").

The following table describes the parameters of the Amazon FSx (Windows) JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryEndpointMetadata | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| fileSystemId               | The identifier of the Amazon FSx file system. You can find your file<br>system ID on the File Systems dashboard in the Amazon FSx console.                                                                                                                                                                                                                                                                                                                                                                                      |
| fileSystemType             | The Amazon FSx file system type. To use Windows File<br>Server as your type of file system, specify `WINDOWS`.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                         |
| All                        | A list of objects that map attributes or field names of your files in your<br>Amazon FSx data source to Amazon Kendra index field names. For more<br>information, see [Mapping data source fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                        |
| additionalProperties       | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| isCrawlAcl                 | `true` to crawl the access control list (ACL) information for your<br>documents, if you have an ACL and want to use it for access control. The ACL specifies<br>which documents that users and groups can access. The ACL information is<br>used to filter search results based on the user or their group access to documents.<br>For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").               |
| inclusionPatterns          | A list of regular expression patterns to \*include<br>• certain<br>files in your Amazon FSx data source. Files that match the patterns are<br>included in the index. Files that don't match the patterns are excluded from the<br>index. If a file matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                         |
| exclusionPatterns          | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Amazon FSx data source. Files that match the patterns are<br>excluded from the index. Files that don't match the patterns are included in the<br>index. If a file matches both an exclusion and inclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                         |
| enableIdentityCrawler      | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| type                       | The type of data source. For Windows file system data sources, specify<br>`FSX`.                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "fileSystemId": {
              "type": "string",
              "pattern": "fs-.*"
            },
            "fileSystemType": {
              "type": "string",
              "pattern": "WINDOWS"
            }
          },
          "required": ["fileSystemId", "fileSystemType"]
        }
      }
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "All": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "STRING_LIST", "DATE"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": ["fieldMappings"]
        }
      },
      "required": ["All"]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "isCrawlAcl": {
          "type": "boolean"
        },
        "exclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": []
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "type" : {
      "type" : "string",
      "pattern": "FSX"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "enableIdentityCrawler",
    "additionalProperties",
    "type"
  ]
}
```

## Amazon FSx (NetApp ONTAP) template

schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the file system ID and
the storage virtual machine (SVM) as part of the connection configuration or repository
endpoint details. You must also specify the type of data source as
`FSXONTAP`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Amazon FSx (NetApp ONTAP) JSON schema](#fsx-ontap-json "#fsx-ontap-json").

The following table describes the parameters of the Amazon FSx (NetApp ONTAP) JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| repositoryEndpointMetadata | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| fileSystemId               | The identifier of the Amazon FSx file system. You can find your file<br>system ID on the File Systems dashboard in the Amazon FSx console. For<br>information about how to create a file system in the Amazon FSx console for<br>NetApp ONTAP, see [Getting Started Guide for NetApp<br>ONTAP](../../../fsx/latest/ONTAPGuide/getting-started.md "../../../fsx/latest/ONTAPGuide/getting-started.md") in the _FSx for ONTAP User<br>Guide_.                                                                                                                                                  |
| fileSystemType             | The Amazon FSx file system type. To use NetApp ONTAP as<br>your type of file system, specify `ONTAP`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| svmId                      | The identifier of storage virtual machine (SVM) used with your Amazon FSx<br>file system for NetApp ONTAP. You can find your SVM ID by going to the<br>File Systems dashboard in the Amazon FSx console, selecting your file system<br>ID, and then selecting **Storage virtual machines**. For information<br>about how to create a file system in the Amazon FSx console for NetApp<br>ONTAP, see [Getting Started Guide for NetApp<br>ONTAP](../../../fsx/latest/ONTAPGuide/getting-started.md "../../../fsx/latest/ONTAPGuide/getting-started.md") in the _FSx for ONTAP User<br>Guide_. |
| protocolType               | Whether you use the Common Internet File System (CIFS) protocol for Windows, or<br>the Network File System (NFS) protocol for Linux.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| file                       | A list of objects that map attributes or field names of your files in your<br>Amazon FSx data source to Amazon Kendra index field names. For more<br>information, see [Mapping data source fields](field-mapping.md "field-mapping.md"). The data source field names must exist in your<br>files custom metadata.                                                                                                                                                                                                                                                                            |
| additionalProperties       | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| crawlAcl                   | `true` to crawl the access control list (ACL) information for your<br>documents, if you have an ACL and want to use it for access control. The ACL specifies<br>which documents that users and groups can access. The ACL information is<br>used to filter search results based on the user or their group access to documents.<br>For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").                                                                            |
| inclusionPatterns          | A list of regular expression patterns to \*include<br>• certain<br>files in your Amazon FSx data source. Files that match the patterns are<br>included in the index. Files that don't match the patterns are excluded from the<br>index. If a file matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                      |
| exclusionPatterns          | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Amazon FSx data source. Files that match the patterns are<br>excluded from the index. Files that don't match the patterns are included in the<br>index. If a file matches both an exclusion and inclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                      |
| type                       | The type of data source. For NetApp ONTAP file system data<br>sources, specify `FSXONTAP`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.                                                              |
| secretArn                  | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Amazon FSx file system. The<br>secret must contain a JSON structure with the following keys:<br>``<br>{<br>"username": "`user@corp.example.com`",<br>"password": "`password`"<br>}<br>``<br>If you use the NFS protocol for your Amazon FSx file system, the secret<br>is stored in a JSON structure with the following keys:<br>``<br>{<br>"leftId": "`left ID`",<br>"rightId": "`right ID`",<br>"preSharedKey": "`pre-shared key`"<br>}<br>``             |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "fileSystemId": {
              "type": "string",
                "pattern": "^(fs-[0-9a-f]{8,21})$"
            },
            "fileSystemType": {
              "type": "string",
              "enum": ["ONTAP"]
            },
            "svmId": {
              "type": "string",
              "pattern": "^(svm-[0-9a-f]{17,21})$"
            },
            "protocolType": {
              "type": "string",
              "enum": [
                "CIFS",
                "NFS"
              ]
            }
          },
          "required": [
            "fileSystemId",
            "fileSystemType"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "file": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string",
                      "pattern": "^([a-zA-Z_]{1,20})$"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string",
                      "pattern": "^([a-zA-Z_]{1,20})$"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ],
              "maxItems": 50
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
        "file"
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "crawlAcl": {
          "type": "boolean"
        },
        "inclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string",
            "maxLength": 30
          },
          "maxItems": 100
        },
        "exclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string",
            "maxLength": 30
          },
          "maxItems": 100
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "FSXONTAP"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string",
      "pattern": "arn:aws:secretsmanager:.*"
    }
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}
```

## Alfresco template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") object. You provide the
Alfresco site ID, repository URL, user interface URL, authentication type,
whether you use cloud or on-premises, and the type of content you want to crawl. You provide
this as a part of the connection configuration or repository endpoint details. Also specify
the type of data source as `ALFRESCO`, a secret for your authentication
credentials, and other necessary configurations. You then specify
`TEMPLATE` as the `Type` when you call [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Alfresco JSON schema](#alfresco-json "#alfresco-json").

The following table describes the parameters of the Alfresco JSON schema.

| Configuration                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                   | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryEndpointMetadata                                                                | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| siteId                                                                                    | The identifier of the Alfresco site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| repoUrl                                                                                   | The URL of your Alfresco repository. You can get the repository<br>URL from your Alfresco administrator. For example, if you use<br>Alfresco Cloud (PaaS), the repository URL could be<br>*https://company.alfrescocloud.com*. Or, if you<br>use Alfresco On-Premises, the repository URL could be<br>*https://company-alfresco-instance.company-domain.suffix:port*.                                                                                                                                                           |
| webAppUrl                                                                                 | The URL of your Alfresco user interface. You can get the<br>Alfresco user interface URL from your Alfresco<br>administrator. For example, the user interface URL could be<br>*https://example.com*.                                                                                                                                                                                                                                                                                                                             |
| repositoryAdditionalProperties                                                            | Additional properties to connect with the repository/data source<br>endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| authType                                                                                  | The type of authentication that you use, whether<br>`OAuth2` or `Basic`.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| type (deployment)                                                                         | The type of Alfresco that you use, whether<br>`PAAS` or `ON-PREM`.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| crawlType                                                                                 | The type of content that you want to crawl, whether<br>`ASPECT` (content marked with 'Aspects' in<br>Alfresco), `SITE_ID` (content within a<br>specific Alfresco site), or `ALL_SITES`<br>(content across all your Alfresco sites).                                                                                                                                                                                                                                                                                             |
| repositoryConfigurations                                                                  | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                         |
| • document<br>• comment                                                                   | A list of objects that map the attributes or field names of your Alfresco<br>documents and comments to Amazon Kendra index field names. For more information,<br>see [Mapping data<br>source fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                      |
| additionalProperties                                                                      | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| aspectName                                                                                | The name of a specific 'Aspect' that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| aspectProperties                                                                          | A list of specific 'Aspect' content properties that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| enableFineGrainedControl                                                                  | `true` to crawl 'Aspects'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| isCrawlComment                                                                            | `true` to crawl comments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| • inclusionFileNamePatterns<br>• inclusionFileTypePatterns<br>• inclusionFilePathPatterns | A list of regular expression patterns to include certain files in your<br>Alfresco data source. Files that match the patterns are included in<br>the index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the file isn't included in the index.                                                                                                                                                 |
| • exclusionFileNamePatterns<br>• exclusionFileTypePatterns<br>• exclusionFilePathPatterns | A list of regular expression patterns to exclude certain files in your<br>Alfresco data source. Files that match the patterns are excluded from<br>the index. Files that don't match the patterns are included in the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the file isn't included in the index.                                                                                                                                                 |
| type                                                                                      | The type of data source. Specify `ALFRESCO` as your<br>data source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| secretArn                                                                                 | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs that are required to connect to your Alfresco.<br>The secret must contain a JSON structure with the following keys:<br>If using basic authentication:<br>``<br>{<br>"username": "`user name`",<br>"password": "`password`"<br>}<br>``<br>If using OAuth 2.0 authentication:<br>``<br>{<br>"clientId": "`client ID`",<br>"clientSecret": "`client secret`",<br>"tokenUrl": "`token URL`"<br>}<br>``                         |
| syncMode                                                                                  | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| enableIdentityCrawler                                                                     | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                    |
| version                                                                                   | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "siteId": {
              "type": "string"
            },
            "repoUrl": {
              "type": "string"
            },
            "webAppUrl": {
              "type": "string"
            },
            "repositoryAdditionalProperties": {
              "type": "object",
              "properties": {
                "authType": {
                  "type": "string",
                  "enum": [
                    "OAuth2",
                    "Basic"
                  ]
                },
                "type": {
                  "type": "string",
                  "enum": [
                    "PAAS",
                    "ON_PREM"
                  ]
                },
                "crawlType": {
                  "type": "string",
                  "enum": [
                    "ASPECT",
                    "SITE_ID",
                    "ALL_SITES"
                  ]
                }
              }
            }
          }
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE",
                          "STRING_LIST",
                          "LONG"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "comment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE",
                          "STRING_LIST",
                          "LONG"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "aspectName": {
          "type": "string"
        },
        "aspectProperties": {
          "type": "array"
        },
        "enableFineGrainedControl": {
          "type": "boolean"
        },
        "isCrawlComment": {
          "type": "boolean"
        },
        "inclusionFileNamePatterns": {
          "type": "array"
        },
        "exclusionFileNamePatterns": {
          "type": "array"
        },
        "inclusionFileTypePatterns": {
          "type": "array"
        },
        "exclusionFileTypePatterns": {
          "type": "array"
        },
        "inclusionFilePathPatterns": {
          "type": "array"
        },
        "exclusionFilePathPatterns": {
          "type": "array"
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "ALFRESCO"
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "version": {
      "type": "string",
      "anyOf": [
        {
          "pattern": "1.0.0"
        }
      ]
    }
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "type",
    "secretArn"
  ]
}
```

## Aurora (MySQL) template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `mysql`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Aurora (MySQL) JSON schema](#aurora-mysql-json "#aurora-mysql-json").

The following table describes the parameters of the Aurora (MySQL) JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Aurora (PostgreSQL) template

schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `postgresql`, a secret for your authentication credentials,
and other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Aurora (PostgreSQL) JSON
schema](#aurora-postgresql-json "#aurora-postgresql-json").

The following table describes the parameters of the Aurora (PostgreSQL) JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Amazon RDS (Microsoft SQL Server)

template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `sqlserver`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Amazon RDS (Microsoft SQL Server) JSON
schema](#rds-ms-sql-server-json "#rds-ms-sql-server-json").

The following table describes the parameters of the Amazon RDS (Microsoft SQL
Server) JSON schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Amazon RDS (MySQL) template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `mysql`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Amazon RDS (MySQL) JSON schema](#rds-mysql-json "#rds-mysql-json").

The following table describes the parameters of the Amazon RDS (MySQL) JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Amazon RDS (Oracle) template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `oracle`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Amazon RDS (Oracle) JSON schema](#rds-oracle-json "#rds-oracle-json").

The following table describes the parameters of the Amazon RDS (Oracle) JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Amazon RDS (PostgreSQL) template

schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `postgresql`, a secret for your authentication credentials,
and other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Amazon RDS (PostgreSQL) JSON schema](#rds-postgresql-json "#rds-postgresql-json").

The following table describes the parameters of the Amazon RDS (PostgreSQL) JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Amazon S3 template schema

You include a JSON that contains the data source schema as part of the template
configuration. You provide the name of the S3 bucket as a part of the connection configuration
or repository endpoint details. Also specify the type of data source as `S3`, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [S3 JSON schema](#s3-json "#s3-json").

The following table describes the parameters of the Amazon S3 JSON schema.

| Configuration                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                  | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryEndpointMetadata                                                               | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| BucketName                                                                               | The name of your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| repositoryConfigurations                                                                 | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                         |
| additionalProperties                                                                     | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| • inclusionPatterns<br>• exclusionPatterns<br>• inclusionPrefixes<br>• exclusionPrefixes | A list of regular expression patterns to include or exclude specific files in<br>your Amazon S3 data source. Files that match the patterns are included in the<br>index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                                     |
| aclConfigurationFilePath                                                                 | The file path that controls access to documents in an Amazon Kendra<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| metadataFilesPrefix                                                                      | The location within your bucket for metadata files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| syncMode                                                                                 | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| type                                                                                     | The type of data source. Specify `S3` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| version                                                                                  | The version of the template that is supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "BucketName": {
              "type": "string"
            }
          },
          "required": [
            "BucketName"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
        "document"
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "inclusionPatterns": {
          "type": "array"
        },
        "exclusionPatterns": {
          "type": "array"
        },
        "inclusionPrefixes": {
          "type": "array"
        },
        "exclusionPrefixes": {
          "type": "array"
        },
        "aclConfigurationFilePath": {
          "type": "string"
        },
        "metadataFilesPrefix": {
          "type": "string"
        }
      }
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL"
      ]
    },
    "type": {
      "type": "string",
      "pattern": "S3"
    },
    "version": {
      "type": "string",
      "anyOf": [
        {
          "pattern": "1.0.0"
        }
      ]
    }
  },
  "required": [
    "connectionConfiguration",
    "type",
    "syncMode",
    "repositoryConfigurations"
  ]
}
```

## Amazon Kendra Web Crawler template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") object.

You provide the seed or starting point URLs, or you can provide the sitemap URLs, as part
of the connection configuration or repository endpoint details. Instead of manually listing
all your URLs, you can provide the path to the Amazon S3 bucket that stores a text
file for your list of seed URLs or sitemap XML files, which you can club together in a ZIP
file in S3.

You also specify the type of data source as `WEBCRAWLERV2`, the
website authentication credentials and authentication type if your websites require
authentication, and other necessary configurations.

You then specify `TEMPLATE` as the `Type` when you
call [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md").

###### Important

Web Crawler v2.0 connector creation is not supported by CloudFormation. Use the Web
Crawler v1.0 connector if you need CloudFormation support.

_When selecting websites to index, you must adhere to the [Amazon Acceptable Use Policy](https://aws.amazon.com/aup/ "https://aws.amazon.com/aup/") and all other
Amazon terms. Remember that you must only use Amazon Kendra Web Crawler to index your
own web pages, or web pages that you have authorization to index. To learn how to stop
Amazon Kendra Web Crawler from indexing your websites, see [Configuring the robots.txt file for
Amazon Kendra Web Crawler](stop-web-crawler.md "stop-web-crawler.md")._

You can use the template provided in this developer guide. See [Amazon Kendra Web Crawler JSON schema](#web-crawler-json "#web-crawler-json").

The following table describes the parameters of the Amazon Kendra Web Crawler JSON
schema.

| Configuration                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| repositoryEndpointMetadata                                 | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| siteMapUrls                                                | The list of sitemap URLs for the websites that you want to crawl. You can list up<br>to three sitemap URLs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| s3SeedUrl                                                  | The S3 path to the text file that stores the list of seed or starting point URLs.<br>For example, _s3://bucket-name/directory/_. Each URL<br>in the text file must be formatted on a separate line. You can list up to 100 seed<br>URLs in a file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| s3SiteMapUrl                                               | The S3 path to the sitemap XML files. For example,<br>_s3://bucket-name/directory/_. You can list up<br>to three sitemap XML files. You can club together multiple sitemap files into a ZIP<br>file and store the ZIP file in your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| seedUrlConnections                                         | The list of seed or starting point URLs for the websites that you want to<br>crawl.You can list up to 100 seed URLs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| seedUrl                                                    | The seed or starting point URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| authentication                                             | The authentication type if your websites require the same authentication,<br>otherwise specify `NoAuthentication`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| repositoryConfigurations                                   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| • webPage<br>• attachment                                  | A list of objects that map the attributes or field names of your web pages and<br>web page files to Amazon Kendra index field names. For example, the HTML web page<br>title tag can be mapped to the `_document_title` index<br>field. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| syncMode                                                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| additionalProperties                                       | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| rateLimit                                                  | The maximum number of URLs crawled per website host per minute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| maxFileSize                                                | The maximum size (in MB) of a web page or attachment to crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| crawlDepth                                                 | The number of levels from the seed URL to crawl. For example, the seed URL page<br>is depth 1 and any hyperlinks on this page that are also crawled are depth 2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| maxLinksPerUrl                                             | The maximum number of URLs on a web page to include when crawling a website. This<br>number is per web page. As a website's web pages are crawled, any URLs that the<br>webpages link to also are crawled. URLs on a web page are crawled in order of<br>appearance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| crawlSubDomain                                             | `true` to crawl the website domains with subdomains. For example, if<br>the seed URL is "abc.example.com", then<br>"a.abc.example.com" and "b.abc.example.com" are also<br>crawled. If you don't set `crawlSubDomain` or<br>`crawlAllDomain` to `true`, then Amazon Kendra only crawls the domains of the websites that you want to crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| crawlAllDomain                                             | `true` to crawl the website domains with subdomains and other domains<br>the web pages link to. If you don't set `crawlSubDomain` or<br>`crawlAllDomain` to `true`, then Amazon Kendra only crawls the domains of the websites that you want to crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| honorRobots                                                | `true` to respect the robots.txt directives of the websites that you<br>want to crawl. These directives control how Amazon Kendra Web Crawler crawls the<br>websites, whether Amazon Kendra can crawl only specific content or not crawl any<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| crawlAttachments                                           | `true` to crawl files that the web pages link to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| • inclusionURLCrawlPatterns<br>• inclusionURLIndexPatterns | A list of regular expression patterns to \*include<br>• crawling<br>certain URLs and indexing any hyperlinks on these URL web pages. URLs that match the<br>patterns are included in the index. URLs that don't match the patterns are excluded<br>from the index. If a URL matches both an inclusion and exclusion pattern, the<br>exclusion pattern takes precedence, and the URL/website's web pages aren't included in<br>the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| • exclusionURLCrawlPatterns<br>• exclusionURLIndexPatterns | A list of regular expression patterns to \*exclude<br>• crawling<br>certain URLs and indexing any hyperlinks on these URL web pages. URLs that match the<br>patterns are excluded from the index. URLs that don't match the patterns are included<br>in the index. If a URL matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence, and the URL/website's web pages aren't included in the<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| inclusionFileIndexPatterns                                 | A list of regular expression patterns to \*include<br>• certain web<br>page files. Files that match the patterns are included in the index. Files that don't<br>match the patterns are excluded from the index. If a file matches both an inclusion<br>and exclusion pattern, the exclusion pattern takes precedence, and the file isn't<br>included in the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| exclusionFileIndexPatterns                                 | A list of regular expression patterns to \*exclude<br>• certain web<br>page files. Files that match the patterns are excluded from the index. Files that<br>don't match the patterns are included in the index. If a file matches both an<br>inclusion and exclusion pattern, the exclusion pattern takes precedence, and the file<br>isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| implicitWaitDuration                                       | implicitWaitDuration specifies how long the connector will wait, in seconds,<br>before crawling a webpage.<br>Range: 0-10<br>eg. "implicitWaitDuration": "5"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| proxy                                                      | Configuration information required to connect to your internal websites via a web<br>proxy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| host                                                       | The host name of the proxy sever you want to use to connect to internal websites.<br>For example, the host name of<br>\*https://a.example.com/page1.html<br>• is<br>"a.example.com".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| port                                                       | The port number of the proxy sever you want to use to connect to internal<br>websites. For example, 443 is the standard port for HTTPS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| secretArn (proxy)                                          | If web proxy credentials are required to connect to a website host, you can<br>create an AWS Secrets Manager secret that stores the credentials. Provide the<br>Amazon Resource Name (ARN) of the secret.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                                                       | The type of data source. Specify `WEBCRAWLERV2` as your<br>data source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| secretArn                                                  | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that's used<br>if your websites require authentication to access the websites. You store the<br>authentication credentials for the website in the secret that contains JSON<br>key-value pairs.<br>If you use basic, or NTML/Kerberos, enter the user name and password. The JSON<br>keys in the secret must be `userName` and<br>`password`. NTLM authentication protocol includes<br>password hashing, and Kerberos authentication protocol includes password<br>encryption.<br>If you use SAML or form authentication, enter the user name and password, XPath<br>for the user name field (and user name button if using SAML), XPaths for the<br>password field and button, and the login page URL. The JSON keys in the secret must<br>be `userName`, `password`,<br>`userNameFieldXpath`,<br>`userNameButtonXpath`,<br>`passwordFieldXpath`,<br>`passwordButtonXpath`, and<br>`loginPageUrl`. You can find the XPaths (XML Path<br>Language) of elements using your web browser's developer tools. XPaths usually<br>follow this format: `//tagname[@Attribute='Value']`.<br>Amazon Kendra also checks if the endpoint information (seed URLs) included<br>in the secret is the same the endpoint information specified in your data source<br>endpoint configuration details. |
| version                                                    | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "siteMapUrls": {
              "type": "array",
              "items":{
                "type": "string",
                "pattern": "https://.*"
              }
            },
            "s3SeedUrl": {
              "type": "string",
              "pattern": "s3:.*"
            },
            "s3SiteMapUrl": {
              "type": "string",
              "pattern": "s3:.*"
            },
            "seedUrlConnections": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "seedUrl":{
                      "type": "string",
                      "pattern": "https://.*"
                    }
                  },
                  "required": [
                    "seedUrl"
                  ]
                }
              ]
            },
            "authentication": {
              "type": "string",
              "enum": [
                "NoAuthentication",
                "BasicAuth",
                "NTLM_Kerberos",
                "Form",
                "SAML"
              ]
            }
          }
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "webPage": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "attachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "rateLimit": {
          "type": "string",
          "default": "300"
        },
        "maxFileSize": {
          "type": "string",
          "default": "50"
        },
        "crawlDepth": {
          "type": "string",
          "default": "2"
        },
        "maxLinksPerUrl": {
          "type": "string",
          "default": "100"
        },
        "crawlSubDomain": {
          "type": "boolean",
          "default": false
        },
        "crawlAllDomain": {
          "type": "boolean",
          "default": false
        },
        "honorRobots": {
          "type": "boolean",
          "default": false
        },
        "crawlAttachments": {
          "type": "boolean",
          "default": false
        },
        "inclusionURLCrawlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionURLCrawlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionURLIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionURLIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "proxy": {
          "type": "object",
          "properties": {
            "host": {
              "type": "string"
            },
            "port": {
              "type": "string"
            },
            "secretArn": {
              "type": "string",
              "minLength": 20,
              "maxLength": 2048
            }
          }
        }
      },
      "implicitWaitDuration":  {
          "type":"object",
          "properties": {
            "innerNumber" : {
              "type": "number",
              "minimum": 0,
              "maximum": 10
            }
          }
        },
      "required": [
        "rateLimit",
        "maxFileSize",
        "crawlDepth",
        "crawlSubDomain",
        "crawlAllDomain",
        "maxLinksPerUrl",
        "honorRobots"
      ]
    },
    "type": {
      "type": "string",
      "pattern": "WEBCRAWLERV2"
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "type",
    "additionalProperties"
  ]
}
```

## Confluence template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the Confluence host URL, the hosting
method, and the authentication type as a part of the connection configuration or repository
endpoint details. Also specify the type of data source as `CONFLUENCEV2`, a secret
for your authentication credentials, and other necessary configurations. You then specify
`TEMPLATE` as the `Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Confluence JSON schema](#confluence-json "#confluence-json").

The following table describes the parameters of the Confluence JSON schema.

| Configuration                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                                                                           | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| repositoryEndpointMetadata                                                                                                                                                                                                                                        | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| hostUrl                                                                                                                                                                                                                                                           | The URL for your Confluence instance. For example,<br>`https://example.confluence.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| type                                                                                                                                                                                                                                                              | The hosting method for your Confluence instance, whether `SAAS` and<br>`ON_PREM`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| authType                                                                                                                                                                                                                                                          | The authentication method for your Confluence instance, whether<br>`Basic`, `OAuth2`, or `Personal-token`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| repositoryConfigurations                                                                                                                                                                                                                                          | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| • space<br>• page<br>• blog<br>• comment<br>• attachment                                                                                                                                                                                                          | A list of objects that map the attributes or field names of your Confluence<br>spaces, pages, blogs, comments, and attachments to Amazon Kendra index field<br>names. For more information, see [Mapping data source fields](field-mapping.md "field-mapping.md"). The<br>Confluence data source field names must exist in your Confluence custom<br>metadata.                                                                                                                                                                                                                                                              |
| additionalProperties                                                                                                                                                                                                                                              | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| isCrawlAcl                                                                                                                                                                                                                                                        | Configure `true` to crawl the access control list (ACL) information<br>for your documents, if you have an ACL and want to use it for access control. Note<br>that the ACL specifies which documents that users and groups can access. The ACL<br>information is used to filter search results based on the user or their group access<br>to documents. This means that if `isCrawlACL` is turned off, documents can<br>be publicly searched. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources"). |
| fieldForUserId                                                                                                                                                                                                                                                    | Specify `email` if you want to use the user email for the user<br>ID. `email` is used by default and is currently the only supported user<br>ID type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| • inclusionSpaceKeyFilter<br>• exclusionSpaceKeyFilter<br>• pageTitleRegEX<br>• blogTitleRegEX<br>• commentTitleRegEX<br>• attachmentTitleRegEX<br>• inclusionFileTypePatterns<br>• exclusionFileTypePatterns<br>• inclusionUrlPatterns<br>• exclusionUrlPatterns | A list of regular expression patterns to include and/or exclude certain files in<br>your Confluence data source. Files that match the patterns are included in the index.<br>Files that don't match the patterns are excluded from the index. If a file matches<br>both an inclusion and exclusion pattern, the exclusion pattern takes precedence and<br>the file isn't included in the index.                                                                                                                                                                                                                             |
| proxyHost                                                                                                                                                                                                                                                         | The host name of the web proxy that you use, without the `http://` or<br>`https://` protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| proxyPort                                                                                                                                                                                                                                                         | The port number used by the host URL transport protocol. Must be a numeric value<br>between 0 and 65535.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| • isCrawlPersonalSpace<br>• isCrawlArchivedSpace<br>• isCrawlArchivedPage<br>• isCrawlPage<br>• isCrawlBlog<br>• isCrawlPageComment<br>• isCrawlPageAttachment<br>• isCrawlBlogComment<br>• isCrawlBlogAttachment                                                 | `true` to crawl files in your Confluence personal spaces, pages,<br>blogs, page comments, page attachments, blog comments, and blog attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| maxFileSizeInMegaBytes                                                                                                                                                                                                                                            | Specify the file size limit in MBs that Amazon Kendra can crawl. Amazon Kendra crawls only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal<br>to 50MB.                                                                                                                                                                                                                                                                                                                                                                |
| type                                                                                                                                                                                                                                                              | The type of data source. Specify `CONFLUENCEV2` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| enableIdentityCrawler                                                                                                                                                                                                                                             | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                |
| syncMode                                                                                                                                                                                                                                                          | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.                                                                                             |
| secretARN                                                                                                                                                                                                                                                         | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Confluence. For information on these<br>key-value pairs, see [Connection instructions for Confluence](data-source-v2-confluence.md#data-source-procedure-v2-confluence "data-source-v2-confluence.md#data-source-procedure-v2-confluence").                                                                                                                                                                                                                                                |
| version                                                                                                                                                                                                                                                           | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "hostUrl": {
              "type": "string",
              "pattern": "https:.*"
            },
            "type": {
              "type": "string",
              "enum": [
                "SAAS",
                "ON_PREM"
              ]
            },
            "authType": {
              "type": "string",
              "enum": [
                "Basic",
                "OAuth2",
                "Personal-token"
              ]
            }
          },
          "required": [
            "hostUrl",
            "type",
            "authType"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "space": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "page": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "blog": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "comment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "attachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "usersAclS3FilePath": {
          "type": "string"
        },
        "isCrawlAcl": {
          "type": "boolean"
        },
        "fieldForUserId": {
          "type": "string"
        },
        "inclusionSpaceKeyFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionSpaceKeyFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "pageTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "blogTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "commentTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "attachmentTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isCrawlPersonalSpace": {
          "type": "boolean"
        },
        "isCrawlArchivedSpace": {
          "type": "boolean"
        },
        "isCrawlArchivedPage": {
          "type": "boolean"
        },
        "isCrawlPage": {
          "type": "boolean"
        },
        "isCrawlBlog": {
          "type": "boolean"
        },
        "isCrawlPageComment": {
          "type": "boolean"
        },
        "isCrawlPageAttachment": {
          "type": "boolean"
        },
        "isCrawlBlogComment": {
          "type": "boolean"
        },
        "isCrawlBlogAttachment": {
          "type": "boolean"
        },
        "maxFileSizeInMegaBytes":  {
          "type":"string"
        },
        "inclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionUrlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionUrlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "proxyHost": {
          "type": "string"
        },
        "proxyPort": {
          "type": "string"
        }
      },
      "required": []
    },
    "type": {
      "type": "string",
      "pattern": "CONFLUENCEV2"
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}
```

## Dropbox template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the Dropbox app key, app secret, and
access token as part of your secret that stores your authentication credentials. Also specify
the type of data source as `DROPBOX`, the type of access token you want to use
(temporary or permanent), and other necessary configurations. You then specify
`TEMPLATE` as the `Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Dropbox JSON schema](#dropbox-json "#dropbox-json").

The following table describes the parameters of the Dropbox JSON schema.

| Configuration                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                         | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata                                      | The endpoint information for the data source. This data source does not specify<br>an endpoint in `repositoryEndpointMetadata`. Rather, the connection<br>information is included in an AWS Secrets Manager secret that you provide the<br>`secretArn`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations                                        | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • file<br>• paper<br>• papert<br>• shortcut                     | A list of objects that map the attributes or field names of your Dropbox files,<br>Dropbox Paper, and shortcuts to Amazon Kendra index field names. For more<br>information, see [Mapping data source fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| syncMode                                                        | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| enableIdentityCrawler                                           | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| secretARN                                                       | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Dropbox. The secret must contain a<br>JSON structure with the following keys:<br>``<br>{<br>"appKey": "`Dropbox app key`",<br>"appSecret": "`Dropbox app secret`",<br>"accesstoken": "`temporary access token or refresh access token`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties                                            | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isCrawlAcl                                                      | `true` to crawl the access control list (ACL) information for your<br>documents, if you have an ACL and want to use it for access control. The ACL specifies<br>which documents that users and groups can access. The ACL information is<br>used to filter search results based on the user or their group access to documents.<br>For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").                                                                                                                                                                                                                                                                       |
| • inclusionFileNamePatterns<br>• inclusionFileTypePatterns      | A list of regular expression patterns to \*include<br>• certain<br>file names and types in your Dropbox data source. Files that match the patterns are<br>included in the index. Files that don't match the patterns are excluded from the<br>index. If a file matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                     |
| • exclusionFileNamePatterns<br>• exclusionFileTypePatterns      | A list of regular expression patterns to \*exclude<br>• certain<br>file names and types in your Dropbox data source. Files that match the patterns are<br>excluded from the index. Files that don't match the patterns are included in the<br>index. If a file matches both an exclusion and inclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                     |
| • crawlFile<br>• crawlPaper<br>• crawlPapert<br>• crawlShortcut | `true` to crawl files in your Dropbox, Dropbox Paper documents,<br>Dropbox Paper templates, and web page shortcuts stored in your Dropbox.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| type                                                            | The type of data source. Specify `DROPBOX` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| tokenType                                                       | Specify your access token type: permanent or temporary access token. It's<br>recommended that you create a refresh access token that never expires in Dropbox<br>rather that relying on a one-time access token that expires after 4 hours. You create<br>an app and a refresh access token in the Dropbox developer console and provide the<br>access token in your secret.                                                                                                                                                                                                                                                                                                                                                                                                            |
| version                                                         | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
          }
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "file": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "paper": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "papert": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "shortcut": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "secretArn": {
      "type": "string"
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "isCrawlAcl": {
          "type": "boolean"
        },
        "inclusionFileNamePatterns": {
          "type": "array"
        },
        "exclusionFileNamePatterns": {
          "type": "array"
        },
        "inclusionFileTypePatterns": {
          "type": "array"
        },
        "exclusionFileTypePatterns": {
          "type": "array"
        },
        "crawlFile": {
          "type": "boolean"
        },
        "crawlPaper": {
          "type": "boolean"
        },
        "crawlPapert": {
          "type": "boolean"
        },
        "crawlShortcut": {
          "type": "boolean"
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "DROPBOX"
    },
    "tokenType": {
      "type": "string",
      "enum": [
        "PERMANENT",
        "TEMPORARY"
      ]
    },
    "version": {
      "type": "string",
      "anyOf": [
        {
          "pattern": "1.0.0"
        }
      ]
    }
  },
  "additionalProperties": false,
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "syncMode",
    "enableIdentityCrawler",
    "secretArn",
    "type",
    "tokenType"
  ]
}
```

## Drupal template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") object. You provide the Drupal host URL and the
authentication type as part of the connection configuration or repository endpoint details.
Also specify the type of data source as DRUPAL, a secret for your authentication credentials,
and other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Drupal JSON schema](#drupal-json "#drupal-json").

The following table describes the parameters of the Drupal JSON schema.

| Configuration                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                              | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata                                                                                                                                                                                           | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| hostUrl                                                                                                                                                                                                              | The host url of your Drupal website. For example,<br>`https://<hostname>/<drupalsitename>`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| repositoryConfigurations                                                                                                                                                                                             | Configuration information for the content of the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| • content<br>• comment<br>• attachment                                                                                                                                                                               | A list of objects that map the attributes or field names of your Drupal files.<br>For more information, see [Mapping data source fields](field-mapping.md "field-mapping.md"). The<br>Drupal data source field names must exist in your Drupal custom metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| additionalProperties                                                                                                                                                                                                 | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| • inclusionFileNamePatterns<br>• articleTitleInclusionPatterns<br>• pageTitleInclusionPatterns<br>• customContentTitleInclusionPatterns<br>• basicBlockTitleInclusionPatterns<br>• customBlockTitleInclusionPatterns | A list of regular expression patterns to \*include<br>• certain<br>files in your Drupal data source. Files that match the patterns are included in the<br>index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                                     |
| • exclusionFileNamePatterns<br>• articleTitleExclusionPatterns<br>• pageTitleExclusionPatterns<br>• customContentTitleExclusionPatterns<br>• basicBlockTitleExclusionPatterns<br>• customBlockTitleExclusionPatterns | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Drupal data source. Files that match the patterns are excluded from the<br>index. Files that don't match the patterns are included in the index. If a file<br>matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                                     |
| contentDefinitions<br>• contentType<br>• fieldDefinition<br>• isCrawlComments<br>• isCrawlFiles<br>• isCrawlArticle<br>• isCrawlBasicPage<br>• isCrawlBasicBlock<br>• isCrawlCustomContentTypesList                  | Specify the content types to crawl and whether to crawl comments and attachments<br>for your selected content types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| type                                                                                                                                                                                                                 | The type of data source. Specify `DRUPAL` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| authType                                                                                                                                                                                                             | The type of authentication that you use, whether `BASIC-AUTH` or<br>`OAUTH2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| syncMode                                                                                                                                                                                                             | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| enableIdentityCrawler                                                                                                                                                                                                | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| secretARN                                                                                                                                                                                                            | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Drupal. The secret must contain a JSON<br>structure with the following keys: **If using basic<br>authentication:**<br>``<br>{<br>"username": `"user name"`,<br>"passwords": `"password"`<br>}<br>``<br>**If using OAuth 2.0<br>authentication:**<br>``<br>{<br>"username": `"user name"`,<br>"password": `"password"`,<br>"clientId": `"client id"`,<br>"clientSecret": `"client secret"`<br>}<br>``                                                                                                                                                                                                                                                   |
| version                                                                                                                                                                                                              | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"type": "object",
	"properties": {
		"connectionConfiguration": {
			"type": "object",
			"properties": {
				"repositoryEndpointMetadata": {
					"type": "object",
					"properties": {
						"hostUrl": {
							"type": "string",
							"pattern": "https:.*"
						}
					},
					"required": [
						"hostUrl"
					]
				}
			},
			"required": [
				"repositoryEndpointMetadata"
			]
		},
		"repositoryConfigurations": {
			"type": "object",
			"properties": {
				"content": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"comment": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"attachment": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				}
			}
		},
		"additionalProperties": {
			"type": "object",
			"properties": {
				"isCrawlArticle": {
					"type": "boolean"
				},
				"isCrawlBasicPage": {
					"type": "boolean"
				},
				"isCrawlBasicBlock": {
					"type": "boolean"
				},
				"crawlCustomContentTypesList": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"crawlCustomBlockTypesList": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"filePath": {
					"anyOf": [
						{
							"type": "string",
							"pattern": "s3:.*"
						},
						{
							"type": "string",
							"pattern": ""
						}
					]
				},
				"inclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"articleTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"articleTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"pageTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"pageTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customContentTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customContentTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"basicBlockTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"basicBlockTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customBlockTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customBlockTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"contentDefinitions": {
					"type": "array",
					"items": {
						"properties": {
							"contentType": {
								"type": "string"
							},
							"fieldDefinition": {
								"type": "array",
								"items": [
									{
										"type": "object",
										"properties": {
											"machineName": {
												"type": "string"
											},
											"type": {
												"type": "string"
											}
										},
										"required": [
											"machineName",
											"type"
										]
									}
								]
							},
							"isCrawlComments": {
								"type": "boolean"
							},
							"isCrawlFiles": {
								"type": "boolean"
							}
						}
					},
					"required": [
						"contentType",
						"fieldDefinition",
						"isCrawlComments",
						"isCrawlFiles"
					]
				}
			},
			"required": []
		},
		"type": {
			"type": "string",
			"pattern": "DRUPAL"
		},
		"authType": {
			"type": "string",
			"enum": [
				"BASIC-AUTH",
				"OAUTH2"
			]
		},
		"syncMode": {
			"type": "string",
			"enum": [
				"FORCED_FULL_CRAWL",
				"FULL_CRAWL",
				"CHANGE_LOG"
			]
		},
		"enableIdentityCrawler": {
			"type": "boolean"
		},
		"secretArn": {
			"type": "string",
			"minLength": 20,
			"maxLength": 2048
		}
	},
	"version": {
		"type": "string",
		"anyOf": [
			{
				"pattern": "1.0.0"
			}
		]
	},
	"required": [
		"connectionConfiguration",
		"repositoryConfigurations",
		"syncMode",
		"additionalProperties",
		"secretArn",
		"type"
	]
}
```

## GitHub template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") object. You provide the GitHub host URL, the organization
name, and whether you use GitHub cloud or GitHub on-premises as part of the connection
configuration or repository endpoint details. Also specify the type of data source as
`GITHUB`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md").

You can use the template provided in this developer guide. See [GitHub JSON schema](#github-json "#github-json").

The following table describes the parameters of the GitHub JSON schema.

| Configuration                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                             | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata                                                                                                                          | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| type                                                                                                                                                | Specify the type as either `SAAS` or `ON_PREMISE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| hostUrl                                                                                                                                             | The GitHub host URL. For example, if you use GitHub SaaS/Enterprise Cloud:<br>*https://api.github.com*. Or, if you use GitHub<br>on-premises/Enterprise Server:<br>_https://on-prem-host-url/api/v3/_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| organizationName                                                                                                                                    | You can find your organization name when you log in to GitHub desktop and go to<br>\*_Your organizations_<br>• under your profile picture dropdown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| repositoryConfigurations                                                                                                                            | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • ghRepository<br>• ghCommit<br>• ghIssueDocument<br>• ghIssueComment<br>• ghIssueAttachment<br>• ghPRDocument<br>• ghPRComment<br>• ghPRAttachment | A list of objects that map the attributes or field names of your GitHub content<br>to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| additionalProperties                                                                                                                                | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isCrawlAcl                                                                                                                                          | `true` to crawl the access control list (ACL) information for your<br>documents, if you have an ACL and want to use it for access control. The ACL specifies<br>which documents that users and groups can access and search. The ACL information is<br>used to filter search results based on the user or their group access to documents.<br>For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").                                                                                                                                                                                                                                                            |
| fieldForUserId                                                                                                                                      | Specify the type of user ID that you want to use for ACL crawling. Specify either<br>`email` if you want to use the user email for the user ID, or<br>`username` if you want to use the user name<br>for the user ID. If you don't specify an option then `email` is used by<br>default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| repositoryFilter                                                                                                                                    | A list of names of the specific repositories and branch names you want to<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| crawlRepository                                                                                                                                     | `true` to crawl repositories.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| crawlRepositoryDocuments                                                                                                                            | `true` to crawl repository documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| crawlIssue                                                                                                                                          | `true` to crawl issues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| crawlIssueComment                                                                                                                                   | `true` to crawl issue comments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| crawlIssueCommentAttachment                                                                                                                         | `true` to crawl issue comment attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| crawlPullRequest                                                                                                                                    | `true` to crawl pull requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| crawlPullRequestComment                                                                                                                             | `true` to crawl pull request comments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| crawlPullRequestCommentAttachment                                                                                                                   | `true` to crawl pull request comment attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| • inclusionFolderNamePatterns<br>• inclusionFileTypePatterns<br>• inclusionFileNamePatterns                                                         | A list of regular expression patterns to include certain content in your GitHub<br>data source. Content that matches the patterns are included in the index. Content that<br>doesn't match the patterns are excluded from the index. If any content matches both an<br>inclusion and exclusion pattern, the exclusion pattern takes precedence, and the<br>content isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                         |
| • exclusionFolderNamePatterns<br>• exclusionFileTypePatterns<br>• exclusionFileNamePatterns                                                         | A list of regular expression patterns to exclude certain content in your GitHub<br>data source. Content that matches the patterns are excluded from the index. Content<br>that doesn't match the patterns are included in the index. If any content matches both<br>an inclusion and exclusion pattern, the exclusion pattern takes precedence, and the<br>content isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                         |
| type                                                                                                                                                | The type of data source. Specify `GITHUB` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| enableIdentityCrawler                                                                                                                               | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| syncMode                                                                                                                                            | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                                                                                                                                           | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your GitHub. The secret must contain a<br>JSON structure with the following keys:<br>``<br>{<br>"personalToken": "`token`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| version                                                                                                                                             | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

The following is the GitHub JSON schema:

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "connectionConfiguration": {
            "type": "object",
            "properties": {
                "repositoryEndpointMetadata": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "hostUrl": {
                            "type": "string",
                            "pattern": "https://.*"
                        },
                        "organizationName": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "hostUrl",
                        "organizationName"
                    ]
                }
            },
            "required": [
                "repositoryEndpointMetadata"
            ]
        },
        "repositoryConfigurations": {
            "type": "object",
            "properties": {
                "ghRepository": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                },
                "ghCommit": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                },
                "ghIssueDocument": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                },
                "ghIssueComment": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                },
                "ghIssueAttachment": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                },
                "ghPRDocument": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                },
                "ghPRComment": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                },
                "ghPRAttachment": {
                    "type": "object",
                    "properties": {
                        "fieldMappings": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "indexFieldName": {
                                            "type": "string"
                                        },
                                        "indexFieldType": {
                                            "type": "string",
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
                                            ]
                                        },
                                        "dataSourceFieldName": {
                                            "type": "string"
                                        },
                                        "dateFieldFormat": {
                                            "type": "string",
                                            "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                                        }
                                    },
                                    "required": [
                                        "indexFieldName",
                                        "indexFieldType",
                                        "dataSourceFieldName"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "fieldMappings"
                    ]
                }
            }
        },
        "additionalProperties": {
            "type": "object",
            "properties": {
                "isCrawlAcl": {
                    "type": "boolean"
                },
                "fieldForUserId": {
                    "type": "string"
                },
                "crawlRepository": {
                    "type": "boolean"
                },
                "crawlRepositoryDocuments": {
                    "type": "boolean"
                },
                "crawlIssue": {
                    "type": "boolean"
                },
                "crawlIssueComment": {
                    "type": "boolean"
                },
                "crawlIssueCommentAttachment": {
                    "type": "boolean"
                },
                "crawlPullRequest": {
                    "type": "boolean"
                },
                "crawlPullRequestComment": {
                    "type": "boolean"
                },
                "crawlPullRequestCommentAttachment": {
                    "type": "boolean"
                },
                "repositoryFilter": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "repositoryName": {
                                    "type": "string"
                                },
                                "branchNameList": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    ]
                },
                "inclusionFolderNamePatterns": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "inclusionFileTypePatterns": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "inclusionFileNamePatterns": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "exclusionFolderNamePatterns": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "exclusionFileTypePatterns": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "exclusionFileNamePatterns": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": []
        },
        "type": {
            "type": "string",
            "pattern": "GITHUB"
        },
        "syncMode": {
            "type": "string",
            "enum": [
                "FULL_CRAWL",
                "FORCED_FULL_CRAWL",
                "CHANGE_LOG"
            ]
        },
        "enableIdentityCrawler": {
            "type": "boolean"
        },
        "secretArn": {
            "type": "string",
            "minLength": 20,
            "maxLength": 2048
        }
    },
    "version": {
        "type": "string",
        "anyOf": [
            {
                "pattern": "1.0.0"
            }
        ]
    },
    "required": [
        "connectionConfiguration",
        "repositoryConfigurations",
        "syncMode",
        "additionalProperties",
        "enableIdentityCrawler"
    ]
}
```

## Gmail template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as
`GMAIL`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Gmail JSON schema](#gmail-json "#gmail-json").

The following table describes the parameters of the Gmail JSON schema.

| Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| connectionConfiguration                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| repositoryEndpointMetadata                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The endpoint information for the data source. This data source does not<br>specify an endpoint in `repositoryEndpointMetadata`. Rather, the<br>connection information is included in an AWS Secrets Manager secret that<br>you provide the `secretArn`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| repositoryConfigurations                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| • message<br>• attachments                                                                                                                                                                                                                                                                                                                                                                                                                                                               | A list of objects that map the attributes or field names of your Gmail messages<br>and attachments to Amazon Kendra index field names. For more information, see<br>[Mapping data<br>source fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| additionalProperties                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| • inclusionLabelNamePatterns<br>• exclusionLabelNamePatterns<br>• inclusionAttachmentTypePatterns<br>• exclusionAttachmentTypePatterns<br>• inclusionAttachmentNamePatterns<br>• exclusionAttachmentNamePatterns<br>• inclusionSubjectFilter<br>• exclusionSubjectFilter<br>• isSubjectAnd<br>• inclusionFromFilter<br>• exclusionFromFilter<br>• inclusionToFilter<br>• exclusionToFilter<br>• inclusionCcFilter<br>• exclusionCcFilter<br>• inclusionBccFilter<br>• exclusionBccFilter | A list of regular expression patterns to include or exclude messages with<br>specific subject names in your Gmail data source. Files that match the patterns are<br>included in the index. If a file matches both an inclusion and an exclusion pattern,<br>the exclusion pattern takes precedence, and the file isn't included in the<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| beforeDateFilter                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Specify messages and attachments to be included before a certain date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| afterDateFilter                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Specify messages and attachments to be included after a certain date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| isCrawlAttachment                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | A Boolean value to choose whether you want to crawl attachments. Messages are<br>automatically crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The type of data source. Specify `GMAIL` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| shouldCrawlDraftMessages                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | A Boolean value to choose whether you want to crawl draft messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| syncMode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>ImportantBecause there is no API to update permanently deleted Gmail messages, any<br>new, modified, or deleted content sync:<br>• Won't remove messages that were permanently deleted from Gmail from your<br>Amazon Kendra index<br>• Won't sync changes in Gmail email labels<br>To sync your Gmail data source label changes and permanently deleted email<br>messages to your Amazon Kendra index, you must run full crawls<br>periodically. |
| secretARN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains the key-value<br>pairs required to connect to your Gmail. The secret must contain a JSON structure with<br>the following keys:<br>``<br>{<br>"adminAccountEmailId": "`service account email`",<br>"clientEmailId": "`user account email`",<br>"privateKey": "`private key`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
      }
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "message": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "STRING_LIST", "DATE"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          }
        },
        "attachments": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          }
        }
      },
      "required": []
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "inclusionLabelNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionLabelNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionAttachmentTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionAttachmentTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionAttachmentNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionAttachmentNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionSubjectFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionSubjectFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isSubjectAnd": {
          "type": "boolean"
        },
        "inclusionFromFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFromFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionToFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionToFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionCcFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionCcFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionBccFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionBccFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "beforeDateFilter": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        },
        "afterDateFilter": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        },
        "isCrawlAttachment": {
          "type": "boolean"
        },
        "shouldCrawlDraftMessages": {
          "type": "boolean"
        }
      },
      "required": [
        "isCrawlAttachment",
        "shouldCrawlDraftMessages"
      ]
    },
    "type" : {
      "type" : "string",
      "pattern": "GMAIL"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string"
    },
    "version": {
      "type": "string",
      "anyOf": [
        {
          "pattern": "1.0.0"
        }
      ]
    }
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "syncMode",
    "secretArn",
    "type"
  ]
}
```

## Google Drive template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as
`GOOGLEDRIVE2`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Google Drive JSON schema](#googledrive-json "#googledrive-json").

The following table describes the parameters of the Google Drive JSON schema.

| Configuration                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                         | Configuration information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| repositoryEndpointMetadata                                                                                                                                      | The endpoint information for the data source. This data source does not specify<br>an endpoint. You choose your authentication type: `serviceAccount` and<br>`OAuth2`. The connection information is included in an AWS Secrets Manager secret that you provide the `secretArn`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| authType                                                                                                                                                        | Choose between `serviceAccount` and `OAuth2` based on your<br>use case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations                                                                                                                                        | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • file<br>• comment                                                                                                                                             | A list of objects that map the attributes or field names of your Google Drive to<br>Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| additionalProperties                                                                                                                                            | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| • maxFileSizeInMegaBytes                                                                                                                                        | Specify a file size limit in MBs that Amazon Kendra should crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| • iscrawlComment                                                                                                                                                | `true` to crawl comments in your Google Drive data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| • isCrawlMyDriveAndSharedWithMe                                                                                                                                 | `true` to crawl MyDrive and Shared With Me Drives in your Google Drive<br>data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| • isCrawlSharedDrives                                                                                                                                           | `true` to crawl Shared Drives in your Google Drive data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| isCrawlAcl                                                                                                                                                      | `true` to crawl the access control list (ACL) information for your<br>documents, if you have an ACL and want to use it for access control. The ACL specifies<br>which documents that users and groups can access and search. The ACL information is<br>used to filter search results based on the user or their group access to documents.<br>For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").                                                                                                                                                                                                                                                            |
| • excludeUserAccounts<br>• excludeSharedDrives<br>• excludeMimeTypes<br>• exclusionFileTypePatterns<br>• exclusionFileNamePatterns<br>• exclusionFilePathFilter | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Google Drive data source. Files that match the patterns are excluded<br>from the index. Files that don't match the patterns are included in the index. If a<br>file matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence, and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                              |
| • includeUserAccounts<br>• includeSharedDrives<br>• includeMimeTypes<br>• inclusionFileTypePatterns<br>• inclusionFileNamePatterns<br>• inclusionFilePathFilter | A list of regular expression patterns to \*include<br>• certain<br>files in your Google Drive data source. Files that match the patterns are included in<br>the index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                              |
| type                                                                                                                                                            | The type of data source. Specify `GOOOGLEDRIVEV2` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| enableIdentityCrawler                                                                                                                                           | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| syncMode                                                                                                                                                        | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretARN                                                                                                                                                       | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Google Drive. The secret must contain<br>a JSON structure with the following keys: If using Google<br>Service Account authentication:<br>``<br>{<br>"clientEmail": "`user account email`",<br>"adminAccountEmail": "`service account email`",<br>"privateKey": "`private key`"<br>}<br>``<br>If using OAuth 2.0 authentication:<br>``<br>{<br>"clientID": "`OAuth client ID`",<br>"clientSecret": "`client secret`",<br>"refreshToken": "`refresh token`"<br>}<br>``                                                                                                                                                                                   |
| version                                                                                                                                                         | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "authType": {
              "type": "string",
              "enum": [
                "serviceAccount",
                "OAuth2"
              ]
            }
          },
          "required": [
            "authType"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "file": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "STRING_LIST",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "comment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "STRING_LIST"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "maxFileSizeInMegaBytes": {
          "type": "string"
        },
        "isCrawlComment": {
          "type": "boolean"
        },
        "isCrawlMyDriveAndSharedWithMe": {
          "type": "boolean"
        },
        "isCrawlSharedDrives": {
          "type": "boolean"
        },
        "isCrawlAcl": {
          "type": "boolean"
        },
        "excludeUserAccounts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "excludeSharedDrives": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "excludeMimeTypes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeUserAccounts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeSharedDrives": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeMimeTypes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeTargetAudienceGroup": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFilePathFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFilePathFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "GOOGLEDRIVEV2"
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}
```

## IBM DB2 template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `db2`, a secret for your authentication credentials, and other
necessary configurations. You then specify `TEMPLATE` as the `Type` when
you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [IBM DB2 JSON schema](#ibm-db2-json "#ibm-db2-json").

The following table describes the parameters of the IBM DB2 JSON schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Microsoft Exchange template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the tenant ID as as a part of the
connection configuration or repository endpoint details. Also specify the type of data source
as `MSEXCHANGE`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Microsoft Exchange JSON schema](#msexchange-json "#msexchange-json").

The following table describes the parameters of the Microsoft Exchange JSON schema.

| Configuration                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata                                                 | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tenantId                                                                   | The Microsoft 365 tenant ID. You can find your tenant ID in the Properties of<br>your Azure Active Directory Portal or in your OAuth application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| repositoryConfigurations                                                   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • email<br>• attachment<br>• calendar<br>• contacts<br>• notes             | A list of objects that map the attributes or field names of your Microsoft<br>Exchange data source to Amazon Kendra index fields. For more information, see<br>[Mapping data<br>source fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| additionalProperties                                                       | Additional configuration options for content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| inclusionPatterns                                                          | A list of regular expression patterns to \*include<br>• certain<br>files in your Microsoft Exchange data source. Files that match the patterns are<br>included in the index. Files that don't match the patterns are excluded from the<br>index. If a file matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                         |
| exclusionPatterns                                                          | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Microsoft Exchange data source. Files that match the patterns are<br>excluded from the index. Files that don't match the patterns are included in the<br>index. If a file matches both an exclusion and inclusion pattern, the exclusion<br>pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                         |
| • inclusionUsersList<br>• inclusionUsersFileName<br>• inclusionDomainUsers | A list of regular expression patterns to \*include<br>• certain<br>users and user files in your Microsofot Exchange data source. Users that match the<br>patterns are included in the index. Users that don't match the patterns are excluded<br>from the index. If a user matches both an inclusion and exclusion pattern, the<br>exclusion pattern takes precedence and the user isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                         |
| • exclusionUsersList<br>• exclusionUsersFileName<br>• exclusionDomainUsers | A list of regular expression patterns to \*exclude<br>• certain<br>users and user files in your Microsoft Exchange data source. Users that match the<br>patterns are excluded from the index. Users that don't match the patterns are included<br>in the index. If a user matches both an exclusion and inclusion pattern, the exclusion<br>pattern takes precedence and the user isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                          |
| s3bucketName                                                               | The name of your S3 bucket if that you want to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| • crawlCalendar<br>• crawlNotes<br>• crawlContacts<br>• crawlFolderAcl     | `true` to crawl these types of content and access control information<br>your Microsoft Exchange data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| startCalendarDateTime                                                      | You can configure a specific start date-time for your calendar content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| endCalendarDateTime                                                        | You can configure a specific end date-time for calendar content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| subject                                                                    | You can configure a specific subject line for your mail content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| emailFrom                                                                  | You can configure a specific email for your 'From' or sender mail<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| emailTo                                                                    | You can configure a specific email for your 'To' or recipient mail<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| syncMode                                                                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| type                                                                       | The type of data source. Specify `MSEXCHANGE` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| secretARN                                                                  | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Microsoft Exchange. This includes your<br>client ID and your client secret that is generated when you create an OAuth<br>application in the Azure portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| version                                                                    | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "tenantId": {
              "type": "string",
              "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
              "minLength": 36,
              "maxLength": 36
            }
          },
          "required": ["tenantId"]
        }
      }
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "email": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "STRING_LIST", "DATE"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "attachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "DATE","LONG"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "calendar": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "STRING_LIST", "DATE"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "contacts": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "STRING_LIST", "DATE"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "notes": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "DATE"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": ["email"
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "inclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionUsersList": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        },
        "exclusionUsersList": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        },
        "s3bucketName": {
          "type": "string"
        },
        "inclusionUsersFileName": {
          "type": "string"
        },
        "exclusionUsersFileName": {
          "type": "string"
        },
        "inclusionDomainUsers": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionDomainUsers": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "crawlCalendar": {
          "type": "boolean"
        },
        "crawlNotes": {
          "type": "boolean"
        },
        "crawlContacts": {
          "type": "boolean"
        },
        "crawlFolderAcl": {
          "type": "boolean"
        },
        "startCalendarDateTime": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        },
        "endCalendarDateTime": {
          "anyOf": [
            {
            "type": "string",
            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        },
        "subject": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "emailFrom": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        },
        "emailTo": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        }
      },
      "required": [
      ]
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "type" : {
      "type" : "string",
      "pattern": "MSEXCHANGE"
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}

```

## Microsoft OneDrive template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the tenant ID as part of the connection
configuration or repository endpoint details. Also specify the type of data source as
`ONEDRIVEV2`, and a secret for your authentication credentials, and other
necessary configurations. You then specify `TEMPLATE` as the `Type` when
you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Microsoft OneDrive JSON schema](#onedrive-json "#onedrive-json").

The following table describes the parameters of the Microsoft OneDrive JSON schema.

| Configuration                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                                                                                                                                                                                                      | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata                                                                                                                                                                                                                                                                                                                                                                   | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tenantId                                                                                                                                                                                                                                                                                                                                                                                     | The Microsoft 365 tenant ID. You can find your tenant ID in the Properties of<br>your Azure Active Directory Portal or in your OAuth application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| repositoryConfigurations                                                                                                                                                                                                                                                                                                                                                                     | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| file                                                                                                                                                                                                                                                                                                                                                                                         | A list of objects that map the attributes or field names of your Microsoft<br>OneDrive files to Amazon Kendra index field names. For more information, see<br>[Mapping data<br>source fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties                                                                                                                                                                                                                                                                                                                                                                         | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| • userNameFilter<br>• userFilterPath<br>• inclusionFileTypePatterns<br>• exclusionFileTypePatterns<br>• inclusionFileNamePatterns<br>• exclusionFileNamePatterns<br>• inclusionFilePathPatterns<br>• exclusionFilePathPatterns<br>• inclusionOneNoteSectionNamePatterns<br>• exclusionOneNoteSectionNamePatterns<br>• inclusionOneNotePageNamePatterns<br>• exclusionOneNotepageNamePatterns | You can choose to index specific files, OneNote sections, OneNote pages, and<br>filter by user name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| isUserNameOnS3                                                                                                                                                                                                                                                                                                                                                                               | `true` to provide a list of user names in a file stored in an Amazon S3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| type                                                                                                                                                                                                                                                                                                                                                                                         | The type of data source. Specify `ONEDRIVEV2` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| enableIdentityCrawler                                                                                                                                                                                                                                                                                                                                                                        | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| type                                                                                                                                                                                                                                                                                                                                                                                         | The type of data source. Specify `ONEDRIVEV2` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| syncMode                                                                                                                                                                                                                                                                                                                                                                                     | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretARN                                                                                                                                                                                                                                                                                                                                                                                    | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Microsoft OneDrive. The secret must<br>contain a JSON structure with the following keys:<br>``<br>{<br>"clientId": "`client ID`",<br>"clientSecret": "`client secret`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| version                                                                                                                                                                                                                                                                                                                                                                                      | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"type": "object",
	"properties": {
		"connectionConfiguration": {
			"type": "object",
			"properties": {
				"repositoryEndpointMetadata": {
					"type": "object",
					"properties": {
						"tenantId": {
							"type": "string",
							"pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
							"minLength": 36,
							"maxLength": 36
						}
					},
					"required": [
						"tenantId"
					]
				}
			},
			"required": [
				"repositoryEndpointMetadata"
			]
		},
		"repositoryConfigurations": {
			"type": "object",
			"properties": {
				"file": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"STRING_LIST",
												"DATE",
												"LONG"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				}
			}
		},
		"additionalProperties": {
			"type": "object",
			"properties": {
				"userNameFilter": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"userFilterPath": {
					"type": "string"
				},
				"isUserNameOnS3": {
					"type": "boolean"
				},
				"inclusionFileTypePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFileTypePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionFilePathPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFilePathPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionOneNoteSectionNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionOneNoteSectionNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionOneNotePageNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionOneNotePageNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				}
			},
			"required": []
		},

		"enableIdentityCrawler": {
			"type": "boolean"
		},
		"type": {
			"type": "string",
			"pattern": "ONEDRIVEV2"
		},
		"syncMode": {
			"type": "string",
			"enum": [
				"FULL_CRAWL",
				"FORCED_FULL_CRAWL",
				"CHANGE_LOG"
			]
		},
		"secretArn": {
			"type": "string",
			"minLength": 20,
			"maxLength": 2048
		}
	},
	"version": {
		"type": "string",
		"anyOf": [
			{
				"pattern": "1.0.0"
			}
		]
	},
	"required": [
		"connectionConfiguration",
		"repositoryConfigurations",
		"syncMode",
		"additionalProperties",
		"secretArn",
		"type"
	]
}
```

## Microsoft SharePoint template schema

You include a JSON that contains the data source schema as part of [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the SharePoint site URL/URLs, domain, and
also a tenant ID if required as a part of the connection configuration or repository endpoint
details. Also specify the type of data source as `SHAREPOINTV2`, a secret for your
authentication credentials, and other necessary configurations. You then specify
`TEMPLATE` as the **Type** when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [SharePoint JSON schema](#sharepoint-json "#sharepoint-json").

The following table describes the parameters of the Microsoft SharePoint JSON
schema.

| Configuration                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                                                                                                                                                                                                                             | Configuration information for the endpoint for the data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| repositoryEndpointMetadata                                                                                                                                                                                                                                                                                                                                                                                          | The endpoint information for the data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| tenantId                                                                                                                                                                                                                                                                                                                                                                                                            | The tenant id of your SharePoint account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| domain                                                                                                                                                                                                                                                                                                                                                                                                              | The domain of your SharePoint account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| siteUrls                                                                                                                                                                                                                                                                                                                                                                                                            | The host URLs of your SharePoint account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| repositoryAdditionalProperties                                                                                                                                                                                                                                                                                                                                                                                      | Additional properties to connect with the repository/data source<br>endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| s3bucketName                                                                                                                                                                                                                                                                                                                                                                                                        | The name of the Amazon S3 bucket that stores your Azure AD self-signed<br>X.509 certificate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| s3certificateName                                                                                                                                                                                                                                                                                                                                                                                                   | The name of the Azure AD self-signed X.509 certificate stored in your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| authType                                                                                                                                                                                                                                                                                                                                                                                                            | The type of authentication that you use, whether `OAuth2`,<br>`OAuth2Certificate`, `OAuth2App`, `Basic`,<br>`OAuth2_RefreshToken`, `NTLM`, or<br>`Kerberos`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| version                                                                                                                                                                                                                                                                                                                                                                                                             | The SharePoint version that you use, whether `Server` or<br>`Online`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| onPremVersion                                                                                                                                                                                                                                                                                                                                                                                                       | The SharePoint Server version that you use, whether `2013`,<br>`2016`<br>`2019`, or `SubscriptionEdition`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| repositoryConfigurations                                                                                                                                                                                                                                                                                                                                                                                            | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • event<br>• page<br>• file<br>• link<br>• attachment<br>• comment                                                                                                                                                                                                                                                                                                                                                  | A list of objects that map the attributes or field names of your SharePoint<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| additionalProperties                                                                                                                                                                                                                                                                                                                                                                                                | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| • eventTitleFilterRegEx<br>• pageTitleFilterRegEx<br>• linkTitleFilterRegEx<br>• inclusionFilePath<br>• exclusionFilePath<br>• inclusionFileTypePatterns<br>• exclusionFileTypePatterns<br>• inclusionFileNamePatterns<br>• exclusionFileNamePatterns<br>• inclusionOneNoteSectionNamePatterns<br>• exclusionOneNoteSectionNamePatterns<br>• inclusionOneNotePageNamePatterns<br>• exclusionOneNotePageNamePatterns | A list of regular expression patterns to include/exclude certain content in your<br>SharePoint data source. Content itmes that match the inclusion patterns are included<br>in the index. Content items that don't match the inclusion patterns are excluded from<br>the index. If a file matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence, and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                         |
| • crawlFiles<br>• crawlPages<br>• crawlEvents<br>• crawlComments<br>• crawlLinks<br>• crawlAttachments                                                                                                                                                                                                                                                                                                              | `true` to crawl these types of content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| crawlAcl                                                                                                                                                                                                                                                                                                                                                                                                            | `true` to crawl the access control list (ACL) information for your<br>documents, if you have an ACL and want to use it for access control. The ACL specifies<br>which documents that users and groups can access and search. The ACL information is<br>used to filter search results based on the user or their group access to documents.<br>For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").                                                                                                                                                                                                                                                            |
| fieldForUserId                                                                                                                                                                                                                                                                                                                                                                                                      | Specify either `email` if you want to use the user email for the user<br>ID, or `userPrincipalName` if you want to use a user name for the user ID.<br>If you don't specify an option then `email` is used by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| aclConfiguration                                                                                                                                                                                                                                                                                                                                                                                                    | Specify either `ACLWithLDAPEmailFmt`,<br>`ACLWithManualEmailFmt`, or `ACLWithUsernameFmtM`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| emailDomain                                                                                                                                                                                                                                                                                                                                                                                                         | The domain of the email. For example,<br>"`amazon.com`".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| • isCrawlLocalGroupMapping<br>• isCrawlAdGroupMapping                                                                                                                                                                                                                                                                                                                                                               | `true` to crawl group mapping information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| proxyHost                                                                                                                                                                                                                                                                                                                                                                                                           | The host name of the web proxy that you use, without the http:// or https://<br>protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| proxyPort                                                                                                                                                                                                                                                                                                                                                                                                           | The port number used by the host URL transport protocol. Must be a numeric value<br>between 0 and 65535.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| type                                                                                                                                                                                                                                                                                                                                                                                                                | Specify `SHAREPOINTV2` as your data source type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| enableIdentityCrawler                                                                                                                                                                                                                                                                                                                                                                                               | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| syncMode                                                                                                                                                                                                                                                                                                                                                                                                            | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretARN                                                                                                                                                                                                                                                                                                                                                                                                           | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your SharePoint. For information on these<br>key-value pairs, see [Connection instructions for SharePoint Online and SharePoint<br>Server](data-source-v2-sharepoint.md#data-source-procedure-v2-sharepoint "data-source-v2-sharepoint.md#data-source-procedure-v2-sharepoint").                                                                                                                                                                                                                                                                                                                                                                            |
| version                                                                                                                                                                                                                                                                                                                                                                                                             | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"type": "object",
	"properties": {
		"connectionConfiguration": {
			"type": "object",
			"properties": {
				"repositoryEndpointMetadata": {
					"type": "object",
					"properties": {
						"tenantId": {
							"type": "string",
							"pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
							"minLength": 36,
							"maxLength": 36
						},
						"domain": {
							"type": "string"
						},
						"siteUrls": {
							"type": "array",
							"items": {
								"type": "string",
								"pattern": "https://.*"
							}
						},
						"repositoryAdditionalProperties": {
							"type": "object",
							"properties": {
								"s3bucketName": {
									"type": "string"
								},
								"s3certificateName": {
									"type": "string"
								},
								"authType": {
									"type": "string",
									"enum": [
										"OAuth2",
										"OAuth2Certificate",
										"OAuth2App",
										"Basic",
										"OAuth2_RefreshToken",
										"NTLM",
										"Kerberos"
									]
								},
								"version": {
									"type": "string",
									"enum": [
										"Server",
										"Online"
									]
								},
								"onPremVersion": {
									"type": "string",
									"enum": [
										"",
										"2013",
										"2016",
										"2019",
										"SubscriptionEdition"
									]
								}
							},
							"required": [
								"authType",
								"version"
							]
						}
					},
					"required": [
						"siteUrls",
						"domain",
						"repositoryAdditionalProperties"
					]
				}
			},
			"required": [
				"repositoryEndpointMetadata"
			]
		},
		"repositoryConfigurations": {
			"type": "object",
			"properties": {
				"event": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"STRING_LIST",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"page": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE",
												"LONG"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"file": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE",
												"LONG"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"link": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"STRING_LIST",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"attachment": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"STRING_LIST",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"comment": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"STRING_LIST",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				}
			}
		},
		"additionalProperties": {
			"type": "object",
			"properties": {
				"eventTitleFilterRegEx": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"pageTitleFilterRegEx": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"linkTitleFilterRegEx": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionFilePath": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFilePath": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionFileTypePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFileTypePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionOneNoteSectionNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionOneNoteSectionNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"inclusionOneNotePageNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionOneNotePageNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"crawlFiles": {
					"type": "boolean"
				},
				"crawlPages": {
					"type": "boolean"
				},
				"crawlEvents": {
					"type": "boolean"
				},
				"crawlComments": {
					"type": "boolean"
				},
				"crawlLinks": {
					"type": "boolean"
				},
				"crawlAttachments": {
					"type": "boolean"
				},
				"crawlListData": {
					"type": "boolean"
				},
				"crawlAcl": {
					"type": "boolean"
				},
				"fieldForUserId": {
					"type": "string"
				},
				"aclConfiguration": {
					"type": "string",
					"enum": [
						"ACLWithLDAPEmailFmt",
						"ACLWithManualEmailFmt",
						"ACLWithUsernameFmt"
					]
				},
				"emailDomain": {
					"type": "string"
				},
				"isCrawlLocalGroupMapping": {
					"type": "boolean"
				},
				"isCrawlAdGroupMapping": {
					"type": "boolean"
				},
				"proxyHost": {
					"type": "string"
				},
				"proxyPort": {
					"type": "string"
				}
			},
			"required": [
			]
		},
		"type": {
			"type": "string",
			"pattern": "SHAREPOINTV2"
		},
		"enableIdentityCrawler": {
			"type": "boolean"
		},
		"syncMode": {
			"type": "string",
			"enum": [
				"FULL_CRAWL",
				"FORCED_FULL_CRAWL",
				"CHANGE_LOG"
			]
		},
		"secretArn": {
			"type": "string",
			"minLength": 20,
			"maxLength": 2048
		}
	},
	"version": {
		"type": "string",
		"anyOf": [
			{
				"pattern": "1.0.0"
			}
		]
	},
	"required": [
		"connectionConfiguration",
		"repositoryConfigurations",
		"enableIdentityCrawler",
		"syncMode",
		"additionalProperties",
		"secretArn",
		"type"
	]
}
```

## Microsoft SQL Server template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `sqlserver`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Microsoft SQL Server JSON schema](#ms-sql-server-json "#ms-sql-server-json").

The following table describes the parameters of the Micorosft SQL Server JSON
schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Microsoft Teams template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the tenant ID as a part of the connection
configuration or repository endpoint details. Also specify the type of data source as
`MSTEAMS`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Microsoft Teams JSON schema](#msteams-json "#msteams-json").

The following table describes the parameters of the Microsoft Teams JSON schema.

| Configuration                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                                              | Configuration information for endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| repositoryEndpointMetadata                                                                                                                                                                                                           | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tenantId                                                                                                                                                                                                                             | The Microsoft 365 tenant ID. You can find your tenant ID in the Properties of<br>your Azure Active Directory Portal or in your OAuth application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| repositoryConfigurations                                                                                                                                                                                                             | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • chatMessage<br>• chatAttachment<br>• channelPost<br>• channelWiki<br>• channelAttachment<br>• meetingChat<br>• meetingFile<br>• meetingNote<br>• calendarMeeting                                                                   | A list of objects that map the attributes or field names of your Microsoft Teams<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| additionalProperties                                                                                                                                                                                                                 | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| paymentModel                                                                                                                                                                                                                         | Specifies what type of payment model to use with your Microsoft Teams data<br>source. Model A payment models are restricted to licensing and payment models that<br>require security compliance. Model B payment models are suitable for licensing and<br>payment models that do not require security compliance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| • inclusionTeamNameFilter<br>• inclusionChannelNameFilter<br>• inclusionFileNamePatterns<br>• inclusionFileTypePatterns<br>• inclusionUserEmailFilter<br>• inclusionOneNoteSectionNamePatterns<br>• inclusionOneNotePageNamePatterns | A list of regular expression patterns to \*include<br>• certain<br>content in your Microsoft Teams data source. Content that matches the patterns are<br>included in the index. Content that doesn't match the patterns are excluded from the<br>index. If content matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence, and the content isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                             |
| • exclusionTeamNameFilter<br>• exclusionChannelNameFilter<br>• exclusionFileNamePatterns<br>• exclusionFileTypePatterns<br>• exclusionUserEmailFilter<br>• exclusionOneNoteSectionNamePatterns<br>• exclusionOneNotePageNamePatterns | A list of regular expression patterns to \*exclude<br>• certain<br>content in your Microsoft Teams data source. Content that matches the patterns are<br>excluded from the index. Content that doesn't match the patterns are included in the<br>index. If content matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence, and the content isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                             |
| • isCrawlChatMessage<br>• isCrawlChatAttachment<br>• isCrawlChannelPost<br>• isCrawlChannelAttachment<br>• isCrawlChannelWiki<br>• isCrawlCalendarMeeting<br>• isCrawlMeetingChat<br>• isCrawlMeetingFile<br>• isCrawlMeetingNote    | `true` to crawl these types of content in your Microsoft Teams data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| startCalendarDateTime                                                                                                                                                                                                                | You can configure a specific start date-time for your calendar content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| endCalendarDateTime                                                                                                                                                                                                                  | You can configure a specific end date-time for calendar content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| type                                                                                                                                                                                                                                 | The type of data source. Specify `MSTEAMS` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| enableIdentityCrawler                                                                                                                                                                                                                | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| syncMode                                                                                                                                                                                                                             | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                                                                                                                                                                                                                            | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Microsoft Teams. This includes your<br>client ID and client secret that is generated when you create an OAuth application in<br>the Azure portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| version                                                                                                                                                                                                                              | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "tenantId": {
              "type": "string",
              "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
              "minLength": 36,
              "maxLength": 36
            }
          },
          "required": [
            "tenantId"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "chatMessage": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "chatAttachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "channelPost": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "channelWiki": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "channelAttachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "meetingChat": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "meetingFile": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "meetingNote": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "calendarMeeting": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
     "additionalProperties": {
      "type": "object",
      "properties": {
        "paymentModel": {
          "type": "string",
          "enum": [
            "A",
            "B",
            "Evaluation Mode"
          ]
        },
        "inclusionTeamNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionTeamNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionChannelNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionChannelNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionUserEmailFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionOneNoteSectionNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionOneNoteSectionNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionOneNotePageNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionOneNotePageNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isCrawlChatMessage": {
          "type": "boolean"
        },
        "isCrawlChatAttachment": {
          "type": "boolean"
        },
        "isCrawlChannelPost": {
          "type": "boolean"
        },
        "isCrawlChannelAttachment": {
          "type": "boolean"
        },
        "isCrawlChannelWiki": {
          "type": "boolean"
        },
        "isCrawlCalendarMeeting": {
          "type": "boolean"
        },
        "isCrawlMeetingChat": {
          "type": "boolean"
        },
        "isCrawlMeetingFile": {
          "type": "boolean"
        },
        "isCrawlMeetingNote": {
          "type": "boolean"
        },
        "startCalendarDateTime": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        },
        "endCalendarDateTime": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        }
      },
      "required": []
    },
    "type": {
      "type": "string",
      "pattern": "MSTEAMS"
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}
```

## Microsoft Yammer template schema

You include a JSON that contains the data source schema as part of [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as
`YAMMER`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the **Type** when
you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide.

The following table describes the parameters of the Microsoft Yammer JSON schema.

| Configuration                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                            | Configuration information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| repositoryEndpointMetadata                                         | The endpoint information for the data source. This data source does not specify<br>an endpoint in `repositoryEndpointMetadata`. Rather, the connection<br>information is included in an AWS Secrets Manager secret that you provide the<br>`secretArn`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations                                           | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| • community<br>• user<br>• message<br>• attachment                 | A list of objects that map attributes or field names of Microsoft Yammer content<br>to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| additionalProperties                                               | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| inclusionPatterns                                                  | A list of regular expression patterns to \*include<br>• certain<br>files in your Microsoft Yammer data source. Files that match the patterns are included<br>in the index. File that don't match the patterns are excluded from the index. If a<br>file matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                            |
| exclusionPatterns                                                  | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Microsoft Yammer data source. Files that match the patterns are excluded<br>from the index. Files that don't match the patterns are included in the index. If a<br>file matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                           |
| sinceDate                                                          | You can choose to configure a `sinceDate` parameter so that the<br>Microsoft Yammer connector crawls content based on a specific<br>`sinceDate`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| communityNameFilter                                                | You can choose to index specific community content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| • isCrawlMessage<br>• isCrawlAttachment<br>• isCrawlPrivateMessage | `true` to crawl messages, message attachments, and private<br>messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| type                                                               | Specify `YAMMER` as your data source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| secretARN                                                          | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Microsoft Yammer. This includes your<br>Microsoft Yammer user name and password, and client ID and client secret that is<br>generated when you create an OAuth application in the Azure portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| useChangeLog                                                       | `true` to use the Microsoft Yammer change log to determine which<br>documents require updating in the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| syncMode                                                           | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| enableIdentityCrawler                                              | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
          }
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "community": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "user": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "message": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "attachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE"
                        ]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "inclusionPatterns": {
          "type": "array"
        },
        "exclusionPatterns": {
          "type": "array"
        },
        "sinceDate": {
          "type": "string",
          "pattern": "^(19|2[0-9])[0-9]{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])((\\+|-)(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]))?$"
        },
        "communityNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isCrawlMessage": {
          "type": "boolean"
        },
        "isCrawlAttachment": {
          "type": "boolean"
        },
        "isCrawlPrivateMessage": {
          "type": "boolean"
        }
      },
      "required": [
        "sinceDate"
      ]
    },
    "type": {
      "type": "string",
      "pattern": "YAMMER"
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "useChangeLog": {
      "type": "string",
      "enum": [
        "true",
        "false"
      ]
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "version": {
      "type": "string",
      "anyOf": [
        {
          "pattern": "1.0.0"
        }
      ]
    }
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "type",
    "secretArn",
    "syncMode"
  ]
}
```

## MySQL template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `mysql`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [MySQL JSON schema](#mysql-json "#mysql-json").

The following table describes the parameters of the MySQL JSON schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Oracle Database template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `oracle`, a secret for your authentication credentials, and
other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Oracle Database JSON schema](#oracle-database-json "#oracle-database-json").

The following table describes the parameters of the Oracle Database JSON schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## PostgreSQL template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. Specify the type of data source as `JDBC`,
the database type as `postgresql`, a secret for your authentication credentials,
and other necessary configurations. You then specify `TEMPLATE` as the
`Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [PostgreSQL JSON schema](#postgresql-json "#postgresql-json").

The following table describes the parameters of the PostgreSQL JSON schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database that you use, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| document                   | A list of objects that map the attributes or field names of your database<br>content to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| primaryKey                 | Provide the primary key for the database table. This identifies a table within<br>your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| titleColumn                | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bodyColumn                 | Provide the name of the document title column within your database table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Kendra uses<br>time stamp information to detect changes in your content and sync only changed<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changeDetectingColumns     | Enter the names of the columns that Amazon Kendra will use to detect content<br>changes. Amazon Kendra will re-index content when there is a change in any of<br>these columns                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| isSslEnabled               | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 32KB. Amazon Kendra will crawl all database content that matches your<br>query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user name and<br>password required to connect to your database. The secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"user name": "`database user name`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string"
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "isSslEnabled": {
          "type": "boolean"
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

## Salesforce template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the Salesforce host URL as a part of the
connection configuration or repository endpoint details. Also specify the type of data source
as `SALESFORCEV2`, a secret for your authentication credentials, and other
necessary configurations. You then specify `TEMPLATE` as the `Type` when
you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Salesforce JSON schema](#salesforce-json "#salesforce-json").

The following table describes the parameters of the Salesforce JSON schema.

| Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| connectionConfiguration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| repositoryEndpointMetadata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| hostUrl                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The URL of the Salesforce instance to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| repositoryConfigurations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| • account<br>• contact<br>• campaign<br>• case<br>• product<br>• lead<br>• contract<br>• partner<br>• profile<br>• idea<br>• pricebook<br>• task<br>• solution<br>• attachment<br>• user<br>• document<br>• knowledgeArticles<br>• group<br>• opportunity<br>• chatter<br>• customEntity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | A list of objects that map the attributes or field names of your Salesforce<br>entities to Amazon Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| secretARN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Salesforce. The secret must contain a<br>JSON structure with the following keys:<br>``<br>{<br>"authenticationUrl": "`OAUTH endpoint that Amazon Kendra connects to get an OAUTH token`",<br>"consumerKey": "`Application public key generated when you created your Salesforce application`",<br>"consumerSecret": "`Application private key generated when you created your Salesforce application`",<br>"password": "`Password associated with the user logging in to the Salesforce instance`",<br>"securityToken": "`Token associated with the user account logging in to the Salesforce instance`",<br>"username": "`User name of the user logging in to the Salesforce instance`"<br>}<br>`` |
| additionalProperties                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| • accountFilter<br>• contactFilter<br>• caseFilter<br>• campaignFilter<br>• contractFilter<br>• groupFilter<br>• leadFilter<br>• productFilter<br>• opportunityFilter<br>• partnerFilter<br>• pricebookFilter<br>• ideaFilter<br>• profileFilter<br>• taskFilter<br>• solutionFilter<br>• userFilter<br>• chatterFilter<br>• documentFilter<br>• knowledgeArticleFilter<br>• customEntities                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | A collection of strings that specifies which entities to filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| inclusionPatterns<br>• inclusionDocumentFileTypePatterns<br>• inclusionDocumentFileNamePatterns<br>• inclusionAccountFileTypePatterns<br>• inclusionCampaignFileTypePatterns<br>• inclusionDocumentFileNamePatterns<br>• inclusionCampaignFileNamePatterns<br>• inclusionCaseFileTypePatterns<br>• inclusionCaseFileNamePatterns<br>• inclusionContactFileTypePatterns<br>• inclusionContractFileNamePatterns<br>• inclusionLeadFileTypePatterns<br>• inclusionLeadFileNamePatterns<br>• inclusionOpportunityFileTypePatterns<br>• inclusionOpportunityFileNamePatterns<br>• inclusionSolutionFileTypePatterns<br>• inclusionSolutionFileNamePatterns<br>• inclusionTaskFileTypePatterns<br>• inclusionTaskFileNamePatterns<br>• inclusionGroupFileTypePatterns<br>• inclusionGroupFileNamePatterns<br>• inclusionChatterFileTypePatterns<br>• inclusionChatterFileNamePatterns<br>• inclusionCustomEntityFileTypePatterns<br>• inclusionCustomEntityFileNamePatterns | A list of regular expression patterns to \*include<br>• certain<br>files in your Salesforce data source. Files that match the patterns are included in<br>the index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| exclusionPatterns<br>• exclusionDocumentFileTypePatterns<br>• exclusionDocumentFileNamePatterns<br>• exclusionAccountFileTypePatterns<br>• exclusionCampaignFileTypePatterns<br>• exclusionCampaignFileNamePatterns<br>• exclusionCaseFileTypePatterns<br>• exclusionCaseFileNamePatterns<br>• exclusionContactFileTypePatterns<br>• exclusionContractFileNamePatterns<br>• exclusionLeadFileTypePatterns<br>• exclusionLeadFileNamePatterns<br>• exclusionOpportunityFileTypePatterns<br>• exclusionOpportunityFileNamePatterns<br>• exclusionSolutionFileTypePatterns<br>• exclusionSolutionFileNamePatterns<br>• exclusionTaskFileTypePatterns<br>• exclusionTaskFileNamePatterns<br>• exclusionGroupFileTypePatterns<br>• exclusionGroupFileNamePatterns<br>• exclusionChatterFileTypePatterns<br>• exclusionChatterFileNamePatterns<br>• exclusionCustomEntityFileTypePatterns<br>• exclusionCustomEntityFileNamePatterns                                        | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Salesforce data source. Files that match the patterns are excluded from<br>the index. Files that don't match the patterns are included in the index. If a file<br>matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| • isCrawlAccount<br>• isCrawlContact<br>• isCrawlCase<br>• isCrawlCampaign<br>• isCrawlProduct<br>• isCrawlLead<br>• isCrawlContract<br>• isCrawlPartner<br>• isCrawlProfile<br>• isCrawlIdea<br>• isCrawlPricebook<br>• isCrawlDocument<br>• crawlSharedDocument<br>• isCrawlGroup<br>• isCrawlOpportunity<br>• isCrawlChatter<br>• isCrawlUser<br>• isCrawlSolution<br>• isCrawlTask<br>• isCrawlAccountAttachments<br>• isCrawlContactAttachments<br>• isCrawlCaseAttachments<br>• isCrawlCampaignAttachments<br>• isCrawlLeadAttachments<br>• isCrawlContractAttachments<br>• isCrawlGroupAttachments<br>• isCrawlOpportunityAttachments<br>• isCrawlChatterAttachments<br>• isCrawlSolutionAttachments<br>• isCrawlTaskAttachments<br>• isCrawlCustomEntityAttachments<br>• isCrawlKnowledgeArticles<br>+ isCrawlDraft<br>+ isCrawlPublish<br>+ isCrawlArchived                                                                                                  | `true` to crawl these types of files in your Salesforce<br>account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The type of data source. Specify `SALESFORCEV2` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| enableIdentityCrawler                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                                                                         |
| syncMode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.                                              |
| version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties":
  {
    "connectionConfiguration": {
      "type": "object",
      "properties":
      {
        "repositoryEndpointMetadata":
        {
          "type": "object",
          "properties":
          {
            "hostUrl":
            {
              "type": "string",
              "pattern": "https:.*"
            }
          },
          "required":
          [
            "hostUrl"
          ]
        }
      },
      "required":
      [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties":
      {
        "account":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "contact":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "campaign":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "case":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "product":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "lead":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "contract":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "partner":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "profile":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "idea":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "pricebook":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "task":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "solution":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "attachment":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "user":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "document":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "knowledgeArticles":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "group":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "opportunity":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE",
                        "LONG"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "chatter":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        },
        "customEntity":
        {
          "type": "object",
          "properties":
          {
            "fieldMappings":
            {
              "type": "array",
              "items":
              [
                {
                  "type": "object",
                  "properties":
                  {
                    "indexFieldName":
                    {
                      "type": "string"
                    },
                    "indexFieldType":
                    {
                      "type": "string",
                      "enum":
                      [
                        "STRING",
                        "STRING_LIST",
                        "DATE"
                      ]
                    },
                    "dataSourceFieldName":
                    {
                      "type": "string"
                    },
                    "dateFieldFormat":
                    {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required":
                  [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required":
          [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties":
      {
        "accountFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "contactFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "caseFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "campaignFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "contractFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "groupFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "leadFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "productFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "opportunityFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "partnerFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "pricebookFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "ideaFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "profileFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "taskFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "solutionFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "userFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "chatterFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "documentFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "knowledgeArticleFilter":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "customEntities":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "isCrawlAccount": {
          "type": "boolean"
        },
        "isCrawlContact": {
          "type": "boolean"
        },
        "isCrawlCase": {
          "type": "boolean"
        },
        "isCrawlCampaign": {
          "type": "boolean"
        },
        "isCrawlProduct": {
          "type": "boolean"
        },
        "isCrawlLead": {
          "type": "boolean"
        },
        "isCrawlContract": {
          "type": "boolean"
        },
        "isCrawlPartner": {
          "type": "boolean"
        },
        "isCrawlProfile": {
          "type": "boolean"
        },
        "isCrawlIdea": {
          "type": "boolean"
        },
        "isCrawlPricebook": {
          "type": "boolean"
        },
        "isCrawlDocument": {
          "type": "boolean"
        },
        "crawlSharedDocument": {
          "type": "boolean"
        },
        "isCrawlGroup": {
          "type": "boolean"
        },
        "isCrawlOpportunity": {
          "type": "boolean"
        },
        "isCrawlChatter": {
          "type": "boolean"
        },
        "isCrawlUser": {
          "type": "boolean"
        },
        "isCrawlSolution":{
          "type": "boolean"
        },
        "isCrawlTask":{
          "type": "boolean"
        },

        "isCrawlAccountAttachments": {
          "type": "boolean"
        },
        "isCrawlContactAttachments": {
          "type": "boolean"
        },
        "isCrawlCaseAttachments": {
          "type": "boolean"
        },
        "isCrawlCampaignAttachments": {
          "type": "boolean"
        },
        "isCrawlLeadAttachments": {
          "type": "boolean"
        },
        "isCrawlContractAttachments": {
          "type": "boolean"
        },
        "isCrawlGroupAttachments": {
          "type": "boolean"
        },
        "isCrawlOpportunityAttachments": {
          "type": "boolean"
        },
        "isCrawlChatterAttachments": {
          "type": "boolean"
        },
        "isCrawlSolutionAttachments":{
          "type": "boolean"
        },
        "isCrawlTaskAttachments":{
          "type": "boolean"
        },
        "isCrawlCustomEntityAttachments":{
          "type": "boolean"
        },
        "isCrawlKnowledgeArticles": {
          "type": "object",
          "properties":
          {
            "isCrawlDraft": {
              "type": "boolean"
            },
            "isCrawlPublish": {
              "type": "boolean"
            },
            "isCrawlArchived": {
              "type": "boolean"
            }
          }
        },
        "inclusionDocumentFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionDocumentFileTypePatterns": {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionDocumentFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionDocumentFileNamePatterns": {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionAccountFileTypePatterns": {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionAccountFileTypePatterns": {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionAccountFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionAccountFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionCampaignFileTypePatterns": {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionCampaignFileTypePatterns": {
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionCampaignFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionCampaignFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionCaseFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionCaseFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionCaseFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionCaseFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionContactFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionContactFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionContactFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionContactFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionContractFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionContractFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionContractFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionContractFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionLeadFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionLeadFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionLeadFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionLeadFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionOpportunityFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionOpportunityFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionOpportunityFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionOpportunityFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionSolutionFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionSolutionFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionSolutionFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionSolutionFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionTaskFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionTaskFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionTaskFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionTaskFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionGroupFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionGroupFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionGroupFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionGroupFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionChatterFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionChatterFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionChatterFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionChatterFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionCustomEntityFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionCustomEntityFileTypePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "inclusionCustomEntityFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        },
        "exclusionCustomEntityFileNamePatterns":{
          "type": "array",
          "items":
          {
            "type": "string"
          }
        }
      },
      "required":
      []
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "type": {
      "type": "string",
      "pattern": "SALESFORCEV2"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}
```

## ServiceNow template schema

You include a JSON that contains the data source schema as part of the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the ServiceNow host URL, authentication
type, and instance version as a part of the connection configuration or repository endpoint
details. Also specify the type of data source as `SERVICENOWV2`, a secret for your
authentication credentials, and other necessary configurations. You then specify
`TEMPLATE` as the `Type` when you call [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [ServiceNow JSON schema](#servicenow-json "#servicenow-json").

The following table describes the parameters of the ServiceNow JSON schema.

| Configuration                                                                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                                                                                                                                                                                                                                                  | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| repositoryEndpointMetadata                                                                                                                                                                                                                                                                                                                                                                                                               | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| hostUrl                                                                                                                                                                                                                                                                                                                                                                                                                                  | The ServiceNow host URL. For example,<br>`your-domain.service-now.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| authType                                                                                                                                                                                                                                                                                                                                                                                                                                 | The type of authentication that you use, whether `basicAuth` or<br>`OAuth2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| servicenowInstanceVersion                                                                                                                                                                                                                                                                                                                                                                                                                | The ServiceNow version that you use. You can choose between `Tokyo`,<br>`Sandiego`, `Rome`, and `Others`.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| repositoryConfigurations                                                                                                                                                                                                                                                                                                                                                                                                                 | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| • knowledgeArticle<br>• attachment<br>• serviceCatalog<br>• incident                                                                                                                                                                                                                                                                                                                                                                     | A list of objects that map the attributes or field names of your ServiceNow<br>knowledge articles, attachments, service catalog, and incidents to Amazon Kendra<br>index field names. For more information, see [Mapping data source fields](field-mapping.md "field-mapping.md"). The<br>ServiceNow data source field names must exist in your ServiceNow custom<br>metadata.                                                                                                                                                                                   |
| additional properties                                                                                                                                                                                                                                                                                                                                                                                                                    | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| maxFileSizeInMegaBytes                                                                                                                                                                                                                                                                                                                                                                                                                   | Specify the file size limit in MBs that Amazon Kendra will crawl. Amazon Kendra will crawl only<br>the files within the size limit you define. The default file size is 50MB. The maximum<br>file size should be greater than 0MB and less than or equal to 50MB.                                                                                                                                                                                                                                                                                                |
| • knowledgeArticleFilter<br>• incidentQueryFilter<br>• serviceCatalogQueryFilter<br>• knowledgeArticleTitleRegExp<br>• serviceCatalogTitleRegExp<br>• incidentTitleRegExp<br>• inclusionFileTypePatterns<br>• exclusionFileTypePatterns<br>• inclusionFileNamePatterns<br>• exclusionFileNamePatterns<br>• incidentStateType                                                                                                             | A list of regular expression patterns to include and/or exclude certain files in<br>your ServiceNow data source. Files that match the patterns are included in the index.<br>Files that don't match the patterns are excluded from the index. If a file matches<br>both an inclusion and exclusion pattern, the exclusion pattern takes precedence and<br>the file isn't included in the index.                                                                                                                                                                  |
| • isCrawlKnowledgeArticle<br>• isCrawlKnowledgeArticleAttachment<br>• includePublicArticlesOnly<br>• isCrawlServiceCatalog<br>• isCrawlServiceCatalogAttachment<br>• isCrawlActiveServiceCatalog<br>• isCrawlInactiveServiceCatalog<br>• isCrawlIncident<br>• isCrawlIncidentAttachment<br>• isCrawlActiveIncident<br>• isCrawlInactiveIncident<br>• applyACLForKnowledgeArticle<br>• applyACLForServiceCatalog<br>• applyACLForIncident | `true` to crawl ServiceNow knowledge articles, service catalogs,<br>incidents, and attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| type                                                                                                                                                                                                                                                                                                                                                                                                                                     | The type of data source. Specify `SERVICENOWV2` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| enableIdentityCrawler                                                                                                                                                                                                                                                                                                                                                                                                                    | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                     |
| syncMode                                                                                                                                                                                                                                                                                                                                                                                                                                 | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.                                  |
| secretARN                                                                                                                                                                                                                                                                                                                                                                                                                                | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your ServiceNow. The secret must contain a<br>JSON structure with the following keys:<br>``<br>{<br>"username": "`user name`",<br>"password": "`password`"<br>}<br>``<br>If you use OAuth2 authentication, your secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"username": "`user name`",<br>"password": "`password`",<br>"clientId": "`client id`",<br>"clientSecret": "`client secret`"<br>}<br>`` |
| version                                                                                                                                                                                                                                                                                                                                                                                                                                  | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "hostUrl": {
              "type": "string",
              "pattern": "^(?!(^(https?|ftp|file):\/\/))[a-z0-9-]+(.service-now.com|.servicenowservices.com)$",
              "minLength": 1,
              "maxLength": 2048
            },
            "authType": {
              "type": "string",
              "enum": [
                "basicAuth",
                "OAuth2"
              ]
            },
            "servicenowInstanceVersion": {
              "type": "string",
              "enum": [
                "Tokyo",
                "Sandiego",
                "Rome",
                "Others"
                ]
            }
          },
          "required": [
            "hostUrl",
            "authType",
            "servicenowInstanceVersion"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "knowledgeArticle": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "STRING_LIST"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "attachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "LONG",
                        "DATE",
                        "STRING_LIST"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "serviceCatalog": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "STRING_LIST"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "incident": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": [
                        "STRING",
                        "DATE",
                        "STRING_LIST"
                      ]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "maxFileSizeInMegaBytes": {
          "type": "string"
        },
        "isCrawlKnowledgeArticle": {
          "type": "boolean"
        },
        "isCrawlKnowledgeArticleAttachment": {
          "type": "boolean"
        },
        "includePublicArticlesOnly": {
          "type": "boolean"
        },
        "knowledgeArticleFilter": {
          "type": "string"
        },
        "incidentQueryFilter": {
          "type": "string"
        },
        "serviceCatalogQueryFilter": {
          "type": "string"
        },
        "isCrawlServiceCatalog": {
          "type": "boolean"
        },
        "isCrawlServiceCatalogAttachment": {
          "type": "boolean"
        },
        "isCrawlActiveServiceCatalog": {
          "type": "boolean"
        },
        "isCrawlInactiveServiceCatalog": {
          "type": "boolean"
        },
        "isCrawlIncident": {
          "type": "boolean"
        },
        "isCrawlIncidentAttachment": {
          "type": "boolean"
        },
        "isCrawlActiveIncident": {
          "type": "boolean"
        },
        "isCrawlInactiveIncident": {
          "type": "boolean"
        },
        "applyACLForKnowledgeArticle": {
          "type": "boolean"
        },
        "applyACLForServiceCatalog": {
          "type": "boolean"
        },
        "applyACLForIncident": {
          "type": "boolean"
        },
        "incidentStateType": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "Open",
              "Open - Unassigned",
              "Resolved",
              "All"
            ]
          }
        },
        "knowledgeArticleTitleRegExp": {
          "type": "string"
        },
        "serviceCatalogTitleRegExp": {
          "type": "string"
        },
        "incidentTitleRegExp": {
          "type": "string"
        },
        "inclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": []
    },
    "type": {
      "type": "string",
      "pattern": "SERVICENOWV2"
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}

```

## Slack template schema

You include a JSON that contains the data source schema as part of [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the host URL as a part of the connection
configuration or repository endpoint details. Also specify the type of data source as
`SLACK`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Slack JSON schema](#slack-json "#slack-json").

The following table describes the parameters of the Slack JSON schema.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| repositoryEndpointMetadata | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| teamId                     | The Slack team ID you copied from your Slack main page URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| All                        | A list of objects that map the attributes or field names of your<br>Slack content to Amazon Kendra index field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| additionalProperties       | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| inclusionPatterns          | A list of regular expression patterns to include specific content in your<br>Slack data source. Content that matches the patterns are included in<br>the index. Content that doesn't match the patterns are excluded from the index. If any<br>content matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the content isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                         |
| exclusionPatterns          | A list of regular expression patterns to exclude specific content in your<br>Slack data source. Content that matches the patterns are excluded<br>from the index. Content that doen't match the patterns are included in the index. If<br>any content matches both an inclusion and exclusion pattern, the exclusion pattern<br>takes precedence, and the content isn't included in the index.                                                                                                                                                                                                                                                                                                                                                                                          |
| crawlBotMessages           | `true` to crawl bot messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| excludeArchived            | `true` to exclude crawling of archived messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| conversationType           | The type of conversation that you want to index whether<br>`PUBLIC_CHANNEL`, `PRIVATE_CHANNEL`,<br>`GROUP_MESSAGE` and `DIRECT_MESSAGE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| channelFilter              | The type of channel that you want to index whether `private_channel`<br>or `public_channel`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| sinceDate                  | You can choose to configure a `sinceDate` parameter so that the<br>Slack connector crawls content based on a specific<br>`sinceDate`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| lookBack                   | You can choose to configure a `lookBack` parameter so that the<br>Slack connector crawls updated or deleted content upto a specified<br>number of hours before your last connector sync.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| syncMode                   | Specify how Amazon Kendra should update your index when your<br>data source content changes. You can choose between:<br>• `FORCED_FULL_CRAWL` to freshly index all content,<br>replacing existing content each time your data source syncs with<br>your index.<br>• `FULL_CRAWL` to index only new, modified and deleted<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync.<br>• `CHANGE_LOG` to index only new and modified<br>content each time your data source syncs with your index. Amazon Kendra<br>can use your data source's mechanism for tracking content changes and<br>index content that changed since the last sync. |
| type                       | The type of data source. Specify `SLACK` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| enableIdentityCrawler      | `true` to use Amazon Kendra's identity crawler to sync<br>identity/principal information on users and groups with access to certain documents.<br>If identity crawler is turned off, all documents can be publicly searched. If you<br>want to use access control for your documents and identity crawler is turned off,<br>you can alternatively use the [PutPrincipalMapping](API_PutPrincipalMapping.md "API_PutPrincipalMapping.md") API to upload user and group access<br>information.                                                                                                                                                                                                                                                                                            |
| secretArn                  | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Slack. The secret<br>must contain a JSON structure with the following keys:<br>``<br>{<br>"slackToken": "`token`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| version                    | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "teamId": {
              "type": "string"
            }
          },
          "required": ["teamId"]
        }
      }
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "All": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "STRING_LIST", "DATE","LONG"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "exclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "crawlBotMessages": {
          "type": "boolean"
        },
        "excludeArchived": {
          "type": "boolean"
        },
        "conversationType": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PUBLIC_CHANNEL",
              "PRIVATE_CHANNEL",
              "GROUP_MESSAGE",
              "DIRECT_MESSAGE"
            ]
          }
        },
        "channelFilter": {
            "type": "object",
            "properties": {
              "private_channel": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "public_channel": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
          }
        },
        "channelIdFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "sinceDate": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        },
        "lookBack": {
          "type": "string",
          "pattern": "^[0-9]*$"
        }
      },
      "required": [
      ]
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "type" : {
      "type" : "string",
      "pattern": "SLACK"
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "secretArn": {
      "type": "string"
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type",
    "enableIdentityCrawler"
  ]
}
```

## Zendesk template schema

You include a JSON that contains the data source schema as part of [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object. You provide the host URL as a part of the connection
configuration or repository endpoint details. Also specify the type of data source as
`ZENDESK`, a secret for your authentication credentials, and other necessary
configurations. You then specify `TEMPLATE` as the `Type` when you call
[CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md").

You can use the template provided in this developer guide. See [Zendesk JSON schema](#zendesk-json "#zendesk-json").

The following table describes the parameters of the Zendesk JSON schema.

| Configuration                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                                                          | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                       |
| repositoryEndpointMetadata                                                                                                                                                                                                                       | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                         |
| hostURL                                                                                                                                                                                                                                          | The Zendesk host URL. For example,<br>*https://yoursubdomain.zendesk.com*.                                                                                                                                                                                                                                                                                                            |
| repositoryConfigurations                                                                                                                                                                                                                         | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                               |
| • ticket<br>• ticketComment<br>• ticketCommentAttachment<br>• article<br>• articleComment<br>• articleAttachment<br>• communityTopic<br>• communityPostComment                                                                                   | A list of objects that map attributes or field names of Zendesk tickets to Amazon<br>Kendra index field names. For more information, see [Mapping data source<br>fields](field-mapping.md "field-mapping.md").                                                                                                                                                                        |
| secretARN                                                                                                                                                                                                                                        | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Zendesk. The secret must contain a<br>JSON structure with the following keys: host URL, client ID, client secret, user name,<br>and password.                                                                                                        |
| additionalProperties                                                                                                                                                                                                                             | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                 |
| organizationNameFilter                                                                                                                                                                                                                           | You can choose to index tickets that exist within a specific<br>**Organization**.                                                                                                                                                                                                                                                                                                     |
| sinceDate                                                                                                                                                                                                                                        | You can choose to configure a `sinceDate` parameter so that the<br>Zendesk connector crawls content based on a specific `sinceDate`.                                                                                                                                                                                                                                                  |
| inclusionPatterns                                                                                                                                                                                                                                | A list of regular expression patterns to \*include<br>• certain<br>files in your Zendesk data source. Files that match the patterns are included in the<br>index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the file isn't included in the index. |
| exclusionPatterns                                                                                                                                                                                                                                | A list of regular expression patterns to \*exclude<br>• certain<br>files in your Zendesk data source. Files that match the patterns are excluded from the<br>index. Files that don't match the patterns are included in the index. If a file<br>matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence, and the file isn't included in the index. |
| • isCrawlTicket<br>• isCrawlTicketComment<br>• isCrawlTicketCommentAttachment<br>• isCrawlArticle<br>• isCrawlArticleComment<br>• isCrawlArticleAttachment<br>• isCrawlCommunityTopic<br>• isCrawlCommunityPost<br>• isCrawlCommunityPostComment | Input "`true`" to crawl these types of content.                                                                                                                                                                                                                                                                                                                                       |
| type                                                                                                                                                                                                                                             | Specify `ZENDESK` as your data source type.                                                                                                                                                                                                                                                                                                                                           |
| useChangeLog                                                                                                                                                                                                                                     | Input "`true`" to use the Zendesk change log to determine which<br>documents require updating in the index. Depending on the change log's size, it might<br>be faster to scan the documents in Zendesk. If you are syncing your Zendesk data<br>source with your index for the first time, all documents are scanned.                                                                 |

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "hostUrl": {
              "type": "string",
              "pattern": "https:.*"
            }
          },
          "required": [
            "hostUrl"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "ticket": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"

                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "ticketComment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"

                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "ticketCommentAttachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "article": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "communityPostComment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "articleComment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "articleAttachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "communityTopic": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
                      }
                    },
                    "required": [
                      "indexFieldName",
                      "indexFieldType",
                      "dataSourceFieldName"
                    ]
                  }
                ]
              }
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "organizationNameFilter": {
          "type": "array"
        },
        "sinceDate": {
          "type": "string",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$"
        },
        "inclusionPatterns": {
          "type": "array"
        },
        "exclusionPatterns": {
          "type": "array"
        },
        "isCrawTicket": {
          "type": "string"
        },
        "isCrawTicketComment": {
          "type": "string"
        },
        "isCrawTicketCommentAttachment": {
          "type": "string"
        },
        "isCrawlArticle": {
          "type": "string"
        },
        "isCrawlArticleAttachment": {
          "type": "string"
        },
        "isCrawlArticleComment": {
          "type": "string"
        },
        "isCrawlCommunityTopic": {
          "type": "string"
        },
        "isCrawlCommunityPost": {
          "type": "string"
        },
        "isCrawlCommunityPostComment": {
          "type": "string"
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "ZENDESK"
    },
    "useChangeLog": {
      "type": "string",
      "enum": ["true", "false"]
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "additionalProperties": false,
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "useChangeLog",
    "secretArn",
    "type"
  ]
}
```
