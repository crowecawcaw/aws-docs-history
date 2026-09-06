

# Reading from Stripe entities
<a name="stripe-reading-from-entities"></a>

 **Prerequisites** 
+  A Stripe object you would like to read from. 

 **Supported entities** 


| Entity | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Balance | No | No | No | Yes | No | 
| Balance Transactions | Yes | Yes | No | Yes | Yes | 
| Charges | Yes | Yes | No | Yes | Yes | 
| Disputes | Yes | Yes | No | Yes | Yes | 
| File Links | Yes | Yes | No | Yes | Yes | 
| PaymentIntents | Yes | Yes | No | Yes | Yes | 
| SetupIntents | Yes | Yes | No | Yes | Yes | 
| Payouts | Yes | Yes | No | Yes | Yes | 
| Refunds | Yes | Yes | No | Yes | Yes | 
| Products | Yes | Yes | No | Yes | Yes | 
| Prices | Yes | Yes | No | Yes | Yes | 
| Coupons | Yes | Yes | No | Yes | Yes | 
| Promotion Codes | Yes | Yes | No | Yes | Yes | 
| Tax Codes | No | Yes | No | Yes | No | 
| Tax Rates | Yes | Yes | No | Yes | Yes | 
| Shipping Rates | Yes | Yes | No | Yes | Yes | 
| Sessions | Yes | Yes | No | Yes | Yes | 
| Credit Notes | Yes | Yes | No | Yes | Yes | 
| Customer | Yes | Yes | No | Yes | Yes | 
| Invoices | Yes | Yes | No | Yes | Yes | 
| Invoice Items | Yes | Yes | No | Yes | No | 
| Plans | Yes | Yes | No | Yes | Yes | 
| Quotes | Yes | Yes | No | Yes | No | 
| Subscriptions | Yes | Yes | No | Yes |  | 
| Subscription Items | No | Yes | No | Yes | No | 
| Subscription Schedules | Yes | Yes | No | Yes | Yes | 
| Accounts | No | Yes | No | Yes | Yes | 
| Application Fees | Yes | Yes | No | Yes | Yes | 
| Country Specs | No | Yes | No | Yes | No | 
| Transfers | Yes | Yes | No | Yes | Yes | 
| Early Fraud Warnings | Yes | Yes | No | Yes | Yes | 
| Report Types | No | No | No | Yes | No | 

 **Example** 

```
stripe_read = glueContext.create_dynamic_frame.from_options(
    connection_type="stripe",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "coupons",
        "API_VERSION": "v1"
    }
)
```

 **Stripe entity and field details** 


| Entity | Field | Data Type | Supported Operators | 
| --- | --- | --- | --- | 
| Balance |  |  |  | 
|  | available | List |  | 
|  | connect\_reserved | List |  | 
|  | pending | List |  | 
|  | livemode | Boolean |  | 
|  | object | String |  | 
|  | instant\_available | List |  | 
|  | issuing | Struct |  | 
| Balance Transactions |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer |  | 
|  | available\_on | DateTime | =, >=, <=,<,> | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String |  | 
|  | description | String |  | 
|  | exchange\_rate | BigDecimal |  | 
|  | fee | Integer |  | 
|  | fee\_details | List |  | 
|  | net | Integer |  | 
|  | reporting\_category | String |  | 
|  | source | String | = | 
|  | status | String |  | 
|  | type | String | = | 
|  | cross\_border\_classification | String |  | 
| Charges |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer | =, <, > | 
|  | amount\_captured | Integer |  | 
|  | amount\_refunded | Integer |  | 
|  | application | String |  | 
|  | application\_fee | String |  | 
|  | application\_fee\_amount | Integer |  | 
|  | balance\_transaction | String |  | 
|  | billing\_details | Struct |  | 
|  | calculated\_statement\_descriptor | String |  | 
|  | captured | Boolean |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String |  | 
|  | customer | String | = | 
|  | description | String |  | 
|  | destination | String |  | 
|  | dispute | String |  | 
|  | disputed | Boolean | = | 
|  | failure\_balance\_transaction | String |  | 
|  | failure\_code | String |  | 
|  | failure\_message | String |  | 
|  | fraud\_details | Struct |  | 
|  | invoice | String |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | on\_behalf\_of | String |  | 
|  | order | String |  | 
|  | outcome | Struct |  | 
|  | paid | Boolean |  | 
|  | payment\_intent | String | = | 
|  | payment\_method | String |  | 
|  | payment\_method\_details | Struct |  | 
|  | receipt\_email | String |  | 
|  | receipt\_number | String |  | 
|  | receipt\_url | String |  | 
|  | refunded | Boolean | = | 
|  | refunds | Struct |  | 
|  | review | String |  | 
|  | shipping | Struct |  | 
|  | source | Struct |  | 
|  | source\_transfer | String |  | 
|  | statement\_descriptor | String |  | 
|  | statement\_descriptor\_suffix | String |  | 
|  | status | String |  | 
|  | transfer | String |  | 
|  | transfer\_data | Struct |  | 
|  | transfer\_group | String | = | 
| Disputes |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer | =, <, > | 
|  | balance\_transaction | String |  | 
|  | balance\_transactions | List |  | 
|  | charge | String | = | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String |  | 
|  | evidence | Struct |  | 
|  | evidence\_details | Struct |  | 
|  | is\_charge\_refundable | Boolean |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | payment\_intent | String | = | 
|  | reason | String | = | 
|  | status | String |  | 
|  | payment\_method\_details | Struct |  | 
| File Links |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | expired | Boolean | = | 
|  | expires\_at | DateTime |  | 
|  | file | String | = | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | url | String |  | 
| PaymentIntents |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer |  | 
|  | amount\_capturable | Integer |  | 
|  | amount\_details | Struct |  | 
|  | amount\_received | Integer |  | 
|  | application | String |  | 
|  | application\_fee\_amount | Integer |  | 
|  | automatic\_payment\_methods | Struct |  | 
|  | canceled\_at | DateTime |  | 
|  | cancellation\_reason | String |  | 
|  | capture\_method | String |  | 
|  | client\_secret | String |  | 
|  | confirmation\_method | String |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String |  | 
|  | customer | String | = | 
|  | description | String |  | 
|  | invoice | String |  | 
|  | last\_payment\_error | Struct |  | 
|  | latest\_charge | String |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | next\_action | Struct |  | 
|  | on\_behalf\_of | String |  | 
|  | payment\_method | String |  | 
|  | payment\_method\_options | Struct |  | 
|  | payment\_method\_types | List |  | 
|  | payment\_method\_configuration\_details | Struct |  | 
|  | processing | Struct |  | 
|  | receipt\_email | String |  | 
|  | review | String |  | 
|  | setup\_future\_usage | String |  | 
|  | shipping | Struct |  | 
|  | source | String |  | 
|  | statement\_descriptor | String |  | 
|  | statement\_descriptor\_suffix | String |  | 
|  | status | String |  | 
|  | transfer\_data | Struct |  | 
|  | transfer\_group | String |  | 
| SetupIntents |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | application | String |  | 
|  | cancellation\_reason | String |  | 
|  | client\_secret | String |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | customer | String | = | 
|  | description | String |  | 
|  | flow\_directions | List |  | 
|  | last\_setup\_error | Struct |  | 
|  | latest\_attempt | String |  | 
|  | livemode | Boolean |  | 
|  | mandate | String |  | 
|  | metadata | Struct |  | 
|  | next\_action | Struct |  | 
|  | on\_behalf\_of | String |  | 
|  | payment\_method | String |  | 
|  | payment\_method\_options | Struct |  | 
|  | payment\_method\_types | List |  | 
|  | single\_use\_mandate | String |  | 
|  | status | String |  | 
|  | usage | String |  | 
|  | automatic\_payment\_methods | Struct |  | 
| Payouts |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer | =, <, > | 
|  | arrival\_date | DateTime | =, >=, <=,<,> | 
|  | automatic | Boolean |  | 
|  | balance\_transaction | String |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String |  | 
|  | description | String | = | 
|  | destination | String |  | 
|  | failure\_balance\_transaction | String |  | 
|  | failure\_code | String |  | 
|  | failure\_message | String |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | method | String |  | 
|  | original\_payout | String |  | 
|  | reversed\_by | String |  | 
|  | reconciliation\_status | String |  | 
|  | source\_type | String |  | 
|  | statement\_descriptor | String |  | 
|  | status | String |  | 
|  | type | String |  | 
|  | application\_fee | String |  | 
|  | application\_fee\_amount | Integer |  | 
| Refunds |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer |  | 
|  | balance\_transaction | String |  | 
|  | charge | String | = | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String |  | 
|  | metadata | Struct |  | 
|  | destination\_details | Struct |  | 
|  | payment\_intent | String | = | 
|  | reason | String |  | 
|  | receipt\_number | String |  | 
|  | source\_transfer\_reversal | String |  | 
|  | status | String |  | 
|  | transfer\_reversal | String |  | 
| Products |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | active | Boolean | = | 
|  | attributes | List |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | default\_price | String |  | 
|  | description | String |  | 
|  | images | List |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | name | String |  | 
|  | package\_dimensions | Struct |  | 
|  | shippable | Boolean |  | 
|  | statement\_descriptor | String |  | 
|  | tax\_code | String |  | 
|  | type | String | = | 
|  | unit\_label | String |  | 
|  | updated | DateTime |  | 
|  | url | String |  | 
|  | features | List |  | 
| Prices |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | active | Boolean | = | 
|  | billing\_scheme | String |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String | = | 
|  | custom\_unit\_amount | Struct |  | 
|  | livemode | Boolean |  | 
|  | lookup\_key | String |  | 
|  | metadata | Struct |  | 
|  | nickname | String |  | 
|  | product | String | = | 
|  | recurring | Struct |  | 
|  | tax\_behavior | String |  | 
|  | tiers\_mode | String |  | 
|  | transform\_quantity | Struct |  | 
|  | type | String | = | 
|  | unit\_amount | Integer |  | 
|  | unit\_amount\_decimal | String |  | 
| Coupons |  |  |  | 
|  | Id | String |  | 
|  | object | String |  | 
|  | amount\_off | Integer |  | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String | = | 
|  | duration | String | = | 
|  | duration\_in\_months | Integer | =,<,> | 
|  | livemode | Boolean |  | 
|  | max\_redemptions | Integer | =, <, > | 
|  | metadata | Struct |  | 
|  | name | String |  | 
|  | percent\_off | Double | = | 
|  | redeem\_by | DateTime | =, >=, <=, <, > | 
|  | times\_redeemed | Integer |  | 
|  | valid | Boolean |  | 
| Promotion Codes |  |  |  | 
|  | Id | String |  | 
|  | object | String |  | 
|  | active | Boolean | = | 
|  | code | String | = | 
|  | coupon | Struct |  | 
|  | created | DateTime | =,>=,<=,<,> | 
|  | customer | String |  | 
|  | expires\_at | DateTime |  | 
|  | livemode | Boolean |  | 
|  | max\_redemptions | Integer |  | 
|  | metadata | Struct |  | 
|  | restrictions | Struct |  | 
|  | times\_redeemed | Integer |  | 
| Tax Codes |  |  |  | 
|  | Id | String |  | 
|  | object | String |  | 
|  | description | String |  | 
|  | name | String |  | 
| Tax Rates |  |  |  | 
|  | Id | String |  | 
|  | object | String |  | 
|  | active | Boolean | = | 
|  | country | String |  | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | description | String |  | 
|  | display\_name | String |  | 
|  | inclusive | Boolean | = | 
|  | jurisdiction | String |  | 
|  | jurisdiction\_level | String |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | percentage | Double |  | 
|  | effective\_percentage | Double |  | 
|  | state | String |  | 
|  | tax\_type | String |  | 
| Shipping Rates |  |  |  | 
|  | Id | String |  | 
|  | object | String |  | 
|  | active | Boolean | = | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | delivery\_estimate | Struct |  | 
|  | display\_name | String |  | 
|  | fixed\_amount | Struct |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | tax\_behavior | String |  | 
|  | tax\_code | String |  | 
|  | type | String |  | 
| Sessions |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | after\_expiration | Struct |  | 
|  | allow\_promotion\_codes | Boolean |  | 
|  | amount\_subtotal | Integer |  | 
|  | amount\_total | Integer |  | 
|  | automatic\_tax | Struct |  | 
|  | billing\_address\_collection | String |  | 
|  | cancel\_url | String |  | 
|  | client\_reference\_id | String |  | 
|  | consent | Struct |  | 
|  | consent\_collection | Struct |  | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | currency | String |  | 
|  | custom\_text | Struct |  | 
|  | customer | String |  | 
|  | customer\_creation | String |  | 
|  | customer\_details | Struct |  | 
|  | customer\_email | String |  | 
|  | expires\_at | DateTime |  | 
|  | invoice | String |  | 
|  | invoice\_creation | Struct |  | 
|  | livemode | Boolean |  | 
|  | locale | String |  | 
|  | metadata | Struct |  | 
|  | mode | String |  | 
|  | payment\_intent | String | = | 
|  | payment\_link | String |  | 
|  | payment\_method\_collection | String |  | 
|  | payment\_method\_options | Struct |  | 
|  | payment\_method\_types | List |  | 
|  | payment\_status | String |  | 
|  | phone\_number\_collection | Struct |  | 
|  | recovered\_from | String |  | 
|  | setup\_intent | String |  | 
|  | shipping\_address\_collection | Struct |  | 
|  | shipping\_cost | Struct |  | 
|  | shipping\_details | Struct |  | 
|  | shipping\_options | List |  | 
|  | status | String |  | 
|  | submit\_type | String |  | 
|  | subscription | String |  | 
|  | success\_url | String |  | 
|  | tax\_id\_collection | Struct |  | 
|  | total\_details | Struct |  | 
|  | url | String |  | 
|  | ui\_mode | String |  | 
| Credit Notes |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer |  | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | currency | String |  | 
|  | customer | String | = | 
|  | customer\_balance\_transaction | String |  | 
|  | discount\_amount | Integer |  | 
|  | discount\_amounts | List |  | 
|  | invoice | String | = | 
|  | lines | Struct |  | 
|  | livemode | Boolean |  | 
|  | memo | String |  | 
|  | metadata | Struct |  | 
|  | number | String |  | 
|  | out\_of\_band\_amount | Integer |  | 
|  | pdf | String |  | 
|  | reason | String |  | 
|  | refund | String |  | 
|  | status | String |  | 
|  | subtotal | Integer |  | 
|  | subtotal\_excluding\_tax | Integer |  | 
|  | tax\_amounts | List |  | 
|  | total | Integer |  | 
|  | total\_excluding\_tax | Integer |  | 
|  | type | String |  | 
|  | voided\_at | DateTime |  | 
|  | amount\_shipping | Integer |  | 
|  | effective\_at | DateTime |  | 
|  | shipping\_cost | Struct |  | 
| Customer |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | address | Struct |  | 
|  | balance | Integer |  | 
|  | created | DateTime |  | 
|  | currency | String | =, >=, <=, <, > | 
|  | default\_source | String |  | 
|  | delinquent | Boolean | = | 
|  | description | String |  | 
|  | discount | Struct |  | 
|  | email | String | = | 
|  | invoice\_prefix | String |  | 
|  | invoice\_settings | Struct |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | name | String |  | 
|  | next\_invoice\_sequence | Integer |  | 
|  | phone | String |  | 
|  | preferred\_locales | List |  | 
|  | shipping | Struct |  | 
|  | tax\_exempt | String |  | 
|  | test\_clock | String |  | 
| Invoices |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | account\_country | String |  | 
|  | account\_name | String |  | 
|  | account\_tax\_ids | List |  | 
|  | amount\_due | Integer |  | 
|  | amount\_paid | Integer |  | 
|  | amount\_remaining | Integer |  | 
|  | application | String |  | 
|  | application\_fee\_amount | Integer |  | 
|  | attempt\_count | Integer |  | 
|  | attempted | Boolean | = | 
|  | auto\_advance | Boolean | = | 
|  | automatic\_tax | Struct |  | 
|  | billing\_reason | String |  | 
|  | charge | String |  | 
|  | collection\_method | String | = | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | currency | String |  | 
|  | custom\_fields | List |  | 
|  | customer | String | = | 
|  | customer\_address | Struct |  | 
|  | customer\_email | String |  | 
|  | customer\_name | String |  | 
|  | customer\_phone | String |  | 
|  | customer\_shipping | Struct |  | 
|  | customer\_tax\_exempt | String |  | 
|  | customer\_tax\_ids | List |  | 
|  | default\_payment\_method | String |  | 
|  | default\_source | String |  | 
|  | default\_tax\_rates | List |  | 
|  | description | String |  | 
|  | discount | Struct |  | 
|  | discounts | List |  | 
|  | due\_date | DateTime | =, >=, <=, <, > | 
|  | ending\_balance | Integer |  | 
|  | footer | String |  | 
|  | from\_invoice | Struct |  | 
|  | hosted\_invoice\_url | String |  | 
|  | invoice\_pdf | String |  | 
|  | last\_finalization\_error | Struct |  | 
|  | latest\_revision | String |  | 
|  | lines | Struct |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | next\_payment\_attempt | DateTime |  | 
|  | number | String |  | 
|  | on\_behalf\_of | String |  | 
|  | paid | Boolean | = | 
|  | paid\_out\_of\_band | Boolean |  | 
|  | payment\_intent | String |  | 
|  | payment\_settings | Struct |  | 
|  | period\_end | DateTime | =, >=, <=, <, > | 
|  | period\_start | DateTime | =, >=, <=, <, > | 
|  | post\_payment\_credit\_notes\_amount | Integer |  | 
|  | pre\_payment\_credit\_notes\_amount | Integer |  | 
|  | quote | String |  | 
|  | receipt\_number | String |  | 
|  | rendering | Struct |  | 
|  | rendering\_options | Struct |  | 
|  | starting\_balance | Integer |  | 
|  | statement\_descriptor | String |  | 
|  | status | String | = | 
|  | status\_transitions | Struct |  | 
|  | subscription | String |  | 
|  | subscription\_details | Struct |  | 
|  | subtotal | Integer | =, <, > | 
|  | subtotal\_excluding\_tax | Integer |  | 
|  | tax | Integer |  | 
|  | test\_clock | String |  | 
|  | total | Integer | =, <, > | 
|  | total\_discount\_amounts | List |  | 
|  | total\_excluding\_tax | Integer |  | 
|  | total\_tax\_amounts | List |  | 
|  | transfer\_data | Struct |  | 
|  | webhooks\_delivered\_at | DateTime |  | 
|  | automatically\_finalizes\_at | DateTime |  | 
|  | effective\_at | DateTime |  | 
|  | issuer | Struct |  | 
| Invoice Items |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer | =, <, > | 
|  | currency | String |  | 
|  | customer | String | = | 
|  | date | DateTime |  | 
|  | description | String |  | 
|  | discountable | Boolean |  | 
|  | discounts | List |  | 
|  | invoice | String | = | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | period | Struct |  | 
|  | plan | Struct |  | 
|  | price | Struct |  | 
|  | proration | Boolean | = | 
|  | quantity | Integer |  | 
|  | subscription | String |  | 
|  | subscription\_item | String |  | 
|  | tax\_rates | List |  | 
|  | test\_clock | String |  | 
|  | unit\_amount | Integer |  | 
|  | unit\_amount\_decimal | String |  | 
| Plans |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | active | Boolean | = | 
|  | aggregate\_usage | String |  | 
|  | amount | Integer |  | 
|  | amount\_decimal | String |  | 
|  | billing\_scheme | String |  | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | currency | String | = | 
|  | interval | String | = | 
|  | interval\_count | Integer |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | nickname | String |  | 
|  | product | String | = | 
|  | tiers\_mode | String |  | 
|  | transform\_usage | Struct |  | 
|  | trial\_period\_days | Integer | =, <, > | 
|  | usage\_type | String |  | 
|  | meter | String |  | 
| Quotes |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount\_subtotal | Integer |  | 
|  | amount\_total | Integer |  | 
|  | application | String |  | 
|  | application\_fee\_amount | Integer |  | 
|  | application\_fee\_percent | Double |  | 
|  | automatic\_tax | Struct |  | 
|  | collection\_method | String |  | 
|  | computed | Struct |  | 
|  | created | DateTime |  | 
|  | currency | String |  | 
|  | customer | String | = | 
|  | default\_tax\_rates | List |  | 
|  | description | String |  | 
|  | discounts | List |  | 
|  | expires\_at | DateTime |  | 
|  | footer | String |  | 
|  | from\_quote | Struct |  | 
|  | header | String |  | 
|  | invoice | String |  | 
|  | invoice\_settings | Struct |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | number | String |  | 
|  | on\_behalf\_of | String |  | 
|  | status | String | = | 
|  | status\_transitions | Struct |  | 
|  | subscription | String |  | 
|  | subscription\_data | Struct |  | 
|  | subscription\_schedule | String |  | 
|  | test\_clock | String |  | 
|  | total\_details | Struct |  | 
|  | transfer\_data | Struct |  | 
| Subscriptions |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | application | String |  | 
|  | application\_fee\_percent | Double |  | 
|  | automatic\_tax | Struct |  | 
|  | billing\_cycle\_anchor | DateTime |  | 
|  | billing\_thresholds | Struct |  | 
|  | cancel\_at | DateTime |  | 
|  | cancel\_at\_period\_end | Boolean |  | 
|  | canceled\_at | DateTime |  | 
|  | collection\_method | String | = | 
|  | created | DateTime | =, >=, <=,<,> | 
|  | currency | String |  | 
|  | current\_period\_end | DateTime | =, >=, <= | 
|  | current\_period\_start | DateTime | =, >=, <= | 
|  | customer | String | = | 
|  | days\_until\_due | Integer |  | 
|  | default\_payment\_method | String |  | 
|  | default\_source | String |  | 
|  | default\_tax\_rates | List |  | 
|  | description | String |  | 
|  | discount | Struct |  | 
|  | ended\_at | DateTime |  | 
|  | items | Struct |  | 
|  | latest\_invoice | String |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | next\_pending\_invoice\_item\_invoice | DateTime |  | 
|  | pause\_collection | Struct |  | 
|  | payment\_settings | Struct |  | 
|  | pending\_invoice\_item\_interval | Struct |  | 
|  | pending\_setup\_intent | String |  | 
|  | pending\_update | Struct |  | 
|  | plan | Struct |  | 
|  | quantity | Integer |  | 
|  | schedule | String |  | 
|  | start\_date | DateTime |  | 
|  | status | String | = | 
|  | test\_clock | String |  | 
|  | transfer\_data | Struct |  | 
|  | trial\_end | DateTime |  | 
|  | trial\_start | DateTime |  | 
| Subscription Items |  |  |  | 
|  | Id | String |  | 
|  | object | String |  | 
|  | billing\_thresholds | Struct |  | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | metadata | Struct |  | 
|  | plan | Struct |  | 
|  | price | Struct |  | 
|  | subscription | String |  | 
|  | tax\_rates | List |  | 
|  | discounts | List |  | 
| Subscription Schedules |  |  |  | 
|  | object | String |  | 
|  | application | String |  | 
|  | canceled\_at | DateTime |  | 
|  | completed\_at | DateTime |  | 
|  | created | DateTime |  | 
|  | current\_phase | Struct |  | 
|  | customer | String | = | 
|  | default\_settings | Struct |  | 
|  | end\_behavior | String |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | phases | List |  | 
|  | released\_at | DateTime |  | 
|  | released\_subscription | String |  | 
|  | renewal\_interval | String |  | 
|  | status | String |  | 
|  | subscription | String |  | 
|  | test\_clock | String |  | 
| Accounts |  |  |  | 
|  | details\_submitted | Boolean |  | 
|  | tos\_acceptance | Struct |  | 
|  | type | String |  | 
|  | metadata | Struct |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | default\_currency | String |  | 
|  | capabilities | Struct |  | 
|  | charges\_enabled | Boolean |  | 
|  | settings | Struct |  | 
|  | requirements | Struct |  | 
|  | payouts\_enabled | Boolean |  | 
|  | future\_requirements | Struct |  | 
|  | external\_accounts | Struct |  | 
|  | controller | Struct |  | 
|  | country | String |  | 
|  | email | String |  | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | business\_profile | Struct |  | 
|  | business\_type | String |  | 
|  | company | Struct |  | 
| Application Fees |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | account | String |  | 
|  | amount | Integer | =, <, > | 
|  | amount\_refunded | Integer | =, <, > | 
|  | application | String |  | 
|  | balance\_transaction | String |  | 
|  | charge | String | = | 
|  | created | DateTime |  | 
|  | currency | String |  | 
|  | livemode | Boolean |  | 
|  | originating\_transaction | String |  | 
|  | refunded | Boolean | = | 
|  | refunds | Struct |  | 
|  | fee\_source | Struct |  | 
| Country Specs |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | default\_currency | String |  | 
|  | supported\_bank\_account\_currencies | Struct |  | 
|  | supported\_payment\_currencies | List |  | 
|  | supported\_payment\_methods | List |  | 
|  | supported\_transfer\_countries | List |  | 
|  | verification\_fields | Struct |  | 
| Transfers |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | amount | Integer | =, <, > | 
|  | amount\_reversed | Integer |  | 
|  | balance\_transaction | String |  | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | currency | String | = | 
|  | description | String |  | 
|  | destination | String | = | 
|  | destination\_payment | String |  | 
|  | livemode | Boolean |  | 
|  | metadata | Struct |  | 
|  | reversals | Struct |  | 
|  | reversed | Boolean |  | 
|  | source\_transaction | String |  | 
|  | source\_type | String |  | 
|  | transfer\_group | String | = | 
| Early Fraud Warnings |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | actionable | Boolean |  | 
|  | charge | String | = | 
|  | created | DateTime | =, >=, <=, <, > | 
|  | fraud\_type | String |  | 
|  | livemode | Boolean |  | 
|  | payment\_intent | String | = | 
| Report Types |  |  |  | 
|  | id | String |  | 
|  | object | String |  | 
|  | data\_available\_end | DateTime |  | 
|  | data\_available\_start | DateTime |  | 
|  | default\_columns | List |  | 
|  | livemode | Boolean |  | 
|  | name | String |  | 
|  | updated | DateTime |  | 
|  | version | Integer |  | 

 **Partitioning queries** 

 Additional spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, `NUM_PARTITIONS` can be provided if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by spark tasks concurrently. 
+  `PARTITION_FIELD`: the name of the field to be used to partition query. 
+  `LOWER_BOUND`: an inclusive lower bound value of the chosen partition field. 

   For date, we accept the Spark date format used in Spark SQL queries. Example of valid value: `"2024-07-01T00:00:00.000Z"`. 
+  `UPPER_BOUND`: an exclusive upper bound value of the chosen partition field. 
+  `NUM_PARTITIONS`: number of partitions. 

 Entity wise partitioning field support details are captured in below table. 


| Entity Name | Partitioning Field | Data Type | 
| --- | --- | --- | 
| Balance Transactions | created | DateTime | 
| Charges | created | DateTime | 
| Disputes | created | DateTime | 
| File Links | created | DateTime | 
| PaymentIntents | created | DateTime | 
| SetupIntents | created | DateTime | 
| Payouts | created | DateTime | 
| Refunds | created | DateTime | 
| Products | created | DateTime | 
| Prices | created | DateTime | 
| Coupons | created | DateTime | 
| Promotion Codes | created | DateTime | 
| Tax Rates | created | DateTime | 
| Shipping Rates | created | DateTime | 
| Sessions | created | DateTime | 
| Credit Notes | created | DateTime | 
| Customer | created | DateTime | 
| Invoices | created | DateTime | 
| Plans | created | DateTime | 
| Subscriptions | created | DateTime | 
| Subscription Schedules | created | DateTime | 
| Accounts | created | DateTime | 
| Application Fees | created | DateTime | 
| Transfers | created | DateTime | 
| Early Fraud Warnings | created | DateTime | 

 **Example** 

```
stripe_read = glueContext.create_dynamic_frame.from_options(
    connection_type="stripe",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "coupons",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "created"
        "LOWER_BOUND": "2024-05-01T20:55:02.000Z"
        "UPPER_BOUND": "2024-07-11T20:55:02.000Z"
        "NUM_PARTITIONS": "10"
    }
)
```