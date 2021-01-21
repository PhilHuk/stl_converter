# stl_converter
Python file that uses Blender to convert .stl to .obj and .ply

# Prerequesities
1. Install blender. E.g.: sudo apt-get install blender
2. Create virtual environment. E.g. conda create -n stl_converter python=3.8
3. Activate environment: conda activate stl_converter
3. Install blender-python api using conda:  conda install -c kitsune.one python-blender

# Run Code
1. Change to directory where stl_converter.py is located.
2. In terminal run: blender --background --python stl_converter.py -- <filepath_to_stl>.stl <filename>.obj <filename>.ply
  
# Settings
It is possible to change coordinates of the objects coordinate system. See blender docs for more information. 
https://docs.blender.org/api/current/bpy.ops.export_scene.html
https://docs.blender.org/api/current/bpy.ops.export_mesh.html

