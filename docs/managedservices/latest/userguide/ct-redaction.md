

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Redacting sensitive information from change types
<a name="ct-redaction"></a>

AMS change type schemas offer a parameter attribute, `"metadata":"ams:sensitive":"true"` that is used for parameters that would contain sensitive information, such as a password. When this attribute is set, the input provided is obscured. Note that you cannot set this parameter attribute; however, if you are working with AMS to create a change type and have a parameter that you would like obscured at input, you can request this.