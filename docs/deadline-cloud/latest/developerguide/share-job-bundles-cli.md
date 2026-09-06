

# Work with shared bundles from the command line
<a name="share-job-bundles-cli"></a>

Use the CLI commands in this section to script bundle operations and to check the state of a queue's bundles while you develop them.

List the bundles shared on the queue:

```
deadline bundle list --queue
```

Print a bundle's name, description, steps, and parameters from its Open Job Description template:

```
deadline bundle info {{my_render_job}} --queue
```

Download a shared bundle to a directory. If the directory already contains a bundle with the same name, the download replaces it:

```
deadline bundle download {{my_render_job}} -o {{~/job-bundles}}
```

Then submit it like any other job bundle:

```
deadline bundle submit {{~/job-bundles/my_render_job}}
```

If you don't pass the `-o` option, the bundle downloads to a local cache and the command prints the path. Downloads are cached, so downloading a bundle that hasn't changed on the queue reuses the local copy.

Hide a bundle from your own listings and from the job bundle browser on your workstation. Hiding is local to your workstation, so the bundle stays on the queue and your teammates still see it. To include hidden bundles when listing, pass `--show-hidden`.

```
deadline bundle hide {{my_render_job}}
deadline bundle unhide {{my_render_job}}
```