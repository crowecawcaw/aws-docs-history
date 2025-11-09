# Reading from Facebook Page Insights entities

**Prerequisite**

A Facebook Page Insights object you would like to read from. You will need the object name.

**Supported entities for source**:

| Entity                 | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ---------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Page Content           | Yes             | No             | Yes               | Yes                | Yes                   |
| Page CTA Clicks        | Yes             | No             | No                | Yes                | Yes                   |
| Page Engagement        | Yes             | No             | No                | Yes                | Yes                   |
| Page Impressions       | Yes             | No             | No                | Yes                | Yes                   |
| Page Posts             | Yes             | No             | No                | Yes                | Yes                   |
| Page Post Engagement   | No              | No             | No                | Yes                | No                    |
| Page Post Reactions    | No              | No             | No                | Yes                | No                    |
| Page Reactions         | Yes             | No             | No                | Yes                | Yes                   |
| Stories                | Yes             | No             | No                | Yes                | Yes                   |
| Page User Demographics | Yes             | No             | No                | Yes                | Yes                   |
| Page Video Views       | Yes             | No             | No                | Yes                | Yes                   |
| Page Views             | Yes             | No             | No                | Yes                | Yes                   |
| Page Video Posts       | Yes             | No             | No                | Yes                | Yes                   |
| Pages                  | No              | Yes            | No                | Yes                | No                    |
| Feeds                  | Yes             | Yes            | No                | Yes                | Yes                   |

**Example**:

```
facebookPageInsights_read = glueContext.create_dynamic_frame. from options(
    connection_type="facebookpageinsights",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v21"
   }
```

**Facebook Page Insights field details**:

| Entity                                     | Field    | Data type | Supported operators |
| ------------------------------------------ | -------- | --------- | ------------------- |
| Page Content                               | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page CTA Clicks                            | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Engagement                            | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Impressions                           | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Posts                                 | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Post Engagement                       | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Post Reactions                        | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page User Demographics                     | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Video Views                           | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Views                                 | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Page Video Posts                           | Name     | String    | N/A                 |
| Period                                     | Period   | EQUAL_TO  |
| Since                                      | DateTime | EQUAL_TO  |
| Values                                     | List     | N/A       |
| Title                                      | String   | N/A       |
| Description                                | String   | N/A       |
| description_from_api_doc                   | String   | N/A       |
| Id                                         | String   | N/A       |
| Pages                                      | Name     | String    | N/A                 |
| About                                      | String   | N/A       |
| access_token                               | String   | N/A       |
| ad_campaign                                | String   | N/A       |
| Affiliation                                | String   | N/A       |
| app_id                                     | String   | N/A       |
| artists_we_like                            | String   | N/A       |
| Attire                                     | String   | N/A       |
| Awards                                     | String   | N/A       |
| band_interests                             | String   | N/A       |
| band_members                               | String   | N/A       |
| best_page                                  | String   | N/A       |
| Bio                                        | String   | N/A       |
| Birthday                                   | String   | N/A       |
| booking_agent                              | String   | N/A       |
| Built                                      | String   | N/A       |
| can_checkin                                | String   | N/A       |
| can_post                                   | String   | N/A       |
| Category                                   | String   | N/A       |
| category_list                              | List     | N/A       |
| Checkins                                   | Integer  | N/A       |
| company_overview                           | String   | N/A       |
| connected_instagram_account                | String   | N/A       |
| contact_address                            | String   | N/A       |
| country_page_likes                         | Integer  | N/A       |
| Cover                                      | Struct   | N/A       |
| culinary_team                              | String   | N/A       |
| current_location                           | String   | N/A       |
| delivery_and_pickup_option_info            | List     | N/A       |
| Description                                | String   | N/A       |
| description_html                           | String   | N/A       |
| differently_open_offerings                 | List     | N/A       |
| directed_by                                | String   | N/A       |
| display_subtext                            | String   | N/A       |
| displayed_message_response_time            | String   | N/A       |
| Emails                                     | String   | N/A       |
| Engagement                                 | String   | N/A       |
| fan_count                                  | Integer  | N/A       |
| featured_video                             | String   | N/A       |
| Features                                   | String   | N/A       |
| followers_count                            | Integer  | N/A       |
| food_styles                                | List     | N/A       |
| Founded                                    | String   | N/A       |
| general_info                               | String   | N/A       |
| general_manager                            | String   | N/A       |
| Genre                                      | String   | N/A       |
| global_brand_page_name                     | String   | N/A       |
| global_brand_root_id                       | String   | N/A       |
| has_added_app                              | Boolean  | N/A       |
| has_transitioned_to_new_page_experience    | Boolean  | N/A       |
| has_whatsapp_business_number               | Boolean  | N/A       |
| has_whatsapp_number                        | Boolean  | N/A       |
| Hometown                                   | String   | N/A       |
| Hours                                      | Struct   | N/A       |
| Impressum                                  | String   | N/A       |
| Influences                                 | String   | N/A       |
| instagram_business_account                 | String   | N/A       |
| is_always_open                             | Boolean  | N/A       |
| is_chain                                   | Boolean  | N/A       |
| is_community_page                          | Boolean  | N/A       |
| is_eligible_for_branded_content            | Boolean  | N/A       |
| is_messenger_bot_get_started_enabled       | Boolean  | N/A       |
| is_messenger_platform_bot                  | Boolean  | N/A       |
| is_owned                                   | Boolean  | N/A       |
| is_permanently_closed                      | Boolean  | N/A       |
| is_published                               | Boolean  | N/A       |
| Name                                       | String   | N/A       |
| Tasks                                      | List     | N/A       |
| is_unclaimed                               | Boolean  | N/A       |
| is_webhooks_subscribed                     | Boolean  | N/A       |
| leadgen_tos_acceptance_time                | DateTime | N/A       |
| leadgen_tos_accepted                       | Boolean  | N/A       |
| leadgen_tos_accepting_user                 | String   | N/A       |
| leadgen_tos_accepting_user                 | Struct   | N/A       |
| Link                                       | Link     | N/A       |
| Location                                   | Struct   | N/A       |
| Members                                    | String   | N/A       |
| merchant_review_status                     | String   | N/A       |
| messenger_ads_default_icebreakers          | List     | N/A       |
| messenger_ads_default_page_welcome_message | Struct   | N/A       |
| messenger_ads_default_quick_replies        | List     | N/A       |
| messenger_ads_quick_replies_type           | String   | N/A       |
| Mission                                    | String   | N/A       |
| Mpg                                        | String   | N/A       |
| name_with_location_descriptor              | String   | N/A       |
| Network                                    | String   | N/A       |
| new_like_count                             | Integer  | N/A       |
| offer_eligible                             | Boolean  | N/A       |
| overall_star_rating                        | Float    | N/A       |
| page_token                                 | String   | N/A       |
| parent_page                                | String   | N/A       |
| Parking                                    | String   | N/A       |
| payment_options                            | Struct   | N/A       |
| personal_info                              | String   | N/A       |
| personal_interests                         | String   | N/A       |
| pharma_safety_info                         | String   | N/A       |
| Phone                                      | String   | N/A       |
| pickup_options                             | List     | N/A       |
| place_type                                 | String   | N/A       |
| plot_outline                               | String   | N/A       |
| press_contact                              | String   | N/A       |
| price_range                                | String   | N/A       |
| privacy_info_url                           | String   | N/A       |
| produced_by                                | String   | N/A       |
| Products                                   | String   | N/A       |
| promotion_eligible                         | Boolean  | N/A       |
| promotion_ineligible_reason                | String   | N/A       |
| public_transit                             | String   | N/A       |
| rating_count                               | Integer  | N/A       |
| record_label                               | String   | N/A       |
| release_date                               | String   | N/A       |
| restaurant_services                        | Struct   | N/A       |
| restaurant_specialties                     | Struct   | N/A       |
| Schedule                                   | String   | N/A       |
| screenplay_by                              | String   | N/A       |
| Season                                     | String   | N/A       |
| single_line_address                        | String   | N/A       |
| Starring                                   | String   | N/A       |
| start_info                                 | Struct   | N/A       |
| store_code                                 | String   | N/A       |
| store_location_descriptor                  | String   | N/A       |
| store_number                               | Integer  | N/A       |
| Studio                                     | String   | N/A       |
| supports_donate_button_in_live_video       | Boolean  | N/A       |
| talking_about_count                        | Integer  | N/A       |
| temporary_status                           | String   | N/A       |
| unread_message_count                       | Integer  | N/A       |
| unread_notif_count                         | Integer  | N/A       |
| unseen_message_count                       | Integer  | N/A       |
| Username                                   | String   | N/A       |
| verification_status                        | String   | N/A       |
| voip_info                                  | Struct   | N/A       |
| Website                                    | String   | N/A       |
| were_here_count                            | Integer  | N/A       |
| whatsapp_number                            | String   | N/A       |
| written_by                                 | String   | N/A       |
| Feeds                                      | Id       | String    | N/A                 |
| Actions                                    | List     | N/A       |
| admin_creator                              | Object   | N/A       |
| Application                                | Object   | N/A       |
| Attachments                                | Objects  | N/A       |
| backdated_time                             | DateTime | N/A       |
| call_to_action                             | Object   | N/A       |
| can_reply_privately                        | Boolean  | N/A       |
| child_attachments                          | List     | N/A       |
| Coordinates                                | Struct   | N/A       |
| created_time                               | DateTime | N/A       |
| Event                                      | Struct   | N/A       |
| expanded_height                            | Integer  | N/A       |
| expanded_width                             | Integer  | N/A       |
| feed_targeting                             | Object   | N/A       |
| From                                       | Object   | N/A       |
| full_picture                               | String   | N/A       |
| Height                                     | Integer  | N/A       |
| Icon                                       | String   | N/A       |
| instagram_eligibility                      | String   | N/A       |
| is_eligible_for_promotion                  | Boolean  | N/A       |
| is_expired                                 | Boolean  | N/A       |
| is_hidden                                  | Boolean  | N/A       |
| is_inline_created                          | Boolean  | N/A       |
| is_instagram_eligible                      | Boolean  | N/A       |
| is_popular                                 | Boolean  | N/A       |
| is_published                               | Boolean  | N/A       |
| is_spherical                               | Boolean  | N/A       |
| Message                                    | String   | N/A       |
| message_tags                               | List     | N/A       |
| multi_share_end_card                       | Boolean  | N/A       |
| multi_share_optimized                      | Boolean  | N/A       |
| parent_id                                  | String   | N/A       |
| permalink_url                              | String   | N/A       |
| Place                                      | String   | N/A       |
| Privacy                                    | Object   | N/A       |
| promotable_id                              | String   | N/A       |
| promotion_status                           | String   | N/A       |
| Properties                                 | List     | N/A       |
| scheduled_publish_time                     | Float    | N/A       |
| Shares                                     | Object   | N/A       |
| status_type                                | String   | N/A       |
| Story                                      | String   | N/A       |
| story_tags                                 | List     | N/A       |
| Subscribed                                 | Boolean  | N/A       |
| Target                                     | Struct   | N/A       |
| Targeting                                  | Object   | N/A       |
| To                                         | Object   | N/A       |
| timeline_visibility                        | String   | N/A       |
| updated_time                               | DateTime | N/A       |
| Via                                        | Struct   | N/A       |
| video_buying_eligibility                   | List     | N/A       |
| Width                                      | Integer  | N/A       |
| Since                                      | DateTime | EQUAL_TO  |

## Partitioning queries

**Filter-based partitioning**:

You can provide the additional Spark options `PARTITION_FIELD`,
`LOWER_BOUND`, `UPPER_BOUND`, and
`NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the Datetime field, we accept the Spark timestamp format used in Spark SQL queries.

Examples of valid value:

```
"2024-09-30T01:01:01.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

Example:

```
facebookPageInsights_read = glueContext.create_dynamic_frame.from_options(
     connection_type="facebookpageinsights",
     connection_options={
         "connectionName": "connectionName",
         "ENTITY_NAME": "entityName",
         "API_VERSION": "v21",
         "PARTITION_FIELD": "created_Time"
         "LOWER_BOUND": "2024-10-27T07:00:00+0000"
         "UPPER_BOUND": "2024-10-27T07:00:00+0000"
         "NUM_PARTITIONS": "10"
     }
```
