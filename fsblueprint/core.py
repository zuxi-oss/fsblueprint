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

def create_yaml_from_structure(source_dir, output_yaml):
    """Generate YAML blueprint from existing directory structure"""
    structure = _scan_structure(Path(source_dir))
    
    with open(output_yaml, 'w') as f:
        yaml.dump(structure, f, default_flow_style=False, sort_keys=False)

def _scan_structure(path):
    """Recursively scan directory structure"""
    if not path.exists():
        raise FileNotFoundError(f"Path {path} does not exist")
    
    if path.is_file():
        return ""  # Empty content for now
    
    result = {}
    
    # Get all items and sort them (directories first, then files)
    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
    
    for item in items:
        if item.is_dir():
            result[item.name] = _scan_structure(item)
        else:
            result[item.name] = ""  # Empty content for now
    
    return result