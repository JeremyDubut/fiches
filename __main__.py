import argparse
import os
from random import sample, randrange
import logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

from fiches.src.tex import fiche_tex
from fiches.src.list import reset_list, load_list
    
def main() -> ():

    # Parsing arguments
    args = parse_command_line_arguments()

    # reset the list if needed, otherwise load it
    if args.r:
        word_list = reset_list("fiches/words/liste.txt")
    else:
        word_list = load_list()
    log.info(f"{args.w} words taken from a list of size {len(word_list)}")

    # generate the tex file

    random_indices = sample(range(0,len(word_list)),args.w)
    rand_words = [word_list[i] for i in random_indices]
    rand_n1 = sample(range(2,10),args.t)
    rand_n2 = sample(range(3,10),args.t)
    swap = randrange(0,2)
    rand_add = [[[0,0],[0,0]],[[0,0],[0,0]]]
    rand_add[swap][0][1] = randrange(0,10)
    rand_add[swap][1][1] = randrange(0,10-rand_add[swap][0][1])
    rand_add[swap][0][0] = randrange(1,9)
    rand_add[swap][1][0] = randrange(1,10-rand_add[swap][0][0])
    rand_add[1-swap][0][1] = randrange(1,10)
    rand_add[1-swap][1][1] = randrange(10-rand_add[1-swap][0][1],10)
    rand_add[1-swap][0][0] = randrange(1,8)
    rand_add[1-swap][1][0] = randrange(1,9-rand_add[1-swap][0][0])
    stories = os.listdir("fiches/stories/")
    random_story = randrange(0,len(stories))
    st = open("fiches/stories/"+stories[random_story],"r")
    story = st.readline()
    st.close()
    # log.debug(f"One story randomly chosen among {stories}")
    fiche_tex(rand_words,rand_n1,rand_n2,args.t,story,rand_add)

    # generate and open the pdf
    # use something safer

    os.system("pdflatex fiches/tex/fiche.tex > /dev/null 2>&1")
    os.system("rm fiche.aux")
    os.system("rm fiche.log")
    os.system("mv fiche.pdf fiches/tex/fiche.pdf")
    os.system("open fiches/tex/fiche.pdf")

    # clean up files



    
def parse_command_line_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog="code",
    )
    parser.add_argument(
        "-w",
        default=8,
        help=(
            "number of words to write"
        ),
        type=int,
    )
    parser.add_argument(
        "-t",
        default=5,
        help=(
            "size of the tashizan table"
        ),
        type=int,
    )
    parser.add_argument(
        "-r",
        help=(
            "Reset the list of words"
        ),
        action=argparse.BooleanOptionalAction
    )

    return parser.parse_args()



if __name__ == "__main__":
    main()

