'''
This code automates the converting-process from .stl to .obj and .ply.

Run in terminal: blender --background --this_file.py -- filename.stl filename_converted.obj filename_converted.ply

'''

import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--". +1 because argv[0] is code-filepath

stl_in = argv[0]    # filepath of .stl
obj_out = argv[1]   # filepath to export .obj
ply_out = argv[2]   # filepath to export .ply


# Delete existing objects in case they exist.
try:
    objs = bpy.data.objects
    objs.remove(objs["Cube"], do_unlink=True)
    objs.remove(objs["Camera"], do_unlink=True)
    objs.remove(objs["Lamp"], do_unlink=True)

    # delete objects
    bpy.ops.object.delete()
except:
    pass



bpy.ops.import_mesh.stl(filepath=stl_in, axis_forward='Y', axis_up='Z')     # import .stl
bpy.ops.export_scene.obj(filepath=obj_out, use_blen_objects=True)           # export .obj
bpy.ops.export_mesh.ply(filepath=ply_out, axis_forward='Y', axis_up='Z')    # export .ply