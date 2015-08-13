STATIC = '../pdf'

rule cv:
    input:   'cv.tex',
             'publications.bib'
    output:  STATIC + '/cv.pdf'
    run:
        prefix = list(input)[0].split('.')[0]
        pdfCmd = 'pdflatex -output-directory=%s -output-format=pdf %s' % (STATIC, prefix)
        latexCmd = 'latex %s' % (prefix, )
        bibtexCmd = 'bibtex %s' % (prefix, )
        
        shell(latexCmd)
        shell(bibtexCmd)
        shell(latexCmd)
        shell(latexCmd)
        shell(pdfCmd)
