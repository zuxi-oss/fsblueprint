from fsblueprint.core import create_from_yaml, create_yaml_from_structure

# Test 1: Create structure from YAML
print("=== Test 1: YAML → Structure ===")
create_from_yaml('examples/simple.yaml', './test_output')
print("Structure created in ./test_output")

# Test 2: Generate YAML from structure
print("\n=== Test 2: Structure → YAML ===")
create_yaml_from_structure('./test_output', './generated.yaml')
print("YAML generated as ./generated.yaml")

# Show the generated YAML
print("\n=== Generated YAML content ===")
with open('./generated.yaml', 'r') as f:
    print(f.read())