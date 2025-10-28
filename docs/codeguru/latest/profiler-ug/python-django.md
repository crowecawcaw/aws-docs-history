# Django

Start the profiler in your settings file. This is usually the file that you’re setting
for `DJANGO_SETTINGS_MODULE`. Then, start your application as usual.

The following is an example that you can add to `settings.py`

```
from codeguru_profiler_agent import Profiler
Profiler(profiling_group_name='MyProfilingGroup').start()
```

Set the following in your `wsgi.py` file. This example is for a module named
`mysite`. Your files may be in a different location.

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
```

Set the following in your `settings.py` file.

```
Profiler(profiling_group_name='MyProfilingGroup').start()
```
