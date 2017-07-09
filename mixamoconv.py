# -*- coding: utf-8 -*-

'''
    Copyright (C) 2017  Antonio Aloisio
  
    Created by Antonio Aloisio
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import bpy
import os

mixamo2ue = {
"Hips": "pelvis",
"Spine": "spine_01", 
"Spine1": "spine_02", 
"Spine2": "spine_03", 
"Neck": "neck_01", 
"Head": "head", 
"HeadTop_End": "head_end", 
"LeftShoulder": "clavicle_l", 
"LeftArm": "upperarm_l", 
"LeftForeArm": "lowerarm_l", 
"LeftHand": "hand_l",
"LeftHandThumb1": "thumb_01_l", 
"LeftHandThumb2": "thumb_02_l", 
"LeftHandThumb3": "thumb_03_l", 
"LeftHandThumb4": "thumb_04_l", 
"LeftHandIndex1": "index_01_l", 
"LeftHandIndex2": "index_02_l", 
"LeftHandIndex3": "index_03_l", 
"LeftHandIndex4": "index_04_l",
"LeftHandMiddle1": "middle_01_l", 
"LeftHandMiddle2": "middle_02_l", 
"LeftHandMiddle3": "middle_03_l", 
"LeftHandMiddle4": "middle_04_l", 
"LeftHandRing1": "ring_01_l", 
"LeftHandRing2": "ring_02_l", 
"LeftHandRing3": "ring_03_l", 
"LeftHandRing4": "ring_04_l", 
"LeftHandPinky1": "pinky_01_l", 
"LeftHandPinky2": "pinky_02_l", 
"LeftHandPinky3": "pinky_03_l", 
"LeftHandPinky4": "pinky_04_l",

"RightShoulder": "clavicle_r", 
"RightArm": "upperarm_r", 
"RightForeArm": "lowerarm_r", 
"RightHand": "hand_r",
"RightHandThumb1": "thumb_01_r", 
"RightHandThumb2": "thumb_02_r", 
"RightHandThumb3": "thumb_03_r", 
"RightHandThumb4": "thumb_04_r", 
"RightHandIndex1": "index_01_r", 
"RightHandIndex2": "index_02_r", 
"RightHandIndex3": "index_03_r", 
"RightHandIndex4": "index_04_r", 
"RightHandMiddle1": "middle_01_r", 
"RightHandMiddle2": "middle_02_r",
"RightHandMiddle3": "middle_03_r", 
"RightHandMiddle4": "middle_04_r", 
"RightHandRing1": "ring_01_r", 
"RightHandRing2": "ring_02_r", 
"RightHandRing3": "ring_03_r", 
"RightHandRing4": "ring_04_r", 
"RightHandPinky1": "pinky_01_r", 
"RightHandPinky2": "pinky_02_r", 
"RightHandPinky3": "pinky_03_r", 
"RightHandPinky4": "pinky_04_r",

"LeftUpLeg": "thigh_l", 
"LeftLeg": "calf_l", 
"LeftFoot": "foot_l", 
"LeftToeBase": "ball_l", 
"LeftToe_End": "toe_end_l",

"RightUpLeg": "thigh_r", 
"RightLeg": "calf_r", 
"RightFoot": "foot_r", 
"RightToeBase": "ball_r", 
"RightToe_End": "toe_end_r"
}

def removeAllDataBlocks():
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete(use_global=True)

  for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh, do_unlink=True)
  for material in bpy.data.materials:
    bpy.data.materials.remove(material, do_unlink=True)
  for action in bpy.data.actions:
    bpy.data.actions.remove(action, do_unlink=True)

def getArmature(objects):
  for a in objects:
    if a.type == 'ARMATURE':
      return a

def exportFBX():
  bpy.ops.export_scene.fbx(filepath=dest_dir + file.name, use_selection=False)
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete(use_global=False)
  print("%d file converted")

def remove_prefix(text, prefix):
  if text.startswith(prefix):
    return text[len(prefix):]
  return text  # or whatever

def setup_scene():
  bpy.context.space_data.context = 'SCENE'
  bpy.context.scene.system = 'METRIC'
  bpy.context.scene.scale_length = 0.01


def create_root_bone():
  bpy.context.space_data.context = 'OBJECT'
  bpy.context.object.name = "Root"
  
armature = getArmature(bpy.context.selected_objects)
create_root_bone()

bones=armature.pose.bones

for x in bones:
    oldName = remove_prefix(x.name, "mixamorig:")
    if oldName in mixamo2ue.keys():
      x.name = mixamo2ue[oldName]
    else:
      print("Cannot find bone " + oldName)
