VARIABLE_NAME_HEADER = "name"
VARIABLE_TYPE_HEADER = "type"
VARIABLE_CONTENT_HEADER = "content"

ACTION_FUNCTION_HEADER = "function"
ACTION_ARGS_HEADER = "args"
ACTION_CHILDREN_HEADER = "children"

def game4d_gen_variable_dict(name, type, content):
    return { VARIABLE_NAME_HEADER: name,
             VARIABLE_TYPE_HEADER: type,
             VARIABLE_CONTENT_HEADER: content }


def game4d_gen_action_dict(function, args, children):
    return {ACTION_FUNCTION_HEADER: function, ACTION_ARGS_HEADER: args, ACTION_CHILDREN_HEADER: children}