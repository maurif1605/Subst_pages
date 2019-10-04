import sys
from FIFO import *
from OTM import *
from LRU import *


def main():
    
    qtd_quadros = int(sys.stdin.readline())

    referencias = map(int, sys.stdin.readlines())

    
    FIFO = FIFO()
    
    PF_fifo = FIFO.execute(qtd_quadros, referencias)

    
    OTM = OTM()
    
    PF_otm = OTM.execute(qtd_quadros, referencias)

    
    LRU = LRU()
    
    PF_lru = LRU.execute(qtd_quadros, referencias)

   
    saida = 'FIFO {0}\nOTM {1}\nLRU {2}'

    
    print(saida.format(PF_fifo, PF_otm, PF_lru))



if __name__ == "__main__":
    main()
