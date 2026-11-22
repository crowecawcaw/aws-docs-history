

# Building Lambda Web Functions with Python

Python Web Functions support applications that use the Asynchronous Server Gateway Interface (ASGI) or Web Server Gateway Interface (WSGI). Put your application in `main.py` and expose it as a callable named `app`. Lambda loads `main:app` by default and manages the HTTP server for your application.

## Application entry point
<a name="web-functions-python-entrypoint"></a>

To use another module or callable, set `AWS_LAMBDA_PYTHON_ENTRYPOINT` in the revision's environment variables. Use `{{module}}:{{callable}}` without the `.py` extension. For example, `api:application` loads `application` from `api.py`.

Lambda automatically detects whether the callable uses ASGI or WSGI. You can override the automatic detection to specify the interface explicitly by prefixing the entry point:
+ `asgi:api:application`
+ `wsgi:api:application`

## Web frameworks
<a name="web-functions-python-frameworks"></a>

ASGI frameworks include FastAPI and Starlette. Flask uses WSGI, and Django supports both interfaces. You don't need to package an HTTP server solely to run these applications on Lambda.

The following FastAPI application uses the default `main:app` entry point:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-world")
async def hello_world():
    return {"message": "Hello from Lambda Web Functions"}
```

## Package dependencies
<a name="web-functions-python-dependencies"></a>

Include your web framework and all other dependencies that your application imports in the .zip deployment package. Lambda expects `main.py` and all of your dependencies at the root of the .zip file. For how to build and upload the archive, see [Web Function deployment package](web-functions-configuration.md#web-functions-configuration-deployment-package).

## Concurrent requests
<a name="web-functions-python-concurrency"></a>

Consider the following behavior when your application serves concurrent requests:

**Concurrency model**  
An ASGI application handles multiple concurrent requests on a single event loop with `async`/`await`. While one request waits for I/O, the event loop can serve another request. A WSGI application handles concurrent requests in a pool of worker threads, with each request running in its own thread.

**Avoid blocking the event loop**  
Synchronous network, file-system, and CPU-intensive calls inside an asynchronous endpoint block the event loop. Use asynchronous I/O for these endpoints. When you create a synchronous endpoint using `def` instead of `async def`, ASGI frameworks such as FastAPI and Starlette can run the endpoint in a thread pool. You can also use WSGI for a synchronous application.

**Thread safety**  
Concurrent WSGI requests can run in parallel threads that share application state and module-level objects. An ASGI application shares state across the requests on its event loop, and across threads when the framework runs a synchronous endpoint in a thread pool. In both cases, use thread-safe handling of shared mutable state and resources.

**Request isolation**  
Avoid storing request-specific data in global variables. Use request-scoped framework context instead. If your application keeps shared mutable state globally, make access concurrency safe.

For information about configuring concurrency, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).

## How Lambda routes requests to your application
<a name="web-functions-python-routing"></a>

Lambda manages the Python HTTP server and passes each request to your application through ASGI or WSGI. Your application doesn't start an HTTP server or read `AWS_LAMBDA_HTTP_ENDPOINT`.

## Logging
<a name="web-functions-python-logging"></a>

Log entries from concurrent requests can be interleaved. When you use the Python standard library `logging` module, Lambda writes structured JSON log events and includes `requestId` for logs emitted while processing a request. Use this field to correlate entries for one request. For more information, see [Web Function logs in Amazon CloudWatch Logs](web-functions-logging.md).