import os
import yaml
from pathlib import Path

def create_from_yaml(yaml_file, target_dir="."):
    """Create folder/file structure from YAML"""
    with open(yaml_file, 'r') as f:
        structure = yaml.safe_load(f)
        print(structure)
    
    _create_structure(structure, Path(target_dir))

def _create_structure(structure, base_path):
    """Recursively create structure"""
    for name, content in structure.items():
        path = base_path / name
        
        if isinstance(content, dict):
            # It's a directory
            path.mkdir(parents=True, exist_ok=True)
            _create_structure(content, path)
        else:
            # It's a file - create empty for now
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()  # Creates empty file