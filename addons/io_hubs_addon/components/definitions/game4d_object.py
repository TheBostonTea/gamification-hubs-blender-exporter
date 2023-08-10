import bpy
from bpy.props import BoolProperty, EnumProperty, StringProperty, IntProperty, CollectionProperty
from bpy.types import PropertyGroup, UIList, Operator, Panel
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType
from ..game4d_consts import VARIABLE_TYPES
from ..game4d_utils import game4d_gen_variable_dict
import json

# id = 0;

class VariableEntry(PropertyGroup):
    name: StringProperty(
        name="Variable Name",
        description="How the variable will be referenced within this object."
    )

    type: EnumProperty(
        name="Variable Type",
        description="The Datatype of the variable.",
        items=VARIABLE_TYPES,
        default="string"
    )

    content: StringProperty(
        name="Variable Content",
        description="What the value will be for the variable.",
    )


class VariablesList(UIList):
    bl_idname = "HUBS_UL_VARIABLES_list"

    # Constants (flags)
    # Be careful not to shadow FILTER_ITEM (i.e. UIList().bitflag_filter_item)!
    # E.g. VGROUP_EMPTY = 1 << 0

    # Custom properties, saved with .blend file. E.g.
    # use_filter_empty: bpy.props.BoolProperty(
    #     name="Filter Empty", default=False, options=set(),
    #     description="Whether to filter empty vertex groups",
    # )

    # Called for each drawn item.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):

        # 'DEFAULT' and 'COMPACT' layout types should usually use the same draw code.
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text="{item.name} : {item.type}", icon = icon)
    
        # 'GRID' layout type should be as compact as possible (typically a single icon!).
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon = icon)

    # # Called once to draw filtering/reordering options.
    # def draw_filter(self, context, layout):
    #     # Nothing much to say here, it's usual UI code...
    #     pass

    # # Called once to filter/reorder items.
    # def filter_items(self, context, data, propname):
    #     # This function gets the collection property (as the usual tuple (data, propname)), and must return two lists:
    #     # * The first one is for filtering, it must contain 32bit integers were self.bitflag_filter_item marks the
    #     #   matching item as filtered (i.e. to be shown), and 31 other bits are free for custom needs. Here we use the
    #     #   first one to mark VGROUP_EMPTY.
    #     # * The second one is for reordering, it must return a list containing the new indices of the items (which
    #     #   gives us a mapping org_idx -> new_idx).
    #     # Please note that the default UI_UL_list defines helper functions for common tasks (see its doc for more info).
    #     # If you do not make filtering and/or ordering, return empty list(s) (this will be more efficient than
    #     # returning full lists doing nothing!).

    #     # Default return values.
    #     flt_flags = []
    #     flt_neworder = []

    #     # Do filtering/reordering here...

    #     return flt_flags, flt_neworder

class VariablesListNewVariable(Operator):

    bl_idname = "variables.new_item"
    bl_label = "Add a new item"

    def execute(self, context):
        # What is the context here?
        # context.

        return{'FINISHED'}



class Game4dObject(HubsComponent):
    _definition = {
        'name': 'game4d-object',
        'display_name': "Game4d Object",
        'category': Category.GAME,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'META_CUBE',
        'version': (1, 0, 0)
    }

    identifier: StringProperty(
        name="Identifier",
        description="The name of the object, used to identify it inside the code",
        default=str(id)
    )

    isActive: BoolProperty(
        name="Starts Active",
        description="Is this Game4d object active at the start of the runtime? (E.g, does it produce behavior?)",
        default=True
    )
  
    # TODO: Deprecate, or at least change. These must not be exported! 
    # variableName: StringProperty(
    #     name="Var Name",
    #     description="How the internally held variable will be named to be accessible by the game system",
    #     default=""
    # )

    # variableType: EnumProperty(
    #     name="Var Type",
    #     description="How the internally held variable will be interpreted by the game system",
    #     items=VARIABLE_TYPES,
    #     default="string"
    # )

    # variableContent: StringProperty(
    #     name="Var Content",
    #     description="What the internally held variable will be for this object",
    #     default=""
    # )

    # variables: StringProperty(
    #     name="Variables",
    #     description="List of all the variables associated with this object.",
    #     default="",
    #     options={'HIDDEN'}
    # )

    variables: CollectionProperty(
        type=VariableEntry
    )

    active_variable_key: IntProperty(
        name="Active variable index",
        description="Active variable index",
        default=-1
    )

    # do I need this?
    # def migrate(self, migration_type, panel_type, instance_version, host, migration_report, ob=None):
    #     migration_occurred = False
    #     if instance_version < (1, 0, 0):
    #         migration_occurred = True

    #         if migration_type != MigrationType.GLOBAL or is_linked(host):
    #             migration_report.append(
    #                 f"Warning: The Media Cone angles may not have migrated correctly for the Audio Settings component on scene \"{host.name_full}\"")

    #     return migration_occurred

    def draw(self, context, layout, panel):
        layout.prop(data=self, property="identifier")
        layout.prop(data=self, property="isActive")

        layout.label(text='Variables of this Game4d Object:')

        row = layout.row()

        row.template_list(VariablesList.bl_idname, "", self,
                          "variables", self, "active_variable_key", rows=3)

        # if self.variableName != "":
        #     layout.prop(data=self, property="variableType")
        #     layout.prop(data=self, property="variableContent")

    def gather(self, export_settings, object):

        # Todo: Gather multiple variables from a collection!
        # variables = [game4d_gen_variable_dict(self.variableName, self.variableType, self.variableContent)]

        varjsonstr = ""

    
        # if self.variableName != "":

        #     varjsonstr = json.dumps(variables)
        #     print(varjsonstr)


        return {
            'identifier': self.identifier,
            'isActive': self.isActive,
            'variables': varjsonstr
        }

    @ staticmethod
    def register():
        bpy.utils.register_class(VariablesList)
    
    @ staticmethod
    def unregister():
        bpy.utils.unregister_class(VariablesList)

def register_module():
    bpy.utils.register_class(VariableEntry)


def unregister_module():
    bpy.utils.unregister_class(VariableEntry)

    



