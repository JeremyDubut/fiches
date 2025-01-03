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
    
def main() -> None:

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

    while True:
        add1 = randrange(100,999)
        add2 = randrange(100,999)
        if add1 + add2 > 999:
            continue
        if add1%10 + add2%10 > 9:
            if (add1//10)%10 + (add2//10)%10 > 8:
                continue
            else:
                break
        elif (add1//10)%10 + (add2//10)%10 > 9:
            break

    
    while True:
        sub1 = randrange(100,1000)
        sub2 = randrange(100,1000)
        if sub1 <= sub2:
            continue
        if sub1%10 - sub2%10 < 0:
            if (sub1//10)%10 - (sub2//10)%10 < 1:
                continue
            else:
                break
        elif (sub1//10)%10 - (sub2//10)%10 < 0:
            break

    mul1 = randrange(10,100)
    mul2 = randrange(10,100)

    log.info(f"Generating the tex file")
    fiche_tex(rand_words,rand_n1,rand_n2,args.t,add1,add2,sub1,sub2,mul1,mul2)

    # generate and open the pdf
    # use something safer

    log.info(f"Generating the pdf file")
    os.system("pdflatex fiches/tex/fiche.tex > /dev/null 2>&1")
    
    log.info(f"Cleaning up")
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

