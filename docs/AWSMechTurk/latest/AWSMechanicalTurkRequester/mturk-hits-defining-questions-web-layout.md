# Requester website layouts

If you have an existing task you created using the Mechanical Turk requester website, you can
create HITs by referencing the `LayoutId` for that task and avoiding the need to
provide a question value. To find the `LayoutId`, navigate to your `Project List` on the
requester website and select the name of the project you want to use. A box pops up showing
the **HIT Type ID**, **Layout ID**, and **Layout
Parameters** that you can reference.

As shown in the following code example, the definition also includes the template
parameters that are defined within the HTML. When you create a HIT, you need to pass both
the `HITLayoutId` and values for the parameters that are defined.

```

{
  ...,
  HITLayoutId: "3O2UWD6SNTXSG9Z4I77HMZAX0U6499",
  HITLayoutParameters: [
    {
      "Name": "image_url",
      "Value": " https://my-bucket.s3.amazonaws.com/img1234.jpg "
    }
  ]
}
 

```

More detail on creating HITs with these values can be found in [Creating HITs](mturk-creating-hits.md "mturk-creating-hits.md").
