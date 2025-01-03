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
    add1: int,
    add2: int,
    sub1: int,
    sub2: int,
    mul1: int,
    mul2: int,
    story: str =""
) -> None:

    # open the tex file
    f = open("fiches/tex/fiche.tex", "w")

    # write the header
    f.write("\\input{fiches/tex/header.tex}\n\n")
    f.write("\\begin{document}\n\n")

    # write the writing exercise
    writing_tex(f,words)

    # some padding
    f.write("\\vspace{1cm}\large\n")
    f.write("~\\\n\n")

    # write the tashizan exercises
    f.write("\\begin{center}\n")
    table_op_tex(f,numbers1,numbers2,size_tashizan)
    f.write("\n\\end{center}~\\\\\n")
    f.write("\n\\begin{center}\n")
    big_op_tex(f,add1,add2,3,"+")
    big_op_tex(f,sub1,sub2,3,"-")
    big_op_tex(f,mul1,mul2,2,"\\times")
    f.write("\n\\end{center}")

    # some padding
    # f.write("\n\n~\\\n\n")

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
) -> None:

    # create the lines
    for w in words:
        f.write("\\writing{"+w[:-1]+"}\n")


closer = "\n\t\\hline\n"

def table_op_tex(
    f,
    numbers1: List[int],
    numbers2: List[int],
    stashi: int
) -> None:

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


def big_op_tex(
    f,
    num1: int,
    num2: int,
    log: int,
    op: str
) -> None:

    f.write("\\qquad")
    f.write("\\begin{tabular}{")
    for _ in range(log+1):
        f.write("c")
    f.write("}\n")
    line = ""
    mem = num1
    for _ in range(log):
        line = "& "+str(mem%10)+line
        mem = mem//10
    f.write("\t"+line+"\\\\\n")
    line = ""
    mem = num2
    for _ in range(log):
        line = "& "+str(mem%10)+line
        mem = mem//10
    f.write("$"+op+"$"+line+"\\\\\n")
    f.write("\t\\hline\n")
    f.write("\t & & \\\\\n")
    f.write("\\end{tabular}\n")
    f.write("\\qquad\\qquad")