# Java 1.x: DynamoDBMapper

###### Note

The SDK for Java has two versions: 1.x and 2.x. The end-of-support for 1.x was [announced](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-java-v1-x-on-december-31-2025/ "https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-java-v1-x-on-december-31-2025/") on January 12, 2024. It will and its end-of-support is due on
December 31, 2025. For new development, we highly recommend that you use 2.x.

The AWS SDK for Java provides a `DynamoDBMapper` class, allowing you to map your
client-side classes to Amazon DynamoDB tables. To use `DynamoDBMapper`, you define the
relationship between items in a DynamoDB table and their corresponding object instances in your
code. The `DynamoDBMapper` class enables you to perform various create, read,
update, and delete (CRUD) operations on items, and run queries and scans against
tables.

###### Topics

- [DynamoDBMapper Class](DynamoDBMapper.md "DynamoDBMapper.md")
- [Supported data types for DynamoDBMapper for
  Java](DynamoDBMapper.md "DynamoDBMapper.md")
- [Java Annotations for DynamoDB](DynamoDBMapper.md "DynamoDBMapper.md")
- [Optional configuration settings for
  DynamoDBMapper](DynamoDBMapper.md "DynamoDBMapper.md")
- [DynamoDB and optimistic locking with
  version number](DynamoDBMapper.md "DynamoDBMapper.md")
- [Mapping arbitrary data in
  DynamoDB](DynamoDBMapper.md "DynamoDBMapper.md")
- [DynamoDBMapper examples](DynamoDBMapper.md "DynamoDBMapper.md")

###### Note

The `DynamoDBMapper` class does not allow you to create, update, or delete
tables. To perform those tasks, use the low-level SDK for Java interface instead.

The SDK for Java provides a set of annotation types so that you can map your classes to tables.
For example, consider a `ProductCatalog` table that has `Id` as the
partition key.

```
ProductCatalog(Id, ...)
```

You can map a class in your client application to the `ProductCatalog` table as
shown in the following Java code. This code defines a plain old Java object (POJO) named
`CatalogItem`, which uses annotations to map object fields to DynamoDB attribute
names.

###### Example

```
package com.amazonaws.codesamples;

import java.util.Set;

import software.amazon.dynamodb.datamodeling.DynamoDBAttribute;
import software.amazon.dynamodb.datamodeling.DynamoDBHashKey;
import software.amazon.dynamodb.datamodeling.DynamoDBIgnore;
import software.amazon.dynamodb.datamodeling.DynamoDBTable;

@DynamoDBTable(tableName="ProductCatalog")
public class CatalogItem {

    private Integer id;
    private String title;
    private String ISBN;
    private Set<String> bookAuthors;
    private String someProp;

    @DynamoDBHashKey(attributeName="Id")
    public Integer getId() { return id; }
    public void setId(Integer id) {this.id = id; }

    @DynamoDBAttribute(attributeName="Title")
    public String getTitle() {return title; }
    public void setTitle(String title) { this.title = title; }

    @DynamoDBAttribute(attributeName="ISBN")
    public String getISBN() { return ISBN; }
    public void setISBN(String ISBN) { this.ISBN = ISBN; }

    @DynamoDBAttribute(attributeName="Authors")
    public Set<String> getBookAuthors() { return bookAuthors; }
    public void setBookAuthors(Set<String> bookAuthors) { this.bookAuthors = bookAuthors; }

    @DynamoDBIgnore
    public String getSomeProp() { return someProp; }
    public void setSomeProp(String someProp) { this.someProp = someProp; }
}
```

In the preceding code, the `@DynamoDBTable` annotation maps the
`CatalogItem` class to the `ProductCatalog` table. You can store
individual class instances as items in the table. In the class definition, the
`@DynamoDBHashKey` annotation maps the `Id` property to the
primary key.

By default, the class properties map to the same name attributes in the table. The
properties `Title` and `ISBN` map to the same name attributes in the
table.

The `@DynamoDBAttribute` annotation is optional when the name of the DynamoDB
attribute matches the name of the property declared in the class. When they differ, use this
annotation with the `attributeName` parameter to specify which DynamoDB attribute
this property corresponds to.

In the preceding example, the `@DynamoDBAttribute` annotation is added to each
property to ensure that the property names match exactly with the tables created in a
previous step, and to be consistent with the attribute names used in other code examples in
this guide.

Your class definition can have properties that don't map to any attributes in the table.
You identify these properties by adding the `@DynamoDBIgnore` annotation. In the
preceding example, the `SomeProp` property is marked with the
`@DynamoDBIgnore` annotation. When you upload a `CatalogItem`
instance to the table, your `DynamoDBMapper` instance does not include the
`SomeProp` property. In addition, the mapper does not return this attribute
when you retrieve an item from the table.

After you define your mapping class, you can use `DynamoDBMapper` methods to
write an instance of that class to a corresponding item in the `Catalog` table.
The following code example demonstrates this technique.

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().build();

DynamoDBMapper mapper = new DynamoDBMapper(client);

CatalogItem item = new CatalogItem();
item.setId(102);
item.setTitle("Book 102 Title");
item.setISBN("222-2222222222");
item.setBookAuthors(new HashSet<String>(Arrays.asList("Author 1", "Author 2")));
item.setSomeProp("Test");

mapper.save(item);
```

The following code example shows how to retrieve the item and access some of its
attributes.

```
CatalogItem partitionKey = new CatalogItem();

partitionKey.setId(102);
DynamoDBQueryExpression<CatalogItem> queryExpression = new DynamoDBQueryExpression<CatalogItem>()
    .withHashKeyValues(partitionKey);

List<CatalogItem> itemList = mapper.query(CatalogItem.class, queryExpression);

for (int i = 0; i < itemList.size(); i++) {
    System.out.println(itemList.get(i).getTitle());
    System.out.println(itemList.get(i).getBookAuthors());
}
```

`DynamoDBMapper` offers an intuitive, natural way of working with DynamoDB data
within Java. It also provides several built-in features, such as optimistic locking, ACID
transactions, autogenerated partition key and sort key values, and object versioning.
