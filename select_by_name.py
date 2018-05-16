# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#  (c) 2018 Dan Pool (dpdp) 
import bpy

# from bpy import context
import os
os.system('cls')

bl_info = {
    "name": "SelectByBasename",
    "author": "Dan Pool (dpdp)",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "description": "Selects all objects with the same base name as the current object",
    "location": "Select > Select by Prefix",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}


class SelectByPrefix(bpy.types.Operator):
    """Select all objects with the same prefix"""
    bl_idname = "object.select_by_prefix"
    bl_label = "Select by Prefix"
    bl_options = {'REGISTER', 'UNDO'}
    global converted

    @classmethod
    def poll(cls, context):
        return ((len(context.selected_objects) > 0)
                and (context.mode == 'OBJECT'))

    def execute(self, context):

        # determine selected material
        sname = context.object.name  # type: object

        if not '_' in sname:
            spreffix = [sname, None]
        else:    
            spreffix = sname.split('_')
            
        for ob in context.scene.objects:
            if not '_' in ob.name:
                preffixes = ob.name, None
            else:
                preffixes = ob.name.split('_')
            if preffixes[0]==spreffix[0]:
                ob.select = True

        return {'FINISHED'}

class SelectBySuffix(bpy.types.Operator):
    """Select all objects with the same suffix"""
    bl_idname = "object.select_by_suffix"
    bl_label = "Select by Suffix"
    bl_options = {'REGISTER', 'UNDO'}
    global converted

    @classmethod
    def poll(cls, context):
        return ((len(context.selected_objects) > 0)
                and (context.mode == 'OBJECT'))

    def execute(self, context):

        # determine selected material
        sname = context.object.name  # type: object

        if not '_' in sname:
            ssuffix = [sname, None]
        else:    
            ssuffix = sname.split('_')
            
        for ob in context.scene.objects:
            if not '_' in ob.name:
                suffixes = ob.name, None
            else:
                suffixes = ob.name.split('_')
            if ssuffix[-1]==suffixes[-1]:
                ob.select = True

        return {'FINISHED'}    



def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_select_object.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_MT_select_object.remove(menu_func)


def menu_func(self, context):
    self.layout.separator()
    self.layout.operator(SelectBySuffix.bl_idname)
    self.layout.operator(SelectByPrefix.bl_idname)
    


if __name__ == "__main__":
    register()
