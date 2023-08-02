from bpy.props import BoolProperty, EnumProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, NodeType, PanelType
from ..game4d_consts import ACTION_TYPES, VARIABLE_TYPES

class OnClickComponent(HubsComponent):
    _definition = {
        'name': 'game4d-on-click',
        'display_name': "Game4d On Click Action",
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

    actionType: EnumProperty(
        name="Action Type",
        description="What Action will be triggered when this object is clicked?",
        items=ACTION_TYPES,
        default="console"
    )

    # This is ugly: We'd want to pool different variables, within the context of this property, and let these populate the list!
    # TODO: Pool variables based on availibility!
    # TODO: For prints and other applications, bind variables to actions!
    # TODO: For actions: Allow multiple actions for one thing
    # TODO: Conditional: add Conditional nodes
    useInternal: BoolProperty(
        name="Use Internal Variable",
        description="Use the Game4d Object internal variable",
        default = True
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

    # def gather(self, export_settings, object):
    #     if self.useInternal:
    #         assert hasComponent(object, 'game4d-object')
    #         self.variableName = object.hubs_component_list.items[object.hubs_component_list.items.index('game4d-object')].variableName
    #         self.variableType = object.hubs_component_list.items[object.hubs_component_list.items.index('game4d-object')].variableType
    #         self.variableContent = object.hubs_component_list.items[object.hubs_component_list.items.index('game4d-object')].variableContent

    #     return {
    #         'isActive': self.isActive,
    #         'actionType': self.actionType,
    #         'useInternal': self.useInternal,
    #         'variableName': self.variableName,
    #         'variableType': self.variableType,
    #         'variableContent': self.variableContent
    #     }
        
        






    def draw(self, context, layout, panel):
        layout.prop(data=self, property="isActive")
        layout.prop(data=self, property="actionType")
        layout.prop(data=self, property="useInternal")
        if self.useInternal:
            return

        layout.prop(data=self, property="variableName")
        layout.prop(data=self, property="variableType")
        layout.prop(data=self, property="variableContent")

