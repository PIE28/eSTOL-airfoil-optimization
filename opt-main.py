class Variable(object):
    
    def __init__(self, name="no_name", init_value=None):
        self.name = name
        self.value = init_value
        if(init_value==None): self.computed = False
        else: self.computed = True
    
    def get_value(self):
        return(self.value)
        
    def set_value(self, value):
        self.computed = True
        self.value=value
        
    
    
class Block(object):
    
    def __init__(self, L_B, name="no_name", INPUTS=[], OUTPUTS=[], compute_function=None):
        self.name = name
        self.INPUTS=INPUTS
        self.OUTPUTS=OUTPUTS
        self.computed = False
        self.compute_function = compute_function
        self.LIST_BLOCKS = L_B
        self.LIST_BLOCKS.append(self)
    
    def is_block_computable(self):
        check=True
        for inp in self.INPUTS:
            if inp.computed == False:
                check=False
        return(check)
    
    def compute_block(self):
        if(self.is_block_computable()==True):
            self.compute_function()
        else:
            print(self.name+" is not computable")

LIST_BLOCKS = []

v1=Variable("v1",7)
v2=Variable("v2",6)
o1=Variable("v3", None)

def funct_calcul_1():
    v=v1.get_value()+v2.get_value()
    o1.set_value(v)
b1=Block(LIST_BLOCKS, "block test", [v1,v2],[o1],funct_calcul_1)


for BLOCK in LIST_BLOCKS:
    BLOCK.compute_block()



print(o1.get_value())

