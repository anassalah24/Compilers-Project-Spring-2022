import ply.lex as lex





def tokengenerator(sentence):
            
        # token names
        tokens = [
        'ID',
        'NUMBER',
        'ASSIGNMENT',
        'SEMICOLON',
        'ILLEGAL',
        'ILLEGALCOLON',
        'ILLEGALPLUS',
        'ILLEGALMINUS',
        'ILLEGAL_ID'
        ]
        
        reserved = {
            'if' : 'IF',
            'IF' : 'IF',
            'If' : 'IF',
            'iF' : 'IF',
            'then' : 'THEN',
            'THEN' : 'THEN',
            'Then' : 'THEN',
            'tHen' : 'THEN',
            'thEn' : 'THEN',
            'theN' : 'THEN',
            'THen' : 'THEN',
            'ThEn' : 'THEN',
            'TheN' : 'THEN',
            'tHEn' : 'THEN',
            'tHeN' : 'THEN',
            'thEN' : 'THEN',
            'end' : 'END',
            'END' : 'END',
            'End' : 'END',
            'eNd' : 'END',
            'enD' : 'END',
            'ENd' : 'END',
            'EnD' : 'END',
            'eND' : 'END',
            'else' : 'ELSE',
            'ELSE' : 'ELSE',
            'Else' : 'ELSE',
            'eLse' : 'ELSE',
            'elSe' : 'ELSE',
            'elsE' : 'ELSE',
            'ELse' : 'ELSE',
            'ElSe' : 'ELSE',
            'ElsE' : 'ELSE',
            'eLSe' : 'ELSE',
            'eLsE' : 'ELSE',
            'elSE' : 'ELSE',
        }
        tokens += reserved.values()
        # Regular expressions for tokens

        t_NUMBER  = r'[+-]?[0-9]+'
        t_ASSIGNMENT = r':='
        t_SEMICOLON = r';'
        t_ILLEGAL = r'[$&,=?@#|<>./\'\"`^*()%!]'
        t_ILLEGAL_ID = r'[-+]?[0-9]+[a-zA-Z_]+'
        t_ILLEGALCOLON = r':'
        t_ILLEGALPLUS = r'[+]'
        t_ILLEGALMINUS = r'[-]'
        
        def t_ID(t):
            r'[a-zA-Z_][a-zA-Z0-9_]*'
            if t.value in reserved:
                t.type = reserved[ t.value ]
            return t
        
        # Define a rule so we can track line numbers
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)
        
        # A string containing ignored characters (spaces and tabs)
        t_ignore  = ' \t'
        
        # Error handling rule
        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)
        
        # Build the lexer
        lexer = lex.lex()

        
        # Give the lexer some input
        lexer.input(sentence)
        mytokens=[]
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            mytokens.append(("<" + tok.type +","+ tok.value +">"))
        return mytokens  
            


