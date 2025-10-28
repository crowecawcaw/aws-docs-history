# Add or remove AWS Direct Connect virtual interface tags

Tags provide a way to identify the virtual interface. You can add or remove a tag using either the AWS Direct Connect console or using the command line or API if you are
the account owner for the virtual interface.

###### To add or remove a virtual interface tag

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Virtual Interfaces**.
3. Select the virtual interface and then choose
   **Edit**.
4. Add or remove a tag.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.[Remove a tag] Next to the tag, choose **Remove tag**.

5. Choose **Edit virtual interface**.

###### To add a tag or remove a tag using the command line

- [tag-resource](../../../cli/latest/reference/directconnect/tag-resource.md "../../../cli/latest/reference/directconnect/tag-resource.md") (AWS CLI)
- [untag-resource](../../../cli/latest/reference/directconnect/untag-resource.md "../../../cli/latest/reference/directconnect/untag-resource.md") (AWS CLI)
