from typing import List
from math import log2, floor
import pickle as pkl
import logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

from fiches.src.bst import BST

determinants = ["le ", "la ", "l'", "un ", "une ", "du ", "les ", "des ", "il ", "elle ", "ma ", ""]

def decompose_det(word:str) -> tuple[str,str]:

    for det in determinants:
        if word.startswith(det):
            return (det,word[len(det):])

def load_list() -> List[str]:

    wl = open("fiches/words/wl.pkl","rb")
    word_list = pkl.load(wl)
    wl.close()

    return word_list

def reset_list(
    file: str
) -> List[str]:

    f = open(file,"r")
    try:
        p = open("fiches/words/bst.pkl","rb")
        bst = pkl.load(p)
        p.close
    except FileNotFoundError:
        bst = BST()

    for word in f:
        det, wo = decompose_det(word)
        bst.insert(det,wo)

    p = open("fiches/words/bst.pkl","wb")
    pkl.dump(bst, p)
    p.close()

    word_list = bst.traversal()
    wl = open("fiches/words/wl.pkl","wb")
    pkl.dump(word_list,wl)
    wl.close()

    log.debug(f"Height of the BST: {bst.height}, optimal height: {1+floor(log2(len(word_list)))}")

    return word_list
