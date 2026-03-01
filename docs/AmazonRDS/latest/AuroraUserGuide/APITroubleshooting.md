# Troubleshooting applications on Aurora

Amazon RDS provides specific and descriptive errors to help you troubleshoot problems
while interacting with the Amazon RDS API.

###### Topics

- [Retrieving errors](#RetrievingErrors "#RetrievingErrors")
- [Troubleshooting tips](#TroubleshootingTipss "#TroubleshootingTipss")

For information about troubleshooting for Amazon RDS DB instances, see
[Troubleshooting for Amazon Aurora](CHAP_Troubleshooting.md "CHAP_Troubleshooting.md").

## Retrieving errors

Typically, you want your application to check whether a request generated an error
before you spend any time processing results. The easiest way to find out if an
error occurred is to look for an `Error` node in the response from the
Amazon RDS API.

XPath syntax provides a simple way to search for the presence of an
`Error` node. It also provides a relatively easy way to retrieve the
error code and message. The following code snippet uses Perl and the XML::XPath
module to determine if an error occurred during a request. If an error occurred, the
code prints the first error code and message in the response.

```
use XML::XPath;
    my $xp = XML::XPath->new(xml =>$response);
    if ( $xp->find("//Error") )
    {print "There was an error processing your request:\n", " Error code: ",
    $xp->findvalue("//Error[1]/Code"), "\n", " ",
    $xp->findvalue("//Error[1]/Message"), "\n\n"; }
```

## Troubleshooting tips

We recommend the following processes to diagnose and resolve problems with the
Amazon RDS API:

- Verify that Amazon RDS is operating normally in the AWS Region that you're
  targeting by checking [http://status.aws.amazon.com](http://status.aws.amazon.com/ "http://status.aws.amazon.com/").
- Check the structure of your request.

Each Amazon RDS operation has a reference page in the _Amazon RDS API
Reference_. Double-check that you are using parameters
correctly. For ideas about what might be wrong, look at the sample requests
or user scenarios to see if those examples do similar operations.

- Check AWS re:Post.

Amazon RDS has a development community where you can search for solutions
to problems others have experienced along the way. To view the topics, go to
[AWS re:Post](https://repost.aws/ "https://repost.aws/").
