import bpy
from bpy.app.handlers import persistent

bl_info = {
    "name": "Extra Mix Nodes",
    "description": "Adds extra varieties of the Mix node, with additional color inputs, allowing for blending of more than just 2 textures",
    "author": "Theanine3D",
    "version": (1, 0, 1),
    "blender": (4, 0, 0),
    "category": "Node",
    "location": "Shader Editor",
    "support": "COMMUNITY"
}

groups_to_add = ["Mix Color (3-Sequential)",
                 "Mix Color (4-Sequential)",
                 "Mix Color (5-Sequential)",
                 "Mix Color (Splat, RGB)",
                 "Mix Color (Splat, RGBA)"]

@persistent
def add_mix_nodes(dummy):

    for group_name in groups_to_add:

        if group_name not in bpy.data.node_groups.keys() and group_name == "Mix Color (3-Sequential)":

            node_group = bpy.data.node_groups.new(name="Mix Color (3-Sequential)", type="ShaderNodeTree")
            node_group.use_fake_user = True

            # Create group inputs
            group_inputs_node = node_group.nodes.new("NodeGroupInput")
            group_inputs_node.location = (-600, 0)
            group_inputs_node.width = 180.0
            interface = node_group.interface
            a_input = interface.new_socket("A", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            b_input = interface.new_socket("B", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            c_input = interface.new_socket("C", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            a_input.default_value, b_input.default_value, c_input.default_value = (0,0,0,1), (0,0,0,1), (0,0,0,1)
            factor_input = interface.new_socket("Factor", description="", in_out='INPUT', socket_type='NodeSocketFloat', parent=None)
            factor_input.default_value = 0.5
            factor_input.min_value = 0.0
            factor_input.max_value = 1.0
            factor_input.subtype = "FACTOR"

            # Create group outputs
            group_outputs_node = node_group.nodes.new("NodeGroupOutput")
            group_outputs_node.location = (600, 0)
            group_output = interface.new_socket("Result", description="", in_out='OUTPUT', socket_type='NodeSocketColor', parent=None)

            # Add internal nodes
            mix_node_1 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_1.location = (0, 100)
            mix_node_1.use_clamp = True
            mix_node_1.blend_type = 'MIX'

            mix_node_2 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_2.location = (200, 100)
            mix_node_2.use_clamp = True
            mix_node_2.blend_type = 'MIX'

            map_range_1 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_1.location = (-200, -100)
            map_range_1.inputs[1].default_value = 0.0
            map_range_1.inputs[2].default_value = 0.5
            map_range_1.inputs[3].default_value = 0.0
            map_range_1.inputs[4].default_value = 1.0
            map_range_1.clamp = True

            map_range_2 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_2.location = (-200, -325)
            map_range_2.inputs[1].default_value = 0.5
            map_range_2.inputs[2].default_value = 1.0
            map_range_2.inputs[3].default_value = 0.0
            map_range_2.inputs[4].default_value = 1.0
            map_range_2.clamp = True

            # Link nodes
            links = node_group.links
            links.new(group_inputs_node.outputs['A'], mix_node_1.inputs[1])
            links.new(group_inputs_node.outputs['B'], mix_node_1.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_1.inputs[0])
            links.new(map_range_1.outputs[0], mix_node_1.inputs[0])

            links.new(mix_node_1.outputs[0], mix_node_2.inputs[1])
            links.new(group_inputs_node.outputs['C'], mix_node_2.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_2.inputs[0])
            links.new(map_range_2.outputs[0], mix_node_2.inputs[0])

            links.new(mix_node_2.outputs[0], group_outputs_node.inputs['Result'])

        if group_name not in bpy.data.node_groups.keys() and group_name == "Mix Color (4-Sequential)":

            node_group = bpy.data.node_groups.new(name="Mix Color (4-Sequential)", type="ShaderNodeTree")
            node_group.use_fake_user = True

            # Create group inputs
            group_inputs_node = node_group.nodes.new("NodeGroupInput")
            group_inputs_node.location = (-600, 0)

            interface = node_group.interface
            a_input = interface.new_socket("A", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            b_input = interface.new_socket("B", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            c_input = interface.new_socket("C", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            d_input = interface.new_socket("D", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            a_input.default_value, b_input.default_value, c_input.default_value, d_input.default_value = (0,0,0,1), (0,0,0,1), (0,0,0,1), (0,0,0,1)
            factor_input = interface.new_socket("Factor", description="", in_out='INPUT', socket_type='NodeSocketFloat', parent=None)
            factor_input.default_value = 0.5
            factor_input.min_value = 0.0
            factor_input.max_value = 1.0
            factor_input.subtype = "FACTOR"

            # Create group outputs
            group_outputs_node = node_group.nodes.new("NodeGroupOutput")
            group_outputs_node.location = (700, 0)
            group_output = interface.new_socket("Result", description="", in_out='OUTPUT', socket_type='NodeSocketColor', parent=None)

            # Add internal nodes
            mix_node_1 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_1.location = (0, 100)
            mix_node_1.use_clamp = True
            mix_node_1.blend_type = 'MIX'

            mix_node_2 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_2.location = (200, 100)
            mix_node_2.use_clamp = True
            mix_node_2.blend_type = 'MIX'

            mix_node_3 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_3.location = (400, 100)
            mix_node_3.use_clamp = True
            mix_node_3.blend_type = 'MIX'

            map_range_1 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_1.location = (-200, -100)
            map_range_1.inputs[1].default_value = 0.0
            map_range_1.inputs[2].default_value = 0.333
            map_range_1.inputs[3].default_value = 0.0
            map_range_1.inputs[4].default_value = 1.0
            map_range_1.clamp = True

            map_range_2 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_2.location = (-200, -325)
            map_range_2.inputs[1].default_value = 0.333
            map_range_2.inputs[2].default_value = 0.666
            map_range_2.inputs[3].default_value = 0.0
            map_range_2.inputs[4].default_value = 1.0
            map_range_2.clamp = True

            map_range_3 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_3.location = (-200, -525)
            map_range_3.inputs[1].default_value = 0.666
            map_range_3.inputs[2].default_value = 1.0
            map_range_3.inputs[3].default_value = 0.0
            map_range_3.inputs[4].default_value = 1.0
            map_range_3.clamp = True

            # Link nodes
            links = node_group.links
            links.new(group_inputs_node.outputs['A'], mix_node_1.inputs[1])
            links.new(group_inputs_node.outputs['B'], mix_node_1.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_1.inputs[0])
            links.new(map_range_1.outputs[0], mix_node_1.inputs[0])

            links.new(mix_node_1.outputs[0], mix_node_2.inputs[1])
            links.new(group_inputs_node.outputs['C'], mix_node_2.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_2.inputs[0])
            links.new(map_range_2.outputs[0], mix_node_2.inputs[0])

            links.new(mix_node_2.outputs[0], mix_node_3.inputs[1])
            links.new(group_inputs_node.outputs['D'], mix_node_3.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_3.inputs[0])
            links.new(map_range_3.outputs[0], mix_node_3.inputs[0])

            links.new(mix_node_3.outputs[0], group_outputs_node.inputs['Result'])

        if group_name not in bpy.data.node_groups.keys() and group_name == "Mix Color (5-Sequential)":

            node_group = bpy.data.node_groups.new(name="Mix Color (5-Sequential)", type="ShaderNodeTree")
            node_group.use_fake_user = True

            # Create group inputs
            group_inputs_node = node_group.nodes.new("NodeGroupInput")
            group_inputs_node.location = (-600, 0)

            interface = node_group.interface
            a_input = interface.new_socket("A", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            b_input = interface.new_socket("B", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            c_input = interface.new_socket("C", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            d_input = interface.new_socket("D", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            e_input = interface.new_socket("E", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            a_input.default_value, b_input.default_value, c_input.default_value, d_input.default_value, e_input.default_value = (0,0,0,1), (0,0,0,1), (0,0,0,1), (0,0,0,1), (0,0,0,1)
            factor_input = interface.new_socket("Factor", description="", in_out='INPUT', socket_type='NodeSocketFloat', parent=None)
            factor_input.default_value = 0.5
            factor_input.min_value = 0.0
            factor_input.max_value = 1.0
            factor_input.subtype = "FACTOR"

            # Create group outputs
            group_outputs_node = node_group.nodes.new("NodeGroupOutput")
            group_outputs_node.location = (800, 0)
            group_output = interface.new_socket("Result", description="", in_out='OUTPUT', socket_type='NodeSocketColor', parent=None)

            # Add internal nodes
            mix_node_1 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_1.location = (0, 100)
            mix_node_1.use_clamp = True
            mix_node_1.blend_type = 'MIX'

            mix_node_2 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_2.location = (200, 100)
            mix_node_2.use_clamp = True
            mix_node_2.blend_type = 'MIX'

            mix_node_3 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_3.location = (400, 100)
            mix_node_3.use_clamp = True
            mix_node_3.blend_type = 'MIX'

            mix_node_4 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_4.location = (600, 100)
            mix_node_4.use_clamp = True
            mix_node_4.blend_type = 'MIX'

            map_range_1 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_1.location = (-200, -100)
            map_range_1.inputs[1].default_value = 0.0
            map_range_1.inputs[2].default_value = 0.25
            map_range_1.inputs[3].default_value = 0.0
            map_range_1.inputs[4].default_value = 1.0
            map_range_1.clamp = True

            map_range_2 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_2.location = (-200, -325)
            map_range_2.inputs[1].default_value = 0.25
            map_range_2.inputs[2].default_value = 0.5
            map_range_2.inputs[3].default_value = 0.0
            map_range_2.inputs[4].default_value = 1.0
            map_range_2.clamp = True

            map_range_3 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_3.location = (-200, -525)
            map_range_3.inputs[1].default_value = 0.5
            map_range_3.inputs[2].default_value = 0.75
            map_range_3.inputs[3].default_value = 0.0
            map_range_3.inputs[4].default_value = 1.0
            map_range_3.clamp = True

            map_range_4 = node_group.nodes.new(type="ShaderNodeMapRange")
            map_range_4.location = (-200, -725)
            map_range_4.inputs[1].default_value = 0.75
            map_range_4.inputs[2].default_value = 1.0
            map_range_4.inputs[3].default_value = 0.0
            map_range_4.inputs[4].default_value = 1.0
            map_range_4.clamp = True

            # Link nodes
            links = node_group.links
            links.new(group_inputs_node.outputs['A'], mix_node_1.inputs[1])
            links.new(group_inputs_node.outputs['B'], mix_node_1.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_1.inputs[0])
            links.new(map_range_1.outputs[0], mix_node_1.inputs[0])

            links.new(mix_node_1.outputs[0], mix_node_2.inputs[1])
            links.new(group_inputs_node.outputs['C'], mix_node_2.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_2.inputs[0])
            links.new(map_range_2.outputs[0], mix_node_2.inputs[0])

            links.new(mix_node_2.outputs[0], mix_node_3.inputs[1])
            links.new(group_inputs_node.outputs['D'], mix_node_3.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_3.inputs[0])
            links.new(map_range_3.outputs[0], mix_node_3.inputs[0])

            links.new(mix_node_3.outputs[0], mix_node_4.inputs[1])
            links.new(group_inputs_node.outputs['E'], mix_node_4.inputs[2])
            links.new(group_inputs_node.outputs['Factor'], map_range_4.inputs[0])
            links.new(map_range_4.outputs[0], mix_node_4.inputs[0])

            links.new(mix_node_4.outputs[0], group_outputs_node.inputs['Result'])


        if group_name not in bpy.data.node_groups.keys() and group_name == "Mix Color (Splat, RGB)":

            node_group = bpy.data.node_groups.new(name="Mix Color (Splat, RGB)", type="ShaderNodeTree")
            node_group.use_fake_user = True

            # Create group inputs
            group_inputs_node = node_group.nodes.new("NodeGroupInput")
            group_inputs_node.location = (-600, 0)

            interface = node_group.interface
            a_input = interface.new_socket("R", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            b_input = interface.new_socket("G", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            c_input = interface.new_socket("B", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            splatmap_input = interface.new_socket("Splat Map", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            a_input.default_value, b_input.default_value, c_input.default_value, splatmap_input.default_value = (0,0,0,1), (0,0,0,1), (0,0,0,1), (0.5,0.5,0.5,1)

            # Create group outputs
            group_outputs_node = node_group.nodes.new("NodeGroupOutput")
            group_outputs_node.location = (600, 0)
            group_output = interface.new_socket("Result", description="", in_out='OUTPUT', socket_type='NodeSocketColor', parent=None)

            # Add internal nodes
            mix_node_1 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_1.location = (0, 100)
            mix_node_1.use_clamp = True
            mix_node_1.blend_type = 'MIX'
            mix_node_1.inputs[1].default_value = (0,0,0,1)

            mix_node_2 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_2.location = (200, 100)
            mix_node_2.use_clamp = True
            mix_node_2.blend_type = 'MIX'

            mix_node_3 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_3.location = (400, 100)
            mix_node_3.use_clamp = True
            mix_node_3.blend_type = 'MIX'

            separate_color_node = node_group.nodes.new(type="ShaderNodeSeparateColor")
            separate_color_node.location = (-200, -100)
            separate_color_node.mode = "RGB"

            # Link nodes
            links = node_group.links
            links.new(group_inputs_node.outputs['R'], mix_node_1.inputs[2])
            links.new(group_inputs_node.outputs['G'], mix_node_2.inputs[2])
            links.new(group_inputs_node.outputs['B'], mix_node_3.inputs[2])
            links.new(group_inputs_node.outputs['Splat Map'], separate_color_node.inputs[0])

            links.new(separate_color_node.outputs[0], mix_node_1.inputs[0])
            links.new(separate_color_node.outputs[1], mix_node_2.inputs[0])
            links.new(separate_color_node.outputs[2], mix_node_3.inputs[0])

            links.new(mix_node_1.outputs[0], mix_node_2.inputs[1])
            links.new(mix_node_2.outputs[0], mix_node_3.inputs[1])
            links.new(mix_node_3.outputs[0], group_outputs_node.inputs['Result'])


        if group_name not in bpy.data.node_groups.keys() and group_name == "Mix Color (Splat, RGBA)":

            node_group = bpy.data.node_groups.new(name="Mix Color (Splat, RGBA)", type="ShaderNodeTree")
            node_group.use_fake_user = True

            # Create group inputs
            group_inputs_node = node_group.nodes.new("NodeGroupInput")
            group_inputs_node.location = (-600, 0)

            interface = node_group.interface
            a_input = interface.new_socket("R", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            b_input = interface.new_socket("G", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            c_input = interface.new_socket("B", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            d_input = interface.new_socket("A", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            splatmap_input = interface.new_socket("Splat Map (RGB)", description="", in_out='INPUT', socket_type='NodeSocketColor', parent=None)
            a_input.default_value, b_input.default_value, c_input.default_value, splatmap_input.default_value = (0,0,0,1), (0,0,0,1), (0,0,0,1), (0.5,0.5,0.5,1)
            alpha_input = interface.new_socket("Splat Map (Alpha)", description="", in_out='INPUT', socket_type='NodeSocketFloat', parent=None)
            alpha_input.default_value = 0.5
            alpha_input.min_value = 0.0
            alpha_input.max_value = 1.0
            alpha_input.subtype = "FACTOR"

            # Create group outputs
            group_outputs_node = node_group.nodes.new("NodeGroupOutput")
            group_outputs_node.location = (800, 0)
            group_output = interface.new_socket("Result", description="", in_out='OUTPUT', socket_type='NodeSocketColor', parent=None)

            # Add internal nodes
            mix_node_1 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_1.location = (0, 100)
            mix_node_1.use_clamp = True
            mix_node_1.blend_type = 'MIX'
            mix_node_1.inputs[1].default_value = (0,0,0,1)

            mix_node_2 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_2.location = (200, 100)
            mix_node_2.use_clamp = True
            mix_node_2.blend_type = 'MIX'

            mix_node_3 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_3.location = (400, 100)
            mix_node_3.use_clamp = True
            mix_node_3.blend_type = 'MIX'

            mix_node_4 = node_group.nodes.new(type="ShaderNodeMixRGB")
            mix_node_4.location = (600, 100)
            mix_node_4.use_clamp = True
            mix_node_4.blend_type = 'MIX'

            separate_color_node = node_group.nodes.new(type="ShaderNodeSeparateColor")
            separate_color_node.location = (-200, -100)
            separate_color_node.mode = "RGB"

            # Link nodes
            links = node_group.links
            links.new(group_inputs_node.outputs['R'], mix_node_1.inputs[2])
            links.new(group_inputs_node.outputs['G'], mix_node_2.inputs[2])
            links.new(group_inputs_node.outputs['B'], mix_node_3.inputs[2])
            links.new(group_inputs_node.outputs['A'], mix_node_4.inputs[2])
            links.new(group_inputs_node.outputs['Splat Map (RGB)'], separate_color_node.inputs[0])
            links.new(group_inputs_node.outputs['Splat Map (Alpha)'], mix_node_4.inputs[0])

            links.new(separate_color_node.outputs[0], mix_node_1.inputs[0])
            links.new(separate_color_node.outputs[1], mix_node_2.inputs[0])
            links.new(separate_color_node.outputs[2], mix_node_3.inputs[0])

            links.new(mix_node_1.outputs[0], mix_node_2.inputs[1])
            links.new(mix_node_2.outputs[0], mix_node_3.inputs[1])
            links.new(mix_node_3.outputs[0], mix_node_4.inputs[1])
            links.new(mix_node_4.outputs[0], group_outputs_node.inputs['Result'])

def register():
    bpy.app.handlers.load_post.append(add_mix_nodes)

def unregister():
    bpy.app.handlers.load_post.remove(add_mix_nodes)

if __name__ == "__main__":
    register()
