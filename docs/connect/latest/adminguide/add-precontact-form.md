

# Add a pre-contact or pre-chat form
<a name="add-precontact-form"></a>

You can capture customer information before starting a contact:
+ **Pre-contact form**: Add to capture information from the customer before starting a task or email contact.
+ **Pre-chat form**: Add to capture information from the customer before starting a chat contact.

After you capture the information, you can display it to the agent through the Contact Control Panel (CCP), or use it elsewhere in the flow.

To create the form, you create a custom view and use the connect action button component. For more information on views, see [Build views with the UI builder in Connect Customer](no-code-ui-builder.md).

With the connect action button, you can take in user input from the form and select what action to take when the form is submitted - start a task/email or chat.

## Customizing the form
<a name="configure-contact-form-customization-object"></a>

To customize the form, pass a `contactFormCustomizationObject` in the widget snippet that you add to your webpage.

The following example sets the form title to an `h1` and overrides the messages that appear after a customer submits a pre-contact form.

```
amazon_connect('contactFormCustomizationObject', { 
        header: { 
            hide: false,
            headingLevel: "h1" 
        },
        submitForm: {
            successMessage: "Thank you. We received your request.",
            errorMessage: "We couldn't submit your request. Try again."
        }
});
```

The following table lists the supported customization fields and recommended value constraints.


| Custom layout option | Type | Values | Description | 
| --- | --- | --- | --- | 
| `header.headingLevel` | String | `h1` \| `h2` \| `h3` \| `h4` \| `h5` \| `h6` | Sets the Hypertext Markup Language (HTML) heading level of the form title so that the form fits the heading structure of your webpage for accessibility. Changing the heading level does not change the visual appearance of the title. By default, or if you don't set a supported heading level, the title uses `h2`. | 
| `header.hide` | Boolean | `true` \| `false` | Hides the form header, including the form title and logo. While the widget is open, this option also hides the button that minimizes the widget. The default value is `false`. | 
| `submitForm.successMessage` | String | Any string | Overrides the message that appears after a customer submits a pre-contact form and the task or email contact starts. This message doesn't appear for pre-chat forms. The default message in English is `Thank you. Your form was successfully submitted.` | 
| `submitForm.errorMessage` | String | Any string | Overrides the message that appears when a pre-contact form can't start the task or email contact. This message doesn't appear for pre-chat forms or for field validation errors. The default message in English is `Your form was not successfully submitted. You may have to update some information to match expected values. Please try again.` | 