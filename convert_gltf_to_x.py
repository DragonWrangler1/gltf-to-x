import sys
import os
import subprocess

def convert_gltf_to_x(input_file, output_file):
    try:
        subprocess.run(['assimp', 'export', input_file, output_file], check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_gltf_to_x.py <input.gltf> <output.x>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_gltf_to_x(input_file, output_file)
