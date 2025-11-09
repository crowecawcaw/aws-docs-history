# Reading the service

price list file for an AWS service

|                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To provide feedback about AWS Price List, complete this [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA "https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA"). Your responses will be anonymous. \*_Note:_<br>• This survey is in English only. |

The service price list files for an AWS service includes the following types of
information:

- Service price list file details – Metadata about the service price list files, such
  as format version and publication date
- Product details – Product metadata that lists the products in a
  service price list file, along with product information
- Pricing details (terms) – Prices for all products in this service
  price list file

###### Contents

- [CSV file](reading-service-price-list-file-for-services.md#reading-service-price-list-file-csv "reading-service-price-list-file-for-services.md#reading-service-price-list-file-csv")
- [JSON file](reading-service-price-list-file-for-services.md#reading-service-price-list-file-json "reading-service-price-list-file-for-services.md#reading-service-price-list-file-json")
- [Service price list
  definitions](reading-service-price-list-file-for-services.md#service-price-list-files-details "reading-service-price-list-file-for-services.md#service-price-list-files-details")
- [Product details (products)
  definitions](reading-service-price-list-file-for-services.md#product-details-terms "reading-service-price-list-file-for-services.md#product-details-terms")
- [Product details (terms)
  definitions](reading-service-price-list-file-for-services.md#product-details-metadata "reading-service-price-list-file-for-services.md#product-details-metadata")

## CSV file

The first five rows of the CSV file contain the metadata for the price list file. The
sixth row has the column names for the products and their attributes, such as
`SKU`, `OfferTermCode`, `RateCode`,
`TermType`, and more.

The number of columns depends on the service. The first few columns contain
the pricing details, and other columns contain the product details for a
service.

## JSON file

The product details and pricing details are in separate sections. The same
product can be offered under multiple terms, and the same term can apply to
multiple products.

For example, an Amazon Elastic Compute Cloud (Amazon EC2) instance is available for an
`Hourly` or `Reserved` term. You can use the SKU of a
product to identify the terms that are available for that product.

###### Example: JSON

```
{
   "formatVersion":"The version of the file format",
   "disclaimer":"The disclaimers for the price list file",
   "offerCode":"The code for the service",
   "version":"The version of the price list file",
   "publicationDate":"The publication date of the price list file",
   "products": {
      "sku": {
         "sku":"The SKU of the product",
         "productFamily":"The product family of the product",
         "attributes": {
            "attributeName":"attributeValue",
         }
      }
   },
   "terms": {
      "termType": {
         "sku": {
            "sku": {
               "offerTermCode":"The term code of the product",
               "sku":"The SKU of the product",
               "effectiveDate":"The effective date of the pricing details",
               "termAttributesType":"The attribute type of the terms",
               "termAttributes": {
                  "attributeName":"attributeValue",
               },
               "priceDimensions": {
                  "rateCode": {
                     "rateCode":"The rate code of the price",
                     "description":"The description of the term",
                     "unit":"The usage measurement unit for the price",
                     "startingRange":"The start range for the term",
                     "endingRange":"The end range for the term",
                     "pricePerUnit": {
                        "currencyCode":"currencyRate",
                     }
                  }
               }
            }
         }
      }
   }
}
```

## Service price list

definitions

The following list defines the terms in the service price list files.

**formatVersion**

An attribute that tracks which format version the service price
list file is in. The `formatVersion` of the file is
updated when the structure is changed. For example, the version will
change from `v1` to `v2`.

**disclaimer**

Any disclaimers that apply to the service price list file.

**offerCode**

A unique code for the product of an AWS service. For example,
`AmazonEC2` for Amazon EC2 or `AmazonS3` for
Amazon S3.

**version**

An attribute that tracks the version of the service price list
file. Each time a new file is published, it contains a new version
number. For example, `20150409022205` and
`20150910182105`.

**publicationDate**

The date and time in UTC format when a service price list file was
published. For example, `2015-04-09T02:22:05Z` and
`2015-09-10T18:21:05Z`.

## Product details (products)

definitions

This section provides information about products in a service price list file
for an AWS service. Products are indexed by SKU.

**products:sku**

A unique code for a product. Use the `SKU` code to
correlate product details and pricing.

For example, a product with a SKU of `HCNSHWWAJSGVAHMH`
is available only for a price that also lists
`HCNSHWWAJSGVAHMH` as a SKU.

**products:sku:productFamily**

The category for the type of product. For example,
`compute` for Amazon EC2 or `storage` for
Amazon S3.

**products:sku:attributes**

A list of all of the product attributes.

**products:sku:attributes:Attribute Name**

The name of a product attribute. For example, `Instance
 Type`, `Processor`, or `OS`.

**products:sku:attributes:Attribute Value**

The value of a product attribute. For example,
`m1.small` (instance type), `xen` (type of
processor), or `Linux` (type of OS).

## Product details (terms)

definitions

This section provides information about the prices for products in a service
price list file for an AWS service.

Prices are indexed first by the terms (`onDemand` and
`reserved`), and then by SKU.

**terms:termType**

The specific type of term that a term definition describes. The
valid term types are `reserved` and
`onDemand`.

**terms:termType:SKU**

A unique code for a product. Use the `SKU` code to
correlate product details and pricing.

For example, a product with a SKU of `HCNSHWWAJSGVAHMH`
is available only for a price that also lists
`HCNSHWWAJSGVAHMH` as a SKU.

**terms:termType:sku:Offer Term Code**

A unique code for a specific type of term. For example,
`KCAKZHGHG`.

Product and price combinations are referenced by the SKU code
followed by the term code, separated by a period. For example,
`U7ADXS4BEK5XXHRU.KCAKZHGHG`.

**terms:termType:sku:Effective Date**

The date that an service price list file goes into effect. For
example, if a term has an `EffectiveDate` of November 1,
2017, the price isn't valid before that date.

**terms:termType:sku:Term Attributes Type**

A unique code for identifying what product and product offering
are covered by a term. For example, an `EC2-Reserved`
attribute type means that a term is available for Amazon EC2 reserved
hosts.

**terms:termType:sku:Term Attributes**

A list of all of the attributes that are applicable to a term
type. The format appears as `attribute-name:
 attribute-value`. For example, this can be the length of
term and the type of purchase covered by the term.

**terms:termType:sku:Term Attributes:Attribute Name**

The name of a `TermAttribute`. You can use it to look
up specific attributes. For example, you can look up terms by
`length` or `PurchaseOption`.

**terms:termType:sku:Term Attributes:Attribute Value**

The value of a `TermAttribute`. For example, terms can
have a length of one year and a purchase option of `All
 Upfront`.

**terms:termType:sku:Price Dimensions**

The pricing details for the price list file, such as how usage is
measured, the currency that you can use to pay with, and the pricing
tier limitations.

**terms:termType:sku:Price Dimensions:Rate Code**

A unique code for a product, offer, and pricing-tier combination.
Product and term combinations can have multiple price dimensions,
such as free tier, low use tier, and high use tier.

**terms:termType:sku:Price Dimensions:Rate Code:Description**

The description for a price or rate.

**terms:termType:sku:Price Dimensions:Rate Code:Unit**

The type of unit that each service uses to measure usage for
billing. For example, Amazon EC2 uses hours, and Amazon S3 uses GB.

**terms:termType:sku:Price Dimensions:Rate Code:Starting Range**

The lower limit of the price tier covered by this price. For
example, 0 GB or 1,001 API operation calls.

**terms:termType:sku:Price Dimensions:Rate Code:Ending Range**

The upper limit of the price tier covered by this price. For
example, 1,000 GB or 10,000 API operation calls.

**terms:termType:sku:Price Dimensions:Rate Code:Price Per Unit**

A calculation of how much a single measured unit for a service
costs.

**terms:termType:sku:Price Dimensions:Rate Code:Price Per Unit:Currency
Code**

A code that indicates the currency for prices for a specific
product.

**terms:termType:sku:Price Dimensions:Rate Code:Price Per Unit:Currency
Rate**

The rate for a product in various supported currencies. For
example, $1.2536 per unit.
