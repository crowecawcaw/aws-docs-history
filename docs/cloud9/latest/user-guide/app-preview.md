AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Previewing running applications in the AWS Cloud9 IDE

You can use the AWS Cloud9 Integrated Development Environment (IDE) to preview a running application from within the
 IDE.


## Run an application


Before you can preview your application from within the IDE, your application must be
 running in the AWS Cloud9 development environment. It must use HTTP over the following ports:



* `8080`
* `8081`
* `8082`

All of the above ports must use the IP address of `127.0.0.1` `localhost`, or `0.0.0.0`.


###### Note

You aren't required to run your application using HTTP over port `8080`,
 `8081`, or `8082` with the IP address of
 `127.0.0.1`, `localhost`, or `0.0.0.0`. However, if you
 don't do so, you can't preview your running application from within the IDE.


###### Note

The preview application is run within the IDE and is loaded inside an iframe
 element. Some application servers might by default block requests that come from iframe
 elements, such as the X-Frame-Options header. If your preview application isn't
 displayed in the preview tab, make sure that your application server doesn't prohibit
 displaying the content in iframes. 


To write code to run your application on a specific port and IP address, see your
 application's documentation.


To run your application, see [Run Your
 Code](build-run-debug.md#build-run-debug-run "build-run-debug.md#build-run-debug-run").


To test this behavior, add the following JavaScript code to a file that's named
 `server.js` in the root of your environment. This code runs a server using
 a file that's named Node.js.


###### Note

In the following example, `text/html` is the `Content-Type` of
 the returned content. To return the content in a different format, specify a different
 `Content-Type`. For example, you can specify `text/css` for a
 CSS file format.



```
var http = require('http');
var fs = require('fs');
var url = require('url');

http.createServer( function (request, response) {
  var pathname = url.parse(request.url).pathname;
  console.log("Trying to find '" + pathname.substr(1) + "'...");

  fs.readFile(pathname.substr(1), function (err, data) {
    if (err) {
      response.writeHead(404, {'Content-Type': 'text/html'});
      response.write("ERROR: Cannot find '" + pathname.substr(1) + "'.");
      console.log("ERROR: Cannot find '" + pathname.substr(1) + "'.");
    } else {
      console.log("Found '" + pathname.substr(1) + "'.");
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(data.toString());
    }
    response.end();
  });
}).listen(8080, 'localhost'); // Or 8081 or 8082 instead of 8080. Or '127.0.0.1' instead of 'localhost'.
```

In the root of your environment, you can add the following Python code to a file with a name
 such as `server.py`. In the following example, a server is run using
 Python.



```
import os
import http.server
import socketserver

ip = 'localhost' # Or '127.0.0.1' instead of 'localhost'.
port = '8080' # Or '8081' or '8082' instead of '8080'.
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((ip, int(port)), Handler)
httpd.serve_forever()
```

In the root of your environment, add the following HTML code to a file that's named
 `index.html`.



```
<html>
  <head>
    <title>Hello Home Page</title>
  </head>
  <body>
    <p style="font-family:Arial;color:blue">Hello, World!</p>
  </body>
</html>
```

To see the HTML output of this file on the application preview tab, run
 `server.js` with Node.js or `server.py` file with
 Python. Then, follow the steps in the next section to preview it. On the application
 preview tab, add `/index.html` to the end of the URL, and then press
 `Enter`.


## Preview a running application


Before you preview your application, confirm the following:



* Your application runs using the HTTP protocol over port `8080`,
 `8081`, or `8082`.
* Your application's IP address in the environment is `127.0.0.1`,
 `localhost`, or `0.0.0.0`.
* Your application code file is open and active in the AWS Cloud9 IDE.

After you confirm all of these details, choose one of the following options from the
 menu bar:



* **Preview, Preview Running Application**
* **Tools, Preview, Preview Running Application**

Either one of these options opens an application preview tab within the environment, and then
 displays the application's output on the tab.


###### Note

If the application preview tab displays an error or is blank, follow the troubleshooting
 steps in [Application preview tab displays an error
 or is blank](troubleshooting.md#troubleshooting-app-preview "troubleshooting.md#troubleshooting-app-preview"). If when you attempt to preview an
 application or file, you get the following notice *"Preview functionality is
 disabled because your browser has third-party cookies disabled"*, follow
 the troubleshooting steps in [Application preview or file preview notice:
 "Third-party cookies disabled"](troubleshooting.md#troubleshooting-preview "troubleshooting.md#troubleshooting-preview").


###### Note

If the application isn't already running, an error appears on the application preview
 tab. To resolve this issue, run or restart the application, and then choose the menu bar
 command again.

Suppose that, for example, your application can't run on any of the ports or IPs
 mentioned. Or, your application must run on more than one of these ports at the same
 time. For example, your application must run on ports `8080` and
 `3000` at the same time. If that's the case, then the application preview
 tab might display an error or might be blank. This is because the application preview
 tab within the environment works only with the preceding ports and IPs. Moreover, the
 application works with only a single port at a time.

We don't recommend sharing the URL in the application preview tab with others. (The
 URL is in the following format:
 `https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`.
 In this format, `12a34567b8cd9012345ef67abcd890e1` is the ID that AWS Cloud9
 assigns to the environment. `us-east-2` is the ID for the AWS Region for the
 environment.) This URL works only when the IDE for the environment is open and the application is
 running in the same web browser.

If you attempt to visit the IP of `127.0.0.1`, `localhost`, or
 `0.0.0.0` by using the application preview tab in the IDE or in a
 separate web browser tab outside of the IDE, the AWS Cloud9 IDE by default attempts to go to
 your local computer, instead of the instance or your own server that's connected to the
 environment.


For instructions on how to provide others with a preview of your running application
 outside of the IDE, see [Share a running application over the internet](app-preview-share.md "app-preview-share.md").
