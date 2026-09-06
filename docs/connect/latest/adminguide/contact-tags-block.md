

# Flow block in Connect Customer: Contact tags
<a name="contact-tags-block"></a>

This topic defines the flow block for creating and applying tags to your contacts.

## Description
<a name="contact-tags-description"></a>
+ Use this block to create and apply user-defined tags (key:value pairs) to your contacts. 
+ You can create up to 6 user-defined tags. 
+ You set a value that can be referenced later in a flow. You can also remove tags in a flow, for example, if the tags aren't relevant to the segment anymore.
+ For more information about how to use tags to obtain a more detailed view of your Connect Customer usage, see [Set up granular billing for a detailed view of your Connect Customer usage](granular-billing.md). 

## Supported channels
<a name="contact-tags-channels"></a>

The following table lists how this block routes a contact who is using the specified channel. 


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | Yes | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="contact-tags-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ All

## Properties
<a name="contact-tags-properties"></a>

The following image shows the **Properties** page of the **Contact tags** block. It is configured to set a tag on the current contact with the key **Department** and the value **Finance**.

![The properties page of the Contact tags block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-contacttags-properties.png)


You can also configure the block to untag a contact, as shown in the following image. 

![The properties page of the Contact tags block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-contacttags-properties-untag.png)


## Configuration tips
<a name="contact-tags-tips"></a>
+ For more information about how Connect Customer processes user-defined tags, see [Things to know about user-defined tags](granular-billing.md#about-user-defined-tags). 

## Configured block
<a name="contact-tags-configured"></a>

The following image shows an example of what this block looks like when it is configured. It has two branches: **Success** and **Error**. 

![A configured Contact tags block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/granularbilling-contacttaggingblock-config.png)
