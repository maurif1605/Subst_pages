class FIFO:
    

    def execute(self, qtd_quadros, referencias):
        
        PageFault = 0 

        quadros = [] 

        
        for ref in referencias:
            if ref not in quadros:
                PageFault += 1 
                
                if len(quadros) == qtd_quadros:
                    quadros.pop(0)

                
                quadros.append(ref)

        
        return PageFault
