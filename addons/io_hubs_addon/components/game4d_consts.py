VARIABLE_TYPES = [(
                      "string", "String",
                      "Variable will be interpreted as a string of characters"
                  ),
                  (
                      "uint", "Unsigned Integer",
                      "Variable will be interpreted as an unsigned integer, meaning only positive integers"
                  ), 
                  (
                      "sint", "Signed Integer",
                      "Variable will be interpreted as a signed integer, supporting negative integers"
                  ),
                  (
                      "float", "Float",
                      "Variable will be interpreted as a floating point number"   
                  )]

ACTION_TYPES =    [(
                      "console", "Console.log()",
                      "Return the internal state of the gameobject in the console, using standard string building functionality"
                  ),
                  (
                      "ui", "Spawn UI",
                      "Spawn a user-interface node for this object"
                  )]