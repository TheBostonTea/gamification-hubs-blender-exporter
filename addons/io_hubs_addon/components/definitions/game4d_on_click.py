from bpy.props import BoolProperty, EnumProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType
from ..game4d_consts import ACTION_TYPES, VARIABLE_TYPES
from ..game4d_utils import game4d_gen_action_dict
import json

class Game4dOnClick(HubsComponent):
    _definition = {
        'name': 'game4d-on-click',
        'display_name': "Game4d On Click Interaction",
        'category': Category.GAME,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'deps': ['game4d-object'],
        'icon': 'META_CUBE'
    }

    isActive: BoolProperty(
        name="Starts Active",
        description="Is this function active at the start of the runtime? (E.g, does it produce behavior?)",
        default=True
    )

    # TODO: Multiple nodes, different vars per action, etc...!
    action: EnumProperty(
        name="Action Type",
        description="What Action will be triggered when this object is clicked?",
        items=ACTION_TYPES,
        default="console"
    )

    actionString: StringProperty(
        name= "Action String",
        description="What arguments will be given to the action?",
        default=""
    )


    def gather(self, export_settings, object):

        # TODO: Gather multiple actions
        actions = [game4d_gen_action_dict(self.action, self.actionString, [])]
        
        actjsonstr = ""

        if self.action != "":
            actjsonstr = json.dumps(actions)
        
        return {
            'isActive': self.isActive,
            'actions': actjsonstr,
        }
        
        
    def draw(self, context, layout, panel):
        layout.prop(data=self, property="isActive")
        layout.prop(data=self, property="action")

        if self.action != "":
            layout.prop(data=self, property="actionString")
        # TODO: display action list!

