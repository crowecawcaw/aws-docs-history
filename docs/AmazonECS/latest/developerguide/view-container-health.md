# Viewing Amazon ECS container health

You can view the container health in the console, and using the API in the
`DescribeTasks` response. For more information, see [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md") in the _Amazon Elastic Container Service API
Reference_.

If you use logging for your container, for example Amazon CloudWatch Logs, you can configure the
health check command to forward the container health output to your logs. Make sure to
use `2&1` to catch both the `stdout` and `stderr`
information. The following example uses `CMD-SHELL` because it requires
shell features like the pipe (`>>`) and logical OR (`||`)
operators:

```
"command": [
     "CMD-SHELL",
     "curl -f http://localhost/ >> /proc/1/fd/1 2>&1  || exit 1"
   ],
```
