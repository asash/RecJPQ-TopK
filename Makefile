cmpile:
	pdflatex --shell-escape -synctex=1 -interaction=nonstopmode main
	bibtex main
	pdflatex --shell-escape -synctex=1 -interaction=nonstopmode main

stoponbug:
	pdflatex --shell-escape -synctex=1 main


arxiv_submission: 
	rm -rf arxiv
	rm -rf arxiv_arXiv
	rm -rf arxiv.tar.gz
	mkdir arxiv
	cp -r figures/ arxiv/figures 
	cp -r data/ arxiv/data 
	cp main.bbl arxiv
	cp *.tex arxiv
	cp references.bib arxiv/
	arxiv_latex_cleaner arxiv
	cp arxiv_arXiv/*.tex arxiv
	cp chato-notes.sty arxiv
	tar cvvzf arxiv.tar.gz arxiv/

submission: 
	rm -rf Source
	rm -rf Source_arXiv
	rm -rf Suppliments
	rm -rf pdf
	rm -rf recsys24-167.zip
	mkdir Source
	mkdir Suppliments
	mkdir pdf
	cp -r figures/ Source/figures 
	cp -r data/ Source/data 
	cp main.bbl Source
	cp *.tex Source
	cp references.bib Source/
	arxiv_latex_cleaner Source/
	cp main.pdf pdf
	arxiv_latex_cleaner Source
	cp Source_arXiv/*.tex Source
	cp chato-notes.sty Source
	zip -r recsys24-167.zip  Source/* pdf/* Suppliments*


clean:
	rm -rf Source
	rm -rf Source_arXiv
	rm -rf Suppliments
	rm -rf pdf
	rm -rf arxiv
	rm -rf arxiv_arXiv
	rm -rf main.fdb_latexmk
	rm -rf main.fls
	rm -rf arxiv.tar.gz
	rm -rf recsys24-167.zip
	rm -rf main.aux
	rm -rf main.bbl
	rm -rf main.blg
	rm -rf main.log
	rm -rf main.out
	rm -rf main.pdf
	rm -rf main.synctex.gz
