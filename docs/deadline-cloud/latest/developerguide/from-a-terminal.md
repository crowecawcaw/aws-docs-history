# Submit a job to Deadline Cloud from a terminal

Using only a job bundle and the Deadline Cloud CLI, you or your more technical users can rapidly
iterate on writing job bundles to test submitting a job. Use the following command to submit a
job bundle:

```
deadline bundle submit <path-to-job-bundle>
```

If you submit a job bundle with parameters that do not have defaults in the bundle, you
can specify them with the `-p` / `--parameter` option.

```
deadline bundle submit <path-to-job-bundle> -p <parameter-name>=<parameter-value> -p ...
```

For a complete list of the available options, run the help command:

```
deadline bundle submit --help
```

## Submit a job to Deadline Cloud using a GUI

The Deadline Cloud CLI also comes with a graphical user interface that enables users to see the
parameters they must provide before submitting a job. If your users prefer not to interact with
the command line, you can write a desktop shortcut that opens a dialog to submit a specific job
bundle:

```
deadline bundle gui-submit <path-to-job-bundle>
```

Use the `--browse` option can so the user can select a job bundle:

```
deadline bundle gui-submit --browse
```

For a complete list of available options, run the help command:

```
deadline bundle gui-submit --help
```
