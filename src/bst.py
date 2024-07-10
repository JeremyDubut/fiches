from typing import List
import logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# determinants = ["le ", "la ", "l'", "un ", "une ", "les ", "des ", ""]

class BST:
    
    def __init__(self):
        self.left = None
        self.right = None
        self.det = None
        self.word = None
        self.height = 0

    # def __init__(
    #     self, 
    #     det:str, 
    #     word:str):

    #     self.left = __init__()
    #     self.right = __init__()
    #     # for det in determinants:
    #     #     if key.startswith(det):
    #     self.det = det
    #     self.word = key[len(det):]
    #             # break

    def insert(
        self,
        det:str,
        word:str):

        if not self.word:
            self.det = det
            self.word = word
            self.left = BST()
            self.right = BST()
            self.height = 1
        elif self.word == word:
            if self.det == "":
                self.det = det
        elif self.word > word:
            self.left.insert(det,word)
            self.height = max(self.left.height,self.right.height)+1
        else:
            self.right.insert(det,word)
            self.height = max(self.left.height,self.right.height)+1

    def traversal(self) -> List[str]:

        if self.word:
            return self.left.traversal()+[self.det+self.word]+self.right.traversal()
        else:
            return list([])



        