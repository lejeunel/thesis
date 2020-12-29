# LaTeX Makefile v0.33 -- LaTeX only

THESIS=main
CV=cv
OUTPUT=thesis_cv.pdf
SHELL=/bin/zsh

all:  ## Compile paper
	./latexrun $(THESIS).tex
	./latexrun $(CV).tex
	pdfunite $(THESIS).pdf $(CV).pdf $(OUTPUT)


clean:  ## Clean output files
	./latexrun --clean-all
