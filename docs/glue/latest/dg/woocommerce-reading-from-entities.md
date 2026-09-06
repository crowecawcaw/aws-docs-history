

# Reading from WooCommerce entities
<a name="woocommerce-reading-from-entities"></a>

**Prerequisite**

A WooCommerce object you would like to read from. You will need the object name such as coupon, order, product, etc.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Coupon | Yes | Yes | Yes | Yes | Yes | 
| Coupon Total | No | No | No | Yes | No | 
| Customers Total | No | No | No | Yes | No | 
| Order | Yes | Yes | Yes | Yes | Yes | 
| Orders Total | No | No | No | Yes | No | 
| Payment Gateway | No | No | No | Yes | No | 
| Product | Yes | Yes | Yes | Yes | Yes | 
| Product attribute | Yes | Yes | Yes | Yes | Yes | 
| Product category | Yes | Yes | Yes | Yes | Yes | 
| Product review | Yes | Yes | Yes | Yes | Yes | 
| Product shipping class | Yes | Yes | Yes | Yes | Yes | 
| Product tag | Yes | Yes | Yes | Yes | Yes | 
| Product variation | Yes | Yes | Yes | Yes | Yes | 
| Products Total | No | No | No | Yes | No | 
| Report (List) | No | No | No | Yes | No | 
| Reviews Total | No | No | No | Yes | No | 
| Sales Report | Yes | No | No | Yes | No | 
| Shipping Method | No | No | No | Yes | No | 
| Shipping Zone | No | No | No | Yes | No | 
| Shipping Zone Location | No | No | No | Yes | No | 
| Shipping Zone Method | No | No | No | Yes | No | 
| Tax Rate | Yes | Yes | Yes | Yes | Yes | 
| Tax Class | No | No | No | Yes | No | 
| Top Sellers Report | Yes | No | No | Yes | No | 

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



- **coupon**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** code / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** amount / **Data type:** String / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_created\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** discount\_type / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_expires / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_expires\_gmt / **Data type:** String / **Supported operators:** N/A
  - **Field:** usage\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** individual\_use / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** product\_ids / **Data type:** List / **Supported operators:** N/A
  - **Field:** excluded\_product\_ids / **Data type:** List / **Supported operators:** N/A
  - **Field:** usage\_limit / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** usage\_limit\_per\_user / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** limit\_usage\_to\_x\_items / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** free\_shipping / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** product\_categories / **Data type:** List / **Supported operators:** N/A
  - **Field:** excluded\_product\_categories / **Data type:** List / **Supported operators:** N/A
  - **Field:** exclude\_sale\_items / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** minimum\_amount / **Data type:** String / **Supported operators:** N/A
  - **Field:** maximum\_amount / **Data type:** String / **Supported operators:** N/A
  - **Field:** email\_restrictions / **Data type:** List / **Supported operators:** N/A
  - **Field:** used\_by / **Data type:** List / **Supported operators:** N/A
  - **Field:** meta\_data / **Data type:** List / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** modified\_after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** modified\_before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** dates\_are\_gmt / **Data type:** Boolean / **Supported operators:** EQUAL\_TO

- **coupon-total**
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** total / **Data type:** Integer / **Supported operators:** N/A

- **customer-total**
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** total / **Data type:** Integer / **Supported operators:** N/A

- **order**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** parent\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** number / **Data type:** String / **Supported operators:** N/A
  - **Field:** order\_key / **Data type:** String / **Supported operators:** N/A
  - **Field:** created\_via / **Data type:** String / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** N/A
  - **Field:** currency / **Data type:** String / **Supported operators:** N/A
  - **Field:** version / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** discount\_total / **Data type:** String / **Supported operators:** N/A
  - **Field:** discount\_tax / **Data type:** String / **Supported operators:** N/A
  - **Field:** shipping\_total / **Data type:** String / **Supported operators:** N/A
  - **Field:** shipping\_tax / **Data type:** String / **Supported operators:** N/A
  - **Field:** cart\_tax / **Data type:** String / **Supported operators:** N/A
  - **Field:** total / **Data type:** String / **Supported operators:** N/A
  - **Field:** total\_tax / **Data type:** String / **Supported operators:** N/A
  - **Field:** prices\_include\_tax / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** customer\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** customer\_ip\_address / **Data type:** String / **Supported operators:** N/A
  - **Field:** customer\_user\_agent / **Data type:** String / **Supported operators:** N/A
  - **Field:** customer\_note / **Data type:** String / **Supported operators:** N/A
  - **Field:** billing / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** shipping / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** payment\_method / **Data type:** String / **Supported operators:** N/A
  - **Field:** payment\_method\_title / **Data type:** String / **Supported operators:** N/A
  - **Field:** transaction\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_paid / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_completed / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** cart\_hash / **Data type:** String / **Supported operators:** N/A
  - **Field:** meta\_data / **Data type:** List / **Supported operators:** N/A
  - **Field:** line\_items / **Data type:** List / **Supported operators:** N/A
  - **Field:** tax\_lines / **Data type:** List / **Supported operators:** N/A
  - **Field:** shipping\_lines / **Data type:** List / **Supported operators:** N/A
  - **Field:** fee\_lines / **Data type:** List / **Supported operators:** N/A
  - **Field:** coupon\_lines / **Data type:** List / **Supported operators:** N/A
  - **Field:** refunds / **Data type:** List / **Supported operators:** N/A
  - **Field:** payment\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** is\_editable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** needs\_payment / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** needs\_processing / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** date\_created\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_completed\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_paid\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** currency\_symbol / **Data type:** String / **Supported operators:** N/A
  - **Field:** set\_paid / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** customer / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** product / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** dp / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** modified\_before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** modified\_after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** dates\_are\_gmt / **Data type:** Boolean / **Supported operators:** EQUAL\_TO

- **order-total**
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** total / **Data type:** Integer / **Supported operators:** N/A

- **payment-gateway**
  - **Field:** title / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** order / **Data type:** String / **Supported operators:** N/A
  - **Field:** enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** method\_title / **Data type:** String / **Supported operators:** N/A
  - **Field:** method\_description / **Data type:** String / **Supported operators:** N/A
  - **Field:** method\_supports / **Data type:** List / **Supported operators:** N/A
  - **Field:** settings / **Data type:** String / **Supported operators:** N/A
  - **Field:** needs\_setup / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** post\_install\_scripts / **Data type:** List / **Supported operators:** N/A
  - **Field:** settings\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** connection\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** setup\_help\_text / **Data type:** String / **Supported operators:** N/A
  - **Field:** required\_settings\_keys / **Data type:** List / **Supported operators:** N/A

- **product**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** permalink / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_created\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** catalog\_visibility / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** short\_description / **Data type:** String / **Supported operators:** N/A
  - **Field:** price / **Data type:** String / **Supported operators:** N/A
  - **Field:** regular\_price / **Data type:** String / **Supported operators:** N/A
  - **Field:** sale\_price / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_from / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_from\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_to / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_to\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** price\_html / **Data type:** String / **Supported operators:** N/A
  - **Field:** purchasable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** total\_sales / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** virtual / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** downloadable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** downloads / **Data type:** List / **Supported operators:** N/A
  - **Field:** download\_limit / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** download\_expiry / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** external\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** button\_text / **Data type:** String / **Supported operators:** N/A
  - **Field:** tax\_status / **Data type:** String / **Supported operators:** N/A
  - **Field:** manage\_stock / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** stock\_quantity / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** backorders / **Data type:** String / **Supported operators:** N/A
  - **Field:** backorders\_allowed / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** backordered / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** sold\_individually / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** weight / **Data type:** String / **Supported operators:** N/A
  - **Field:** dimensions / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** shipping\_required / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** shipping\_taxable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** shipping\_class\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** reviews\_allowed / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** average\_rating / **Data type:** String / **Supported operators:** N/A
  - **Field:** rating\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** related\_ids / **Data type:** List / **Supported operators:** N/A
  - **Field:** upsell\_ids / **Data type:** List / **Supported operators:** N/A
  - **Field:** cross\_sell\_ids / **Data type:** List / **Supported operators:** N/A
  - **Field:** parent\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** purchase\_note / **Data type:** String / **Supported operators:** N/A
  - **Field:** categories / **Data type:** List / **Supported operators:** N/A
  - **Field:** tags / **Data type:** List / **Supported operators:** N/A
  - **Field:** images / **Data type:** List / **Supported operators:** N/A
  - **Field:** attributes / **Data type:** List / **Supported operators:** N/A
  - **Field:** default\_attributes / **Data type:** List / **Supported operators:** N/A
  - **Field:** variations / **Data type:** List / **Supported operators:** N/A
  - **Field:** grouped\_products / **Data type:** List / **Supported operators:** N/A
  - **Field:** menu\_order / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** meta\_data / **Data type:** List / **Supported operators:** N/A
  - **Field:** low\_stock\_amount / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** jetpack\_publicize\_connections / **Data type:** List / **Supported operators:** N/A
  - **Field:** jetpack-related-posts / **Data type:** List / **Supported operators:** N/A
  - **Field:** jetpack\_likes\_enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** jetpack\_sharing\_enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** slug / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** status / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** sku / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** featured / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** tag / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** shipping\_class / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** tax\_class / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** on\_sale / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** stock\_status / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** has\_options / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** modified\_after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** modified\_before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** dates\_are\_gmt / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** category / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** attribute / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** min\_price / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** max\_price / **Data type:** String / **Supported operators:** EQUAL\_TO

- **product-attribute**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A
  - **Field:** order\_by / **Data type:** String / **Supported operators:** N/A
  - **Field:** has\_archives / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO

- **product-attribute-term**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** menu\_order / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** hide\_empty / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** parent / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** product / **Data type:** Integer / **Supported operators:** EQUAL\_TO

- **product-category**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** slug / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** display / **Data type:** String / **Supported operators:** N/A
  - **Field:** image / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** menu\_order / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** hide\_empty / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** parent / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** product / **Data type:** Integer / **Supported operators:** EQUAL\_TO

- **product-review**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_created\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** product\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** product\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** product\_permalink / **Data type:** String / **Supported operators:** N/A
  - **Field:** review / **Data type:** String / **Supported operators:** N/A
  - **Field:** rating / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** verified / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** reviewer / **Data type:** String / **Supported operators:** N/A
  - **Field:** reviewer\_email / **Data type:** String / **Supported operators:** N/A
  - **Field:** reviewer\_avatar\_urls / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** status / **Data type:** String / **Supported operators:** EQUAL\_TO

- **product-shipping-class**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** slug / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** hide\_empty / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** product / **Data type:** Integer / **Supported operators:** EQUAL\_TO

- **product-tag**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** slug / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** hide\_empty / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** product / **Data type:** Integer / **Supported operators:** EQUAL\_TO

- **product-total**
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** total / **Data type:** Integer / **Supported operators:** N/A

- **product-variation**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_created\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_modified\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** permalink / **Data type:** String / **Supported operators:** N/A
  - **Field:** price / **Data type:** String / **Supported operators:** N/A
  - **Field:** regular\_price / **Data type:** String / **Supported operators:** N/A
  - **Field:** sale\_price / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_from / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_from\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_to / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** date\_on\_sale\_to\_gmt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** purchasable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** virtual / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** downloadable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** downloads / **Data type:** List / **Supported operators:** N/A
  - **Field:** download\_limit / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** download\_expiry / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** tax\_status / **Data type:** String / **Supported operators:** N/A
  - **Field:** manage\_stock / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** stock\_quantity / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** backorders / **Data type:** String / **Supported operators:** N/A
  - **Field:** backorders\_allowed / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** backordered / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** low\_stock\_amount / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** weight / **Data type:** String / **Supported operators:** N/A
  - **Field:** dimensions / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** shipping\_class / **Data type:** String / **Supported operators:** N/A
  - **Field:** shipping\_class\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** image / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** attributes / **Data type:** List / **Supported operators:** N/A
  - **Field:** menu\_order / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** meta\_data / **Data type:** List / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** search / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** after / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** before / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** slug / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** status / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** sku / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** tax\_class / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** on\_sale / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** min\_price / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** max\_price / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** stock\_status / **Data type:** String / **Supported operators:** EQUAL\_TO

- **report**
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A

- **review-total**
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** total / **Data type:** Integer / **Supported operators:** N/A

- **sales-report**
  - **Field:** total\_sales / **Data type:** String / **Supported operators:** N/A
  - **Field:** net\_sales / **Data type:** String / **Supported operators:** N/A
  - **Field:** average\_sales / **Data type:** String / **Supported operators:** N/A
  - **Field:** total\_orders / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** total\_items / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** total\_tax / **Data type:** String / **Supported operators:** N/A
  - **Field:** total\_shipping / **Data type:** String / **Supported operators:** N/A
  - **Field:** total\_refunds / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** total\_discount / **Data type:** String / **Supported operators:** N/A
  - **Field:** totals\_grouped\_by / **Data type:** String / **Supported operators:** N/A
  - **Field:** totals / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** total\_customers / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** period / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** date\_min / **Data type:** Date / **Supported operators:** EQUAL\_TO
  - **Field:** date\_max / **Data type:** Date / **Supported operators:** EQUAL\_TO

- **shipping-method**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** title / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A

- **shipping-zone**
  - **Field:** id / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** order / **Data type:** Integer / **Supported operators:** N/A

- **shipping-zone-location**
  - **Field:** code / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A

- **shipping-zone-method**
  - **Field:** instance\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** id / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** title / **Data type:** String / **Supported operators:** N/A
  - **Field:** order / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** method\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** method\_title / **Data type:** String / **Supported operators:** N/A
  - **Field:** method\_description / **Data type:** String / **Supported operators:** N/A
  - **Field:** settings / **Data type:** Struct / **Supported operators:** N/A

- **tax-class**
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A

- **tax-rate**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** country / **Data type:** String / **Supported operators:** N/A
  - **Field:** state / **Data type:** String / **Supported operators:** N/A
  - **Field:** postcode / **Data type:** String / **Supported operators:** N/A
  - **Field:** city / **Data type:** String / **Supported operators:** N/A
  - **Field:** postcodes / **Data type:** List / **Supported operators:** N/A
  - **Field:** cities / **Data type:** List / **Supported operators:** N/A
  - **Field:** rate / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** priority / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** compound / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** shipping / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** order / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** orderby / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** class / **Data type:** String / **Supported operators:** EQUAL\_TO

- **top-seller-report**
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** product\_id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** quantity / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** period / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** date\_min / **Data type:** Date / **Supported operators:** EQUAL\_TO
  - **Field:** date\_max / **Data type:** Date / **Supported operators:** EQUAL\_TO



**Note**  
Struct and List data types are converted to String data type, and DateTime data type is converted to Timestamp in the response of the connectors.

## Partitioning queries
<a name="woocommerce-reading-partitioning-queries"></a>

**Record-based partitioning**:

You can provide the additional Spark option `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

In record-based partitioning, the total number of records present is queried from the WooCommerce API, and divided by a `NUM_PARTITIONS` number provided. The resulting number of records are then concurrently fetched by each sub-query.
+ `NUM_PARTITIONS`: the number of partitions.

The following entities support record-based partitioning:
+ coupon
+ order
+ product
+ product-attribute
+ product-attribute-term
+ product-category
+ product-review
+ product-shipping-class
+ product-tag
+ product-variation
+ tax-rate

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
+ `NUM_PARTITIONS`: the number of partitions.

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