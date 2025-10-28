# WSGI servers

Start the profiler based on the configuration for your web server.

## uWSGI

Configure CodeGuru Profiler in your `wsgi.py` file. Then, start your application by
adding the `--enable-threads` and `--lazy-apps` parameters to your
uWSGI startup configuration. These are required for CodeGuru Profiler to run in your uWSGI
applications.

```
uwsgi --http :8000 --chdir . --wsgi-file wsgi.py --enable-threads --lazy-apps --workers=4
```

## gunicorn

Configure CodeGuru Profiler in your `post-fork` method. Then start the application as
usual.

```
def post_fork(server, worker):
    server.log.info('Starting profiler for {} in {}'.format(os.getpid(), threading.get_ident()))
    worker.profiler = Profiler(profiling_group_name='MyProfilingGroup')
    worker.profiler.start()
    server.log.info('Profiler started running for worker pid {}: master pid {}.'.format(os.getpid(), worker.ppid))
```

## Apache

For Apache (httpd) with `mod_wsgi` module, use the same wsgi configuration.
Make sure the `wsgi.py` file is configured to be visible in the
`httpd.conf` file.

```
<Directory [to_be_replaced]>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
```

Start your application with `apachectl start`.
