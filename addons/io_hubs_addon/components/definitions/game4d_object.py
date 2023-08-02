from bpy.props import BoolProperty, EnumProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType
from ..game4d_consts import VARIABLE_TYPES

id = 0; 

class GameObjectComponent(HubsComponent):
    _definition = {
        'name': 'game4d-object',
        'display_name': "Game4d Object",
        'category': Category.GAME,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'META_CUBE'
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

    hasVariable: BoolProperty(
        name="Has Variable",
        description="Does this Game4d object hold a variable?",
        default=False
    )

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

    def draw(self, context, layout, panel):
        layout.prop(data=self, property="identifier")
        layout.prop(data=self, property="isActive")
        layout.prop(data=self, property="hasVariable")
        if not self.hasVariable:
            return

        layout.prop(data=self, property="variableName")
        layout.prop(data=self, property="variableType")
        layout.prop(data=self, property="variableContent")

