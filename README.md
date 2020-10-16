# Galaxy Workflow Testing

This repository runs automated tests of several workflows against various Galaxy servers.

## Testing

We are [automatically running](https://build.galaxyproject.eu/job/usegalaxy-eu/job/workflow-testing/) these workflows against UseGalaxy.eu, [and we can test against your server too!](https://github.com/usegalaxy-eu/workflow-testing/issues/new)

## Contributing

An introduction to workflow testing and a tutorial can be found at the [Galaxy Training Network](https://galaxyproject.github.io/training-material/topics/contributing/tutorials/create-new-tutorial-technical/tutorial.html#testing-the-workflow-recommended).

## About

Based off of [jmchilton's template](https://github.com/jmchilton/planemo-workflow-test-template), except running tests against UseGalaxy.eu

## Pretty-printing Worfklow JSON

You can use the command line tool `jq` to pretty-print the workflow .ga files:

```console
cat wf.ga | jq . -S > out.ga
```

or this webservice: https://jsonformatter.org/
