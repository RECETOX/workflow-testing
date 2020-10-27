# Galaxy Workflow Testing
[![GitHub license](https://img.shields.io/github/license/RECETOX/workflow-testing?logoColor=lightgrey&style=plastic)](https://github.com/RECETOX/workflow-testing/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/RECETOX/workflow-testing?style=plastic)](https://github.com/RECETOX/workflow-testing/issues)
[![GitHub forks](https://img.shields.io/github/forks/RECETOX/workflow-testing?style=plastic)](https://github.com/RECETOX/workflow-testing/network)
[![Actions Status](https://github.com/RECETOX/workflow-testing/workflows/Galaxy%20Workflows%20Testing%20for%20Push%20and%20PR/badge.svg)](https://github.com/RECETOX/workflow-testing/actions)
[![Actions Status](https://github.com/RECETOX/workflow-testing/workflows/Weekly%20workflow%20testing/badge.svg)](https://github.com/RECETOX/workflow-testing/actions)

This repository runs automated tests of several workflows against a specific Galaxy server.

## Instructions
If planemo test is called on a Galaxy workflow called ref-rnaseq.ga, tests should be defined in ref-rnaseq-tests.yml.
How to create workflow test(s) can be found at the official source of 
[Planemo](https://planemo.readthedocs.io/en/latest/test_format.html#job).


## Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/RECETOX/workflow-testing.


## TODO's
- Add linting for *-test.yml (low priority)
- Delete user histories periodically (medium priority)
- Don't fail the pipeline when any workflow fails (low priority)
