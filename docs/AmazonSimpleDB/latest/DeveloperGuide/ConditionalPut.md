# Performing a Conditional Put

Conditional put enables you to insert or replace values for one or more attributes of an item
if the existing value of an attribute matches a value that you specify.
If the value does not match or is not present, the insert or update is rejected with a 409
(MultiValuedAttribute, ConditionalCheckFailed ) or 404 (AttributeDoesNotExist) error code.

Conditional updates are useful for preventing lost updates when different sources concurrently
write to the same item.

###### Note

Conditional puts can only match single-valued attributes.

## Optimistic Concurrency Control

Applications can implement optimistic concurrency control (OCC) by maintaining a
version number (or timestamp) attribute as part of an item and by performing a conditional
update based on the value of this version number.

To set up optimistic concurrency control, configure each writer to specify the expected name and expected value in
put requests. If the expected value changes between the time the writer reads and writes to that value, the
writer does not perform the update. The writer can then read the update to the value and perform another write
based on the change.

###### Note

All writers must use conditional updates or updates can be lost

In the following example, the application does a conditional update of the item's state and sets
the value to "fuzzy" only if the value of VersionNumber is 30. If another application changes the value of
VersionNumber between this read and write, so that it is no longer 30, the updates fails.

```
https://sdb.amazonaws.com/
?Action=PutAttributes
&DomainName=MyDomain
&ItemName=JumboFez
&Attribute.1.Name=state
&Attribute.1.Value=fuzzy
&Attribute.1.Replace=true
&Attribute.2.Name=VersionNumber
&Attribute.2.Value=31
&Attribute.2.Replace=true
&Expected.1.Name=VersionNumber
&Expected.1.Value=30
&AWSAccessKeyId=[valid access key id]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A05-07%3A00
&Version=2009-04-15
&Signature=[valid signature]
```

If the condition is met, Amazon SimpleDB returns output similar to the following.

```

<PutAttributesResponse>
  <ResponseMetadata>
    <RequestId>490206ce-8292-456c-a00f-61b335eb202b</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</PutAttributesResponse>

```

## Counters

You can also use conditional puts to implement counters. For example, an application might issue
a `GetAttributes` call to retrieve the current page counter for a web page and write the new value
using `PutAttributes` only if no other host has updated the value.

To set up counters, configure each writer to specify the expected name and expected value in
put requests. If the counter value changes between the time the writer reads and writes to that value, the
writer does not update the counter. The writer can then read the counter value and perform another write
based on the change.

###### Note

All writers must use conditional updates or updates can be lost

When updating a counter, you can use eventually consistent or consistent reads. If a stale value is read,
the write is rejected by the system.

If a counter is updated frequently, make sure to re-read the updated counter value on failure.

In the following example, the application updates the counter if the value did not change between the read and the write.
If another application changes the value of PageHits between this read and write, so that it is no longer 121, the updates fails.

```

https://sdb.amazonaws.com/
?Action=PutAttributes
&DomainName=MyDomain
&ItemName=www.fezco.com
&Attribute.1.Name=PageHits
&Attribute.1.Value=122
&Attribute.1.Replace=true
&Expected.1.Name=PageHits
&Expected.1.Value=121
&AWSAccessKeyId=[valid access key id]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A05-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

If the condition is met, Amazon SimpleDB returns output similar to the following.

```

<PutAttributesResponse>
  <ResponseMetadata>
    <RequestId>490206ce-8292-456c-a00f-61b335eb202b</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</PutAttributesResponse>

```

## Existence Check

You can use conditional puts to only put an attribute if it does not exist.

To perform an existence check, specify expected name and set expected exists to false. If the specified attribute
does not exist, Amazon SimpleDB performs the update.

In the following example, Amazon SimpleDB creates the `quantity` attribute and sets its value to
`144` for the `PetiteFez` item, if its `quantity` attribute does not exist.

```

https://sdb.amazonaws.com/
?Action=PutAttributes
&DomainName=MyDomain
&ItemName=PetiteFez
&Attribute.1.Name=quantity
&Attribute.1.Value=144
&Expected.1.Name=quantity
&Expected.1.Exists=false
&AWSAccessKeyId=[valid access key id]
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A05-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

If the condition is met, Amazon SimpleDB returns output similar to the following.

```

<PutAttributesResponse>
  <ResponseMetadata>
    <RequestId>490206ce-8292-456c-a00f-61b335eb202b</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</PutAttributesResponse>

```
