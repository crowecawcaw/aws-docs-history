# Reading from WooCommerce entities

**Prerequisite**

A WooCommerce object you would like to read from. You will need the object name such as coupon, order, product, etc.

**Supported entities for source**:

| Entity                 | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ---------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Coupon                 | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Coupon Total           | No              | No             | No                | Yes                | No                    |
| Customers Total        | No              | No             | No                | Yes                | No                    |
| Order                  | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Orders Total           | No              | No             | No                | Yes                | No                    |
| Payment Gateway        | No              | No             | No                | Yes                | No                    |
| Product                | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Product attribute      | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Product category       | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Product review         | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Product shipping class | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Product tag            | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Product variation      | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Products Total         | No              | No             | No                | Yes                | No                    |
| Report (List)          | No              | No             | No                | Yes                | No                    |
| Reviews Total          | No              | No             | No                | Yes                | No                    |
| Sales Report           | Yes             | No             | No                | Yes                | No                    |
| Shipping Method        | No              | No             | No                | Yes                | No                    |
| Shipping Zone          | No              | No             | No                | Yes                | No                    |
| Shipping Zone Location | No              | No             | No                | Yes                | No                    |
| Shipping Zone Method   | No              | No             | No                | Yes                | No                    |
| Tax Rate               | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Tax Class              | No              | No             | No                | Yes                | No                    |
| Top Sellers Report     | Yes             | No             | No                | Yes                | No                    |

**Example**:

```
woocommerce_read = glueContext.create_dynamic_frame.from_options(
    connection_type="glue.spark.woocommerce",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "coupon",
        "API_VERSION": "v3",
        "INSTANCE_URL": "instanceUrl"
    }
```

**WooCommerce entity and field details**:

| Entity                          | Field        | Data type | Supported operators |
| ------------------------------- | ------------ | --------- | ------------------- |
| coupon                          | id           | Integer   | N/A                 |
| code                            | String       | EQUAL\_TO |
| amount                          | String       | N/A       |
| status                          | String       | N/A       |
| date\_created                   | DateTime     | N/A       |
| date\_created\_gmt              | DateTime     | N/A       |
| date\_modified                  | DateTime     | N/A       |
| date\_modified\_gmt             | DateTime     | N/A       |
| discount\_type                  | String       | N/A       |
| description                     | String       | N/A       |
| date\_expires                   | String       | N/A       |
| date\_expires\_gmt              | String       | N/A       |
| usage\_count                    | Integer      | N/A       |
| individual\_use                 | Boolean      | N/A       |
| product\_ids                    | List         | N/A       |
| excluded\_product\_ids          | List         | N/A       |
| usage\_limit                    | Integer      | N/A       |
| usage\_limit\_per\_user         | Integer      | N/A       |
| limit\_usage\_to\_x\_items      | Integer      | N/A       |
| free\_shipping                  | Boolean      | N/A       |
| product\_categories             | List         | N/A       |
| excluded\_product\_categories   | List         | N/A       |
| exclude\_sale\_items            | Boolean      | N/A       |
| minimum\_amount                 | String       | N/A       |
| maximum\_amount                 | String       | N/A       |
| email\_restrictions             | List         | N/A       |
| used\_by                        | List         | N/A       |
| meta\_data                      | List         | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| after                           | DateTime     | EQUAL\_TO |
| before                          | DateTime     | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| modified\_after                 | DateTime     | EQUAL\_TO |
| modified\_before                | DateTime     | EQUAL\_TO |
| dates\_are\_gmt                 | Boolean      | EQUAL\_TO |
| coupon-total                    | slug         | String    | N/A                 |
| name                            | String       | N/A       |
| total                           | Integer      | N/A       |
| customer-total                  | slug         | String    | N/A                 |
| name                            | String       | N/A       |
| total                           | Integer      | N/A       |
| order                           | id           | Integer   | N/A                 |
| parent\_id                      | Integer      | N/A       |
| number                          | String       | N/A       |
| order\_key                      | String       | N/A       |
| created\_via                    | String       | N/A       |
| status                          | String       | N/A       |
| currency                        | String       | N/A       |
| version                         | String       | N/A       |
| date\_created                   | DateTime     | N/A       |
| date\_modified                  | DateTime     | N/A       |
| discount\_total                 | String       | N/A       |
| discount\_tax                   | String       | N/A       |
| shipping\_total                 | String       | N/A       |
| shipping\_tax                   | String       | N/A       |
| cart\_tax                       | String       | N/A       |
| total                           | String       | N/A       |
| total\_tax                      | String       | N/A       |
| prices\_include\_tax            | Boolean      | N/A       |
| customer\_id                    | Integer      | N/A       |
| customer\_ip\_address           | String       | N/A       |
| customer\_user\_agent           | String       | N/A       |
| customer\_note                  | String       | N/A       |
| billing                         | Struct       | N/A       |
| shipping                        | Struct       | N/A       |
| payment\_method                 | String       | N/A       |
| payment\_method\_title          | String       | N/A       |
| transaction\_id                 | String       | N/A       |
| date\_paid                      | DateTime     | N/A       |
| date\_completed                 | DateTime     | N/A       |
| cart\_hash                      | String       | N/A       |
| meta\_data                      | List         | N/A       |
| line\_items                     | List         | N/A       |
| tax\_lines                      | List         | N/A       |
| shipping\_lines                 | List         | N/A       |
| fee\_lines                      | List         | N/A       |
| coupon\_lines                   | List         | N/A       |
| refunds                         | List         | N/A       |
| payment\_url                    | String       | N/A       |
| is\_editable                    | Boolean      | N/A       |
| needs\_payment                  | Boolean      | N/A       |
| needs\_processing               | Boolean      | N/A       |
| date\_created\_gmt              | DateTime     | N/A       |
| date\_modified\_gmt             | DateTime     | N/A       |
| date\_completed\_gmt            | DateTime     | N/A       |
| date\_paid\_gmt                 | DateTime     | N/A       |
| currency\_symbol                | String       | N/A       |
| set\_paid                       | Boolean      | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| after                           | DateTime     | EQUAL\_TO |
| before                          | DateTime     | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| customer                        | Integer      | EQUAL\_TO |
| product                         | Integer      | EQUAL\_TO |
| dp                              | Integer      | EQUAL\_TO |
| modified\_before                | DateTime     | EQUAL\_TO |
| modified\_after                 | DateTime     | EQUAL\_TO |
| dates\_are\_gmt                 | Boolean      | EQUAL\_TO |
| order-total                     | slug         | String    | N/A                 |
| name                            | String       | N/A       |
| total                           | Integer      | N/A       |
| payment-gateway                 | title        | String    | N/A                 |
| description                     | String       | N/A       |
| order                           | String       | N/A       |
| enabled                         | Boolean      | N/A       |
| method\_title                   | String       | N/A       |
| method\_description             | String       | N/A       |
| method\_supports                | List         | N/A       |
| settings                        | String       | N/A       |
| needs\_setup                    | Boolean      | N/A       |
| post\_install\_scripts          | List         | N/A       |
| settings\_url                   | String       | N/A       |
| connection\_url                 | String       | N/A       |
| setup\_help\_text               | String       | N/A       |
| required\_settings\_keys        | List         | N/A       |
| product                         | id           | Integer   | N/A                 |
| name                            | String       | N/A       |
| type                            | String       | EQUAL\_TO |
| permalink                       | String       | N/A       |
| date\_created                   | DateTime     | N/A       |
| date\_created\_gmt              | DateTime     | N/A       |
| date\_modified                  | DateTime     | N/A       |
| date\_modified\_gmt             | DateTime     | N/A       |
| catalog\_visibility             | String       | N/A       |
| description                     | String       | N/A       |
| short\_description              | String       | N/A       |
| price                           | String       | N/A       |
| regular\_price                  | String       | N/A       |
| sale\_price                     | String       | N/A       |
| date\_on\_sale\_from            | DateTime     | N/A       |
| date\_on\_sale\_from\_gmt       | DateTime     | N/A       |
| date\_on\_sale\_to              | DateTime     | N/A       |
| date\_on\_sale\_to\_gmt         | DateTime     | N/A       |
| price\_html                     | String       | N/A       |
| purchasable                     | Boolean      | N/A       |
| total\_sales                    | Integer      | N/A       |
| virtual                         | Boolean      | N/A       |
| downloadable                    | Boolean      | N/A       |
| downloads                       | List         | N/A       |
| download\_limit                 | Integer      | N/A       |
| download\_expiry                | Integer      | N/A       |
| external\_url                   | String       | N/A       |
| button\_text                    | String       | N/A       |
| tax\_status                     | String       | N/A       |
| manage\_stock                   | Boolean      | N/A       |
| stock\_quantity                 | Integer      | N/A       |
| backorders                      | String       | N/A       |
| backorders\_allowed             | Boolean      | N/A       |
| backordered                     | Boolean      | N/A       |
| sold\_individually              | Boolean      | N/A       |
| weight                          | String       | N/A       |
| dimensions                      | Struct       | N/A       |
| shipping\_required              | Boolean      | N/A       |
| shipping\_taxable               | Boolean      | N/A       |
| shipping\_class\_id             | Integer      | N/A       |
| reviews\_allowed                | Boolean      | N/A       |
| average\_rating                 | String       | N/A       |
| rating\_count                   | Integer      | N/A       |
| related\_ids                    | List         | N/A       |
| upsell\_ids                     | List         | N/A       |
| cross\_sell\_ids                | List         | N/A       |
| parent\_id                      | Integer      | N/A       |
| purchase\_note                  | String       | N/A       |
| categories                      | List         | N/A       |
| tags                            | List         | N/A       |
| images                          | List         | N/A       |
| attributes                      | List         | N/A       |
| default\_attributes             | List         | N/A       |
| variations                      | List         | N/A       |
| grouped\_products               | List         | N/A       |
| menu\_order                     | Integer      | N/A       |
| meta\_data                      | List         | N/A       |
| low\_stock\_amount              | Integer      | N/A       |
| jetpack\_publicize\_connections | List         | N/A       |
| jetpack-related-posts           | List         | N/A       |
| jetpack\_likes\_enabled         | Boolean      | N/A       |
| jetpack\_sharing\_enabled       | Boolean      | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| after                           | DateTime     | EQUAL\_TO |
| before                          | DateTime     | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| slug                            | String       | EQUAL\_TO |
| status                          | String       | EQUAL\_TO |
| sku                             | String       | EQUAL\_TO |
| featured                        | Boolean      | EQUAL\_TO |
| tag                             | String       | EQUAL\_TO |
| shipping\_class                 | String       | EQUAL\_TO |
| tax\_class                      | String       | EQUAL\_TO |
| on\_sale                        | Boolean      | EQUAL\_TO |
| stock\_status                   | String       | EQUAL\_TO |
| has\_options                    | Boolean      | N/A       |
| modified\_after                 | DateTime     | EQUAL\_TO |
| modified\_before                | DateTime     | EQUAL\_TO |
| dates\_are\_gmt                 | Boolean      | EQUAL\_TO |
| category                        | String       | EQUAL\_TO |
| attribute                       | String       | EQUAL\_TO |
| min\_price                      | String       | EQUAL\_TO |
| max\_price                      | String       | EQUAL\_TO |
| product-attribute               | id           | Integer   | N/A                 |
| name                            | String       | N/A       |
| slug                            | String       | N/A       |
| type                            | String       | N/A       |
| order\_by                       | String       | N/A       |
| has\_archives                   | Boolean      | N/A       |
| context                         | String       | EQUAL\_TO |
| product-attribute-term          | id           | Integer   | N/A                 |
| name                            | String       | N/A       |
| slug                            | String       | N/A       |
| description                     | String       | N/A       |
| menu\_order                     | Integer      | N/A       |
| count                           | Integer      | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| hide\_empty                     | Boolean      | EQUAL\_TO |
| parent                          | Integer      | EQUAL\_TO |
| product                         | Integer      | EQUAL\_TO |
| product-category                | id           | Integer   | N/A                 |
| name                            | String       | N/A       |
| slug                            | String       | EQUAL\_TO |
| description                     | String       | N/A       |
| display                         | String       | N/A       |
| image                           | Struct       | N/A       |
| menu\_order                     | Integer      | N/A       |
| count                           | Integer      | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| hide\_empty                     | Boolean      | EQUAL\_TO |
| parent                          | Integer      | EQUAL\_TO |
| product                         | Integer      | EQUAL\_TO |
| product-review                  | id           | Integer   | N/A                 |
| date\_created                   | DateTime     | N/A       |
| date\_created\_gmt              | DateTime     | N/A       |
| product\_id                     | Integer      | N/A       |
| product\_name                   | String       | N/A       |
| product\_permalink              | String       | N/A       |
| review                          | String       | N/A       |
| rating                          | Integer      | N/A       |
| verified                        | Boolean      | N/A       |
| reviewer                        | String       | N/A       |
| reviewer\_email                 | String       | N/A       |
| reviewer\_avatar\_urls          | Struct       | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| after                           | DateTime     | EQUAL\_TO |
| before                          | DateTime     | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| status                          | String       | EQUAL\_TO |
| product-shipping-class          | id           | Integer   | N/A                 |
| name                            | String       | N/A       |
| slug                            | String       | EQUAL\_TO |
| description                     | String       | N/A       |
| count                           | Integer      | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| hide\_empty                     | String       | EQUAL\_TO |
| product                         | Integer      | EQUAL\_TO |
| product-tag                     | id           | Integer   | N/A                 |
| name                            | String       | N/A       |
| slug                            | String       | EQUAL\_TO |
| description                     | String       | N/A       |
| count                           | Integer      | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| hide\_empty                     | Boolean      | EQUAL\_TO |
| product                         | Integer      | EQUAL\_TO |
| product-total                   | slug         | String    | N/A                 |
| name                            | String       | N/A       |
| total                           | Integer      | N/A       |
| product-variation               | id           | Integer   | N/A                 |
| date\_created                   | DateTime     | N/A       |
| date\_created\_gmt              | DateTime     | N/A       |
| date\_modified                  | DateTime     | N/A       |
| date\_modified\_gmt             | DateTime     | N/A       |
| description                     | String       | N/A       |
| permalink                       | String       | N/A       |
| price                           | String       | N/A       |
| regular\_price                  | String       | N/A       |
| sale\_price                     | String       | N/A       |
| date\_on\_sale\_from            | DateTime     | N/A       |
| date\_on\_sale\_from\_gmt       | DateTime     | N/A       |
| date\_on\_sale\_to              | DateTime     | N/A       |
| date\_on\_sale\_to\_gmt         | DateTime     | N/A       |
| purchasable                     | Boolean      | N/A       |
| virtual                         | Boolean      | N/A       |
| downloadable                    | Boolean      | N/A       |
| downloads                       | List         | N/A       |
| download\_limit                 | Integer      | N/A       |
| download\_expiry                | Integer      | N/A       |
| tax\_status                     | String       | N/A       |
| manage\_stock                   | Boolean      | N/A       |
| stock\_quantity                 | Integer      | N/A       |
| backorders                      | String       | N/A       |
| backorders\_allowed             | Boolean      | N/A       |
| backordered                     | Boolean      | N/A       |
| low\_stock\_amount              | Integer      | N/A       |
| weight                          | String       | N/A       |
| dimensions                      | Struct       | N/A       |
| shipping\_class                 | String       | N/A       |
| shipping\_class\_id             | Integer      | N/A       |
| image                           | Struct       | N/A       |
| attributes                      | List         | N/A       |
| menu\_order                     | Integer      | N/A       |
| meta\_data                      | List         | N/A       |
| context                         | String       | EQUAL\_TO |
| search                          | String       | EQUAL\_TO |
| after                           | DateTime     | EQUAL\_TO |
| before                          | DateTime     | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| slug                            | String       | EQUAL\_TO |
| status                          | String       | EQUAL\_TO |
| sku                             | String       | EQUAL\_TO |
| tax\_class                      | String       | EQUAL\_TO |
| on\_sale                        | Boolean      | EQUAL\_TO |
| min\_price                      | String       | EQUAL\_TO |
| max\_price                      | String       | EQUAL\_TO |
| stock\_status                   | String       | EQUAL\_TO |
| report                          | slug         | String    | N/A                 |
| description                     | String       | N/A       |
| review-total                    | slug         | String    | N/A                 |
| name                            | String       | N/A       |
| total                           | Integer      | N/A       |
| sales-report                    | total\_sales | String    | N/A                 |
| net\_sales                      | String       | N/A       |
| average\_sales                  | String       | N/A       |
| total\_orders                   | Integer      | N/A       |
| total\_items                    | Integer      | N/A       |
| total\_tax                      | String       | N/A       |
| total\_shipping                 | String       | N/A       |
| total\_refunds                  | Integer      | N/A       |
| total\_discount                 | String       | N/A       |
| totals\_grouped\_by             | String       | N/A       |
| totals                          | Struct       | N/A       |
| total\_customers                | Integer      | N/A       |
| context                         | String       | EQUAL\_TO |
| period                          | String       | EQUAL\_TO |
| date\_min                       | Date         | EQUAL\_TO |
| date\_max                       | Date         | EQUAL\_TO |
| shipping-method                 | id           | String    | N/A                 |
| title                           | String       | N/A       |
| description                     | String       | N/A       |
| shipping-zone                   | id           | Integer   | EQUAL\_TO           |
| name                            | String       | N/A       |
| order                           | Integer      | N/A       |
| shipping-zone-location          | code         | String    | N/A                 |
| type                            | String       | N/A       |
| shipping-zone-method            | instance\_id | Integer   | N/A                 |
| id                              | Integer      | EQUAL\_TO |
| title                           | String       | N/A       |
| order                           | Integer      | N/A       |
| enabled                         | Boolean      | N/A       |
| method\_id                      | String       | N/A       |
| method\_title                   | String       | N/A       |
| method\_description             | String       | N/A       |
| settings                        | Struct       | N/A       |
| tax-class                       | slug         | String    | N/A                 |
| name                            | String       | N/A       |
| tax-rate                        | id           | Integer   | N/A                 |
| country                         | String       | N/A       |
| state                           | String       | N/A       |
| postcode                        | String       | N/A       |
| city                            | String       | N/A       |
| postcodes                       | List         | N/A       |
| cities                          | List         | N/A       |
| rate                            | String       | N/A       |
| name                            | String       | N/A       |
| priority                        | Integer      | N/A       |
| compound                        | Boolean      | N/A       |
| shipping                        | Boolean      | N/A       |
| context                         | String       | EQUAL\_TO |
| order                           | String       | EQUAL\_TO |
| orderby                         | String       | EQUAL\_TO |
| class                           | String       | EQUAL\_TO |
| top-seller-report               | name         | String    | N/A                 |
| product\_id                     | Integer      | N/A       |
| quantity                        | Integer      | N/A       |
| context                         | String       | EQUAL\_TO |
| period                          | String       | EQUAL\_TO |
| date\_min                       | Date         | EQUAL\_TO |
| date\_max                       | Date         | EQUAL\_TO |

###### Note

Struct and List data types are converted to String data type, and DateTime data type is converted to Timestamp in the response of the connectors.

## Partitioning queries

**Record-based partitioning**:

You can provide the additional Spark option `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks concurrently.

In record-based partitioning, the total number of records present is queried from the WooCommerce API, and divided by a `NUM_PARTITIONS` number provided. The resulting number of records are then concurrently fetched by each sub-query.

- `NUM_PARTITIONS`: the number of partitions.

The following entities support record-based partitioning:

- coupon
- order
- product
- product-attribute
- product-attribute-term
- product-category
- product-review
- product-shipping-class
- product-tag
- product-variation
- tax-rate

Example:

```
woocommerce_read = glueContext.create_dynamic_frame.from_options(
    connection_type="glue.spark.woocommerce",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "coupon",
        "API_VERSION": "v3",
        "INSTANCE_URL": "instanceUrl"
        "NUM_PARTITIONS": "10"
    }
```

**Record-based partitioning**:

The original query is splitinto `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently:

- `NUM_PARTITIONS`: the number of partitions.

Example:

```
WooCommerce_read = glueContext.create_dynamic_frame.from_options(
    connection_type="WooCommerce",
    connection_options={
        "connectionName": "connectionName",
        "REALMID": "1234567890123456789",
        "ENTITY_NAME": "Bill",
        "API_VERSION": "v3",
        "NUM_PARTITIONS": "10"
    }
```
