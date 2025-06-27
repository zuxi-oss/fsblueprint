# fsblueprint

**fsblueprint** is a Python utility for generating file and folder structures from YAML blueprints—and for creating blueprints from existing directory structures. Define complex directory and file layouts (including file contents) in a simple YAML format, and automatically create them on disk, or extract a YAML blueprint from any folder.

## Features

- Define nested directories and files in YAML
- Optionally specify file contents directly in the YAML
- Scaffold new projects or codebases from blueprints
- Generate a YAML blueprint from an existing directory structure

## Installation

Clone the repository and install dependencies:

```sh
git clone https://github.com/yourusername/fsblueprint.git
cd fsblueprint
pip install -r requirements.txt
```

Or, if using `pyproject.toml`:

```sh
pip install .
```

## Usage

### Create structure from YAML

```python
from fsblueprint.core import create_from_yaml

create_from_yaml('examples/simple.yaml', 'output_directory')
```

### Generate YAML blueprint from a directory

```python
from fsblueprint.core import blueprint_from_dir

blueprint = blueprint_from_dir('some_directory')
print(blueprint)
```

## Example YAML

```yaml
project:
  src:
    main.py: ""
    utils:
      helper.py: ""
  README.md: ""
  tests: {}
```

## License

MIT License
