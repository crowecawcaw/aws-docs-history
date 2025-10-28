# Build a container image

You can use the `AWS_BATCH_JOB_ARRAY_INDEX` in a job definition in the command
parameter. However, we recommend that you create a container image that uses the variable in an
entrypoint script instead. This section describes how to create such a container image.

###### To build your Docker container image

1. Create a new directory to use as your Docker image workspace and navigate to it.
2. Create a file named `colors.txt` in your workspace directory and paste the following into
   it.

```
red
orange
yellow
green
blue
indigo
violet
```

3. Create a file named `print-color.sh` in your workspace directory and paste the following
   into it.

###### Note

The `LINE` variable is set to the `AWS_BATCH_JOB_ARRAY_INDEX` + 1 because the array
index starts at 0, but line numbers start at 1. The `COLOR` variable is set to the color in
`colors.txt` that's associated with its line number.

```
#!/bin/sh
LINE=$((AWS_BATCH_JOB_ARRAY_INDEX + 1))
COLOR=$(sed -n ${LINE}p /tmp/colors.txt)
echo My favorite color of the rainbow is $COLOR.
```

4. Create a file named `Dockerfile` in your workspace directory and paste
   the following content into it. This Dockerfile copies the previous files to your container and
   sets the entrypoint script to run when the container starts.

```
FROM busybox
COPY print-color.sh /tmp/print-color.sh
COPY colors.txt /tmp/colors.txt
RUN chmod +x /tmp/print-color.sh
ENTRYPOINT /tmp/print-color.sh
```

5. Build your Docker image.

```
`$` `docker build -t print-color .`
```

6. Test your container with the following script. This script sets the
   `AWS_BATCH_JOB_ARRAY_INDEX` variable to 0 locally and then increments it to
   simulate what an array job with seven children does.

```
`$` `AWS_BATCH_JOB_ARRAY_INDEX=0
while [ $AWS_BATCH_JOB_ARRAY_INDEX -le 6 ]
do
 docker run -e AWS_BATCH_JOB_ARRAY_INDEX=$AWS_BATCH_JOB_ARRAY_INDEX print-color
 AWS_BATCH_JOB_ARRAY_INDEX=$((AWS_BATCH_JOB_ARRAY_INDEX + 1))
done`
```

The following is the output.

```
My favorite color of the rainbow is red.
My favorite color of the rainbow is orange.
My favorite color of the rainbow is yellow.
My favorite color of the rainbow is green.
My favorite color of the rainbow is blue.
My favorite color of the rainbow is indigo.
My favorite color of the rainbow is violet.
```
