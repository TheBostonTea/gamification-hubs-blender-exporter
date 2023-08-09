from bpy.props import BoolProperty, EnumProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType, MigrationType
from ..utils import is_linked
from ..game4d_consts import VARIABLE_TYPES
import json

# id = 0; 

class Game4dObjectComponent(HubsComponent):
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

    # Just use an empty string for no variables!
    # hasVariable: BoolProperty(
    #     name="Has Variable",
    #     description="Does this Game4d object hold a variable?",
    #     default=False
    # )
  
    # TODO: Deprecate, or at least change. These must not be exported! 
    variableName: StringProperty(
        name="Var Name",
        description="How the internally held variable will be named to be accessible by the game system",
        default=""
    )

    variableType: EnumProperty(
        name="Var Type",
        description="How the internally held variable will be interpreted by the game system",
        items=VARIABLE_TYPES,
        default="string"
    )

    variableContent: StringProperty(
        name="Var Content",
        description="What the internally held variable will be for this object",
        default=""
    )

    variables: StringProperty(
        name="Vars",
        description=".json Representation of the variables!",
        default="",
        options={'HIDDEN'}
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

    def gather(self, export_settings, object):

        # Todo: Gather all the variables into dictionaries!
        variables = [{"name" : self.variableName, "type": self.variableType, "content": self.variableContent}]

        varjsonstr = ""

    
        if self.variableName != "":

            varjsonstr = json.dumps(variables)
            print(varjsonstr)


        return {
            'identifier': self.identifier,
            'isActive': self.isActive,
            'variables': varjsonstr
        }
    

    def draw(self, context, layout, panel):
        layout.prop(data=self, property="identifier")
        layout.prop(data=self, property="isActive")

        layout.prop(data=self, property="variableName")

        if self.variableName != "":
            layout.prop(data=self, property="variableType")
            layout.prop(data=self, property="variableContent")

