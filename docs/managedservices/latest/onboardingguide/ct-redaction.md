# Redacting sensitive information from change types

AMS change type schemas offer a parameter attribute, `"metadata":"ams:sensitive":"true"` that is used
for parameters that
would contain sensitive information, such as a password. When this attribute is set, the input provided is obscured.
Note that you cannot set
this parameter attribute; however, if you are working with AMS to create a change type and have a parameter that
you would like obscured at input,
you can request this.
