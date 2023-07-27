from bpy.props import BoolProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType

class DoorComponent(HubsComponent):
    _definition = {
        'name': 'door',
        'display_name': "Door",
        'category': Category.OBJECT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'GRID'
    }

    isOpen: BoolProperty(
        name="isOpen", description="This door is open", default=False)
