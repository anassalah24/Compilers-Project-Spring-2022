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
        'ILLEGALMINUS'
        ]
        
        reserved = {
            'if' : 'IF',
            'then' : 'THEN',
            'end' : 'END',
            'else' : 'ELSE',
        }
        tokens += reserved.values()
        # Regular expressions for tokens

        t_NUMBER  = r'[+-]?[0-9]+'
        t_ASSIGNMENT = r':='
        t_SEMICOLON = r';'
        t_ILLEGAL = r'[$&,=?@#|<>./\'\"`^*()%!]'
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
            


