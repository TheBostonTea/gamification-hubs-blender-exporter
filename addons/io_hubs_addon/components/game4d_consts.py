VARIABLE_TYPES =    [(
                        "int", "Integer",
                        "Variable will be interpreted as an integer, or a whole number"
                    ), 
                    (
                        "float", "Float",
                        "Variable will be interpreted as a floating point number"   
                    ),
                    (
                        "string", "String",
                        "Variable will be interpreted as a string of characters"
                    ),
                    (
                        "boolean", "Boolean",
                        "Variable will be interpreted as a Boolean, expecting \"True\" and \"False\""
                    )]

ACTION_TYPES =      [(
                        "console", "Console.log()",
                        "Return the internal state of the gameobject in the console, using standard string building functionality"
                    ),
                    (
                        "ui", "Spawn UI",
                        "Spawn a user-interface node for this object"
                    )]