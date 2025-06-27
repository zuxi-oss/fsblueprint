from fsblueprint.core import create_from_yaml

# Test the basic functionality
create_from_yaml('./examples/simple.yaml', '.')

# List what was created
import os
for root, dirs, files in os.walk('./test_output'):
    level = root.replace('./test_output', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f'{subindent}{file}')