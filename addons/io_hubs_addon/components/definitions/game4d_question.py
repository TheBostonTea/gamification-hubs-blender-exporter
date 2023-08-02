from bpy.props import StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType

class QuestionComponent(HubsComponent):
    _definition = {
        'name': 'question',
        'display_name': "Question (Deprecated)",
        'category': Category.GAME,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'QUESTION'
    }

    question: StringProperty(
        name="Question", description="What the question will be for this question mark", default="NONE")
