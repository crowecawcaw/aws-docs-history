# Test a distribution

After you've created your distribution, CloudFront knows where your origin server is, and you
 know the domain name associated with the distribution. To test your distribution, do the following:


1. Wait until your distribution is deployed.




	* View your distribution **Details** in the console. When your distribution is done deploying, the **Last modified** field changes from **Deploying** to a date and time.
2. Create links to your objects with the CloudFront domain name by using the following procedure.
3. Test the links. CloudFront serves the objects to your webpage
 or application.
## Create links to your objects


Use the following procedure to create test links for the objects in your CloudFront web distribution.


###### To create links to objects in a web 
 distribution

1. Copy the following HTML code into a new file, replace 
 `domain-name` with your distribution's domain name, and replace 
 `object-name` with the name of your object.



```
<html>
<head>
	<title>My CloudFront Test</title>
</head>
<body>
	<p>My text content goes here.</p>
	<p><img src="https://`domain-name`/`object-name`" alt="my test image"></p>
</body>
</html>
```

For example, if your domain name were `d111111abcdef8.cloudfront.net` and your 
 object were `image.jpg`, the URL for the link would be:


`https://d111111abcdef8.cloudfront.net/image.jpg`.


If your object is in a folder on your origin server, then the folder must also be 
 included in the URL. For example, if image.jpg were located in the images folder on your 
 origin server, then the URL would be: 


`https://d111111abcdef8.cloudfront.net/images/image.jpg`
2. Save the HTML code in a file that has an .html file name extension.
3. Open your webpage in a browser to ensure that you can see your object.

The browser returns your page with the embedded image file, served from the edge location 
 that CloudFront determined was appropriate to serve the object.
