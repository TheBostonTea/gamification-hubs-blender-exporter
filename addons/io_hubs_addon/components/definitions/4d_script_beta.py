from bpy.props import StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType

class ScriptingComponent(HubsComponent):
    _definition = {
        'name': 'script',
        'display_name': "Script",
        'category': Category.OBJECT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'TEXT'
    }

    script: StringProperty(
        name="Script", description="What the script will be that will run in your mozilla hubs world.", default="NONE")