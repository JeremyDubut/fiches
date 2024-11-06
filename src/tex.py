from typing import List
import logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def fiche_tex(
    words: List[str],
    numbers1: List[int],
    numbers2: List[int],
    size_tashizan: int,
    num_add: List[list],
    num_sub: List[list],
    story: str =""
) -> ():

    # open the tex file
    f = open("fiches/tex/fiche.tex", "w")

    # write the header
    f.write("\\input{fiches/tex/header.tex}\n\n")
    f.write("\\begin{document}\n\n")

    # write the writing exercise
    writing_tex(f,words)

    # some padding
    f.write("\\vspace{1cm}\large\n")
    f.write("~\\\\\n\n")

    # write the tashizan exercises
    f.write("\\begin{center}\n")
    tashizan_tex(f,numbers1,numbers2,size_tashizan)
    f.write("\n\\end{center}~\\\\\n")
    f.write("\n\\begin{center}\n")
    big_tashizan_tex(f,num_add)
    big_hikizan_tex(f,num_sub)
    f.write("\n\\end{center}")

    # some padding
    f.write("\n\n~\\\\\n\n")

    # write a story
    f.write("{\\fontfamily{phv}\\selectfont\n")
    f.write(story+"\n}")

    # finish the file
    f.write("\n\n\\end{document}")

    # close the file
    f.close()

def writing_tex(
    f,
    words: List[str]
) -> ():

    # create the lines
    for w in words:
        f.write("\\writing{"+w[:-1]+"}\n")


closer = "\n\t\\hline\n"

def tashizan_tex(
    f,
    numbers1: List[int],
    numbers2: List[int],
    stashi: int
) -> ():

    # begin the table
    header = "\\begin{CJK}{UTF8}{min}\n\\begin{tabular}{|"
    for i in range(stashi+1):
        header = header+"q|"
    header = header+"}\n"
    f.write(header)

    # Japanese header
    jph = "\t\\cline{1-3}\n\t\\multicolumn{3}{|c|}{掛算\\pgfmathparse{int("
    jph = jph+str(stashi)+"*"+str(stashi)+")}\\pgfmathresultマス} \\\\\n"
    f.write(jph+closer)

    # first line
    fl = "\t$\\times$ "
    for k in numbers1:
        fl = fl + "& " + str(k) + " "
    fl = fl + "\\\\" + closer
    f.write(fl)

    # other lines
    li = "\t"
    for j in numbers2:
        li = li + str(j) + " "
        for l in range(stashi):
            li = li + "&   "
        li = li + "\\\\" + closer
    f.write(li)

    # close the table
    f.write("\\end{tabular}\n\\end{CJK}")


def big_tashizan_tex(
    f,
    num_add: List[list]
) -> ():

    for nums in num_add:
        f.write("\\qquad")
        f.write("\\begin{tabular}{ccc}\n")
        f.write("\t& "+str(nums[0][0])+" & "+str(nums[0][1])+"\\\\\n")
        f.write("\t $+$ & "+str(nums[1][0])+" & "+str(nums[1][1])+"\\\\\n")
        f.write("\t\\hline\n")
        f.write("\t & & \\\\\n")
        f.write("\\end{tabular}\n")
    f.write("\\qquad\\qquad")

def big_hikizan_tex(
    f,
    num_sub: List[list]
) -> ():

    for nums in num_sub:
        # f.write("\\qquad\\qquad")
        f.write("\\begin{tabular}{ccc}\n")
        f.write("\t& "+str(nums[0][0])+" & "+str(nums[0][1])+"\\\\\n")
        f.write("\t $-$ & "+str(nums[1][0])+" & "+str(nums[1][1])+"\\\\\n")
        f.write("\t\\hline\n")
        f.write("\t & & \\\\\n")
        f.write("\\end{tabular}\n")
        f.write("\\qquad")