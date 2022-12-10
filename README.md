# version_lister
## Hard pin your dependencies in `requirements.txt`

This is a simple python program or rather script to update `requirements.txt` depending upon its state:
1. Check the dependencies(packages) currently installed in the environment.
2. **(Req.file Present)**:For each value of packages present in environment, update those which were listed already in       `requirements.txt` dependency version.
3. **(Req.file absent)**: For all the values of packages in the environment, list them in `requirements.txt` as it is,
    with dependencies locked.(You may have to manually remove un-necessary values.)
Note : *Hence as a necessity, it requires that project dependencies are already installed with working versions*.
## Aim:
- helping python package authors/owners to **hard pin** their dependencies with the working version installed in their `requirements.txt` file before making it public.

- It is not a complete solution for dependency management in building python projects, nor does it in anyway attempts to become so.

## Getting Started

- #### Install:
    - Activate venv/virtualenv, install through `pip`:
    - `pip install version_lister`
- #### Run:
    - `add-version`
        in the top level working dir where requirements.txt is present.
- **recommended usage** :
    * Before running `add-version` make sure :
        - **All required project dependencies are installed.**
        - **All dependencies are mentioned in the requirements.txt file in any way with or without any semantic versioning.**
        - Failure of first results in requirements.txt updated with un-necessary environment packages and no actual required dependency mentioned.
        - Failure of second results in noisy requirements file where other system packages are mentioned alongside actual dependencies.
## Contribution
- see [issues](https://github.com/azzamzafar/version_lister/issues)
- create [pull requests](https://github.com/azzamzafar/version_lister/pulls)
## License
`version_lister` was created by Azzam Zafar. It is licensed under the terms
of the MIT license.