import sys
from prettytable import PrettyTable
lookUpTable = {';', '=', '+', '-', '*', '/', '%', '(', ')', 
               'READ', 'PRINT', 'int', 'float', 'boolean', 
                'if', ':', 'else', 'end', 
              'while', 'do', 'and', 'or', '>', 
               '<', '>=', '==', ' ', '{', '}'}
user_tokens = {}

def read_token():   
        print ('Enter a string:')
        line = sys.stdin.readline().strip() 
        return line
    
#trans str-->line to a list-->word_list, return word_list[]
def lexemes(line):
    word_list = list(line)
    remove_values_from_list(word_list, ' ')
    return word_list

#no blank in list - a set of token, return tokens[]
def tokenRecogn(word_list):
    v = []
    flag = True
    length = len(word_list)
    tokens = []

    for i in range(length):
        #print("word_list[i] = ", word_list[i] )
        if word_list[0] == " ":
            v.clear()
            continue
        else:            
            if word_list[i] in lookUpTable:
                    if  word_list[i] == '=':
                        v.append(word_list[i])
                        
                        if i < length - 1:
                            if word_list[i+1] == '=':
                                flag = True
                            else:
                                flag = False
                                token = ''.join(v)
                                tokens.append(token)
                                v.clear()
                                                                               
                    elif  word_list[i] == '>':
                        v.append(word_list[i])
                        
                        if i < length - 1:
                            if word_list[i+1] == '=':
                                flag = True
                            else:
                                flag = False
                                token = ''.join(v)
                                tokens.append(token)
                                v.clear()
                    elif word_list[i] == ' ':
                        flag = False
                        if v:                        
                            token = ''.join(v)
                            tokens.append(token)                     
                            v.clear()                          
                    else:
                        flag = False  
                        if v:                      
                            token = ''.join(v)
                            tokens.append(token)                     
                            v.clear()   
                        v.append(word_list[i])                                                                       
            else:
                if flag:
                    
                    v. append(word_list[i])
                else:
                    if v:
                        token = ''.join(v)
                        tokens.append(token)
                        v.clear()
                    v.append(word_list[i])
                    flag = True
    if v:
        token = ''.join(v)
        tokens.append(token)
    
    return tokens

def get_keyword(num):
    switcher = {
        0: "UNVAILD_TYPE",
        1: "VAR_CODE",
        2: "DIGIT_CODE_FLOAT",
        3: "DIGIT_CODE_INT",
        4: "COLON",
        5: "SEMICOLON",
        6: "RADIX_POINT",
        7: "ASSIGN_OP",
        8: "ADDITION_OP",
        9: "SUBTRACTION_OP",
        10: "MUTIPLY_OP",
        11: "DIVISION_OP",
        12: "COMPLEMENTATION_OP",
        13: "LEFT_PARENTHSIS",
        14: "RIGHT_PARENTHSIS",
        15: "READ_STAT_KEYWORD",
        16: "WRITE_STAT_KEYWORD",
        17: "TYPE_INT",
        18: "TYPE_FLOAT",
        19: "TYPE_BOOLEAN",
        20: "IF_STMT_IF",
        21: "IF_STMT_ELSE",
        22: "END",
        23: "WHILE_STMT_WHILE",
        24: "WHILE_STMT_DO",
        25: "BOOL_STMT_AND",
        26: "BOOL_STMT_OR",
        27: "REL_STMT_LESS",
        28: "REL_STMT_GREATER",
        29: "REL_STMT_GREATEREQUAL",
        30: "REL_STMT_EQUAL",
        31: "LEFT_BLOCK",
        32: "RIGHT_BLOCK",
        33: "USER_DEFINED_TOKEN"  
        }
    return switcher.get(num)

def errorInfo(error_num):
    print('\n',"-------------ERROR!----------", '\n')
    switcher = {
       0: "WRONG GRAMMAR: UNVILD TYPE",
       1: "WRONG GRAMMAR: NOT A STATEMENT!",
       2: "WRONG GRAMMAR: LESS SEMICOLON",
       3: "WRONG GRAMMAR: USELESS KEY",
       4: "WRONG GRAMMAR: MISS VAR IN VAR_DEC",
       5: "WRONG GRAMMAR: UNPAIR PPARENTHESIS",
       6: "WRONG GRAMMAR: A SYNTACTIC ERROR IN IF_STMT",
       7: "WRONG GARMMAR: A SYNTACTIC ERROR IN WHILE_STMT",
       8: "WRONG GARMMAR: A SYNTACTIC ERROR IN EXPR",
       9: "WRONG GARMMAR: A SYNTACTIC ERROR IN BLOCK",  
       10: "WRONG GARMMAR: INT CANNOT BEGIN AT 0",  
       11: "WRONG GARMMAR: MISS ASSIGN_EQUE",
       12: "WRONG GRAMMAR: LESS COLON"      
        }
    print (switcher.get(error_num))
    sys.exit(0)


#classify tokens to type, return token_type[]
#def tokensType(word_list):
def tokensType(word_list):
    token_type = []    
    #for words in tokens:
    for i in range(len(word_list)):
        if word_list[i] not in user_tokens:            
            if word_list[i] not in lookUpTable:                
                var_len = len(word_list[i])
                #letter A-Z; a-z
                letter = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]
                number = [chr(i) for i in range(48, 58)]
                if word_list[i][0] in letter:
                    if checkLetter(word_list[i]):
                        token_type.append(get_keyword(1))                        
                    else:                         
                        token_type.append(get_keyword(0))                        
                        errorInfo(0)                                       
                elif word_list[i][0] in number:
                    
                    if word_list[i][0] == '0':
                        if checkPoint(word_list[i]):
                            if checkNum(word_list[i]):
                                token_type.append(get_keyword(2)) 
                            else:
                                token_type.append(get_keyword(0)) 
                                errorInfo(0)
                        else:
                            if var_len == 1:
                                token_type.append(get_keyword(3))
                            else:                                  
                                if checkNum(word_list[i]):
                                    token_type.append(get_keyword(0)) 
                                    errorInfo(10)
                                else:
                                    token_type.append(get_keyword(0)) 
                                    errorInfo(0)
                    else:
                        if checkPoint(word_list[i]):
                            if checkNum(word_list[i]):
                                
                                token_type.append(get_keyword(2))                            
                            else:
                                token_type.append(get_keyword(0)) 
                                errorInfo(0)
                        else: 
                            
                            if checkNum(word_list[i]):
                                token_type.append(get_keyword(3))                            
                            else:
                                token_type.append(get_keyword(0)) 
                                errorInfo(0) 
                else:   
                    token_type.append(get_keyword(0)) 
                    errorInfo(0)                                                                                                                                         
            else:
                #keywords
                if word_list[i] == ':':
                    token_type.append(get_keyword(4)) 
                elif word_list[i] == ';':
                    token_type.append(get_keyword(5)) 
                elif word_list[i] == '.':
                    token_type.append(get_keyword(6)) 
                elif word_list[i] == '=':
                    token_type.append(get_keyword(7))                       
                elif word_list[i] == '+':
                    token_type.append(get_keyword(8)) 
                elif word_list[i] == '-':
                    token_type.append(get_keyword(9)) 
                elif word_list[i] == '*':
                    token_type.append(get_keyword(10)) 
                elif word_list[i] == '/':
                    token_type.append(get_keyword(11)) 
                elif word_list[i] == '%':
                    token_type.append(get_keyword(12))
                
                elif word_list[i] == '(':
                    token_type.append(get_keyword(13)) 
                elif word_list[i] == ')':
                    token_type.append(get_keyword(14)) 
                
                elif word_list[i] == 'READ':
                    token_type.append(get_keyword(15)) 
                elif word_list[i] == 'PRINT':
                    token_type.append(get_keyword(16)) 
                
                elif word_list[i] == 'int':
                    token_type.append(get_keyword(17)) 
                elif word_list[i] == 'float':
                    token_type.append(get_keyword(18)) 
                elif word_list[i] == 'boolean':
                    token_type.append(get_keyword(19)) 
                
                elif word_list[i] == 'if':
                    token_type.append(get_keyword(20)) 
                elif word_list[i] == 'else':
                    token_type.append(get_keyword(21)) 
                elif word_list[i] == 'end':
                    token_type.append(get_keyword(22)) 
                elif word_list[i] == 'while':
                    token_type.append(get_keyword(23))             
                elif word_list[i] == 'do':
                    token_type.append(get_keyword(24))            
                
                elif word_list[i] == 'and':
                    token_type.append(get_keyword(25)) 
                elif word_list[i] == 'or':
                    token_type.append(get_keyword(26)) 
                
                elif word_list[i] == '<':
                    token_type.append(get_keyword(27)) 
                elif word_list[i] == '>':   
                    token_type.append(get_keyword(28)) 
                elif word_list[i] == '>=':   
                    token_type.append(get_keyword(29)) 
                elif word_list[i] == '==':
                    token_type.append(get_keyword(30))
                elif word_list[i] == '{':
                    token_type.append(get_keyword(31))
                elif word_list[i] == '}':
                    token_type.append(get_keyword(32))                                             
                elif word_list[i] == " ":
                    continue
                else:
                    token_type.append(get_keyword(0)) 
                    
                    
        else:
            token_type.append(get_keyword(33)) 
    return token_type  

def checkPoint(word):
    if '.' in word:
        return True
    else:
        return False
    
def checkNum(word):
    number = [chr(i) for i in range(48, 58)]    
    count = 0
    for i in word:
        if i == '.':
            continue
        if i not in number:
            count += 1
    
    if count != 0:
        return False
    else:
        return True
    
def checkLetter(word):
    letter = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]

    count = 0
    for i in word:
        if i not in letter:
            count += 1
    
    if count != 0:
        return False
    else:
        return True
            
##zip tokens to each type,return token_type[]   
def showTokensType(tokens, token_type):
    remove_values_from_list(tokens, ' ')
    
    col = PrettyTable()
    col.add_column("Tokens", tokens)
    col.add_column("Type", token_type)

    print('\n', col)

def splitBlock(token_type):
    set_bl_left = 'LEFT_BLOCK'
    set_bl_right = 'RIGHT_BLOCK'
    set_split = ['COLON', 'WHILE_STMT_DO']
    set_fin = ['END', 'IF_STMT_ELSE']
    lent = len(token_type)      
    block_list = []
    new_block = []
    fin_bl = []
    contr = False
    con_b = 0
    block = ''
    
    if len(token_type) == 1:
        fin_bl = token_type 
    #no '{' in expr
    if (set_bl_left not in token_type):
        #print("1")
        #no '{' in expr but have '}'
        if set_bl_right in token_type:
            errorInfo(9)
        else: #no '{}'
            fin_bl = token_type         
    else:  #have '{''}' 
        if checkBlock(block_list): 
            for i in range(lent):
                if contr:                
                    if token_type[i] in set_split:
                        new_block.append(token_type[i])
                        con_b += 1
                    if token_type[i] in set_fin:
                        con_b -= 1
                        if(con_b == 0):                
                            block = '!'.join(new_block)
                            #print("block = ", block)
                            fin_bl.append(block)
                            fin_bl.append(token_type[i])
                            contr = False
                            new_block.clear()
                            
                        else:
                            new_block.append(token_type[i])
                            con_b -= 1
                    else:
                        new_block.append(token_type[i])
                else:
                    if token_type[i] in set_split:
                        
                        fin_bl.append(token_type[i])
                        contr = True
                        con_b += 1
                    else: 
                        fin_bl.append(token_type[i])
        else:
            errorInfo(9)           
    return fin_bl

def stmtRecogn(s_list): 
    #print("-----SR")
    #print("SR= ", s_list)         
    stmt = []
    tc = []
    stmt_count = 0  
    #统计有几个分隔符
    for i in range(len(s_list)):
        if(s_list[i] == 'SEMICOLON'):
            stmt_count += 1
        
    #1.如果是判断；， 没有就整句话输入
    if(stmt_count == 0):
        stmt_list = s_list
    else:        
        for i in range(len(s_list)):
            if(i < len(s_list) - 1):            
                nextToken = s_list[i + 1]            
                if(s_list[i] == 'SEMICOLON'):
                        continue
                else:
                    if nextToken == 'SEMICOLON':
                        tc.append(s_list[i])
                        tc.append(nextToken)                                 
                        stmt.append(','.join(tc))                            
                        tc.clear()
                    else:
                        tc.append(s_list[i])
            elif s_list[i] != 'SEMICOLON':   
                stmt_count += 1 
                tc.append(s_list[i])
                stmt.append(','.join(tc))                                                   
    
        for i in range(stmt_count):
            stmt_list = stmt[i].split(',')

    check_syntactic_error(stmt_list)
          
    #print("before s_list = ",s_list)
    if s_list[0] not in ['VAR_CODE', 'DIGIT_CODE_INT', 'DIGIT_CODE_FLOAT', '', 'READ_STAT_KEYWORD', 'WRITE_STAT_KEYWORD' ]:
        for item in s_list:
            if len(item) >= 22 :              
                tmp = item.split('!')
                tmp.remove('LEFT_BLOCK') 
                tmp.remove('RIGHT_BLOCK')
                #print("tmp = ", tmp)
                
                check_syntactic_error(splitBlock(tmp))
                
    else:
        #print("")
        pass

    return stmt_list
                                
def nextToken(i, tokensType):
    nextToken = tokensType[i + 1]
    return nextToken

def remove_values_from_list(the_list, val):
    while val in the_list:
        the_list.remove(val)
            
def splitExpr(stmt_list):
    set_par_left = 'LEFT_PARENTHSIS'
    set_par_right = 'RIGHT_PARENTHSIS'

    lent = len(stmt_list)  
    if lent != 0:
        if(checkPar(stmt_list)):
            remove_values_from_list(stmt_list, set_par_left)
            remove_values_from_list(stmt_list, set_par_right)            
            checkExpr(stmt_list)          
        else:
            errorInfo(5)
     
def checkExpr(expr):
    #print("check expr: ", expr)
    expr_set = ['DIGIT_CODE_INT','DIGIT_CODE_FLOAT','VAR_CODE']
    set_split = ['ADDITION_OP', 'SUBTRACTION_OP',
                 'MUTIPLY_OP', 'DIVISION_OP', 'COMPLEMENTATION_OP',
                 'BOOL_STMT_AND', 'BOOL_STMT_OR', 
                 'REL_STMT_LESS', 'REL_STMT_GREATER', 'REL_STMT_GREATEREQUAL', 'REL_STMT_EQUAL']
    ident = 0
    for i in range(len(expr)):
        if expr[i] not in expr_set+set_split:
            errorInfo(8)
        if expr[i] in set_split:
            ident += 1
    #print("id = ", ident)    
    if len(expr) - ident != ident+1:
        errorInfo(8)   
    return 

def checkBlock(block):
    #print("check block: ", block)
    set_bl_left = 'LEFT_BLOCK'
    set_bl_right = 'RIGHT_BLOCK'
    left = 0
    right = 0
    
    for i in range(len(block)):
        if block[i] in set_bl_left:
            left += 1
        if block[i] in set_bl_right:
            right += 1
            
    if left != right:        
        return False
        errorInfo(9)
    else:
        return True

def checkPar(expr): 
    left = 0
    right = 0
    
    for item in expr:       
        if item == 'LEFT_PARENTHSIS':
            left += 1
        if item == 'RIGHT_PARENTHSIS':
            right += 1
    if left != right:
        errorInfo(5)
        return False
    else:
        return True

          
def check_syntactic_error(stmt_list):  
    set_of_type = ['TYPE_INT', 'TYPE_FLOAT', 'TYPE_BOOLEAN']
    set_of_stmt = set_of_type + ['VAR_CODE', 'READ_STAT_KEYWORD', 'WRITE_STAT_KEYWORD', 'IF_STMT_IF', 'WHILE_STMT_WHILE']
    sign_if = True
    sign_while = True
    check = True
    
    if get_keyword(0) in stmt_list:
        errorInfo(0)
        check = False
    
    if(stmt_list[0] in set_of_stmt):
        ##var_dec
        
        if(stmt_list[0] in set_of_type):      
            print('\n',"-----------Var_dec------------ ")          
            if(stmt_list[-1] != 'SEMICOLON'):
                errorInfo(2)
                check = False

            if(stmt_list[1] != 'VAR_CODE'):
                errorInfo(4)
                check = False 
                
        ##assign              
        if(check and stmt_list[0] == 'VAR_CODE'):
            print('\n',"-----------Assign------------ ")
            if(stmt_list[-1] != 'SEMICOLON'):
                errorInfo(2)
                check = False
            if(stmt_list[1] != 'ASSIGN_OP'):
                errorInfo(11)
                check = False              
            else:                  
                expr = stmt_list[2:]
                del expr[-1]
                #print("expr (in assign) = ", expr)
                splitExpr(expr)
                
        ##read_stat 
        if(stmt_list[0] == 'READ_STAT_KEYWORD'):
            print('\n',"-----------Read_Statement-----------")
            if(stmt_list[-1] != 'SEMICOLON'):
                errorInfo(2)
                check = False
            if(stmt_list[1] != 'LEFT_PARENTHSIS'):
                errorInfo(5)
                check = False
            else:
                if(stmt_list[-2] != 'RIGHT_PARENTHSIS'):
                    errorInfo(5)
                    check = False
                else:
                    expr = stmt_list[2:-2]
                    #print("expr(in read) = ", expr)
                    splitExpr(expr)
                    
        ##write_stat 
        if(stmt_list[0] == 'WRITE_STAT_KEYWORD'):
            print('\n',"-----------Write_Statement-----------")
            if(stmt_list[-1] != 'SEMICOLON'):
                errorInfo(2)
                check = False
            if(stmt_list[1] != 'LEFT_PARENTHSIS'):
                errorInfo(5)
                check = False
            else:
                if(stmt_list[-2] != 'RIGHT_PARENTHSIS'):
                        errorInfo(5)
                        check = False
                else:
                    expr = stmt_list[2:-2]
                    #print("expr(in write) = ", expr)
                    splitExpr(expr)
                                            
        #if_stmt
        if(stmt_list[0] == 'IF_STMT_IF'):
            print('\n',"-----------If_Statement-----------")
            
            if(stmt_list[-1] != 'SEMICOLON'):
                sign_if = False
                errorInfo(2)
                check = False
            if(stmt_list[-2] != 'IF_STMT_IF' or stmt_list[-3] != 'END'):
                sign_if = False
                errorInfo(6)
                check = False
            else:
                num_colon = stmt_list.count('COLON')
                # no :
                if( num_colon == 0):
                    sign_if = False
                    errorInfo(12)
                    check = False
                # have :
                else:
                    #have more then 2
                    if(num_colon > 2):
                        sign_if = False
                        errorInfo(3)
                        check = False
                    #only 1 : after else, no : after if
                    if(num_colon == 1):
                        index = stmt_list.index('COLON')
                        if 'IF_STMT_ELSE' in stmt_list:
                            errorInfo(12)
                            check = False
                        else:
                            if(stmt_list[index - 1] == 'IF_STMT_ELSE'):
                                sign_if = False
                                errorInfo(12)
                                check = False
                    #have 2 :
                    if(num_colon == 2):
                        for k in range(len(stmt_list)):
                            if(stmt_list[k] == 'COLON'):
                                index = k
                        ##there are 2 ':'after if, no : after if
                        if(stmt_list[index - 1] != 'IF_STMT_ELSE'):
                            sign_if = False
                            errorInfo(3)
                            check = False
            if sign_if:
                expr = stmt_list[1:stmt_list.index('COLON')] 
                #print("expr(in if) = ", expr)  
                splitExpr(expr)
            #check block                    
                                    
        ##while_stmt
        if(stmt_list[0] == 'WHILE_STMT_WHILE'):
            print('\n',"-----------While_Statement-----------")
            if(stmt_list[-1] != 'SEMICOLON'):
                sign_while = False
                errorInfo(2)
                check = False
            if(stmt_list[-2] != 'WHILE_STMT_WHILE' or stmt_list[-3] != 'END'):                   
                sign_while = False
                errorInfo(7)
                check = False
            else:
                num_do = stmt_list.count('WHILE_STMT_DO')
                if(num_do != 1):
                    sign_while = False
                    errorInfo(7)
                    check = False
            if sign_while:
                expr = stmt_list[1:stmt_list.index('WHILE_STMT_DO')] 
                #print("expr(in while) = ", expr)  
                splitExpr(expr)
                    
                expr_block = stmt_list[stmt_list.index('WHILE_STMT_DO'):stmt_list.index('END')] 
                #print("expr_block(in while_block) = ", expr_block)            
                stmt_while_block = stmtRecogn(token_type)
                check_syntactic_error(stmt_while_block)                              
    else:
        
        errorInfo(1)
        check = False
    
    print('\n', "-----------------------------")
    
    if check:
        print("        NO ERROR FOUND!")

    
line = read_token()
print("str: ", line)

word_list = lexemes(line)
print("lexemes: ", word_list)

#tokens = tokenRecogn(word_list)
tokens = tokenRecogn(line)
print("tokens: ", tokens)

token_type = tokensType(tokens)

showTokensType(tokens, token_type)

block = splitBlock(token_type)
#print("bolck = ", block)

stmtRecogn(block)






